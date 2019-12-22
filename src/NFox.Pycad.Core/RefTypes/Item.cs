using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{
    internal abstract class Item
    {

        public string Name { get; protected set; }

        public virtual void Desc(StreamWriter sw, int space) { }

        private static List<string> _keywords;

        public Item() { }

        public override string ToString()
        {
            return Name;
        }

        protected static string Checkname(string name)
        {
            if (_keywords == null)
            {
                IEnumerable names = Engine.Instance.GetValue("keyword.kwlist");
                _keywords = names.Cast<string>().ToList();
                _keywords.AddRange(new string[] { "None", "True", "False" });
            }
            if (_keywords.Contains(name))
                return "_" + name;
            return name;
        }

        protected string GetPrefixSpace(int count)
        {
            return new string(' ', count);
        }

        public static T Parse<T>(XElement xe) where T: Item, new()
        {
            T tobj = new T();
            tobj.FromXml(xe);
            return tobj;
        }


        public static T Parse<T>(XElement xe, string name) where T : Item, new()
        {
            T tobj = Parse<T>(xe);
            tobj.Name = name;
            return tobj;
        }

        public virtual void FromXml(XElement xe)
        {
            Name = xe.Attribute("Name").Value;
        }

        public virtual XElement ToXml()
        {
            return
                new XElement(GetType().Name,
                    new XAttribute("Name", Name));
        }



    }
}
