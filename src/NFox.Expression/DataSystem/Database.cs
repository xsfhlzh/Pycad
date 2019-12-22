using System.Linq;
using System.Collections.Generic;
using System.Xml.Linq;
using NFox.Expression.SymbolValues;
using System.IO;
using NFox.Pycad;
using System.Reflection;

namespace NFox.Expression.DataSystem
{

    public class Database
    {

        public ImagePartTable ImagePartTable
        { private set; get; }

        public FunctionTable FunctionTable
        { private set; get; }

        public PartFolder Root
        { private set; get; }

        public ConfigDictionary ConfigDictionary
        { private set; get; }

        public string FileName
        { private set; get; }

        public Engine Engine
        { private set; get; }

        public Database(PartFolder folder) 
        {
            FunctionTable = new FunctionTable { Database = this };
            ImagePartTable = new ImagePartTable { Database = this };
            var parts = folder.GetAllParts();
            foreach (var p in parts.OfType<ParameterizedPart>())
                FunctionTable.Add(p.Function, true);
            foreach (var p in parts)
                ImagePartTable.Add(p.Copy() as ImagePart, true);
            Root = folder.Copy() as PartFolder;
            Root.Database = this;
            foreach (var f in Root.GetAllFolders())
                f.Database = this;
        }

        public Database()
        {
            Engine = new Engine();
            Engine.Restart();
            Engine.LoadAssembly(Assembly.GetExecutingAssembly());
            FunctionTable = new FunctionTable { Database = this };
            ImagePartTable = new ImagePartTable { Database = this };
            ConfigDictionary = new ConfigDictionary { Database = this };
            Root = new PartFolder { Database = this };
        }

        public Database(string fileName)
        {
            FileName = fileName;
            Engine = new Engine();
            Engine.Restart();
            Engine.LoadAssembly(Assembly.GetExecutingAssembly());
            FunctionTable = new FunctionTable { Database = this };
            ImagePartTable = new ImagePartTable { Database = this };
            ConfigDictionary = new ConfigDictionary { Database = this };
            Root = new PartFolder { Database = this };
            if (File.Exists(FileName))
                Root.FromX(ZipUtils.Extract(FileName, "Root"));
            else
                Root.Name = "所有元件";
        }

        /// <summary>
        /// 将源数据库合并到目标项目
        /// </summary>
        /// <param name="owner">目标项目</param>
        /// <param name="database">源数据库</param>
        /// <param name="over">是否覆盖元件定义</param>
        public void Merge(PartFolder owner, Database database, bool over)
        {
            FunctionTable.Merge(database.FunctionTable, over);
            ImagePartTable.Merge(database.ImagePartTable, over);
            owner.Merge(database.Root, over);
        }

        public void Save()
        {
            string bakFileName = FileName + ".bak";
            string tmpFileName = FileName + ".tmp";
            SaveAs(tmpFileName);
            if (File.Exists(bakFileName))
                File.Delete(bakFileName);
            File.Move(FileName, bakFileName);
            File.Move(tmpFileName, FileName);
        }

        public void SaveAs(string fileName)
        {
            if (fileName == null)
                return;

            var dict =
                new Dictionary<string, XElement> 
                { 
                    { "Root", Root.ToX() },
                    { "Config", ConfigDictionary.ToX() }
                };
            
            ZipUtils.Compress(
                fileName, 
                dict, 
                ImagePartTable,
                FunctionTable);
        }

        /// <summary>
        /// 按给定的符号索引和名称重定位元件定义
        /// </summary>
        /// <param name="part">元件定义</param>
        /// <param name="index">符号索引</param>
        /// <param name="name">名称</param>
        public void Redirect(ImagePart part, SymbolIndex index, string name)
        {
            var oldName = part.Name;

            var oldid = part.Index;
            var folders =
                Root
                .GetAllFolders()
                .Where(f => f.HasPartIndex(oldid));
            ImagePartTable.Redirect(part, index);
            foreach (var folder in folders)
                folder.Redirect(oldid, index);

            if (oldName != name)
                part.Rename(name);
        }








    }

}
