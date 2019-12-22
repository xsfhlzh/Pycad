using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ICSharpCode.TextEditor.Gui.CompletionWindow;
using System.Collections;

namespace NFox.TFunc
{

    internal class VariateData : Data
    {

            public string Type;

            public VariateData(string name, string type)
                : base(name, 4)
            {
                Type = type;
                _description =
                    string.Format(
                        "\n{0} {1}\n",
                        type,
                        name);
            }
    }

}
