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
        pl = tr.getobject(res[0])  #type: acdb.Curve
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
    res0 = edx.entsel(opts)
    if not res0.ok(): return
    res1 = edx.entsel(opts)
    if not res1.ok(): return
    with dbtrans(doc) as tr:
        curves = (tr.getobject(res0[0]).GetGeCurve(), tr.getobject(res1[0]).GetGeCurve())
        pocs = curves[0].GetClosestPointTo(curves[1]) #type: typing.List[acge.PointOnCurve3d]
        line = acdb.Line(pocs[0].Point, pocs[1].Point)
        tr.addentity(tr.opencurrspace(), line)

@command()
def comptest(doc):
    #曲线任意连, 创意来自大胃王
    #获取两条曲线, 可以是首尾连接的, 或者重合一部分(只能是直线)
    opts = aced.PromptEntityOptions('\n请选择曲线:')
    opts.SetRejectMessage('错误类型!')
    opts.AddAllowedClass(acdb.Curve, False)
    res0 = edx.entsel(opts)
    if not res0.ok(): return
    res1 = edx.entsel(opts)
    if not res1.ok(): return
    with dbtrans(doc) as tr:
        #转换为ge曲线
        curves = [tr.getobject(res0[0]).GetGeCurve(), tr.getobject(res1[0]).GetGeCurve()]
        cci = acge.CurveCurveIntersector3d(curves[0], curves[1], acge.Vector3d.ZAxis)
        if cci.NumberOfIntersectionPoints == 1 and cci.OverlapCount() == 0:
            #保证两个曲线的方向是连续的
            ends = tuple(get_endpoints(c) for c in curves)
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
        curves = newcurve3d.GetCurves()
        hasnurb = False
        for c in curves:
            if isinstance(c, (acge.EllipticalArc3d, acge.NurbCurve3d)):
                hasnurb = True
                break
        if hasnurb:
            #如果包含样条曲线, 转换为样条曲线连接
            newcurve3d = conv_to_nurb(curves[0])
            for i in range(1, curves.Length):
                newcurve3d.JoinWith(conv_to_nurb(curves[i]))
            curve = acdb.Spline()
        else:
            #否则使用多义线连接为一个整体
            curve = acdb.Polyline()
        curve.SetFromGeCurve(newcurve3d)
        tr.addentity(tr.opencurrspace(), curve)

def get_endpoints(curve3d):
    #ge库2016似乎有bug, 样条曲线直接取的终点是错误的
    inte = curve3d.GetInterval()
    return (
        curve3d.HasStartPoint and curve3d.EvaluatePoint(inte.LowerBound) or None,
        curve3d.HasEndPoint and curve3d.EvaluatePoint(inte.UpperBound) or None)

def conv_to_nurb(curve3d):
    #转换ge曲线为B样条, 支持直线/圆(弧)/椭圆(弧)/多段线
    case = switch(curve3d)
    if case[acge.NurbCurve3d]:
        return curve3d
    elif case[acge.LineSegment3d, acge.EllipticalArc3d]:
        return acge.NurbCurve3d(curve3d)
    elif case[acge.CircularArc3d]:
        return acge.NurbCurve3d(
            acge.EllipticalArc3d(
                curve3d.Center,
                curve3d.ReferenceVector,
                curve3d.Normal.CrossProduct(curve3d.ReferenceVector),
                curve3d.Radius,
                curve3d.Radius,
                curve3d.StartAngle,
                curve3d.EndAngle))
    elif case[acge.PolylineCurve3d]:
        acge.NurbCurve3d(3, curve3d, False)

def get_interval_params(curve3d1, curve3d2, normal = acge.Vector3d.ZAxis):
    cci = acge.CurveCurveIntersector3d(curve3d1, curve3d2, normal)
    pars1, pars2 = set(), set()
    for k in range(cci.NumberOfIntersectionPoints):
        pars = cci.GetIntersectionParameters(k)
        pars1.add(pars[0])
        pars2.add(pars[1])
    for r in range(cci.OverlapCount()):
        overloads = cci.GetOverlapRanges(r)
        pars1.add(overloads[0].LowerBound)
        pars1.add(overloads[0].UpperBound)
        pars2.add(overloads[1].LowerBound)
        pars2.add(overloads[1].UpperBound)
    return (pars1, pars2)

@command()
def linetest(doc):
    #获取两条直线
    res = edx.entsel("\n请选择第一条直线:")
    if not res.ok(): return
    res2 = edx.entsel("\n请选择第二条直线:")
    if not res2.ok(): return
    with dbtrans(doc) as tr:
        line1 = tr.getobject(res[0]) #type: acdb.Line
        line2 = tr.getobject(res2[0]) #type: acdb.Line
        #用向量判断是否平行
        print(line1.Delta.IsParallelTo(line2.Delta))