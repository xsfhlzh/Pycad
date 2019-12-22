using IronPython.Hosting;
using IronPython.Runtime.Exceptions;
using Microsoft.Scripting.Hosting;
using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Threading;
using System.Windows.Forms;
using System.Xml.Linq;
using System.Linq;
using System.Text.RegularExpressions;

namespace NFox.Pycad
{

    /// <summary>
    /// Pycad引擎
    /// </summary>
    public class Engine
    {

        #region Extensions

        public Extension Extensions { get; set; }

        private void ImportSpecModules(Extension p, string modules)
        {
            try
            {
                foreach (dynamic name in Execute($"{p.Name}.{modules}"))
                    TryImport($"{p.Name}.{name}");
            }
            catch { }
        }

        private void Regist(Extension ext)
        {

            if (ext.Type != Extension.ExtensionType.Extension)
                return;

            var filenames = new List<string>();
            ext.GetFileNames(filenames);

            var funcs =
                new Dictionary<string, List<dynamic>>
                {
                    { "command", new List<dynamic>() },
                    { "panel", new List<dynamic>() },
                    { "lisp", new List<dynamic>() },
                };
            var len = ext.Directory.FullName.Length;

            string content = null;
            Regex r = null;

            foreach (var path in filenames)
            {
                if (!path.EndsWith(".py"))
                    continue;
                using (StreamReader sr = new StreamReader(path))
                {
                    string modname = ext.Name + path.Substring(len, path.Length - len - 3);
                    modname = modname.Replace("\\", ".");
                    if (modname.EndsWith(".__init__"))
                        modname = modname.Substring(0, modname.Length - 9);
                    content = sr.ReadToEnd();
                    r = new Regex(@"(?:\n|^)@(command|lisp|panel)\((.*?)\)\s+(?:@.*?\s+)*(?:def|class)\s+(.*?)\s*[\(:]");
                    var ms = r.Matches(content);
                    foreach (Match m in ms)
                    {
                        funcs[m.Groups[1].Value].Add(
                            new
                            {
                                name = modname + "." + m.Groups[3].Value,
                                pars = m.Groups[2].Value.Replace('"', '\'')
                            });
                    }
                }
            }

            using (var sr = new StreamReader(ext.File.FullName))
                content = sr.ReadToEnd();

            r = new Regex(@"(?:\n|^)(commands|lisps|panels)\s*=\s*{(\s+(.*)\s*:\s*(.*))+\s*}");
            if (r.IsMatch(content))
                content = r.Replace(content, "");

            using (StreamWriter sw = new StreamWriter(ext.File.FullName, false, System.Text.Encoding.UTF8))
            {
                sw.Write(content);
                foreach (var kv in funcs)
                {
                    if (kv.Value.Count > 0)
                    {
                        sw.Write(kv.Key + "s = {\n");
                        foreach (var func in kv.Value)
                            sw.Write($"    \"{func.name}\": \"{func.pars}\",\n");
                        sw.Write("}\n");
                    }
                }
            }
        }

        public void LoadExtensions(bool loadfirst)
        {

            Extensions = new Extension("所有项目", DirectoryEx.Extensions);

            if (!loadfirst)
            {
                foreach (Extension ext in Extensions.Packages)
                    Regist(ext);
            }

            foreach (Extension p in Extensions.Packages)
            {
                if (p.Type == Extension.ExtensionType.CompiledExtension)
                {
                    if (File.Exists(p.Path))
                    {
                        var code = $"clr.AddReferenceToFileAndPath('{p.Path}/{p.Name}.dll')";
                        Execute(code.Replace("\\", "/"));
                    }
                }
                TryImport(p.Name);
            }
        }

        #endregion

        #region Script

        public Engine() { }

        public static Engine Instance { get; } = new Engine();

        ScriptEngine _engine;
        ScriptScope _scope;

        private void Load()
        {
            try
            {

                //生成py引擎
                var options = new Dictionary<string, object>();
                options["Frames"] = true;
                options["FullFrames"] = true;
                //options["Debug"] = true;
                //options["Tracing"] = true;
                _engine = Python.CreateEngine(AppDomain.CurrentDomain, options);

                //设置搜索目录
                var paths = _engine.GetSearchPaths();
                paths.Add(AppDomain.CurrentDomain.BaseDirectory);
                paths.Add(DirectoryEx.Bin.FullName);
                paths.Add(DirectoryEx.Support.FullName);
                paths.Add(DirectoryEx.PythonLib.FullName);
                paths.Add(DirectoryEx.Extensions.FullName);
                _engine.SetSearchPaths(paths);
                _scope = _engine.CreateScope();

                _values = new Dictionary<string, dynamic>();

                _loaded = true;

            }
            catch (Exception ex)
            {
                MessageBox.Show("Err:" + ex.Message);
            }

        }

        private bool _loaded;
        private void Unload()
        {
            foreach (Extension p in Extensions.Packages)
                ImportSpecModules(p, "unloads"); 
        }

        public void Restart()
        {
            if (_loaded) Unload();
            Load();
        }

        public void AddSearchPath(string path)
        {
            var paths = _engine.GetSearchPaths();
            paths.Add(path);
            _engine.SetSearchPaths(paths);
        }

        public void LoadAssembly(Assembly assem)
        {
            _engine.Runtime.LoadAssembly(assem);
        }

        #region Import

        public dynamic GetImportClass(string name)
        {
            Import(name);
            return Execute(name);
        }

        public void Import(string name)
        {
            Execute($"import {name}");
        }

        public void TryImport(string name)
        {
            Execute($"try: import {name}\nexcept: pass");
        }

        #endregion

        #region Values

        public Dictionary<string, Action> SystemCommands { get; }
            = new Dictionary<string, Action>();

        public void AddSystemCommand(string name, Action action)
        {
            SystemCommands[name] = action;
        }

        public dynamic GetVariable(string name)
        {
            return _scope.GetVariable(name);
        }

        public void SetVariable(string name, dynamic value)
        {
            _scope.SetVariable(name, value);
        }

        public void RemoveVariable(string name)
        {
            _scope.RemoveVariable(name);
        }

        private Dictionary<string, dynamic> _values;

        public dynamic GetValue(string name)
        {
            if (!_values.ContainsKey(name))
            {
                try
                {
                    _values[name] = Execute(name);
                }
                catch
                {
                    Import(name.Split('.')[0]);
                    _values[name] = Execute(name);
                }
            }
            return _values[name];
        }

        public class TempValue : IDisposable
        {

            static int _num = 0;
            string _name;
            Engine _engine;

            public TempValue(Engine engine, dynamic value)
            {
                _name = "Temp" + Interlocked.Increment(ref _num);
                _engine = engine;
                _engine.SetVariable(_name, value);
            }

            public void Dispose()
            {
                _engine.RemoveVariable(_name);
            }

            public override string ToString()
            {
                return _name;
            }

        }

        public TempValue NewTempValue(dynamic value)
        {
            return new TempValue(this, value);
        }

        #endregion

        #region Exec

        public dynamic Execute(string code)
        {
            ScriptSource script =
               _engine.CreateScriptSourceFromString(code);
            return script.Execute(_scope);
        }

        public dynamic Execute(string code, ScriptScope scope)
        {
            ScriptSource script =
               _engine.CreateScriptSourceFromString(code);
            return script.Execute(scope);
        }

        public dynamic TryExecute(string code)
        {

            try
            {
                ScriptSource script =
                   _engine.CreateScriptSourceFromString(code);
                return script.Execute(_scope);
            }
            catch { }
            return null;
        }

        public string GetStr(dynamic obj)
        {
            string s = "";
            if (obj != null)
            {
                if (obj is string)
                    s = $"'{obj}'";
                else
                    using (var value = NewTempValue(obj))
                        s = Execute($"str({value})");
            }
            return s;
        }

        public void SetTrace(TracebackDelegate func)
        {
            _engine.SetTrace(func);
        }

        public void TryReference(string dllname)
        {
            TryExecute($"import clr;clr.AddReference('{dllname}')");
        }

        public dynamic CreateScope()
        {
            return _engine.CreateScope();
        }

        public dynamic ExecuteFile(string path, bool createscope = false)
        {
            ScriptSource script =
               _engine.CreateScriptSourceFromFile(path);
            return script.Execute(createscope ? _engine.CreateScope() : _scope);
        }

        public dynamic ExecuteFile(string path, ScriptScope scope)
        {
            ScriptSource script =
               _engine.CreateScriptSourceFromFile(path);
            return script.Execute(scope);
        }

        #endregion

        #region Build

        public void Release(string name, List<Extension> extensions)
        {
            string path = $"{DirectoryEx.Temp.FullName}\\Release.zip";
            using (var target = new FileStream(path, FileMode.Create))
            {
                using (var zip = new ZipArchive(target, ZipArchiveMode.Update))
                {
                    using (var stream = zip.CreateEntry("Version").Open())
                    using (var sw = new StreamWriter(stream))
                        sw.Write($"{Application.GetVariable("version")}");
                    XElement xe = XElement.Load(DirectoryEx.Bin.GetFile("package.xml").FullName);
                    CopyFiles(xe, DirectoryEx.Root, zip);
                    foreach (var e in extensions)
                    {
                        using (var stream = zip.CreateEntry($"update\\extensions\\{e.Name}").Open())
                            Build(e.Name, stream);
                    }
                }
            }
        }

        private void CopyFiles(XElement xe, DirectoryInfo dir, ZipArchive zip)
        {
            foreach (var e in xe.Elements())
            {
                string name = e.Attribute("Name").Value;
                if (e.Name == "Directory")
                {
                    CopyFiles(e, dir.GetDirectory(name), zip);
                }
                else if (e.Name == "Plugin")
                {
                    var plugin = PluginBase.GetPlugin(e.Attribute("Name").Value);
                    using (var stream = zip.CreateEntry($"update\\plugins\\{e.Attribute("Name").Value}").Open())
                    {
                        using (var pzip = new ZipArchive(stream, ZipArchiveMode.Update))
                        {
                            var pdir = plugin.Info.Directory;
                            int len = pdir.FullName.Length;
                            foreach (var file in pdir.GetAllFiles())
                            {
                                using (var target = pzip.CreateEntry(file.FullName.Substring(len + 1)).Open())
                                {
                                    using (var source = file.OpenRead())
                                        source.CopyTo(target);
                                }
                            }
                        }
                    }

                }
                else
                {
                    if (e.Attribute("Build") != null && bool.Parse(e.Attribute("Build").Value))
                    {
                        using (var stream = zip.CreateEntry($"update\\{e.Attribute("Name").Value}").Open())
                            Build(name, stream);
                    }
                    else
                    {
                        using (var stream = zip.CreateEntry($"update\\{name}").Open())
                        {
                            var file = dir.GetFile(name);
                            using (FileStream source = file.OpenRead())
                                source.CopyTo(stream);
                        }
                    }
                }
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
            foreach(var sdir in dir.GetDirectories())
            {
                CopyAllDataFiles(sdir, zip, $"{path}{sdir.Name}\\");
            }
        }

        public void Build(string name, Stream stream)
        {

            var project = Extensions.GetExtension(name);
            if (project == null)
                project = new Extension(DirectoryEx.Support.GetDirectory(name));

            using (ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Update))
            {

                CopyAllDataFiles(project.DataDirectory, zip, "data\\");
                string targetpath = $"{DirectoryEx.Temp.FullName}\\{name}.dll";
                List<string> names = new List<string>();
                project.GetFileNames(names);
                var code = $"clr.CompileModules('{targetpath}',{string.Join(",", names.Select(s => $"'{s}'"))});";
                Execute(code.Replace("\\", "/"));
                var dllfile = new FileInfo(targetpath);
                using (var target = zip.CreateEntry($"{name}.dll").Open())
                {
                    using (var source = dllfile.OpenRead())
                        source.CopyTo(target);
                }
                dllfile.Delete();
            }

        }

        public void Build(string name, string path)
        {
            using (var fs = File.Create(Path.Combine(path, name + ".prj")))
                Build(name, fs);
        }

        #endregion

        #endregion

    }



}
