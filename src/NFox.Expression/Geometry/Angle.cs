
using System;
using System.Collections.Generic;

namespace NFox.Geometry
{
    public struct Angle : IEqualityComparer<Angle>, IComparable<Angle>
    {

        public Angle(double radian)
        {
            if (GeoUtils.Equals(radian, 0))
            {
                _radian = 0;
            }
            else if (GeoUtils.Equals(radian, PI2))
            {
                _radian = PI2;
            }
            else
            {

                while (radian < 0)
                    radian += PI2;

                while (radian > PI2)
                    radian -= PI2;

                _radian = radian;

            }
        }

        public Angle(double radian, bool format)
        {

            if (format)
            {
                if (GeoUtils.Equals(radian, PI2))
                {
                    _radian = PI2;
                }
                else
                {

                    while (radian < 0)
                        radian += PI2;

                    while (radian > PI2)
                        radian -= PI2;

                    _radian = radian;

                }
            }
            else
            {
                _radian = radian;
            }
        }

        public static Angle FormDegree(double value)
        {
            return new Angle(value / 180 * Math.PI);
        }

        public static Angle FormDegree(double value, bool format)
        {
            return new Angle(value / 180 * Math.PI, format);
        }

        #region Member

        private const double PI2 = Math.PI * 2;

        double _radian;
        public double Radian
        {
            set 
            {
                if (GeoUtils.Equals(value, PI2))
                {
                    _radian = PI2;
                }
                else
                {

                    while (value < 0)
                        value += PI2;

                    while (value > PI2)
                        value -= PI2;

                    _radian = value;

                }
            }
            get 
            {
                return _radian; 
            }
        }

        public float RadianF
        {
            get { return (float)_radian; }
        }

        public double Degree
        {
            set { Radian = value / 180 * Math.PI; }
            get { return Radian / Math.PI * 180; }
        }

        public float DegreeF
        {
            get { return (float)Degree; }
        }

        public Angle Supplementary
        {
            get { return new Angle(Math.PI - _radian); }
        }

        public Angle Coangle
        {
            get { return new Angle(Math.PI / 2 - _radian); }
        }

        public static Angle Zero
        {
            get { return new Angle(0); }
        }

        public static Angle Degree30
        {
            get { return new Angle(Math.PI / 6); }
        }

        public static Angle Degree45
        {
            get { return new Angle(Math.PI / 4); }
        }

        public static Angle Degree60
        {
            get { return new Angle(Math.PI / 3); }
        }

        public static Angle Degree90
        {
            get { return new Angle(Math.PI / 2); }
        }

        public static Angle Degree120
        {
            get { return new Angle(Math.PI / 3 * 2); }
        }

        public static Angle Degree135
        {
            get { return new Angle(Math.PI / 4 * 3); }
        }

        public static Angle Degree180
        {
            get { return new Angle(Math.PI); }
        }

        public static Angle Degree270
        {
            get { return new Angle(Math.PI / 2 * 3); }
        }

        public static Angle Degree360
        {
            get { return new Angle(PI2); }
        }

        #endregion

        #region operator

        public static implicit operator double(Angle angle)
        {
            return angle._radian;
        }

        public static implicit operator float(Angle angle)
        {
            return (float)angle.Degree;
        }

        public static Angle operator -(Angle angle)
        {
            return new Angle(-angle._radian , false);
        }

        public static Angle operator +(Angle angle1, Angle angle2)
        {
            double angle = angle1._radian + angle2._radian;
            return new Angle(angle);
        }

        public static Angle operator -(Angle angle1, Angle angle2)
        {
            double angle = angle1._radian - angle2._radian;
            return new Angle(angle);
        }

        public static Angle operator *(Angle angle1, double value)
        {
            double angle = angle1._radian * value;
            return new Angle(angle);
        }

        public static Angle operator /(Angle angle1, double value)
        {
            double angle = angle1._radian / value;
            return new Angle(angle);
        }

        public bool IsZero()
        {
            return GeoUtils.Equals(_radian, 0);
        }

        public bool IsWholeCircle()
        {
            return GeoUtils.Equals(_radian, PI2);
        }

        #endregion

        #region Comparer

        public int CompareTo(Angle other)
        {
            return _radian.CompareTo(other._radian);
        }


        public bool Equals(Angle x, Angle y)
        {
            return GeoUtils.Equals(x._radian, y._radian);
        }

        public int GetHashCode(Angle obj)
        {
            return obj._radian.GetHashCode();
        }

        #endregion

        public override string ToString()
        {
            return
                string.Format(
                    "Radian({0}) Degree({1})",
                    Radian,
                    Degree);
        }

    }
}
