__all__ = [
    'And', 'And2', 'Or', 'Or2', 'Not', 'Not2', 'Xor', 'Xor2',
    'BuildFilter', 'ToSafeArray', 'ToList', 
    'ToTuple', 'ToBuffer', 'ToFilter',
    'FromLispData', 'ToLispData']

And = "&"
And2 = "and"
Or = "|"
Or2 = "or"
Not = "~"
Not2 = "not"
Xor = "^"
Xor2 = "xor"

from pycad.system.mgdnss import *

def BuildFilter(*lst):
    from NFox.Pycad.Core.Filters import OpFilter
    return aced.SelectionFilter(OpFilter.Create(lst).ToTuple())

def ToPoint3dCol(pts):
    from pycad.system import acge
    if isinstance(pts, acge.Point3dCollection):
        return pts
    points = acge.Point3dCollection()
    for pt in pts:
        points.Add(pt)
    return points

def ToSafeArray(objs):
    import clr
    clr.AddReference('stdole')
    from System import Array
    from stdole import IDispatch
    return Array[IDispatch](objs)

def ToList(rb):
    try: return [[v.TypeCode, v.Value] for v in rb]
    except: return []

def ToTuple(lst):
    return tuple(_newvalue(*v) for v in lst)

def ToBuffer(lst):
    try: return acdb.ResultBuffer(ToTuple(lst))
    except: pass

def ToFilter(lst):
    return aced.SelectionFilter(ToTuple(lst))

def FromLispData(rb):
    if rb: return _getlist(rb.GetEnumerator())
    return []

def ToLispData(obj):
    lst = []
    _getbuffer(obj, lst)
    n = len(lst)
    if n == 0:
        return _newvalue(acrx.LispDataType.Nil)
    elif n == 1:
        return lst[0]
    return acdb.ResultBuffer(tuple(lst))

def _getlist(it):
    lst = []
    while it.MoveNext():
        from System import Enum
        code = Enum.ToObject(acrx.LispDataType, it.Current.TypeCode)
        if code == acrx.LispDataType.ListEnd:
            return lst
        elif code == acrx.LispDataType.DottedPair:
            return tuple(lst)
        elif code == acrx.LispDataType.ListBegin:
            lst.append(_getlist(it))
        elif code == acrx.LispDataType.T_atom:
            lst.append(True)
        elif code == acrx.LispDataType.Nil:
            lst.append(False)
        else:
            lst.append(it.Current.Value)
    return lst

def _getbuffer(obj, lst):
    from System import Int16, Int32
    if isinstance(obj, acdb.TypedValue):
        lst.append(obj)
    elif isinstance(obj, (Int16, Int32, int)):
        lst.append(_newvalue(acrx.LispDataType.Int32, obj))
    elif obj == True:
        lst.append(_newvalue(acrx.LispDataType.T_atom))
    elif obj in (False, None):
        lst.append(_newvalue(acrx.LispDataType.Nil))
    elif isinstance(obj, float):
        lst.append(_newvalue(acrx.LispDataType.Double, obj))
    elif isinstance(obj, str):
        lst.append(_newvalue(acrx.LispDataType.Text, obj))
    elif isinstance(obj, acge.Point2d):
        lst.append(_newvalue(acrx.LispDataType.Point2d, obj))
    elif isinstance(obj, acge.Point3d):
        lst.append(_newvalue(acrx.LispDataType.Point3d, obj))
    elif isinstance(obj, acdb.ObjectId):
        lst.append(_newvalue(acrx.LispDataType.ObjectId, obj))
    elif isinstance(obj, aced.SelectionSet):
        lst.append(_newvalue(acrx.LispDataType.SelectionSet, obj))
    else:
        from collections import Iterable
        if isinstance(obj, Iterable):
            lst.append(_newvalue(acrx.LispDataType.ListBegin))
            for o in obj:
                _getbuffer(o, lst)
            if isinstance(obj, tuple):
                lst.append(_newvalue(acrx.LispDataType.DottedPair))
            else:
                lst.append(_newvalue(acrx.LispDataType.ListEnd))

def _newvalue(code, value = -1):
    try:
        return acdb.TypedValue(code, value)
    except TypeError:
        return acdb.TypedValue(code.value__, value)
