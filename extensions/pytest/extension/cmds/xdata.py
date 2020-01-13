from pycad.system import *
from pycad.runtime import *

@command()
def myxdata(doc):
    with dbtrans(doc) as tr:
        #新建一个匿名块,并放入一条直线
        ents = (acdb.Line(acge.Point3d(), acge.Point3d(10,10,0)),)
        bdefid = tr.addblock('*u', *ents)
        btr = tr.opencurrspace()
        #新建块引用
        bref = acdb.BlockReference(acge.Point3d(), bdefid)
        tr.addentity(btr, bref)
        #添加Xdata
        tr.addregapp('MyXdata')
        bref.XData = conv.ToBuffer(((1001, 'MyXdata'), (1000, 'test')))
        
@command()
def myxdata2(doc):
    #按Xdata程序名过滤图元
    ss = edx.ssget_x(filters=(1001, 'MyXdata'))
    print(len(ss))

class mydata(serializable):

    class myinfo(serializable):
        def __init__(self, name=''):
            self._name = name
            self._sex = True

        @serializable.Str
        def Name(self): return self._name
        @Name.setter
        def Name(self, value): self._name = value

        @serializable.Bool
        def Sex(self): return self._sex
        @Sex.setter
        def Sex(self, value): self._sex = value

    def __init__(self, name='', info=None):
        self._name = name
        self._info = info

    @serializable.Str
    def Name(self): return self._name
    @Name.setter
    def Name(self, value): self._name = value

    @serializable.Type(myinfo)
    def Info(self): return self._info
    @Info.setter
    def Info(self, value): self._info = value

@command()
def deserializetest(doc):
    #序列化和反序列化
    data = mydata.loads('{ "Name": "xsfh", "Info": { "Name": "man", "Sex": true } }')
    d = data.serialize()
    print(d)
    data2 = mydata.deserialize(d)
    print(data2.serialize())
    print(data2.dumps())