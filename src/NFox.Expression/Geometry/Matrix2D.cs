
using System;
using System.Drawing.Drawing2D;

namespace NFox.Geometry
{
    public struct Matrix2D
    {

        private Matrix2D(double[,] elements)
        {
            _elements = elements;
        }

        public Matrix2D(double m11, double m12, double m21, double m22, double dx, double dy)
        {
            _elements =
                new double[,]
                {
                    { m11, m21, dx },
                    { m12, m22, dy },
                    { 0, 0, 1 }
                };
        }

        public double this[int row, int col]
        {
            set { _elements[row, col] = value; }
            get { return _elements[row, col]; }
        }

        #region Member

        /// <summary>
        /// 元素集合
        /// </summary>
        private double[,] _elements;

        private static Matrix2D _identity = new Matrix2D(1, 0, 0, 1, 0, 0);
        /// <summary>
        /// 单位矩阵
        /// </summary>
        public static Matrix2D Identity
        {
            get { return _identity; }
        }

        #endregion

        #region operator

        /// <summary>
        /// 矩阵相乘
        /// </summary>
        /// <param name="mat1"></param>
        /// <param name="mat2"></param>
        /// <returns></returns>
        public static Matrix2D operator *(Matrix2D mat1, Matrix2D mat2)
        {
            double[,] elements = new double[3, 3];
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    for (int k = 0; k < 3; k++)
                    {
                        elements[i, j] += mat1[i, k] * mat2[k, j];
                    } 
                }
            }
            return new Matrix2D(elements);
        }

        public static implicit operator Matrix(Matrix2D mat)
        {
            return
                new Matrix(
                    (float)mat[0, 0],
                    (float)mat[1, 0],
                    (float)mat[0, 1],
                    (float)mat[1, 1],
                    (float)mat[0, 2],
                    (float)mat[1, 2]);
        }

        /// <summary>
        /// 获取逆矩阵
        /// </summary>
        /// <returns></returns>
        public Matrix2D? Inverse()
        {
            Matrix2D mat = Clone();
            if (GeoUtils.Inverse(ref mat._elements, 3))
                return mat;
            else
                return null;
        }

        /// <summary>
        /// 获取拷贝矩阵
        /// </summary>
        /// <returns></returns>
        public Matrix2D Clone()
        {
            double[,] elements = new double[3, 3];
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    elements[i, j] = _elements[i, j];
                }
            }
            return new Matrix2D(elements);
        }

        /// <summary>
        /// 获取转置矩阵
        /// </summary>
        /// <returns></returns>
        public Matrix2D Transpose()
        {
            Matrix2D mat = Clone();
            mat.Swap(0, 1, 1, 0);
            mat.Swap(0, 2, 2, 0);
            mat.Swap(1, 2, 2, 1);
            return mat;
        }

        /// <summary>
        /// 交换矩阵元素
        /// </summary>
        /// <param name="x1"></param>
        /// <param name="y1"></param>
        /// <param name="x2"></param>
        /// <param name="y2"></param>
        public void Swap(int x1, int y1, int x2, int y2)
        {
            GeoUtils.Swap(ref _elements, x1, y1, x1, y1);
        }

        #endregion

        #region Make

        /// <summary>
        /// 按统一比例的缩放矩阵
        /// </summary>
        /// <param name="xy"></param>
        /// <returns></returns>
        public static Matrix2D Scale(double xy)
        {
            return new Matrix2D(xy, 0, 0, xy, 0, 0);
        }

        /// <summary>
        /// 有基点的按统一比例的缩放矩阵
        /// </summary>
        /// <param name="xy"></param>
        /// <param name="pt"></param>
        /// <returns></returns>
        public static Matrix2D Scale(double xy, Point2D pt)
        {
            return
                Translation(pt) *
                Scale(xy) *
                Translation(-pt);
        }

        /// <summary>
        /// 比例缩放矩阵
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <returns></returns>
        public static Matrix2D Scale(double x, double y)
        {
            return new Matrix2D(x, 0, 0, y, 0, 0);
        }

        /// <summary>
        /// 有基点的比例缩放矩阵
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <param name="pt"></param>
        /// <returns></returns>
        public static Matrix2D Scale(double x, double y, Point2D pt)
        {
            return
                Translation(pt) *
                Scale(x, y) *
                Translation(-pt);
        }

        /// <summary>
        /// 旋转矩阵
        /// </summary>
        /// <param name="angle"></param>
        /// <returns></returns>
        public static Matrix2D Rotation(Angle angle)
        {
            double s = Math.Sin(angle);
            double c = Math.Cos(angle);
            return new Matrix2D(c, s, -s, c, 0, 0);
        }

        /// <summary>
        /// 有基点的旋转矩阵
        /// </summary>
        /// <param name="angle"></param>
        /// <param name="pt"></param>
        /// <returns></returns>
        public static Matrix2D Rotation(Angle angle, Point2D pt)
        {
            return
                Translation(-pt) *
                Rotation(angle) *
                Translation(pt);
        }

        /// <summary>
        /// 移动矩阵
        /// </summary>
        /// <param name="pt"></param>
        /// <returns></returns>
        public static Matrix2D Translation(Point2D pt)
        {
            return Translation(pt.X, pt.Y);
        }

        /// <summary>
        /// 移动矩阵
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <returns></returns>
        public static Matrix2D Translation(double x, double y)
        {
            return new Matrix2D(1, 0, 0, 1, x, y);
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="line"></param>
        /// <returns></returns>
        public static Matrix2D Mirror(LineSegment2D line)
        {
            return Matrix2D.Mirror(line.StartPoint, line.EndPoint);
        }

        /// <summary>
        /// 按直线的镜像矩阵
        /// </summary>
        /// <param name="start"></param>
        /// <param name="end"></param>
        /// <returns></returns>
        public static Matrix2D Mirror(Point2D start, Point2D end)
        {
            return Matrix2D.Mirror(start, end - start);
        }

        /// <summary>
        /// 按直线的镜像矩阵
        /// </summary>
        /// <param name="start"></param>
        /// <param name="vec"></param>
        /// <returns></returns>
        public static Matrix2D Mirror(Point2D start, Vector2D vec)
        {

            bool ex = GeoUtils.Equals(vec.X, 0);
            bool ey = GeoUtils.Equals(vec.Y, 0);
            if (ex && ey)
                return Rotation(new Angle(Math.PI), start);
            else if (ex)
                return new Matrix2D(-1, 0, 0, 1, start.X * 2, 0);
            else if (ey)
                return new Matrix2D(1, 0, 0, -1, 0, start.Y * 2);

            double k = vec.Y / vec.X;
            double b = (start.Y - k * start.X);
            double x0 = b / k;
            double angle = vec.Angle * 2;
            double s2 = Math.Sin(angle);
            double c2 = Math.Cos(angle);
            return
                new Matrix2D(c2, s2, s2, -c2, -b * s2, x0 * s2);

        }

        /// <summary>
        /// 按向量的镜像矩阵
        /// </summary>
        /// <param name="start"></param>
        /// <param name="end"></param>
        /// <returns></returns>
        public static Matrix2D Mirror(Vector2D vec)
        {

            bool ex = GeoUtils.Equals(vec.X, 0);
            bool ey = GeoUtils.Equals(vec.Y, 0);
            if (ex && ey)
                return Rotation(new Angle(Math.PI));
            else if (ex)
                return new Matrix2D(-1, 0, 0, 1, 0, 0);
            else if (ey)
                return new Matrix2D(1, 0, 0, -1, 0, 0);

            double angle = vec.Angle * 2;
            double s2 = Math.Sin(angle);
            double c2 = Math.Cos(angle);
            return new Matrix2D(c2, s2, s2, -c2, 0, 0);

        }

        #endregion

        public override string ToString()
        {
            string s = "(";
            for (int i = 0; i < 3; i++)
            {
                s +=
                    string.Format(
                        "({0},{1},{2})",
                        _elements[i, 0],
                        _elements[i, 1],
                        _elements[i, 2]);
            }
            return s + ")";
        }

    }
}
