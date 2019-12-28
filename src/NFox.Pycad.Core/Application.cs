using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
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

        public void Edit()
        {
            System.Diagnostics.Process pro = new System.Diagnostics.Process();
            pro.EnableRaisingEvents = false;
            pro.StartInfo.FileName = Application.GetVariable("editor.path");
            pro.StartInfo.Arguments = $"\"{DirectoryEx.Extensions.FullName}\\\"";
            pro.Start();
        }

        protected override void OnInitializing()
        {
            LoadSettings();
            Engine.Instance.AddSystemCommand("pyrb", new Action(Start));
            Engine.Instance.AddSystemCommand("pye", new Action(Edit));
        }

        private void LoadSettings()
        {
            //从配置文件中获取系统变量
            string settings = DirectoryEx.Bin.GetFile("settings.json")?.FullName;
            using (FileStream fs = new FileStream(settings, FileMode.Open))
            {
                using (var sr = new StreamReader(fs))
                using (JsonTextReader reader = new JsonTextReader(sr))
                {
                    foreach (JProperty info in JToken.ReadFrom(reader))
                        SetVariable(info.Name, ((JValue)info.Value).Value);
                }
            }
        }

        private void SaveSettings()
        {
            string settings = DirectoryEx.Bin.GetFile("settings.json")?.FullName;
            using (FileStream fs = new FileStream(settings, FileMode.Create))
            {
                using (var sw = new StreamWriter(fs))
                using (JsonTextWriter writer = new JsonTextWriter(sw))
                {
                    writer.Formatting = Formatting.Indented;
                    JObject obj = new JObject();
                    foreach (var info in _settings)
                        obj.Add(new JProperty(info.Key, info.Value));
                    obj.WriteTo(writer);
                }
            }
        }

        protected override void OnLoading()
        {
            try
            {
               
                //初始化引擎
                Engine.Instance.Restart();
                Engine.Instance.LoadAssembly(Assembly.GetExecutingAssembly());

                //从acad.py中获取初始化信息
                //Engine.Instance.TryReference("pycad.dll");
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
                Engine.Instance.LoadExtensions(_loadfirst);
                _loadfirst = false;
                DynamicCompiler.BuildUserAssembly();

                if (CurrSystem != "acore")
                {
                    var menus = Engine.Instance.Execute("acapp.MenuGroups");
                    foreach(Extension p in Engine.Instance.Extensions.Packages)
                        p.LoadCuixs(menus);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Err:" + ex.Message);
            }

        }

        #endregion

    }

}
