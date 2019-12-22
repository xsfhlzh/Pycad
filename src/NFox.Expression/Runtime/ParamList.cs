using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using NFox.Expression;
using NFox.Expression.SymbolValues;

namespace NFox.Expression.Runtime
{
    public partial class ParamList : UserControl
    {

        public ParamList()
        {
            InitializeComponent();
        }

        private bool _isSelectting;

        public delegate void ParamChangedEvent(object sender, EventArgs e);
        public event ParamChangedEvent ParamChanged;

        public Image2D Image
        { private set; get; }

        private List<ParamBox> _items;
        public List<ParamBox> Items
        {
            get
            {
                return
                    flowLayoutPanel1
                    .Controls
                    .Cast<ParamBox>()
                    .ToList();
            }
        }

        private ParameterizedPart _part;
        public ParameterizedPart Part
        {
            set
            {
                _isSelectting = false;
                flowLayoutPanel1.Controls.Clear();
                if (value == null) return;

                _part = value as ParameterizedPart;
                var func = _part.Function;
                if (func.Data != null)
                {

                    var keys = func.ParamNames.GetEnumerator();
                    int count = _part.ParamCount;
                    keys.MoveNext();
                    string code = keys.Current;
                    var pbox =
                        new ParamBox(
                            code,
                            func.Data.Rows.Cast<DataRow>().Select(r => r[code].ToString()),
                            true,
                            first_SelectedIndexChanged);
                    pbox.Width = flowLayoutPanel1.Width - 20;
                    flowLayoutPanel1.Controls.Add(pbox);

                    while(keys.MoveNext())
                    {
                        code = keys.Current;
                        pbox =
                            new ParamBox(
                                code,
                                func.Data.Rows.Cast<DataRow>().Select(r => r[code].ToString()),
                                false,
                                other_SelectedIndexChanged);
                        pbox.Width = flowLayoutPanel1.Width - 20;
                        flowLayoutPanel1.Controls.Add(pbox);
                    }

                }

                _items =
                    flowLayoutPanel1
                    .Controls
                    .Cast<ParamBox>()
                    .ToList();

                for (int i = 0; i < _part.ParamCount; i++)
                    _items[i].Text = func.ParamNames[i];

                _isSelectting = true;
                Image = _part.Image;

            }

            get
            {
                return _part;
            }

        }

        void first_SelectedIndexChanged(object sender, EventArgs e)
        {
            var first = sender as ComboBox;
            var count = flowLayoutPanel1.Controls.Count;
            for (int i = 1; i < _items.Count; i++)
            {
                var pbox = _items[i];
                pbox.SelectedIndex = first.SelectedIndex;
            }
            if (_isSelectting) Eval();
        }

        void other_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (_isSelectting) Eval();
        }

        private void Eval()
        {
            var pars =
                _items
                .Select(p => p.Text)
                .ToList();
            Image = _part.Eval(pars);
            if (ParamChanged != null)
                ParamChanged(Image, null);
        }

    }
}
