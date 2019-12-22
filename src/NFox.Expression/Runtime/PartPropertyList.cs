using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using NFox.Expression;
using System.Runtime.InteropServices;
using NFox.Expression.SymbolValues;

namespace NFox.Expression.Runtime
{
    public partial class PartPropertyList : UserControl
    {


        public event Part.EventHandler ParamChanged;

        public PartPropertyList()
        {
            InitializeComponent();
        }

        private ImagePart _part;
        public ImagePart Part
        {
            set
            {

                if (value is ParameterizedPart)
                {
                    var ppart = _part as ParameterizedPart;
                    paramList1.Part = ppart;
                    paramList1.ParamChanged += new ParamList.ParamChangedEvent(paramList1_ParamChanged);
                }
                else
                {
                    paramList1.Part = null;
                    if(value == null)
                        return;
                }

                txtName.Text = value.Name;
                _part = value;
                odxView1.Image = value.Image;

            }
            get { return _part; }
        }

        void paramList1_ParamChanged(object sender, EventArgs e)
        {
            odxView1.Image = sender as Image2D;
            if(ParamChanged != null)
                ParamChanged(this, new PartEventArgs(_part) { Tag = this.Tag });
        }


        private void mouseMove(object sender, MouseEventArgs e)
        {
            Control ctl = sender as Control;
            var pt = e.Location;
            var off = ctl.Location;
            pt.Offset(off);
            base.OnMouseMove(new MouseEventArgs(e.Button, e.Clicks, pt.X, pt.Y, e.Delta));
        }




    }
}
