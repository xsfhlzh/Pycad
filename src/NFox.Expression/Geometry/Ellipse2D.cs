
using System;
using System.Xml.Linq;
using System.Drawing.Drawing2D;

using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;
using System.Drawing;
using System.Collections.Generic;

namespace NFox.Geometry
{
    public class Ellipse2D : Curve2D
    {

        public Ellipse2D() { }

        public Ellipse2D(Point2D center, double major, double minor, Angle rotation, Angle startAngle, Angle endAngle)
        {
            Center = center;
            Major = major;
            Minor = minor;
            Rotation = rotation;
            StartAngle = startAngle;
            EndAngle = endAngle;
        }

        public Ellipse2D(Point2D center, double major, double minor, Angle rotation)
        {
            Center = center;
            Major = major;
            Minor = minor;
            Rotation = rotation;
            StartAngle = Angle.Zero;
            EndAngle = Angle.Degree360;
        }

        #region Member

        public Point2D Center;
        public double Major;
        public double Minor;
        public Angle Rotation;
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

        public Vector2D MajorAxis
        {
            get { return new Vector2D(Major, Rotation); }
        }

        public Vector2D MinorAxis
        {
            get { return Vector2D.YAxis.RotateBy(Rotation) * Minor; }
        }

        #endregion

        #region Entity

        public override Entity2D Copy()
        {
            var ell =
                new Ellipse2D(
                    Center,
                    Major,
                    Minor,
                    Rotation,
                    StartAngle,
                    EndAngle);
            ell.LayerName = LayerName;
            return ell;
        }


        public override void FromX(XElement xe)
        {

            Center = Point2D.Parse(xe.Attribute("Center").Value);
            Major = double.Parse(xe.Attribute("Major").Value);
            Minor = double.Parse(xe.Attribute("Minor").Value);
            Rotation = Angle.FormDegree(double.Parse(xe.Attribute("Rotation").Value));
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
            xe.Add(new XAttribute("Rotation", Rotation.Degree));
            xe.Add(new XAttribute("Major", Major));
            xe.Add(new XAttribute("Minor", Minor));
            if (!Closed)
            {
                xe.Add(new XAttribute("StartAngle", StartAngle.Degree));
                xe.Add(new XAttribute("EndAngle", EndAngle.Degree));
            }
            MakeLayer(xe);
        }

        public override string XName
        {
            get { return "Ellipse"; }
        }

        public override IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path)
        {

            var epath = new GraphicsPath();

            var rec =
                new Rectangle2D(
                    -Major,
                    -Minor,
                    Major * 2,
                    Minor * 2);
            if (IsClockWise)
                epath.AddArc(rec, StartAngle, -TotalAngle);
            else
                epath.AddArc(rec, StartAngle, TotalAngle);
            epath.StartFigure();

            Matrix m = new Matrix();
            if (!Rotation.IsZero())
                m.Rotate(Rotation, MatrixOrder.Append);
            m.Translate((float)Center.X, (float)Center.Y, MatrixOrder.Append);
            epath.Transform(m);

            path.AddPath(epath, false);
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
            var pt0 = GetPointAtParam(StartParam);
            var pt1 = GetPointAtParam((StartParam + EndParam)/ 2);
            var pt2 = GetPointAtParam(EndParam);
            pt0 *= mat;
            pt1 *= mat;
            pt2 *= mat;
            var vec = MinorAxis * mat;
            Minor = vec.Length;
            vec = MajorAxis * mat;
            Major = vec.Length;
            Center *= mat;
            Rotation = vec.Angle;
            var vec0 = pt0 - Center;
            var vec2 = pt2 - Center;
            StartAngle = vec0.Angle - Rotation;
            EndAngle = vec2.Angle - Rotation;
            IsClockWise = Vector2D.IsClockWise(vec0, pt1 - Center, vec2);
        }

        #endregion

        #region Curve2D

        public override bool Closed
        {
            get { return GeoUtils.Equals(StartAngle, 0f) && GeoUtils.Equals(EndAngle, 360f); }
        }

        public override double Length
        {
            get { throw new NotImplementedException(); }
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

            Angle angle = StartAngle + new Angle(IsClockWise ? -par : par);
            Vector2D vec =
                new Vector2D(
                    Major * Math.Cos(angle),
                    Minor * Math.Sin(angle));
            return Center + vec.RotateBy(Rotation);


        }

        #endregion

    }
}
