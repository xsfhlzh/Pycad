using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NFox.Geometry;
using System.Windows.Forms;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Xml.Linq;
using System.Collections;
using NFox.Expression;
using NFox.Expression.DataSystem;

namespace NFox.Expression.Runtime
{
    public class Image2D : IEnumerable<Entity2D>, IParser
    {

        public Image2D()
        {
            Layers = new Dictionary<string, List<Entity2D>>();
        }

        public Image2D(IEnumerable<Entity2D> ents)
            : this()
        {
            foreach (var ent in ents)
                Add(ent);
        }

        public Image2D(IEnumerable ents)
            : this()
        {
            foreach (var ent in ents)
            {
                var ent2D = Entity2D.FromObject(ent);
                if(ent2D!= null)
                    Add(ent2D);
            }
        }

        public IEnumerable<T> Cast<T>()
        {
            foreach (var ent in this)
                yield return (T)ent.ToObject();
        }

        #region Member

        public Dictionary<string, List<Entity2D>> Layers { private set; get; }
        public Matrix Transform { private set; get; }

        #endregion

        #region Method

        #region IParser

        public void FromX(XElement xe)
        {
            foreach (var ent in xe.Elements())
                Add(Entity2D.Parse(ent));
        }

        public string XName
        {
            get { return "Image"; }
        }

        public void ToX(XElement xe)
        {
            foreach (var layer in Layers)
            {
                foreach (Entity2D ent in layer.Value)
                    xe.Add(ent.ToX());
            }
        }

        #endregion

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

        public void Remove(Entity2D ent)
        {
            foreach (var layer in Layers)
            {
                if (layer.Value.Contains(ent))
                {
                    layer.Value.Remove(ent);
                    break;
                }
            }
        }

        public void Union(Image2D image)
        {
            foreach (var layer in image.Layers)
            {
                var ents = GetLayer(layer.Key);
                ents.AddRange(layer.Value);
            }
        }

        public void CloneFrom(Image2D image)
        {
            Layers = image.Layers;
        }

        public void Draw(Graphics graphics, RectangleF rec)
        {
            //分层获取path
            var paths = new Dictionary<string, GraphicsPath>();
            //状态机集合
            var ies = new List<IEnumerator<int>>();
            //遍历层集合
            foreach (var layer in Layers)
            {
                var path = new GraphicsPath();
                paths.Add(layer.Key, path);
                foreach (var ent in layer.Value)
                {
                    //获取实体绘制函数状态机，先走一步获取path
                    var pen = Application.GetPen(layer.Key);
                    var ie =
                        ent.Draw(graphics, pen, path)
                        .GetEnumerator();
                    ie.MoveNext();
                    ies.Add(ie);
                }
            }

            var lst = paths.Select(kv => kv.Value).ToList();
            if (lst.Count == 0) return;

            //遍历paths获取最小包围矩形
            var recEntitys = lst[0].GetBounds();
            for (int i = 1; i < lst.Count; i++)
            {
                var recCurr = lst[i].GetBounds();
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



            //window坐标系转换为Cad坐标系
            var mat = new Matrix();
            //1.先将图形中心置于原点
            mat.Translate(
                -recEntitys.X - recEntitys.Width / 2,
                -recEntitys.Y - recEntitys.Height / 2,
                  MatrixOrder.Append);
            //2.按X轴镜像
            mat.Multiply(new Matrix(1, 0, 0, -1, 0, 0), MatrixOrder.Append);
            //获取缩放比例
            var sc =
                Math.Min(
                    rec.Height / recEntitys.Height,
                    rec.Width / recEntitys.Width);
            sc *= 0.9f;
            //3.再将图形按比例缩放
            mat.Scale(sc, sc, MatrixOrder.Append);
            //4.按最终位置将图形放置到位
            mat.Translate(rec.Left + rec.Width / 2, rec.Top + rec.Height / 2, MatrixOrder.Append);
            Transform = mat.Clone();
            Transform.Invert();
            graphics.Transform = mat;

            //绘制path
            foreach (var path in paths)
            {
                var pen = Application.GetPen(path.Key);
                pen.Transform = Transform;
                graphics.DrawPath(pen, path.Value);
            }

            //执行状态机的下一步
            foreach (var ie in ies)
                ie.MoveNext();

            //绘制起点标识
            var startPointPath = new GraphicsPath();
            float r = 6 / sc;
            startPointPath.AddRectangle(new RectangleF(new PointF(-r / 2, -r / 2), new SizeF(r, r)));
            var markPen = Application.DefaultLayers["Mark"];
            markPen.Transform = Transform;
            graphics.DrawPath(markPen, startPointPath);

            graphics.ResetTransform();
    
        }

        #endregion

        #region IEnumerable

        public IEnumerator<Entity2D> GetEnumerator()
        {
            foreach (var layer in Layers)
            {
                foreach (Entity2D ent in layer.Value)
                    yield return ent;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        #endregion


    }
}
