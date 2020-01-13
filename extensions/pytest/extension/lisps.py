from pycad.system import *
from pycad.runtime import *

#linq支持
import clr
import System
clr.ImportExtensions(System.Linq)

@lisp()
@showtime
def mylisp(doc, args):
    #获取当前运行的所有进程
    from System.Diagnostics import Process
    return [x.ProcessName for x in Process.GetProcesses()]

@lisp()
def mylisp0(doc, args):
    for lispdata in args[0]:
        print(lispdata)
    return args[0][0]

@lisp()
@showtime
def mylisp1(doc, args):
    import random, string
    strs = [
        ''.join(
            random.choice(string.ascii_lowercase) 
            for _ in range(500)) 
        for _ in range(10000)]
    return strs

@lisp()
def mylisp2(doc, args):
    return sum(args)

@lisp()
def mylisp3(doc, args):
    from .forms.WpfTestForm import WpfTestForm
    acapp.ShowModalDialog(WpfTestForm())
    return utils.getvalue('WpfTestForm')

@lisp()
def mylisp4(doc, args):
    return [1,[2,3],4,[5,6,[7,8,[9]]]]

@lisp()
def clipboard(doc, args):
    from System.Windows.Forms import Clipboard
    count = len(args)
    if count == 0:
        return Clipboard.GetText()
    elif count == 1:
        Clipboard.SetText(args[0])
