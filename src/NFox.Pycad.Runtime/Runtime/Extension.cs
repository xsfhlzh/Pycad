using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Text.RegularExpressions;

namespace NFox.Pycad
{
    public class Extension : Package
    {

        public bool Compiled { get; private set; }

        public Engine Engine { get; private set; }

        public override string FullName
        {
            get { return Name; }
        }

        public override bool IsExtension { get { return true; } }

        public override string Path
        {
            get { return _path; }
        }


        public dynamic Funcs { get; private set; }

        public DirectoryInfo CodeDirectory { get; }

        public DirectoryInfo DataDirectory { get; }

        public DirectoryInfo CuixDirectory { get; }

        public Extension(DirectoryInfo dir) : base(dir)
        {

            _path = dir.FullName;
            CodeDirectory = dir.GetDirectory("extension");
            DataDirectory = dir.GetDirectory("data");
            CuixDirectory = dir.GetDirectory("cuix");

        }

        public void Init(bool loadfirst)
        {

            Engine = new Engine();
            Engine.Restart();

            Engine.TryReference("pycad.dll");
            Engine.Execute($"import pycad.system;pycad.system.cext = '{Name}'");

            if (CodeDirectory == null)
            {
                Compiled = true;
                var code = $"import clr;clr.AddReferenceToFileAndPath('{Path}/extension.dll')";
                Engine.Execute(code.Replace("\\", "/"));
            }
            else
            {
                Compiled = false;
                Engine.AddSearchPath(Directory.FullName);
            }
            Engine.TryImport("extension");

            if (Compiled || loadfirst)
            {
                //从配置文件中获取
                var settings = Directory.GetFileFullName("funcs.json");
                if (settings != null)
                {
                    Dictionary<string, dynamic> dict = new Dictionary<string, dynamic>();
                    using (FileStream fs = new FileStream(settings, FileMode.Open))
                    {
                        using (var sr = new StreamReader(fs))
                        using (JsonTextReader reader = new JsonTextReader(sr))
                            Funcs = JToken.ReadFrom(reader);
                    }
                }
            }
            else
            {

                var filenames = new List<string>();
                GetFileNames(filenames);

                var funcs =
                    new Dictionary<string, List<dynamic>>
                    {
                        { "command", new List<dynamic>() },
                        { "panel", new List<dynamic>() },
                        { "lisp", new List<dynamic>() },
                    };
                var len = CodeDirectory.FullName.Length + 1;

                string content = null;
                Regex r = null;

                foreach (var path in filenames)
                {
                    if (!path.EndsWith(".py"))
                        continue;
                    using (StreamReader sr = new StreamReader(path))
                    {
                        string modulename = path.Substring(len, path.Length - len - 3);
                        modulename = modulename.Replace("\\", ".");
                        if (modulename == "__init__")
                            modulename = "";
                        else
                        {
                            if (modulename.EndsWith(".__init__"))
                                modulename = modulename.Substring(0, modulename.Length - 9);
                            modulename = "." + modulename;
                        }
                        content = sr.ReadToEnd();
                        r = new Regex(@"(?:\n|^)@(command|lisp|panel)\((.*?)\)\s+(?:@.*?\s+)*(?:def|class)\s+(.*?)\s*[\(:]");
                        var ms = r.Matches(content);
                        foreach (Match m in ms)
                        {
                            funcs[m.Groups[1].Value].Add(
                                new
                                {
                                    modulename = modulename,
                                    name = m.Groups[3].Value,
                                    pars = m.Groups[2].Value.Replace('"', '\'')
                                });
                        }
                    }
                }

                Funcs = new JObject();
                foreach (var items in funcs)
                {
                    JObject obj = new JObject();
                    foreach (var g in items.Value.GroupBy(i => i.modulename))
                    {
                        JObject gobj = new JObject();
                        foreach (var item in g)
                            gobj.Add(new JProperty(item.name, item.pars));
                        obj.Add(new JProperty(g.Key, gobj));
                    }
                    JProperty prop = new JProperty($"{items.Key}s", obj);
                    Funcs.Add(prop);
                }

                new Action(() =>
                {
                    var settings = Directory.GetFileFullName("funcs.json");
                    using (FileStream fs = new FileStream(settings, FileMode.Create))
                    {
                        using (StreamWriter sw = new StreamWriter(fs))
                        using (JsonTextWriter writer = new JsonTextWriter(sw))
                        {
                            writer.Formatting = Formatting.Indented;
                            Funcs.WriteTo(writer);
                        }
                    }
                }).BeginInvoke(null, null);
            }

            if (Application.CurrSystem != "acore")
            {
                new Action(() =>
                {
                    foreach (var cmds in Funcs)
                    {
                        foreach (var module in cmds.Value)
                            Engine.TryImport($"extension{module.Name}");
                    }
                }).BeginInvoke(null, null);
            }
        }

        public void CopyAllDataFiles(DirectoryInfo dir, ZipArchive zip, string path)
        {
            if (dir == null) return;
            foreach (var file in dir.GetFiles())
            {
                using (var target = zip.CreateEntry($"{path}{file.Name}").Open())
                {
                    using (var source = file.OpenRead())
                        source.CopyTo(target);
                }
            }
            foreach (var sdir in dir.GetDirectories())
            {
                CopyAllDataFiles(sdir, zip, $"{path}{sdir.Name}\\");
            }
        }

        public override void Build(Stream stream)
        {
            using (ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Update))
            {

                foreach (var file in Directory.GetFiles())
                {
                    using (var target = zip.CreateEntry(file.Name).Open())
                    {
                        using (var source = file.OpenRead())
                            source.CopyTo(target);
                    }
                }

                if (DataDirectory != null)
                    CopyAllDataFiles(DataDirectory, zip, "data\\");
                if (CuixDirectory != null)
                    CopyAllDataFiles(CuixDirectory, zip, "cuix\\");

                using (var target = zip.CreateEntry($"extension.dll").Open())
                    Packages["extension"].Build(target);

            }
        }

        public void CheckInfo()
        {
            string json = Directory.GetFileFullName("package.json");
            if (!System.IO.File.Exists(json))
                CreatePackageJson(json);
            json = Directory.CreateSubdirectory(".vscode").GetFileFullName("settings.json");
            if (!System.IO.File.Exists(json))
            {
                CreateSettingsJson(json);
            }
            else
            {
                JObject root = null;
                using (FileStream fs = new FileStream(json, FileMode.Open))
                {
                    using (var sr = new StreamReader(fs))
                    using (JsonTextReader reader = new JsonTextReader(sr))
                        root = JToken.ReadFrom(reader) as JObject;
                }

                var extra = root["python.autoComplete.extraPaths"] as JArray;
                if (!((string)extra[0]).StartsWith(DirectoryEx.Root.FullName))
                {
                    extra.Clear();
                    extra.Add(DirectoryEx.Root.GetDirectory("stubs").GetDirectory("pycadsys").FullName);
                    extra.Add(DirectoryEx.Root.GetDirectory("stubs").GetDirectory("clrclasses").FullName);
                    using (FileStream fs = new FileStream(json, FileMode.Create))
                    {
                        using (StreamWriter sw = new StreamWriter(fs))
                        using (JsonTextWriter writer = new JsonTextWriter(sw))
                        {
                            writer.Formatting = Formatting.Indented;
                            root.WriteTo(writer);
                        }
                    }
                }

            }
        }

        private void CreatePackageJson(string json)
        {
            using (FileStream fs = new FileStream(json, FileMode.Create))
            {
                using (StreamWriter sw = new StreamWriter(fs))
                using (JsonTextWriter writer = new JsonTextWriter(sw))
                {
                    writer.Formatting = Formatting.Indented;
                    JObject root = new JObject();
                    root.Add(new JProperty("name", Name));
                    root.Add(new JProperty("author", ""));
                    root.Add(new JProperty("dependencies", new JObject()));
                    root.WriteTo(writer);
                }
            }
        }

        private void CreateSettingsJson(string json)
        {
            using (FileStream fs = new FileStream(json, FileMode.Create))
            {
                using (StreamWriter sw = new StreamWriter(fs))
                using (JsonTextWriter writer = new JsonTextWriter(sw))
                {
                    writer.Formatting = Formatting.Indented;
                    JObject root = new JObject();
                    root.Add(new JProperty("python.pythonPath", "C:\\Program Files\\Python37\\python.exe"));
                    var arr = new JArray();
                    arr.Add(DirectoryEx.Root.GetDirectory("stubs").GetDirectory("pycadsys").FullName);
                    arr.Add(DirectoryEx.Root.GetDirectory("stubs").GetDirectory("clrclasses").FullName);
                    root.Add(new JProperty("python.autoComplete.extraPaths", arr));
                    root.Add(new JProperty("python.linting.enabled", true));
                    root.Add(new JProperty("terminal.integrated.shell.windows", "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"));
                    arr = new JArray();
                    arr.Add("../../bin/pyconsole.exe");
                    root.Add(new JProperty("terminal.integrated.shellArgs.windows", arr));
                    root.WriteTo(writer);
                }
            }
        }

        public void CreateInfo()
        {
            var json = Directory.GetFileFullName("package.json");
            CreatePackageJson(json);
            json = Directory.CreateSubdirectory(".vscode").GetFileFullName("settings.json");
            CreateSettingsJson(json);
        }

        public void LoadCuixs(dynamic menus)
        {
            if (CuixDirectory == null) return;
            string settings = CuixDirectory.GetFile("settings.json")?.FullName;
            if (settings != null)
            {
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
                                    var file = CuixDirectory.GetFile(((JValue)cuix.Value).Value as string);
                                    if (file != null) menus.Load(file.FullName);
                                }
                                catch { }
                            }
                        }
                    }
                }
            }
        }

        public string FindFile(string filename)
        {
            return DataDirectory.GetFileFullName(filename);
        }

        public override void GetFileNames(List<string> names)
        {
            Packages["extension"].GetFileNames(names);
        }


        public override string ToString()
        {
            return $"{Name}:({Path})";
        }

    }
}
