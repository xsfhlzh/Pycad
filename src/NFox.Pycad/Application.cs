
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace NFox.Pycad
{

    public class Application : PluginBase
    {

        public override string Name
        {
            get { return "NFox.Pycad"; }
        }

        protected override void OnInitializing()
        {

            VersionBase.RegApp();

            var domain = AppDomain.CurrentDomain;
            domain.AssemblyResolve += assemblyResolve;
            CurrSystem =
                domain.SetupInformation.ApplicationName.ToLower() == "accoreconsole.exe" ?
                "acore" : HostAppName;

            _plugins = new Dictionary<string, PluginBase>();
            _plugins[Name] = Root = this;
            Assembly = Assembly.GetExecutingAssembly();

            _searchpaths =
                new List<string>
                {
                    DirectoryEx.Bin.FullName,
                    DirectoryEx.Support.FullName,
                };

            var infos = 
                DirectoryEx
                .Plugins
                .GetDirectories()
                .Select(d => new PluginInfo(d))
                .Where(i => i.Name != Name);

            StartPluginTree(infos.Where(p => p.Preload), true);
            StartPluginTree(infos.Where(p => !p.Preload));

        }

        private static List<string> _searchpaths;

        static Assembly assemblyResolve(object sender, ResolveEventArgs args)
        {

            Regex r = new Regex("^(.*?), Version=(.*?), Culture=(.*?), PublicKeyToken=(.*?)$");
            if (r.IsMatch(args.Name))
            {

                var name = r.Match(args.Name).Groups[1].Value;
                string path = DirectoryEx.Bin.GetFile(name + ".dll")?.FullName;
                if (path != null)
                    return Assembly.LoadFrom(path);

                foreach(var p in _plugins)
                {
                    var ass = p.Value.Assembly;
                    if (ass.FullName == args.Name)
                        return ass;
                }

                foreach (var sp in _searchpaths)
                {
                    string dllname = Path.Combine(sp, name + ".dll");
                    if(File.Exists(dllname))
                        return Assembly.LoadFrom(dllname);
                }

            }
            return null;
        }

        private void StartPluginTree(IEnumerable<PluginInfo> infos, bool preload = false)
        {

            //去除无效分支
            while(true)
            {
                var names = infos.Select(i => i.Name).ToList();
                names.Add(Name);
                var lst = new List<PluginInfo>();
                foreach (var info in infos)
                {
                    if (!names.Contains(info.Parent))
                        lst.Add(info);
                }
                if (lst.Count == 0)
                    break;
                else
                    infos = infos.Intersect(lst);
            }

            //设置搜索目录
            foreach (var info in infos)
            {
                _searchpaths.Add(info.Directory.FullName);
            }

            //更新预加载插件
            if (preload)
            {
                foreach (var info in infos)
                {
                    var dir = DirectoryEx.Update.GetDirectory("Plugins", info.Name);
                    if (dir != null)
                    {
                        DirectoryEx.Plugins.GetDirectory(info.Name)?.Delete(true);
                        dir.MoveTo(Path.Combine(DirectoryEx.Plugins.FullName, info.Name));
                    }
                }
            }

            //反射创建子插件
            foreach (var info in infos)
            {
                try
                {
                    Assembly ass = Assembly.LoadFrom(info.Path);
                    Type t = ass.GetType($"{info.Name}.Application");
                    _plugins[info.Name] = (PluginBase)Activator.CreateInstance(t);
                    _plugins[info.Name].Assembly = ass;
                    _plugins[info.Name].Info = info;
                }
                catch { }
            }

            //设置插件树父子关系
            foreach (var info in infos)
            {
                _plugins[info.Parent].Add(_plugins[info.Name]);
            }

            infos = infos.Where(i => i.Parent == Name);

            //运行初始化例程
            foreach (var info in infos)
            {
                _plugins[info.Name].Initialize();
            }

            //启动例程
            foreach (var info in infos)
            {
                _plugins[info.Name].Start();
            }

        }

    }
}
