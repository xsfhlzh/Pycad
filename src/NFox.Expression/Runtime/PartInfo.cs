using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using NFox.Expression.SymbolValues;
using NFox.Expression.DataSystem;

namespace NFox.Expression.Runtime
{
    public partial class PartInfo : UserControl
    {

        private Database _database;
        private ImagePart _part;

        private bool _bName;
        private bool _bStandard;
        private bool _bChangedByCode;

        public bool AllowDuplicated { set; get; }
        [Browsable(false)]
        public bool Duplicated { private set; get; }

        [Browsable(false)]
        public bool OK
        {
            get { return !string.IsNullOrEmpty(Name) && _bName && _bStandard; }
        }

        [Browsable(false)]
        public bool Changed 
        { private set; get; }

        [Browsable(false)]
        public string PartName
        {
            private set { txtName.Text = value; }
            get { return txtName.Text.Trim(); }
        }

        [Browsable(false)]
        public string LongName
        {
            private set { txtLongName.Text = value; }
            get { return txtLongName.Text.Trim(); }
        }

        private string Standard
        {
            set { cboStandard.Text = value; }
            get { return cboStandard.Text.Trim(); }
        }

        private string No
        {
            set { txtNo.Text = value; }
            get { return txtNo.Text.Trim(); }
        }

        [Browsable(false)]
        public SymbolIndex Index
        {
            get { return new SymbolIndex(PartName, Standard, No); }
        }

        public void UpdateView()
        {
            odxView1.Image = _part.Image;
        }

        public void SetValues(Database database, ImagePart part)
        {
            _bChangedByCode = true;
            if (part != null)
            {
                _database = database;
                _part = part;
                UpdateView();
                PartName = part.Name;
                LongName = part.LongName;
                foreach (var name in _database.ImagePartTable.DictionaryNames)
                    cboStandard.Items.Add(name);
                cboStandard.Items.Add("新的标准......");
                Standard = _standard = part.Index.DictionaryName;
                No = part.Index.Key;
            }
            _bChangedByCode = false;
            Check(null, null);
        }

        public PartInfo()
        {
            InitializeComponent();
            _bChangedByCode = false;
        }

        public void Update(ImagePart part)
        {
            part.Name = PartName;
            part.Index = Index;
            part.LongName = LongName;
        }

        private string _standard;
        private void cboStandard_SelectedIndexChanged(object sender, EventArgs e)
        {

            var lastIndex = cboStandard.Items.Count - 1;
            if (cboStandard.SelectedIndex == lastIndex)
            {
                frmInputBox inputBox = new frmInputBox("请输入标准名称:", "添加标准", "新的标准");
                var res = inputBox.ShowDialog();
                if (res == DialogResult.OK)
                {

                    var newName = inputBox.NewText.Trim();
                    if (string.IsNullOrEmpty(newName))
                        return;

                    if (cboStandard.Items.Contains(newName))
                    {
                        MessageBox.Show(
                            string.Format("无法添加标准\"{0}\":与现有标准重名", newName),
                            "添加标准时出错");
                        Standard = _standard;
                        return;
                    }
                    else
                    {
                        _database.ImagePartTable.AddDictionary(newName);
                        cboStandard.Items.Insert(lastIndex, newName);
                        cboStandard.SelectedIndex = lastIndex;
                    }
                }
                else
                {
                    cboStandard.Text = _standard;
                }
            }

            _standard = Standard;
            if (txtNo.Enabled = lblNo.Enabled = Standard != "Main")
                txtNo.Select();
            Check(null, null);

        }


        private void textBox_Click(object sender, EventArgs e)
        {
            TextBox txt = sender as TextBox;
            txt.Click -= textBox_Click;
            if (txt.SelectionLength == 0)
                txt.SelectAll();
        }

        private void textBox_Enter(object sender, EventArgs e)
        {
            TextBox txt = sender as TextBox;
            txt.Click += textBox_Click;
            if (txt.SelectionLength == 0)
                txt.SelectAll();
        }

        private void textBox_Leave(object sender, EventArgs e)
        {
            TextBox txt = sender as TextBox;
            txt.Click -= textBox_Click;
        }



        private void Check(object sender, EventArgs e)
        {

            if (_bChangedByCode || _part == null)
                return;

            lblCheckName.Text = lblCheckStandard.Text = "*";
            if (_part.Index.Equals(Index) && _part.Name == PartName)
            {
                Changed = false;
                _bName = _bStandard = true;
                return;
            }

            Changed = true;
            Duplicated = false;

            if (PartName == "")
            {
                lblError.Text = "* 名字不能为空！";
                _bName = false;
            }
            else if (Standard == "Main")
            {
                _bStandard = true;
                if (_part.Name != PartName && _database.ImagePartTable.Has(Index))
                {
                    lblError.Text = "* 名字有重复！";
                    _bName = AllowDuplicated;
                    Duplicated = true;
                }
                else
                {
                    lblCheckName.Text = "OK!";
                    lblError.Text = "";
                    _bName = true;
                }
            }
            else
            {
                _bName = true;
                if (No == "")
                {
                    lblError.Text = "* 序号不能为空！";
                    _bStandard = false;
                }
                else
                {
                    if (!_part.Index.Equals(Index) && _database.ImagePartTable.Has(Index))
                    {
                        lblError.Text = "* 序号有重复！";
                        _bStandard = AllowDuplicated;
                        Duplicated = true;
                    }
                    else
                    {
                        lblCheckStandard.Text = "OK!";
                        lblError.Text = "";
                        _bStandard = true;
                    }
                }
            }
        }



    }

}
