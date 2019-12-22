using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;

namespace NFox.Expression.SymbolValues
{
    public class ParameterizedPart : ImagePart
    {

        #region Member

        public override Image2D Image
        {
            get
            {
                if (base.Image == null)
                    base.Image = Eval(Function.DefaultParams);
                return base.Image;
            }
        }

        public string Dict { private set; get; }

        public string Alias { private set; get; }

        public Function Function
        {
            get { return Database.FunctionTable[new SymbolIndex(Dict, Alias)]; }
        }

        public int ParamCount
        {
            get { return Function.ParamNames.Count; }
        }

        public override bool HasParams
        {
            get { return ParamCount > 0; }
        }

        public override bool IsParameterized
        {
            get { return true; }
        }

        #endregion

        public override Part Copy()
        {
            var part =
                new ParameterizedPart
                {
                    Database = this.Database,
                    Name = this.Name,
                    Standard = this.Standard,
                    No = this.No,
                    Dict = this.Dict,
                    Alias = this.Alias,
                };
            return part;
        }

        public override string XName
        {
            get { return "Parameterized"; }
        }

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Name", Name));
            xe.Add(new XAttribute("LongName", LongName ?? ""));
            if (Dict != null)
                xe.Add(new XAttribute("Dict", Dict));
            xe.Add(new XAttribute("Alias", Alias));
            SaveStandardInfo(xe);
            SaveAttributeInfos(xe);
        }

        public override void FromX(XElement xe)
        {
            Name = xe.Attribute("Name").Value;
            LongName = xe.Attribute("LongName").Value;
            if (xe.Attribute("Dict") != null)
                Dict = xe.Attribute("Dict").Value;
            Alias = xe.Attribute("Alias").Value;
            LoadStandardInfo(xe);
            LoadAttributeInfos(xe);
        }

        public Image2D Eval(List<string> pars)
        {
            return new Image2D(Function.__call__(pars.ToArray()));
        }

    }
}
