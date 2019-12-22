using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace NFox.Expression.Runtime
{
    public partial class frmInputBox : Form
    {
        public frmInputBox(string title, string caption, string displayText)
        {
            InitializeComponent();
            label1.Text = string.Format(title, displayText);
            textBox1.Text = displayText;
            textBox1.Focus();
            textBox1.SelectionStart = 0;
            textBox1.SelectionLength = displayText.Length;
            this.Text = caption;
            DialogResult = DialogResult.Cancel;
        }

        public string NewText
        {
            get { return textBox1.Text; }
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                DialogResult = DialogResult.OK;
                this.Close();
            }
        }
   
    }
}
