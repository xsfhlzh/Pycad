using NFox.Expression.DataSystem;
using NFox.Expression.SymbolValues;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Windows.Forms;

namespace NFox.Expression.Runtime
{
    public partial class frmAttributeListView : Form
    {

        ConfigDictionary _dict;
        List<PartAttrib> _atts;
        ImagePart _part;
        Database _database;

        public frmAttributeListView(Database database, ImagePart part)
        {
            InitializeComponent();
            _database = database;
            _part = part;
            partInfo1.SetValues(_database, _part);
            _atts = CopyFrom(part.Attributes, true);
            dataGridView1.DataSource = new BindingList<PartAttrib>(_atts);
            _dict = _database.ConfigDictionary;
            if(part.IsParameterized)
                partCode1.SetValues(database, part);
            else
                tabControl1.Controls.Remove(tabPage3);
            partInfo1.Select();
        }


        #region Attrib

        private List<PartAttrib> CopyFrom(List<PartAttrib> atts, bool hasData)
        {
            var newatts = new List<PartAttrib>();
            foreach (var att in atts)
                newatts.Add(att.Copy(hasData));
            return newatts;
        }

        private void btnSaveDefault_Click(object sender, EventArgs e)
        {
            var atts = 
                CopyFrom(_atts, false)
                .Select(a => a.Name)
                .ToArray();
            _dict["Attdef"].Value = string.Join(",", atts) ;
        }

        private void btnLoadDefault_Click(object sender, EventArgs e)
        {
            _atts = 
                _dict["Attdef"]
                .Value
                .Split(',')
                .Select(s => new PartAttrib(s))
                .ToList();
            dataGridView1.DataSource = new BindingList<PartAttrib>(_atts);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            var name = dataGridView1.Columns[e.ColumnIndex].Name;
            if (e.RowIndex > -1)
            {
                if (name == "Remove")
                {
                    dataGridView1.Rows.RemoveAt(e.RowIndex);
                }
                else if (name == "Insert")
                {
                    _atts.Insert(e.RowIndex, new PartAttrib());
                    dataGridView1.DataSource = new BindingList<PartAttrib>(_atts);
                }
            }
        }

        #endregion


        private void btnOK_Click(object sender, EventArgs e)
        {
            if (partInfo1.Changed && partInfo1.OK)
            {
                _database.Redirect(
                    _part,
                    partInfo1.Index,
                    partInfo1.PartName);
            }
            _part.LongName = partInfo1.LongName;
            _part.Attributes = _atts;
        }


        private void frmAttributeListView_FormClosing(object sender, FormClosingEventArgs e)
        {
            e.Cancel = !partInfo1.OK && _cancel;
        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (tabControl1.SelectedIndex == 0)
                partInfo1.Select();
            else
                dataGridView1.Select();
        }

        bool _cancel = true;
        private void button1_Click(object sender, EventArgs e)
        {
            _cancel = false;
        }













    }



}
