using System.IO;
using System.IO.Compression;
using System.Xml.Linq;

namespace NFox.Pycad.Update
{
    public class Application : PluginBase
    {

        protected override void OnInitializing()
        {
            XElement xe = XElement.Load(DirectoryEx.Bin.GetFile("package.xml").FullName);
            UpdateFiles(xe, DirectoryEx.Root);
            UnzipDllxs();
        }

        private void UpdateFiles(XElement xe, DirectoryInfo dir)
        {
            foreach(var e in xe.Elements())
            {
                string name = e.Attribute("Name").Value;
                if (e.Name == "Directory")
                {
                    UpdateFiles(e, dir.GetDirectory(name));
                }
                else
                {
                    var file = DirectoryEx.Update.GetFile(name);
                    if (name != "NFox.Pycad.dll")
                    {
                        file?.CopyTo($"{dir.FullName}\\{name}");
                        file?.Delete();
                    }
                }
            }
        }

        private void UnzipDllxs()
        {
            foreach (var file in DirectoryEx.Update.GetDirectory("extensions").GetFiles())
            {
                using (Stream stream = file.OpenRead())
                {
                    using (ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Read))
                    {
                        foreach (var ent in zip.Entries)
                        {
                            string path = DirectoryEx.Extensions.FullName + "\\" + ent.FullName;
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
