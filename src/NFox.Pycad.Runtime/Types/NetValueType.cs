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

        public override ValueList GetItems()
        {
            List lst = Engine.Instance.GetValue("clr").Dir(Value);
            ValueList result = new ValueList();
            var names = lst.Cast<string>().Where(s => !s.StartsWith("_"));
            foreach (var name in names)
            {
                dynamic obj = null;
                try { obj = Engine.Instance.GetValue("getattr")(Value, name); }
                catch { }
                result.Add(ValueBase.GetValue(name, obj));
            }
            return result;
        }

    }

    public class NetVariant : NetValueType
    {

        private PythonType _type;

        public NetVariant(string name, object value, PythonType type = null) : base(name, value)
        {
           _type = type ?? Engine.Instance.GetValue("type")(value);
        }

        public override int ImageIndex { get { return 1; } }
        public override string Title { get { return $"变量:{Name}"; } }
        public override string Description { get { return $"类型:{ClrType.FullName}"; } }

        public override string TypeName
        {
            get { return _type.__clrtype__().Name; }
        }

        public override ValueList GetItems()
        {
            List lst = Engine.Instance.GetValue("clr").Dir(_type);
            ValueList result = new ValueList();
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
                result.Add(ValueBase.GetValue(name, obj, type));
            }
            return result;
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

        public override int ImageIndex { get { return 5; } }

        public override string Title
        {
            get
            {
                string s = "";
                if (IsCallable && Overloads.Count > 1)
                    s = $"(+{Overloads.Count - 1}重载)";
                return $"类型:{Name}{s}";
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
                        return $"静态类:{t.FullName}";
                    else
                        return $"抽象类:{t.FullName}";
                }
                if (Overloads.Count > 0)
                    return Overloads[0].ToString();
                else
                    return Value.__doc__;
            }
        }

        public override dynamic ClrType
        {
            get { return Engine.Instance.GetValue("clr").GetClrType(Value); }
        }

    }

    public class Event : NetValueType
    {
        public Event(string name, object value) : base(name, value) { }

        public override int ImageIndex { get { return 6; } }
        public override string Title { get { return $"事件:{Name}"; } }
        public override string Description
        {
            get { return $"类型:{Value.Event.Info.EventHandlerType.FullName}"; }
        }
    }

    public class Namespace : NetValueType
    {
        public Namespace(string name, object value) : base(name, value) { }

        public override string Title { get { return $"命名空间"; } }
        public override string Description { get { return Value.Name; } }
        public override int ImageIndex { get { return 7; } }
    }
    
    public class Enum : NetType
    {
        public Enum(string name, object value) : base(name, value) { }

        public override int ImageIndex { get { return 8; } }
        public override string Title { get { return $"枚举:{Name}"; } }
        public override string Description
        {
            get
            {
                var names = System.Enum.GetNames(Value);
                var values = System.Enum.GetValues(Value);
                var res = new List<string>();
                for (int i = 0; i < names.Length; i++)
                    res.Add($"{names[i]}({(int)values[i]})");
                return string.Join("\n", res);
            }
        }
    }


}
