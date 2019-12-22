using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NFox.TFunc
{
    internal class ConstantData : Data
    {

        public ConstantData(string name, string desc)
            : base(name, 3)
        {
            _description =
                string.Format(
                    "\n{0}\n{1}\n",
                    Text,
                    desc);
        }

    }
}
