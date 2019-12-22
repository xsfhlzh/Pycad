
using System;
using System.Xml.Linq;

namespace NFox.Expression.DataSystem
{
    public class SymbolIndex : IEquatable<SymbolIndex>, IComparable<SymbolIndex>, IParser
    {

        public string DictionaryName;
        public string Key;

        public SymbolIndex() { }

        public SymbolIndex(string name)
        {
            DictionaryName = "Main";
            Key = name;
        }

        public SymbolIndex(string dictionaryName, string key)
        {
            if (string.IsNullOrEmpty(dictionaryName))
                DictionaryName = "Main";
            else
                DictionaryName = dictionaryName;
            Key = key;
        }


        public SymbolIndex(string name, string dictionaryName, string key)
        {
            if (string.IsNullOrEmpty(dictionaryName))
                DictionaryName = "Main";
            else
                DictionaryName = dictionaryName;
            if (DictionaryName == "Main")
                Key = name;
            else
                Key = key;
        }


        public string XName
        {
            get { return "Index"; }
        }

        public void FromX(XElement xe)
        {
            DictionaryName = xe.Attribute("Dict").Value;
            Key = xe.Attribute("Key").Value;
        }

        public void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Dict", DictionaryName));
            xe.Add(new XAttribute("Key", Key));
        }

        public bool Equals(SymbolIndex other)
        {
            return
                DictionaryName == other.DictionaryName &&
                Key == other.Key;
        }

        private static SymbolIndex _null = new SymbolIndex(null, null);
        public static SymbolIndex Null
        { 
            get { return _null; } 
        }

        public bool IsNull
        { 
            get { return Equals(_null); } 
        }

        public int CompareTo(SymbolIndex other)
        {
            return
                DictionaryName == other.DictionaryName ?
                Key.CompareTo(other.Key) :
                DictionaryName.CompareTo(other.DictionaryName);
        }

        public static bool operator <(SymbolIndex a, SymbolIndex b)
        {
            return a.CompareTo(b) == -1;
        }

        public static bool operator >(SymbolIndex a, SymbolIndex b)
        {
            return a.CompareTo(b) == 1;
        }

        public override string ToString()
        {
            return string.Format("{0}.{1}", DictionaryName, Key);
        }

        public static SymbolIndex Parse(XElement xe, string attname)
        {
            var att = xe.Attribute(attname);
            if (att != null)
            {
                var keys = att.Value.Split('.');
                return new SymbolIndex(keys[0], keys[1]);
            }
            return null;
        }

    }
}
