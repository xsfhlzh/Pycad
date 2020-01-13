using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NFox.Pycad
{

    public class ExtensionCollection: Package, IEnumerable<Extension>
    {

        public ExtensionCollection(string name) : base(name)
        {
            foreach (var d in DirectoryEx.Extensions.GetDirectories())
            {
                if (!d.Name.Contains("."))
                    Add(new Extension(d));
            }

            foreach(var d in DirectoryEx.Extensions.GetDirectory(".release").GetDirectories())
            {
                if(Packages.ContainsKey(d.Name))
                    Packages.Remove(d.Name);
                if (!d.Name.Contains("."))
                    Add(new Extension(d));
            }

        }

        public Extension this[string name]
        {
            get { return (Extension)Packages[name]; }
        }

        public Extension this[int index]
        {
            get { return (Extension)Packages.ElementAt(index).Value; }
        }

        public int Count
        {
            get { return Packages.Count; }
        }

        public IEnumerator<Extension> GetEnumerator()
        {
            foreach (var ext in Packages)
                yield return (Extension)ext.Value;
        }


        IEnumerator IEnumerable.GetEnumerator()
        {
           return GetEnumerator();
        }
    }

}
