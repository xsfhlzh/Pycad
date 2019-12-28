import typing

class acdoc(object):
    def __init__(self, lock = True):
        """
        获取当前文档

            lock: 是否加文档锁
        """

class lisp(object):
    def __init__(self, name = None, lock = True):
        """
        LispFunction装饰器(函数装饰器)

            name: Lisp函数名，默认为函数名
            lock: 是否加文档锁
        """        
class command(object):
    def __init__(self, name = None, flags = 0, lock = True):
        """
        Command装饰器(函数装饰器)

            name: 命令名，默认为函数名
            flags: 命令模式
            lock: 是否加文档锁
        """
class panel(object):
    def __init__(self, name = None, flags = 0):
        """
        面板装饰器(类装饰器)

            name: 命令名，默认为py类名
            flags: 命令模式
        """
class vcm(object):
    """
    版本控制装饰器(函数装饰器)

        vcm.default
        vcm.apply(appname, ver = -1)
    """
    @staticmethod
    def default(func):...
    @staticmethod
    def apply(appname, ver = -1):...

def showtime(func):
    """
    显示函数耗费时间
    """