from pycad.system import *
from pycad.runtime import *
import typing

@command()
def ccitest(doc):
    #新建两个ge库的直线段
    line1 = acge.LineSegment3d(acge.Point3d.Origin, acge.Vector3d.YAxis * 10)
    line2 = acge.LineSegment3d(acge.Point3d.Origin, acge.Vector3d.YAxis * 20)
    #用cci类判断重合
    cci = acge.CurveCurveIntersector3d(line1, line2, acge.Vector3d.ZAxis)
    for r in range(cci.OverlapCount()):
        overloads = cci.GetOverlapRanges(r) 
        #显示重合信息,即重合部分的曲线参数范围
        print("%s, %s" % (overloads[0].LowerBound, overloads[0].UpperBound))
        print("%s, %s" % (overloads[1].LowerBound, overloads[1].UpperBound))

@command()
def ccitest2(doc):
    #获取曲线自交点
    #获取曲线
    opts = aced.PromptEntityOptions('\n请选择曲线:')
    opts.SetRejectMessage('错误类型!')
    opts.AddAllowedClass(acdb.Curve, False)
    res = edx.entsel(opts)
    if not res.ok(): return
    with dbtrans(doc) as tr:
        pl = tr.getobject(res.ObjectId)  #type: acdb.Curve
        curve3d = pl.GetGeCurve()
        #用cci类判断自相交
        cci = acge.CurveCurveIntersector3d(curve3d, curve3d, acge.Vector3d.ZAxis)
        for k in range(cci.NumberOfIntersectionPoints):
            #显示自相交点
            pars = cci.GetIntersectionParameters(k)
            print(curve3d.EvaluatePoint(pars[0]))

@command()
def mindict(doc):
    #两曲线间最短距离
    #获取曲线
    opts = aced.PromptEntityOptions('\n请选择曲线:')
    opts.SetRejectMessage('错误类型!')
    opts.AddAllowedClass(acdb.Curve, False)
    res = edx.entsel(opts)
    if not res.ok(): return
    res2 = edx.entsel(opts)
    if not res2.ok(): return
    with dbtrans(doc) as tr:
        curves = (tr.getobject(res.ObjectId).GetGeCurve(), tr.getobject(res2.ObjectId).GetGeCurve())
        pocs = curves[0].GetClosestPointTo(curves[1])
        line = acdb.Line(pocs[0].Point, pocs[1].Point)
        tr.addentity(tr.opencurrspace(), line)

@command()
def comptest(doc):
    #曲线任意连, 创意来自大胃王
    #获取两条曲线, 可以是首尾连接的, 或者重合一部分(只能是直线)
    opts = aced.PromptEntityOptions('\n请选择曲线:')
    opts.SetRejectMessage('错误类型!')
    opts.AddAllowedClass(acdb.Curve, False)
    res = edx.entsel(opts)
    if not res.ok(): return
    res2 = edx.entsel(opts)
    if not res2.ok(): return
    with dbtrans(doc) as tr:
        #转换为ge曲线
        curves = [tr.getobject(res.ObjectId).GetGeCurve(), tr.getobject(res2.ObjectId).GetGeCurve()]
        cci = acge.CurveCurveIntersector3d(curves[0], curves[1], acge.Vector3d.ZAxis)
        if cci.NumberOfIntersectionPoints == 1 and cci.OverlapCount() == 0:
            #保证两个曲线的方向是连续的
            ends = tuple(gex.get_endpoints(c) for c in curves)
            if ends[0][0] == ends[1][0]:
                curves[0] = curves[0].GetReverseParameterCurve()
            elif ends[0][0] == ends[1][1]:
                curves = curves[::-1]
            elif ends[0][1] == ends[1][1]:
                curves[1] = curves[1].GetReverseParameterCurve()
            elif ends[0][1] != ends[1][0]:
                return
        else: return
        newcurve3d = acge.CompositeCurve3d(tuple(curves))
        tr.addentity(tr.opencurrspace(), gex.conv_to_db(newcurve3d))

def get_intersection_params(cci):
    return [
        cci.GetIntersectionParameters(i) 
        for i in range(cci.NumberOfIntersectionPoints)]

def get_overload_ranges(cci):
    for i in range(cci.OverlapCount()):
        overloads = cci.GetOverlapRanges(i)
        for j in range(2):
            yield (overloads[j].LowerBound, overloads[j].UpperBound)

@command()
def linetest(doc):
    #获取两条直线
    res = edx.entsel("\n请选择第一条直线:")
    if not res.ok(): return
    res2 = edx.entsel("\n请选择第二条直线:")
    if not res2.ok(): return
    with dbtrans(doc) as tr:
        line1 = tr.getobject(res.ObjectId) #type: acdb.Line
        line2 = tr.getobject(res2.ObjectId) #type: acdb.Line
        #用向量判断是否平行
        print(line1.Delta.IsParallelTo(line2.Delta))

