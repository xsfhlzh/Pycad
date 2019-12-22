using System.IO;

namespace NFox.Pycad
{
    public class Module
    {

        public Package Parent { get; set; }

        public string Name { get; set; }

        public virtual string FullName
        {
            get { return $"{Parent.FullName}.{Name.Substring(0, Name.Length - 3)}"; }
        }

        public virtual FileInfo File
        {
            get { return new FileInfo(Path); }
        }

        protected string _path;

        public virtual string Path
        {
            get { return _path ?? $"{Parent.Path}\\{Name}"; }
        }

        public bool IsRoot { get { return this == Engine.Instance.Extensions; } }

        public virtual bool IsModule { get { return true; } }

        public virtual bool IsPackage { get { return false; } }

        public virtual bool IsExtension { get { return false; } }

        public bool IsSystem { get; set; }

        public Module(string name)
        {
            Name = name;
            IsSystem = false;
        }

        public static Module FromFile(string path)
        {
            string name = System.IO.Path.GetFileNameWithoutExtension(path);
            Module m = new Module(name);
            m._path = path;
            return m;
        }

        public bool IsPartOf(Module other)
        {
            if (other is Package)
            {
                var p = this;
                while (p != null)
                {
                    if (p == other)
                        return true;
                    p = p.Parent;
                }
            }
            return false;
        }

        public bool IsSubOf(Module other)
        {
            return Parent == other;
        }

        public override string ToString()
        {
            return $"Module:({Path})";
        }

    }
}
