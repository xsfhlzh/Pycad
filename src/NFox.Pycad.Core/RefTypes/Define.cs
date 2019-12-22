using System.Collections.Generic;
using System.Reflection;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using System.Runtime.CompilerServices;
using System.IO;

namespace NFox.Pycad.RefTypes
{
    internal class Define : Variable
    {

        public ItemList<Param> Params { get; private set; }  = new ItemList<Param>();

        public bool IsStatic { get; private set; }

        public bool IsExtension { get; protected set; }

        public string DeclaringType { get; protected set; }

        public Define() { }

        public Define(MethodInfo method, string name = null)
            : base(name ?? method.Name, method.ReturnType)
        {
            IsStatic = method.IsStatic;
            var pars = method.GetParameters();
            foreach (var p in pars)
                Params.Add(new Param(p));
            if (IsStatic && method.IsDefined(typeof(ExtensionAttribute)))
            {
                var type = TypeIndex.FromSystemType(pars[0].ParameterType);
                var ns = Namespace.FromString(type.Namespace);
                var etype = ns.GetExtype(type.Name, true);
                Method emethod = null;
                if (etype.Methods.ContainsKey(Name))
                {
                    emethod = etype.Methods[Name];
                }
                else
                {
                    emethod = new Method(Name);
                    etype.Methods.Add(emethod);
                }

                var define =
                    new Define
                    {
                        Name = Name,
                        TypeIndex = TypeIndex.FromSystemType(method.ReturnType),
                        IsExtension = true,
                        DeclaringType = method.DeclaringType.FullName,
                    };

                for (int i = 1; i < pars.Length; i++)
                    define.Params.Add(new Param(pars[i]));
                emethod.AddDefine(define);


            }
        }
     
        public Define(ConstructorInfo method)
            : base("__init__", method.DeclaringType)
        {
            foreach (var pi in method.GetParameters())
                Params.Add(new Param(pi));
        }

        public override void Desc(StreamWriter sw, int space)
        {

            var pre = GetPrefixSpace(space);
            string pars = string.Join(", ", Params.Select(p => p.ToString()));
            if (IsStatic)
                sw.WriteLine($"{pre}@staticmethod");
            else if (Params.Count > 0)
                pars = "self, " + pars;
            else
                pars = "self";

            if(Name == "__init__")
                sw.Write($"{pre}def {Name}({pars}) -> {TypeIndex.Name}:");
            else if(TypeIndex.Equals(TypeIndex.None))
                sw.Write($"{pre}def {Name}({pars}):");
            else
                sw.Write($"{pre}def {Name}({pars}) -> {TypeIndex.Fullname}:");

            if (IsExtension)
            {
                sw.WriteLine();
                sw.WriteLine($"{pre}    \"\"\"Extension from: {DeclaringType}\"\"\"");
            }
            else
            {
                sw.WriteLine("...");
            }
        }

        public override void FromXml(XElement xe)
        {
            TypeIndex = Parse<TypeIndex>(xe.Element("TypeIndex"));
            if(xe.Attribute("IsStatic") != null)
                IsStatic = true;
            DeclaringType = xe.Attribute("DeclaringType")?.Value;
            IsExtension = DeclaringType != null;
            foreach (var e in xe.Elements("Param"))
                Params.Add(Parse<Param>(e));
        }

        public override XElement ToXml()
        {
            var xe =
                new XElement("Define", TypeIndex.ToXml());
            if(IsStatic)
                xe.Add(new XAttribute("IsStatic", IsStatic));
            if(IsExtension)
                xe.Add(new XAttribute("DeclaringType", DeclaringType));
            foreach (var par in Params)
                xe.Add(par.ToXml());
            return xe;
        }


    }
}
