
using System;
using System.Collections.Generic;
using System.Linq;
using System.Drawing;
using System.Xml.Linq;
using System.Drawing.Drawing2D;

using NFox.Expression.DataSystem;
using NFox.Expression.Runtime;


namespace NFox.Geometry
{
    public class Spline2D : Curve2D
    {

        public Spline2D() { }

        /// <summary>
        /// 插值点反求控制点
        /// </summary>
        /// <param name="closed"></param>
        /// <param name="fitPoints"></param>
        public Spline2D(bool closed, IEnumerable<Point2D> fitPoints)
        {

            Periodic = false;
            HasFitPoints = true;
            FitPoints = new List<Point2D>(fitPoints);
            
            //参数区间数
            int n = FitPoints.Count - 1;

            //参数化
            List<double> knots = new List<double>();
            knots.Add(0);
            double totalLength = 0;
            for (int i = 0; i < n; i++)
            {
                totalLength += (FitPoints[i + 1] - FitPoints[i]).Length;
                knots.Add(totalLength);
            }
            if (closed)
            {
                totalLength += (FitPoints[0] - FitPoints[FitPoints.Count - 1]).Length;
                knots.Add(totalLength);
            }

            NurbsData = new NurbsData(knots, 3, closed);

            if (closed)
            {
                //构建矩阵方程组
                double[,] mat = new double[n + 1, n + 1];
                for (int i = 0; i < n + 1; i++)
                {
                    var par = NurbsData.Knots[i + Degree];
                    int span = NurbsData.Knots.FindSpan(par);
                    var nn = NurbsData.Knots.BasicFuns(span, par);
                    for (int j = 0; j < Degree; j++)
                        mat[i, (span - Degree + j) % (n + 1)] = nn[j];
                }
                var fpts = new List<Point2D>(FitPoints);
                //求解
                GeoUtils.Inverse(ref mat, n + 1);
                for (int i = 0; i < n + 1; i++)
                {
                    NurbsData.AddControlPoint(new Point2D());
                    for (int j = 0; j < n + 1; j++)
                        NurbsData.ControlPoints[i] += fpts[j] * mat[i, j];
                }
            }
            else
            {
                //构建矩阵方程组
                double[,] mat = new double[n + 3, n + 3];
                //计算插值点的非零幂基函数值
                for (int i = 1; i < n; i++)
                {
                    var par = NurbsData.Knots[i + Degree];
                    int span = NurbsData.Knots.FindSpan(par);
                    var nn = NurbsData.Knots.BasicFuns(span, par);
                    for (int j = 0; j < Degree; j++)
                        mat[i + 1, span - Degree + j] = nn[j];
                }

                mat[1, 0] = mat[n + 1, n + 2] = 1;

                //使用自由边界条件，即端点处二阶导数为0
                var t1 = totalLength / NurbsData.Knots[Degree + 1];
                var t2 = totalLength / NurbsData.Knots[Degree + 2];
                mat[0, 0] = t1;
                mat[0, 1] = -t1 - t2;
                mat[0, 2] = t2;
                t1 = totalLength / (totalLength - NurbsData.Knots[n + Degree - 2]);
                t2 = totalLength / (totalLength - NurbsData.Knots[n + Degree - 1]);
                mat[n + 2, n] = t1;
                mat[n + 2, n + 1] = -t1 - t2;
                mat[n + 2, n + 2] = t2;

                var fpts = new List<Point2D>();
                fpts.Add(Point2D.Origin);
                fpts.AddRange(FitPoints);
                fpts.Add(Point2D.Origin);

                //求解
                GeoUtils.Inverse(ref mat, n + 3);
                for (int i = 0; i < n + 3; i++)
                {
                    NurbsData.AddControlPoint(new Point2D());
                    for (int j = 0; j < n + 3; j++)
                        NurbsData.ControlPoints[i] += fpts[j] * mat[i, j];
                }
            }

        }

        public Spline2D(bool closed, bool periodic, List<Point2D> controlPoints, List<double> knots)
        {

            Periodic = periodic;
            int n = controlPoints.Count() - 1;

            FitPoints = new List<Point2D>();
            HasFitPoints = false;

            NurbsData = new NurbsData(controlPoints, knots, 3, closed);

        }

        public void SetFitData(IEnumerable<Point2D> fitPoints)
        {
            HasFitPoints = true;
            FitPoints = new List<Point2D>(fitPoints);
        }

        public void SetFitData(IEnumerable<Point2D> fitPoints, Vector2D startTangent, Vector2D endTangent)
        {
            HasFitPoints = true;
            FitPoints = new List<Point2D>(fitPoints);
            TangentsExist = !(startTangent.IsZreo || endTangent.IsZreo);
            if (TangentsExist)
            {
                StartTangent = startTangent;
                EndTangent = endTangent;
            }
        }

        #region Member

        /// <summary>
        /// 次数
        /// </summary>
        public int Degree
        {
            get
            {
                return NurbsData.Degree;
            }
        }

        /// <summary>
        /// 阶数
        /// </summary>
        public int Order
        {
            get
            {
                return NurbsData.Degree + 1;
            }
        }

        public bool Periodic
        { private set; get; }

        public bool TangentsExist
        { private set; get; }

        public Vector2D StartTangent
        { private set; get; }

        public Vector2D EndTangent
        { private set; get; }

        public NurbsData NurbsData
        { private set; get; }

        /// <summary>
        /// 拟合点集合
        /// </summary>
        public List<Point2D> FitPoints
        { private set; get; }

        public bool HasFitPoints
        { private set; get; }

        #endregion

        #region Entity

        public override Entity2D Copy()
        {
            var spline =
                new Spline2D(
                    Closed,
                    Periodic,
                    NurbsData.ControlPoints,
                    NurbsData.Knots.ToList());
            if (spline.HasFitPoints = HasFitPoints)
            {
                if (TangentsExist)
                    spline.SetFitData(FitPoints, StartTangent, EndTangent);
                else
                    spline.SetFitData(FitPoints);
            }
            spline.LayerName = LayerName;
            return spline;
        }

        public override void FromX(XElement xe)
        {
            Periodic = bool.Parse(xe.Attribute("Periodic").Value);
            NurbsData = new NurbsData();
            NurbsData.FromX(xe.Element("NurbsData"));

            HasFitPoints = bool.Parse(xe.Attribute("HasFitPoints").Value);
            if (HasFitPoints)
            {
                var fpts = xe.Element("FitPoints");
                FitPoints = new List<Point2D>();
                foreach (var pt in fpts.Elements())
                    FitPoints.Add(XParser.Parse<Point2D>(pt));
                TangentsExist = bool.Parse(fpts.Attribute("TangentsExist").Value);
                if (TangentsExist)
                {
                    StartTangent = Vector2D.Parse(fpts.Attribute("Start").Value);
                    EndTangent = Vector2D.Parse(fpts.Attribute("End").Value);
                }
            }
        }

        public override void ToX(XElement xe)
        {

            xe.Add(new XAttribute("Periodic", Periodic));
            xe.Add(new XAttribute("HasFitPoints", HasFitPoints));
            xe.Add(NurbsData.ToX());
            if (HasFitPoints)
            {
                var e = new XElement("FitPoints",
                    new XAttribute("TangentsExist", TangentsExist));
                xe.Add(e);
                if (TangentsExist)
                {
                    e.Add(new XAttribute("Start", StartTangent.ToString()));
                    e.Add(new XAttribute("End", EndTangent.ToString()));
                }
                foreach (var pt in FitPoints)
                    e.Add(pt.ToX("Point"));
            }
            MakeLayer(xe);
        }

        public override string XName
        {
            get { return "Spline"; }
        }


        public override IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path)
        {
            int count = (NurbsData.ControlPoints.Count - 1) * 10;
            List<PointF> pts = new List<PointF>();
            double t = (EndParam - StartParam) / count;//变化量
            double par = StartParam; 
            for (int i = 0; i < count + 1; i++)
            {
                pts.Add(GetPointAtParam(par));
                par += t;
            }
            path.AddCurve(pts.ToArray());
            path.StartFigure();
            yield return 0;
            yield break;
        }

        public override void TransformBy(Matrix2D mat)
        {
            for (int i = 0; i < NurbsData.ControlPoints.Count; i++)
                NurbsData.ControlPoints[i] *= mat;
            if (HasFitPoints)
            {
                for (int i = 0; i < FitPoints.Count; i++)
                    FitPoints[i] *= mat;
                if (TangentsExist)
                {
                    StartTangent *= mat;
                    EndTangent *= mat;
                }
            }
        }

        #endregion

        #region Curve2D

        /// <summary>
        /// 起点参数
        /// </summary>
        public override double StartParam
        {
            get { return NurbsData.Knots.StartParam; }
        }

        /// <summary>
        /// 终点参数
        /// </summary>
        public override double EndParam
        {
            get { return NurbsData.Knots.EndParam; }
        }

        public override bool Closed
        {
            get { return NurbsData.Closed; }
        }

        public override double Length
        {
            get { throw new NotImplementedException(); }
        }

        /// <summary>
        /// 获取参数对应点
        /// </summary>
        /// <param name="par">参数</param>
        /// <returns>参数对应点</returns>
        public override Point2D GetPointAtParam(double par)
        {
            return NurbsData.GetPointAtParam(par);
        }

        #endregion



    }
}
