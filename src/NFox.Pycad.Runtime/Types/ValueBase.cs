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

        public virtual ValueBase GetItem(string key)
        {
            if (Marshal.IsComObject(Value))
                return null;
            try { return ValueBase.GetValue(key, Engine.Instance.GetValue("getattr")(Value, key)); }
            catch { return null; }
        }

        public virtual ValueList GetItems()
        {
            List lst = Engine.Instance.GetValue("clr").Dir(Value);
            ValueList result = new ValueList();
            if (lst != null)
            {
                foreach (string key in lst)
                {
                    dynamic obj = null;
                    try { obj = Engine.Instance.GetValue("getattr")(Value, key); }
                    catch { }
                    result.Add(ValueBase.GetValue(key, obj));
                }
            }
            return result;
        }

        public virtual string TypeName { get { return Engine.Instance.GetValue("type")(Value).__name__; } }

    }

    public class Variant : ValueBase
    {
        public Variant(string name, object value) : base(name, value) { }

        public override int ImageIndex { get { return 1; } }
        public override string Title { get { return $"变量:{Name}"; } }
        public override string Description { get { return $"类型:{ClrType.FullName}"; } }
    }

    public class None : Variant
    {

        public override ValueBase GetItem(string key)
        {
            return null;
        }

        public None(string name) : base(name, null) { }

        public override string Description { get { return $"None"; } }

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

        public override int ImageIndex { get { return 3; } }
        public override string Title
        {
            get
            {
                string s = "";
                if (Overloads.Count > 1)
                    s = $"(+{Overloads.Count - 1}重载)";
                return $"函数:{Name}{s}";
            }
        }

        public override string Description
        {
            get
            {
                if (Overloads.Count > 0)
                    return Overloads[0].ToString();
                else
                    return Value.__doc__;
            }
        }
    }

    public class Module : ValueBase
    {
        public Module(string name, object value) : base(name, value) { }

        public override int ImageIndex { get { return 4; } }
        public override string Title { get { return $"模块:{Value.__name__}"; } }
        public override string Description { get { return Value.__doc__ ?? Value.__file__; } }
    }

    public class Class : ValueBase
    {
        public Class(string name, object value) : base(name, value) { }

        public override int ImageIndex { get { return 5; } }
        public override string Title { get { return $"经典类:{Value.__name__}"; } }
        public override string Description { get { return Value.__file__; } }
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

        public override int ImageIndex { get { return 5; } }
        public override string Title { get { return $"新式类:{Name}"; } }
        public override string Description
        {
            get
            {
                if (Engine.Instance.GetValue("hasattr")(Value, "__doc__") && Value.__doc__ != null)
                    return Value.__doc__;
                else if(Value.__new__.__doc__ != null)
                    return Value.__new__.__doc__;
                return "";
            }
        }
    }


}
