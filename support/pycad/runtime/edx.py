__all__ = [
    'ssget', 'ssget_x', 'ssget_l', 'ssget_p', 'ssget_f',
    'ssget_w', 'ssget_c', 'ssget_wp', 'ssget_cp', 'entsel',
    'getnested', 'getfile', 'getpoint', 'getcorner', 'getdist',
    'getangle', 'getstr', 'getreal', 'getint']

class __result(object):
    def __init__(self, status, value = None):
        self.status, self.value = status, value
    def ok(self):
        from pycad.system import aced
        return self.status == aced.PromptStatus.OK
    def cancel(self):
        from pycad.system import aced
        return self.status == aced.PromptStatus.Cancel
    def keyword(self, *keywords):
        from pycad.system import aced
        b = self.status == aced.PromptStatus.Keyword
        if keywords:
            return b and self.value in keywords
        return b
    def modeless(self):
        from pycad.system import aced
        return self.status == aced.PromptStatus.Modeless
    def error(self):
        from pycad.system import aced
        return self.status == aced.PromptStatus.Error
    def other(self):
        from pycad.system import aced
        return self.status == aced.PromptStatus.Other
    def none(self):
        from pycad.system import aced
        return self.status == getattr(aced.PromptStatus, "None")

from System.Collections import IEnumerable as __ie
class selection_result(__result, __ie):
    def __init__(self, ss_or_status, value = None):
        from pycad.system import aced
        if isinstance(ss_or_status, aced.PromptStatus):
            super(selection_result, self).__init__(ss_or_status, value)
        elif ss_or_status.Status == aced.PromptStatus.OK:
            super(selection_result, self).__init__(aced.PromptStatus.OK, ss_or_status.Value)
        else:
            super(selection_result, self).__init__(ss_or_status.Status)
    def GetEnumerator(self):
        for selobj in self.value:
            yield selobj.ObjectId
    def __getitem__(self, id):
        return self.value[id]

class value_result(__result):
    def __init__(self, res):
        from pycad.system import aced
        if res.Status == aced.PromptStatus.OK:
            super(value_result, self).__init__(aced.PromptStatus.OK, res.Value)
        elif res.Status == aced.PromptStatus.Keyword:
            super(value_result, self).__init__(aced.PromptStatus.Keyword, res.StringResult)
        else:
            super(value_result, self).__init__(res.Status)

class string_result(__result):
    def __init__(self, res):
        from pycad.system import aced
        if res.Status == aced.PromptStatus.OK:
            super(string_result, self).__init__(aced.PromptStatus.OK, res.StringResult)
        elif res.Status == aced.PromptStatus.Keyword:
            super(string_result, self).__init__(aced.PromptStatus.Keyword, res.StringResult)
        else:
            super(string_result, self).__init__(res.Status)

class entity_result(value_result):
    @property
    def ObjectId(self):
        return self.value.ObjectId
    @property
    def PickedPoint(self):
        return self.value.PickedPoint

class subentity_result(entity_result):
    @property
    def Transform(self):
        return self.value.Transform
    def GetContainers(self):
        return self.value.GetContainers()

def ssget(mode = None, filters = None, messages = None, keywords = None):
    from pycad.system import stdio, conv, aced
    pso = aced.PromptSelectionOptions()
    if mode:
        mode = mode.upper()
        pso.SinglePickInSpace = mode.find(':A') > -1
        pso.RejectObjectsFromNonCurrentSpace = mode.find(':C') > -1
        pso.AllowDuplicates = mode.find(':D') > -1
        pso.SelectEverythingInAperture = mode.find(':E') > -1
        pso.RejectObjectsOnLockedLayers = mode.find(':L') > -1
        pso.PrepareOptionalDetails = mode.find(':N') > -1
        pso.SingleOnly = mode.find(':S') > -1
        pso.RejectPaperspaceViewport = mode.find(':V') > -1
        pso.AllowSubSelections = mode.find('-A') > -1
        pso.ForceSubSelections = mode.find('-F') > -1
    if messages:
        pso.MessageForAdding, pso.MessageForRemoval = messages
    if keywords:
        for keyword in keywords:
            pso.Keywords.Add(keyword)
        if pso.MessageForAdding is None:
            pso.MessageForAdding = "选择对象"
        pso.MessageForAdding += "[%s]" % "/".join(keywords)
        def func(s, e): raise KeyError(e.Input)
        pso.KeywordInput += func
    try:
        if filters:
            ss = stdio.ed.GetSelection(pso, conv.BuildFilter(filters))
        else:
            ss = stdio.ed.GetSelection(pso)
    except KeyError as e:
        return selection_result(aced.PromptStatus.Keyword, e.message)
    return selection_result(ss)

def ssget_x(filters = None):
    from pycad.system import stdio, conv
    if filters:
        ss = stdio.ed.SelectAll(conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectAll()
    return selection_result(ss)

def ssget_l():
    from pycad.system import stdio
    ss = stdio.ed.SelectLast()
    return selection_result(ss)

def ssget_p():
    from pycad.system import stdio
    ss = stdio.ed.SelectPrevious()
    return selection_result(ss)

def ssget_f(pts, filters = None):
    from pycad.system import stdio, conv
    if filters:
        ss = stdio.ed.SelectFence(conv.ToPoint3dCol(pts), conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectFence(conv.ToPoint3dCol(pts))
    return selection_result(ss)

def ssget_w(pt1, pt2, filters = None):
    from pycad.system import stdio, conv
    if filters:
        ss = stdio.ed.SelectWindow(pt1, pt2, conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectWindow(pt1, pt2)
    return selection_result(ss)

def ssget_c(pt1, pt2, filters = None):
    from pycad.system import stdio, conv
    if filters:
        ss = stdio.ed.SelectCrossingWindow(pt1, pt2, conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectCrossingWindow(pt1, pt2)
    return selection_result(ss)

def ssget_wp(pts, filters = None):
    from pycad.system import stdio, conv
    if filters:
        ss = stdio.ed.SelectWindowPolygon(conv.ToPoint3dCol(pts), conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectWindowPolygon(conv.ToPoint3dCol(pts))
    return selection_result(ss)

def ssget_cp(pts, filters = None):
    from pycad.system import stdio, conv
    if filters:
        ss = stdio.ed.SelectCrossingPolygon(conv.ToPoint3dCol(pts), conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectCrossingPolygon(conv.ToPoint3dCol(pts))
    return selection_result(ss)

def sssetfirst(ss=None):
    from pycad.system import stdio
    stdio.ed.SetImpliedSelection(ss)

def ssgetfirst():
    from pycad.system import stdio
    return selection_result(stdio.ed.SelectImplied())

def entsel(message):
    from pycad.system import stdio
    return entity_result(stdio.ed.GetEntity(message))

def getnested(message):
    from pycad.system import stdio
    return subentity_result(stdio.ed.GetNestedEntity(message))

def getpoint(message):
    from pycad.system import stdio
    return value_result(stdio.ed.GetPoint(message))

def getcorner(message, basept = None):
    from pycad.system import stdio
    if basept:
        if isinstance(basept, __result):
            basept = basept.value
        return value_result(stdio.ed.GetCorner(message, basept))
    else:
        return value_result(stdio.ed.GetCorner(message))

def getfile(message, foropen = True):
    from pycad.system import stdio
    if foropen:
        return string_result(stdio.ed.GetFileNameForOpen(message))
    else:
        return string_result(stdio.ed.GetFileNameForSave(message))

def getangle(message):
    from pycad.system import stdio
    return value_result(stdio.ed.GetAngle(message))

def getdist(message):
    from pycad.system import stdio
    return value_result(stdio.ed.GetDistance(message))

def getreal(message):
    from pycad.system import stdio
    return value_result(stdio.ed.GetDouble(message))

def getint(message):
    from pycad.system import stdio
    return value_result(stdio.ed.GetInteger(message))

def getstr(message):
    from pycad.system import stdio
    return string_result(stdio.ed.GetString(message))

