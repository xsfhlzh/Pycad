
using System.Collections.Generic;
using System.Xml.Linq;
using System;
using NFox.Expression.SymbolValues;

namespace NFox.Expression.DataSystem
{

    public class SymbolDictionary<T> : 
        SimpleDictionary<T>
        where T : ISymbolValue, new()
    {

        public string Name
        { set; get; }

        public Database Database { set; get; }

        #region Add Remove

        public void Add(T value)
        {
            Add(value.Index.Key, value);
        }

        public override void Add(string key, T value)
        {
            base.Add(key, value);
            value.Database = Database;
        }

        public void AddRange(IEnumerable<T> values, bool over)
        {
            foreach (var value in values)
            {
                if (Has(value.Index.Key))
                {
                    if (over)
                        this[value.Index.Key] = value;
                }
                else
                {
                    Add(value);
                }
            }
        }

        public void Remove(T value)
        {
            Remove(value.Index.Key);
        }

        #endregion


    }

}
