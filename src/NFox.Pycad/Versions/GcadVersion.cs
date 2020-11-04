using Microsoft.Win32;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace NFox.Pycad
{
    public class GcadVersion: VersionBase
    {

        private GcadVersion(string rootkey)
        {
            ProductRootKey = $@"SOFTWARE\Gstarsoft\GstarCAD\{rootkey}\zh-CN";
            using (var rk = Registry.CurrentUser.OpenSubKey(ProductRootKey))
            {
                ProductName = rk.GetValue("ProductName").ToString();
                var arr = rk.GetValue("Version").ToString().Split('.');
                Major = int.Parse(arr[0]);
                Minor = int.Parse(arr[1]);
                var gs2 = Regex.Match(ProductName, "浩辰CAD (\\d+)");
                if (gs2.Success) Number = int.Parse(gs2.Groups[1].Value);
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
            //注册预加载程序集
            try
            {
                using (var rootkey = Registry.CurrentUser.OpenSubKey(ProductRootKey, true))
                using (var appskey = rootkey.CreateSubKey("Applications"))
                using (var rk = appskey.CreateSubKey(info.Name))
                {
                    rk.SetValue("DESCRIPTION", info.Description, RegistryValueKind.String);
                    rk.SetValue("LOADER", info.Location, RegistryValueKind.String);
                    rk.SetValue("LOADCTRLS", info.LoadType, RegistryValueKind.DWord);
                    rk.SetValue("MANAGED", 1, RegistryValueKind.DWord);
                }
            }
            catch { }
        }

    }
}
