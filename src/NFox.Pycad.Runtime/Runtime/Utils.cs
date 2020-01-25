using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.IO;
using System.Net;
using System.Net.NetworkInformation;

namespace NFox.Pycad
{
    public static class Utils
    {

        private static JObject _values;

        public static T GetVariable<T>(string name)
        {
            if (_values == null)
            {
                //从配置文件中获取系统变量
                string settings = DirectoryEx.Bin.GetFileFullName("settings.json");
                using (FileStream fs = new FileStream(settings, FileMode.Open))
                using (var sr = new StreamReader(fs))
                using (JsonTextReader reader = new JsonTextReader(sr))
                    _values = JToken.ReadFrom(reader) as JObject;
            }
            return _values[name].Value<T>();
        }

        public static void SetVariable<T>(string name, T value)
        {

            _values[name] = new JValue(value);
            //在配置文件中设置系统变量
            string settings = DirectoryEx.Bin.GetFileFullName("settings.json");
            using (FileStream fs = new FileStream(settings, FileMode.Create))
            using (var sw = new StreamWriter(fs))
            using (JsonTextWriter writer = new JsonTextWriter(sw))
            {
                writer.Formatting = Formatting.Indented;
                _values.WriteTo(writer);
            }
        }

        public static JObject UsingJsonFile(string filename, Action<JObject> action, bool save = false)
        {
            JObject obj;
            if (File.Exists(filename))
            {
                string settings = DirectoryEx.Bin.GetFileFullName(filename);
                using (FileStream fs = new FileStream(settings, FileMode.Open))
                using (var sr = new StreamReader(fs))
                using (JsonTextReader reader = new JsonTextReader(sr))
                {
                    obj = JToken.ReadFrom(reader) as JObject;
                    action(obj);
                }
                if (save)
                {
                    using (FileStream fs = new FileStream(settings, FileMode.Create))
                    using (var sw = new StreamWriter(fs))
                    using (JsonTextWriter writer = new JsonTextWriter(sw))
                    {
                        writer.Formatting = Formatting.Indented;
                        obj.WriteTo(writer);
                    }
                }
                return obj;
            }
            return null;
        }

        public static int GetFreePort(int port)
        {

            bool isAvailable = true;
            var endPoints =
                IPGlobalProperties
                .GetIPGlobalProperties()
                .GetActiveTcpListeners();

            do
            {
                if (!isAvailable)
                {
                    port++;
                    isAvailable = true;
                }

                foreach (IPEndPoint endPoint in endPoints)
                {
                    if (endPoint.Port != port) continue;
                    isAvailable = false;
                    break;
                }

            } while (!isAvailable && port < IPEndPoint.MaxPort);

            if (!isAvailable)
                return -1;
            return port;

        }


    }
}
