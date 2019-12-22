using NFox.Expression.SymbolValues;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NFox.Expression.Runtime
{
    public partial class frmMakeParameterizedPart : Form
    {

        PartCode _pe;

        public frmMakeParameterizedPart(ImagePart part)
        {
            InitializeComponent();
            _pe = new PartCode();
            //_pe.ImagePart = part;
            _pe.Dock = DockStyle.Fill;
            this.Controls.Add(_pe);
        }



    }
}
