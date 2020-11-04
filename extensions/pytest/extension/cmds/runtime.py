from pycad.system import *
from pycad.runtime import *


@command()
def cstest(doc):
    with cs.opencprofile() as cpf:
        tpaths = cpf.Variables['TRUSTEDPATHS']
        s = 'c:\\nfox'
        patt = '(^|;)%s(;|$)' % s
        import re
        m = re.search(patt, tpaths, re.IGNORECASE)
        if not m:
            print(';'.join((tpaths, s)))


@command(lock=False)
def switchtotest(doc):
    ed = doc.Editor  #type: aced.Editor
    if doc.Database.TileMode: ed.SwitchToPaperSpace()
    else: ed.SwitchToModelSpace()


@command()
def cmdtest(doc):
    ed = doc.Editor  #type: aced.Editor
    from random import uniform
    ed.Command(
        '._line',
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        '')
    ed.Command(
        '._line',
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        '')
    print('\nOK!')


@command()
def dbxtest(doc):
    filename = 'd:\\test.dwg'
    with dbtrans(filename) as tr:
        btr = tr.openmodelspace()
        mat = acge.Matrix3d.Displacement(acge.Vector3d(10,0,0))
        for i in btr:
            ent = tr.getobject(i)  #type: acdb.Entity
            with upopen(ent):
                case = switch(ent)
                if case[acdb.Line]:
                    ent.LayerId = tr.LayerTable['1']
                elif case[acdb.DBText]:
                    ent.TransformBy(mat)
        tr.Database.SaveAs(filename, acdb.DwgVersion.Current)


class clstest:
    @vcm.default
    def func(self):
        print("default", -1)

    @vcm.apply("acad")
    def func(self):
        print("acad", -1)

    @vcm.apply("acad", 20.1)
    def func(self):
        print("acad", 2016)

    @vcm.apply("gcad")
    def func(self):
        print("gcad", -1)


def pickfirst_changed(sender, e):
    #事件的触发者即当前文档
    ed = sender.Editor  #type: aced.Editor
    #获取PickFirst选择集
    res = ed.SelectImplied()
    if res.Status == aced.PromptStatus.OK:
        ed.WriteMessage(str(res.Value.Count))
    else:
        ed.WriteMessage("0")


def doc_created(sender, e):
    #新文档创建后,绑定ImpliedSelectionChanged事件
    e.Document.ImpliedSelectionChanged += pickfirst_changed


@command()
def showpickfirstinfo(doc):
    #获取文档集合
    docs = acap.Application.DocumentManager
    #绑定DocumentCreated事件
    docs.DocumentCreated += doc_created
    for d in docs:
        #遍历已有文档,绑定ImpliedSelectionChanged事件
        d.ImpliedSelectionChanged += pickfirst_changed


@command()
def unshowpickfirstinfo(doc):
    docs = acap.Application.DocumentManager
    docs.DocumentCreated -= doc_created
    for d in docs:
        d.ImpliedSelectionChanged -= pickfirst_changed


@invokeArx.lib("acdb@")
@invokeArx.pointer32("?acdbGetAdsName@@YA?AW4ErrorStatus@Acad@@AAY01JVAcDbObjectId@@@Z")
@invokeArx.pointer64("?acdbGetAdsName@@YA?AW4ErrorStatus@Acad@@AEAY01_JVAcDbObjectId@@@Z")
def GetAdsName(*args): pass


@invokeArx.lib("accore")
@invokeArx.pointer("acdbEntGetX")
def EntGetX(*arg): pass


from ctypes import Structure, c_longlong, byref
class adsname(Structure):
    _fields_ = [
        ("name1", c_longlong),
        ("name2", c_longlong)]


@command()
def runarx(doc):
    res = edx.entsel("请选择图元")
    if not res.ok(): return
    name = adsname()
    GetAdsName(byref(name), res.ObjectId)
    rb = acdb.ResultBuffer((acdb.TypedValue(int(acrx.LispDataType.Text), "*"),))
    ip = EntGetX(name, rb.UnmanagedObject)
    from System import IntPtr
    rb = acdb.ResultBuffer.Create(IntPtr(ip), True)
    print(rb)


@command(flags=acrx.CommandFlags.Session)
def runlisp(doc):
    print(invokeArx.lisp("+", 1, 2))


@command()
def zoomtest(doc):
    acapp.AcadApplication.ZoomExtents()
