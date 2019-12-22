using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing.Drawing2D;
using System.Drawing;
using NFox.Expression;
using NFox.Expression.Runtime;

namespace NFox.Geometry
{
    public class HatchLoop
    {

        public string LayerName;
        public string TypeName;
        public GraphicsPath Boundary;

        public HatchLoop(GraphicsPath boundary, string layer, string typeName)
        {
            Boundary = boundary;
            LayerName = layer;
            TypeName = typeName;
        }

        public HatchLoop(GraphicsPath loop, string layer)
        {
            Boundary = loop;
            LayerName = layer;
        }

        public HatchLoop Clone()
        {
            return 
                new HatchLoop(
                    Boundary.Clone() as GraphicsPath,
                    LayerName, 
                    TypeName);
        }

        public void Draw(Graphics g)
        {
            var pen =
               Application.DefaultLayers.ContainsKey(LayerName) ?
               Application.DefaultLayers[LayerName] :
               Application.DefaultLayer;
            g.FillPath(pen.Brush, Boundary as GraphicsPath);
        }

        public void Transform(Matrix mat)
        {
            var path = Boundary as GraphicsPath;
            path.Transform(mat);
        }

    }
}
