namespace NFox.Pycad
{
    public abstract class VersionBase
    {

        public int Major { get; protected set; }

        public int Minor { get; protected set; }

        public double ProgId
        {
            get { return double.Parse($"{Major}.{Minor}"); }
        }

        public int Number { get; protected set; }

        public string ProductName { get; protected set; }

        public string ProductRootKey { get; protected set; }

        public string Location { get; protected set; }

        public abstract void RegApp(string name, string location, string desc);

        public static void RegApp()
        {

            //注册所有AutoCad版本
            foreach (var ver in AcadVersion.Versions)
            {

                if (ver.Number >= 2012)
                    ver.RegApp(
                        "NFox.Pycad",
                        DirectoryEx.Root.GetFile("NFox.Pycad.Acad.dll").FullName,
                        "NFox Pycad Loader");

            }



            //注册所有GstarCAD版本
            foreach (var ver in GcadVersion.Versions)
            {

                ver.RegApp(
                    "NFox.Pycad",
                    DirectoryEx.Root.GetFile("NFox.Pycad.Gcad.dll").FullName,
                    "NFox Pycad Loader");

            }

        }

    }

    public struct AssemInfo
    {
        /// <summary>
        /// 注册名
        /// </summary>
        public string Name;

        /// <summary>
        /// 程序集路径
        /// </summary>
        public string Location;

        /// <summary>
        /// 加载方式
        /// </summary>
        public AssemLoadType LoadType;

        /// <summary>
        /// 程序集说明
        /// </summary>
        public string Description;

        public AssemInfo(string name, string location, string desc)
        {
            Name = name;
            Location = location;
            Description = desc;
            LoadType = AssemLoadType.Startting;
        }

    }

    public enum AssemLoadType
    {
        Startting = 2,
        ByCommand = 12,
        Disabled = 20
    }

}
