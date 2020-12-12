import clr
clr.AddReference('WindowsFormsIntegration')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System')

clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')

from System.Windows.Forms import Form, DockStyle
from System.Windows.Forms.Integration import ElementHost
from System.Drawing import Point
from System.Windows.Controls import UserControl
import wpf

from pycad.system import *
from pycad.runtime import *

class WpfTestForm(Form):
    def __init__(self):
        self.elementHost = ElementHost()
        self.elementHost.Child = UCWpfTestForm()
        self.elementHost.Location = Point(0, 0)
        self.elementHost.Dock = DockStyle.Fill
        self.Controls.Add(self.elementHost)
        self.Text = "WpfTest"


class UCWpfTestForm(UserControl):
    def __init__(self):
        from pycad.system import findfile
        wpf.LoadComponent(self, findfile('WpfTestForm.xaml'))
        from pycad.runtime import utils
        utils.setvalue('WpfTestForm')

    def Input_Button_Click(self, sender, e):
        self.InputTb.Text += sender.Content
        from pycad.runtime import utils
        utils.setvalue('WpfTestForm', self.InputTb.Text)


    def Input_Button_Click2(self, sender, e):
        doc = acapp.DocumentManager.MdiActiveDocument
        if doc:
            with doc.LockDocument():
                with dbtrans(doc) as tr:
                    btr = tr.opencurrspace()
                    tr.addentity(btr, acdb.Line(acge.Point3d(0,0,0), acge.Point3d(10,10,0)))
