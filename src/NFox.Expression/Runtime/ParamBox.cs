using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace NFox.Expression.Runtime
{
    public partial class ParamBox : UserControl
    {


        enum ParamBoxType
        {
            First,
            ComBox,
            Label
        }

        private EventHandler _selectedIndexChanged;
        private List<string> _items;
        private Control _ctl;
        private ParamBoxType _type;

        public string Label
        {
            set { label1.Text = value + ":"; }
            get { var s =label1.Text;  return s.Substring(0, s.Length - 1); }
        }

        public override string Text
        {
            get { return _ctl.Text; }
            set { _ctl.Text = value; }
        }

        private int _slectedIndex;
        public int SelectedIndex
        {
            set
            {

                _slectedIndex = value;
                string s = _items[value];

                ComboBox cbo = null;
                switch (_type)
                {
                    case ParamBoxType.Label:
                        _ctl.Text = s;
                        break;
                    case ParamBoxType.First:
                        cbo = _ctl as ComboBox;
                        cbo.SelectedIndex = value;
                        break;
                    case ParamBoxType.ComBox:
                        cbo = _ctl as ComboBox;
                        cbo.SelectedIndexChanged -= _selectedIndexChanged;
                        cbo.Items.Clear();
                        cbo.Items.AddRange(s.Split(','));
                        cbo.SelectedIndex = 0;
                        cbo.SelectedIndexChanged += _selectedIndexChanged;
                        break;
                }

            }
            get { return _slectedIndex; }
        }

        public ParamBox(string label, IEnumerable<string> items, bool atFirst, Action<object, EventArgs> selectedIndexChanged)
        {

            InitializeComponent();

            Label = label;
            _items = items.ToList();
            _selectedIndexChanged = new EventHandler(selectedIndexChanged);

            var margin = new Padding(0, 0, 0, 3);

            if (atFirst)
                _type = ParamBoxType.First;
            else if (_items[0].Contains(','))
                _type = ParamBoxType.ComBox;
            else
                _type = ParamBoxType.Label;

            if (_type == ParamBoxType.Label)
            {
                var lbl =
                   new Label
                   {
                       AutoSize = false,
                       Margin = margin,
                       BorderStyle = BorderStyle.Fixed3D,
                       BackColor = Color.Transparent,
                       TextAlign = ContentAlignment.MiddleLeft,
                       Dock = DockStyle.Fill,
                   };
                tableLayoutPanel1.Controls.Add(_ctl = lbl, 1, 0);
            }
            else
            {
                var cbo =
                   new ComboBox
                   {
                       Margin = margin,
                       DropDownStyle = ComboBoxStyle.DropDownList,
                       Dock = DockStyle.Fill,
                   };

                cbo.MouseEnter += new EventHandler(cbo_MouseEnter);

                tableLayoutPanel1.Controls.Add(_ctl = cbo, 1, 0);
                if(_type == ParamBoxType.First)
                    cbo.Items.AddRange(items.ToArray());

                cbo.SelectedIndexChanged += _selectedIndexChanged;
            }

        }

        [DllImport("user32.dll", SetLastError = true)]
        static extern IntPtr SetActiveWindow(IntPtr hWnd);

        void cbo_MouseEnter(object sender, EventArgs e)
        {
            ComboBox cbo = sender as ComboBox;
            SetActiveWindow(cbo.Handle);
            cbo.Focus();
        }



    }
}
