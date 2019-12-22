
using System.Collections.Generic;
using System.Xml.Linq;

using NFox.Expression.DataSystem;

namespace NFox.Geometry
{
    public class NurbsData : IParser
    {

        public KnotCollection Knots
        { private set; get; }

        public List<Point2D> ControlPoints
        { private set; get; }

        public int Degree
        { internal set; get; }
        public bool Closed
        { internal set; get; }

        public NurbsData()
        {
            Knots = new KnotCollection(this);
            ControlPoints = new List<Point2D>();
        }

        public NurbsData(List<double> knots, int degree, bool closed)
        {
            Knots = new KnotCollection(this);
            Knots.AddRange(knots);
            ControlPoints = new List<Point2D>();
            Degree = degree;
            Closed = closed;
        }

        public NurbsData(List<Point2D> controlPoints, List<double> knots, int degree, bool closed)
        {
            Degree = degree;
            Closed = closed;
            int num = controlPoints.Count -2;
            Knots = new KnotCollection(this);
            if (knots[0] <= knots[1] && knots[0] <= 0)
            {
                Closed = knots[0] < 0;
                for (int i = degree; i < knots.Count - degree; i++)
                    Knots.Add(knots[i]);
            }
            else
            {
                Knots.AddRange(knots);
            }

            ControlPoints = new List<Point2D>(controlPoints);
        }

        public void AddControlPoint(Point2D point)
        {
            ControlPoints.Add(point);
        }

        public Point2D GetControlPointAt(int index)
        {
            return ControlPoints[index % ControlPoints.Count];
        }

        public void SetControlPointAt(int index, Point2D point)
        {
            ControlPoints[index % ControlPoints.Count] = point;
        }

        /// <summary>
        /// 获取参数对应点
        /// </summary>
        /// <param name="par">参数</param>
        /// <returns>参数对应点</returns>
        public Point2D GetPointAtParam(double par)
        {
            int span = Knots.FindSpan(par);
            var nn = Knots.BasicFuns(span, par);
            Point2D pt = new Point2D();
            int id = span - Degree;
            for (int i = 0; i <= Degree; i++)
                pt += GetControlPointAt(id + i) * nn[i];
            return pt;
        }

        public void FromX(XElement xe)
        {
            Closed = bool.Parse(xe.Attribute("Closed").Value);
            Degree = 3;
            ControlPoints.Clear();
            foreach (var pt in xe.Element("ControlPoints").Elements())
                ControlPoints.Add(XParser.Parse<Point2D>(pt));
            Knots.FromX(xe.Element("Knots"));
        }

        public void ToX(XElement xe)
        {
            var closed = Closed;
            if (GeoUtils.Equals(ControlPoints[0], ControlPoints[ControlPoints.Count - 1]))
                closed = true;

            xe.Add(new XAttribute("Closed", closed));
            xe.Add(new XAttribute("Degree", Degree));
            var controlPoints = new XElement("ControlPoints");
            xe.Add(controlPoints);
            foreach (var pt in ControlPoints)
                controlPoints.Add(pt.ToX("Point"));
            xe.Add(Knots.ToX());
        }

        public string XName
        {
            get { return "NurbsData"; }
        }

        

    }
}
