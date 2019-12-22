from pycad.system import *
from pycad.runtime import *

@command()
def mymsg(doc):
    from ctypes import windll
    windll.user32.MessageBoxW(0, "Great", "Hello World", 0)

@command()
def showwpf(doc):
    from pytest.forms.WpfTestForm import WpfTestForm
    acap.Application.ShowModalDialog(WpfTestForm())

@command()
def showfrm(doc):
    from pytest.forms.TForm import TForm
    acap.Application.ShowModalDialog(TForm())


        
