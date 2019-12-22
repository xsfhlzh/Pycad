
using System;
using System.Xml.Linq;
using System.Drawing.Drawing2D;

using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;
using System.Collections.Generic;
using System.Drawing;

namespace NFox.Geometry
{
    public sealed class CircleArc2D : Curve2D
    {

        public CircleArc2D() { }

        public CircleArc2D(Point2D center, double radius)
        {

            Center = center;
            Radius = radius;

            StartAngle = Angle.Zero;
            EndAngle = Angle.Degree360;

        }

        public CircleArc2D(Point2D center, double radius, Angle startAngle, Angle endAngle)
        {

            Center = center;
            Radius = radius;

            StartAngle = startAngle;
            EndAngle = endAngle;

        }

        public CircleArc2D(Point2D start, Point2D end, double bulge)
        {

            int sign = Math.Sign(bulge);
            IsClockWise = sign == -1;
            bulge = Math.Abs(bulge);

            Point2D cen = (start + end) / 2;
            Vector2D vec = (end - start) / 2;
            vec = vec.RotateBy(Angle.Degree90);
            vec *= (1 - bulge) * sign;
            Center = cen + vec;

            vec = start - Center;
            Radius = vec.Length;
            StartAngle = vec.Angle;
            EndAngle = (end - Center).Angle;

        }

        public CircleArc2D(Point2D pt1, Point2D pt2, Point2D pt3)
            : this(pt1, pt2, pt3, false)
        {
            
        }

        public CircleArc2D(Point2D pt1, Point2D pt2, Point2D pt3, bool isWholeCircle)
        {

            if (isWholeCircle)
            {
                var xy1 = Math.Pow(pt1.X, 2) + Math.Pow(pt1.Y, 2);
                var xy2 = xy1 - Math.Pow(pt3.X, 2) - Math.Pow(pt3.Y, 2);
                var xy3 = xy1 - Math.Pow(pt2.X, 2) - Math.Pow(pt2.Y, 2);
                xy1 = (pt1.X - pt2.X) * (pt1.Y - pt3.Y) - (pt1.X - pt3.X) * (pt1.Y - pt2.Y);
                if (GeoUtils.Equals(xy1, 0))
                    throw new Exception("无法创建圆!");

                Center =
                    new Point2D(
                        (xy3 * (pt1.Y - pt3.Y) - xy2 * (pt1.Y - pt2.Y)) / (2 * xy1),
                        (xy2 * (pt1.X - pt2.X) - xy3 * (pt1.X - pt3.X)) / (2 * xy1));

                Radius = (pt1 - Center).Length;
                if (GeoUtils.Equals(Radius, 0))
                    throw new Exception("半径为零!");

                StartAngle = Angle.Zero;
                EndAngle = Angle.Degree360;

            }
            else
            {
                CircleArc2D cir = new CircleArc2D(pt1, pt2, pt3, true);
                Center = cir.Center;
                Radius = cir.Radius;

                IsClockWise = 
                    Vector2D.IsClockWise(
                        pt1 - cir.Center, 
                        pt2 - cir.Center, 
                        pt3 - cir.Center);

            }
        }


        #region Member

        public Point2D Center;
        public double Radius;
        public Angle StartAngle;
        public Angle EndAngle;
        public bool IsClockWise;

        public Angle TotalAngle
        {
            get
            {
                return 
                    IsClockWise ? 
                    StartAngle - EndAngle : 
                    EndAngle - StartAngle;
            }
        }

        public double Diameter
        {
            get { return Radius * 2; }
        }

        public Point2D StartPoint
        {
            get { return Center + new Vector2D(Radius, StartAngle); }
        }

        public Point2D EndPoint
        {
            get { return Center + new Vector2D(Radius, EndAngle); }
        }

        #endregion

        #region Entity

        public override Entity2D Copy()
        {
            var cir =
                new CircleArc2D(
                    Center,
                    Radius,
                    StartAngle,
                    EndAngle);
            cir.LayerName = LayerName;
            return cir;
        }

        public override void FromX(XElement xe)
        {

            Center = Point2D.Parse(xe.Attribute("Center").Value);
            Radius = double.Parse(xe.Attribute("Radius").Value);

            if (xe.Attribute("StartAngle") == null)
            {
                StartAngle = Angle.Zero;
                EndAngle = Angle.Degree360;
            }
            else
            {
                StartAngle = Angle.FormDegree(double.Parse(xe.Attribute("StartAngle").Value));
                EndAngle = Angle.FormDegree(double.Parse(xe.Attribute("EndAngle").Value));
            }
        }

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Center", Center.ToString()));
            xe.Add(new XAttribute("Radius", Radius));
            if (!Closed)
            {
                xe.Add(new XAttribute("StartAngle", StartAngle.Degree));
                xe.Add(new XAttribute("EndAngle", EndAngle.Degree));
            }
            MakeLayer(xe);
        }

        public override string XName
        {
            get { return "CircleArc"; }
        }

        public override IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path)
        {
            var rec =
                new Rectangle2D(
                    Center.X - Radius,
                    Center.Y - Radius,
                    Diameter,
                    Diameter);
            if (IsClockWise)
                path.AddArc(rec, StartAngle, -TotalAngle);
            else
                path.AddArc(rec, StartAngle, TotalAngle);
            path.StartFigure();
            yield return 0;
            yield break;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="mat"></param>
        public override void TransformBy(Matrix2D mat)
        {
            var vec1 = GetPointAtParam((StartParam + EndParam) / 2) - Center;
            Center *= mat;
            var vec = Vector2D.XAxis * mat;
            Radius *= vec.Length;
            if (!Closed)
            {
                var vec0 = new Vector2D(Radius, StartAngle) * mat;
                vec1 *= mat;
                var vec2 = new Vector2D(Radius, EndAngle)* mat;
                StartAngle = vec0.Angle;
                EndAngle = vec2.Angle;
                IsClockWise = Vector2D.IsClockWise(vec0, vec1, vec2);
            }
        }

        #endregion

        #region Curve2D

        public override double Length
        {
            get { return TotalAngle.Radian * Radius; }
        }

        public override bool Closed
        {
            get { return StartAngle.IsZero() && EndAngle.IsWholeCircle(); }
        }

        public override double StartParam
        {
            get { return 0; }
        }

        public override double EndParam
        {
            get { return TotalAngle; }
        }

        public override Point2D GetPointAtParam(double par)
        {
            Vector2D vec = new Vector2D(Radius, StartAngle);
            Angle angle = new Angle(IsClockWise ? -par : par);
            return Center + vec.RotateBy(angle);
        }

        #endregion

    }
}
