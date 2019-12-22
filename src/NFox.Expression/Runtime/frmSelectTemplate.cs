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
    public partial class frmSelectTemplate : Form
    {

        List<List<PartAttrib>> _templates;
        public List<PartAttrib> Attribs { private set; get; }

        public frmSelectTemplate(List<List<PartAttrib>> templates)
        {

            InitializeComponent();
            _templates = templates;

            listView1.Items.Add("默认",0 );
            for (int i = 1; i< _templates.Count; i++)
                listView1.Items.Add("Template" + i, 1);
            listView1.SelectedIndices.Add(0);
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedIndices.Count == 1)
            {
                Attribs = _templates[listView1.SelectedIndices[0]];
                textBox1.Text = "\r\n名称\r\n________________________\r\n\r\n";
                foreach (var att in Attribs)
                    textBox1.Text += att.Name + "\r\n\r\n";
            }
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                DialogResult = DialogResult.Cancel;
                this.Close();
            }
            else if (e.KeyCode == Keys.Delete)
            {
                int i = listView1.SelectedIndices[0];
                listView1.Items.RemoveAt(i);
                for (; i < listView1.Items.Count; i++)
                    listView1.Items[i].Text = "Template" + i;
            }
        }

        private void listView1_DoubleClick(object sender, EventArgs e)
        {
            DialogResult = DialogResult.OK;
            this.Close();
        }



    }
}
