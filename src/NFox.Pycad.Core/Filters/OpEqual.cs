using IronPython.Runtime;
using System.Collections.Generic;

namespace NFox.Pycad.Core.Filters
{
    public class OpEqual : OpFilter
    {

        public object Value { get; private set; }

        public override string Name
        {
            get { return "Equal"; }
        }

        public OpEqual(object code, object value)
        {
            Value = CreateTypedValue(code, value);
        }

        public override void GetValues(List lst)
        {
            lst.append(Value);
        }

    }
}
