
using System.Collections.Generic;
using System.Xml.Linq;

using NFox.Expression.DataSystem;

namespace NFox.Geometry
{

    public class KnotCollection : IEnumerable<double>, IParser
    {

        NurbsData _owner;

        private List<double> _knots;

        public bool Closed
        {
            get { return _owner.Closed; }
        }

        public int Degree
        {
            get { return _owner.Degree; }
        }

        /// <summary>
        /// 起点参数
        /// </summary>
        public double StartParam
        {
            get { return _knots[0]; }
        }

        /// <summary>
        /// 终点参数
        /// </summary>
        public double EndParam
        {
            get { return _knots[_knots.Count - 1]; }
        }

        internal KnotCollection(NurbsData owner)
        {
            _owner = owner;
            _knots = new List<double>();
        }

        public void Add(double knot)
        {
            _knots.Add(knot);
        }

        public void AddRange(IEnumerable<double> knots)
        {
            _knots.AddRange(knots);
        }

        public void InsertAt(int realIndex, double knot)
        {
            _knots.Insert(realIndex, knot);
        }

        public void RemoveAt(int realIndex)
        {
            _knots.RemoveAt(realIndex);
        }

        public double this[int index]
        {
            get
            {
                int realIndex = index - Degree;
                int last = _knots.Count - 1;
                if (realIndex < 0)
                {
                    if (Closed)
                        return _knots[last + realIndex] - _knots[last];
                    return _knots[0];
                }
                else if (realIndex > last)
                {
                    if (Closed)
                        return _knots[realIndex - last] + _knots[last];
                    return _knots[last];
                }
                return _knots[realIndex];
            }
        }

        /// <summary>
        /// 二分法查找参数对应区间
        /// </summary>
        /// <param name="par">参数</param>
        /// <returns>参数对应区间</returns>
        public int FindSpan(double par)
        {
            var n = _knots.Count - 1;
            if (GeoUtils.Equals(par, _knots[_knots.Count - 1]))
                return n + Degree - 1;
            int low = 0, high = n;
            int mid = (low + high) / 2;
            while (par < _knots[mid] || par >= _knots[mid + 1])
            {
                if (par < _knots[mid])
                    high = mid;
                else
                    low = mid;
                mid = (low + high) / 2;
            }
            return mid + Degree;
        }

        /// <summary>
        /// 幂基函数
        /// </summary>
        /// <param name="span">参数对应区间</param>
        /// <param name="par">参数</param>
        /// <returns>非零幂基函数值，从span-p开始</returns>
        public double[] BasicFuns(int span, double par)
        {
            int order = Degree + 1;
            double[] nn = new double[order];
            double[] left = new double[order];
            double[] right = new double[order];
            nn[0] = 1;
            for (int j = 1; j < order; j++)
            {
                left[j] = par - this[span + 1 - j];
                right[j] = this[span + j] - par;
                double saved = 0;
                for (int k = 0; k < j; k++)
                {
                    double temp = nn[k] / (right[k + 1] + left[j - k]);
                    nn[k] = saved + right[k + 1] * temp;
                    saved = left[j - k] * temp;
                }
                nn[j] = saved;
            }
            return nn;
        }

        public IEnumerator<double> GetEnumerator()
        {
            for(int i = 0; i< _knots.Count + Degree * 2; i++)
                yield return this[i];
        }

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        public void FromX(XElement xe)
        {
            _knots.Clear();
            foreach (var knot in xe.Elements())
            {
                _knots.Add(
                    double.Parse(
                    knot.Attribute("Value").Value));
            }
        }

        public void ToX(XElement xe)
        {
            foreach (var knot in _knots)
            {
                xe.Add(
                    new XElement("Knot",
                        new XAttribute("Value", knot)));
            }
        }

        public string XName
        {
            get { return "Knots"; }
        }

    }

}
