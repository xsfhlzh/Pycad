
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Xml.Linq;

namespace NFox.Geometry
{
    public struct Vector2D : IComparer<Vector2D>
    {

        /// <summary>
        /// 按笛卡尔坐标系初始化向量
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        public Vector2D(double x, double y)
        {
            _x = x;
            _y = y;
        }

        /// <summary>
        /// 按极坐标创建向量
        /// </summary>
        /// <param name="len"></param>
        /// <param name="angle"></param>
        /// <returns></returns>
        public Vector2D(double len, Angle angle)
        {
            _x = len * Math.Cos(angle);
            _y = len * Math.Sin(angle);
        }

        public Vector2D(double[] arr)
        {
            _x = arr[0];
            _y = arr[1];
        }

        public static Vector2D Parse(string value)
        {
            var arr = value.Split(',');
            return
                new Vector2D(
                    double.Parse(arr[0]),
                    double.Parse(arr[1]));
        }

        public Vector2D Round()
        {
            return
                new Vector2D(
                    GeoUtils.Round(_x),
                    GeoUtils.Round(_y));
        }

        public string XName
        {
            get { return "Vector"; }
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
                    default:
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

        #region Member



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

        /// <summary>
        /// 角度
        /// </summary>
        public Angle Angle
        {
            get { return new Angle(Math.Atan2(Y, X)); }
        }

        /// <summary>
        /// 长度
        /// </summary>
        public double Length
        {
            get { return Math.Sqrt(X * X + Y * Y); }
        }

        /// <summary>
        /// 单位向量
        /// </summary>
        public Vector2D UnitVector
        {
            get
            { return this / Length; }
        }

        /// <summary>
        /// X轴单位向量
        /// </summary>
        public static Vector2D XAxis
        {
            get { return new Vector2D(1, 0); }
        }

        /// <summary>
        /// Y轴单位向量
        /// </summary>
        public static Vector2D YAxis
        {
            get { return new Vector2D(0, 1); }
        }

        public static Vector2D Zreo
        {
            get { return new Vector2D(); }
        }

        public bool IsZreo
        {
            get 
            {
                return
                    GeoUtils.Equals(X, 0, GeoUtils.EqualsVector) &&
                    GeoUtils.Equals(Y, 0, GeoUtils.EqualsVector);
            }
        }

        #endregion

        #region operator

        public static implicit operator SizeF(Vector2D vec)
        {
            return new SizeF((float)vec.X, (float)vec.Y);
        }


        public static Vector2D operator *(Vector2D vec, Matrix2D mat)
        {
            return vec.TransformBy(mat);
        }

        /// <summary>
        /// 左乘矩阵
        /// </summary>
        /// <param name="mat"></param>
        /// <returns></returns>
        public Vector2D TransformBy(Matrix2D mat)
        {
            return
                new Vector2D(
                    mat[0, 0] * X + mat[0, 1] * Y,
                    mat[1, 0] * X + mat[1, 1] * Y);
        }

        public static Vector2D operator *(Vector2D vec, double scale)
        {
            return new Vector2D(vec.X * scale, vec.Y * scale);
        }

        public static Vector2D operator /(Vector2D vec, double scale)
        {
            return new Vector2D(vec.X / scale, vec.Y / scale);
        }

        public static Vector2D operator +(Vector2D vec1, Vector2D vec2)
        {
            return
                new Vector2D(
                    vec1.X + vec2.X,
                    vec1.Y + vec2.Y);
        }

        public static Vector2D operator -(Vector2D vec1, Vector2D vec2)
        {
            return
                new Vector2D(
                    vec1.X - vec2.X,
                    vec1.Y - vec2.Y);
        }

        public static Vector2D operator -(Vector2D vec)
        {
            return new Vector2D(-vec.X, -vec.Y);
        }

        public static bool operator ==(Vector2D v1, Vector2D v2)
        {
            return
                GeoUtils.Equals(v1.X, v2.X, GeoUtils.EqualsPoint) &&
                GeoUtils.Equals(v1.Y, v2.Y, GeoUtils.EqualsPoint);
        }

        public static bool operator !=(Vector2D v1, Vector2D v2)
        {
            return !(v1 == v2);
        }

        /// <summary>
        /// 点乘
        /// </summary>
        /// <param name="vec"></param>
        /// <returns></returns>
        public double DotProduct(Vector2D vec)
        {
            return X * vec.X + Y * vec.Y;
        }

        /// <summary>
        /// 叉乘
        /// </summary>
        /// <param name="vec"></param>
        /// <returns></returns>
        public double CrossProduct(Vector2D vec)
        {
            return X * vec.Y - Y * vec.X;
        }

        /// <summary>
        /// 获取旋转后的向量
        /// </summary>
        /// <param name="angle"></param>
        /// <returns></returns>
        public Vector2D RotateBy(Angle angle)
        {
            return TransformBy(Matrix2D.Rotation(angle));
        }

        public Angle GetAngleTo(Vector2D vec)
        {
            return Angle - vec.Angle;
        }

        public Vector2D Mirror(Vector2D vec)
        {
            return TransformBy(Matrix2D.Mirror(vec));
        }

        public bool IsCodirectionalTo(Vector2D vec)
        {
            return IsParallelTo(vec) && DotProduct(vec) > 0;
        }

        public bool IsParallelTo(Vector2D vec)
        {
            return GeoUtils.Equals(CrossProduct(vec), 0);
        }

        public bool IsPerpendicularTo(Vector2D vec)
        {
            return GeoUtils.Equals(DotProduct(vec), 0);
        }

        #endregion

        #region Compare

        public override bool Equals(object obj)
        {
            if (obj is Vector2D)
            {
                var v2 = (Vector2D)obj;
                return
                    GeoUtils.Equals(X, v2.X, GeoUtils.EqualsVector) &&
                    GeoUtils.Equals(Y, v2.Y, GeoUtils.EqualsVector);
            }
            return false;
        } 

        public override int GetHashCode()
        {
            return X.GetHashCode() ^ Y.GetHashCode();
        }

        public int Compare(Vector2D v1, Vector2D v2)
        {
            if (GeoUtils.Equals(v1.X, v2.X, GeoUtils.EqualsVector))
            {
                if (GeoUtils.Equals(v1.Y, v2.Y, GeoUtils.EqualsVector))
                    return 0;
                else
                    return v1.Y.CompareTo(v2.Y);
            }
            return v1.X.CompareTo(v2.X);
        }

        #endregion

        public static bool IsClockWise(Vector2D start, Vector2D center, Vector2D end)
        {
            var startAngle = start.Angle;
            var endAngle = end.Angle;
            var angle = center.Angle;
            return !((startAngle < angle) ^ (angle < endAngle) ^ (startAngle < endAngle));
        }

        public override string ToString()
        {
            return string.Format("{0},{1}", X, Y); ;
        }

    }
}
