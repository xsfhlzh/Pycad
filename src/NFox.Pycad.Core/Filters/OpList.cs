using IronPython.Runtime;
using System.Collections;
using System.Collections.Generic;

namespace NFox.Pycad.Core.Filters
{
    public abstract class OpList : OpLogi
    {

        protected List<OpFilter> _lst
            = new List<OpFilter>();

        public virtual void Add(OpFilter value)
        {
            _lst.Add(value);
        }

        public override IEnumerator<OpFilter> GetEnumerator()
        {
            foreach (var value in _lst)
                yield return value;
        }

    }

    public class OpRange : OpList
    {

        public override string Name
        {
            get { return "Range"; }
        }

        public OpRange(object code, IList range)
        {
            if (range is List)
            {
                List lst = (List)range;
                if (lst[0] is string)
                {
                    for (int i = 0; i < lst.Count - 1; i += 2)
                        Add(new OpComp((string)lst[i], code, lst[i + 1]));
                }
                else
                {
                    Add(new OpComp(">=", code, lst[0]));
                    Add(new OpComp("<=", code, lst[1]));
                }
            }
            else if (range is PythonTuple)
            {
                PythonTuple lst = (PythonTuple)range;
                Add(new OpComp(">", code, lst[0]));
                Add(new OpComp("<", code, lst[1]));
            }
        }

        public override void GetValues(List lst)
        {
            foreach (var item in this)
                item.GetValues(lst);
        }

    }

    public class OpAnd : OpList
    {

        public OpAnd(IList source)
        {
            foreach (var v in source)
                Add(CreateFromSource(v));
        }

        public override string Name
        {
            get { return "And"; }
        }

        public override void Add(OpFilter value)
        {
            if (value is OpAnd)
            {
                foreach (var item in (OpAnd)value)
                    _lst.Add(item);
            }
            else
            {
                _lst.Add(value);
            }
        }

        public override void GetValues(List lst)
        {
            if (_lst.Count == 1 || lst.Count == 0)
            {
                foreach (var item in this)
                    item.GetValues(lst);
            }
            else
            {
                base.GetValues(lst);
            }
        }

    }

    public class OpOr : OpList
    {

        public OpOr(IList source)
        {
            foreach (var v in source)
                Add(CreateFromSource(v));
        }

        public override string Name
        {
            get { return "Or"; }
        }

        public override void Add(OpFilter value)
        {
            if (value is OpOr)
            {
                foreach (var item in (OpOr)value)
                    _lst.Add(item);
            }
            else
            {
                _lst.Add(value);
            }
        }

        public override void GetValues(List lst)
        {
            if (_lst.Count == 1)
                _lst[0].GetValues(lst);
            else
                base.GetValues(lst);
        }

    }

}
