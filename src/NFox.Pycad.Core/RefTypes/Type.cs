using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{
    internal class Type : TypeIndex
    {

        public Type Owner { get; private set; }

        public ItemDictionary<Field> Fields { get; } = new ItemDictionary<Field>();
        public ItemDictionary<Property> Properties { get; } = new ItemDictionary<Property>();
        public ItemDictionary<Event> Events { get; } = new ItemDictionary<Event>();
        public ItemDictionary<Method> Methods { get; } = new ItemDictionary<Method>();
        public ItemDictionary<Type> Types { get; } = new ItemDictionary<Type>();
        public ItemList<TypeIndex> BaseTypes { get; } = new ItemList<TypeIndex>();

        #region Constructor

        public Type() { }

        private readonly System.Type _type_int = typeof(int);

        public Type(Namespace @namespace, Type owner, string name)
        {
            Owner = owner;
            Name = name;
            Namespace = @namespace.Fullname;
        }

        public Type(System.Type type)
        {

            if (type.FullName == "System.Array")
            {
                Namespace = "System";
                Name = "Array";
                Kind = TypeIndexKind.GenericDefinition;
                GenericParams.Add(new TypeIndex("T", TypeIndexKind.GenericParam));
            }
            else
            {
                var ti = FromSystemType(type);
                if (string.IsNullOrEmpty(ti.Namespace)) return;
                Namespace = ti.Namespace;
                Name = ti.Name;
                Kind = ti.Kind;
                GenericParams = ti.GenericParams;
            }

            var ns = GetNamespace();
            if (type.IsNested)
            {
                var names = Name.Split('.');
                var ptype = ns.Types[names[0]];
                int i = 1;
                for(; i < names.Length - 1; i++)
                    ptype = ptype.Types[names[i]];
                Owner = ptype;
                Name = names[i];
                if (ptype.Types.ContainsKey(Name))
                {
                    if (ptype.Types[Name].Kind == TypeIndexKind.General)
                        ptype.Types.Remove(Name);
                    else
                        return;
                }
                ptype.Types.Add(this);
            }
            else
            {

                if (ns.Types.ContainsKey(Name))
                {
                    if (ns.Types[Name].Kind == TypeIndexKind.General)
                        ns.Types.Remove(Name);
                    else
                        return;
                }
                ns.Types.Add(this);
            }

            if (type.BaseType != null)
                BaseTypes.Add(FromSystemType(type.BaseType));

            var itypes = type.GetInterfaces().ToList();
            for (int i = itypes.Count - 1; i >= 0; i--)
            {
                for (int j = 0; j < i; j++)
                {
                    if (itypes[i].IsAssignableFrom(itypes[j]))
                    {
                        itypes.RemoveAt(i);
                        break;
                    }
                }
            }

            foreach (var it in itypes)
                BaseTypes.Add(FromSystemType(it));

            foreach (var field in type.GetFields())
                Fields.Add(new Field(field, _type_int));

            if (!type.IsEnum)
            {

                foreach (var field in type.GetFields())
                    Fields.Add(new Field(field));

                foreach (var property in type.GetProperties())
                    Properties.Add(new Property(property));

                foreach (var @event in type.GetEvents())
                    Events.Add(new Event(@event));

                var inits = type.GetConstructors().Where(m => !m.IsStatic);
                Methods.Add(new Method(inits));

                //去除基类已定义的函数
                var imethodnames =
                    type.GetInterfaces()
                    .SelectMany(t => t.GetMethods())
                    .Select(m => m.Name)
                    .Distinct();
                var methodnames =
                    Properties.SelectMany(p => p.Value.Methodnames)
                    .Union(Events.SelectMany(e => e.Value.Methodnames))
                    .Union(imethodnames);
                if(type.BaseType != null)
                {
                    var bmethodnames =
                        type.BaseType
                        .GetMethods()
                        .Select(m => m.Name)
                        .Distinct();
                    methodnames = methodnames.Union(bmethodnames);
                }
                var methods =
                    type.GetMethods()
                    .Where(m => !(m.IsStatic && m.Name.StartsWith("op_")) && !m.Name.Contains("."))
                    .GroupBy(m => m.Name)
                    .Where(g => !methodnames.Contains(g.Key));

                foreach (var g in methods)
                    Methods.Add(new Method(g));

                if (Kind == TypeIndexKind.GenericDefinition)
                {
                    var bti = new TypeIndex("typing", "Generic", TypeIndexKind.GenericDefinition);
                    foreach(var p in GenericParams)
                        bti.GenericParams.Add(p);
                    BaseTypes.Add(bti);
                }

                var prop = Properties.Select(p => p.Value).FirstOrDefault(p => p.IsIndex);
                if (prop != null)
                {
                    var bti = new TypeIndex("typing", "Iterable", TypeIndexKind.GenericDefinition);
                    bti.GenericParams.Add(prop.TypeIndex);
                    BaseTypes.Add(bti);
                }
                else if(type.FullName == "System.Array")
                {
                    var bti = new TypeIndex("typing", "Iterable", TypeIndexKind.GenericDefinition);
                    bti.GenericParams.Add(new TypeIndex("T", TypeIndexKind.GenericParam));
                    BaseTypes.Add(bti);
                }

                if (BaseTypes.Count > 1 && BaseTypes[0].Equals(Object))
                    BaseTypes.RemoveAt(0);

                //去除基类已定义的事件
                var eventnames =
                    type.GetInterfaces()
                    .SelectMany(i => i.GetEvents())
                    .Select(e => e.Name);
                if (type.BaseType != null)
                {
                    eventnames =
                        type.BaseType
                        .GetEvents()
                        .Select(e => e.Name)
                        .Union(eventnames);
                }
                foreach (var name in eventnames.Distinct())
                    Events.Remove(name);

                //去除基类已定义的属性
                var propnames =
                    type.GetInterfaces()
                    .SelectMany(i => i.GetProperties())
                    .Select(p => p.Name);
                if (type.BaseType != null)
                {
                    propnames =
                        type.BaseType
                        .GetProperties()
                        .Select(p => p.Name)
                        .Union(propnames);
                }
                foreach(var name in propnames.Distinct())
                    Properties.Remove(name);

            }

        }


        #endregion

        #region LoadAndSave

        public override void Desc(StreamWriter sw, int space)
        {

            var pre = GetPrefixSpace(space);

            var btypes = BaseTypes.Select(t => t.Fullname).ToList();
            sw.WriteLine($"{pre}class {Name}({string.Join(", ", btypes)}):");

            IEnumerable<string> names = Methods.Keys;
            var definess = Methods.SelectMany(m => m.Value.Defines);
            var extmethods = RefTypes.Namespace.FromString(Namespace).GetExtype(Name)?.Methods;
            if (extmethods != null)
                definess = definess.Union(extmethods.SelectMany(m => m.Value.Defines));
            if (Fields.Count == 0 && Events.Count == 0 && Properties.Count == 0 && definess.Count() == 0)
            {
                sw.WriteLine($"{pre}    pass");
            }
            else
            {

                space += 4;
                foreach (var field in Fields)
                    field.Value.Desc(sw, space);
                foreach (var property in Properties)
                    property.Value.Desc(sw, space);
                foreach (var @event in Events)
                    @event.Value.Desc(sw, space);

                foreach (var defines in definess.GroupBy(d => d.Name))
                {
                    foreach (var define in defines)
                        define.Desc(sw, space);
                }

                foreach (var type in Types)
                    type.Value.Desc(sw, space);
            }
        }

        public override void FromXml(XElement xe)
        {
            base.FromXml(xe);
            foreach (var e in xe.Elements("TypeIndex"))
            {
                var bti = Parse<TypeIndex>(e);
                BaseTypes.Add(bti);
            }
            foreach (var e in xe.Elements("Field"))
                Fields.Add(Parse<Field>(e));
            foreach (var e in xe.Elements("Event"))
                Events.Add(Parse<Event>(e));
            foreach (var e in xe.Elements("Property"))
                Properties.Add(Parse<Property>(e));
            foreach (var e in xe.Elements("Method"))
                Methods.Add(Parse<Method>(e));
            foreach (var e in xe.Elements("Type"))
            {
                var type = Parse<Type>(e);
                type.Owner = this;
                Types.Add(Parse<Type>(e));
            }
        }

        public override XElement ToXml()
        {
            XElement xe = base.ToXml();
            xe.Attribute("Namespace").Remove();
            foreach (var ti in BaseTypes)
                xe.Add(ti.ToXml());
            foreach (var field in Fields)
                xe.Add(field.Value.ToXml());
            foreach (var @event in Events)
                xe.Add(@event.Value.ToXml());
            foreach (var property in Properties)
                xe.Add(property.Value.ToXml());
            foreach (var method in Methods)
                xe.Add(method.Value.ToXml());
            foreach (var type in Types)
                xe.Add(type.Value.ToXml());
            return xe;
        }

        #endregion

        public Namespace GetNamespace()
        {
            return RefTypes.Namespace.FromString(Namespace);
        }

        public override string ToString()
        {
            return $"{Namespace}.{Name}";
        }

    }
}
