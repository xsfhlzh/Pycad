using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NFox.Expression.DataSystem;
using System.Xml.Linq;

namespace NFox.Expression.SymbolValues
{
    public class PartAttrib : IEquatable<PartAttrib>, IParser
    {

        public string Name { set; get; }
        public string Value { set; get; }

        public PartAttrib()
        {

        }

        public PartAttrib(string name)
        {
            Name = name;
        }

        public PartAttrib(string name, string value)
        {
            Name = name;
            Value = value;
        }

        public PartAttrib Copy(bool hasData)
        {
            if (hasData)
                return new PartAttrib(Name, Value);
            else
                return new PartAttrib(Name);
        }

        public bool Equals(PartAttrib other)
        {
            return
                this.Name == other.Name &&
                this.Value == other.Value;
        }

        public void FromX(XElement xe)
        {
            Name = xe.Attribute("Name").Value;
            Value = xe.Attribute("Value").Value;
        }

        public string XName
        {
            get { return "Attrib"; }
        }

        public void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Name", Name));
            xe.Add(new XAttribute("Value", Value + ""));
        }



    }
}
