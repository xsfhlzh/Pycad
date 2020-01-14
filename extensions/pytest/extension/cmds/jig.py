from pycad.system import *
from pycad.runtime import *


@command()
def testblockjig(doc):
    with dbtrans(doc) as tr:
        bdefid = tr.addblock("*u", acdb.Line(acge.Point3d.Origin, acge.Point3d(10,10,0)))
        bref = acdb.BlockReference(acge.Point3d.Origin, bdefid)
        btr = tr.opencurrspace()
        tr.addentity(btr, bref)
        tr.dragblock(bref)


@command()
def testcirjig(doc):
    jig = cirjig(doc)
    if jig.move() and jig.scale():
        with dbtrans(doc) as tr:
            btr = tr.opencurrspace()
            tr.addentity(btr, jig.Entity)


class cirjig(aced.EntityJig):
    def __new__(cls, *args):
        return aced.EntityJig.__new__(cls, acdb.Circle(acge.Point3d.Origin, acge.Vector3d.ZAxis, 10))

    def __init__(self, doc):
        self.center, self.radius = self.Entity.Center, self.Entity.Radius
        self.ed = doc.Editor

    def move(self):
        self.it = 0
        res = self.ed.Drag(self)
        return res.Status == aced.PromptStatus.OK

    def scale(self):
        self.it = 1
        res = self.ed.Drag(self)
        return res.Status == aced.PromptStatus.OK

    def Sampler(self, prompts):
        if self.it == 0:
            opts = aced.JigPromptPointOptions('\n请输入圆心:')
            opts.UserInputControls = (
                aced.UserInputControls.Accept3dCoordinates |
                aced.UserInputControls.NoZeroResponseAccepted |
                aced.UserInputControls.NoNegativeResponseAccepted |
                aced.UserInputControls.NullResponseAccepted)
            res = prompts.AcquirePoint(opts)
            if res.Status == aced.PromptStatus.OK:
                if self.center == res.Value:
                    return aced.SamplerStatus.NoChange
                else:
                    self.center = res.Value
                    return aced.SamplerStatus.OK
            return aced.SamplerStatus.Cancel
        elif self.it == 1:
            opts = aced.JigPromptDistanceOptions('\n请输入半径:')
            opts.UserInputControls = (
                aced.UserInputControls.Accept3dCoordinates |
                aced.UserInputControls.NoZeroResponseAccepted |
                aced.UserInputControls.NoNegativeResponseAccepted |
                aced.UserInputControls.NullResponseAccepted)
            opts.UseBasePoint = True
            opts.BasePoint = self.center
            opts.Cursor = aced.CursorType.RubberBand
            res = prompts.AcquireDistance(opts)
            if res.Status == aced.PromptStatus.OK:
                if self.radius == res.Value:
                    return aced.SamplerStatus.NoChange
                else:
                    self.radius = res.Value
                    return aced.SamplerStatus.OK
            return aced.SamplerStatus.Cancel
        else:
            return aced.SamplerStatus.Cancel

    def Update(self):
        self.Entity.Center, self.Entity.Radius = self.center, self.radius
