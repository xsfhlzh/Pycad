using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using NFox.Expression.DataSystem;
using System.Drawing;
using System.Drawing.Drawing2D;

namespace NFox.Expression.Runtime
{

    public static class Application
    {

        public static Database WorkingDatabase { set; get; }

        public static string DefaultLayerName = "Default";
        public static Pen DefaultLayer = new Pen(new SolidBrush(Color.Cyan));

        //默认线型
        public static Dictionary<string, Pen> DefaultLayers =
            new Dictionary<string, Pen>
            {
                //粗实线
                { "Default", DefaultLayer }, 
                //细实线
                { "Solid", new Pen(new SolidBrush(Color.Green)) },
                //虚线
                { "Dash", new Pen(new SolidBrush(Color.Yellow)){ DashStyle = DashStyle.Dash } },
                //点划线
                { "DashDot", new Pen(new SolidBrush(Color.Red)){ DashStyle = DashStyle.DashDot } }, 
                //双点划线
                { "DashDotDot", new Pen(new SolidBrush(Color.Purple)){ DashStyle = DashStyle.DashDotDot } },
                { "Mark",  new Pen(new SolidBrush(Color.Yellow), 1.5f) }
            };

        public static Pen GetPen(string layer)
        {
            return
                DefaultLayers.ContainsKey(layer) ?
                DefaultLayers[layer] :
                DefaultLayer;
        }

    }

}
