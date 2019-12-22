
using System.Xml.Linq;
using System.Drawing.Drawing2D;

using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;
using System.Collections.Generic;
using System.Drawing;

namespace NFox.Geometry
{

    public sealed class LineSegment2D : Curve2D
    {

        public LineSegment2D() { }

        public LineSegment2D(Point2D start, Point2D end)
        {
            StartPoint = start;
            EndPoint = end;
        }

        public LineSegment2D(Point2D start, Angle angle, double length)
        {
            StartPoint = start;
            EndPoint = start + new Vector2D(length, angle);
        }

        public LineSegment2D(Point2D start, Angle angle, double minlength, double maxlength)
        {
            StartPoint = start + new Vector2D(minlength, angle);
            EndPoint = start + new Vector2D(maxlength, angle);
        }

        Point2D? IntersectWith(LineSegment2D other)
        {
            var d0 = Delta;
            var d1= other.Delta;
            if (!d0.IsParallelTo(d1))
            {
                var e = other.StartPoint - StartPoint;
                double s = e.CrossProduct(d1) / d0.CrossProduct(d1);
                return StartPoint + d0 * s;
            }
            return null;
        }

        #region Member

        public Point2D StartPoint;
        public Point2D EndPoint;
        public Vector2D Delta { get { return EndPoint - StartPoint; } }

        #endregion

        #region Entity

        public override Entity2D Copy()
        {
            var line =
                new LineSegment2D(
                    StartPoint,
                    EndPoint);
            line.LayerName = LayerName;
            return line;
        }

        public override void FromX(XElement xe)
        {
            StartPoint = Point2D.Parse(xe.Attribute("Start").Value);
            EndPoint = Point2D.Parse(xe.Attribute("End").Value);
        }

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Start", StartPoint.ToString()));
            xe.Add(new XAttribute("End", EndPoint.ToString()));
            MakeLayer(xe);
        }

        public override string XName
        {
            get { return "Line"; }
        }

        public override IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path)
        {
            path.AddLine(StartPoint, EndPoint);
            path.StartFigure();
            yield return 0;
            yield break;
        }

        public override void TransformBy(Matrix2D mat)
        {
            StartPoint *= mat;
            EndPoint *= mat;
        }

        #endregion

        #region Curve2D

        public override bool Closed
        {
            get { return false; }
        }

        public override double Length
        {
            get { return Delta.Length; }
        }

        public override double StartParam
        {
            get { return 0; }
        }

        public override double EndParam
        {
            get { return 1; }
        }

        public override Point2D GetPointAtParam(double par)
        {
            return StartPoint + Delta * par;
        }

        #endregion



    }

}
