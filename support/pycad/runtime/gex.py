from pycad.system import switch, acge, acdb

def get_endpoints(curve3d):
    #GE库2016似乎有bug, 样条曲线直接取的终点是错误的
    interval = curve3d.GetInterval()
    return (
        curve3d.HasStartPoint and curve3d.EvaluatePoint(interval.LowerBound) or None,
        curve3d.HasEndPoint and curve3d.EvaluatePoint(interval.UpperBound) or None)

def conv_to_nurb(curve3d):
    #转换GE曲线为B样条, 支持直线/圆(弧)/椭圆(弧)/多段线
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

def conv_to_db(curve3d):
    #转换GE曲线为DB曲线
    case = switch(curve3d)
    if case[acge.LineSegment3d]:
        line = acdb.Line()
        line.SetFromGeCurve(curve3d)
        return line
    elif case[acge.CircularArc3d]:
        if curve3d.IsClosed:
            cir = acdb.Circle()
            cir.SetFromGeCurve(curve3d)
            return cir
        else:
            arc = acdb.Arc()
            arc.SetFromGeCurve(curve3d)
            return arc
    elif case[acge.EllipticalArc3d]:
        ell = acdb.Ellipse()
        ell.SetFromGeCurve(curve3d)
        return ell
    elif case[acge.Ray3d]:
        ray = acdb.Ray()
        ray.SetFromGeCurve(curve3d)
        return ray
    elif case[acge.Line3d]:
        xline = acdb.Xline()
        xline.SetFromGeCurve(curve3d)
        return xline
    elif case[acge.PolylineCurve3d]:
        pl3d = acdb.Polyline3d()
        pl3d.SetFromGeCurve(curve3d)
        return pl3d
    elif case[acge.NurbCurve3d]:
        spl = acdb.Spline()
        spl.SetFromGeCurve(curve3d)
        return spl
    elif case[acge.CompositeCurve3d]:
        curves = curve3d.GetCurves()
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
        return curve