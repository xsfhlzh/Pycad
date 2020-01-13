using System;
using System.IO;
using System.IO.Compression;
using Microsoft.Win32;
using System.Xml.Linq;

namespace NFox.Pycad.Loader
{
    public class Application
    {
        public Application(ZipArchive zip)
        {
            
            using (Stream cstream = zip.GetEntry("Version").Open())
            using (StreamReader sr = new StreamReader(cstream))
            {

                Version newver = Version.Parse(sr.ReadToEnd());
                String mainpath;
                using (RegistryKey rk = Registry.CurrentUser.OpenSubKey("Software", RegistryKeyPermissionCheck.ReadWriteSubTree))
                using (RegistryKey nfoxrk = rk.OpenSubKey("NFox"))
                using (RegistryKey pycadrk = rk.CreateSubKey("NFox").CreateSubKey("Pycad"))
                {
                    if (nfoxrk == null || nfoxrk.OpenSubKey("Pycad") == null)
                    {
                        pycadrk.SetValue("Version", newver.ToString());
                        String path = "C:\\Program Files\\Pycad";
                        mainpath = path;
                        for (int i = 2; Directory.Exists(mainpath); i++)
                            mainpath = path + i;
                        pycadrk.SetValue("MainPath", mainpath);
                        DirectoryInfo dir = Directory.CreateDirectory(mainpath);
                        Stream pstream = zip.GetEntry("Update\\Package.xml").Open();
                        XElement xe = XElement.Load(pstream); ;
                        pstream.Dispose();
                        CopyFiles(xe, dir, zip);
                    }
                    else
                    {
                        Version oldver = Version.Parse(pycadrk.GetValue("Version").ToString());
                        mainpath = pycadrk.GetValue("MainPath").ToString();
                        if (newver > oldver)
                        {
                            foreach (var ent in zip.Entries)
                                Copy(ent, mainpath + "\\" + ent.FullName);
                        }
                        else
                        {
                            foreach (var ent in zip.Entries)
                            { 
                                if (ent.FullName.StartsWith("Update\\Projects"))
                                    Copy(ent, mainpath + "\\" + ent.FullName);
                            }
                        }
                    }
                }
            }
        }

        private void Copy(ZipArchiveEntry ent, String path)
        {
            using (Stream source = ent.Open())
            using (Stream target = File.OpenWrite(path))
                source.CopyTo(target);
        }

        private void UnzipDllx(Stream stream, DirectoryInfo dir)
        {
            ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Read);
            foreach (var ent in zip.Entries)
            {
                string path = dir.FullName + "\\" + ent.FullName;
                string pdir = Path.GetDirectoryName(path);
                if (!Directory.Exists(pdir))
                    Directory.CreateDirectory(pdir);
                using (Stream source = ent.Open())
                using (Stream target = File.Open(path, FileMode.Create))
                    source.CopyTo(target);
            }
            zip.Dispose();
        }

        private void CopyFiles(XElement xe, DirectoryInfo dir, ZipArchive zip)
        {
            foreach (var e in xe.Elements())
            {
                var name = e.Attribute("Name").Value;
                if (e.Name.LocalName == "Directory")
                {
                    DirectoryInfo sdir = dir.CreateSubdirectory(name);
                    CopyFiles(e, sdir, zip);
                }
                else if (e.Name.LocalName == "Plugin")
                {
                    DirectoryInfo sdir = dir.CreateSubdirectory(name);
                    UnzipDllx(zip.GetEntry(name).Open(), sdir);
                }
                else if (e.Name.LocalName == "Module")
                {
                    var dllname = name + ".dll";
                    Copy(zip.GetEntry(dllname), dir.FullName + "\\" + dllname);
                }
                else if (e.Name.LocalName == "File")
                {
                    Copy(zip.GetEntry(name), dir.FullName + "\\" + name);
                }
            }
        }
    }
}
        
    




