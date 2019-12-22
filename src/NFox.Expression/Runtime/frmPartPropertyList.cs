using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using NFox.Expression.SymbolValues;

namespace NFox.Expression.Runtime
{
    public partial class frmPartPropertyList : Form
    {
        public frmPartPropertyList(ImagePart part)
        {
            InitializeComponent();
            partPropertyList1.Part = part;
        }

        private void frmPartPropertyList_Leave(object sender, EventArgs e)
        {
            this.Close();
        }

        private void partPropertyList1_Leaving(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
