using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NFox.Expression.DataSystem;
using System.Xml.Linq;

namespace NFox.Expression.SymbolValues
{

    public class ConfigItem : IParser
    {

        public virtual void FromX(XElement xe)
        {
            Value = xe.Attribute("Value").Value;
        }

        public virtual void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Value", Value));
        }

        public string XName
        {
            get { throw new NotImplementedException(); }
        }
        
        public string Value { set; get; }




    }

}
