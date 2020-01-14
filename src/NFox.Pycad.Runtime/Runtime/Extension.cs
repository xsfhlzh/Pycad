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

                Funcs = 
                    new JObject(
                        new JProperty("commands", new JObject()),
                        new JProperty("lisps", new JObject()),
                        new JProperty("panels", new JObject()));

                var len = CodeDirectory.FullName.Length + 1;
                var filenames = new List<string>();
                GetFileNames(filenames);
                foreach (var path in filenames)
                {

                    if (!path.EndsWith(".py")) continue;
                    string modulename = path.Substring(len, path.Length - len - 3);
                    modulename = modulename.Replace("\\", ".");
                    if (modulename == "__init__")
                    {
                        modulename = "";
                    }
                    else
                    {
                        if (modulename.EndsWith(".__init__"))
                            modulename = modulename.Substring(0, modulename.Length - 9);
                        modulename = "." + modulename;
                    }

                    using (StreamReader sr = new StreamReader(path))
                    {
                        Regex r = new Regex(@"(?:\n|^)@(command|lisp|panel)\((.*?)\)\s+(?:@.*?\s+)*(?:def|class)\s+(.*?)\s*[\(:]");
                        var ms = r.Matches(sr.ReadToEnd());
                        foreach (Match m in ms)
                        {
                            var type = $"{m.Groups[1].Value}s";
                            var items = Funcs[type];
                            if (items[modulename] == null)
                                items.Add(new JProperty(modulename, new JObject()));
                            items[modulename].Add(
                                new JProperty(
                                    m.Groups[3].Value,
                                    m.Groups[2].Value.Replace('"', '\'')));
                        }
                    }
                }

                //保存命令到配置文件
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

            //预加载各模块以加快命令运行速度
            if (Application.CurrSystem != "acore")
            {
                new Action(() =>
                {
                    foreach (var items in Funcs)
                    {
                        foreach (var module in items.Value)
                            Engine.TryImport($"extension{module.Name}");
                    }
                }).BeginInvoke(null, null);
            }
        }

        private void CopyAllDataFiles(DirectoryInfo dir, ZipArchive zip, string path)
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
                    using (var source = file.OpenRead())
                    using (var target = zip.CreateEntry(file.Name).Open())
                        source.CopyTo(target);
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
            json = Directory.GetFileFullName("funcs.json");
            if (!System.IO.File.Exists(json))
                CreateFuncsJson(json);
            json = Directory.CreateSubdirectory(".vscode").GetFileFullName("settings.json");
            if (!System.IO.File.Exists(json))
                CreateSettingsJson(json);
        }

        private void CreateFuncsJson(string json)
        {
            using (FileStream fs = new FileStream(json, FileMode.Create))
            {
                using (StreamWriter sw = new StreamWriter(fs))
                using (JsonTextWriter writer = new JsonTextWriter(sw))
                {
                    writer.Formatting = Formatting.Indented;
                    JObject root =
                        new JObject
                        (
                            new JProperty("commands", new JObject()),
                            new JProperty("lisps", new JObject()),
                            new JProperty("panels", new JObject())
                        );
                    root.WriteTo(writer);
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
                    JObject root = 
                        new JObject
                        (
                            new JProperty("name", Name),
                            new JProperty("author", ""),
                            new JProperty("dependencies", new JObject())
                        );
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
                    JObject root =
                        new JObject
                        (
                            new JProperty(
                                "python.pythonPath", 
                                "C:\\Program Files\\Python37\\python.exe"),
                            new JProperty(
                                "python.autoComplete.extraPaths",
                                new JArray(
                                    "..\\.stubs\\pycadsys",
                                    "..\\.stubs\\clrclasses")),
                            new JProperty(
                                "python.linting.flake8Enabled",
                                true),
                            new JProperty(
                                "python.linting.flake8Args",
                                new JArray(
                                    "--ignore=E231,E262,E265,E401,E402,E501,E701,E704,E722,F403,F405,F811,W504",
                                    "--verbose")),
                            new JProperty(
                                "terminal.integrated.shell.windows", 
                                "powershell.exe"),
                            new JProperty(
                                "terminal.integrated.shellArgs.windows", 
                                new JArray("..\\..\\bin\\pyconsole.exe"))
                        );
                    root.WriteTo(writer);
                }
            }
        }

        public void CreateInfo()
        {
            var json = Directory.GetFileFullName("package.json");
            CreatePackageJson(json);
            json = Directory.GetFileFullName("funcs.json");
            CreateFuncsJson(json);
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
