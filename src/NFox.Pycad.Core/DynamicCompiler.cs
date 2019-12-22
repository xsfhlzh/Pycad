using Microsoft.CSharp;
using System.Linq;
using System.CodeDom;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.IO;
using System;

namespace NFox.Pycad
{
    public static class DynamicCompiler
    {

        public static List<string> Mgdlls { get; set; }

        #region SysCmds

        public static bool BuildSystemAssembly()
        {

            //动态编译系统命令集

            //声明代码的部分
            CodeCompileUnit compunit = new CodeCompileUnit();
            CodeNamespace ns = new CodeNamespace("NFox.Pycad");
            compunit.Namespaces.Add(ns);

            //引用命名空间
            ns.Imports.Add(new CodeNamespaceImport("System"));

            switch (Application.HostAppName)
            {
                case "acad":
                    ns.Imports.Add(new CodeNamespaceImport("Autodesk.AutoCAD.Runtime"));
                    break;
                case "gcad":
                    ns.Imports.Add(new CodeNamespaceImport("GrxCAD.Runtime"));
                    break;
            }

            //在命名空间下添加一个类
            CodeTypeDeclaration cmdsclass = new CodeTypeDeclaration("Commands");
            ns.Types.Add(cmdsclass);

            foreach (var cmd in Engine.Instance.SystemCommands)
                cmdsclass.Members.Add(BuildCmdMethod(cmd.Key));

            //生成驻留内存的动态程序集
            CompilerParameters pars = new CompilerParameters();
            pars.CompilerOptions = "/target:library /optimize";
            pars.GenerateExecutable = false;
            pars.GenerateInMemory = true;

            //添加引用
            var asslst = pars.ReferencedAssemblies;
            asslst.Add("System.dll");
            asslst.Add("System.Core.dll");
            asslst.Add("Microsoft.CSharp.dll");
            asslst.Add(DirectoryEx.Bin.GetFile("NFox.Pycad.Runtime.dll").FullName);
            asslst.Add(DirectoryEx.Plugins.GetFile("NFox.Pycad.Core", "NFox.Pycad.Core.dll").FullName);
            foreach (string name in Mgdlls)
                asslst.Add(name);

            //编译并加载
            CSharpCodeProvider cprovider = new CSharpCodeProvider();
            CompilerResults cr =
                cprovider.CompileAssemblyFromDom(pars, compunit);
            return cr.Errors.Count == 0;
        }

        private static CodeMemberMethod BuildCmdMethod(string name)
        {

            CodeMemberMethod method =
                new CodeMemberMethod { Name = name };

            //设置命令名
            var args = new List<CodeAttributeArgument>();
            args.Add(
                new CodeAttributeArgument(
                    new CodePrimitiveExpression(name)));
            method.CustomAttributes.Add(
                new CodeAttributeDeclaration(
                    "CommandMethod",
                    args.ToArray()));
            method.Attributes = MemberAttributes.Static | MemberAttributes.Public;

            method.Statements.Add(
                new CodeSnippetStatement(
                    $"NFox.Pycad.Core.Modules.pye.runsyscmd(\"{name}\");"));
            return method;

        }

        #endregion

        #region UserCmds

        private static int _tempIndex;

        private static List<string> _modules;

        public static bool BuildUserAssembly()
        {

            //声明代码的部分
            CodeCompileUnit ccu = new CodeCompileUnit();
            CodeNamespace ns = new CodeNamespace($"NFox.Pycad{_tempIndex++}");
            ccu.Namespaces.Add(ns);

            //引用命名空间
            ns.Imports.Add(new CodeNamespaceImport("System"));
            ns.Imports.Add(new CodeNamespaceImport("NFox.Pycad.Core"));

            switch (Application.HostAppName)
            {
                case "acad":
                    ns.Imports.Add(new CodeNamespaceImport("Autodesk.AutoCAD.Runtime"));
                    ns.Imports.Add(new CodeNamespaceImport("Autodesk.AutoCAD.DatabaseServices"));
                    break;
                case "gcad":
                    ns.Imports.Add(new CodeNamespaceImport("GrxCAD.Runtime"));
                    ns.Imports.Add(new CodeNamespaceImport("GrxCAD.DatabaseServices"));
                    break;
            }

            //在命名空间下添加一个类
            CodeTypeDeclaration cmdsclass = new CodeTypeDeclaration("Commands");
            ns.Types.Add(cmdsclass);
            
            var prjnames = 
                Engine.Instance.Extensions.Packages
                .Select(p => p.Name)
                .ToList();
            prjnames.Add("pycad");

            int i = 0;
            _modules = new List<string>();
            foreach (string name in prjnames)
            {
                foreach (dynamic cmd in GetItems(name, "commands").items())
                     cmdsclass.Members.Add(BuildCmdMethod(cmd, "command", i++));
                foreach (dynamic cmd in GetItems(name, "panels").items())
                    cmdsclass.Members.Add(BuildCmdMethod(cmd, "panel", i++));
                foreach (dynamic lisp in GetItems(name, "lisps").items())
                    cmdsclass.Members.Add(BuildLispMethod(lisp, i++));
            }

            if (Application.CurrSystem != "acore")
            {
                new Action(() =>
                {
                    foreach (var name in _modules.Distinct())
                        Engine.Instance.TryImport(name);
                }).BeginInvoke(null, null);
            }

            //生成驻留内存的动态程序集
            CompilerParameters pars = new CompilerParameters();
            pars.CompilerOptions = "/target:library /optimize";
            pars.GenerateExecutable = false;
            pars.GenerateInMemory = true;

            //添加引用
            var asslst = pars.ReferencedAssemblies;
            asslst.Add("System.dll");
            asslst.Add("System.Core.dll");
            asslst.Add("Microsoft.CSharp.dll");
            asslst.Add(DirectoryEx.Plugins.GetFile("NFox.Pycad.Core", "NFox.Pycad.Core.dll").FullName);
            foreach (string name in Mgdlls)
                asslst.Add(name);

            //编译并加载
            CSharpCodeProvider cprovider = new CSharpCodeProvider();
            CompilerResults cr =
                cprovider.CompileAssemblyFromDom(pars, ccu);
            return cr.Errors.Count == 0;

        }

        private static dynamic GetItems(string prjname, string type)
        {
            try { return Engine.Instance.Execute($"{prjname}.{type}"); }
            catch { return new IronPython.Runtime.PythonDictionary(); }
        }

        private static CodeMemberMethod BuildCmdMethod(dynamic cmd, string type, int index)
        {

            CodeMemberMethod method =
                new CodeMemberMethod { Name = $"Cmd_{index}" };
            var args = new List<CodeAttributeArgument>();

            dynamic instance = Engine.Instance.Execute($"{type}({cmd[1]})");

            string name = cmd[0];
            if (instance.name == null)
                instance.name = name.Substring(name.LastIndexOf(".") + 1);
            _modules.Add(name.Substring(0, name.LastIndexOf(".")));

            if ((int)instance.flags != 0)
                args.Add(
                    new CodeAttributeArgument(
                        new CodeCastExpression(
                            "CommandFlags",
                            new CodePrimitiveExpression((int)instance.flags))));

            //设置命令名
            args.Insert(0,
                new CodeAttributeArgument(
                    new CodePrimitiveExpression(instance.name)));
            method.CustomAttributes.Add(
                new CodeAttributeDeclaration(
                    "CommandMethod",
                    args.ToArray()));
            method.Attributes = MemberAttributes.Static | MemberAttributes.Public;

            method.Statements.Add(
                new CodeSnippetStatement(
                    $"NFox.Pycad.Core.Modules.pye.runcmd(\"{cmd[0]}\");"));
            return method;

        }

        private static CodeMemberMethod BuildLispMethod(dynamic lisp, int index)
        {

            CodeMemberMethod method =
                new CodeMemberMethod { Name = $"Lisp_{index}" };
            var args = new List<CodeAttributeArgument>();

            dynamic instance = Engine.Instance.Execute($"lisp({lisp[1]})");
            string name = lisp[0];
            if (instance.name == null)
                instance.name = name.Substring(name.LastIndexOf(".") + 1);
            _modules.Add(name.Substring(0, name.LastIndexOf(".")));

            //设置命令名
            args.Add(
                new CodeAttributeArgument(
                    new CodePrimitiveExpression(instance.name)));
            method.CustomAttributes.Add(
                new CodeAttributeDeclaration(
                    "LispFunction",
                    args.ToArray()));
            method.Attributes = MemberAttributes.Static | MemberAttributes.Public;
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "ResultBuffer", "rb"));
            method.ReturnType = new CodeTypeReference("Object");

            method.Statements.Add(
                new CodeSnippetStatement(
                    $"return NFox.Pycad.Core.Modules.pye.invokelisp(\"{lisp[0]}\", rb);"));
            return method;

        }

        #endregion

        # region Release

        public static bool BuildReleaseAssembly(string dllpath)
        {

            string releasepath = $"{DirectoryEx.Temp.FullName}\\Release.zip";

            //动态编译安装程序集
            CompilerParameters pars = new CompilerParameters();
            pars.EmbeddedResources.Add(releasepath);
            pars.GenerateExecutable = false;
            pars.GenerateInMemory = false;
            pars.OutputAssembly = dllpath;

            //声明代码的部分
            CodeCompileUnit compunit = new CodeCompileUnit();

            CodeNamespace ns = new CodeNamespace("NFox.Pycad.Setup");
            compunit.Namespaces.Add(ns);

            //引用命名空间
            ns.Imports.Add(new CodeNamespaceImport("Autodesk.AutoCAD.Runtime"));
            ns.Imports.Add(new CodeNamespaceImport("System"));
            ns.Imports.Add(new CodeNamespaceImport("System.Collections.Generic"));
            ns.Imports.Add(new CodeNamespaceImport("System.IO"));
            ns.Imports.Add(new CodeNamespaceImport("System.IO.Compression"));
            ns.Imports.Add(new CodeNamespaceImport("System.Reflection"));
            ns.Imports.Add(new CodeNamespaceImport("System.Xml.Linq"));

            //设置程序集特性
            compunit.AssemblyCustomAttributes.Add(
                new CodeAttributeDeclaration(
                    "Autodesk.AutoCAD.Runtime.ExtensionApplication",
                    new CodeAttributeArgument(
                        new CodeTypeOfExpression("NFox.Pycad.Setup.Application"))));

            //在命名空间下添加一个类
            CodeTypeDeclaration appclass = new CodeTypeDeclaration("Application");
            ns.Types.Add(appclass);
            appclass.BaseTypes.Add(new CodeTypeReference("IExtensionApplication"));

            //函数Initialize
            CodeMemberMethod method =
                new CodeMemberMethod { Name = "Initialize" };
            method.Attributes = MemberAttributes.Public;
            appclass.Members.Add(method);

            method.Statements.Add(
                new CodeVariableDeclarationStatement("String", "mainpath"));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "Assembly", "ass",
                    new CodeSnippetExpression("Assembly.GetExecutingAssembly()")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "String", "resname",
                    new CodeSnippetExpression("ass.GetManifestResourceNames()[0]")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "Stream", "stream",
                    new CodeSnippetExpression("ass.GetManifestResourceStream(resname)")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "ZipArchive", "zip",
                    new CodeSnippetExpression("new ZipArchive(stream, ZipArchiveMode.Read)")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "Stream", "cstream",
                    new CodeSnippetExpression("zip.GetEntry(\"Version\").Open()")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "StreamReader", "sr",
                    new CodeSnippetExpression("new StreamReader(cstream)")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "Version", "newver",
                    new CodeSnippetExpression("Version.Parse(sr.ReadToEnd())")));
            method.Statements.Add(
                new CodeSnippetStatement("sr.Dispose();"));
            method.Statements.Add(
                new CodeSnippetStatement("cstream.Dispose();"));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "RegistryKey", "rk",
                    new CodeSnippetExpression("Registry.CurrentUser.OpenSubKey(\"Software\", Microsoft.Win32.RegistryKeyPermissionCheck.ReadWriteSubTree)")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "RegistryKey", "nfoxrk",
                    new CodeSnippetExpression("rk.OpenSubKey(\"NFox\")")));
            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "RegistryKey", "pycadrk",
                    new CodeSnippetExpression("rk.CreateSubKey(\"NFox\").CreateSubKey(\"Pycad\")")));

            var ifstat =
                new CodeConditionStatement(
                    new CodeSnippetExpression("nfoxrk == null || nfoxrk.OpenSubKey(\"Pycad\") == null"));
            method.Statements.Add(ifstat);

            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("pycadrk.SetValue(\"Version\", newver.ToString());"));
            ifstat.TrueStatements.Add(
                new CodeVariableDeclarationStatement(
                    "String", "path",
                    new CodeSnippetExpression("\"C:\\\\Program Files\\\\Pycad\"")));
            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("mainpath = path;"));

            ifstat.TrueStatements.Add(
                new CodeIterationStatement(
                    new CodeVariableDeclarationStatement(
                        "Int32", "i",
                        new CodeSnippetExpression("2")),
                    new CodeSnippetExpression("Directory.Exists(mainpath)"),
                    new CodeSnippetStatement("i++"),
                    new CodeSnippetStatement("mainpath = path + i;")));
            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("pycadrk.SetValue(\"MainPath\", mainpath);"));
            ifstat.TrueStatements.Add(
                new CodeVariableDeclarationStatement(
                    "DirectoryInfo", "dir",
                    new CodeSnippetExpression("Directory.CreateDirectory(mainpath)")));
            ifstat.TrueStatements.Add(
                new CodeVariableDeclarationStatement(
                    "Stream", "pstream",
                    new CodeSnippetExpression("zip.GetEntry(\"Update\\\\Package.xml\").Open()")));
            ifstat.TrueStatements.Add(
                new CodeVariableDeclarationStatement(
                    "XElement", "xe",
                    new CodeSnippetExpression("XElement.Load(pstream);")));
            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("pstream.Dispose();"));
            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("CopyFiles(xe, dir, zip);"));

            ifstat.TrueStatements.Add(
                new CodeIterationStatement(
                    new CodeVariableDeclarationStatement(
                        "IEnumerator<ZipArchiveEntry>", "itor",
                        new CodeSnippetExpression("zip.Entries.GetEnumerator()")),
                    new CodeSnippetExpression("itor.MoveNext()"),
                    new CodeSnippetStatement(""),
                    new CodeSnippetStatement("ZipArchiveEntry ent = itor.Current;"),
                    new CodeConditionStatement(
                        new CodeSnippetExpression("ent.FullName.StartsWith(\"Update\\\\Projects\")"),
                        new CodeSnippetStatement("Copy(ent, mainpath + \"\\\\\" + ent.FullName);"))));

            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("Assembly.LoadFrom(mainpath+ \"\\\\NFox.Pycad.dll\");"));

            ifstat.FalseStatements.Add(
                new CodeVariableDeclarationStatement(
                    "Version", "oldver",
                    new CodeSnippetExpression("Version.Parse(pycadrk.GetValue(\"Version\").ToString())")));
            ifstat.FalseStatements.Add(
                new CodeSnippetStatement("mainpath = pycadrk.GetValue(\"MainPath\").ToString();"));

            var ifstat2 =
                new CodeConditionStatement(
                    new CodeSnippetExpression("newver > oldver"));
            ifstat.FalseStatements.Add(ifstat2);

            ifstat2.TrueStatements.Add(
                new CodeIterationStatement(
                    new CodeVariableDeclarationStatement(
                        "IEnumerator<ZipArchiveEntry>", "itor",
                        new CodeSnippetExpression("zip.Entries.GetEnumerator()")),
                    new CodeSnippetExpression("itor.MoveNext()"),
                    new CodeSnippetStatement(""),
                    new CodeSnippetStatement("ZipArchiveEntry ent = itor.Current;"),
                    new CodeSnippetStatement("Copy(ent, mainpath + \"\\\\\" + ent.FullName);")));

            ifstat2.FalseStatements.Add(
                new CodeIterationStatement(
                    new CodeVariableDeclarationStatement(
                        "IEnumerator<ZipArchiveEntry>", "itor",
                        new CodeSnippetExpression("zip.Entries.GetEnumerator()")),
                    new CodeSnippetExpression("itor.MoveNext()"),
                    new CodeSnippetStatement(""),
                    new CodeSnippetStatement("ZipArchiveEntry ent = itor.Current;"),
                    new CodeConditionStatement(
                        new CodeSnippetExpression("ent.FullName.StartsWith(\"Update\\\\Projects\")"),
                        new CodeSnippetStatement("Copy(ent, mainpath + \"\\\\\" + ent.FullName);"))));

            method.Statements.Add(
                new CodeSnippetStatement("pycadrk.Dispose();"));
            method.Statements.Add(
                new CodeSnippetStatement("nfoxrk.Dispose();"));
            method.Statements.Add(
                new CodeSnippetStatement("rk.Dispose();"));
            method.Statements.Add(
                new CodeSnippetStatement("zip.Dispose();"));
            method.Statements.Add(
                new CodeSnippetStatement("stream.Dispose();"));

            //函数Terminate
            method =
                new CodeMemberMethod { Name = "Terminate" };
            method.Attributes = MemberAttributes.Public;
            appclass.Members.Add(method);

            //函数Copy
            method =
                new CodeMemberMethod { Name = "Copy" };
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "ZipArchiveEntry", "ent"));
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "String", "path"));
            method.Attributes = MemberAttributes.Private;
            appclass.Members.Add(method);

            method.Statements.Add(
                new CodeSnippetStatement("Stream source = ent.Open();"));
            method.Statements.Add(
                new CodeSnippetStatement("Stream target = File.OpenWrite(path);"));
            method.Statements.Add(
                new CodeSnippetStatement("source.CopyTo(target);"));
            method.Statements.Add(
                new CodeSnippetStatement("target.Dispose();"));
            method.Statements.Add(
                new CodeSnippetStatement("source.Dispose();"));

            //函数UnzipDllx
            method =
                new CodeMemberMethod { Name = "UnzipDllx" };
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "Stream", "stream"));
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "DirectoryInfo", "dir"));
            method.Attributes = MemberAttributes.Private;
            appclass.Members.Add(method);

            method.Statements.Add(
                new CodeVariableDeclarationStatement(
                    "ZipArchive", "zip",
                    new CodeSnippetExpression("new ZipArchive(stream, ZipArchiveMode.Read)")));
            method.Statements.Add(
                new CodeIterationStatement(
                    new CodeVariableDeclarationStatement(
                        "IEnumerator<ZipArchiveEntry>", "it",
                        new CodeSnippetExpression("zip.Entries.GetEnumerator()")),
                    new CodeSnippetExpression("it.MoveNext()"),
                    new CodeSnippetStatement(""),
                    new CodeSnippetStatement("ZipArchiveEntry ent = it.Current;"),
                    new CodeSnippetStatement("string path = dir.FullName + \"\\\\\" + ent.FullName;"),
                    new CodeSnippetStatement("string ddir = Path.GetDirectoryName(path);"),
                    new CodeConditionStatement(
                        new CodeSnippetExpression("!Directory.Exists(ddir)"),
                        new CodeSnippetStatement("Directory.CreateDirectory(ddir);")),
                    new CodeSnippetStatement("Stream source = ent.Open();"),
                    new CodeSnippetStatement("Stream target = File.Open(path, FileMode.Create);"),
                    new CodeSnippetStatement("source.CopyTo(target);"),
                    new CodeSnippetStatement("target.Dispose();"),
                    new CodeSnippetStatement("source.Dispose();")));
            method.Statements.Add(
                new CodeSnippetStatement("zip.Dispose();"));

            //函数CopyFiles
            method =
                new CodeMemberMethod { Name = "CopyFiles" };
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "XElement", "xe"));
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "DirectoryInfo", "dir"));
            method.Parameters.Add(
                new CodeParameterDeclarationExpression(
                    "ZipArchive", "zip"));
            method.Attributes = MemberAttributes.Private;
            appclass.Members.Add(method);

            var forstat =
                new CodeIterationStatement();
            method.Statements.Add(forstat);

            forstat.InitStatement =
                new CodeVariableDeclarationStatement(
                    "IEnumerator<XElement>", "it",
                    new CodeSnippetExpression("xe.Elements().GetEnumerator()"));
            forstat.TestExpression =
                new CodeSnippetExpression("it.MoveNext()");
            forstat.IncrementStatement =
                new CodeSnippetStatement("");
            forstat.Statements.Add(
                 new CodeVariableDeclarationStatement(
                    "XElement", "e",
                    new CodeSnippetExpression("it.Current")));

            ifstat = 
                new CodeConditionStatement(
                    new CodeSnippetExpression("e.Name.LocalName == \"Directory\""));
            forstat.Statements.Add(ifstat);

            ifstat.TrueStatements.Add(
                new CodeVariableDeclarationStatement(
                    "DirectoryInfo", "sdir",
                    new CodeSnippetExpression("dir.CreateSubdirectory(e.Attribute(\"Name\").Value)")));
            ifstat.TrueStatements.Add(
                new CodeSnippetStatement("CopyFiles(e, sdir, zip);"));

            ifstat2 = 
                new CodeConditionStatement(
                    new CodeSnippetExpression("e.Name.LocalName == \"Plugin\""));
            ifstat.FalseStatements.Add(ifstat2);

            //TODO
            //ifstat2.TrueStatements.Add(
                
            //    )

            ifstat2.FalseStatements.Add(
                new CodeVariableDeclarationStatement(
                    "String", "name",
                    new CodeSnippetExpression("e.Attribute(\"Name\").Value")));

            var forstat2 =
                new CodeIterationStatement(
                    new CodeVariableDeclarationStatement(
                        "IEnumerator<ZipArchiveEntry>", "itor",
                        new CodeSnippetExpression("zip.Entries.GetEnumerator()")),
                    new CodeSnippetExpression("itor.MoveNext()"),
                    new CodeSnippetStatement(""),
                    new CodeSnippetStatement("ZipArchiveEntry ent = itor.Current;"));
            ifstat2.FalseStatements.Add(forstat2);

            var ifstat3 =
                new CodeConditionStatement(
                    new CodeSnippetExpression("ent.Name == name"));
            forstat2.Statements.Add(ifstat3);

            ifstat3.TrueStatements.Add(
                new CodeVariableDeclarationStatement(
                    "Stream", "source",
                    new CodeSnippetExpression("ent.Open()")));

            var ifstat4 =
                new CodeConditionStatement(
                    new CodeSnippetExpression("e.Attribute(\"Build\") != null && Boolean.Parse(e.Attribute(\"Build\").Value)"));
            ifstat3.TrueStatements.Add(ifstat4);

            ifstat4.TrueStatements.Add(
                new CodeSnippetStatement("UnzipDllx(source, dir);"));
            ifstat4.FalseStatements.Add(
                new CodeVariableDeclarationStatement(
                    "Stream", "target",
                    new CodeSnippetExpression("File.Open(dir.FullName + \"\\\\\" + name, FileMode.Create)")));
            ifstat4.FalseStatements.Add(
                new CodeSnippetStatement("source.CopyTo(target);"));
            ifstat4.FalseStatements.Add(
                new CodeSnippetStatement("target.Dispose();"));

            ifstat3.TrueStatements.Add(
                new CodeSnippetStatement("source.Dispose();"));
            ifstat3.TrueStatements.Add(
                new CodeSnippetStatement("break;"));

            //添加引用
            var asslst = pars.ReferencedAssemblies;
            asslst.Add("System.dll");
            asslst.Add("System.Core.dll");
            asslst.Add("Microsoft.CSharp.dll");
            asslst.Add("System.Xml.dll");
            asslst.Add("System.Xml.Linq.dll");
            asslst.Add("System.IO.Compression.dll");
            foreach (string name in Mgdlls)
                asslst.Add(name);

            //编译并加载
            CSharpCodeProvider cprovider = new CSharpCodeProvider();
            CompilerResults cr =
                cprovider.CompileAssemblyFromDom(pars, compunit);
            File.Delete(releasepath);
            return cr.Errors.Count == 0;
        }

    #endregion

    }

}
