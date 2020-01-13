from pycad.system import *
from pycad.runtime import *

import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *

@panel('testpanel')
class showpanel(object):
    guid = '49ddd006-4411-46a9-bc55-86c5e2fb8410'
    text = '测试面板'
    dock = acws.DockSides.Right
    size = (320, 320)
    from extension.forms.TPanel import TPanel
    itemtypes = {"T1": TPanel, "T2": Button}
    def __init__(self, doc, tabs):
        pass
    def __docked__(self, doc):
        print("\nhello world!")


