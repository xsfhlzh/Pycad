namespace NFox.Expression.Runtime
{
    partial class PartInfo
    {
        /// <summary> 
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region 组件设计器生成的代码

        /// <summary> 
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            NFox.Expression.Runtime.Image2D image2D1 = new NFox.Expression.Runtime.Image2D();
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.txtLongName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblCheckStandard = new System.Windows.Forms.Label();
            this.txtField = new System.Windows.Forms.TextBox();
            this.txtNo = new System.Windows.Forms.TextBox();
            this.lblField = new System.Windows.Forms.Label();
            this.lblNo = new System.Windows.Forms.Label();
            this.lblStandard = new System.Windows.Forms.Label();
            this.lblName = new System.Windows.Forms.Label();
            this.txtName = new System.Windows.Forms.TextBox();
            this.lblCheckName = new System.Windows.Forms.Label();
            this.cboStandard = new System.Windows.Forms.ComboBox();
            this.odxView1 = new NFox.Expression.Runtime.OdxView();
            this.lblError = new System.Windows.Forms.Label();
            this.tableLayoutPanel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.ColumnCount = 5;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 60F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 60F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 32F));
            this.tableLayoutPanel1.Controls.Add(this.txtLongName, 1, 1);
            this.tableLayoutPanel1.Controls.Add(this.label1, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.lblCheckStandard, 4, 2);
            this.tableLayoutPanel1.Controls.Add(this.txtField, 1, 3);
            this.tableLayoutPanel1.Controls.Add(this.txtNo, 3, 2);
            this.tableLayoutPanel1.Controls.Add(this.lblField, 0, 3);
            this.tableLayoutPanel1.Controls.Add(this.lblNo, 2, 2);
            this.tableLayoutPanel1.Controls.Add(this.lblStandard, 0, 2);
            this.tableLayoutPanel1.Controls.Add(this.lblName, 0, 0);
            this.tableLayoutPanel1.Controls.Add(this.txtName, 1, 0);
            this.tableLayoutPanel1.Controls.Add(this.lblCheckName, 4, 0);
            this.tableLayoutPanel1.Controls.Add(this.cboStandard, 1, 2);
            this.tableLayoutPanel1.Controls.Add(this.odxView1, 0, 5);
            this.tableLayoutPanel1.Controls.Add(this.lblError, 0, 4);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
            this.tableLayoutPanel1.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 6;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 25F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 25F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 25F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 25F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 25F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(340, 290);
            this.tableLayoutPanel1.TabIndex = 1;
            // 
            // txtLongName
            // 
            this.tableLayoutPanel1.SetColumnSpan(this.txtLongName, 3);
            this.txtLongName.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtLongName.Location = new System.Drawing.Point(63, 28);
            this.txtLongName.Name = "txtLongName";
            this.txtLongName.Size = new System.Drawing.Size(242, 21);
            this.txtLongName.TabIndex = 1;
            this.txtLongName.Enter += new System.EventHandler(this.textBox_Enter);
            this.txtLongName.Leave += new System.EventHandler(this.textBox_Leave);
            // 
            // label1
            // 
            this.label1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.label1.Location = new System.Drawing.Point(3, 25);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 25);
            this.label1.TabIndex = 10;
            this.label1.Text = "全名";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblCheckStandard
            // 
            this.lblCheckStandard.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblCheckStandard.ForeColor = System.Drawing.Color.Red;
            this.lblCheckStandard.Location = new System.Drawing.Point(311, 50);
            this.lblCheckStandard.Name = "lblCheckStandard";
            this.lblCheckStandard.Size = new System.Drawing.Size(26, 25);
            this.lblCheckStandard.TabIndex = 8;
            this.lblCheckStandard.Text = "*";
            this.lblCheckStandard.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // txtField
            // 
            this.tableLayoutPanel1.SetColumnSpan(this.txtField, 3);
            this.txtField.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtField.Location = new System.Drawing.Point(63, 78);
            this.txtField.Name = "txtField";
            this.txtField.Size = new System.Drawing.Size(242, 21);
            this.txtField.TabIndex = 4;
            this.txtField.Enter += new System.EventHandler(this.textBox_Enter);
            this.txtField.Leave += new System.EventHandler(this.textBox_Leave);
            // 
            // txtNo
            // 
            this.txtNo.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtNo.Enabled = false;
            this.txtNo.Location = new System.Drawing.Point(217, 53);
            this.txtNo.Name = "txtNo";
            this.txtNo.Size = new System.Drawing.Size(88, 21);
            this.txtNo.TabIndex = 3;
            this.txtNo.TextChanged += new System.EventHandler(this.Check);
            this.txtNo.Enter += new System.EventHandler(this.textBox_Enter);
            this.txtNo.Leave += new System.EventHandler(this.textBox_Leave);
            // 
            // lblField
            // 
            this.lblField.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblField.Location = new System.Drawing.Point(3, 75);
            this.lblField.Name = "lblField";
            this.lblField.Size = new System.Drawing.Size(54, 25);
            this.lblField.TabIndex = 3;
            this.lblField.Text = "搜索字段";
            this.lblField.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblNo
            // 
            this.lblNo.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblNo.Enabled = false;
            this.lblNo.Location = new System.Drawing.Point(157, 50);
            this.lblNo.Name = "lblNo";
            this.lblNo.Size = new System.Drawing.Size(54, 25);
            this.lblNo.TabIndex = 2;
            this.lblNo.Text = "标准序号";
            this.lblNo.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblStandard
            // 
            this.lblStandard.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblStandard.Location = new System.Drawing.Point(3, 50);
            this.lblStandard.Name = "lblStandard";
            this.lblStandard.Size = new System.Drawing.Size(54, 25);
            this.lblStandard.TabIndex = 1;
            this.lblStandard.Text = "所属标准";
            this.lblStandard.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblName
            // 
            this.lblName.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblName.Location = new System.Drawing.Point(3, 0);
            this.lblName.Name = "lblName";
            this.lblName.Size = new System.Drawing.Size(54, 25);
            this.lblName.TabIndex = 0;
            this.lblName.Text = "简称";
            this.lblName.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // txtName
            // 
            this.tableLayoutPanel1.SetColumnSpan(this.txtName, 3);
            this.txtName.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtName.Location = new System.Drawing.Point(63, 3);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(242, 21);
            this.txtName.TabIndex = 0;
            this.txtName.TextChanged += new System.EventHandler(this.Check);
            this.txtName.Enter += new System.EventHandler(this.textBox_Enter);
            this.txtName.Leave += new System.EventHandler(this.textBox_Leave);
            // 
            // lblCheckName
            // 
            this.lblCheckName.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblCheckName.ForeColor = System.Drawing.Color.Red;
            this.lblCheckName.Location = new System.Drawing.Point(311, 0);
            this.lblCheckName.Name = "lblCheckName";
            this.lblCheckName.Size = new System.Drawing.Size(26, 25);
            this.lblCheckName.TabIndex = 5;
            this.lblCheckName.Text = "*";
            this.lblCheckName.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // cboStandard
            // 
            this.cboStandard.Dock = System.Windows.Forms.DockStyle.Fill;
            this.cboStandard.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboStandard.FormattingEnabled = true;
            this.cboStandard.Location = new System.Drawing.Point(63, 53);
            this.cboStandard.Name = "cboStandard";
            this.cboStandard.Size = new System.Drawing.Size(88, 20);
            this.cboStandard.TabIndex = 2;
            this.cboStandard.SelectedIndexChanged += new System.EventHandler(this.cboStandard_SelectedIndexChanged);
            // 
            // odxView1
            // 
            this.odxView1.BackColor = System.Drawing.Color.Black;
            this.tableLayoutPanel1.SetColumnSpan(this.odxView1, 5);
            this.odxView1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.odxView1.Image = image2D1;
            this.odxView1.Location = new System.Drawing.Point(3, 128);
            this.odxView1.Name = "odxView1";
            this.odxView1.Size = new System.Drawing.Size(334, 159);
            this.odxView1.TabIndex = 7;
            // 
            // lblError
            // 
            this.tableLayoutPanel1.SetColumnSpan(this.lblError, 5);
            this.lblError.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lblError.ForeColor = System.Drawing.Color.Red;
            this.lblError.Location = new System.Drawing.Point(3, 100);
            this.lblError.Name = "lblError";
            this.lblError.Size = new System.Drawing.Size(334, 25);
            this.lblError.TabIndex = 9;
            this.lblError.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // PartInfo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.tableLayoutPanel1);
            this.Name = "PartInfo";
            this.Size = new System.Drawing.Size(340, 290);
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.TextBox txtField;
        private System.Windows.Forms.TextBox txtNo;
        private System.Windows.Forms.Label lblField;
        private System.Windows.Forms.Label lblNo;
        private System.Windows.Forms.Label lblStandard;
        private System.Windows.Forms.Label lblName;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label lblCheckName;
        private System.Windows.Forms.ComboBox cboStandard;
        private OdxView odxView1;
        private System.Windows.Forms.Label lblCheckStandard;
        private System.Windows.Forms.Label lblError;
        private System.Windows.Forms.TextBox txtLongName;
        private System.Windows.Forms.Label label1;

    }
}
