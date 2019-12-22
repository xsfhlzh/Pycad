from pycad.system import *
from pycad.runtime import *
#加载linq扩展函数
import clr, System
clr.ImportExtensions(System.Linq)

@command(flags=acrx.CommandFlags.UsePickSet)
def linqtest(doc):
    #linq去重,留下同心圆中直径最小的
    #选择圆
    ss = edx.ssget(filters=(0, "circle"))
    if not ss.ok(): return
    with dbtrans(doc) as tr:
        #流程:按圆心分组->每组排序后->跳过第一个元素
        cirs = \
            ss.Cast[acdb.ObjectId]()\
            .Select(lambda i: tr.getobject(i))\
            .GroupBy(lambda c: c.Center)\
            .SelectMany(lambda cs: cs.OrderBy(lambda c: c.Radius).Skip(1))
        tr.erase(*cirs)

@command()
def linqtest2(doc):
    #选择圆
    ss = edx.ssget(
        filters=(0, 'circle'), 
        messages=("\n请选择圆", ""), 
        keywords=("fIist", "Second"))
    if ss.ok():
        with dbtrans(doc) as tr:
            #按圆心的X坐标排序
            cirs = \
                ss.Cast[acdb.ObjectId]()\
                .Select(lambda i: tr.getobject(i))\
                .OrderBy(lambda c: c.Center.X)
            for cir in cirs:
                print(cir.Center)
    elif ss.keyword("fIist"):
        print("first!")
    elif ss.keyword("Second"):
        print("second!")
    