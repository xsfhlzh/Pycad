#coding:utf-8

#初始化模块

__all__ = [
    'conv', 'acapp', 'acdoc', 'guid', 'stdio', 'pye',
    'lisp', 'command', 'panel', 'vcm','showtime',
    'help', 'switch', 'flatten']

from pycad.system.mgdnss import *
from pycad.system.wraps import *
from pycad.system.decorators import *
from pycad.system import conv

from NFox.Pycad.Core.Modules import pye, io

import sys
stdio = io.instance
sys.stdin = sys.stdout = sys.stderr = stdio

from . import mgdnss
__all__ += mgdnss.__all__
mgds = mgdnss._mgds

#设置中文支持
import imp
imp.reload(sys)
sys.setdefaultencoding('utf-8')

_filename = None

@command()
def pyrun(doc):
    pfo = aced.PromptOpenFileOptions("选择Python脚本")
    pfo.Filter = "Python脚本文件(*.py)|*.py"
    pfo.PreferCommandLine = acapp.GetSystemVariable("FILEDIA") == 0
    pfo.InitialDirectory = pye.extensionspath + "\\scripts\\"
    global _filename
    pfo.InitialFileName = _filename
    pr = doc.Editor.GetFileNameForOpen(pfo)
    if pr.Status == aced.PromptStatus.OK:
        try:
            pye.executefile(pr.StringResult)
            _filename = pr.StringResult.rsplit('\\',1)[1]
        except: pass

@command()
def pyinstall(doc):
    pfo = aced.PromptOpenFileOptions("选择py工程(编译版本)")
    pfo.Filter = "py工程(*.ext)|*.ext"
    pfo.PreferCommandLine = acapp.GetSystemVariable("FILEDIA") == 0
    pr = doc.Editor.GetFileNameForOpen(pfo)
    if pr.Status == aced.PromptStatus.OK:
        pye.install(pr.StringResult)

@command()
def pyreference(doc):
    pfo = aced.PromptOpenFileOptions("选择.Net类库")
    pfo.Filter = ".Net类库(*.dll)|*.dll"
    pfo.PreferCommandLine = acapp.GetSystemVariable("FILEDIA") == 0
    pr = doc.Editor.GetFileNameForOpen(pfo)
    if pr.Status == aced.PromptStatus.OK:
        pye.reference(pr.StringResult)