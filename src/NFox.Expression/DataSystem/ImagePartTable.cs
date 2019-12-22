
using NFox.Expression.SymbolValues;
using System.Xml.Linq;

namespace NFox.Expression.DataSystem
{

    public class ImagePartTable : SymbolTable<ImagePart>
    {

        protected override ImagePart FromX(XElement xe)
        {
            switch (xe.Name.LocalName)
            {
                case "Parameterized":
                    return XParser.Parse<ParameterizedPart>(xe);
                default:
                    return base.FromX(xe);
            }
        }

        protected override string Prefix
        {
            get { return "ImagePartTable/"; }
        }

        protected override string Postfix
        {
            get { return ".pd";}
        }

    }

}
