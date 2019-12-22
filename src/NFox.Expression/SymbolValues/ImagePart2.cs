using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using TlsCad.Expression;
using System.IO;
using System.Windows.Forms;
using TlsCad.Expression.Runtime;
using TlsCad.Expression.DataSystem;

namespace TlsCad.Expression.SymbolValues
{

    public abstract class ImagePart2 : Part, ISymbol
    {

        public event Part.EventHandler PartRenaming;

        #region Member

        public virtual Image2D Image
        { protected set; get; }

        public override bool IsFolder
        {
            get { return false; }
        }

        public override bool IsImage
        {
            get { return true; }
        }

        public abstract bool IsGeneral { get; }
        public abstract bool IsParameterized { get; }

        public override string Description
        {
            get
            {
                string format = "{0}:{1}";
                string s = string.Format(format, "名称", Name);
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
                PartRenaming(null, new PartEventArgs(this) { Tag = newName, });
        }

        public override string ToString()
        {
            return ToX().ToString();
        }

        public override bool HasParams
        {
            get { throw new NotImplementedException(); }
        }

        public SymbolIndex Index
        {
            set
            {
                var name = value.DictionaryName;
                if (string.IsNullOrEmpty(name) || name == "Main")
                {
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

        public virtual void CopyFrom(ImagePart part) { }

    }

    

   


}
