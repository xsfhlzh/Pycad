import clr
clr.AddReference('WindowsFormsIntegration')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System')

clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')

from System.Windows.Forms import DockStyle, UserControl as WinFormUserControl
from System.Windows.Forms.Integration import ElementHost
from System.Drawing import Point
from System.Windows.Controls import UserControl
import wpf

from pycad.system import *
from pycad.runtime import *


class WpfTestPanel(WinFormUserControl):
    def __init__(self):
        self.elementHost = ElementHost()
        self.elementHost.Child = WpfTestPanel()
        self.elementHost.Location = Point(0, 0)
        self.elementHost.Dock = DockStyle.Fill
        self.Controls.Add(self.elementHost)
        self.Text = "WpfTest"


class UCWpfTestPanel(UserControl):
    def __init__(self):
        from pycad.system import findfile
        wpf.LoadComponent(self, findfile('WpfTestForm.xaml'))

    def Input_Button_Click(self, sender, e):
        self.InputTb.Text += sender.Content

    def Input_Button_Click2(self, sender, e):
        with acdoc(True) as cdoc:
            with dbtrans(cdoc.doc) as tr:
                btr = tr.opencurrspace()
                tr.addentity(btr, acdb.Line(acge.Point3d(0,0,0), acge.Point3d(10,10,0)))
