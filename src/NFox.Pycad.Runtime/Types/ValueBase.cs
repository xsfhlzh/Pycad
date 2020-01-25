using IronPython.Runtime;
using IronPython.Runtime.Types;
using Microsoft.Scripting.Actions;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

namespace NFox.Pycad.Types
{
    public abstract class ValueBase : TypeBase
    {

        protected ValueBase(string text, object value)
        {
            Name = text;
            Value = value;
        }

        public dynamic Value { get; protected set; }

        public virtual bool IsCallable { get { return false; } }

        protected virtual void NewOverloads() { }

        public List<string> _overloads;
        public List<string> Overloads
        {
            get
            {
                if (_overloads == null)
                    NewOverloads();
                return _overloads;
            }
        }

        public virtual dynamic ClrType
        {
            get { return Engine.Instance.GetValue("clr").GetClrType(Engine.Instance.GetValue("type")(Value)); }
        }

        private const string NewStyleTypeName =
            "IronPython.NewTypes.System.Object_1$1";

        public static ValueBase GetValue(string name, object value, dynamic type = null)
        {

            if (type == null)
            {
                if (value == null)
                    return new None(name);
                type = Engine.Instance.GetValue("type")(value);
            }

            //.Net数据类型
            if (value is NamespaceTracker)
                return new Namespace(name, value);
            if (value is ReflectedEvent.BoundEvent)
                return new Event(name, value);

            //Python数据类型
            if (value is PythonModule)
                return new Module(name, value);
            if (value is OldClass)
                return new Class(name, value);

            if (value is Method ||
                value is PythonFunction ||
                value is BuiltinFunction ||
                value is BuiltinMethodDescriptor ||
                value is ClassMethodDescriptor)
                return new Function(name, value);

            //类型
            if (value is PythonType)
            {
                type = Engine.Instance.GetValue("clr").GetClrType(value);
                if (type.IsEnum)
                    return new Enum(name, value);
                else if (type.FullName == NewStyleTypeName)
                    return new Type(name, value);
                else
                    return new NetType(name, value);
            }

            if (type is ReflectedProperty)
                type = type.PropertyType;
            if (type is ReflectedPropertyTracker)
                type = type.DeclaringType;

            if (type is PythonType || type is System.Type)
            {

                dynamic t = Engine.Instance.GetValue("clr").GetClrType(type);
                //Python对象
                if (value is OldInstance || t.FullName == NewStyleTypeName)
                {
                    //设置__call__按函数处理
                    if (Engine.Instance.GetValue("callable")(value))
                        return new Function(name, value);
                    else
                        return new Variant(name, value);
                }
                return new NetVariant(name, value, type);
            }

            return new NetVariant(name, value);

        }

        
        public virtual bool HasItems { get { return false; } }

        public virtual ValueBase GetItem(string key)
        {
            if (Marshal.IsComObject(Value))
                return null;
            try { return ValueBase.GetValue(key, Engine.Instance.GetValue("getattr")(Value, key)); }
            catch { return null; }
        }

        public virtual IEnumerable<ValueTree> GetItems()
        {
            List lst = Engine.Instance.GetValue("clr").Dir(Value);
            if (lst != null)
            {
                foreach (string key in lst)
                {
                    dynamic obj = null;
                    try { obj = Engine.Instance.GetValue("getattr")(Value, key); }
                    catch { }
                    yield return new ValueTree(ValueBase.GetValue(key, obj));
                }
            }
        }

        public virtual string TypeName { get { return Engine.Instance.GetValue("type")(Value).__name__; } }

    }

    public class Variant : ValueBase
    {

        private static List<string> _basetypes =
            new List<string>{
                "int", "float", "bool", "tuple", "list", "dict", "set", "str"
            };

        public Variant(string name, object value) : base(name, value) { }

        public override string Description { get { return Engine.Instance.GetStr(Value); } }

        public override bool HasItems
        {
            get { return !_basetypes.Contains(TypeName); }
        }

        public override int Order
        {
            get { return 0; }
        }

    }

    public class None : Variant
    {

        public override ValueBase GetItem(string key)
        {
            return null;
        }

        public None(string name) : base(name, null) { }

        public override string Description { get { return "None"; } }

        public override bool HasItems
        {
            get { return false; }
        }

        public override int Order
        {
            get { return 0; }
        }

    }


    public class Function : ValueBase
    {

        public Function(string name, object value) : base(name, value) { }

        public override bool IsCallable { get { return true; } }

        protected override void NewOverloads()
        {
            var newfunc = Value;
            _overloads = new List<string>();
            if (Engine.Instance.GetValue("hasattr")(newfunc, "Overloads"))
            {
                foreach (var func in newfunc.Overloads.Functions)
                    _overloads.Add(func.__doc__);
            }
            else if (newfunc.__doc__ != null)
            {
                var ms = Regex.Matches(newfunc.__doc__, $"{Name}\\(.*?\\)(->.*?)*");
                foreach (Match m in ms)
                    _overloads.Add(m.Value);
            }
        }

        public override string Description
        {
            get
            {
                if (Engine.Instance.GetValue("hasattr")(Value, "__name__"))
                    return $"function {Engine.Instance.GetValue("getattr")(Value, "__name__")}";
                return $"function {Value.__func__.__name__}";
            }
        }

        public override int Order
        {
            get { return 1; }
        }

    }

    public class Module : ValueBase
    {

        public Module(string name, object value) : base(name, value) { }

        public override string Description { get { return $"module: {Value.__name__}"; } }

        public override bool HasItems
        {
            get { return true; }
        }

        public override int Order
        {
            get { return 2; }
        }

    }

    public class Class : ValueBase
    {
        public Class(string name, object value) : base(name, value) { }

        public override string Description { get { return $"class {Value.__name__}"; } }

        public override bool HasItems
        {
            get { return true; }
        }

        public override int Order
        {
            get { return 3; }
        }

    }

    public class Type : ValueBase
    {
        public Type(string name, object value) : base(name, value) { }

        public override bool IsCallable { get { return Engine.Instance.GetValue("callable")(Value.__new__); } }

        protected override void NewOverloads()
        {
            var newfunc = Value.__new__;
            _overloads = new List<string>();
            if (Engine.Instance.GetValue("hasattr")(newfunc, "Overloads"))
            {
                foreach (var func in newfunc.Overloads.Functions)
                    _overloads.Add(func.__doc__);
            }
            else
            {
                _overloads.Add(newfunc.__doc__);
            }
        }

        public override string Description
        {
            get
            {
                return $"type {Value.__name__}";
            }
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
