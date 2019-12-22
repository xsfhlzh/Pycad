using IronPython.Runtime;
using System.Collections;
using System.Collections.Generic;

namespace NFox.Pycad.Core.Filters
{
    public class OpComp : OpEqual
    {

        public string Content { get; }

        public override string Name
        {
            get { return "Comp"; }
        }

        public OpComp(string content, IList lst)
            : base(lst[0], lst[1])
        {
            Content = content;
        }

        public OpComp(string content, object code, object value)
            : base(code, value)
        {
            Content = content;
        }

        public override void GetValues(List lst)
        {
            lst.append(CreateTypedValue(-4, Content));
            lst.append(Value);
        }

    }

}
