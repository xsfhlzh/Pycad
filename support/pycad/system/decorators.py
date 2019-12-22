
class acdoc(object):
    def __init__(self, lock = True):
        from . import acapp, io
        self.doc = acapp.DocumentManager.MdiActiveDocument
        self.ed, io.instance.ed = io.instance.ed, self.doc.Editor
        self.lock = lock
        if self.lock:
            self.doclock = self.doc.LockDocument()
    def __enter__(self):
        return self.doc
    def __exit__(self, t, v, b):
        from . import io
        io.instance.ed = self.ed
        if self.lock:
            self.doclock.Dispose()

class lisp(object):
    """
    LispFunction装饰器(函数装饰器) 

    lisp(name = None, lock = True) -> lisp

    name: Lisp函数名，默认为py函数名

    lock: 是否加文档锁
    """
    def __init__(self, name = None, lock = True):
        self.name = name
        self.lock = lock
    def __call__(self, args):
        if callable(args):
            if not self.name:
                self.name = args.__name__
            self.func = args
            return self
        else:
            from . import acdoc
            with acdoc(self.lock) as doc:
                from pycad.system import conv
                return conv.ToLispData(self.func(doc, conv.FromLispData(args)))

class command(object):
    """
    Command装饰器(函数装饰器)

    command(name = None, flags = 0, lock = True) -> command

    name: 命令名，默认为py函数名

    flags: 命令模式

    lock: 是否加文档锁
    """
    def __init__(self, name = None, flags = 0, lock = True):
        self.name = name
        self.flags = flags
        self.lock = lock
    def __call__(self, args = None):
        if args:
            if not self.name:
                self.name = args.__name__
            self.func = args
            return self
        else:
            from . import acdoc
            with acdoc(self.lock) as doc:
                self.func(doc)

class panel(object):
    """
    面板装饰器(类装饰器)

    panel(name = None, flags = 0): -> panel

    name: 命令名，默认为py类名

    flags: 命令模式
    """
    def __init__(self, name = None, flags = 0):
        from pycad.system import guid
        self.name = name
        self.flags = flags
    def __call__(self, cls = None):
        if cls:
            self.cls = cls
            if not self.name:
                self.name = cls.__name__
            from pycad.system import acws
            self._checkattr('dock', acws.DockSides.None)
            self._checkattr('dockenable', acws.DockSides.None | acws.DockSides.Left | acws.DockSides.Right | acws.DockSides.Top | acws.DockSides.Bottom)
            self._checkattr('text', self.cls.__name__)
            self._checkattr('style', acws.PaletteSetStyles.NameEditable | acws.PaletteSetStyles.ShowCloseButton | acws.PaletteSetStyles.Notify)
            self._checkattr('size', (320, 320))
            self.obj = None
            self.ps = None
            return self
        else:
            import clr
            clr.AddReference('System.Drawing')
            from System.Drawing import Size
            with acdoc() as doc:
                if not self.obj:
                    self.tabs = {
                        key: value() 
                        for key, value in 
                        self.cls.itemtypes.items()}
                    self.obj = self.cls(doc, self.tabs)
                    from pycad.system import acws, guid
                    self.ps = acws.PaletteSet(self.cls.text, self.name, guid(self.cls.guid))
                    self.ps.Style = self.cls.style
                    self.ps.DockEnabled = self.cls.dockenable
                    self.ps.MinimumSize = Size(*self.cls.size)
                    for key,value in self.tabs.items():
                        self.ps.Add(key, value)
                self.ps.Visible = True
                self.ps.Size = Size(*self.cls.size)
                self.ps.Dock = self.cls.dock
                if hasattr(self.cls, "__docked__"):
                    self.obj.__docked__(doc)
    def _checkattr(self, name, value):
        if not hasattr(self.cls, name):
            setattr(self.cls, name, value)

def showtime(func):
    from functools import wraps
    @wraps(func)
    def _func(*args, **kwargs):
        from datetime import datetime
        oldtime = datetime.now()
        res = func(*args, **kwargs)
        t = datetime.now() - oldtime
        print("函数名称:%s.%s" % (func.__module__, func.__name__))
        print("花费时间:%f秒" % t.total_seconds())
        return res
    return _func
