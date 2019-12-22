using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;
using System.Windows.Forms;
using NFox.Expression;
using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;

namespace NFox.Expression.SymbolValues
{

    public abstract class Part : ISymbolValue
    {


        #region Member

        public string Name { set; get; }

        public string LongName { set; get; }

        public virtual Database Database { set; get; }

        public abstract bool IsFolder { get; }
        public abstract bool IsImage { get; }

        public abstract bool HasParams { get; }

        public List<PartAttrib> Attributes = new List<PartAttrib>();

        public virtual string Description
        {
            get { return ""; }
        }

        #endregion

        protected Part()
        {
        }

        public delegate void EventHandler(object sender, PartEventArgs e);

        public abstract Part Copy();

        public abstract void Rename(string newName);

        public abstract void ToX(XElement xe);
        public abstract void FromX(XElement xe);
        public abstract string XName { get; }

        public void LoadAttributeInfos(XElement xe)
        {
            var xatts = xe.Element("Attributes");
            if (xatts != null)
            {
                Attributes = new List<PartAttrib>();
                foreach (var xatt in xatts.Elements("Attribute"))
                {
                    PartAttrib att = new PartAttrib();
                    att.FromX(xatt);
                    Attributes.Add(att);

                }
            }
        }

        protected void SaveAttributeInfos(XElement xe)
        {
            if (Attributes.Count > 0)
            {
                var xatts = new XElement("Attributes");
                xe.Add(xatts);
                foreach (var att in Attributes)
                    if (att.Name != null) xatts.Add(att.ToX());
            }
        }

        public virtual SymbolIndex Index { get; set; }

    }

    public class PartEventArgs : EventArgs
    {
        public Part Part { set; get; }
        public object Tag { set; get; }

        public PartEventArgs(Part part)
        {
            Part = part;
        }
    }
}
