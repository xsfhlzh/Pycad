using IronPython.Runtime;
using System.Collections;

namespace NFox.Pycad.Core.Filters
{
    public abstract class OpFilter
    {

        protected static dynamic CreateTypedValue(dynamic code, object value = null)
        {
            if (!(code is int))
                code = code.value__;
            return Engine.Instance.GetValue("acdb.TypedValue")(code, value ?? -1);
        }

        public static OpFilter Create(params object[] source)
        {
            List targe = new List();
            object lst = source;
            if (source.Length == 1)
                lst = source[0];
            else
                lst = new PythonTuple(source);
            return CreateFromSource(lst);
        }

        protected static OpFilter CreateFromSource(object source)
        {
            if (source is List)
                return CreateFromList((List)source);
            else
                return CreateFromTuple((PythonTuple)source);
        }


        private static OpFilter CreateFromList(List source)
        {
            if (source[0] is string)
            {
                string loginame = source[0] as string;
                var itor = new List();
                itor.extend(source[new Slice(1, null)]);
                return CreateLogi(loginame, itor);
            }
            else if (source[0] is IList)
            {
                return new OpOr(source);
            }
            else
            {
                return new OpEqual(source[0], source[1]);
            }
        }

        private static OpFilter CreateFromTuple(PythonTuple source)
        {
            if (source[0] is string)
            {
                string loginame = source[0] as string;
                var itor = new PythonTuple(source[new Slice(1, null)]);
                return CreateLogi(loginame, itor);
            }
            else if (source[0] is IList)
            {
                return new OpAnd(source);
            }
            else if (source[1] is IList)
            {
                return new OpRange(source[0], (IList)source[1]);
            }
            else
            {
                return new OpEqual(source[0], source[1]);
            }
        }

        private static OpFilter CreateLogi(string loginame, IList source)
        {
            switch (loginame.ToLower())
            {
                case "&":
                case "and":
                    return new OpAnd(source);
                case "|":
                case "or":
                    return new OpOr(source);
                case "^":
                case "xor":
                    return new OpXor(source);
                case "~":
                case "not":
                    return new OpNot(CreateFromSource(source));
                default:
                    return new OpComp(loginame, source);
            }
        }


        public abstract string Name { get; }

        public abstract void GetValues(List lst);

        public static OpFilter operator !(OpFilter item)
        {
            return item.Not;
        }

        public OpFilter Not
        {
           get { return new OpNot(this); }
        }

        public PythonTuple ToTuple()
        {
            List lst = new List();
            GetValues(lst);
            return new PythonTuple(lst);
        }

        public override string ToString()
        {
            string s = "";
            foreach (var value in ToTuple())
                s += value.ToString();
            return s;
        }

    }

}
