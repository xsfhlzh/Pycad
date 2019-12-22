namespace NFox.Expression.Runtime
{
    partial class OdxListView
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(OdxListView));
            this.vScrollBar = new System.Windows.Forms.VScrollBar();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.mnuAdd = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRemove = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRename = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuRedefine = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuAttributes = new System.Windows.Forms.ToolStripMenuItem();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // vScrollBar
            // 
            this.vScrollBar.Dock = System.Windows.Forms.DockStyle.Right;
            this.vScrollBar.LargeChange = 120;
            this.vScrollBar.Location = new System.Drawing.Point(483, 0);
            this.vScrollBar.Maximum = 500;
            this.vScrollBar.Name = "vScrollBar";
            this.vScrollBar.Size = new System.Drawing.Size(17, 400);
            this.vScrollBar.SmallChange = 60;
            this.vScrollBar.TabIndex = 1;
            this.vScrollBar.ValueChanged += new System.EventHandler(this.vScrollBar_ValueChanged);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuAdd,
            this.mnuRemove,
            this.mnuRename,
            this.toolStripSeparator2,
            this.mnuRedefine,
            this.mnuAttributes});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(153, 142);
            // 
            // mnuAdd
            // 
            this.mnuAdd.Image = ((System.Drawing.Image)(resources.GetObject("mnuAdd.Image")));
            this.mnuAdd.Name = "mnuAdd";
            this.mnuAdd.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.W)));
            this.mnuAdd.ShowShortcutKeys = false;
            this.mnuAdd.Size = new System.Drawing.Size(152, 22);
            this.mnuAdd.Text = "新建(&W)";
            this.mnuAdd.Click += new System.EventHandler(this.mnuAdd_Click);
            // 
            // mnuRemove
            // 
            this.mnuRemove.Image = ((System.Drawing.Image)(resources.GetObject("mnuRemove.Image")));
            this.mnuRemove.Name = "mnuRemove";
            this.mnuRemove.ShortcutKeys = System.Windows.Forms.Keys.Delete;
            this.mnuRemove.ShowShortcutKeys = false;
            this.mnuRemove.Size = new System.Drawing.Size(152, 22);
            this.mnuRemove.Text = "删除(&D)";
            this.mnuRemove.Click += new System.EventHandler(this.mnuRemove_Click);
            // 
            // mnuRename
            // 
            this.mnuRename.Name = "mnuRename";
            this.mnuRename.Size = new System.Drawing.Size(152, 22);
            this.mnuRename.Text = "重命名(&N)";
            this.mnuRename.Click += new System.EventHandler(this.mnuRename_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(149, 6);
            // 
            // mnuRedefine
            // 
            this.mnuRedefine.Image = ((System.Drawing.Image)(resources.GetObject("mnuRedefine.Image")));
            this.mnuRedefine.Name = "mnuRedefine";
            this.mnuRedefine.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.M)));
            this.mnuRedefine.ShowShortcutKeys = false;
            this.mnuRedefine.Size = new System.Drawing.Size(152, 22);
            this.mnuRedefine.Text = "重定义(&M)";
            this.mnuRedefine.Click += new System.EventHandler(this.mnuRedefine_Click);
            // 
            // mnuAttributes
            // 
            this.mnuAttributes.Name = "mnuAttributes";
            this.mnuAttributes.Size = new System.Drawing.Size(152, 22);
            this.mnuAttributes.Text = "编辑属性(&E)";
            this.mnuAttributes.Click += new System.EventHandler(this.mnuAttributes_Click);
            // 
            // toolTip1
            // 
            this.toolTip1.AutoPopDelay = 5000;
            this.toolTip1.InitialDelay = 200;
            this.toolTip1.ReshowDelay = 100;
            this.toolTip1.ToolTipTitle = "零件说明";
            // 
            // OdxListView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Transparent;
            this.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.Controls.Add(this.vScrollBar);
            this.DoubleBuffered = true;
            this.Name = "OdxListView";
            this.Size = new System.Drawing.Size(500, 400);
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.VScrollBar vScrollBar;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mnuRemove;
        private System.Windows.Forms.ToolStripMenuItem mnuRedefine;
        private System.Windows.Forms.ToolStripMenuItem mnuAdd;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.ToolStripMenuItem mnuAttributes;
        private System.Windows.Forms.ToolStripMenuItem mnuRename;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
    }
}
