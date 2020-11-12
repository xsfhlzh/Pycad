using System;
using System.IO;
using System.IO.Compression;
using System.Xml.Linq;

namespace NFox.Pycad.Update
{
    public class Application : PluginBase
    {

        protected override void OnInitializing()
        {

            //保证下次从主目录启动
            VersionBase.RegApp();

            //更新其他的文件
            var file = DirectoryEx.Update.GetFile("package.xml");
            if (file != null)
            {
                XElement xe = XElement.Load(file.FullName);
                UpdateFiles(xe, DirectoryEx.Root, true);
            }
            UnzipExts();

        }

        protected override void OnTerminated()
        {
            
            if(!DirectoryEx.StartFromMain)
            {
                DelFiles(DirectoryEx.Main);
                foreach (var sdir in DirectoryEx.MainBackupPlugins.GetDirectories())
                    sdir.Delete();
            }

            var file = DirectoryEx.Update.GetFile("package.xml");
            if (file != null)
            {
                //更新主文件至备份目录
                XElement xe = XElement.Load(file.FullName);
                UpdateFiles(xe, DirectoryEx.Root, false);
                DirectoryEx.Update.GetFile("Version")?.Delete();
            }
        }

        private void DelFiles(DirectoryInfo dir)
        {
            foreach (var file in dir.GetFiles())
                file.Delete();
            foreach (var sdir in dir.GetDirectories())
                DelFiles(sdir);
        }

        private void CopyTo(DirectoryInfo source, DirectoryInfo target)
        {
            foreach (var file in source.GetFiles())
                file.CopyTo(target.GetFileFullName(file.Name));
            foreach (var dir in source.GetDirectories())
                CopyTo(dir, target.CreateSubdirectory(dir.Name));
        }

        private void UpdateFiles(XElement xe, DirectoryInfo dir, bool atStart)
        {
            foreach (var e in xe.Elements())
            {
                string name = e.Attribute("Name").Value;
                FileInfo file;
                switch (e.Name.LocalName)
                {
                    case "Directory":
                        UpdateFiles(e, dir.CreateSubdirectory(name), atStart);
                        break;
                    case "Module":
                        if (atStart)
                        {
                            var dllname = name + ".dll";
                            file = DirectoryEx.Update.GetFile(dllname);
                            file.CopyTo($"{dir.FullName}\\{dllname}", true);
                            file.Delete();
                        }
                        break;
                    case "Plugin":
                        file = DirectoryEx.Update.GetFile(name);
                        using (var source = File.OpenRead(file.FullName))
                            Unzip(source, DirectoryEx.MainBackupPlugins.CreateSubdirectory(name));
                        file.Delete();
                        break;
                    case "File":
                        if (dir == DirectoryEx.Root)
                        {
                            file = DirectoryEx.Update.GetFile(name);
                            file.CopyTo(DirectoryEx.MainBackup.GetFileFullName(name), true);
                            file.Delete();
                        }
                        else if (atStart)
                        {
                            file = DirectoryEx.Update.GetFile(name);
                            file.CopyTo($"{dir.FullName}\\{name}", true);
                            file.Delete();
                        }
                        break;
                }
            }
        }

        private void Unzip(Stream stream, DirectoryInfo dir)
        {
            ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Read);
            foreach (var ent in zip.Entries)
            {
                string path = dir.FullName + "\\" + ent.FullName;
                string ddir = Path.GetDirectoryName(path);
                if (!Directory.Exists(ddir))
                    Directory.CreateDirectory(ddir);
                Stream source = ent.Open();
                Stream target = File.Open(path, FileMode.Create);
                source.CopyTo(target);
                target.Dispose();
                source.Dispose();
            }
            zip.Dispose();
        }

        private void UnzipExts()
        {
            foreach (var file in DirectoryEx.Update.GetDirectory("extensions").GetFiles())
            {
                if (file.Name == "placeholder.___")
                    continue;
                using (Stream stream = file.OpenRead())
                {
                    using (ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Read))
                    {
                        foreach (var ent in zip.Entries)
                        {
                            string path = DirectoryEx.Extensions.FullName + $"\\.release\\{file.Name}\\" + ent.FullName;
                            string dir = Path.GetDirectoryName(path);
                            if (!Directory.Exists(dir))
                                Directory.CreateDirectory(dir);
                            using (Stream source = ent.Open())
                            {
                                using (Stream target = File.Open(path, FileMode.Create))
                                    source.CopyTo(target);
                            }
                        }
                    }
                }
                file.Delete();
            }
        }



    }
}
