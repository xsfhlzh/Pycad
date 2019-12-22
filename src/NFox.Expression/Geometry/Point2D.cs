
using System;
using System.Drawing;
using System.Xml.Linq;
using System.Collections.Generic;
using NFox.Expression.DataSystem;

namespace NFox.Geometry
{
    public struct Point2D : IComparer<Point2D>, IParser
    {

        public Point2D(double x, double y)
        {
            _x = x;
            _y = y;
        }

        public Point2D(double[] arr)
            :this(arr[0], arr[1])
        { }

        public static Point2D Parse(string value)
        {
            var arr = value.Split(',');
            return
                new Point2D(
                    double.Parse(arr[0]),
                    double.Parse(arr[1]));
        }

        public Point2D Round()
        {
            return
                new Point2D(
                    GeoUtils.Round(_x),
                    GeoUtils.Round(_y));
        }

        public string XName
        {
            get { return "Point"; }
        }

        public void FromX(XElement xe)
        {
            X = double.Parse(xe.Attribute("X").Value);
            Y = double.Parse(xe.Attribute("Y").Value);
        }

        public void ToX(XElement xe)
        {
            xe.Add(new XAttribute("X", GeoUtils.Round(X)));
            xe.Add(new XAttribute("Y", GeoUtils.Round(Y)));
        }

        public double this[int index]
        {
            get
            {
                switch (index)
                {
                    case 0:
                        return _x;
                    case 1:
                        return _y;
                    default :
                        throw new OverflowException();
                }
            }
            set
            {
                switch (index)
                {
                    case 0:
                        _x = value;
                        return;
                    case 1:
                        _y = value;
                        return;
                    default:
                        throw new OverflowException();
                }

            }
        }

        #region member

        /// <summary>
        /// 元素集合
        /// </summary>
        private double _x, _y;

        public double X
        {
            get { return _x; }
            private set { _x = value; }
        }

        public double Y
        {
            get { return _y; }
            private set { _y = value; }
        }

        public static Point2D Origin
        { 
            get { return new Point2D(); }
        }

        #endregion

        #region operator

        public static implicit operator PointF(Point2D pt)
        {
            return new PointF((float)pt.X, (float)pt.Y);
        }

        /// <summary>
        /// 左乘矩阵
        /// </summary>
        /// <param name="mat"></param>
        /// <returns></returns>
        public Point2D TransformBy(Matrix2D mat)
        {
            return
                new Point2D(
                    mat[0, 0] * X + mat[0, 1] * Y + mat[0, 2],
                    mat[1, 0] * X + mat[1, 1] * Y + mat[1, 2]);
        }

        public static Point2D operator *(Point2D pt, Matrix2D mat)
        {
            return pt.TransformBy(mat);
        }

        public static Point2D operator *(Point2D pt, double scale)
        {
            return new Point2D(pt.X * scale, pt.Y * scale);
        }

        public static Point2D operator /(Point2D pt, double scale)
        {
            return new Point2D(pt.X / scale, pt.Y / scale);
        }

        public static Point2D operator -(Point2D pt)
        {
            return new Point2D(-pt.X, -pt.Y);
        }

        public static Vector2D operator-(Point2D p1, Point2D p2)
        {
            return
                new Vector2D(
                    p1.X - p2.X,
                    p1.Y - p2.Y);
        }

        public static Point2D operator +(Point2D pt, Vector2D vec)
        {
            return
                new Point2D(
                    pt.X + vec.X,
                    pt.Y + vec.Y);
        }

        public static Point2D operator +(Point2D pt, Point2D vec)
        {
            return
                new Point2D(
                    pt.X + vec.X,
                    pt.Y + vec.Y);
        }

        public static Point2D operator -(Point2D pt, Vector2D vec)
        {
            return
                new Point2D(
                    pt.X - vec.X,
                    pt.Y - vec.Y);
        }

        public static bool operator ==(Point2D p1, Point2D p2)
        {
            return
                GeoUtils.Equals(p1.X, p2.X, GeoUtils.EqualsPoint) &&
                GeoUtils.Equals(p1.Y, p2.Y, GeoUtils.EqualsPoint);
        }

        public static bool operator !=(Point2D p1, Point2D p2)
        {
            return !(p1 == p2);
        }

        public Vector2D GetAsVector()
        {
            return new Vector2D(X, Y);
        }

        #endregion

        #region Compare

        public override bool Equals(object obj)
        {
            if (obj is Point2D)
            {
                var p2 = (Point2D)obj;
                return
                    GeoUtils.Equals(X, p2.X, GeoUtils.EqualsPoint) &&
                    GeoUtils.Equals(Y, p2.Y, GeoUtils.EqualsPoint);
            }
            return false;
        }

        public override int GetHashCode()
        {
            return X.GetHashCode() ^ Y.GetHashCode();
        }

        public int Compare(Point2D p1, Point2D p2)
        {
            if (GeoUtils.Equals(p1.X, p2.X, GeoUtils.EqualsPoint))
            {
                if (GeoUtils.Equals(p1.Y, p2.Y, GeoUtils.EqualsPoint))
                    return 0;
                else
                    return p1.Y.CompareTo(p2.Y);
            }
            return p1.X.CompareTo(p2.X);
        }

        #endregion

        public override string ToString()
        {
            return string.Format("{0},{1}", GeoUtils.Round(X), GeoUtils.Round(Y)); ;
        }

    }
}
