using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using NFox.Expression;
using NFox.Expression.SymbolValues;
using NFox.Expression.Runtime;
using XApp = NFox.Expression.Runtime.Application;
using NFox.Geometry;
using System.Collections;

namespace NFox.Expression.Runtime
{
    public partial class frmMakeGeneralPart : Form
    {

        private Part.EventHandler _partDefining;
        private PartFolder _owner;
        private ImagePart _part;

        public frmMakeGeneralPart(PartFolder owner, Part.EventHandler partDefining)
        {
            InitializeComponent();
            _owner = owner;
            _partDefining = partDefining;
        }

        public bool Define()
        {
            var e = new PartEventArgs(null);
            _partDefining(this, e);
            if (e.Part == null) return false;
            var part = e.Part as ImagePart;
            if (_part == null)
            {
                _part = part;
                partInfo1.SetValues(_owner.Database, _part);
            }
            else
            {
                _part.Image = part.Image;
                partInfo1.UpdateView();
            }
            partInfo1.Select();
            return true;
        }

        #region Ok

        private void btnOK_Click(object sender, EventArgs e)
        {
            if (partInfo1.OK)
            {
                partInfo1.Update(_part);
                _owner.Add(_part);
            }
        }

        #endregion

        private void btnRedefine_Click(object sender, EventArgs e)
        {
            this.Hide();
            Define();
            this.Show();

        }

        private void frmMakeGeneralPart_FormClosing(object sender, FormClosingEventArgs e)
        {
            e.Cancel = !partInfo1.OK && DialogResult != DialogResult.Cancel;
        }







    }



}
