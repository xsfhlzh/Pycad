using IronPython.Runtime;
using IronPython.Runtime.Types;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace NFox.Pycad.Types
{
    public abstract class NetValueType : ValueBase
    {

        public NetValueType(string name, object value) : base(name, value){ }

        public override IEnumerable<ValueTree> GetItems()
        {
            List lst = Engine.Instance.GetValue("clr").Dir(Value);
            var names = lst.Cast<string>().Where(s => !s.StartsWith("_"));
            foreach (var name in names)
            {
                dynamic obj = null;
                try { obj = Engine.Instance.GetValue("getattr")(Value, name); }
                catch { }
                yield return new ValueTree(ValueBase.GetValue(name, obj));
            }
        }

    }

    public class NetVariant : NetValueType
    {

        private PythonType _type;

        private static List<string> _basetypes =
            new List<string>
            {
                "System.Object", "System.String",
                "System.Boolean", "System.Byte", "System.SByte", "System.Char",
                "System.Decimal", "System.Double", "System.Single",
                "System.Int64", "System.UInt64",
                "System.Int32", "System.UInt32",
                "System.Int16", "System.UInt16",
                "IronPython.Runtime.PythonDictionary",
                "IronPython.Runtime.PythonTuple",
                "IronPython.Runtime.List",
                "IronPython.Runtime.SetCollection",
            };

        public NetVariant(string name, object value, PythonType type = null) : base(name, value)
        {
           _type = type ?? Engine.Instance.GetValue("type")(value);
        }

        public override string Description
        {
            get { return Engine.Instance.GetStr(Value); }
        }

        public override string TypeName
        {
            get { return _type.__clrtype__().FullName; }
        }

        public override IEnumerable<ValueTree> GetItems()
        {
            List lst = Engine.Instance.GetValue("clr").Dir(_type);
            var names = lst.Cast<string>().Where(s => !s.StartsWith("_"));
            foreach (var name in names)
            {
                dynamic type = null;
                dynamic obj = null;
                try
                {
                    type = Engine.Instance.GetValue("getattr")(_type, name);
                    obj = Engine.Instance.GetValue("getattr")(Value, name);
                }
                catch { }
                yield return new ValueTree(ValueBase.GetValue(name, obj, type));
            }
        }

        public override bool HasItems
        {
            get { return !_basetypes.Contains(TypeName); }
        }

        public override int Order
        {
            get { return 0; }
        }

    }

    public class NetType : NetValueType
    {
        public NetType(string name, object value) : base(name, value) { }

        public override bool IsCallable { get { return Engine.Instance.GetValue("callable")(Value.__new__); } }

        protected override void NewOverloads()
        {
            string s = Value.__doc__;
            if(s != null)
            {
                if(Regex.IsMatch(s, $@"{Name}\(.*?\)"))
                {
                    Match m = Regex.Match(s, $@"^(.*?)\s*(?={Name}\()");
                    s = m.Value;
                }
                s = Regex.Replace(s, @"^\s*|\s*$", "");
            }

            if (s != null)
                s += "\n";

            var newfunc = Value.__new__;
            _overloads = new List<string>();
            string patt = @"__new__\(cls: type(, )*";
            if (Engine.Instance.GetValue("hasattr")(newfunc, "Overloads"))
            {
                foreach (var func in newfunc.Overloads.Functions)
                    _overloads.Add(s + Regex.Replace(func.__doc__, patt, $"{Name}("));
            }
            else
            {
                _overloads.Add(s + Regex.Replace(newfunc.__doc__, patt, $"{Name}("));
            }
        }

        public override string Description
        {
            get
            {
                var t = ClrType;
                if (t.IsAbstract)
                {
                    if(t.IsSealed)
                        return $"static class {t.FullName}";
                    else
                        return $"abstract class {t.FullName}";
                }
                return $"class {t.FullName}";
            }
        }

        public override dynamic ClrType
        {
            get { return Engine.Instance.GetValue("clr").GetClrType(Value); }
        }

        public override bool HasItems
        {
            get { return true; }
        }

        public override int Order
        {
            get { return 3; }
        }

    }

    public class Event : NetValueType
    {
        public Event(string name, object value) : base(name, value) { }

        public override string Description
        {
            get { return $"event {Value.Event.Info.EventHandlerType.Name}"; }
        }

        public override int Order
        {
            get { return 2; }
        }

    }

    public class Namespace : NetValueType
    {
        public Namespace(string name, object value) : base(name, value) { }

        public override string Description { get { return $"namespace {Name}"; } }

        public override bool HasItems
        {
            get { return true; }
        }

        public override int Order
        {
            get { return 1; }
        }

    }
    
    public class Enum : NetType
    {
        public Enum(string name, object value) : base(name, value) { }

        public override string Description
        {
            get { return $"enum {Name}"; }
        }

        public override bool HasItems
        {
            get { return true; }
        }

        public override int Order
        {
            get { return 3; }
        }

    }


}
