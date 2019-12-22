
using System;
using System.Drawing;
using System.Linq;
using System.Collections.Generic;
using System.Xml.Linq;
using System.Drawing.Drawing2D;

using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;


namespace NFox.Geometry
{
    public class PolyLine2D : Curve2D, IEnumerable<Curve2D>
    {

        public PolyLine2D()
        {
            _closed = false;
            Vertexs = new List<BulgeVertex2D>();
        }

        public PolyLine2D(bool isClosed)
        {
            _closed = isClosed;
            Vertexs = new List<BulgeVertex2D>();
        }

        public PolyLine2D(bool closed, List<BulgeVertex2D> vertexs)
        {
            _closed = closed;
            Vertexs = vertexs;
        }


        public void Add(Point2D vertex, double bulge, double startWidth, double endWidth)
        {
            Vertexs.Add(new BulgeVertex2D(vertex, bulge, startWidth, endWidth));
        }

        public void Add(Point2D vertex, double bulge)
        {
            Vertexs.Add(new BulgeVertex2D(vertex, bulge));
        }

        public void Add(BulgeVertex2D bulgeVertex)
        {
            Vertexs.Add(bulgeVertex);
        }

        public void Add(Point2D vertex)
        {
            Add(vertex, 0);
        }

        public void MakeOpen(bool isOpen)
        {
            _closed = !isOpen;
        }

        #region Member

        public List<BulgeVertex2D> Vertexs
        { private set; get; }

        public int SegmentCount
        {
            get { return Closed ? Vertexs.Count : Vertexs.Count - 1; }
        }

        #endregion

        #region Entity

        public override Entity2D Copy()
        {
            var pline = new PolyLine2D(Closed);
            foreach (var ver in Vertexs)
                pline.Vertexs.Add(ver);
            pline.LayerName = LayerName;
            return pline;
        }

        public override IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path)
        {
            GraphicsPath fill = new GraphicsPath();
            for (int i = 0; i < SegmentCount; i++)
            {
                var curve = GetSegmentAt(i);
                var ver = Vertexs[i];
                if (ver.StartWidth == 0 && ver.EndWidth == 0)
                {
                    curve.DrawTo(g, path);
                }
                else
                {
                    var w1 = ver.StartWidth / 2;
                    var w2 = ver.EndWidth / 2;
                    var cpath = new GraphicsPath();
                    if (curve is LineSegment2D)
                    {
                        var line = curve as LineSegment2D;
                        var vec = line.EndPoint - line.StartPoint;
                        vec = vec.UnitVector.RotateBy(Angle.Degree90);
                        var pts =
                            new PointF[]
                            {
                                line.StartPoint + vec * w1,
                                line.EndPoint + vec * w2,
                                line.EndPoint - vec * w2,
                                line.StartPoint - vec * w1
                            };
                        cpath.AddLines(pts);
                        cpath.CloseFigure();
                    }
                    else
                    {

                        var arc = curve as CircleArc2D;
                        var vec1 = new Vector2D(w1, arc.StartAngle);
                        var pt = arc.GetPointAtParam(arc.EndParam / 2);
                        var vec2 = (pt - arc.Center).UnitVector * (w1 + w2) / 2;
                        var vec3 = new Vector2D(w2, arc.EndAngle);
                        var pts =
                            new Point2D[] 
                            { 
                                arc.StartPoint + vec1,  
                                pt + vec2, 
                                arc.EndPoint + vec3 ,
                                arc.EndPoint - vec3, 
                                pt - vec2, 
                                arc.StartPoint - vec1 
                            };

                        var arc1 = new CircleArc2D(pts[0], pts[1], pts[2]);
                        var line1 = new LineSegment2D(pts[2], pts[3]);
                        var arc2 = new CircleArc2D(pts[3], pts[4], pts[5]);
                        var line2 = new LineSegment2D(pts[5], pts[0]);
                        arc1.DrawTo(g, cpath);
                        line1.DrawTo(g, cpath);
                        arc2.DrawTo(g, cpath);
                        line2.DrawTo(g, cpath);
                    }
                    fill.AddPath(cpath, false);
                    path.AddPath(cpath, false);
                    path.StartFigure();
                }
            }
            yield return 0;
            g.FillPath(pen.Brush, fill);
            yield break;
        }

        public override void FromX(XElement xe)
        {
            _closed = bool.Parse(xe.Attribute("Closed").Value);
            Vertexs = new List<BulgeVertex2D>();
            foreach (var e in xe.Elements("Vertex"))
                Vertexs.Add(XParser.Parse<BulgeVertex2D>(e));
        }

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Closed", Closed));
            foreach (var bv in Vertexs)
                xe.Add(bv.ToX());
        }

        public override string XName
        {
            get { return "PolyLine"; }
        }

        public override void TransformBy(Matrix2D mat)
        {
            for (int i = 0; i < Vertexs.Count; i++)
            {
                var vex = Vertexs[i];
                vex.Position *= mat;
            }
        }

        #endregion

        #region Curve2D

        private bool _closed;
        public override bool Closed
        {
            get { return _closed; }
        }

        public override double Length
        {
            get { return this.Select(c => c.Length).Sum(); }
        }

        public override double StartParam
        {
            get { return 0; }
        }

        public override double EndParam
        {
            get { return Closed ? Vertexs.Count + 1 : Vertexs.Count; }
        }

        public override Point2D GetPointAtParam(double par)
        {
            int index = Convert.ToInt32(Math.Floor(par));
            Curve2D curve = GetSegmentAt(index);
            double cpar = curve.EndParam * (par - index);
            return curve.GetPointAtParam(cpar);
        }

        #endregion

        #region IEnumerable

        public Curve2D GetSegmentAt(int index)
        {

            if (index < 0 || index >= SegmentCount)
                return null;
            var pt1 = Vertexs[index];
            var pt2 =
                index == Vertexs.Count - 1 ?
                Vertexs[0] :
                Vertexs[index + 1];
            if (GeoUtils.Equals(pt1.Bulge, 0))
                return new LineSegment2D(pt1.Position, pt2.Position);
            else
                return new CircleArc2D(pt1.Position, pt2.Position, pt1.Bulge);
        }

        public IEnumerator<Curve2D> GetEnumerator()
        {
            for (int i = 0; i < SegmentCount; i++)
            {
                var pt1 = Vertexs[i];
                var pt2 =
                    i == Vertexs.Count - 1 ?
                    Vertexs[0] :
                    Vertexs[i + 1];
                if (GeoUtils.Equals(pt1.Bulge, 0))
                    yield return new LineSegment2D(pt1.Position, pt2.Position);
                else
                    yield return new CircleArc2D(pt1.Position, pt2.Position, pt1.Bulge);
            }
                
        }

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        #endregion


    }
}
