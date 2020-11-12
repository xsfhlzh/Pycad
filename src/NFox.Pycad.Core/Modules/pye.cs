using System;
using System.IO;
using System.Reflection;
using Microsoft.Win32;
using System.IO.Compression;
using System.Linq;
using Mono.Cecil;

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

        public static void runcmd(string extname, string name)
        {
            try
            {
                Application.Curr.SendMessage("BeforeCommand", name);
                GetFunc(extname, name).__call__();
            }
            finally
            {
                Application.Curr.SendMessage("AfterCommand", name);
            }
        }

        public static object invokelisp(string extname, string name, dynamic args)
        {
            try
            {
                Application.Curr.SendMessage("BeforeCommand", name);
                return GetFunc(extname, name).__call__(args);
            }
            catch
            {
                return null;
            }
            finally
            {
                Application.Curr.SendMessage("AfterCommand", name);
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
            var rpath = 
                Registry.ClassesRoot
                .OpenSubKey("*")?
                .OpenSubKey("shell")?
                .OpenSubKey("VSCode")?
                .GetValue("Icon")?
                .ToString();
            if (rpath != null && !File.Exists(rpath))
                rpath = null;
            pro.StartInfo.FileName = rpath ?? getvar("editor.path");
            pro.StartInfo.Arguments = $"\"{path}\\\"";
            pro.Start();
        } 

        public static void open_extension(string name)
        {
            var ext = extensions[name];
            if (ext != null)
                open(extensions[name].Path);
        }

        public static void create_extension(string name)
        {
            var dir = DirectoryEx.Extensions.CreateSubdirectory(name);
            var zipfile = DirectoryEx.Extensions.GetDirectory(".stubs").GetFileFullName("template.zip");
            using (FileStream fs = new FileStream(zipfile, FileMode.Open))
            using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
            {
                var ents = zip.Entries.OrderBy(e => e.FullName);
                foreach (var ent in zip.Entries.OrderBy(e => e.FullName))
                {
                    var fullname = ent.FullName;
                    if (fullname.EndsWith("/"))
                    {
                        dir.CreateSubdirectory(fullname);
                    }
                    else
                    {
                        using (var source = ent.Open())
                        using (var target = File.Create(dir.GetFileFullName(fullname)))
                        {
                            source.CopyTo(target);
                        }
                    }
                }
            }
            var ext = new Extension(dir);
            ext.Init(false);
            Engine.Extensions.Add(ext);
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
            return Utils.GetVariable<string>(name);
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
            get { return Version.Parse(Utils.GetVariable<string>("version")); }
        }

        public static void release(string packagename, Extension[] exts)
        {

            string name = packagename;
            int i = 2;
            while (DirectoryEx.Temp.GetFile($"{name}.Setup.exe") != null)
                name = $"{packagename}{i++}";
            name = $"{name}.Setup.exe";

            //修改安装程序,将包含主程序文件和插件的压缩流写入最终安装程序的资源
            var definition = AssemblyDefinition.ReadAssembly(DirectoryEx.Bin.GetFileFullName("NFox.Pycad.Setup.exe"));
            using (var rstream = Engine.Instance.GetReleaseStream(exts))
            using(var fs = File.Create(DirectoryEx.Bin.GetFileFullName("Release.zip")))
            {
                rstream.CopyTo(fs);
                rstream.Seek(0, SeekOrigin.Begin);
                var er = new EmbeddedResource("Release", ManifestResourceAttributes.Public, rstream);
                definition.MainModule.Resources.Add(er);
                definition.Write(DirectoryEx.Temp.GetFileFullName(name));
            }

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


