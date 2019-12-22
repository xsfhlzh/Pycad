using System.IO;
using System.Reflection;
using System.Text;

namespace NFox.Pycad.RefTypes
{
    class Field : Variable
    {

        public Field() { }

        public Field(FieldInfo field, System.Type type = null) 
            : base(field.Name, type ?? field.FieldType) { }

        public override void Desc(StreamWriter sw, int space)
        {
            var pre = GetPrefixSpace(space);
            sw.WriteLine($"{pre}{Checkname(Name)}: {TypeIndex.Fullname}");
        }

    }
}
