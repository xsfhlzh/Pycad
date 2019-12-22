
using NFox.Expression.DataSystem;
using System.Xml.Linq;
namespace NFox.Geometry
{
    public struct BulgeVertex2D : IParser
    {

        public double Bulge;
        public Point2D Position;
        public double StartWidth;
        public double EndWidth;

        public BulgeVertex2D(Point2D pos, double bulge)
        {
            Position = pos;
            Bulge = bulge;
            StartWidth = EndWidth = 0;
        }

        public BulgeVertex2D(Point2D pos, double bulge, double startWidth, double endWidth)
        {
            Position = pos;
            Bulge = bulge;
            StartWidth = startWidth;
            EndWidth = endWidth;
        }

        public BulgeVertex2D(Point2D pos)
        {
            Position = pos;
            Bulge = 0;
            StartWidth = EndWidth = 0;
        }


        public void FromX(XElement xe)
        {
            Position = Point2D.Parse(xe.Attribute("Position").Value);
            Bulge = GetAttribute(xe, "Bulge");
            StartWidth = GetAttribute(xe, "StartWidth");
            EndWidth = GetAttribute(xe, "EndWidth");
        }

        public void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Position", Position.ToString()));
            AddAttribute(xe, "Bulge", GeoUtils.Round(Bulge));
            AddAttribute(xe, "StartWidth", GeoUtils.Round(StartWidth));
            AddAttribute(xe, "EndWidth", GeoUtils.Round(EndWidth));
        }

        public string XName
        {
            get { return "Vertex"; }
        }


        private double GetAttribute(XElement xe, string name)
        {
            var att = xe.Attribute(name);
            if (att == null)
                return 0;
            return double.Parse(xe.Attribute(name).Value);
        }

        private void AddAttribute(XElement xe, string name, double value)
        {
            if (!GeoUtils.Equals(value, 0))
                xe.Add(new XAttribute(name, value));
        }

    }
}
