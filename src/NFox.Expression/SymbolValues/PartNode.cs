using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace NFox.Expression.SymbolValues
{
    public class PartNode : IDisposable
    {

        public PartNode Parent
        { private set; get; }

        public TreeNode Node
        { private set; get; }

        public Part Part
        { private set; get; }

        public List<PartNode> Nodes
        { private set; get; }

        public bool CreateImageNodes
        { private set; get; }

        public PartNode(PartFolder part, bool createImageNodes)
        {
            Part = part;
            CreateImageNodes = createImageNodes;
            Node = new TreeNode(part.Name, 0, 1);
            Node.Tag = this;
            MakeNode();
            part.PartAdding += partAdding;
            part.PartRemoving += partRemoving;
            part.PartRenaming += partRenaming;
        }

        private PartNode(PartFolder part, PartNode parent, bool createImageNodes)
        {
            Part = part;
            CreateImageNodes = createImageNodes;
            Node = new TreeNode(part.Name, 0, 1);
            Node.Tag = this;
            Parent = parent;
            parent.Node.Nodes.Add(Node);
            part.PartAdding += partAdding;
            part.PartRemoving += partRemoving;
            part.PartRenaming += partRenaming;
        }

        private PartNode(ImagePart part, PartNode parent)
        {
            Part = part;
            CreateImageNodes = true;
            if (part is ImagePart)
                Node = new TreeNode(part.Name, 2, 3);
            else
                Node = new TreeNode(part.Name, 4, 5);
            Node.Tag = this;
            Parent = parent;
            parent.Node.Nodes.Add(Node);
            part.PartRenaming += partRenaming;
        }

        private void partRenaming(object sender, PartEventArgs e)
        {
            Node.Text = e.Tag as string;
        }

        private void partRemoving(object sender, PartEventArgs e)
        {
            if (e.Part.IsFolder || CreateImageNodes)
            {
                foreach (var pnode in Nodes)
                {
                    if (pnode.Part == e.Part)
                    {
                        Node.Nodes.Remove(pnode.Node);
                        Nodes.Remove(pnode);
                        pnode.Dispose();
                        return;
                    }
                }
            }
        }

        private void partAdding(object sender, PartEventArgs e)
        {
            if (e.Part.IsFolder)
            {
                var pnode = new PartNode(e.Part as PartFolder, CreateImageNodes);
                pnode.Parent = this;
                Nodes.Add(pnode);
                Node.Nodes.Add(pnode.Node);
            }
            else if (CreateImageNodes)
            {
                var pnode = new PartNode(e.Part as ImagePart, this);
                Nodes.Add(pnode);
            }
        }

        private void MakeNode()
        {
            if (Part.IsFolder)
            {
                Nodes = new List<PartNode>();
                var folder = Part as PartFolder;
                foreach (var subFolder in folder.Folders)
                {
                    var pnode = new PartNode(subFolder, this, CreateImageNodes);
                    pnode.MakeNode();
                    Nodes.Add(pnode);
                }
                if (CreateImageNodes)
                {
                    foreach (var subPart in folder.GetParts())
                        Nodes.Add(new PartNode(subPart, this));
                }
            }
        }


        public void Dispose()
        {
            if (Part.IsFolder)
            {
                foreach (var pnode in Nodes)
                    pnode.Dispose();
                PartFolder folder = Part as PartFolder;
                folder.PartAdding -= partAdding;
                folder.PartRemoving -= partRemoving;
                folder.PartRenaming -= partRenaming;
            }
            else
            {
                ImagePart part = Part as ImagePart;
                part.PartRenaming -= partRenaming;
            }

            Parent = null;
            Part = null;
            Nodes = null;
            Node = null;

        }
    }
}
