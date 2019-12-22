using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace NFox.Expression.Runtime
{
    public partial class OdxView : UserControl
    {

        Image2D _image = new Image2D();      
        public Image2D Image
        {
            set
            {
                if (value != null)
                    _image.CloneFrom(value);
                else
                    _image = new Image2D();
                this.Invalidate();
            }
            get
            {
                return _image;
            }
        }

        public OdxView()
        {
            InitializeComponent();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            var graphics = e.Graphics;
            graphics.SmoothingMode = SmoothingMode.AntiAlias;
            _image.Draw(graphics, new Rectangle(0, 0, Width, Height));
        }

        protected override void OnResize(EventArgs e)
        {
            base.OnResize(e);
            this.Invalidate();
        }



    }
}
