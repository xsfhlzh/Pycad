__all__ = [
    'ssget', 'ssget_x', 'ssget_l', 'ssget_p', 'ssget_f',
    'ssget_w', 'ssget_c', 'ssget_wp', 'ssget_cp',
    'entsel', 'getpt']

def __getids(ss):
    for obj in ss:
        yield obj.ObjectId

def __getss(res):
    from pycad.system import aced
    if res.Status == aced.PromptStatus.OK:
        return __result(aced.PromptStatus.OK, __getids(res.Value))
    else:
        return __result(res.Status)

def __getvalue(res):
    from pycad.system import aced
    if res.Status == aced.PromptStatus.OK:
        return __result(aced.PromptStatus.OK, res.Value)
    elif res.Status == aced.PromptStatus.Keyword:
        return __result(aced.PromptStatus.Keyword, res.StringResult)
    else:
        return __result(res.Status)

from System.Collections import IEnumerable as __ie
class __result(__ie):
    def __init__(self, status, value = None):
        self.status, self.value = status, value
    def __getitem__(self, id):
        return self.value.__getitem__(id)
    def GetEnumerator(self):
        for v in self.value:
            yield v
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


def ssget(mode = None, filters = None, messages = None, keywords = None):
    from pycad.system import stdio, conv, aced, acrx
    pso = aced.PromptSelectionOptions()
    if mode:
        mode = mode.upper()
        pso.SelectEverythingInAperture = mode.find(':A') > -1
        pso.AllowDuplicates = mode.find(':D') > -1
        pso.SelectEverythingInAperture = mode.find(':E') > -1
        pso.RejectObjectsOnLockedLayers = mode.find(':L') > -1
        pso.PrepareOptionalDetails = mode.find(':N') > -1
        pso.SingleOnly = mode.find(':S') > -1
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
    except KeyError, e:
        return __result(aced.PromptStatus.Keyword, e.message)
    return __getss(ss)


def ssget_x(filters = None):
    from pycad.system import stdio, conv, aced
    if filters:
        ss = stdio.ed.SelectAll(conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectAll()
    return __getss(ss)

def ssget_l():
    from pycad.system import stdio, aced
    ss = stdio.ed.SelectLast()
    return __getss(ss)

def ssget_p():
    from pycad.system import stdio, aced
    ss = stdio.ed.SelectPrevious()
    return __getss(ss)

def ssget_f(pts, filters = None):
    from pycad.system import stdio, conv, aced
    if filters:
        ss = stdio.ed.SelectFence(conv.ToPoint3dCol(pts), conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectFence(conv.ToPoint3dCol(pts))
    return __getss(ss)

def ssget_w(pt1, pt2, filters = None):
    from pycad.system import stdio, conv, aced
    if filters:
        ss = stdio.ed.SelectWindow(pt1, pt2, conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectWindow(pt1, pt2)
    return __getss(ss)

def ssget_c(pt1, pt2, filters = None):
    from pycad.system import stdio, conv, aced
    if filters:
        ss = stdio.ed.SelectCrossingWindow(pt1, pt2, conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectCrossingWindow(pt1, pt2)
    return __getss(ss)

def ssget_wp(pts, filters = None):
    from pycad.system import stdio, conv, aced
    if filters:
        ss = stdio.ed.SelectWindowPolygon(conv.ToPoint3dCol(pts), conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectWindowPolygon(conv.ToPoint3dCol(pts))
    return __getss(ss)

def ssget_cp(pts, filters = None):
    from pycad.system import stdio, conv, aced
    if filters:
        ss = stdio.ed.SelectCrossingPolygon(conv.ToPoint3dCol(pts), conv.BuildFilter(filters))
    else:
        ss = stdio.ed.SelectCrossingPolygon(conv.ToPoint3dCol(pts))
    return __getss(ss)

def sssetfirst(ss=None):
    from pycad.system import stdio
    stdio.ed.SetImpliedSelection(ss)

def ssgetfirst():
    from pycad.system import stdio
    return __getss(stdio.ed.SelectImplied())

def entsel(message):
    from pycad.system import stdio, aced
    res = stdio.ed.GetEntity(message)
    if res.Status == aced.PromptStatus.OK:
        return __result(aced.PromptStatus.OK, (res.ObjectId, res.PickedPoint))
    else:
        return __result(res.Status)

def getpoint(message):
    from pycad.system import stdio, aced
    res = stdio.ed.GetPoint(message)
    return __getvalue(res)

def getcorner(message, basept = None):
    from pycad.system import stdio, aced
    if basept:
        if isinstance(basept, __result):
            basept = basept.value
        res = stdio.ed.GetCorner(message, basept)
    else:
        res = stdio.ed.GetCorner(message)
    return __getvalue(res)

def getreal(message):
    from pycad.system import stdio, aced
    res = stdio.ed.GetDouble(message)
    return __getvalue(res)

def getint(message):
    from pycad.system import stdio, aced
    res = stdio.ed.GetInteger(message)
    return __getvalue(res)

def getangle(message):
    from pycad.system import stdio, aced
    res = stdio.ed.GetAngle(message)
    return __getvalue(res)

def getfile(message, foropen = True):
    from pycad.system import stdio, aced
    if foropen:
        res = stdio.ed.GetFileNameForOpen(message)
    else:
        res = stdio.ed.GetFileNameForSave(message)
    if res.Status == aced.PromptStatus.OK:
        return __result(aced.PromptStatus.OK, res.StringResult)
    else:
        return __result(res.Status)

def getstr(message):
    from pycad.system import stdio, aced
    res = stdio.ed.GetString(message)
    if res.Status == aced.PromptStatus.OK:
        return __result(aced.PromptStatus.OK, res.StringResult)
    elif res.Status == aced.PromptStatus.Keyword:
        return __result(aced.PromptStatus.Keyword, res.StringResult)
    else:
        return __result(res.Status)