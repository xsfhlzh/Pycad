using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NFox.Expression.DataSystem
{

    public class SortedList<T> : IEnumerable<T>
        where T : IComparable<T>
    {

        protected List<T> _list = new List<T>();


        public T this[int index]
        {
            get { return _list[index]; }
        }

        public int Count
        {
            get { return _list.Count; }
        }

        public int IndexOf(T value)
        {

            if (Count == 0)
                return -1;

            if (value.CompareTo(_list[0]) == 0)
                return 0;

            int low = 1, high = Count - 1;
            int mid = (low + high) / 2;

            while (low <= high)
            {
                mid = (low + high) / 2;
                switch (_list[mid].CompareTo(value))
                {
                    case 0:
                        if (_list[mid - 1].CompareTo(value) == -1)
                            return mid;
                        else
                            high = mid - 1;
                        break;
                    case 1:
                        high = mid - 1;
                        break;
                    default:
                        low = mid + 1;
                        break;
                }
            }
            return -1;
        }

        public bool Contains(T value)
        {
            return IndexOf(value) != -1;
        }

        public int Add(T value)
        {

            if (Count == 0 || value.CompareTo(_list[0]) < 1)
            {
                _list.Insert(0, value);
                return 0;
            }
            else if (value.CompareTo(_list[Count - 1]) == 1)
            {
                _list.Add(value);
                return Count - 1;
            }
            else
            {
                int low = 0, high = Count - 1;
                int mid = (low + high) / 2;

                while (low <= high)
                {
                    mid = (low + high) / 2;
                    if (_list[mid].CompareTo(value) == -1)
                    {
                        low = mid + 1;
                        if (_list[low].CompareTo(value) > -1)
                            break;
                    }
                    else
                    {
                        high = mid - 1;
                    }
                }
                _list.Insert(low, value);
                return low;
            }
        }

        public void Remove(T value)
        {
            _list.RemoveAt(IndexOf(value));
        }

        public void RemoveAt(int index)
        {
            _list.RemoveAt(index);
        }


        public IEnumerator<T> GetEnumerator()
        {
            foreach (var value in _list)
                yield return value;
        }

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            foreach (var value in _list)
                yield return value;
        }

    }

}
