using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ICSharpCode.TextEditor.Gui.CompletionWindow;
using System.Collections;

namespace NFox.TFunc
{
    internal class MethodData : Data, IEnumerable<ICompletionData>
    {

        private class ParamData : Data
        {

            public string Type;
            bool _isParams = false;
            bool _isOptional = false;

            public ParamData(string name, string type, string desc)
                : base(name, 4)
            {
                Type = type;
                _description = desc;
            }

            public ParamData(string name, string type, string desc, bool isOptional, bool isParams)
                : base(name, 4)
            {
                Type = type;
                _description = desc;
                _isOptional = isOptional;
                _isParams = isParams;
            }

            public string CallWay
            {
                get
                {
                    string desc = Type + " " + Text;
                    if (_isOptional) desc = "[" + desc + "]";
                    if (_isParams) desc += "...";
                    return desc;
                }
            }

            public override string Description
            {
                get
                {
                    string desc = Text;
                    string desc2 = _description;
                    if (_isOptional)
                    {
                        desc = "[" + desc + "]";
                        desc2 = "可选参数，" + _description;
                    }
                    if (_isParams)
                    {
                        desc += "...";
                        desc2 = "参数数目可变，" + _description;
                    }
                    desc += " " + desc2;
                    return desc;
                }
            }

        }

        List<ParamData> _pars = new List<ParamData>();

        public MethodData(string name, string desc)
            : base(name, 2)
        {
            _description = desc;
        }

        public void Add(string name, string type, string desc)
        {
            _pars.Add(new ParamData(name, type, desc));
        }

        public void Add(string name, string type, string desc, bool isOptional, bool isParams)
        {
            _pars.Add(new ParamData(name, type, desc, isOptional, isParams));
        }

        public override string Description
        {
            get
            {
                string paramDesc = string.Join("\n  ", _pars.Select(p => p.Description).ToArray());
                if (paramDesc == "") paramDesc = "无";
                return
                    string.Format(
                        "\n{0}({1})\n{2}\n参数\n  {3}\n",
                        Text,
                        string.Join(", ", _pars.Select(p => p.CallWay).ToArray()),
                        _description,
                        paramDesc);
            }
        }


        public IEnumerator<ICompletionData> GetEnumerator()
        {
            foreach (ICompletionData par in _pars)
                yield return par;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
