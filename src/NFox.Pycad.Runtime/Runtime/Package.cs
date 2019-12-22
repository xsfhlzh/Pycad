using System.Collections.Generic;
using System.IO;

namespace NFox.Pycad
{
    public class Package : Module
    {

        public readonly string InitPyFileName = "__init__.py";

        public List<Module> Modules = new List<Module>();
        public List<Package> Packages = new List<Package>();

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

        public void GetFileNames(List<string> names)
        {
            names.Add(File.FullName);
            foreach (var m in Modules)
                names.Add(m.File.FullName);
            foreach (Package p in Packages)
                p.GetFileNames(names);
        }

        protected Package(string name) : base(name) { }

        protected Package(DirectoryInfo dir) : this(dir.Name)
        {
            foreach (var f in dir.GetFiles("*.py"))
            {
                if (f.Name != InitPyFileName)
                    Add(new Module(f.Name));
            }
            foreach (var d in dir.GetDirectories())
            {
                Add(new Package(d));
            }
        }

        #region Edit


        public void Add(Module module)
        {
            module.Parent = this;
            if (module is Package)
                Packages.Add((Package)module);
            else
                Modules.Add(module);
        }

        public void RemoveModule(Module module, bool delete)
        {
            if (delete) module.File.Delete();
            Modules.Remove(module);
        }

        #endregion

        public Package GetPackage(string name)
        {
            foreach (Package p in Packages)
            {
                if (p.Name == name)
                    return p;
            }
            return null;
        }

        public Module GetModule(string name)
        {
            foreach (Module m in Modules)
            {
                if (m.Name == name)
                    return m;
            }
            return null;
        }

        public bool Contains(string name)
        {
            foreach (var p in Packages)
            {
                if (p.Name.ToLower() == name.ToLower())
                    return true;
            }
            foreach (var m in Modules)
            {
                if (m.Name.ToLower() == name.ToLower())
                    return true;
            }
            return false;
        }

        public override string ToString()
        {
            return $"Package:({Path})";
        }

        public Module FindModuleByPath(string path)
        {

            if (Path == path)
                return this;

            foreach (var m in Modules)
            {
                if (m.Path == path)
                    return m;
            }

            foreach (var p in Packages)
            {
                var m = p.FindModuleByPath(path);
                if (m != null)
                    return m;
            }

            return null;

        }

    }
}
