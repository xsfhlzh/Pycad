using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Xml.Linq;
using NFox.Expression;
using System.IO;
using NFox.Expression.DataSystem;
using NFox.Expression.SymbolValues;

namespace NFox.Expression.Runtime
{
    public partial class PartListView : UserControl
    {

        public static Part SelectedItem { private set; get; }
        PartNode _pnode;

        public event Part.EventHandler DragStart;
        public event Part.EventHandler PartDefining;

        public PartListView()
        {
            InitializeComponent();
        }

        #region Member

        private PartFolder _root;
        [Browsable(false)]
        public PartFolder Root
        {
            set
            {
                _root = value;
                if (_root == null)
                {
                    _pnode = null;
                    treeView1.Nodes.Clear();
                    Database = null;
                }
                else
                {
                    _pnode = new PartNode(_root, false);
                    var root = _pnode.Node;
                    Database = _root.Database;
                    treeView1.Nodes.Add(root);
                    root.ExpandAll();
                    treeView1.SelectedNode = root;
                    Select(treeView1.SelectedNode);
                }
            }
            get
            {
                return _root;
            }
        }

        public PartFolder Folder
        {
            get
            {
                var pnode = treeView1.SelectedNode.Tag as PartNode;
                return pnode.Part as PartFolder;
            }
        }

        public Database Database { private set; get; }

        #endregion

        #region DragDrop

        bool _isDragDrop;

        private void odxListView1_MouseDown(object sender, MouseEventArgs e)
        {
            var ids = odxListView1.SelectedIndexs;
            if (ids.Count == 1)
            {
                var pIndex = Folder.PartIndexs[odxListView1.SelectedIndex];
                SelectedItem = odxListView1.Database.ImagePartTable[pIndex];
                _isDragDrop = true;
            }
        }

        private void odxListView1_MouseMove(object sender, MouseEventArgs e)
        {
            if (SelectedItem == null) return;
            if (_isDragDrop && e.Button == System.Windows.Forms.MouseButtons.Left)
            {
                _isDragDrop = false;
                if (DragStart != null)
                {
                    DragStart(this, new PartEventArgs(SelectedItem));
                }
            }
        }

        private void partListView_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.UnicodeText))
                e.Effect = DragDropEffects.Move;
        }

        #endregion

        private void odxListView1_PartDefining(object sender, PartEventArgs e)
        {
            if (PartDefining != null)
                PartDefining(sender, e);
        }
        public void UpdateView()
        {
            odxListView1.UpdateSize(false);
        }

        private void Select(TreeNode node)
        {
            PartNode pnode = node.Tag as PartNode;
            odxListView1.Folder = pnode.Part as PartFolder;
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            Select(e.Node);
        }

        private bool _visible = true;
        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            if (_visible)
            {
                tableLayoutPanel1.RowStyles[1].SizeType = SizeType.Absolute;
                tableLayoutPanel1.RowStyles[1].Height = 0;
                tableLayoutPanel1.RowStyles[2].Height = 100f;
                btnDisplay.ToolTipText = "显示目录";
                btnDisplay.Image = NFox.Expression.Properties.Resources.tree1;
            }
            else
            {
                tableLayoutPanel1.RowStyles[1].SizeType = SizeType.Percent;
                tableLayoutPanel1.RowStyles[1].Height = 100 / 3;
                tableLayoutPanel1.RowStyles[2].Height = 100f;
                btnDisplay.ToolTipText = "隐藏目录";
                btnDisplay.Image = NFox.Expression.Properties.Resources.tree0;
            }
            _visible = !_visible;
        }

        private void treeView1_NodeMouseClick(object sender, TreeNodeMouseClickEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                treeView1.SelectedNode = e.Node;
                contextMenuStrip1.Show(treeView1, new Point(e.X, e.Y));
            }

        }

        #region Edit

        private void AddFolder(object sender, EventArgs e)
        {
            frmInputBox form = new frmInputBox("输入目录名称:", "新建目录", "");
            var res = form.ShowDialog();
            if (res == DialogResult.OK && !Folder.HasFolder(form.NewText))
            {
                PartFolder folder = new PartFolder { Name = form.NewText };
                Folder.Add(folder);
            }
        }

        private void RemoveFolder(object sender, EventArgs e)
        {
            var res = MessageBox.Show(
                string.Format("确定删除名为\"{0}\"的目录", Folder.Name),
                "确认删除",
                 MessageBoxButtons.OKCancel);
            if (res == DialogResult.OK)
            {
                if (Folder != Database.Root)
                {
                    var folder = Folder.Parent;
                    folder.Remove(Folder);
                }
            }
        }

        private void RenameFolder(object sender, EventArgs e)
        {
            frmInputBox form =
                new frmInputBox(
                    string.Format("将名为{0}的项目重命名为:", Folder.Name),
                    "项目重命名",
                    Folder.Name);
            var res = form.ShowDialog();
            if (res == DialogResult.OK)
                Folder.Rename(form.NewText);
        }

        private void Save(object sender, EventArgs e)
        {
            odxListView1.Database.Save();
        }

        private void Out(object sender, EventArgs e)
        {
            var folder = Folder;
            SaveFileDialog dlg =
                new SaveFileDialog
                {
                    Filter = "目录(*.pxx)|*.pxx",
                    FileName = folder.Name,
                    RestoreDirectory = true,
                };
            var res = dlg.ShowDialog();
            if (res == DialogResult.OK)
            {
                var database = new Database(folder);
                database.SaveAs(dlg.FileName);
            }
        }

        private void In(object sender, EventArgs e)
        {
            OpenFileDialog dlg =
                new OpenFileDialog
                {
                    Filter = "目录(*.pxx)|*.pxx",
                    RestoreDirectory = true,
                };
            var res = dlg.ShowDialog();
            if (res == DialogResult.OK)
            {
                res = 
                    MessageBox.Show(
                        "同名元件是否覆盖?", 
                        "导入目录",
                        MessageBoxButtons.YesNo);

                var database = new Database(dlg.FileName);
                Database.Merge(Folder, database, res == DialogResult.Yes);
            }
        }


        #endregion


    }
}
