
using System.Xml.Linq;
using System.Drawing.Drawing2D;

using NFox.Expression.DataSystem;
using NFox.Expression.Runtime;
using System.Drawing;
using System.Collections.Generic;

namespace NFox.Geometry
{

    public abstract class Entity2D : IParser
    {

        public static IEntityProvider EntityProvider;

        public string LayerName = Application.DefaultLayerName;

        public abstract IEnumerable<int> Draw(Graphics g, Pen pen, GraphicsPath path);

        public void DrawTo(Graphics g, GraphicsPath path)
        {
            var ie = Draw(g, null, path).GetEnumerator();
            ie.MoveNext();
        }

        public abstract void TransformBy(Matrix2D mat);
        public abstract Entity2D Copy();

        public object ToObject()
        {
            if (EntityProvider == null)
                return null;
            return EntityProvider.ToObject(this);
        }

        public static Entity2D FromObject(object obj)
        {
            if (EntityProvider == null) 
                return null;
            return EntityProvider.FromObjet(obj);
        }

        public static Entity2D Parse(XElement xe)
        {

            switch (xe.Name.LocalName)
            {
                case "Line":
                    return XParser.Parse<LineSegment2D>(xe);
                case "CircleArc":
                    return XParser.Parse<CircleArc2D>(xe);
                case "Ellipse":
                    return XParser.Parse<Ellipse2D>(xe);
                case "Text":
                    return XParser.Parse<Text2D>(xe);
                case "PolyLine":
                    return XParser.Parse<PolyLine2D>(xe);
                case "Spline":
                    return XParser.Parse<Spline2D>(xe);
                default:
                    return null;
            }

        }

        protected void MakeLayer(XElement entity)
        {
            if (LayerName != Application.DefaultLayerName)
                entity.Add(new XElement("Layer", LayerName));
        }

        public override string ToString()
        {
            return this.ToX().ToString();
        }

        public abstract string XName { get; }
        public abstract void FromX(XElement xe);
        public abstract void ToX(XElement xe);


    }

}
