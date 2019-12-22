
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.IO.Compression;


namespace NFox.Expression.DataSystem
{
    public static class ZipUtils
    {

        #region XElement

        /// <summary>
        /// 按元素名压缩XElement元素集合
        /// </summary>
        /// <param name="fileName">文件名</param>
        /// <param name="dicts">XElement元素集合</param>
        public static void Compress(string fileName, params IEnumerable<XElement>[] dicts)
        {

            using (FileStream fs = new FileStream(fileName, FileMode.Create))
            {
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Update))
                {
                    foreach (var dict in dicts)
                    {
                        foreach (var xe in dict)
                        {
                            string name = xe.Name.LocalName;
                            var ent = zip.GetEntry(name);
                            if (ent != null) ent.Delete();
                            ent = zip.CreateEntry(name);
                            using (var sw = new StreamWriter(ent.Open(), Encoding.UTF8))
                            {
                                xe.Save(sw);
                            }
                        }
                    }
                }
                fs.Close();
            }
        }


        /// <summary>
        /// 按给定的名称压缩XElement元素集合
        /// </summary>
        /// <param name="fileName">文件名</param>
        /// <param name="dicts">XElement元素集合</param>
        public static void Compress(string fileName, params IEnumerable<KeyValuePair<string, XElement>>[] dicts)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.Create))
            {
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Update))
                {
                    foreach (var dict in dicts)
                    {
                        foreach (var kv in dict)
                        {
                            string name = kv.Key;
                            var ent = zip.GetEntry(name);
                            if (ent != null) ent.Delete();
                            ent = zip.CreateEntry(name);
                            using (var sw = new StreamWriter(ent.Open(), Encoding.UTF8))
                            {
                                kv.Value.Save(sw);
                            }
                        }
                    }
                }
                fs.Close();
            }
        }

        /// <summary>
        /// 解压缩全部元素
        /// </summary>
        /// <param name="fileName">文件名</param>
        /// <returns>XElement元素集合</returns>
        public static Dictionary<string, XElement> Extract(string fileName)
        {
            Dictionary<string, XElement> dict =
                new Dictionary<string, XElement>();
            using (FileStream fs = new FileStream(fileName, FileMode.Open))
            {
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
                {
                    foreach (var ent in zip.Entries)
                    {
                        using (var sr = new StreamReader(ent.Open()))
                        {
                            dict.Add(ent.Name, XElement.Load(sr));
                        }
                    }
                }
                fs.Close();
            }
            return dict;
        }

        /// <summary>
        /// 解压缩单个元素
        /// </summary>
        /// <param name="fileName">文件名</param>
        /// <param name="entryName">zip实体名</param>
        /// <returns>XElement元素</returns>
        public static XElement Extract(string fileName, string entryName)
        {
            XElement xe;
            using (FileStream fs = new FileStream(fileName, FileMode.Open))
            {
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
                {
                    var ent = zip.GetEntry(entryName);
                    using (var sr = new StreamReader(ent.Open()))
                    {
                        xe = XElement.Load(sr);
                    }
                }
                fs.Close();
            }
            return xe;
        }

        #endregion

        #region Names

        /// <summary>
        /// 获取zip实体名集合
        /// </summary>
        /// <param name="fileName">zip文件名</param>
        /// <returns>实体名字集合</returns>
        public static IEnumerable<string> GetEntryNames(string fileName)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.Open))
            {
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
                {
                    foreach (var ent in zip.Entries)
                        yield return ent.Name;
                }
                fs.Close();
            }
        }

        /// <summary>
        /// 按给定的后缀获取zip实体名集合
        /// </summary>
        /// <param name="fileName">zip文件名</param>
        /// <param name="postfix">实体名后缀</param>
        /// <param name="keepTheSuffix">返回值是否保留后缀</param>
        /// <returns>实体名字集合</returns>
        public static IEnumerable<string> GetEntryNames(string fileName, string prefix, string postfix, bool keepTheSuffix)
        {

            Regex r = new Regex("^(.*)" + postfix + "$");
            int i = keepTheSuffix ? 0 : 1;
            using (FileStream fs = new FileStream(fileName, FileMode.Open))
            {
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
                {
                    foreach (var ent in zip.Entries)
                    {
                        if (r.IsMatch(ent.Name))
                        {
                            var m = r.Match(ent.Name);
                            yield return m.Groups[i].Value;
                        }
                    }
                }
                fs.Close();
            }
        }

        #endregion

    }
}
