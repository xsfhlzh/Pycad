from pycad.system import *
from pycad.runtime import *
from extension.utils import *

from NFox.Expression.DataSystem import *
from NFox.Expression.Runtime import *
from NFox.Expression.SymbolValues import *
from NFox.Geometry import *

#初始化数据
Application.WorkingDatabase = Database(findfile('parts.odx'))

#初始化实体转换器
Entity2D.EntityProvider = AcadEntityProvider()


def part_defining(sender, e):
    from ctypes import windll
    windll.user32.SetActiveWindow(acap.Application.MainWindow.Handle)
    with acdoc() as doc:
        ed = doc.Editor
        respt = ed.GetPoint('\n指定插入基点')
        if respt.Status == aced.PromptStatus.OK:
            pt = respt.Value
            opts = aced.PromptSelectionOptions()
            opts.MessageForAdding = '\n请选择曲线或文字:'
            resss = ed.GetSelection(opts, conv.ToFilter([[0, 'line,circle,ellipse,arc,lwpolyline,spline,*text']]))
            if resss.Status == aced.PromptStatus.OK:
                from System.Collections.Generic import List
                ents = List[acdb.Entity]()
                with dbtrans(doc) as tr:
                    mat = acge.Matrix3d.Displacement(acge.Point3d.Origin - pt)
                    for i in resss.Value.GetObjectIds():
                        copy = tr.getobject(i).Clone()
                        copy.TransformBy(mat)
                        ents.Add(copy)
                e.Part = ImagePart()
                e.Part.Image = Image2D(ents)


def drag_start(sender, e):
    if e.Part:
        part = e.Part
        import clr
        clr.AddReference('System.Windows.Forms')
        from System.Windows.Forms import DataObject, DragDropEffects
        data = DataObject()
        data.SetData(SymbolIndex, part.Index)
        acapp.DoDragDrop(sender, data, DragDropEffects.Move, PartDropTarget())


class PartDropTarget(acws.DropTarget):
    def OnDrop(self, e):
        from ctypes import windll
        windll.user32.SetActiveWindow(acap.Application.MainWindow.Handle)
        index = e.Data.GetData(SymbolIndex)
        with acdoc() as doc:
            doc.SendStringToExecute('Tls:InsertPart\n%s\n%s\n' % (index.DictionaryName, index.Key), False, False, False)


@panel('Tls:ShowPartListView')
class ShowPartListView(object):
    guid = '600420e2-5a0c-4935-8f3a-d5714531cd11'
    text = '预览零件库'
    dock = acws.DockSides.Right
    itemtypes = {"T1": PartListView}

    def __init__(self, doc, tabs):
        plv = tabs["T1"]
        plv.Root = Application.WorkingDatabase.Root
        plv.DragStart += drag_start
        plv.PartDefining += part_defining


_lastIndex = None


@command("Tls:InsertPart", acrx.CommandFlags.Redraw)
def InsertPart(doc):
    ed = doc.Editor  #type:aced.Editor
    res = ed.GetString('\n请输入元件集名或标准号:')
    global _lastIndex
    if res.Status == aced.PromptStatus.OK:
        name = res.StringResult
        res = ed.GetString('\n请输入元件名:')
        if res.Status == aced.PromptStatus.OK:
            key = res.StringResult
            _lastIndex = SymbolIndex(name, key)
    ipart = Application.WorkingDatabase.ImagePartTable[_lastIndex]
    if ipart:
        with dbtrans(doc) as tr:
            bdefid = tr.addblock('*u')
            bref = acdb.BlockReference(acge.Point3d.Origin, bdefid)
            btr = tr.opencurrspace()
            tr.addentity(btr, bref)
            tr.addregapp(RegAppName)
            SetData(bref, ipart, None)
            if tr.dragblock(bref) and ipart.HasParams:
                ed.SetImpliedSelection((bref.ObjectId,))
            #ed.Document.SendStringToExecute('Tls:ShowPartPropertyList\n', False, False, False)
