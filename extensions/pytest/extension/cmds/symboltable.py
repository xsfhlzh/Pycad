from pycad.system import *
from pycad.runtime import *


@command()
def dicttest(doc):
    with dbtrans(doc) as tr:
        #获取根字典
        d = tr.getdict()
        d.setxrecord('NFox.Cad', [[1000, 'abc']])
        print('\n在命名字典中设置了值为%s的扩展数据' % d.getxrecord('NFox.Cad'))


@command()
def dicttest2(doc):
    res = edx.getpoint('\n输入一个点')
    if not res.ok(): return
    with dbtrans(doc) as tr:
        btr = tr.opencurrspace()
        cir = acdb.Circle(res.value, acge.Vector3d.ZAxis, 2)
        tr.addentity(btr, cir)
        #获取对象字典下的多级子字典
        d = tr.getdict(cir, "name1", "name2")
        d.setxrecord('test1', [[1000, 'abc']])
        print('\n在对象字典中设置了值为%s的扩展数据' % d.getxrecord('test1'))
        #获取根字典下的多级子字典
        d = tr.getdict('NFox.Cad', "name1", "name2")
        d.setxrecord('test1', [[1000, 'abc']])
        print('\n在字典中设置了值为%s的扩展数据' % d.getxrecord('test1'))


@command()
def dicttest3(doc):
    res = edx.entsel('\n选择一个圆')
    if not res.ok(): return
    with dbtrans(doc) as tr:
        cir = tr.getobject(res.ObjectId)
        #获取对象字典
        d = tr.getdict(cir)
        d.setxrecord('NFox.Cad', [[1000, 'abc']])
        print('\n在对象字典中设置了值为%s的扩展数据' % d.getxrecord('NFox.Cad'))


@command()
def layertest(doc):
    with dbtrans(doc) as tr:
        #新建图层
        tr.addlayer('1')
