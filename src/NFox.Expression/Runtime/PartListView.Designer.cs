namespace NFox.Expression.Runtime
{
    partial class PartListView
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(PartListView));
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.btnAddFolder = new System.Windows.Forms.ToolStripButton();
            this.btnRemoveFolder = new System.Windows.Forms.ToolStripButton();
            this.btnRenameFolder = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.btnSave = new System.Windows.Forms.ToolStripButton();
            this.btnOut = new System.Windows.Forms.ToolStripButton();
            this.btnIn = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.btnDisplay = new System.Windows.Forms.ToolStripButton();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.mnuAddFolder = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRemoveFolder = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRenameFolder = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
            this.mnuSave = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuOut = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuIn = new System.Windows.Forms.ToolStripMenuItem();
            this.odxListView1 = new NFox.Expression.Runtime.OdxListView();
            this.tableLayoutPanel1.SuspendLayout();
            this.toolStrip1.SuspendLayout();
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // treeView1
            // 
            this.treeView1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(224)))), ((int)(((byte)(192)))));
            this.treeView1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.treeView1.ImageIndex = 0;
            this.treeView1.ImageList = this.imageList1;
            this.treeView1.Location = new System.Drawing.Point(0, 25);
            this.treeView1.Margin = new System.Windows.Forms.Padding(0);
            this.treeView1.Name = "treeView1";
            this.treeView1.SelectedImageIndex = 0;
            this.treeView1.ShowLines = false;
            this.treeView1.Size = new System.Drawing.Size(320, 200);
            this.treeView1.TabIndex = 0;
            this.treeView1.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.treeView1_AfterSelect);
            this.treeView1.NodeMouseClick += new System.Windows.Forms.TreeNodeMouseClickEventHandler(this.treeView1_NodeMouseClick);
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "06.png");
            this.imageList1.Images.SetKeyName(1, "010.png");
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.ColumnCount = 1;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel1.Controls.Add(this.treeView1, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.toolStrip1, 0, 0);
            this.tableLayoutPanel1.Controls.Add(this.odxListView1, 0, 2);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
            this.tableLayoutPanel1.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 3;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 25F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 200F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(320, 640);
            this.tableLayoutPanel1.TabIndex = 212;
            // 
            // toolStrip1
            // 
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnAddFolder,
            this.btnRemoveFolder,
            this.btnRenameFolder,
            this.toolStripSeparator1,
            this.btnSave,
            this.btnOut,
            this.btnIn,
            this.toolStripSeparator2,
            this.btnDisplay});
            this.toolStrip1.Location = new System.Drawing.Point(0, 0);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(320, 25);
            this.toolStrip1.TabIndex = 3;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // btnAddFolder
            // 
            this.btnAddFolder.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnAddFolder.Image = ((System.Drawing.Image)(resources.GetObject("btnAddFolder.Image")));
            this.btnAddFolder.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnAddFolder.Name = "btnAddFolder";
            this.btnAddFolder.Size = new System.Drawing.Size(23, 22);
            this.btnAddFolder.Text = "新建目录";
            this.btnAddFolder.Click += new System.EventHandler(this.AddFolder);
            // 
            // btnRemoveFolder
            // 
            this.btnRemoveFolder.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnRemoveFolder.Image = ((System.Drawing.Image)(resources.GetObject("btnRemoveFolder.Image")));
            this.btnRemoveFolder.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnRemoveFolder.Name = "btnRemoveFolder";
            this.btnRemoveFolder.Size = new System.Drawing.Size(23, 22);
            this.btnRemoveFolder.Text = "删除目录";
            this.btnRemoveFolder.Click += new System.EventHandler(this.RemoveFolder);
            // 
            // btnRenameFolder
            // 
            this.btnRenameFolder.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnRenameFolder.Image = ((System.Drawing.Image)(resources.GetObject("btnRenameFolder.Image")));
            this.btnRenameFolder.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnRenameFolder.Name = "btnRenameFolder";
            this.btnRenameFolder.Size = new System.Drawing.Size(23, 22);
            this.btnRenameFolder.Text = "目录重命名";
            this.btnRenameFolder.Click += new System.EventHandler(this.RenameFolder);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(6, 25);
            // 
            // btnSave
            // 
            this.btnSave.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnSave.Image = ((System.Drawing.Image)(resources.GetObject("btnSave.Image")));
            this.btnSave.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(23, 22);
            this.btnSave.Text = "保存";
            this.btnSave.Click += new System.EventHandler(this.Save);
            // 
            // btnOut
            // 
            this.btnOut.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnOut.Image = ((System.Drawing.Image)(resources.GetObject("btnOut.Image")));
            this.btnOut.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnOut.Name = "btnOut";
            this.btnOut.Size = new System.Drawing.Size(23, 22);
            this.btnOut.Text = "导出";
            this.btnOut.Click += new System.EventHandler(this.Out);
            // 
            // btnIn
            // 
            this.btnIn.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnIn.Image = ((System.Drawing.Image)(resources.GetObject("btnIn.Image")));
            this.btnIn.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnIn.Name = "btnIn";
            this.btnIn.Size = new System.Drawing.Size(23, 22);
            this.btnIn.Text = "导入";
            this.btnIn.Click += new System.EventHandler(this.In);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(6, 25);
            // 
            // btnDisplay
            // 
            this.btnDisplay.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnDisplay.Image = ((System.Drawing.Image)(resources.GetObject("btnDisplay.Image")));
            this.btnDisplay.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnDisplay.Name = "btnDisplay";
            this.btnDisplay.Size = new System.Drawing.Size(23, 22);
            this.btnDisplay.Text = "隐藏目录";
            this.btnDisplay.Click += new System.EventHandler(this.toolStripButton1_Click);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuAddFolder,
            this.mnuRemoveFolder,
            this.mnuRenameFolder,
            this.toolStripSeparator5,
            this.mnuSave,
            this.mnuOut,
            this.mnuIn});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(149, 142);
            // 
            // mnuAddFolder
            // 
            this.mnuAddFolder.Image = ((System.Drawing.Image)(resources.GetObject("mnuAddFolder.Image")));
            this.mnuAddFolder.Name = "mnuAddFolder";
            this.mnuAddFolder.Size = new System.Drawing.Size(148, 22);
            this.mnuAddFolder.Text = "新建目录(&M)";
            this.mnuAddFolder.Click += new System.EventHandler(this.AddFolder);
            // 
            // mnuRemoveFolder
            // 
            this.mnuRemoveFolder.Image = ((System.Drawing.Image)(resources.GetObject("mnuRemoveFolder.Image")));
            this.mnuRemoveFolder.Name = "mnuRemoveFolder";
            this.mnuRemoveFolder.Size = new System.Drawing.Size(148, 22);
            this.mnuRemoveFolder.Text = "删除目录(&D)";
            this.mnuRemoveFolder.Click += new System.EventHandler(this.RemoveFolder);
            // 
            // mnuRenameFolder
            // 
            this.mnuRenameFolder.Image = ((System.Drawing.Image)(resources.GetObject("mnuRenameFolder.Image")));
            this.mnuRenameFolder.Name = "mnuRenameFolder";
            this.mnuRenameFolder.Size = new System.Drawing.Size(148, 22);
            this.mnuRenameFolder.Text = "目录重命名(&M)";
            this.mnuRenameFolder.Click += new System.EventHandler(this.RenameFolder);
            // 
            // toolStripSeparator5
            // 
            this.toolStripSeparator5.Name = "toolStripSeparator5";
            this.toolStripSeparator5.Size = new System.Drawing.Size(145, 6);
            // 
            // mnuSave
            // 
            this.mnuSave.Image = ((System.Drawing.Image)(resources.GetObject("mnuSave.Image")));
            this.mnuSave.Name = "mnuSave";
            this.mnuSave.Size = new System.Drawing.Size(148, 22);
            this.mnuSave.Text = "保存(&S)";
            this.mnuSave.Click += new System.EventHandler(this.Save);
            // 
            // mnuOut
            // 
            this.mnuOut.Image = ((System.Drawing.Image)(resources.GetObject("mnuOut.Image")));
            this.mnuOut.Name = "mnuOut";
            this.mnuOut.Size = new System.Drawing.Size(148, 22);
            this.mnuOut.Text = "导出";
            this.mnuOut.Click += new System.EventHandler(this.Out);
            // 
            // mnuIn
            // 
            this.mnuIn.Image = ((System.Drawing.Image)(resources.GetObject("mnuIn.Image")));
            this.mnuIn.Name = "mnuIn";
            this.mnuIn.Size = new System.Drawing.Size(148, 22);
            this.mnuIn.Text = "导入";
            this.mnuIn.Click += new System.EventHandler(this.In);
            // 
            // odxListView1
            // 
            this.odxListView1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.odxListView1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.odxListView1.ColumnCount = 3;
            this.odxListView1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.odxListView1.Edge = new System.Drawing.Size(10, 10);
            this.odxListView1.Folder = null;
            this.odxListView1.Location = new System.Drawing.Point(0, 225);
            this.odxListView1.Margin = new System.Windows.Forms.Padding(0);
            this.odxListView1.Name = "odxListView1";
            this.odxListView1.Size = new System.Drawing.Size(320, 415);
            this.odxListView1.TabIndex = 4;
            this.odxListView1.PartDefining += new NFox.Expression.SymbolValues.Part.EventHandler(this.odxListView1_PartDefining);
            this.odxListView1.DragEnter += new System.Windows.Forms.DragEventHandler(this.partListView_DragEnter);
            this.odxListView1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.odxListView1_MouseDown);
            this.odxListView1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.odxListView1_MouseMove);
            // 
            // PartListView
            // 
            this.AllowDrop = true;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.tableLayoutPanel1);
            this.Name = "PartListView";
            this.Size = new System.Drawing.Size(320, 640);
            this.DragEnter += new System.Windows.Forms.DragEventHandler(this.partListView_DragEnter);
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripButton btnDisplay;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.ToolStripButton btnAddFolder;
        private System.Windows.Forms.ToolStripButton btnRemoveFolder;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripButton btnSave;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mnuAddFolder;
        private System.Windows.Forms.ToolStripMenuItem mnuRemoveFolder;
        private System.Windows.Forms.ToolStripMenuItem mnuSave;
        private System.Windows.Forms.ToolStripButton btnRenameFolder;
        private System.Windows.Forms.ToolStripMenuItem mnuRenameFolder;
        private System.Windows.Forms.ToolStripButton btnOut;
        private System.Windows.Forms.ToolStripButton btnIn;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator5;
        private System.Windows.Forms.ToolStripMenuItem mnuOut;
        private System.Windows.Forms.ToolStripMenuItem mnuIn;
        private Expression.Runtime.OdxListView odxListView1;
    }
}
