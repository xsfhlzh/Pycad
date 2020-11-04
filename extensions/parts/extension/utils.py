__all__ = [
    'RegAppName', 'GetPart', 'GetSubEntitys', 'SetData',
    'AcadEntityProvider']

from pycad.system import *

from NFox.Expression.DataSystem import *
from NFox.Expression.Runtime import *
from NFox.Geometry import *

RegAppName = 'NFox.Cad.Part'


def GetPart(bref):
    rb = bref.GetXDataForApplication(RegAppName)
    if rb:
        rlst = conv.ToList(rb)
        if len(rlst) >= 3:
            index = SymbolIndex(rlst[1][1], rlst[2][1])
            ipart = Application.WorkingDatabase.ImagePartTable[index]
            if ipart:
                ipart = ipart.Copy()
                if ipart.IsParameterized:
                    ipart.Eval(tuple(d[1] for d in rlst[3:]))
                return ipart


def GetSubEntitys(bref):
    part = GetPart(bref)
    if part:
        ents = tuple(part.Image.Cast[acdb.Entity]())
        for e in ents:
            e.TransformBy(bref.BlockTransform)
        return ents


def SetData(bref, part, pars):
    rlst = [
        [1001, RegAppName],
        [1000, part.Index.DictionaryName],
        [1000, part.Index.Key]]
    if part.HasParams and part.HasData:
        if not pars: pars = part.DefaultParams
        for p in pars:
            rlst.append([1000, p])
    bref.XData = conv.ToBuffer(rlst)


class AcadEntityProvider(IEntityProvider):

    def ToPoint2D(self, pt):
        return Point2D(pt[0], pt[1]).Round()

    def ToPoint2d(self, pt):
        return acge.Point2d(pt[0], pt[1])

    def ToPoint3d(self, pt):
        return acge.Point3d(pt[0], pt[1], 0)

    def ToVector2D(self, pt):
        return Vector2D(pt[0], pt[1]).Round()

    def ToVector2d(self, pt):
        return acge.Vector2d(pt[0], pt[1])

    def ToVector3d(self, pt):
        return acge.Vector3d(pt[0], pt[1], 0)

    def FromObjet(self, obj):
        case = switch(obj)
        if case[acdb.Line]:
            return LineSegment2D(self.ToPoint2D(obj.StartPoint), self.ToPoint2D(obj.EndPoint))
        elif case[acdb.Circle]:
            return CircleArc2D(self.ToPoint2D(obj.Center), obj.Radius)
        elif case[acdb.Arc]:
            return CircleArc2D(self.ToPoint2D(obj.Center), obj.Radius, Angle(obj.StartAngle), Angle(obj.EndAngle))
        elif case[acdb.Ellipse]:
            return Ellipse2D(self.ToPoint2D(obj.Center), obj.MajorRadius, obj.MinorRadius, Angle(obj.MajorAxis.AngleOnPlane(obj.GetPlane())), Angle(obj.StartAngle), Angle(obj.EndAngle))
        elif case[acdb.Polyline]:
            pline = PolyLine2D(obj.Closed)
            for i in range(obj.NumberOfVertices):
                pline.Add(self.ToPoint2D(obj.GetPoint2dAt(i)), obj.GetBulgeAt(i), obj.GetStartWidthAt(i), obj.GetEndWidthAt(i))
            return pline
        elif case[acdb.Spline]:
            from System import Double
            from System.Collections.Generic import List
            spline = Spline2D(obj.Closed, obj.NurbsData.Periodic, List[Point2D]((self.ToPoint2D(pt) for pt in obj.NurbsData.GetControlPoints())), List[Double](obj.NurbsData.GetKnots()))
            if obj.HasFitData:
                fdata = obj.FitData
                fitPoints = List[Point2D]((self.ToPoint2D(pt) for pt in fdata.GetFitPoints()))
                if fdata.TangentsExist:
                    spline.SetFitData(fitPoints, self.ToVector2D(fdata.StartTangent), self.ToVector2D(fdata.EndTangent))
                else:
                    spline.SetFitData(fitPoints)
            return spline
        elif case[acdb.DBText]:
            return Text2D(self.GetCenter(obj), obj.TextString, obj.Height)
        elif case[acdb.MText]:
            return Text2D(self.GetCenter(obj), obj.Text, obj.Height)

    def GetCenter(self, ent):
        ext = ent.GeometricExtents
        return ext.MinPoint + (ext.MaxPoint - ext.MinPoint) / 2

    def ToObject(self, entity):
        case = switch(entity)
        if case[LineSegment2D]:
            return acdb.Line(self.ToPoint3d(entity.StartPoint), self.ToPoint3d(entity.EndPoint))
        elif case[CircleArc2D]:
            if entity.Closed:
                return acdb.Circle(self.ToPoint3d(entity.Center), acge.Vector3d.ZAxis, entity.Radius)
            else:
                normal = acge.Vector3d.ZAxis
                if entity.IsClockWise: normal = -normal
                return acdb.Arc(self.ToPoint3d(entity.Center), normal, entity.Radius, entity.StartAngle, entity.EndAngle)
        elif case[Ellipse2D]:
            normal = acge.Vector3d.ZAxis
            if entity.IsClockWise: normal = -normal
            return acdb.Ellipse(self.ToPoint3d(entity.Center), normal, self.ToVector3d(entity.MajorAxis), entity.Minor / entity.Major, entity.StartAngle, entity.EndAngle)
        elif case[PolyLine2D]:
            pline = acdb.Polyline()
            i = 0
            for bv in entity.Vertexs:
                pline.AddVertexAt(i, self.ToPoint2d(bv.Position), bv.Bulge, bv.StartWidth, bv.EndWidth)
                i += 1
            pline.Closed = entity.Closed
            return pline
        elif case[Spline2D]:
            tol = acge.Tolerance.Global.EqualPoint
            if entity.HasFitPoints:
                pts = acge.Point3dCollection()
                for pt in entity.FitPoints:
                    pts.Add(self.ToPoint3d(pt))
                if entity.TangentsExist:
                    return acdb.Spline(pts, self.ToVector3d(entity.StartTangent), self.ToVector3d(entity.EndTangent), entity.Order, tol)
                else:
                    return acdb.Spline(pts, entity.Order, tol)
            else:
                pts = acge.Point3dCollection()
                for pt in entity.NurbsData.ControlPoints:
                    pts.Add(self.ToPoint3d(pt))
                knots = acge.DoubleCollection()
                for knot in spl.NurbsData.Knots:
                    knots.Add(knot)
                return acdb.Spline(entity.Degree, False, entity.Closed, entity.Periodic, pts, knots, acge.DoubleCollection(), tol, tol)
        elif case[Text2D]:
            txt = acdb.MText()
            txt.Attachment = acdb.AttachmentPoint.MiddleCenter
            txt.Location = self.ToPoint3d(entity.Position)
            txt.Contents = entity.Content
            txt.TextHeight = entity.Height
            return txt
