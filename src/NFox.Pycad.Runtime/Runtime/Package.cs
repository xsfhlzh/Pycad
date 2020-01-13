using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace NFox.Pycad
{
    public class Package : Module
    {

        public readonly string InitPyFileName = "__init__.py";

        public Dictionary<string, Module> Modules = new Dictionary<string, Module>();
        public Dictionary<string, Package> Packages = new Dictionary<string, Package>();

        public virtual DirectoryInfo Directory
        {
            get { return new DirectoryInfo(Path); }
        }

        public override FileInfo File
        {
            get { return Directory.GetFile(InitPyFileName); }
        }

        public override string FullName
        {
            get { return $"{Parent.FullName}.{Name}"; }
        }

        public override bool IsModule { get { return false; } }

        public override bool IsPackage { get { return true; } }

        public virtual void GetFileNames(List<string> names)
        {
            names.Add(File.FullName);
            foreach (var m in Modules)
                names.Add(m.Value.File.FullName);
            foreach (var p in Packages)
                p.Value.GetFileNames(names);
        }

        public virtual void Build(Stream stream)
        {
            string targetpath = Build();
            var dllfile = new FileInfo(targetpath);
            using (var source = dllfile.OpenRead())
                source.CopyTo(stream);
            dllfile.Delete();
        }

        public string Build()
        {
            string targetpath = $"{DirectoryEx.Temp.FullName}\\{Name}.dll";
            List<string> names = new List<string>();
            GetFileNames(names);
            var code = $"import clr;clr.CompileModules('{targetpath}',{string.Join(",", names.Select(s => $"'{s}'"))});";
            Engine.Instance.Execute(code.Replace("\\", "/"));
            return targetpath;
        }

        protected Package(string name) : base(name) { }

        public Package(DirectoryInfo dir, bool isroot = false): this(dir.Name)
        {
            if (isroot)
                _path = dir.FullName;
            foreach (var f in dir.GetFiles("*.py"))
            {
                if (f.Name != InitPyFileName)
                    Add(new Module(f.Name));
            }
            foreach (var d in dir.GetDirectories())
            {
                if (!d.Name.Contains("."))
                    Add(new Package(d));
            }
        }

        #region Edit


        public void Add(Module module)
        {
            module.Parent = this;
            if (module is Package)
                Packages.Add(module.Name, (Package)module);
            else
                Modules.Add(module.Name, module);
        }

        #endregion

        public override string ToString()
        {
            return $"Package:({Path})";
        }


    }
}
