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
using System.Threading.Tasks;

namespace NFox.Pycad
{

    /// <summary>
    /// Pycad引擎
    /// </summary>
    public class Engine
    {

        #region Extensions

        public static ExtensionCollection Extensions { get; set; }

        public static Package Support { get; set; }

        public static List<Assembly> Assemblies { get; set; }

        public static void LoadExtensions(bool loadfirst)
        {
            Extensions = new ExtensionCollection("所有项目");
            Support = new Package(DirectoryEx.Support, true);
            foreach (var ext in Extensions)
                try { ext.Init(loadfirst); }
                catch { }
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
                _engine.SetSearchPaths(paths);
                _scope = _engine.CreateScope();

                foreach(var assem in Assemblies)
                    _engine.Runtime.LoadAssembly(assem);

                _values = new Dictionary<string, dynamic>();

                _loaded = true;

            }
            catch (Exception ex)
            {
                MessageBox.Show("Err:" + ex.Message);
            }

        }

        public ScriptScope CreateScope()
        {
            return _engine.CreateScope();
        }

        private bool _loaded;
        private void Unload()
        {
            foreach (Extension p in Extensions)
                TryImport($"{p.Name}.unloads"); 
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

        public void AddBuiltin(string name, object value)
        {
            var builtin = _engine.GetBuiltinModule();
            builtin.SetVariable(name, value);
        }

        public void LoadAssembly(Assembly assem)
        {
            _engine.Runtime.LoadAssembly(assem);
        }

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
            if(obj == null)
            {
                return "";
            }
            else
            {
                if (obj is string)
                    return $"'{obj}'";
                else
                    using (var value = NewTempValue(obj))
                        return Execute($"str({value})");
            }
        }

        public void SetTrace(TracebackDelegate func)
        {
            foreach (var ext in Extensions)
            {
                if (ext.Engine != null)
                    ext.Engine._engine.SetTrace(func);
            }
        }

        public void TryReference(string dllname)
        {
            TryExecute($"import clr;clr.AddReference('{dllname}')");
        }

        public dynamic ExecuteFile(string path)
        {
            ScriptSource script =
               _engine.CreateScriptSourceFromFile(path);
            return script.Execute(_scope);
        }

        #endregion

        #region Build
        
        public void Release(IEnumerable<Extension> extensions)
        {
            string path = $"{DirectoryEx.Temp.FullName}\\Release.zip";
            using (var target = new FileStream(path, FileMode.Create))
            {
                using (var zip = new ZipArchive(target, ZipArchiveMode.Update))
                {
                    using (var stream = zip.CreateEntry("Version").Open())
                    using (var sw = new StreamWriter(stream))
                        sw.Write($"{Utils.GetVariable<string>("version")}");
                    XElement xe = XElement.Load(DirectoryEx.Bin.GetFile("package.xml").FullName);
                    CopyFiles(xe, DirectoryEx.Root, zip);
                    foreach (var e in extensions)
                    {
                        if (e.Name != "pycad")
                        {
                            using (var stream = zip.CreateEntry($"extensions\\{e.Name}").Open())
                                e.Build(stream);
                        }
                    }
                }
            }
        }

        private void CopyFiles(XElement xe, DirectoryInfo dir, ZipArchive zip)
        {
            foreach (var e in xe.Elements())
            {
                string name = e.Attribute("Name").Value;
                switch (e.Name.LocalName)
                {
                    case "Directory":
                        CopyFiles(e, dir.GetDirectory(name), zip);
                        break;
                    case "Plugin":
                        var plugin = PluginBase.GetPlugin(name);
                        using (var stream = zip.CreateEntry(name).Open())
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
                        break;
                    case "Module":
                        using (var stream = zip.CreateEntry($"{name}.dll").Open())
                            Support.Packages[name].Build(stream);
                        break;
                    case "Extension":
                        using (var stream = zip.CreateEntry($"extensions\\{name}").Open())
                            Extensions[name].Build(stream);
                        break;
                    case "File":
                        using (var stream = zip.CreateEntry(name).Open())
                        {
                            var file = dir.GetFile(name);
                            using (FileStream source = file.OpenRead())
                                source.CopyTo(stream);
                        }
                        break;
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

        #endregion

        #endregion

    }



}
