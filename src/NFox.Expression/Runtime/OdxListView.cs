using System;
using System.Collections.Generic;

using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Threading;
using System.Drawing.Drawing2D;

using System.Drawing.Printing;

using System.Text.RegularExpressions;
using NFox.Expression.DataSystem;
using NFox.Expression.SymbolValues;

namespace NFox.Expression.Runtime
{
    public partial class OdxListView : UserControl
    {

        public OdxListView()
        {
            InitializeComponent();
            SelectedIndexs = new List<int>();
            SelectedItemsChanged = selectedItemsChanged;
        }

        #region Member

        private static Size SmallSize = new Size(400, 300);
        private static Size BigSize = new Size(3200, 2400);

        private int _virtualHeight;
        private int _virtualTop;

        private PartFolder _folder = null;
        [Browsable(false)]
        public PartFolder Folder
        {
            set
            {
                if (value != null)
                {
                    SelectedIndexs = new List<int>();
                    SelectedItemsChanged(this, null);
                    _folder = value;
                    Database = _folder.Database;
                    UpdateSize(false);
                }
            }
            get
            {
                return _folder;
            }
        }

        public Database Database
        { private set; get; }

        private List<int> _visibleItems = new List<int>();
        private Size _itemSize = new Size();

        [Browsable(false)]
        public ImagePart CurrImagePart { private set; get; }


        public event EventHandler SelectedItemsChanged;

        [Browsable(false)]
        public List<int> SelectedIndexs
        { private set; get; }

        [Browsable(false)]
        public int SelectedIndex
        {
            get
            {
                if (SelectedIndexs.Count == 0)
                    return -1;
                return SelectedIndexs.Last();
            }
        }

        [Browsable(false)]
        public ImagePart SelectedItem
        {
            get
            {
                if (SelectedIndex == -1)
                    return null;
                else
                    return Database.ImagePartTable[Folder.PartIndexs[SelectedIndex]];
            }
        }

        private int _wedge = 10;
        private int _hedge = 10;
        [DefaultValue("10,10"), Description("边界大小"), Category("Appearance"), Browsable(true)]
        public Size Edge
        {
            get { return new Size(_wedge, _hedge); }
            set { _wedge = value.Width; _hedge = value.Height; }
        }

        private int _rowCount;
        private int _columnCount = 5;
        [DefaultValue("5"), Description("列数"), Category("Appearance"), Browsable(true)]
        public int ColumnCount
        {
            set
            {
                if (value <= 0)
                    return;
                _columnCount = value;
                UpdateSize(true);
            }
            get
            {
                return _columnCount;
            }
        }

        #endregion

        #region Select

        public IEnumerable<ImagePart> GetSelectedItems()
        {
            return SelectedIndexs.Select(i => Database.ImagePartTable[Folder.PartIndexs[i]]);
        }

        private void selectedItemsChanged(object sender, EventArgs e)
        {
            mnuRemove.Enabled = SelectedIndexs.Count > 0;
            mnuRedefine.Enabled = 
                mnuRename.Enabled = 
                mnuAttributes.Enabled = 
                SelectedIndexs.Count == 1;
        }

        public void SelectAll()
        {
            SelectedIndexs =
                Enumerable
                .Range(0, Folder.PartIndexs.Count)
                .ToList();
            if (SelectedItemsChanged != null)
                SelectedItemsChanged(this, null);
            this.Invalidate();
        }

        public void SelectInvert()
        {
            SelectedIndexs =
               Enumerable.Range(0, Folder.PartIndexs.Count)
               .Except(SelectedIndexs)
               .ToList();
            SelectedItemsChanged(this, null);
            this.Invalidate();
        }

        public void SelectNull()
        {
            SelectedIndexs.Clear();
            SelectedItemsChanged(this, null);
            this.Invalidate();
        }

        public void Select(params int[] ids)
        {
            SelectedIndexs = ids.ToList();
            SelectedItemsChanged(this, null);
            foreach (var id in ids)
                this.Invalidate(id);
        }

        #endregion

        #region Evens

        #region Mouse

        protected override void OnMouseDown(MouseEventArgs e)
        {

            var pindex = GetIndexAtPoint(new Point(e.X, e.Y));
            var index = GetIndex(pindex);
            if (GetImageBounds(pindex).Contains(e.X, e.Y) && index < Folder.PartIndexs.Count)
            {

                if ((ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (e.Button == MouseButtons.Left)
                    {
                        if (SelectedIndexs.Contains(index))
                        {
                            SelectedIndexs.Remove(index);
                            SelectedItemsChanged(this, null);
                            Invalidate(index);
                        }
                        else
                        {
                            SelectedIndexs.Add(index);
                            SelectedItemsChanged(this, null);
                            Invalidate(index);
                        }
                    }
                }
                else
                {
                    if (!SelectedIndexs.Contains(index))
                    {
                        SelectedIndexs.Clear();
                        SelectedIndexs.Add(index);
                        SelectedItemsChanged(this, null);
                        Invalidate();
                    }
                    if (e.Button == MouseButtons.Right)
                        contextMenuStrip1.Show(this,new Point(e.X, e.Y));
                }
            }
            else
            {
                SelectedIndexs.Clear();
                SelectedItemsChanged(this, null);
                Invalidate();
                if (e.Button == MouseButtons.Right)
                    contextMenuStrip1.Show(this, e.X, e.Y);
            }

            base.OnMouseDown(e);

        }

        private int _currX, _currY;

        private void GetCurrInfo(int x, int y)
        {
            _currX = x;
            _currY = y;
            var pt = new Point(x, y);
            var pindex = GetIndexAtPoint(pt);
            var index = GetIndex(pindex);
            if (index < Folder.PartIndexs.Count && GetImageBounds(pindex).Contains(pt))
                CurrImagePart = Database.ImagePartTable[Folder.PartIndexs[index]];
            else
                CurrImagePart = null;
        }

        private bool _showToolTip;
        private ImagePart _oldPart;
        protected override void OnMouseMove(MouseEventArgs e)
        {
            base.OnMouseMove(e);
            GetCurrInfo(e.X, e.Y);
            if (e.Button != MouseButtons.Left && CurrImagePart != null)
            {
                if (!_showToolTip || _oldPart != CurrImagePart)
                {
                    var pindex = GetIndexAtPoint(new Point(e.X, e.Y));
                    var rec = GetImageBounds(pindex);
                    _oldPart = CurrImagePart;
                    var s = _oldPart.Description;
                    var n = s.Split('\n').Length;
                    var t = 20 * (n + 1);
                    var h =
                        Height - rec.Bottom > t ?
                        rec.Bottom :
                        rec.Top - t;
                    toolTip1.Show(s, this, rec.X, h);
                    _showToolTip = true;
                }
            }
            else
            {
                HideToolTip();
            }
        }

        public void HideToolTip()
        {
            toolTip1.Hide(this);
            _showToolTip = false;
        }

        protected override void OnMouseLeave(EventArgs e)
        {
            base.OnMouseLeave(e);
            CurrImagePart = null;
            HideToolTip();
        }

        protected override void OnMouseWheel(MouseEventArgs e)
        {


            base.OnMouseWheel(e);

            if (vScrollBar.Visible)
            {
                var value = vScrollBar.Value;
                value -= e.Delta / 120 * _itemSize.Height;
                if (value < this.Height)
                    value = this.Height;
                else if (value > _virtualHeight)
                    value = _virtualHeight;
                vScrollBar.Value = value;
                GetCurrInfo(e.X, e.Y);
            }

        }

        #endregion

        #region Menu



        public event Part.EventHandler PartDefining;

        private void mnuAdd_Click(object sender, EventArgs e)
        {

            if (PartDefining != null)
            {
                frmMakeGeneralPart form =
                    new frmMakeGeneralPart(
                        Folder,
                        PartDefining);
                if (form.Define())
                {
                    form.ShowDialog();
                    UpdateSize(false);
                }
            }
        }

        private void mnuRedefine_Click(object sender, EventArgs e)
        {
            if (PartDefining != null)
            {
                PartEventArgs pe = new PartEventArgs(null);
                PartDefining(this, pe);
                if (pe.Part != null)
                {
                    SelectedItem.Image = ((ImagePart)pe.Part).Image;
                    UpdateView();
                }
            }
        }

        public void Remove(SymbolIndex index)
        {
            Folder.Remove(index);
            UpdateSize(false);
        }

        private void mnuRemove_Click(object sender, EventArgs e)
        {
            if (SelectedIndexs.Count > 0)
            {
                var parts =
                    SelectedIndexs
                    .Select(i => Folder.PartIndexs[i])
                    .ToList();
                string text;
                if (parts.Count == 1)
                    text = string.Format("确定把\"{0}\"删除", Database.ImagePartTable[parts[0]].Name);
                else
                    text = string.Format("确定把{0}项删除", parts.Count);
                var res =
                    MessageBox.Show(
                        text,
                        "确定删除",
                        MessageBoxButtons.OKCancel);
                if (res == DialogResult.OK)
                {
                    SelectedIndexs.Clear();
                    SelectedItemsChanged(this, null);
                    foreach (var part in parts)
                        Remove(part);
                    UpdateSize(false);
                }
            }
        }

        public void Rename(ImagePart part, string newName)
        {
            var index = part.Index;

            if (Folder.PartIndexs.Contains(index))
            {
                if (Database.ImagePartTable[index.DictionaryName].Has(newName))
                {
                    MessageBox.Show(
                        string.Format("无法重命名\"{0}\":与现有元件重名", newName),
                        "重命名时出错");
                }
                else
                {
                    SymbolIndex oldid = part.Index;
                    SymbolIndex newid = new SymbolIndex(newName, part.Standard, part.No);
                    if (!index.Equals(newid))
                    {
                        Database.ImagePartTable.Redirect(part, newid);
                        Folder.Redirect(oldid, newid);
                    }
                    part.Rename(newName);
                }
            }
        }

        private void mnuRename_Click(object sender, EventArgs e)
        {
            var index = Folder.PartIndexs[SelectedIndex];
            var part = Database.ImagePartTable[index];
            frmInputBox form = 
                new frmInputBox(
                    string.Format("将名为{0}的项目重命名为:", part.Name), 
                    "项目重命名", 
                    part.Name);
            form.ShowDialog();
            if (form.DialogResult == DialogResult.OK)
            {
                Rename(part, form.NewText);
                UpdateView();
            } 
        }

        private void mnuAttributes_Click(object sender, EventArgs e)
        {
            frmAttributeListView form = 
                new frmAttributeListView(Database, SelectedItem);
            var res = form.ShowDialog();
            if (res == DialogResult.OK)
                UpdateView();
        }

        #endregion

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            if (Folder == null) return;

            var g = e.Graphics;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            var foreColorBrush = new SolidBrush(this.ForeColor);
            var halfWhiteBrush = new SolidBrush(Color.FromArgb(96, Color.White));

            var ips =
                from i in _visibleItems
                let index = Folder.PartIndexs[i]
                let Part = Database.ImagePartTable[index]
                select new { Index = i, Part };

            foreach (var ip in ips)
            {

                var pindex = GetIndex(ip.Index);

                //绘制图形
                var imgrec = GetImageBounds(pindex);
                g.FillRectangle(foreColorBrush, imgrec);
                ip.Part.Image.Draw(g, imgrec);

                //计算文字位置
                var name = ip.Part.Name;
                var txtrec = GetTextBounds(pindex);
                var txtsize = g.MeasureString(name, this.Font);
                var pt = new PointF(
                    txtrec.Left + (txtrec.Width - txtsize.Width) / 2,
                    txtrec.Top - txtsize.Height / 2);

                if (SelectedIndexs.Contains(ip.Index))
                {

                    //选中图形加半透明
                    g.FillRectangle(halfWhiteBrush, imgrec);

                    var rec = new RectangleF(pt, txtsize);
                    rec.Offset(-1, -1);
                    //选中文字白色加蓝色底框
                    g.FillRectangle(Brushes.MediumPurple, rec);
                    g.DrawString(name, this.Font, Brushes.WhiteSmoke, pt);
                }
                else
                {
                    //正常绘制文字
                    g.DrawString(name, this.Font, foreColorBrush, pt);
                }
            }

        }
        
        private void vScrollBar_ValueChanged(object sender, EventArgs e)
        {
            _virtualTop = this.Height - vScrollBar.Value;
            UpdateView();
        }

        protected override void OnResize(EventArgs e)
        {
            base.OnResize(e);
            UpdateSize(true);
        }

        protected override void OnKeyDown(KeyEventArgs e)
        {
            base.OnKeyDown(e);
            if (e.KeyData == Keys.Escape)
                SelectNull();
        }



        #endregion

        #region Update

        private void Invalidate(int index)
        {
            if (_visibleItems.Contains(index))
            {
                var olditems = _visibleItems;
                _visibleItems = new List<int> { index };
                this.Invalidate(GetItemBounds(GetIndex(index)));
                _visibleItems = olditems;
            }
        }

        public void UpdateSize(bool isColumnChanged)
        {

            var count = Folder == null ? 0 : Folder.PartIndexs.Count;

            var w = (this.Width - _wedge) / _columnCount;
            var h = (w - _wedge) / 4 * 3 + _hedge + 10;
            _itemSize = new Size((int)w, (int)h);

            int d;
            _rowCount = Math.DivRem(count, _columnCount, out d);
            if (d > 0)
                _rowCount++;
            _virtualHeight = Math.Max(_rowCount * _itemSize.Height + _hedge, this.Height);

            if (vScrollBar.Visible = this.Height < _virtualHeight)
            {
                _itemSize.Width -= 10 / _columnCount;
                vScrollBar.Maximum = _virtualHeight + this.Height;
                vScrollBar.Value = vScrollBar.Minimum = this.Height;
                vScrollBar.SmallChange = _itemSize.Height / 2;
                vScrollBar.LargeChange = this.Height;
            }

            if (isColumnChanged)
                _virtualTop = 0;

            UpdateView();


        }

        public void UpdateView()
        {
            UpdateView(true);
        }

        private void UpdateView(bool redraw)
        {

            if (Folder == null)
                return;

            var minRow = Math.Max(GetNumber(-_virtualTop, _itemSize.Height) - 1, 0);
            var rowCount = GetNumber(Folder.PartIndexs.Count, _columnCount);
            var maxRow = Math.Min(GetNumber(-_virtualTop + this.Height, _itemSize.Height) + 1, rowCount);
            var maxIndex = Math.Min((maxRow + 1) * _columnCount + 1, Folder.PartIndexs.Count);

            _visibleItems = new List<int>();
            for (int i = minRow * _columnCount; i < maxIndex; i++)
                _visibleItems.Add(i);

            if (redraw)
                this.Invalidate();
        }


        #endregion

        #region Bounds

        private int GetNumber(int total, int single)
        {
            int d;
            var index = Math.DivRem(total, single, out d);
            return index;
        }

        //获取单元区域
        internal Rectangle GetItemBounds(Point pindex)
        {
            return
                new Rectangle(
                    _itemSize.Width * pindex.X + _wedge,
                    _itemSize.Height * pindex.Y + _virtualTop + _hedge,
                    _itemSize.Width - _wedge,
                    _itemSize.Height);
        }

        //获取图形区域
        internal Rectangle GetImageBounds(Point pindex)
        {
            return
                new Rectangle(
                    _itemSize.Width * pindex.X + _wedge,
                    _itemSize.Height * pindex.Y + _virtualTop + _hedge,
                    _itemSize.Width - _wedge,
                    _itemSize.Height - _hedge - 10);
        }

        //获取标签区域
        internal RectangleF GetTextBounds(Point pindex)
        {
            return
                new RectangleF(
                    _itemSize.Width * pindex.X + _wedge,
                    _itemSize.Height * (pindex.Y + 1) + _virtualTop,
                    _itemSize.Width - _wedge,
                    10);
        }

        //按一维数组索引返回行列索引
        private Point GetIndex(int index)
        {
            int row, col;
            row = Math.DivRem(index, _columnCount, out col);
            return new Point(col, row);
        }

        //按行列索引返回一维数组索引
        private int GetIndex(Point pindex)
        {
            return pindex.Y * _columnCount + pindex.X;
        }



        //返回点所在的行列索引
        private Point GetIndexAtPoint(Point pt)
        {
            var col = GetNumber(pt.X, _itemSize.Width);
            var row = GetNumber(pt.Y - _virtualTop, _itemSize.Height);
            return new Point(col, row);
        }

        #endregion

    }

}

