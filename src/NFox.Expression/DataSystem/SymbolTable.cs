
using System.Linq;
using System.Xml.Linq;
using System.Collections.Generic;
using System.Collections;
using NFox.Expression.SymbolValues;
using System.IO;

namespace NFox.Expression.DataSystem
{

    public abstract class SymbolTable<T> : 
        SimpleDictionary<SymbolDictionary<T>>, 
        IEnumerable<KeyValuePair<string, XElement>>
        where T : ISymbolValue, new()
    {

        #region Member

        private Database _database;
        public Database Database
        {
            set
            {
                _database = value;
                if (_database.FileName != null && File.Exists(_database.FileName))
                {
                    _dictNames =
                        ZipUtils
                        .GetEntryNames(_database.FileName, Prefix, Postfix, false)
                        .ToList();
                }
            }
            get
            {
                return _database;
            }
        }

        protected abstract string Prefix { get; }

        protected abstract string Postfix { get; }

        private List<string> _dictNames = new List<string>();
        public IEnumerable<string> DictionaryNames
        {
            get { return _dictNames; }
        }

        public override SymbolDictionary<T> this[string name]
        {
            get
            {
                SymbolDictionary<T> dict;
                Has(name, out dict);
                return dict;
            }
        }

        public T this[SymbolIndex index]
        {
            get { return this[index.DictionaryName, index.Key]; }
            set { this[index.DictionaryName, index.Key] = value; }
        }

        public T this[string dictName, string key]
        {
            get
            {
                SymbolDictionary<T> dict;
                if (Has(dictName, out dict))
                    return dict[key];
                return default(T);
            }
            set
            {
                SymbolDictionary<T> dict;
                if (Has(dictName, out dict))
                    if (dict.Has(key)) dict[key] = value;
            }
        }

        #endregion

        #region Has

        public override bool Has(string key)
        {
            return _dictNames.Contains(key);
        }

        public bool Has(SymbolIndex index)
        {
            return
                Has(index.DictionaryName) &&
                this[index.DictionaryName].Has(index.Key);
        }

        private string GetDictRealName(string dictName)
        {
            return Prefix + dictName + Postfix;
        }

        public bool Has(string key, out SymbolDictionary<T> dict)
        {
            dict = null;
            if (base.Has(key))
                dict = base[key];
            else if (Has(key))
                dict = Load(key);
            else
                return false;
            return true;
        }

        public bool IsLoad(string key)
        {
            return Has(key) && base.Has(key);
        }

        private SymbolDictionary<T> Load(string key)
        {
            XElement xe = ZipUtils.Extract(Database.FileName, GetDictRealName(key));
            var dict = new SymbolDictionary<T> { Name = key, Database = Database };
            foreach (var e in xe.Elements())
                dict.Add(FromX(e));
            Add(key, dict);
            return dict;
        }

        public void LoadAllDictionaries()
        {
            foreach (var name in _dictNames)
            {
                if (!base.Has(name))
                    Load(name);
            }
        }

        #endregion

        #region Add Remove

        public void Add(T value, bool createDictionary)
        {

            if (value == null || value.Index.IsNull)
                return;

            var dictName = value.Index.DictionaryName;
            AddDictionary(dictName);
            this[dictName].Add(value); 

        }

        public void Add(T value)
        {
            Add(value, false);
        }

        public void Add(string dictName, T value)
        {
            SymbolDictionary<T> dict;
            if (Has(dictName, out dict))
                dict.Add(value);
        }

        public void Remove(T value)
        {
            var index = value.Index;
            Remove(index.DictionaryName, index.Key);
        }


        public void Remove(string dictName, string key)
        {
            SymbolDictionary<T> dict;
            if (Has(dictName, out dict))
                dict.Remove(key);
        }

        public void AddDictionary(string name)
        {
            if (!Has(name))
            {
                _dictNames.Add(name);
                var dict = new SymbolDictionary<T> { Name = name, Database = Database };
                Add(name, dict);
            }
        }

        /// <summary>
        /// 按给定索引重定位符号元素
        /// </summary>
        /// <param name="value">符号元素</param>
        /// <param name="index">索引</param>
        internal void Redirect(T value, SymbolIndex index)
        {
            Remove(value);
            value.Index = index;
            Add(value);
        }

        #endregion

        #region IEnumerator

        private IEnumerator<KeyValuePair<string, XElement>> GetXDicts()
        {
            foreach (var name in _dictNames)
            {
                var dname = GetDictRealName(name);
                XElement xe;
                if (IsLoad(name))
                {
                    xe = new XElement("Dict");
                    foreach (var value in this[name])
                        xe.Add(value.ToX());
                }
                else
                {
                    xe = ZipUtils.Extract(Database.FileName, dname);
                    xe.Name = "Dict";
                }
                yield return new KeyValuePair<string, XElement>(dname, xe);
            }
        }

        IEnumerator<KeyValuePair<string, XElement>> IEnumerable<KeyValuePair<string, XElement>>.GetEnumerator()
        {
            return GetXDicts();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetXDicts();
        }

        #endregion

        /// <summary>
        /// 从xml中反序列化ISave接口对象,如T有派生类,需重写
        /// </summary>
        /// <param name="xe">xml.linq</param>
        /// <returns>对象</returns>
        protected virtual T FromX(XElement xe)
        {
            return XParser.Parse<T>(xe);
        }

        internal void Merge(SymbolTable<T> sourceTable, bool over)
        {
            sourceTable.LoadAllDictionaries();
            foreach (var sdict in sourceTable.Values)
            {
                SymbolDictionary<T> dict;
                if (Has(sdict.Name, out dict))
                    dict.AddRange(sdict, over);
                else
                    dict.AddRange(sdict, over);
            }
        }

    }
}
