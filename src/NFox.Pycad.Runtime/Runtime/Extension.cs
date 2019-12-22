using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.IO;

namespace NFox.Pycad
{
    public class Extension : Package
    {

        public enum ExtensionType
        {
            Root,
            Extension,
            CompiledExtension
        }

        public ExtensionType Type { get; }

        public override string FullName
        {
            get { return Name; }
        }

        public override bool IsExtension { get { return true; } }

        public override string Path
        {
            get { return _path; }
        }

        //初始化所有项目
        public Extension(string name, DirectoryInfo dir) : base(name)
        {
            _path = dir.FullName;
            Type = ExtensionType.Root;
            foreach (var d in DirectoryEx.Extensions.GetDirectories())
            {
                if (!d.Name.Contains("."))
                    Add(new Extension(d));
            }
        }

        public DirectoryInfo DataDirectory
        {
            get
            {
                if (Type != ExtensionType.Root)
                    return Directory.GetDirectory("data");
                return null;
            }
        }

        public Extension(DirectoryInfo dir) : base(dir)
        {
            _path = dir.FullName;
            if (dir.GetFile(InitPyFileName) == null)
            {
                Type = ExtensionType.CompiledExtension;
            }
            else
            {
                Type = ExtensionType.Extension;
                for (int i = Packages.Count - 1; i > -1; i--)
                {
                    if (Packages[i].Name == "data")
                    {
                        Packages.RemoveAt(i);
                        break;
                    }
                }
            }
        }

        public void LoadCuixs(dynamic menus)
        {
            var cuixs = DataDirectory?.GetDirectory("cuixs");
            if (cuixs == null) return;
            string settings = cuixs.GetFile("settings.json")?.FullName;
            using (FileStream fs = new FileStream(settings, FileMode.Open))
            {
                using (var sr = new StreamReader(fs))
                using (JsonTextReader reader = new JsonTextReader(sr))
                {
                    foreach (JProperty cuix in JToken.ReadFrom(reader))
                    {
                        try { menus.Item(cuix.Name); }
                        catch
                        {
                            try
                            {
                                var file = cuixs.GetFile(((JValue)cuix.Value).Value as string);
                                if (file != null) menus.Load(file.FullName);
                            }
                            catch { }
                        }
                    }
                }
            }
        }

        public string FindFile(string filename)
        {
            return DataDirectory.GetFileFullName(filename);
        }

        public Extension GetExtension(string name)
        {
            if (name.Contains("."))
                name = name.Substring(0, name.IndexOf('.'));
            foreach (Extension p in Packages)
            {
                if (p.Name == name)
                    return p;
            }
            return null;
        }

        public override string ToString()
        {
            return $"Extension:({Path})";
        }

    }
}
