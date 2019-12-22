using System;
using System.Collections.Generic;
using System.Linq;

namespace NFox.Pycad.RefTypes
{

    internal class ItemDictionary<T> : SortedDictionary<string, T>
            where T : Item
    {

        public void Add(Variable item)
        {
            if (!ContainsKey(item.Name))
            {
                //Owner?.GetNamespace()?.Import(item.TypeIndex);
                Add(item.Name, item as T);
            }
        }

        public void Add(TypeIndex item)
        {
            if (!ContainsKey(item.Name))
            {
                Add(item.Name, item as T);
            }
        }

    }

    internal class ItemList<T> : List<T>
        where T : Item
    {

        public void Add(Variable item)
        {
            //Owner?.GetNamespace()?.Import(item.TypeIndex);
            Add(item as T);
        }

        public void Add(TypeIndex item)
        {
            Add(item as T);
        }

    }

}
