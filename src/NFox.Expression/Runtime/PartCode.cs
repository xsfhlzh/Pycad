using NFox.Expression.DataSystem;
using NFox.Expression.SymbolValues;
using System.Data;
using System.Windows.Forms;

namespace NFox.Expression.Runtime
{
    public partial class PartCode : UserControl
    {

        ImagePart _part;

        public PartCode()
        {
            InitializeComponent();
        }

        public void SetValues(Database database, ImagePart part)
        {
            dataGridView1.Rows.Clear();
            dataGridView1.Columns.Clear();

            _part = part;

            if (_part is ParameterizedPart)
            {
                var pp = _part as ParameterizedPart;
                foreach (var name in database.FunctionTable.DictionaryNames)
                    cboBinName.Items.Add(name);
                cboBinName.Items.Add("新的函数库......");
                cboBinName.Text = pp.Function.Index.DictionaryName;
                txtName.Text = pp.Function.Index.Key;

                var func = pp.Function;
                if (func.Data != null)
                {
                    int i = 0;
                    foreach (var parCode in func.ParamNames)
                    {
                        var cell = new DataGridViewTextBoxCell();
                        dataGridView1.Columns.Add(new DataGridViewColumn(cell));
                        dataGridView1.Columns[i++].HeaderText = parCode;
                    }

                    i = 0;
                    foreach (DataRow r in func.Data.Rows)
                    {
                        dataGridView1.Rows.Add(r.ItemArray);
                    }
                }
                txtCode.Text = func.Code.Replace("\n", "\r\n");
            }
            //else
            //{
            //    txtCode.Text = XParser.ToX(_part).ToString().Replace("\n", "\r\n");
            //}
        }

    }
}
