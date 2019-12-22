using NFox.Expression.SymbolValues;
using System.Windows.Forms;

namespace NFox.Expression.Runtime
{
    public partial class frmEdit : Form
    {

        public frmEdit()
        {

            InitializeComponent();
            PartNode pnode = new PartNode(Application.WorkingDatabase.Root, false);
            var root = pnode.Node;
            treeView1.Nodes.Add(root);
            root.ExpandAll();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            var pnode = e.Node.Tag as PartNode;
            if (pnode.Part.IsFolder)
            {
                odxListView1.Folder = pnode.Part as PartFolder;
                odxListView1.Visible = true;
                //partEdit1.Visible = false;
            }
            else
            {
                //partEdit1.ImagePart = pnode.Part as ImagePart;
                //partEdit1.Visible = true;
                odxListView1.Visible = false;
            }
        }

    }
}
