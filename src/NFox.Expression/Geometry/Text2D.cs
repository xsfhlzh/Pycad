
using System.Xml.Linq;
using System.Drawing.Drawing2D;
using System.Drawing;
using NFox.Expression.Runtime;
using NFox.Expression.DataSystem;
using System.Collections.Generic;

namespace NFox.Geometry
{
    public class Text2D : Entity2D
    {

        public Text2D() { }

        public Text2D(Point2D position, string content, double height)
        {
            Position = position;
            Content = content;
            Height = height;
        }
        
        #region Member

        public Point2D Position;
        public string Content;
        public double Height;

        #endregion

        #region Entity

        public override Entity2D Copy()
        {
            var ent =
                new Text2D(
                    Position,
                    Content,
                    Height);
            ent.LayerName = LayerName;
            return ent;
        }

        public override IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path)
        {
            var tpath = new GraphicsPath();
            var font =
                new System.Drawing.Font("@宋体", (float)Height, FontStyle.Italic);
            var format = new StringFormat { Alignment = StringAlignment.Center };
            var size = g.MeasureString(Content, font);
            var rec =
                new RectangleF(
                    new PointF(-size.Width / 2, -size.Height / 2),
                    size);
            
            tpath.AddString(
                Content,
                font.FontFamily,
                (int)font.Style,
                (float)Height,
                rec,
                format);

            //文字宽度比例0.7，水平翻转
            Matrix m = new Matrix(1, 0, 0, -1, 0, 0);
            m.Scale(0.7f, 1, MatrixOrder.Append);
            m.Translate((float)Position.X,(float)Position.Y, MatrixOrder.Append);
            tpath.Transform(m);

            path.AddPath(tpath, false);
            path.StartFigure();
            yield return 0;
            yield break;
        }

        public override void FromX(XElement xe)
        {
            Position = Point2D.Parse(xe.Attribute("Position").Value);
            Content = xe.Attribute("Content").Value;
            Height = double.Parse(xe.Attribute("Height").Value);
        }

        public override void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Position", Position.ToString()));
            xe.Add(new XAttribute("Content", Content));
            xe.Add(new XAttribute("Height", Height));
            MakeLayer(xe);
        }

        public override string XName
        {
            get { return "Text"; }
        }

        public override void TransformBy(Matrix2D mat)
        {
            Position *= mat;
            var vec = Vector2D.YAxis * mat;
            Height *= vec.Length;
        }

        #endregion

    }
}
