using System.Collections.Generic;
using System.IO;
using System.Reflection;

namespace NFox.Pycad
{
    public static class DirectoryEx
    {

        static FileInfo _location;
        static DirectoryInfo _main;
        static bool _startFromMain;
        static DirectoryInfo _root;
        static DirectoryInfo _mainBackup;

        public static void Init()
        {
            _location = new FileInfo(Assembly.GetExecutingAssembly().Location);
            _main = _location.Directory;
            _startFromMain = _main.Name == "main";
            if (_startFromMain)
            {
                _root = _mainBackup = _main.Parent;
            }
            else
            {
                _root = _main;
                _mainBackup = _main.CreateSubdirectory("main");
            }

            //如果从Main目录启动, 更新主目录文件
            if (_startFromMain)
            {
                foreach (var file in _main.GetFiles())
                    file.CopyTo(_mainBackup.GetFileFullName(file.Name));
            }
        }

        public static bool StartFromMain { get { return _startFromMain; } }

        public static DirectoryInfo Main { get { return _main; } }

        public static DirectoryInfo MainBackup { get { return _mainBackup; } }

        public static FileInfo Location { get { return _location; } }

        public static DirectoryInfo Root
        {
            get
            {
                if (_root == null)
                    Init();
                return _root;
            }
        }

        public static DirectoryInfo Bin { get; } = Root.GetDirectory("bin");

        public static DirectoryInfo Plugins { get; } = Root.GetDirectory("plugins");
        public static DirectoryInfo Support { get; } = Root.GetDirectory("support");
        public static DirectoryInfo Extensions { get; } = Root.GetDirectory("extensions");
        public static FileInfo PythonLib { get; } = Bin.GetFile("Lib.zip");
        public static DirectoryInfo Temp { get; } = Root.GetDirectory("temp");
        public static DirectoryInfo Update { get; } = Root.GetDirectory("update");

        public static DirectoryInfo GetDirectory(Assembly assem)
        {
            return new FileInfo(assem.Location).Directory;
        }

        public static DirectoryInfo GetDirectory(this DirectoryInfo dir, string name)
        {
            var dirs = dir.GetDirectories(name);
            if (dirs.Length > 0)
                return dirs[0];
            return null;
        }

        public static DirectoryInfo GetDirectory(this DirectoryInfo dir, params string[] names)
        {
            foreach (var name in names)
            {
                if (dir != null)
                    dir = GetDirectory(dir, name);
                else
                    return null;
            }
            return dir;
        }

        public static FileInfo GetFile(this DirectoryInfo dir, params string[] names)
        {
            if (names.Length == 0)
                return null;
            int i = 0;
            for (; i< names.Length - 1; i++)
            {
                if (dir != null)
                    dir = GetDirectory(dir, names[i]);
                else
                    return null;
            }
            return dir.GetFile(names[i]);
        }

        public static FileInfo GetFile(this DirectoryInfo dir, string name)
        {
            var files = dir.GetFiles(name);
            if (files.Length > 0)
                return files[0];
            return null;
        }

        public static string GetFileFullName(this DirectoryInfo dir, string name)
        {
            return Path.Combine(dir.FullName, name);
        }

        public static List<FileInfo> GetAllFiles(this DirectoryInfo dir)
        {
            var files = new List<FileInfo>();
            GetAllFiles(dir, files);
            return files;
        }

        private static void GetAllFiles(this DirectoryInfo dir, List<FileInfo> files)
        {
            foreach (var d in dir.GetDirectories())
                GetAllFiles(d, files);
            foreach (var f in dir.GetFiles())
                files.Add(f);
        }

    }
}
