using IronPython.Runtime;
using System.Collections;
using System.Collections.Generic;

namespace NFox.Pycad.Core.Filters
{
    public abstract class OpLogi : OpFilter, IEnumerable<OpFilter>
    {

        public object First
        {
            get { return CreateTypedValue(-4, $"<{Name}"); }
        }

        public object Last
        {
            get { return CreateTypedValue(-4, $"{Name}>"); }
        }

        public override void GetValues(List lst)
        {
            lst.append(First);
            foreach (var item in this)
            {
                item.GetValues(lst);
            }
            lst.append(Last);
        }

        public abstract IEnumerator<OpFilter> GetEnumerator();

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }

    public class OpNot : OpLogi
    {

        public OpFilter Value { get; }

        public OpNot(OpFilter value)
        {
            Value = value;
        }

        public override string Name
        {
            get { return "Not"; }
        }

        public override IEnumerator<OpFilter> GetEnumerator()
        {
            yield return Value;
        }
    }

    public class OpXor : OpLogi
    {

        public OpXor(IList source)
        {
            Left = CreateFromSource(source[0]);
            Right = CreateFromSource(source[1]);
        }

        public OpFilter Left { get; }
        public OpFilter Right { get; }

        public override string Name
        {
            get { return "Xor"; }
        }

        public override IEnumerator<OpFilter> GetEnumerator()
        {
            yield return Left;
            yield return Right;
        }
    }


}
