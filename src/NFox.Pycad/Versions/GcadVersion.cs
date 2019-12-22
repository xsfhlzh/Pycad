using Microsoft.Win32;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace NFox.Pycad
{
    public class GcadVersion: VersionBase
    {

        private GcadVersion(string rootkey)
        {
            ProductRootKey = rootkey;
            var rk =
                Registry
                .CurrentUser
                .OpenSubKey($@"SOFTWARE\Gstarsoft\GstarCAD\{ProductRootKey}\zh-CN");
            ProductName = rk.GetValue("ProductName").ToString();
            var arr = rk.GetValue("Version").ToString().Split('.');
            Major = int.Parse(arr[0]);
            Minor = int.Parse(arr[1]);
            var gs2 = Regex.Match(ProductName, "浩辰CAD (\\d+)");
            if (gs2.Success) Number = int.Parse(gs2.Groups[1].Value);
            Location = rk.GetValue("LOCATION").ToString();
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
                           .CurrentUser
                           .OpenSubKey(@"SOFTWARE\Gstarsoft\GstarCAD")
                           .GetSubKeyNames();
                        foreach (var rootkey in copys)
                        {
                            try { _versions.Add(new GcadVersion(rootkey)); }
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
                .OpenSubKey($@"SOFTWARE\Gstarsoft\GstarCAD\{ProductRootKey}\zh-CN", true);
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
                rootkey.Close();
            }
            catch { }
        }

    }
}
