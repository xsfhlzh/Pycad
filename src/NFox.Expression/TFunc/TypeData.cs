using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NFox.TFunc
{
    internal class TypeData : Data
    {

        public TypeData(string name, string desc)
            : base(name, 1)
        {
            _description =
                string.Format(
                    "\n{0}\n{1}\n",
                    Text,
                    desc);
        }

    }
}
