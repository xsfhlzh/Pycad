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

@command()
def xhqtest(doc):
    res1 = edx.getint("\n请输入序号:")
    if not res1.ok(): return
    res2 = edx.getpoint("\n请输入起点:")
    if not res2.ok(): return
    jig = XhqJig(res2.value, str(res1.value))
    res = doc.Editor.Drag(jig)
    if res.Status == aced.PromptStatus.OK:
        with dbtrans(doc) as tr:
            btr = tr.opencurrspace()
            tr.addentity(btr, *jig.GetEntities())

class XhqJig(aced.DrawJig):

    def __init__(self, basept, no):
        self.text = acdb.MText()
        self.text.Attachment = acdb.AttachmentPoint.MiddleCenter
        self.text.TextHeight = 5
        self.text.Contents = no
        self.line = acdb.Line(basept, basept)
        self.circle = acdb.Circle()
        self.circle.Radius = 10
        self.location = self.text.Location = self.circle.Center = basept

    def Sampler(self, prompts):
        opts = aced.JigPromptPointOptions('\n请输入终点:')
        opts.UserInputControls = (
            aced.UserInputControls.Accept3dCoordinates |
            aced.UserInputControls.NoZeroResponseAccepted |
            aced.UserInputControls.NoNegativeResponseAccepted)
        res = prompts.AcquirePoint(opts)
        if res.Value != self.location:
            self.location = res.Value
        else:
            return aced.SamplerStatus.NoChange
        if res.Status == aced.PromptStatus.Cancel:
            return aced.SamplerStatus.Cancel
        else:
            return aced.SamplerStatus.OK

    def WorldDraw(self, draw):
        try:
            for ent in self.GetEntities():
                draw.Geometry.Draw(ent)
        except:
            return False
        return True

    def Update(self):
        self.text.Location = self.circle.Center = self.location
        vec = self.location - self.line.StartPoint
        if vec.Length <= self.circle.Radius:
            self.line.EndPoint = self.line.StartPoint
        else:
            vec = vec.GetNormal() * self.circle.Radius
            self.line.EndPoint = self.location - vec

    def GetEntities(self):
        self.Update()
        return self.line, self.circle, self.text
