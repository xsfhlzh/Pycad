using System.Reflection;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{

    internal class Param : Variable
    {

        public Param() { }

        public Param(ParameterInfo par) 
            : base(Checkname(par.Name), par.ParameterType) { }

        public override string ToString()
        {
            return $"{Name}: {TypeIndex.Fullname}";
        }
    }
}
