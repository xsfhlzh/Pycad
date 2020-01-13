#coding:utf-8

#初始化模块

__all__ = [
    'conv', 'acapp', 'acdoc', 'guid', 'stdio', 'pye',
    'lisp', 'command', 'panel', 'vcm','showtime',
    'help', 'switch', 'flatten', 'findfile']

from pycad.system.mgdnss import *
from pycad.system.wraps import *
from pycad.system.decorators import *
from pycad.system import conv

from NFox.Pycad.Core.Modules import pye, io

import sys
stdio = io.instance
sys.stdin = sys.stdout = sys.stderr = stdio

from pycad.system import mgdnss
__all__ += mgdnss.__all__
mgds = mgdnss._mgds

#设置中文支持
import imp
imp.reload(sys)
sys.setdefaultencoding('utf-8')

cext = None
def findfile(filename):
    return pye.findfile(cext, filename)