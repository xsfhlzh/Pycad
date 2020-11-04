using Microsoft.CSharp;
using System.Linq;
using System.CodeDom;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.IO;

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
                Engine.Extensions
                .Select(p => p.Name)
                .ToList();

            int i = 0;
            foreach (Extension ext in Engine.Extensions)
            {
                if (ext.Funcs != null)
                {
                    foreach (dynamic cmds in ext.Funcs["commands"])
                    {
                        foreach(var cmd in cmds.Value)
                            cmdsclass.Members.Add(BuildCmdMethod(ext.Name, cmds.Name, cmd, "command", i++));
                    }
                    foreach (dynamic cmds in ext.Funcs["panels"])
                    {
                        foreach (var cmd in cmds.Value)
                            cmdsclass.Members.Add(BuildCmdMethod(ext.Name, cmds.Name, cmd, "panel", i++));
                    }
                    foreach (dynamic lisps in ext.Funcs["lisps"])
                    {
                        foreach (var lisp in lisps.Value)
                            cmdsclass.Members.Add(BuildLispMethod(ext.Name, lisps.Name, lisp, i++));
                    }
                }
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

        private static CodeMemberMethod BuildCmdMethod(string prjname, string modulename, dynamic cmd, string type, int index)
        {

            CodeMemberMethod method =
                new CodeMemberMethod { Name = $"Cmd_{index}" };
            var args = new List<CodeAttributeArgument>();

            dynamic instance = Engine.Instance.Execute($"{type}({cmd.Value})");

            string name = cmd.Name;
            if (instance.name == null)
                instance.name = name;

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
                    $"NFox.Pycad.Core.Modules.pye.runcmd(\"{prjname}\", \"extension{modulename}.{cmd.Name}\");"));
            return method;

        }

        private static CodeMemberMethod BuildLispMethod(string prjname, string modulename, dynamic lisp, int index)
        {

            CodeMemberMethod method =
                new CodeMemberMethod { Name = $"Lisp_{index}" };
            var args = new List<CodeAttributeArgument>();

            dynamic instance = Engine.Instance.Execute($"lisp({lisp.Value})");
            string name = lisp.Name;
            if (instance.name == null)
                instance.name = name;

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
                    $"return NFox.Pycad.Core.Modules.pye.invokelisp(\"{prjname}\", \"extension{modulename}.{lisp.Name}\", rb);"));
            return method;

        }

        #endregion

    }

}
