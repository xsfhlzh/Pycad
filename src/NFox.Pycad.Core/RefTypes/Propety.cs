using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{
    internal class Property : Variable
    {

        public List<string> Methodnames { get; } = new List<string>();

        public bool CanRead { get; private set; }
        public bool CanWrite { get; private set; }

        public bool IsIndex { get; }

        public Property() { }

        public Property(PropertyInfo prop) : base(prop.Name, prop.PropertyType)
        {
            if (CanRead = prop.CanRead)
                Methodnames.Add(prop.GetMethod.Name);
            if(CanWrite = prop.CanWrite)
                Methodnames.Add(prop.SetMethod.Name);
            if (prop.Name == "Item" && !TypeIndex.Equals(TypeIndex.Object) && prop.GetIndexParameters().Length > 0)
                IsIndex = true;
        }

        public override void Desc(StreamWriter sw, int space)
        {
            var pre = GetPrefixSpace(space);
            sw.WriteLine($"{pre}@property");
            sw.Write($"{pre}def {Name}(self) -> {TypeIndex.Fullname}:");
            string desc = null;
            if (CanRead)
                desc = " get;";
            if (CanWrite)
                desc += " set;";
            sw.WriteLine($"\"\"\"{Name} {{{desc} }} -> {TypeIndex.Name}\"\"\"");
        }

        public override void FromXml(XElement xe)
        {
            base.FromXml(xe);
            CanRead = bool.Parse(xe.Attribute("CanRead").Value);
            CanWrite = bool.Parse(xe.Attribute("CanWrite").Value);
        }

        public override XElement ToXml()
        {
            XElement xe = base.ToXml();
            xe.Add(
                new XAttribute("CanRead", CanRead),
                new XAttribute("CanWrite", CanWrite));
            return xe;
        }

    }
}
