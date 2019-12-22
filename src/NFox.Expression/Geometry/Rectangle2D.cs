

using System.Drawing;

namespace NFox.Geometry
{

    public struct Rectangle2D
    {

        #region Member

        private Point2D _minPt;
        public Point2D MinPoint 
        {
            get { return _minPt; }
        }

        private Vector2D _size;
        public Vector2D Size
        {
            get { return _size; }
        }

        public Point2D MaxPoint
        {
            get { return _minPt + _size; }
        }

        # endregion

        public Rectangle2D(Point2D minPt, Vector2D size)
        {
            _minPt = minPt;
            _size = size;
        }

        public Rectangle2D(double x, double y, double width, double height)
        {
            _minPt = new Point2D(x, y);
            _size = new Vector2D(width, height);
        }

        public static implicit operator RectangleF(Rectangle2D rec)
        {
            return
                new RectangleF(rec.MinPoint, rec.Size);
        }

    }

}
