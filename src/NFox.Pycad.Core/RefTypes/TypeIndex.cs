
using System;
using System.Linq;
using System.Collections.Generic;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{

    internal enum TypeIndexKind
    {
        General,
        System,
        GenericType,
        GenericDefinition,
        GenericParam
    }

    internal class TypeIndex : Item, IEquatable<TypeIndex>
    {

        public readonly static TypeIndex None
           = new TypeIndex("None");
        public readonly static TypeIndex Object
            = new TypeIndex("object");
        public readonly static TypeIndex Bool
            = new TypeIndex("bool");
        public readonly static TypeIndex Int
            = new TypeIndex("int");
        public readonly static TypeIndex Float
            = new TypeIndex("float");
        public readonly static TypeIndex String
            = new TypeIndex("str");

        private static Dictionary<string, TypeIndex> _types =
            new Dictionary<string, TypeIndex>
            {
                { "System.Void", None },
                { "System.None", None },
                { "System.Object", Object },
                { "System.Boolean", Bool },
                { "System.Int16", Int },
                { "System.Int32", Int },
                { "System.Int64", Int },
                { "System.Single", Float },
                { "System.Double", Float },
                { "System.String", String },
            };

        public List<TypeIndex> GenericParams { get; protected set; } = new List<TypeIndex>();

        public TypeIndexKind Kind { get; protected set; }

        public string Namespace { get; set; }

        public string Fullname
        {
            get
            {
                switch (Kind)
                {
                    case TypeIndexKind.System:
                        return Name;
                    case TypeIndexKind.GenericParam:
                        if (RefTypes.Namespace.CurrType.GenericParams.Select(p => p.Name).Contains(Name))
                            return Name;
                        else
                            return "typing.Any";
                    case TypeIndexKind.GenericDefinition:
                    case TypeIndexKind.GenericType:
                        string names = string.Join(", ", GenericParams.Select(t => t.Fullname));
                        return $"{Alias}[{names}]";
                    default:
                        return Alias;
                }
            }
        }

        private string Alias
        {
            get
            {
                var ns = RefTypes.Namespace.Curr;
                if (Namespace == ns.Fullname)
                {
                    return Name;
                }
                else if(Namespace == "typing")
                {
                    return $"typing.{Name}";
                }
                else
                {
                    var nindex = ns.Imports.IndexOfKey(Namespace);
                    var names = Name.Split(new char[] { '.' }, 2);
                    var mindex = ns.Imports[Namespace].IndexOf(names[0]);
                    if (names.Length == 1)
                        return $"_n_{nindex}_t_{mindex}";
                    return $"_n_{nindex}_t_{mindex}{names[1]}";
                }
            }
        }

        public TypeIndex() { }

        public TypeIndex(string name, TypeIndexKind kind = TypeIndexKind.System)
        {
            Namespace = "";
            Name = name;
            Kind = kind;
        }

        public TypeIndex(string @namespace, string name, TypeIndexKind kind = TypeIndexKind.General)
        {
            Namespace = @namespace ?? "";
            Name = name;
            Kind = kind;
        }

        public override void FromXml(XElement xe)
        {
            base.FromXml(xe);
            Namespace = xe.Attribute("Namespace")?.Value ?? "";
            Kind = (TypeIndexKind)Enum.Parse(typeof(TypeIndexKind), xe.Attribute("Kind").Value);
            switch (Kind)
            {
                case TypeIndexKind.GenericDefinition:
                    foreach (var name in xe.Attribute("Params").Value.Split(','))
                        GenericParams.Add(new TypeIndex(name, TypeIndexKind.GenericParam));
                    break;
                case TypeIndexKind.GenericType:
                    foreach (var e in xe.Elements("TypeIndex"))
                        GenericParams.Add(Parse<TypeIndex>(e));
                    break;
            }
        }

        public override XElement ToXml()
        {
            var xe = base.ToXml();
            xe.Add(new XAttribute("Namespace", Namespace));
            xe.Add(new XAttribute("Kind", Kind));
            switch (Kind)
            {
                case TypeIndexKind.GenericDefinition:
                    var names = GenericParams.Select(p => p.Name);
                    xe.Add(new XAttribute("Params", string.Join(",", names)));
                    break;
                case TypeIndexKind.GenericType:
                    foreach (var par in GenericParams)
                        xe.Add(par.ToXml());
                    break;
            }
            return xe;
        }

        public static TypeIndex FromSystemType(System.Type type)
        {

            if (string.IsNullOrEmpty(type.Namespace))
            {
                return Object;
            }
            else if (type.IsByRef)
            {
                try
                {
                    string tname = type.FullName.Substring(0, type.FullName.Length - 1);
                    return FromSystemType(type.Assembly.GetType(tname));
                }
                catch { }
                return Object;
            }
            else if (type.IsArray)
            {
                var ti = FromSystemType(typeof(Array));
                ti.Kind = TypeIndexKind.GenericType;
                ti.GenericParams.Add(FromSystemType(type.GetElementType()));
                return ti;
            }
            else if (type.IsGenericParameter)
            {
                return new TypeIndex(type.Name, TypeIndexKind.GenericParam);
            }
            else if (type.IsNested)
            {
                var ti = FromSystemType(type.DeclaringType);
                ti.Name += "." + type.Name;
                if (type.IsGenericTypeDefinition && ti.Name.Contains("`"))
                {
                    ti.Name = ti.Name.Substring(0, type.Name.IndexOf('`'));
                    foreach (var t in type.GetGenericParameterConstraints())
                        ti.GenericParams.Add(FromSystemType(t));
                    ti.Kind = TypeIndexKind.GenericDefinition;
                }
                return ti;
            }
            else if (type.IsGenericTypeDefinition)
            {
                var ti =
                    new TypeIndex(
                        type.Namespace,
                        type.Name.Substring(0, type.Name.IndexOf('`')));
                foreach (var t in type.GetGenericArguments())
                {
                    var pti = new TypeIndex(t.Name, TypeIndexKind.GenericParam);
                    ti.GenericParams.Add(pti);
                }
                ti.Kind = TypeIndexKind.GenericDefinition; ;
                return ti;
            }
            else if (type.IsGenericType)
            {
                var gtype = type.GetGenericTypeDefinition();
                var ti = FromSystemType(gtype);
                ti.GenericParams.Clear();
                foreach (var t in type.GenericTypeArguments)
                    ti.GenericParams.Add(FromSystemType(t));
                ti.Kind = TypeIndexKind.GenericType;
                return ti;
            }
            else
            {
                string name = type.FullName;
                if (_types.ContainsKey(name))
                    return _types[name];
                if (type.Namespace != null && name.StartsWith(type.Namespace))
                    name = name.Substring(type.Namespace.Length + 1);
                name = name.Replace("*", "");
                return new TypeIndex(type.Namespace, name);
            }

        }

        public bool Equals(TypeIndex other)
        {

            if (Kind == other.Kind)
            {
                switch (Kind)
                {
                    case TypeIndexKind.System:
                    case TypeIndexKind.GenericParam:
                        return Name == other.Name;
                    default:
                        return Namespace == other.Namespace && Name == other.Name;
                }
            }
            return false;
        }


    }
}