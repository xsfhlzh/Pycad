from pycad.system import *
from pycad.runtime import *

@command()
def myss1(doc):
    #获取两个角点
    respt = edx.getpoint("选择起点")
    if not respt.ok(): return
    rescor = edx.getcorner("选择终点", respt)
    if not rescor.ok(): return
    #将穿过矩形窗口的直线选中
    ss = edx.ssget_w(respt.value, rescor.value, ((0, 'line'), (8, '0')))
    if ss.ok(): edx.sssetfirst(tuple(ss))

@command()
def myss2(doc):
    with dbtrans(doc) as tr:
        #选中当前空间内的所有直线
        ids = tuple(
            i for i in tr.opencurrspace()
            if i.ObjectClass.DxfName == 'LINE')
        edx.sssetfirst(ids)

@command(flags=acrx.CommandFlags.UsePickSet)
def comtest(doc):
    #com方式获取图元图像
    ss = edx.ssget()
    if not ss.ok(): return
    acdoc = acapp.AcadApplication.ActiveDocument
    try: acdoc.SelectionSets['CURRENT'].Delete()
    except: pass
    acdoc.Export('d:\\1', 'wmf', acdoc.ActiveSelectionSet)

