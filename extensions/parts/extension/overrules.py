from pycad.system import *
from pycad.runtime import *
from extension.utils import *


class PartDrawOverrule(acgi.DrawableOverrule):
    def __init__(self):
        self.SetXDataFilter(RegAppName)

    def WorldDraw(self, drawable, wd):
        from math import pi
        ents = GetSubEntitys(drawable)
        if ents:
            with acdoc(False) as doc:
                with dbtrans(doc) as tr:
                    tstrid = tr.TextStyleTable['Standard']
                    b = drawable.Rotation > pi / 2 and drawable.Rotation <= pi * 3 / 2
                    for e in ents:
                        if isinstance(e, acdb.MText):
                            e.TextStyleId = tstrid
                            if b: e.Rotation -= pi
                        wd.Geometry.Draw(e)
            return True
        return False


class PartTransformOverrule(acdb.TransformOverrule):
    def __init__(self):
        self.SetXDataFilter(RegAppName)

    def Explode(self, entity, entitySet):
        ents = GetSubEntitys(entity)
        if ents:
            for e in ents:
                entitySet.Add(e)


class PartOsnapOverrule(acdb.OsnapOverrule):
    def __init__(self):
        self.SetXDataFilter(RegAppName)

    def GetObjectSnapPoints(self, entity, mode, mark, pick, lastpt, mat, snappts, geids, insmat=None):
        ents = GetSubEntitys(entity)
        if ents:
            for e in ents:
                pts = acge.Point3dCollection()
                e.GetObjectSnapPoints(mode, mark.ToInt32(), pick, lastpt, mat, pts, geids)
                if insmat:
                    for pt in pts: pt.TransformBy(insmat)
                for pt in pts:
                    snappts.Add(pt)


#开启重定义
_r = acrx.RXObject.GetClass(acdb.BlockReference)
acrx.Overrule.AddOverrule(_r, PartDrawOverrule(), False)
acrx.Overrule.AddOverrule(_r, PartTransformOverrule(), False)
acrx.Overrule.AddOverrule(_r, PartOsnapOverrule(), False)

# _r = acrx.RXObject.GetClass(acdb.BlockReference)
# acrx.Overrule.RemoveOverrule(_r, PartDrawOverrule())
# acrx.Overrule.RemoveOverrule(_r, PartTransformOverrule())
# acrx.Overrule.RemoveOverrule(_r, PartOsnapOverrule())
