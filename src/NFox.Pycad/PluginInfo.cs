using System.IO;
using System.Xml.Linq;

namespace NFox.Pycad
{
    public class PluginInfo
    {

        public DirectoryInfo Directory { get; }

        public string Name { get; }

        public bool Preload { get; }

        public string Parent { get; }

        public string Path => Directory.GetFile(Name + ".dll")?.FullName;

        public PluginInfo(DirectoryInfo dir)
        {
            Directory = dir;
            Name = dir.Name;
            Preload = false;
            Parent = "NFox.Pycad";
            var settingsFile = dir.GetFile("settings.xml");
            if(settingsFile != null)
            {
                var xe = XElement.Load(settingsFile.FullName);
                if(xe != null)
                {
                    if (xe.Attribute("Name") != null)
                        Name = xe.Attribute("Name").Value;
                    if (xe.Element("Preload") != null)
                        Preload = bool.Parse(xe.Element("Preload").Attribute("Value").Value);
                    if (xe.Element("Parent") != null)
                        Parent = xe.Element("Parent").Attribute("Value").Value;
                }
            }
        }

    }
}
