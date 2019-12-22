namespace NFox.Expression.Runtime
{
    partial class frmPartPropertyList
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.partPropertyList1 = new NFox.Expression.Runtime.PartPropertyList();
            this.SuspendLayout();
            // 
            // partPropertyList1
            // 
            this.partPropertyList1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.partPropertyList1.Location = new System.Drawing.Point(0, 0);
            this.partPropertyList1.Margin = new System.Windows.Forms.Padding(0);
            this.partPropertyList1.Name = "partPropertyList1";
            this.partPropertyList1.Part = null;
            this.partPropertyList1.Size = new System.Drawing.Size(232, 140);
            this.partPropertyList1.TabIndex = 0;
            // 
            // frmPartPropertyList
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(232, 140);
            this.ControlBox = false;
            this.Controls.Add(this.partPropertyList1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "frmPartPropertyList";
            this.Opacity = 0.8D;
            this.Leave += new System.EventHandler(this.frmPartPropertyList_Leave);
            this.ResumeLayout(false);

        }

        #endregion

        private PartPropertyList partPropertyList1;
    }
}