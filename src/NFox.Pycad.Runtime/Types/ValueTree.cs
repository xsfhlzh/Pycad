using IronPython.Runtime;
using IronPython.Runtime.Exceptions;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System;
using Microsoft.Scripting.Hosting;

namespace NFox.Pycad.Types
{
    public class ValueTree : IEnumerable<ValueTree>, IComparable<ValueTree>
    {

        private static ValueTree _root;
        public static ScriptScope Scope { get; private set; }

        private static int _maxid = 0;

        public string Name { get; private set; }

        public ValueBase Value { get; private set; }

        public bool HasItems { get; private set; }

        public int Id { get; private set; }

        public bool Expanded { get; private set; }

        private List<ValueTree> _values = new List<ValueTree>();

        public ValueTree this[int index]
        {
            get { return _values[index]; }
        }

        public ValueTree this[string name]
        {
            get
            {
                if(HasItems)
                {
                    Expand();
                    foreach(var item in _values)
                    {
                        if (item.Name == name)
                            return item;
                    }
                }
                return null;
            }
        }

        public ValueTree(string name, bool hasitems, bool expanded = false)
        {
            Name = name;
            Expanded = expanded;
            if (HasItems = hasitems)
                Id = _maxid++;
        }

        public ValueTree(ValueBase value, bool expanded = false)
        {
            Name = value.Name;
            Expanded = expanded;
            Value = value;
            if (HasItems = Value.HasItems)
                Id = _maxid++;
        }

        public static ValueTree GetValues(TraceBackFrame frame)
        {

            Scope = Engine.Instance.CreateScope();
            _maxid = 0;
            _root =
                new ValueTree(".", true, true)
                {
                    new ValueTree("Globals", true, true),
                    new ValueTree("Locals", true, true)
                };
            if (frame.f_globals != null)
            {
                foreach (var kv in frame.f_globals)
                {
                    string name = kv.Key.ToString();
                    object value = kv.Value; 
                    _root[0].Add(ValueBase.GetValue(name, value));
                    if(value != null)
                        Scope.SetVariable(name, value);
                }
            }

            if (frame.f_locals != null)
            {
                var dict = (PythonDictionary)frame.f_locals;
                foreach (var kv in (PythonDictionary)frame.f_locals)
                {
                    string name = kv.Key.ToString();
                    dynamic value = kv.Value;
                    if (value is ClosureCell)
                    {

                        if(name.EndsWith("1"))
                        {
                            var rname = name.Substring(0, name.Length - 1);
                            if (dict.keys().Cast<string>().Contains(rname))
                                name = rname;
                        }
                        try { value = value.cell_contents; }
                        catch { value = null; }
                        _root[1].Add(ValueBase.GetValue(name, value));
                        if (value != null)
                            Scope.SetVariable(name, value);
                    }
                }
            }
            return _root;
        }

        public void Add(ValueBase item, bool expanded = false)
        {
            Add(new ValueTree(item, expanded));
        }

        public void Add(ValueTree item)
        {
            _values.Add(item);
        }

        private void Expand()
        {
            if (!Expanded)
            {
                Expanded = true;
                _values = Value.GetItems().OrderBy(i => i).ToList();
            }
        }

        public ValueTree GetTree(int index)
        {
            if (Id == index)
            {
                Expand();
                return this;
            }
            else if(HasItems && Expanded)
            {
                foreach (var tree in _values)
                {
                    var res = tree.GetTree(index);
                    if (res != null)
                        return res;
                }
            }
            return null;
        }

        private static List<string> _keywords;

        public ValueTree GetTree(string name)
        {

            if (name.StartsWith("\"") && name.StartsWith("'"))
            {
                return new ValueTree($"str: {name}", false);
            }
            else if (Regex.IsMatch(name, @"^(0[xXoO])?\d+$"))
            {
                return new ValueTree($"int: {name}", false);
            }
            else if (Regex.IsMatch(name, @"^[\+\-]?\d+\.?\d*([eE][+-]?\d+)?$"))
            {
                return new ValueTree($"float: {name}", false);
            }
            else
            {

                if (_keywords == null)
                {
                    _keywords = 
                        ((IEnumerable)Engine.Instance.GetValue("keyword.kwlist"))
                        .Cast<string>().ToList();
                }

                if (_keywords.Contains(name))
                {
                    return new ValueTree($"keyword: {name}", false);
                }
                else
                {

                    var names = name.Split('.');
                    var tree = _root[0][names[0]] ?? _root[1][names[0]];
                    if (tree != null)
                    {
                        for (int i = 1; i < names.Length; i++)
                        {
                            tree = tree[names[i]];
                            if (tree == null)
                                break;
                        }
                    }
                    return tree;

                }
            }
        }

        public IEnumerator<ValueTree> GetEnumerator()
        {
            return _values.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return _values.GetEnumerator();
        }

        public override string ToString()
        {
            return $"{{ Name: {Name}, Value: {Value.Value}, Id: {Id} }}";
        }

        public int CompareTo(ValueTree other)
        {
            return Value.CompareTo(other.Value);
        }

    }
}
