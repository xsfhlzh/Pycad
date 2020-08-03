using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

namespace NFox.Pycad.Core
{
    public class Application : PluginBase
    {

        public static Application Curr { get; private set; }

        public Application()
        {
            Curr = this;
        }

        #region Plugin

        protected override void OnInitializing()
        {
            Engine.Instance.AddSystemCommand("pyrb", new Action(Start));
        }

        protected override void OnLoading()
        {
            try
            {
                Engine.Assemblies = new List<Assembly> { Assembly.GetExecutingAssembly() };
                //初始化引擎
                Engine.Instance.Restart();

                //从acad.py中获取初始化信息
                Engine.Instance.TryReference("pycad.dll");
                Engine.Instance.Execute($"from pycad.acad import *");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Err:" + ex.Message);
            }

        }

        bool _loadfirst = true;

        protected override void OnLoaded()
        {
            try
            {


                //获取当前版本Cad的Mgd程序集
                List<string> mgds = new List<string>();
                var mainmgds = Engine.Instance.Execute("pycad.system.mgds[0]");
                var acadroot = AppDomain.CurrentDomain.BaseDirectory;
                foreach (string name in mainmgds)
                {
                    string path = Path.Combine(acadroot, name);
                    if (File.Exists(path))
                        mgds.Add(path);
                }
                DynamicCompiler.Mgdlls = mgds;
                DynamicCompiler.BuildSystemAssembly();

                //动态编译用户命令集
                Engine.LoadExtensions(_loadfirst);
                _loadfirst = false;
                DynamicCompiler.BuildUserAssembly();

                if (CurrSystem != "acore")
                {
                    var menus = Engine.Instance.Execute("acapp.MenuGroups");
                    foreach(Extension p in Engine.Extensions)
                        p.LoadCuixs(menus);
                }
                Engine.Instance.Execute("with acdoc(): print('项目编译成功!')");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Err:" + ex.Message);
            }

        }

        #endregion

    }

}
