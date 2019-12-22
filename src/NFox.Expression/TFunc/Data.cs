using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ICSharpCode.TextEditor.Gui.CompletionWindow;

namespace NFox.TFunc
{
    internal class Data : DefaultCompletionData
    {

        public Data(string name, int imageIndex)
            : base(name, imageIndex)
        { }

        protected string _description;
        public override string Description
        {
            get { return _description; }
        }

    }
}
