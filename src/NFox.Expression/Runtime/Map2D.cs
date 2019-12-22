using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Xml.Linq;
using TlsCad.Geometry;
using TlsCad.Expression;

namespace TlsCad.Expression.Runtime
{

    class Map2D
    {

        public Map2D(Graphics g)
        {
            Layers = new Dictionary<string, List<Entity2D>>();
            _graphics = g;
        }

        public Graphics _graphics;

        public Dictionary<string, List<Entity2D>> Layers { private set; get; }
        public Matrix Transform { private set; get; }


        private List<Entity2D> GetLayer(string layerName)
        {
            if (Layers.ContainsKey(layerName))
            {
                return Layers[layerName];
            }
            else
            {
                var layer = new List<Entity2D>();
                Layers.Add(layerName, layer);
                return layer;
            }
        }

        public void Add(Entity2D entity)
        {
            var layer = GetLayer(entity.LayerName);
            layer.Add(entity);
        }

        //private string GetLayerName(XElement entity)
        //{
        //    var xlayer = entity.Element("Layer");
        //    return
        //        xlayer == null ?
        //        Application.DefaultLayerName :
        //        xlayer.Value;
        //}


        //public Map2D Clone()
        //{
        //    Map2D clone = new Map2D(_graphics);
        //    foreach (var layer in Layers)
        //        clone.Layers.Add(layer.Key, (GraphicsPath)layer.Value.Clone());
        //    foreach (var loop in HatchLoops)
        //        clone.HatchLoops.Add(loop.Clone());
        //    return clone;
        //}

        public void Union(Map2D entitys)
        {
            foreach (var layer in entitys.Layers)
            {
                var ents = GetLayer(layer.Key);
                ents.AddRange(layer.Value);
            }
        }

        public void Draw(RectangleF rec)
        {

            var paths = new Dictionary<string, GraphicsPath>();
            foreach (var layer in Layers)
            {
                var path = new GraphicsPath();
                foreach (var ent in layer.Value)
                {
                    ent.GeneratePath();
                    path.AddPath(ent.GraphicsPath, false);
                    path.StartFigure();
                }
                paths.Add(layer.Key, path);
            }

            var lst = paths.ToList();
            var recEntitys = lst[0].Value.GetBounds();
            for (int i = 1; i < lst.Count; i++ )
            {
                var recCurr = lst[i].Value.GetBounds();
                var pt =
                    new PointF(
                        Math.Min(recEntitys.Left, recCurr.Left),
                        Math.Min(recEntitys.Top, recCurr.Top));
                var size =
                    new SizeF(
                        Math.Max(recEntitys.Right, recCurr.Right) - pt.X,
                        Math.Max(recEntitys.Bottom, recCurr.Bottom) - pt.Y);
                recEntitys = new RectangleF(pt, size);
            }

            var sc =
                Math.Min(
                    rec.Height / recEntitys.Height,
                    rec.Width / recEntitys.Width);
            sc *= 0.9f;

            //window坐标系转换为Cad坐标系
            var mat = new Matrix();
            mat.Translate(
                -recEntitys.X - recEntitys.Width / 2,
                -recEntitys.Y - recEntitys.Height / 2,
                  MatrixOrder.Append);
            mat.Multiply(new Matrix(1, 0, 0, -1, 0, 0), MatrixOrder.Append);
            mat.Scale(sc, sc, MatrixOrder.Append);
            mat.Translate(rec.Left + rec.Width / 2, rec.Top + rec.Height / 2, MatrixOrder.Append);
            Transform = mat.Clone();
            Transform.Invert();
            _graphics.Transform = mat;

            foreach (var path in paths)
            {
                var pen =
                    Application.DefaultLayers.ContainsKey(path.Key) ?
                    Application.DefaultLayers[path.Key] :
                    Application.DefaultLayer;
                pen.Transform = Transform;
                _graphics.DrawPath(pen, path.Value);
                foreach (var ent in GetLayer(path.Key))
                    ent.Draw(_graphics, pen);
            }

            var startPointPath = new GraphicsPath();
            float r = 6 / sc;
            startPointPath.AddRectangle(new RectangleF(new PointF(-r / 2, -r / 2), new SizeF(r, r)));
            var mpen = Application.DefaultLayers["Mark"];
            mpen.Transform = Transform;
            _graphics.DrawPath(mpen, startPointPath);

            _graphics.ResetTransform();

        }

    }
}
