using NFox.Expression.Runtime;
using System.Collections.Generic;

namespace NFox.Geometry
{
    public class Image
    {

        List<Entity2D> _ents;

        internal void SetData(List<Entity2D> ents)
        {
            _ents = ents;
        }

        public Entity2D add(Entity2D ent, string layer = null)
        {
            if (layer == null)
                ent.LayerName = _layer;
            else
                ent.LayerName = layer;
            _ents.Add(ent);
            return ent;
        }

        public void add(IEnumerable<Entity2D> ents)
        {
            _ents.AddRange(ents);
        }

        private string _layer = Application.DefaultLayerName;
        public string clayer
        {
            set { _layer = value; }
            get { return _layer; }
        }

        public Entity2D addline(Point2D start, Point2D end, string layer = null)
        {
            return add(new LineSegment2D(start, end), layer);
        }

        public Entity2D addline(Point2D start, Angle angle, double length, string layer = null)
        {
            return add(new LineSegment2D(start, angle, length), layer);
        }

        public Entity2D addline(Point2D start, Angle angle, double minlength, double maxlength, string layer = null)
        {
            return add(new LineSegment2D(start, angle, minlength, maxlength), layer);
        }

        public Entity2D addcircle(Point2D center, double radius, string layer = null)
        {
            return add(new CircleArc2D(center, radius), layer);
        }

        public Entity2D addcircle(Point2D pt1, Point2D pt2, Point2D pt3, string layer = null)
        {
            return add(new CircleArc2D(pt1, pt2, pt3), layer);
        }

        public Entity2D addarc(Point2D center, double radius, Angle startAngle, Angle endAngle, string layer = null)
        {
            return add(new CircleArc2D(center, radius, startAngle, endAngle), layer);
        }

        public Entity2D addarc(Point2D start, Point2D end, double bulge, string layer = null)
        {
            return add(new CircleArc2D(start, end, bulge), layer);
        }

        public Entity2D addarc(Point2D pt1, Point2D pt2, Point2D pt3, string layer = null)
        {
            return add(new CircleArc2D(pt1, pt2, pt3, false), layer);
        }

        public Entity2D addellipse(Point2D center, double major, double minor, Angle rotation, Angle startAngle, Angle endAngle, string layer = null)
        {
            return add(new Ellipse2D(center, major, minor, rotation, startAngle, endAngle), layer);
        }

        public Entity2D addellipse(Point2D center, double major, double minor, Angle rotation, string layer = null)
        {
            return add(new Ellipse2D(center, major, minor, rotation), layer);
        }

        public Entity2D addpolyline(string layer = null)
        {
            return add(new PolyLine2D(), layer);
        }

        public Entity2D addpolyline(bool closed, BulgeVertex2D[] vertexs, string layer = null)
        {
            return add(new PolyLine2D(closed, new List<BulgeVertex2D>(vertexs)), layer);
        }

        public void addvexto(PolyLine2D pl, Point2D vertex, double bulge, double startWidth, double endWidth)
        {
            pl.Add(vertex, bulge, startWidth, endWidth);
        }

        public void addvexto(PolyLine2D pl, Point2D vertex, double bulge)
        {
            pl.Add(vertex, bulge);
        }

        public void addvexto(PolyLine2D pl, Point2D vertex)
        {
            pl.Add(vertex, 0);
        }


        public Entity2D addspline(bool closed, IEnumerable<Point2D> fitPoints, string layer = null)
        {
            return add(new Spline2D(closed, fitPoints), layer);
        }

        public Entity2D addspline(bool closed, bool periodic, List<Point2D> controlPoints, double[] knots, string layer = null)
        {
            return add(new Spline2D(closed, periodic, controlPoints, new List<double>(knots)), layer);
        }

        public void setfitdata(Spline2D spl, IEnumerable<Point2D> fitPoints)
        {
            spl.SetFitData(fitPoints);
        }

        public void setfitdata(Spline2D spl, IEnumerable<Point2D> fitPoints, Vector2D startTangent, Vector2D endTangent)
        {
            spl.SetFitData(fitPoints, startTangent, endTangent);
        }

        public Entity2D addtext(Point2D position, string content, double height, string layer = null)
        {
            return add(new Text2D(position, content, height), layer);
        }

    }
}
