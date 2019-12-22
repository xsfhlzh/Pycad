using System.Collections.Generic;
using System.Collections;
using System.Dynamic;

namespace NFox.Expression.DataSystem
{
    public abstract class SimpleDictionary<T> : DynamicObject, IEnumerable<T>
    {
        
        #region Dictionary

        //protected Dictionary<string, T> _dict =
        //    new Dictionary<string, T>();

        //public virtual void Add(string key, T obj)
        //{
        //    _dict.Add(key, obj);
        //}

        //public virtual void Remove(string key)
        //{
        //    _dict.Remove(key);
        //}

        //public virtual bool Has(string key)
        //{
        //    return _dict.ContainsKey(key);
        //}

        //public virtual T this[string key]
        //{
        //    get { return _dict[key]; }
        //    set { _dict[key] = value; }
        //}

        #endregion

        public SimpleDictionary()
        {
            Keys = new SortedList<string>();
            Values = new List<T>();
        }

        public SortedList<string> Keys { protected set; get; }
        public List<T> Values { protected set; get; }

        public int Count
        {
            get { return Keys.Count; }
        }

        public virtual void Add(string key, T value)
        {
            int i = Keys.Add(key);
            Values.Insert(i, value);
        }

        public virtual void Remove(string key)
        {
            var index = Keys.IndexOf(key);
            Keys.RemoveAt(index);
            Values.RemoveAt(index);
        }

        public virtual bool Has(string key)
        {
            return Keys.Contains(key);
        }

        public virtual T this[string key]
        {
            get { return Values[Keys.IndexOf(key)]; }
            set { Values[Keys.IndexOf(key)] = value; }
        }

        public IEnumerator<T> GetEnumerator()
        {
            foreach (var value in Values)
                yield return value;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            foreach (var value in Values)
                yield return value;
        }

        public override bool TryGetMember(GetMemberBinder binder, out object result)
        {
            if(Has(binder.Name))
            {
                result = this[binder.Name];
                return true;
            }
            return base.TryGetMember(binder, out result);
        }

    }
}
