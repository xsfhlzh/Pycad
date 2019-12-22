using NFox.Expression.DataSystem;
using NFox.Expression.Runtime;
using System.Xml.Linq;

namespace NFox.Expression.SymbolValues
{
    public class ImagePart : Part
    {

        public event Part.EventHandler PartRenaming;

        #region Member

        public override SymbolIndex Index
        {
            set
            {
                var name = value.DictionaryName;
                if (string.IsNullOrEmpty(name) || name == "Main")
                {
                    Name = value.Key;
                    Standard = null;
                    No = null;
                }
                else
                {
                    Standard = value.DictionaryName;
                    No = value.Key;
                }
            }
            get
            {
                if (Standard == null)
                    return new SymbolIndex(Name);
                return new SymbolIndex(Standard, No);
            }
        }

        public string Standard { protected set; get; }
        public string No { protected set; get; }

        public virtual Image2D Image
        { set; get; }

        public override bool IsFolder
        {
            get { return false; }
        }

        public override bool IsImage
        {
            get { return true; }
        }

        public override bool HasParams
        {
            get { return false; }
        }

        public virtual bool IsParameterized
        {
            get { return false; }
        }

        public override string Description
        {
            get
            {
                string format = "{0}:{1}";
                string s = string.Format(format, "简称", Name);
                s += "\n" + string.Format(format, "全名", LongName);
                s += "\n" + string.Format(format, "所属标准", Index.DictionaryName);
                s += "\n" + string.Format(format, "标准序号", Index.Key);
                foreach (var att in Attributes)
                    s += "\n" + string.Format(format, att.Name, att.Value);
                return s;
            }
        }

        #endregion

        public override void Rename(string newName)
        {
            Name = newName;
            if (PartRenaming != null)
                PartRenaming(null, new PartEventArgs(this) { Tag = Name, });
        }

        protected void LoadStandardInfo(XElement xe)
        {
            var a = xe.Attribute("Standard");
            if (a != null)
            {
                Standard = a.Value;
                No = xe.Attribute("No").Value;
            }
        }

        protected void SaveStandardInfo(XElement xe)
        {
            if (Standard != null)
            {
                xe.Add(new XAttribute("Standard", Standard));
                xe.Add(new XAttribute("No", No));
            }
        }

        public override Part Copy()
        {
            return this;
        }

        public override string XName
        {
            get { return "General"; }
        }

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Name", Name));
            xe.Add(new XAttribute("LongName", LongName ?? ""));
            xe.Add(Image.ToX());
            SaveStandardInfo(xe);
            SaveAttributeInfos(xe);
        }

        public override void FromX(XElement xe)
        {
            Name = xe.Attribute("Name").Value;
            LongName = xe.Attribute("LongName").Value;
            Image = new Image2D();
            Image.FromX(xe.Element("Image"));
            LoadStandardInfo(xe);
            LoadAttributeInfos(xe);
        }

        public virtual void CopyFrom(ImagePart image)
        {
            Image = image.Image;
        }

    }
}
