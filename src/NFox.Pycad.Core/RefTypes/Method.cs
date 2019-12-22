using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{
    internal class Method : Variable
    {

        public ItemList<Define> Defines { get; } = new ItemList<Define>();

        public Method() { }

        public Method(string name)
            : base(name)
        { }

        public Method(IEnumerable<ConstructorInfo> methods)
            : base("__init__")
        {
            foreach (var method in methods)
                AddDefine(new Define(method));
        }

        public Method(IGrouping<string, MethodInfo> methods)
            : base(methods.Key)
        {
            var defines = methods.Select(m => new Define(m));
            var num = defines.Count();
            var sdefines = defines.Where(d => d.IsStatic);
            var snum = sdefines.Count();
            if (num != snum && snum != 0)
                defines = defines.Except(sdefines);
            foreach (var define in defines)
                AddDefine(define);
        }

        public override void FromXml(XElement xe)
        {
            Name = xe.Attribute("Name").Value;
            foreach (var e in xe.Elements("Define"))
                AddDefine(Parse<Define>(e, Name));
        }

        public void AddDefine(Define define)
        {
            int i = 0;
            int num = define.Params.Count;
            foreach(var cdefine in Defines.Where(d => d.Params.Count == num))
            {
                bool b = true;
                for (int j = 0; j < num; j++)
                {
                    if (!define.Params[j].TypeIndex.Equals(cdefine.Params[j].TypeIndex))
                    {
                        b = false;
                        break;
                    }
                }
                //找到定义相同的扩展就直接退出
                if (b) return;
            }
            Defines.Insert(i, define);
        }

        public override XElement ToXml()
        {
            var xe = 
                new XElement("Method", 
                    new XAttribute("Name", Name));
            foreach (var define in Defines)
                xe.Add(define.ToXml());
            return xe;
        }



    }
}
