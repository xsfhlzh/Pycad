using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NFox.TFunc
{
    internal class KeyWordData : Data
    {

        public KeyWordData(string name)
            : base(name, 0)
        {
            _description =
                string.Format(
                    "\n{0}\n{0} 语句的代码段\n",
                    Text);
        }

    }
}
