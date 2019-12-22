using Microsoft.Win32;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text.RegularExpressions;

namespace NFox.Pycad
{
    public class AcadVersion: VersionBase
    {

        const string _pattern = @"Autodesk\\AutoCAD\\R(\d+)\.(\d+)\\.*?";

        private AcadVersion(string rootkey)
        {
            //从注册表获取版本信息
            var gs = Regex.Match(rootkey, _pattern).Groups;
            ProductRootKey = rootkey;
            Major = int.Parse(gs[1].Value);
            Minor = int.Parse(gs[2].Value);
            var rk =
                Registry
                .LocalMachine
                .OpenSubKey("SOFTWARE")
                .OpenSubKey(rootkey);
            ProductName = rk.GetValue("ProductName").ToString();
            var gs2 = Regex.Match(ProductName, "AutoCAD (\\d+)");
            if (gs2.Success) Number = int.Parse(gs2.Groups[1].Value);
            Location = rk.GetValue("Location").ToString();
            rk.Close();
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
                        string[] copys =
                           Registry
                           .LocalMachine
                           .OpenSubKey(@"SOFTWARE\Autodesk\Hardcopy")
                           .GetValueNames();
                        foreach (var rootkey in copys)
                        {
                            try
                            {
                                if (Regex.IsMatch(rootkey, _pattern))
                                    _versions.Add(new AcadVersion(rootkey));
                            }
                            catch { }
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
                var rootkey =
                    Registry
                    .CurrentUser
                    .OpenSubKey("SOFTWARE")
                    .OpenSubKey(ProductRootKey, true);
                RegistryKey appskey = rootkey.CreateSubKey("Applications");

                //注册预加载程序集
                RegistryKey rk = appskey.OpenSubKey(info.Name, true);
                if (rk == null)
                {
                    rk = appskey.CreateSubKey(info.Name);
                    rk.SetValue("DESCRIPTION", info.Description, RegistryValueKind.String);
                    rk.SetValue("LOADER", info.Location, RegistryValueKind.String);
                    rk.SetValue("LOADCTRLS", info.LoadType, RegistryValueKind.DWord);
                    rk.SetValue("MANAGED", 1, RegistryValueKind.DWord);
                }
                else if (rk.GetValue("LOADER").ToString() != info.Location)
                {
                    rk.SetValue("LOADER", info.Location, RegistryValueKind.String);
                }

                rk.Close();
                appskey.Close();

                try
                {
                    //添加信任目录
                    var profileskey = rootkey.OpenSubKey("Profiles");
                    foreach (string keyname in profileskey.GetSubKeyNames())
                    {
                        var profilekey = profileskey.OpenSubKey(keyname);
                        var variableskey = profilekey?.OpenSubKey("Variables", true);
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
                        variableskey.Close();
                        profilekey.Close();
                    }
                    profileskey.Close();
                    rootkey.Close();
                }
                catch { }
            }
            catch { }

        }

    }

}
