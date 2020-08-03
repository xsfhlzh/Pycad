from pycad.system import *

class upopen(object):
    """
    提升acdb.DBObject对象的打开权限(上下文管理器)

    with upopen(obj): dosomething()
    """
    def __init__(self, obj):
        self._obj = obj
        self._isnotify = obj.IsNotifyEnabled
        self._isread = not obj.IsWriteEnabled
        if self._isnotify:
            self._obj.UpgradeFromNotify()
        elif self._isread:
            self._obj.UpgradeOpen()

    def __enter__(self):
        return self

    def __exit__(self, t, v, b):
        if b is None:
            if self._isnotify:
                self._obj.DowngradeToNotify()
            elif self._isread:
                self._obj.DowngradeOpen()

class cs(object):
    """
    读取注册表配置

    with cs.opencprofile() as cpf:

    tpaths = cpf.Variables['TRUSTEDPATHS']
    """
    _ucm = acapp.UserConfigurationManager
    @classmethod
    def opencprofile(cls):
        """
        读取当前配置的数据
        """
        return cs(cls._ucm.OpenCurrentProfile())
    @classmethod
    def openglobal(cls):
        """
        读取公共配置的数据
        """
        return cs(cls._ucm.OpenGlobalSection())
    @classmethod
    def opendialog(cls, dialog):
        """
        读取对话框配置的数据
        """
        return cs(cls._ucm.OpenDialogSection(dialog))

    def __init__(self, csobj):
        self._cs = csobj
        self.sections = {}
    def __enter__(self):
        return self
    def __exit__(self, t, v, b):
        if b is None: self._close()
    def _close(self):
        for s in self.sections.values():
            s._close()
        self._cs.Close()
        self._cs.Dispose()
    def __getattr__(self, name):
        if self._cs.ContainsSubsection(name):
            if not self.sections.has_key(name):
                self.sections[name] = cs(self._cs.OpenSubsection(name))
            return self.sections[name]
    def __getitem__(self, key):
        if self._cs.Contains(key):
            return self._cs.ReadProperty(key, '')
    def __setitem__(self, key, value):
        if self._cs.Contains(key):
            self._cs.WriteProperty(key, value)

class dbdict(object):
    """
    字典封装类
    """
    def __init__(self, d, tr, parent = None, hasother = False):
        self._tr, self._parent, self._hasother = tr, parent, hasother
        self._dict = None
        self._name = None
        if not hasother:
            if isinstance(d, str):
                self._name = d
            elif isinstance(d, (acdb.ObjectId, acdb.DBObject)):
                self._dict = self._tr.getrealobject(d)
                if not isinstance(self._dict, acdb.DBDictionary):
                    self._hasother = True
    def __setitem__(self, key, value):
        if self._hasother:
            return
        elif self._name:
            self._createdict()
        with upopen(self._dict):
            self._dict.SetAt(key, value)
            self._tr.Trans.AddNewlyCreatedDBObject(value, True)
    def __getitem__(self, key):
        if self._dict and self._dict.Contains(key):
            return self._tr.getobject(self._dict.GetAt(key))
    def __delitem__(self, key):
        if self._dict and self._dict.Contains(key):
            self._dict.Remove(key)
    def _createdict(self):
        if self._parent._name:
            self._parent._createdict()
        with upopen(self._parent._dict):
            self._dict = acdb.DBDictionary()
            self._dict.TreatElementsAsHard = True
            self._parent._dict.SetAt(self._name, self._dict)
            self._tr.Trans.AddNewlyCreatedDBObject(self._dict, True)
            self._name = None
    def getchild(self, key):
        """
        获取子字典
        """
        if self._hasother:
            return self
        if self._name:
            return dbdict(key, self._tr, self)
        elif self._dict.Contains(key):
            return dbdict(self[key], self._tr, self)
        else:
            return dbdict(key, self._tr, self)
    def setxrecord(self, key, value):
        """
        将数据集转换为扩展数据,存入字典

        setxrecord(key, [[1000, "mydata"]])
        """
        if not self._hasother:
            xr = acdb.Xrecord()
            xr.Data = conv.ToBuffer(value)
            self[key] = xr
    def getxrecord(self, key):
        """
        从字典中获取扩展数据,并转换为数据集
        """
        xr = self[key]
        if xr: return conv.ToList(xr.Data)

class serializable(object):
    types = (str, int, float, bool)
    class property(object):
        def __init__(self, objtype):
            self.type = objtype
            self.fget = self.fset = None
        def __call__(self, fget):
            self.fget = fget
            self.__doc__ = fget.__doc__
            return self
        def setter(self, fset):
            self.fset = fset
            return self
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError
            return self.fget(obj)
        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("can't set")
            self.fset(obj, value)

    def serialize(self):
        t = type(self)
        d = {}
        for k,v in t.__dict__.items():
            if isinstance(v, serializable.property):
                s = getattr(self, k)
                if v.type in serializable.types:
                    d[k] = s
                elif serializable in v.type.mro():
                    d[k] = s.serialize()
                else:
                    raise TypeError
        return d

    @classmethod
    def deserialize(cls, objdict):
        obj = cls()
        for k,v in objdict.items():
            s = cls.__dict__[k]
            if isinstance(s, serializable.property):
                t = s.type
                if t in serializable.types:
                    setattr(obj, k, t(v))
                elif isinstance(v, dict):
                    setattr(obj, k, t.deserialize(v))
                else:
                    raise TypeError
        return obj
    
    def dumps(self, stype = 'json'):
        stype = stype.lower()
        if stype == 'json':
            import json
            return json.dumps(self.serialize())
    
    @classmethod
    def loads(cls, s, stype = 'json'):
        if stype.lower() == 'json':
            import json
            return cls.deserialize(json.loads(s))

    @staticmethod
    def Type(objtype):
        return serializable.property(objtype)

    @staticmethod
    def Str(fget):
        return serializable.property(str)(fget)

    @staticmethod
    def Int(fget):
        return serializable.property(int)(fget)
    
    @staticmethod
    def Float(fget):
        return serializable.property(float)(fget)

    @staticmethod
    def Bool(fget):
        return serializable.property(bool)(fget)


class invokeArx(object):

    _dlls = []
    _funcs = {}
    from ctypes import cdll as _cdll

    @classmethod
    def load(cls, name):
        name = name.lower()
        if not cls._dlls.__contains__(name):
            cls._dlls.append(name)
            cls._cdll.LoadLibrary(name)
        return cls._cdll[name]

    @classmethod
    def lib(cls, name):
        return cls._arxfuncbody(name)

    @classmethod
    def apply32(cls, entry, ver=-1):
        func = cls._arxfuncbody()
        func.apply32(entry, ver)
        return func

    @classmethod
    def apply64(cls, entry, ver=-1):
        func = cls._arxfuncbody()
        func.apply64(entry, ver)
        return func

    class _arxfuncbody(object):

        def __init__(self, name=None):
            self.dll = name
            self.dict32, self.dict64 = {}, {}

        def apply32(self, entry, ver):
            self.dict32[ver] = entry

        def apply64(self, entry, ver):
            self.dict64[ver] = entry

        def __call__(self, body):
            self.__name__ = body.__name__
            if isinstance(body, invokeArx._arxfuncbody):
                self.dict32.update(body.dict32)
                self.dict64.update(body.dict64)
                entry = None
            else:
                entry = self.__name__
            if self.dll:
                if not entry:
                    curr_version = float('%s.%s' % (acapp.Version.Major, acapp.Version.Minor))
                    from platform import architecture
                    d = self.dict64 if architecture()[0] == "64bit" else self.dict32
                    for key in sorted(d):
                        if curr_version >= key: ver = key
                        else: break
                    if ver:
                        entry = d[ver]
                if entry:
                    if self.dll == "acad":
                        dll = invokeArx.load("acad.exe")
                    elif self.dll == "accore":
                        dll = invokeArx.load("accore.dll")
                        if not dll:
                            dll = invokeArx.load("acad.exe")
                    elif self.dll == "acdb@":
                        dll = invokeArx.load("acdb%s.dll" % acapp.Version.Major)
                    else:
                        dll = invokeArx.load(self.dll)
                    return dll[entry]
            else:
                return self

    _lispfuncs = []

    @classmethod
    def lisp(cls, *args):
        accore = cls.load("accore.dll")
        if not cls._lispfuncs.__contains__(args[0]):
            cls._lispfuncs.append(args[0])
            accore.ads_queueexpr("(vl-acad-defun '%s)\n" % args[0])
        d = acdb.ResultBuffer(tuple(conv.ToTypedValue(x) for x in args))
        from ctypes import c_long, byref
        ip = c_long()
        res = accore.acedInvoke(d.UnmanagedObject, byref(ip))
        if res != -5001:
            from System import IntPtr
            return acdb.ResultBuffer.Create(IntPtr(ip.value), True)