And = "&"
And2 = "and"
Or = "|"
Or2 = "or"
Not = "~"
Not2 = "not"
Xor = "^"
Xor2 = "xor"
__all__ = [
    'And', 'And2', 'Or', 'Or2', 'Not', 'Not2', 'Xor', 'Xor2',
    'BuildFilter', 'ToSafeArray', 'ToList', 
    'ToTuple', 'ToBuffer', 'ToFilter',
    'FromLispData', 'ToLispData', 'ToTypedValue']

from pycad.system.mgdnss import aced as __aced, acdb as __acdb
import typing as __typing

def BuildFilter(*lst: __typing.Iterable) -> __aced.SelectionFilter:
    """
    创建选择集过滤器

    (0, 'line'), (8, '0') -> ((0, 'line'), (8, '0'))

    (conv.Not, 0, 'line'), -> ((-4, '<not')(0, 'line'), (-4, 'not>'))

    (10, [">,>,*", acge.Point3d(), "<,<,*", acge.Point3d(10,10,0)]) -> ((-4, '>,>,*'), (10, (0,0,0)), (-4, '<,<,*'), (10, (10,10,0)))
    """
def ToSafeArray(objs: __typing.Iterable) -> __typing.Iterable:
    """
    将Net对象迭代器转换为Com对象数组
    """
def ToList(rb: __acdb.ResultBuffer) -> list:
    """
    将ResultBuffer转换为列表,可用于XData、扩展数据等
    """
def ToBuffer(lst: __typing.Iterable) -> __acdb.ResultBuffer:
    """
    将迭代器转换为ResultBuffer,可用于XData、扩展数据等

    ToBuffer(((1001, "MyApp"), (1000, "MyData")))
    """
def ToTuple(lst: __typing.Iterable) -> tuple:
    """
    将迭代器转换为TypedValue元组
    """
def ToFilter(lst: __typing.Iterable) -> __aced.SelectionFilter:
    """
    将迭代器转换为过滤器

    ToFilter(((0, "line"), (8, "0")))
    """
def FromLispData(rb: __acdb.ResultBuffer) -> list:
    """
    将Lisp数据(ResultBuffer)转换为列表
    """
def ToLispData(obj: __typing.Iterable) -> __acdb.ResultBuffer:
    """
    将迭代器转换为Lisp数据(ResultBuffer)
    """
def ToTypedValue(obj) -> __acdb.TypedValue:
    """
    将数据转换为Lisp数据(TypedValue)
    """