from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LayerTableRecord as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_1_t_0
from __clrclasses__.System import Array as _n_2_t_0
from __clrclasses__.System import IDisposable as _n_2_t_1
from __clrclasses__.System import ICloneable as _n_2_t_2
from __clrclasses__.System import Enum as _n_2_t_3
from __clrclasses__.System import IComparable as _n_2_t_4
from __clrclasses__.System import IFormattable as _n_2_t_5
from __clrclasses__.System import IConvertible as _n_2_t_6
from __clrclasses__.System import ValueType as _n_2_t_7
from __clrclasses__.System import IntPtr as _n_2_t_8
from __clrclasses__.System.Collections import ICollection as _n_3_t_0
import typing
class AndExpression(object):
    def GetRelationalExpressions(self) -> _n_2_t_0[RelationalExpression]:...
class LayerCollection(_n_3_t_0, typing.Iterable[_n_0_t_0]):
    @property
    def Item(self) -> _n_0_t_0:"""Item { get; } -> ObjectId"""
    def Add(self, value: _n_0_t_0):...
    def Clear(self):...
    def Contains(self, value: _n_0_t_0) -> bool:...
    def Remove(self, value: _n_0_t_0):...
class LayerFilter(_n_1_t_0, _n_2_t_1, _n_2_t_2):
    @property
    def AllowDelete(self) -> bool:"""AllowDelete { get; } -> bool"""
    @property
    def AllowNested(self) -> bool:"""AllowNested { get; } -> bool"""
    @property
    def AllowRename(self) -> bool:"""AllowRename { get; } -> bool"""
    @property
    def DisplayImages(self) -> LayerFilterDisplayImages:"""DisplayImages { get; } -> LayerFilterDisplayImages"""
    @property
    def DynamicallyGenerated(self) -> bool:"""DynamicallyGenerated { get; } -> bool"""
    @property
    def FilterExpression(self) -> str:"""FilterExpression { get; set; } -> str"""
    @property
    def IsIdFilter(self) -> bool:"""IsIdFilter { get; } -> bool"""
    @property
    def IsProxy(self) -> bool:"""IsProxy { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NestedFilters(self) -> LayerFilterCollection:"""NestedFilters { get; } -> LayerFilterCollection"""
    @property
    def Parent(self) -> LayerFilter:"""Parent { get; } -> LayerFilter"""
    def __init__(self) -> LayerFilter:...
    def Filter(self, layer: _n_0_t_1) -> bool:...
    def GenerateNested(self):...
    def GetFilterExpressionTree(self) -> _n_2_t_0[AndExpression]:...
    def ShowEditor(self) -> LayerFilter.DialogResult:...
    class DialogResult(_n_2_t_3, _n_2_t_4, _n_2_t_5, _n_2_t_6):
        Cancel: int
        OK: int
        UseDefault: int
        value__: int
class LayerFilterCollection(_n_3_t_0, typing.Iterable[LayerFilter]):
    @property
    def Item(self) -> LayerFilter:"""Item { get; } -> LayerFilter"""
    def Add(self, value: LayerFilter):...
    def Clear(self):...
    def Contains(self, value: LayerFilter) -> bool:...
    def Remove(self, value: LayerFilter):...
class LayerFilterDisplayImages(_n_2_t_7):
    @property
    def ImageIndex(self) -> int:"""ImageIndex { get; } -> int"""
    @property
    def ImageListHandle(self) -> _n_2_t_8:"""ImageListHandle { get; } -> IntPtr"""
    @property
    def SelectedImageIndex(self) -> int:"""SelectedImageIndex { get; } -> int"""
    def __init__(self, imageListHandle: _n_2_t_8, imageIndex: int, selectedImageIndex: int) -> LayerFilterDisplayImages:...
class LayerFilterTree(_n_2_t_7):
    @property
    def Current(self) -> LayerFilter:"""Current { get; } -> LayerFilter"""
    @property
    def Root(self) -> LayerFilter:"""Root { get; } -> LayerFilter"""
    def __init__(self, root: LayerFilter, current: LayerFilter) -> LayerFilterTree:...
class LayerGroup(LayerFilter, _n_2_t_1, _n_2_t_2):
    @property
    def LayerIds(self) -> LayerCollection:"""LayerIds { get; } -> LayerCollection"""
    def __init__(self) -> LayerGroup:...
class RelationalExpression(object):
    @property
    def Constant(self) -> str:"""Constant { get; } -> str"""
    @property
    def Variable(self) -> str:"""Variable { get; } -> str"""
