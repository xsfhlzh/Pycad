using System.IO;
using System.IO.Compression;
using System.Xml.Linq;

namespace NFox.Pycad.Update
{
    public class Application : PluginBase
    {

        protected override void OnInitializing()
        {

            var file = DirectoryEx.Update.GetFile("package.xml");
            if (file != null)
            {
                XElement xe = XElement.Load(file.FullName);
                UpdateFiles(xe, DirectoryEx.Root);
            }
            UnzipExts();
        }

        private void UpdateFiles(XElement xe, DirectoryInfo dir)
        {
            foreach(var e in xe.Elements())
            {
                string name = e.Attribute("Name").Value;
                FileInfo file;
                switch(e.Name.LocalName)
                {
                    case "Directory":
                        UpdateFiles(e, dir.CreateSubdirectory(name));
                        break;
                    case "Plugin":
                        file = DirectoryEx.Update.GetFile(name);
                        using (var source = File.OpenRead(file.FullName))
                            Unzip(source, dir.GetDirectory(name));
                        file.Delete();
                        break;
                    case "Module":
                        var dllname = name + ".dll";
                        file = DirectoryEx.Update.GetFile(dllname);
                        file.CopyTo($"{dir.FullName}\\{dllname}");
                        file.Delete();
                        break;
                    case "File":
                        if (dir != DirectoryEx.Root)
                        {
                            file = DirectoryEx.Update.GetFile(name);
                            file.CopyTo($"{dir.FullName}\\{name}");
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
