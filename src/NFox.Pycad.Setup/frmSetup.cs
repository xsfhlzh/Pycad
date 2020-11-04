using Microsoft.Win32;
using System;
using System.IO;
using System.IO.Compression;
using System.Windows.Forms;
using System.Linq;
using System.Xml.Linq;
using System.Reflection;

namespace NFox.Pycad.Setup
{

    public partial class frmSetup : Form
    {

        ZipArchive _zip;
        Version _ver;
        string _rootpath;
        string _updatepath;
        DirectoryInfo _rootdir;
        DirectoryInfo _maindir;

        bool _setuped = false;

        public frmSetup()
        {

            InitializeComponent();

            using (RegistryKey pycadkey = Registry.CurrentUser.CreateSubKey("Software\\NFox\\Pycad"))
            {
                _rootpath = pycadkey.GetValue("MainPath")?.ToString();
                try { _ver = Version.Parse(pycadkey.GetValue("Version").ToString()); }
                catch { }
            }

            _setuped = true;
            if (_rootpath != null && Directory.Exists(_rootpath))
            {
                _setuped = false;
                textBox1.Text = _rootpath;
                textBox1.Enabled = label2.Enabled = btnSelRoot.Enabled = false;
            }

            var num = Math.Max(AcadVersion.Versions.Count, GcadVersion.Versions.Count);
            tableLayoutPanel4.ColumnCount = num;
            int i = 0;
            for (; i < num - 1; i++)
                tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));

            Height += num * 30;

            i = 0;
            foreach (var verobj in AcadVersion.Versions)
            {
                var chkbox =
                    new CheckBox
                    {
                        Text = verobj.ProductName,
                        Checked = verobj.Selected = true,
                        Tag = verobj
                    };
                tableLayoutPanel4.Controls.Add(chkbox, 0, i++);
            }

            i = 0;
            foreach (var verobj in GcadVersion.Versions)
            {
                var chkbox =
                    new CheckBox
                    {
                        Text = verobj.ProductName,
                        Checked = true,
                        Tag = verobj
                    };
                tableLayoutPanel4.Controls.Add(chkbox, 1, i++);
            }

            using (var stream = Assembly.GetExecutingAssembly().GetManifestResourceStream("Release"))
            using (var zip = new ZipArchive(stream, ZipArchiveMode.Read))
            {
                var ents =
                    zip
                    .Entries
                    .Where(e => e.FullName.Length > 10 && e.FullName.StartsWith("extensions"))
                    .Select(e => e.Name);
                label3.Text = "包含插件：" + string.Join(",", ents);
            }

        }

        private void AddVersionCheckBox(VersionBase verobj, int col, int row)
        {
            var chkbox =
                new CheckBox
                {
                    Text = verobj.ProductName,
                    Checked = verobj.Selected = true,
                    Tag = verobj
                };
            chkbox.CheckedChanged +=
                (s, e) =>
                {
                    var c = (CheckBox)s;
                    var v = (VersionBase)c.Tag;
                    v.Selected = c.Checked;
                };
            tableLayoutPanel4.Controls.Add(chkbox, col, row);
        }


        private void btnCancel_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnOK_Click(object sender, EventArgs e)
        {

            try
            {
                using (var stream = Assembly.GetExecutingAssembly().GetManifestResourceStream("Release"))
                using (_zip = new ZipArchive(stream, ZipArchiveMode.Read))
                using (var cstream = _zip.GetEntry("Version").Open())
                using (var sr = new StreamReader(cstream))
                {

                    var newver = Version.Parse(sr.ReadToEnd());

                    if (!_setuped)
                        Directory.CreateDirectory(_rootpath);

                    if (!_setuped || newver > _ver)
                    {
                        _rootdir = new DirectoryInfo(_rootpath);
                        _updatepath = Path.Combine(_rootpath, "update");
                        if(!Directory.Exists(_updatepath))
                            Directory.CreateDirectory(_updatepath);
                        _maindir = _rootdir.CreateSubdirectory("main");
                        using (RegistryKey pycadkey = Registry.CurrentUser.CreateSubKey("Software\\NFox\\Pycad"))
                        {
                            pycadkey.SetValue("MainPath", _rootpath);
                            pycadkey.SetValue("Version", newver.ToString());
                        }
                        bool inUse = IsFileInUse(Path.Combine(_rootpath, "NFox.Pycad.dll"));
                        VersionBase.RegApp(inUse ? _maindir.FullName : _rootpath);
                        using (var pstream = _zip.GetEntry("package.xml").Open())
                            UpdateFiles(XElement.Load(pstream), new DirectoryInfo(_rootpath), inUse);
                    }

                    //将插件拷贝到更新子目录
                    foreach (var ent in _zip.Entries.Where(ee => ee.FullName.StartsWith("extensions")))
                        CopyTo(ent.Open(), Path.Combine(_updatepath, ent.FullName));

                    MessageBox.Show("安装完毕！");
                }
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
            finally
            {
                Close();
            }

        }

        private void UpdateFiles(XElement xe, DirectoryInfo dir, bool inUse)
        {
            //如果主文件被占用,拷贝主文件和插件到备用目录,否则覆盖主目录文件
            //其余文件拷贝至更新子目录
            foreach (var e in xe.Elements())
            {
                string name = e.Attribute("Name").Value;
                switch (e.Name.LocalName)
                {
                    case "Directory":
                        UpdateFiles(e, dir.CreateSubdirectory(name), inUse);
                        break;
                    case "Module":
                        var dllname = name + ".dll";
                        CopyTo(dllname, Path.Combine(_updatepath, dllname));
                        break;
                    case "Plugin":
                        if (inUse)
                            Unzip(name, _maindir.CreateSubdirectory("plugins\\" + name));
                        else
                            Unzip(name, dir.CreateSubdirectory(name));
                        break;
                    case "File":
                        if(inUse && dir == _rootdir)
                            CopyTo(name, Path.Combine(_maindir.FullName, name));
                        else
                            CopyTo(name, Path.Combine(_updatepath, name));
                        break;
                }
            }
        }

        private void Unzip(string pname, DirectoryInfo dir)
        {
            using (var stream = _zip.GetEntry(pname).Open())
            using (ZipArchive zip = new ZipArchive(stream, ZipArchiveMode.Read))
            {
                foreach (var ent in zip.Entries)
                {
                    string path = dir.FullName + "\\" + ent.FullName;
                    string ddir = Path.GetDirectoryName(path);
                    if (!Directory.Exists(ddir))
                        Directory.CreateDirectory(ddir);
                    CopyTo(ent.Open(), path);
                }
            }
        }

        private void CopyTo(string name, string path)
        {
            CopyTo(_zip.GetEntry(name).Open(), path);
        }

        private void CopyTo(Stream source, string path)
        {
            using(source)
            using (var target = File.OpenWrite(path))
                source.CopyTo(target);
        }

        private static bool IsFileInUse(string fileName)
        {
            bool inUse = true;
            FileStream fs = null;
            try
            {
                fs = new FileStream(fileName, FileMode.Open, FileAccess.Read, FileShare.None);
                inUse = false;
            }
            catch { }
            finally
            {
                if (fs != null)
                    fs.Close();
            }
            return inUse;
        }

    }
}
