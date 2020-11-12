using Microsoft.Win32;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

namespace NFox.Pycad
{
    public class AcadVersion: VersionBase
    {

        const string _pattern = @"AutoCAD\\R(\d+)\.(\d+)\\.*?";

        private AcadVersion(string rootkey)
        {
            //从注册表获取版本信息
            var gs = Regex.Match(rootkey, _pattern).Groups;
            ProductRootKey = "Software\\" + rootkey;
            Major = int.Parse(gs[1].Value);
            Minor = int.Parse(gs[2].Value);
            using (var rk = Registry.LocalMachine.OpenSubKey(ProductRootKey))
            {
                var path = rk.GetValue("ProductNameGlob").ToString();
                var gs2 = Regex.Match(path, "AutoCAD (\\d+)");
                if (gs2.Success)
                {
                    Number = int.Parse(gs2.Groups[1].Value);
                    ProductName = gs2.Groups[0].Value;
                }
            }
        }

        private static List<VersionBase> _versions;
        public static List<VersionBase> Versions
        {
            get
            {
                if (_versions == null)
                {
                    _versions = new List<VersionBase>();
                    try
                    {
                        using (var acadkey = Registry.LocalMachine.OpenSubKey("Software\\Autodesk\\Hardcopy"))
                        {
                            var copys =
                                acadkey
                                .GetSubKeyNames()
                                .Select(name => acadkey.OpenSubKey(name));
                            foreach (var name in acadkey.GetValueNames())
                            {
                                try
                                {
                                    if (Regex.IsMatch(name, _pattern))
                                        _versions.Add(new AcadVersion(name));
                                }
                                catch { }
                            }
                        }
                    }
                    catch { }
                }
                return _versions;
            }
        }

        public override void RegApp(string name, string location, string desc)
        {

            var info = new AssemInfo(name, location, desc);

            try
            {

                //注册预加载程序集
                using (var rootkey = Registry.CurrentUser.OpenSubKey(ProductRootKey, true))
                using (var appskey = rootkey.CreateSubKey("Applications"))
                using (var rk = appskey.CreateSubKey(info.Name))
                {
                    rk.SetValue("DESCRIPTION", info.Description, RegistryValueKind.String);
                    rk.SetValue("LOADER", info.Location, RegistryValueKind.String);
                    rk.SetValue("LOADCTRLS", info.LoadType, RegistryValueKind.DWord);
                    rk.SetValue("MANAGED", 1, RegistryValueKind.DWord);


                    try
                    {
                        //添加信任目录
                        using (var profileskey = rootkey.OpenSubKey("Profiles"))
                        {
                            foreach (string keyname in profileskey.GetSubKeyNames())
                            {
                                using (var profilekey = profileskey.OpenSubKey(keyname))
                                using (var variableskey = profilekey?.OpenSubKey("Variables", true))
                                {
                                    string paths = variableskey?.GetValue("TRUSTEDPATHS")?.ToString();
                                    if (paths != null)
                                    {
                                        List<string> names = new List<string>();
                                        if (paths != "")
                                        {
                                            foreach (string s in paths.Split(';'))
                                                names.Add(s.ToLower());
                                        }
                                        string path = Path.GetDirectoryName(info.Location);
                                        if (!names.Contains(path.ToLower()))
                                        {
                                            names.Add(path);
                                            variableskey.SetValue("TRUSTEDPATHS", string.Join(";", names));
                                        }
                                    }
                                }
                            }
                        }
                    }
                    catch { }
                }
            }
            catch { }

        }

    }

}
