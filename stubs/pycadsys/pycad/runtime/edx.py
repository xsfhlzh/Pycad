__all__ = [
    'ssget', 'ssget_x', 'ssget_l', 'ssget_p', 'ssget_f',
    'ssget_w', 'ssget_c', 'ssget_wp', 'ssget_cp', 'entsel',
    'getnested', 'getfile', 'getpoint', 'getcorner', 'getdist',
    'getangle', 'getstr', 'getreal', 'getint']

from pycad.system import acge as __acge, acdb as __acdb
import typing as __typing
from System.Collections import IEnumerable as __ie

class __result(object):
    """
    带状态的返回值
    """
    def __init__(self, status, value = None):...
    @property
    def status(self):...
    @property
    def value(self):...
    def ok(self) -> bool:...
    def cancel(self) -> bool:...
    def keyword(self, *keywords) -> bool:...
    def modeless(self) -> bool:...
    def error(self) -> bool:...
    def other(self) -> bool:...
    def none(self) -> bool:...

class selection_result(__result, __ie):
    def __init__(self, ss_or_status, value = None):...
    def GetEnumerator(self):...
    def __getitem__(self, id):...

class value_result(__result):
    def __init__(self, res):...

class string_result(__result):
    def __init__(self, res):...

class entity_result(value_result):
    @property
    def ObjectId(self):...
    @property
    def PickedPoint(self):...

class subentity_result(entity_result):
    @property
    def Transform(self):...
    def GetContainers(self) -> tuple:...

def ssget(mode: __typing.Optional[str], filters: __typing.Iterable, messages: __typing.Tuple[str, str], keywords: __typing.Tuple) -> selection_result:
    """
    在屏幕上选择图元

        mode: 选择模式,可以是下面多种模式的组合
            :A SinglePickInSpace
            :C RejectObjectsFromNonCurrentSpace
            :D AllowDuplicates
            :E SelectEverythingInAperture
            :L RejectObjectsOnLockedLayers
            :N PrepareOptionalDetails
            :S SingleOnly
            :V RejectPaperspaceViewport
            -A AllowSubSelections
            -F ForceSubSelections
        filters: 过滤器,参考conv.BuildFilter函数
        messages: 添加/删除图元时的提示
        keywords: 关键字集合
    """

def ssget_x(filters: __typing.Optional[__typing.Iterable])  -> selection_result:
    """
    选择全部图元

        filters: 过滤器,参考conv.BuildFilter函数
    """

def ssget_l() -> selection_result:
    """
    选择最后一个图元
    """

def ssget_p() -> selection_result:
    """
    选择上一个选择集
    """

def ssget_f(pts: __typing.Iterable[__acge.Point3d], filters: __typing.Optional[__typing.Iterable]) -> selection_result:
    """
    按给定的路径在屏幕上选择图元

        pts: 描述路径的点集合
        filters: 过滤器,参考conv.BuildFilter函数
    """

def ssget_w(pt1: __acge.Point3d, pt2: __acge.Point3d, filters: __typing.Optional[__typing.Iterable]) -> selection_result:
    """
    按两个角点在屏幕上选择矩形窗口内的图元

        pt1: 第一角点
        pt2: 第二角点
        filters: 过滤器,参考conv.BuildFilter函数
    """

def ssget_c(pt1: __acge.Point3d, pt2: __acge.Point3d, filters: __typing.Optional[__typing.Iterable]) -> selection_result:
    """
    按两个角点在屏幕上选择穿过矩形窗口的图元

        pt1: 第一角点
        pt2: 第二角点
        filters: 过滤器,参考conv.BuildFilter函数
    """

def ssget_wp(pts: __typing.Iterable[__acge.Point3d], filters: __typing.Optional[__typing.Iterable]) -> selection_result:
    """
    按两个角点在屏幕上选择多边形窗口内的图元

        pt1: 第一角点
        pt2: 第二角点
        filters: 过滤器,参考conv.BuildFilter函数
    """

def ssget_cp(pts: __typing.Iterable[__acge.Point3d], filters: __typing.Optional[__typing.Iterable]) -> selection_result:
    """
    按两个角点在屏幕上选择穿过多边形窗口的图元

        pt1: 第一角点
        pt2: 第二角点
        filters: 过滤器,参考conv.BuildFilter函数
    """

def sssetfirst(ss: __typing.Iterator[__acdb.ObjectId]):
    """
    将给定的图元加入Pickfirst选择集

        ss: 图元Id集合或选择集
    """

def ssgetfirst() -> selection_result:
    """
    获取Pickfirst选择集
    """

def entsel(message) -> entity_result:
    """
    获取图元

        message: 选择图元时的提示或设置
    """

def getnested(message) -> value_result:
    """
    获取子实体

        message: 选择子实体时的提示或设置
    """

def getfile(message, foropen = True) -> string_result:
    """
    获取文件

        message: 选择文件时的提示或设置
        foropen： 显示打开或保存
    """

def getpoint(message) -> value_result:
    """
    获取点

        message: 选择点时的提示或设置
    """

def getcorner(message) -> value_result:
    """
    获取角点

        message: 选择角点时的提示或设置
    """

def getangle(message) -> value_result:
    """
    获取角度

        message: 输入角度时的提示或设置
    """

def getdist(message) -> value_result:
    """
    获取距离

        message: 输入距离时的提示或设置
    """

def getreal(message) -> value_result:
    """
    获取浮点数

        message: 输入浮点数时的提示或设置
    """

def getint(message) -> value_result:
    """
    获取整数

        message: 输入整数时的提示或设置
    """

def getstr(message, foropen = True) -> string_result:
    """
    获取字符串

        message: 输入字符串时的提示或设置
    """



