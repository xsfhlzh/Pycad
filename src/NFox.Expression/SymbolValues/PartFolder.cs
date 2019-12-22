using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using System.IO;
using System.Windows.Forms;
using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;

namespace NFox.Expression.SymbolValues
{

    public class PartFolder : Part, IEnumerable<Part>
    {

        public PartFolder() { }

        public PartFolder(DirectoryInfo dir, Func<string, FileInfo, ImagePart> makeOtherFile)
        {
            Name = dir.Name;
            foreach (var subdir in dir.GetDirectories())
                Add(new PartFolder(subdir, makeOtherFile));
            foreach (var file in dir.GetFiles())
            {
                var ext = file.Extension.ToLower();
                ImagePart part;
                switch (ext)
                {
                    case ".px":
                        var xe = XElement.Load(file.FullName);
                        part = XParser.Parse<ParameterizedPart>(xe);
                        break;
                    default:
                        part = makeOtherFile(ext, file);
                        break;
                }
                if (part != null) Add(part);
            }
        }

        
        #region Member

        public PartFolder Parent { internal set; get; }

        public bool IsRoot
        {
            get { return Parent == null; }
        }

        public PartFolder Root
        {
            get
            {
                var folder = this;
                while (folder.Parent != null)
                    folder = folder.Parent;
                return folder;
            }
        }

        private SortedList<SymbolIndex> _partIndexs = new SortedList<SymbolIndex>();
        public SortedList<SymbolIndex> PartIndexs
        {
            get { return _partIndexs; }
        }

        private List<PartFolder> _folders = new List<PartFolder>();
        public List<PartFolder> Folders
        {
            get { return _folders; }
        }


        public override bool HasParams
        {
            get { return false; }
        }

        public override bool IsFolder
        {
            get { return true; }
        }

        public override bool IsImage
        {
            get { return false; }
        }

        #endregion

        #region Add Remove

        public event Part.EventHandler PartAdding;
        public event Part.EventHandler PartRemoving;
        public event Part.EventHandler PartRenaming;

        public void Add(ImagePart part)
        {

            var ipt = Database.ImagePartTable;
            var index = part.Index;
            if (ipt.Has(index))
            {
                var oldpart = ipt[index];
                 var res = MessageBox.Show(
                    string.Format("是否替换元件\"{0}\":与现有元件重名", part.Name),
                    "元件定义",
                    MessageBoxButtons.YesNo);
                 if (res == DialogResult.Yes)
                 {
                     ipt[index] = part;
                     if (!HasPartIndex(index))
                         Add(index);
                 }
            }
            else
            {
                ipt.Add(part);
                Add(part.Index);
            }
        }

        public void Add(SymbolIndex index)
        {
            _partIndexs.Add(index);
            if (PartAdding != null)
                PartAdding(this, new PartEventArgs(Database.ImagePartTable[index]));
        }

        public void Add(PartFolder folder)
        {
            if (HasFolder(folder.Name))
            {
                MessageBox.Show(
                    string.Format("无法新建文件夹\"{0}\":与现有文件夹重名", folder.Name),
                    "新建文件夹时出错");
                return;
            }
            folder.Parent = this;
            folder.Database = Database;
            _folders.Add(folder);
            if (PartAdding != null)
                PartAdding(this, new PartEventArgs(folder));
        }

        public void Remove(SymbolIndex index)
        {
            _partIndexs.Remove(index);
            if (PartRemoving != null)
                PartRemoving(this, new PartEventArgs(Database.ImagePartTable[index]));
        }


        public void Remove(PartFolder folder)
        {
            _folders.Remove(folder);
            if (PartRemoving != null)
                PartRemoving(this, new PartEventArgs(folder));
        }

        /// <summary>
        /// 将源分支合并到目标分支
        /// </summary>
        /// <param name="folder">源</param>
        /// <param name="over">是否覆盖元件数据</param>
        internal void Merge(PartFolder folder, bool over)
        {

            PartFolder subFolder;
            if (HasFolder(folder.Name))
            {
                subFolder = GetFolder(folder.Name);
            }
            else
            {
                subFolder = new PartFolder { Name = folder.Name };
                Add(subFolder);
            }

            foreach (var index in folder.GetPartIndexs())
            {
                if (!subFolder.HasPartIndex(index))
                    subFolder.Add(index);
            }

            foreach (var f in folder.Folders)
            {
                subFolder.Merge(f, over);
            }

        }


        internal void Redirect(SymbolIndex index, SymbolIndex newIndex)
        {
            _partIndexs.Remove(index);
            _partIndexs.Add(newIndex);
        }

        public void Clear()
        {
            foreach (var index in _partIndexs)
                Remove(index);
            foreach (var folder in _folders)
                Remove(folder);
        }

        public override void Rename(string newName)
        {
            if (!IsRoot && Parent.HasFolder(newName))
            {
                MessageBox.Show(
                    string.Format("无法重命名\"{0}\":指定的项目与现有项目重名", newName),
                    "重命名时出错");
            }
            else
            {
                Name = newName;
                if (PartRenaming != null)
                    PartRenaming(null, new PartEventArgs(this) { Tag = newName, });
            }
        }


        #endregion

        #region Has

        public bool HasFolder(string name)
        {
            foreach (var f in _folders)
                if (f.Name == name) return true;
            return false;
        }

        public bool HasPartIndex(SymbolIndex index)
        {
            foreach (var i in _partIndexs)
            {
                if (i.Equals(index))
                    return true;
            }
            return false;
        }

        #endregion

        #region GetPart

        public PartFolder GetFolder(string name)
        {
            foreach (var f in _folders)
                if (f.Name == name) return f;
            return null;
        }

        public IEnumerable<PartFolder> GetFolders()
        {
            foreach (var folder in _folders)
                yield return folder; 
        }

        public IEnumerable<PartFolder> GetAllFolders()
        {
            foreach (var folder in _folders)
            {
                foreach (var f in folder.GetAllFolders())
                    yield return f;
                yield return folder;
            }
        }

        public IEnumerable<T> GetAllParts<T>() where T : ImagePart
        {
            return GetAllParts().OfType<T>();
        }

        public IEnumerable<ImagePart> GetAllParts()
        {
            return
                GetAllPartIndexs()
                .Select(i => Database.ImagePartTable[i]);
        }

        public IEnumerable<SymbolIndex> GetAllPartIndexs()
        {

            foreach (var index in _partIndexs)
                yield return index;

            foreach (var folder in _folders)
            {
                foreach (var index in folder.GetAllPartIndexs())
                    yield return index;
            }

        }

        public IEnumerable<SymbolIndex> GetPartIndexs()
        {
            return _partIndexs;
        }

        public IEnumerable<ImagePart> GetParts()
        {
            return _partIndexs.Select(i => Database.ImagePartTable[i]);
        }

        #endregion

        #region ISave

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Name", Name));
            foreach (var pf in _folders) 
                xe.Add(pf.ToX());
            foreach (var p in _partIndexs)
                xe.Add(p.ToX("Part"));
            SaveAttributeInfos(xe);
        }

        public override string XName
        {
            get { return "Folder"; }
        }

        public override void FromX(XElement xe)
        {
            XAttribute att = xe.Attribute("Root");
            Name = xe.Attribute("Name").Value;
            foreach (var e in xe.Elements())
            {
                if (e.Name.LocalName == "Folder")
                    XParser.Parse<PartFolder>(e, f => Add(f));
                else
                    _partIndexs.Add(XParser.Parse<SymbolIndex>(e));
            }
            LoadAttributeInfos(xe); 
        }

        #endregion

        public override Part Copy()
        {
            PartFolder folder = new PartFolder { Name = Name };
            foreach (var f in _folders)
                folder._folders.Add(f.Copy() as PartFolder);
            foreach (var i in _partIndexs)
                folder._partIndexs.Add(i);
            return folder;
        }

        public override string ToString()
        {
            return Name;
        }


        public IEnumerator<Part> GetEnumerator()
        {
            foreach (var folder in _folders)
                yield return folder;
            foreach (var index in _partIndexs)
                yield return Database.ImagePartTable[index];
        }

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

    }
}
