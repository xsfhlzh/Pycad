import typing

class acdoc(object):
    """
    获取当前文档

    acdoc(lock = True)

    lock: 是否加文档锁
    """

class lisp(object):
    """
    LispFunction装饰器(函数装饰器)

    lisp(name = None, lock = True) -> lisp

    name: Lisp函数名，默认为py函数名

    lock: 是否加文档锁
    """        
class command(object):
    """
    Command装饰器(函数装饰器)

    command(name = None, flags = 0, lock = True) -> command

    name: 命令名，默认为py函数名

    flags: 命令模式

    lock: 是否加文档锁
    """
class panel(object):
    """
    面板装饰器(类装饰器)

    panel(name = None, flags = 0): -> panel

    name: 命令名，默认为py类名

    flags: 命令模式
    """

def showtime(func):
    """
    显示函数耗费时间
    """