using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace NFox.Pycad.Core.Modules
{

    /// <summary>
    /// Pycad引擎
    /// </summary>
    public static class pye
    {

        private static dynamic GetFunc(string prjname, string name)
        {
            int index = name.LastIndexOf('.');
            string modname = name.Substring(0, index);
            var ext = Engine.Extensions[prjname];
            ext.Engine.Import(modname);
            return ext.Engine.Execute(name);
        }

        public static void runsyscmd(string name)
        {
            Engine.Instance.SystemCommands[name]();
        }

        public static void runcmd(string prjname, string name)
        {
            try
            {
                Application.Curr.SendMessage("BeforeCommand");
                GetFunc(prjname, name).__call__();
            }
            finally
            {
                Application.Curr.SendMessage("AfterCommand");
            }
        }

        public static object invokelisp(string prjname, string name, dynamic args)
        {
            try
            {
                Application.Curr.SendMessage("BeforeCommand");
                return GetFunc(prjname, name).__call__(args);
            }
            catch
            {
                return null;
            }
            finally
            {
                Application.Curr.SendMessage("AfterCommand");
            }
        }

        public static ExtensionCollection extensions
        {
            get { return Engine.Extensions; }
        }

        public static Package supportmodules
        {
            get { return Engine.Support; }
        }

        private static void open(string path)
        {
            var pro = new System.Diagnostics.Process();
            pro.EnableRaisingEvents = false;
            pro.StartInfo.FileName = getvar("editor.path");
            pro.StartInfo.Arguments = $"\"{path}\\\"";
            pro.Start();
        } 

        public static void open_extension(string name)
        {
            var ext = extensions[name];
            if (ext != null)
            {
                ext.CheckInfo();
                open(extensions[name].Path);
            }
        }

        public static void create_extension(string name)
        {
            var dir = DirectoryEx.Extensions.CreateSubdirectory(name);
            var extdir = dir.CreateSubdirectory("extension");
            var file = File.Create(extdir.GetFileFullName("__init__.py"));
            file.Close();
            dir.CreateSubdirectory("data");
            dir.CreateSubdirectory("cuix");
            var ext = new Extension(dir);
            ext.Init(false);
            Engine.Extensions.Add(ext);
            ext.CreateInfo();
            open_extension(name);
        }

        public static void open_support()
        {
            open(DirectoryEx.Support.FullName);
        }

        public static void create_supportmodule(string name)
        {
            var dir = DirectoryEx.Support.CreateSubdirectory(name);
            var file = File.Create(dir.GetFileFullName("__init__.py"));
            Engine.Support.Add(new Package(dir));
            open_support();
        }

        public static dynamic getvar(string name)
        {
            return Application.GetVariable(name);
        }

        private static dynamic _tempvalue;

        public static void settempvalue(dynamic value)
        {
            _tempvalue = value;
        }

        public static dynamic gettempvalue()
        {
            return _tempvalue;
        }

        public static dynamic execute(string code)
        {
            return Engine.Instance.Execute(code);
        }

        public static void executefile(string path)
        {
            Engine.Instance.ExecuteFile(path);
        }

        public static string findfile(string modulename, string filename)
        {
            return Engine.Extensions[modulename].FindFile(filename);
        }

        public static string location
        {
            get { return DirectoryEx.Location.FullName; }
        }

        public static string mainpath
        {
            get { return DirectoryEx.Root.FullName; }
        }

        public static string libpath
        {
            get { return DirectoryEx.Bin.FullName; }
        }

        public static string supportpath
        {
            get { return DirectoryEx.Support.FullName; }
        }

        public static string extensionspath
        {
            get { return DirectoryEx.Extensions.FullName; }
        }

        public static Version version
        {
            get { return Application.Version; }
        }

        public static void release(string packagename, Extension[] exts)
        {
            Engine.Instance.Release(exts);
            string name = packagename;
            int i = 2;
            while(DirectoryEx.Temp.GetFile(name + ".Setup.dll") != null)
                name = packagename + i++;
            DynamicCompiler.BuildReleaseAssembly($"{DirectoryEx.Temp.FullName}\\{name}.Setup.dll");
        }

        public static void build_extension(string name)
        {
            var ext = Engine.Extensions[name];
            if (ext == null || ext.Compiled)
                ext = new Extension(DirectoryEx.Extensions.GetDirectory(name));
            using (var fs = File.Create(Path.Combine(DirectoryEx.Temp.FullName, name + ".ext")))
                ext.Build(fs);
        }

        public static void build_module(string name)
        {
            Engine.Support.Packages[name].Build();
        }

        public static void reference(string filename)
        {
            var ass = Assembly.LoadFile(filename);
            foreach (var type in ass.GetExportedTypes())
                new RefTypes.Type(type);
            RefTypes.Namespace.SaveAll();
            io.instance?.write($"\n{ass.FullName}解析完成!");
        }

    }

}


