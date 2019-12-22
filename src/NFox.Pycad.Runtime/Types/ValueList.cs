using IronPython.Runtime;
using Newtonsoft.Json.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace NFox.Pycad.Types
{
    public class ValueList : IEnumerable<ValueBase>
    {

        public List<ValueBase> _values { get; private set; }

        public ValueList()
        {
            _values = new List<ValueBase>();
        }

        public static ValueList GetGlobals(PythonDictionary dict)
        {
            ValueList lst = new ValueList();
            if (dict != null)
            {
                foreach (var kv in dict)
                    lst.Add(ValueBase.GetValue(kv.Key.ToString(), kv.Value));
            }
            return lst;
        }

        public static ValueList[] GetLocals(PythonDictionary dict)
        {
            ValueList[] lsts = { new ValueList(), new ValueList() };
            if (dict != null)
            {
                foreach (var kv in dict)
                {
                    dynamic v = kv.Value;
                    if (v is ClosureCell)
                    {
                        try { v = v.cell_contents; }
                        catch { v = null; }
                        lsts[1].Add(ValueBase.GetValue(kv.Key.ToString(), v));
                    }
                    else
                    {
                        lsts[0].Add(ValueBase.GetValue(kv.Key.ToString(), v));
                    }
                }
            }
            return lsts;
        }

        public void Clear()
        {
            _values.Clear();
        }

        public void Add(string key, object obj)
        {
            Add(ValueBase.GetValue(key, obj));
        }

        public void Add(ValueBase item)
        {
            _values.Add(item);
        }

        public ValueBase GetValue(string name)
        {
            string[] names = name.Split('.');
            var t = _values.FirstOrDefault(v => v.Name == names[0]);
            for(int i = 1; i < names.Length; i++)
            {
                if (t == null)
                    return t;
                t = t.GetItem(names[i]);
            }
            return t;
        }

        public JObject ToJson()
        {
            JObject jobj = new JObject();
            foreach (var v in _values)
                jobj.Add(new JProperty(v.Name, GetJsonValue(v.Value)));
            return jobj;
        }

        private object GetJsonValue(object value)
        {
            if (value == null || value is short || value is int || value is long || value is float || value is double || value is bool)
                return value;
            if (value is string)
                return $"\"{value}\"";
            else
                return Engine.Instance.GetStr(value);
        }

        public IEnumerator<ValueBase> GetEnumerator()
        {
            foreach (var item in _values)
                yield return item;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

    }
}
