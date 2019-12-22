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

        private static dynamic GetFunc(string name)
        {
            int index = name.LastIndexOf('.');
            string modname = name.Substring(0, index);
            Engine.Instance.Import(modname);
            return Engine.Instance.Execute(name);
        }

        public static void runsyscmd(string name)
        {
            Engine.Instance.SystemCommands[name]();
        }

        public static void runcmd(string name)
        {
            try
            {
                Application.Curr.SendMessage("BeforeCommand");
                GetFunc(name).__call__();
            }
            catch { }
            finally
            {
                Application.Curr.SendMessage("AfterCommand");
            }
        }

        public static object invokelisp(string name, dynamic args)
        {
            try
            {
                Application.Curr.SendMessage("BeforeCommand");
                return GetFunc(name).__call__(args);
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
            Engine.Instance.ExecuteFile(path, true);
        }

        public static string findfile(string modulename, string filename)
        {
            if (modulename.Contains("."))
                modulename = modulename.Substring(0, modulename.IndexOf('.'));
            return Engine.Instance.Extensions.GetExtension(modulename).FindFile(filename);
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

        public static void install(string extfile)
        {

        }

        public static Version version
        {
            get { return Application.Version; }
        }

        public static void release(dynamic module)
        {
            string name = module.__name__;
            Extension e = Engine.Instance.Extensions.GetExtension(name);
            Engine.Instance.Release(name, new List<Extension> { e });
            DynamicCompiler.BuildReleaseAssembly($"{DirectoryEx.Temp.FullName}\\{name}.Setup.dll");
        }

        public static void build(dynamic module)
        {
            string name = module.__name__;
            var path = DirectoryEx.Temp.FullName;
            Engine.Instance.Build(name, path);
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


