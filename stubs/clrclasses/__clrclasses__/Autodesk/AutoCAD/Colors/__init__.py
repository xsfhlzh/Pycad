from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import AuditInfo as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DwgFiler as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DxfFiler as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_1_t_0
from __clrclasses__.System import IDisposable as _n_2_t_0
from __clrclasses__.System import IComparable as _n_2_t_1
from __clrclasses__.System import ICloneable as _n_2_t_2
from __clrclasses__.System import Byte as _n_2_t_3
from __clrclasses__.System import Enum as _n_2_t_4
from __clrclasses__.System import IFormattable as _n_2_t_5
from __clrclasses__.System import IConvertible as _n_2_t_6
from __clrclasses__.System import ValueType as _n_2_t_7
from __clrclasses__.System import Array as _n_2_t_8
from __clrclasses__.System.Collections import IList as _n_3_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_3_t_1
from __clrclasses__.System.ComponentModel import TypeConverter as _n_4_t_0
from __clrclasses__.System.Drawing import Color as _n_5_t_0
from __clrclasses__.System.Windows.Media import Color as _n_6_t_0
import typing
class Color(_n_1_t_0, _n_2_t_0, _n_2_t_1, _n_2_t_2):
    @property
    def Blue(self) -> _n_2_t_3:"""Blue { get; } -> Byte"""
    @property
    def BookName(self) -> str:"""BookName { get; } -> str"""
    @property
    def ColorIndex(self) -> int:"""ColorIndex { get; } -> int"""
    @property
    def ColorMethod(self) -> ColorMethod:"""ColorMethod { get; } -> ColorMethod"""
    @property
    def ColorName(self) -> str:"""ColorName { get; } -> str"""
    @property
    def ColorNameForDisplay(self) -> str:"""ColorNameForDisplay { get; } -> str"""
    @property
    def ColorValue(self) -> _n_5_t_0:"""ColorValue { get; } -> Color"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def DictionaryKey(self) -> str:"""DictionaryKey { get; } -> str"""
    @property
    def DictionaryKeyLength(self) -> int:"""DictionaryKeyLength { get; } -> int"""
    @property
    def EntityColor(self) -> EntityColor:"""EntityColor { get; } -> EntityColor"""
    @property
    def Explanation(self) -> str:"""Explanation { get; } -> str"""
    @property
    def Green(self) -> _n_2_t_3:"""Green { get; } -> Byte"""
    @property
    def HasBookName(self) -> bool:"""HasBookName { get; } -> bool"""
    @property
    def HasColorName(self) -> bool:"""HasColorName { get; } -> bool"""
    @property
    def IsByAci(self) -> bool:"""IsByAci { get; } -> bool"""
    @property
    def IsByBlock(self) -> bool:"""IsByBlock { get; } -> bool"""
    @property
    def IsByColor(self) -> bool:"""IsByColor { get; } -> bool"""
    @property
    def IsByLayer(self) -> bool:"""IsByLayer { get; } -> bool"""
    @property
    def IsByPen(self) -> bool:"""IsByPen { get; } -> bool"""
    @property
    def IsForeground(self) -> bool:"""IsForeground { get; } -> bool"""
    @property
    def IsNone(self) -> bool:"""IsNone { get; } -> bool"""
    @property
    def PenIndex(self) -> int:"""PenIndex { get; } -> int"""
    @property
    def Red(self) -> _n_2_t_3:"""Red { get; } -> Byte"""
    def __init__(self) -> Color:...
    def Audit(self, auditInfo: _n_0_t_0):...
    @staticmethod
    def DwgIn(inputFiler: _n_0_t_1) -> Color:...
    def DwgOut(self, outputFiler: _n_0_t_1):...
    @staticmethod
    def DxfIn(inputFiler: _n_0_t_2, groupCodeOffset: int) -> Color:...
    def DxfOut(self, outputFiler: _n_0_t_2, groupCodeOffset: int):...
    @staticmethod
    def FromColor(value: _n_5_t_0) -> Color:...
    @staticmethod
    def FromColor(value: _n_6_t_0) -> Color:...
    @staticmethod
    def FromColorIndex(colorMethod: ColorMethod, colorIndex: int) -> Color:...
    @staticmethod
    def FromDictionaryName(name: str) -> Color:...
    @staticmethod
    def FromEntityColor(eclr: EntityColor) -> Color:...
    @staticmethod
    def FromNames(colorName: str, bookName: str) -> Color:...
    @staticmethod
    def FromRgb(red: _n_2_t_3, green: _n_2_t_3, blue: _n_2_t_3) -> Color:...
class ColorConverter(_n_4_t_0):
    def __init__(self) -> ColorConverter:...
class ColorMethod(_n_2_t_4, _n_2_t_1, _n_2_t_5, _n_2_t_6):
    ByAci: int
    ByBlock: int
    ByColor: int
    ByLayer: int
    ByPen: int
    Foreground: int
    LayerFrozen: int
    LayerOff: int
    _None: int
    value__: int
class EntityColor(_n_2_t_7):
    @property
    def Blue(self) -> _n_2_t_3:"""Blue { get; } -> Byte"""
    @property
    def ColorIndex(self) -> int:"""ColorIndex { get; } -> int"""
    @property
    def ColorMethod(self) -> ColorMethod:"""ColorMethod { get; } -> ColorMethod"""
    @property
    def Green(self) -> _n_2_t_3:"""Green { get; } -> Byte"""
    @property
    def IsByAci(self) -> bool:"""IsByAci { get; } -> bool"""
    @property
    def IsByBlock(self) -> bool:"""IsByBlock { get; } -> bool"""
    @property
    def IsByColor(self) -> bool:"""IsByColor { get; } -> bool"""
    @property
    def IsByLayer(self) -> bool:"""IsByLayer { get; } -> bool"""
    @property
    def IsByPen(self) -> bool:"""IsByPen { get; } -> bool"""
    @property
    def IsForeground(self) -> bool:"""IsForeground { get; } -> bool"""
    @property
    def IsLayerFrozen(self) -> bool:"""IsLayerFrozen { get; } -> bool"""
    @property
    def IsLayerFrozenOrOff(self) -> bool:"""IsLayerFrozenOrOff { get; } -> bool"""
    @property
    def IsLayerOff(self) -> bool:"""IsLayerOff { get; } -> bool"""
    @property
    def IsNone(self) -> bool:"""IsNone { get; } -> bool"""
    @property
    def LayerIndex(self) -> int:"""LayerIndex { get; } -> int"""
    @property
    def PenIndex(self) -> int:"""PenIndex { get; } -> int"""
    @property
    def Red(self) -> _n_2_t_3:"""Red { get; } -> Byte"""
    @property
    def TrueColor(self) -> int:"""TrueColor { get; } -> int"""
    def __init__(self, trueColor: int) -> EntityColor:...
    def __init__(self, value: ColorMethod) -> EntityColor:...
    def __init__(self, value: ColorMethod, index: int) -> EntityColor:...
    def __init__(self, red: _n_2_t_3, green: _n_2_t_3, blue: _n_2_t_3) -> EntityColor:...
    @staticmethod
    def LookUpAci(red: _n_2_t_3, green: _n_2_t_3, blue: _n_2_t_3) -> _n_2_t_3:...
    @staticmethod
    def LookUpRgb(colorIndex: _n_2_t_3) -> int:...
class EntityColorCollection(_n_3_t_0, typing.Iterable[EntityColor]):
    DefaultSize: int
    @property
    def Capacity(self) -> int:"""Capacity { get; set; } -> int"""
    def __init__(self) -> EntityColorCollection:...
    def __init__(self, capacity: int) -> EntityColorCollection:...
    def __init__(self, values: _n_2_t_8[EntityColor]) -> EntityColorCollection:...
    def AddRange(self, range: _n_2_t_8[EntityColor]):...
    def ToArray(self) -> _n_2_t_8[EntityColor]:...
    def TrimToSize(self):...
class EntityColorCollectionEnumerator(_n_3_t_1):
    def __init__(self, col: EntityColorCollection) -> EntityColorCollectionEnumerator:...
class Transparency(_n_2_t_7):
    @property
    def Alpha(self) -> _n_2_t_3:"""Alpha { get; } -> Byte"""
    @property
    def IsByAlpha(self) -> bool:"""IsByAlpha { get; } -> bool"""
    @property
    def IsByBlock(self) -> bool:"""IsByBlock { get; } -> bool"""
    @property
    def IsByLayer(self) -> bool:"""IsByLayer { get; } -> bool"""
    @property
    def IsClear(self) -> bool:"""IsClear { get; } -> bool"""
    @property
    def IsInvalid(self) -> bool:"""IsInvalid { get; } -> bool"""
    @property
    def IsSolid(self) -> bool:"""IsSolid { get; } -> bool"""
    def __init__(self, method: TransparencyMethod) -> Transparency:...
    def __init__(self, alpha: _n_2_t_3) -> Transparency:...
class TransparencyCollection(_n_3_t_0, typing.Iterable[Transparency]):
    DefaultSize: int
    @property
    def Capacity(self) -> int:"""Capacity { get; set; } -> int"""
    def __init__(self) -> TransparencyCollection:...
    def __init__(self, capacity: int) -> TransparencyCollection:...
    def __init__(self, values: _n_2_t_8[Transparency]) -> TransparencyCollection:...
    def AddRange(self, range: _n_2_t_8[Transparency]):...
    def ToArray(self) -> _n_2_t_8[Transparency]:...
    def TrimToSize(self):...
class TransparencyCollectionEnumerator(_n_3_t_1):
    def __init__(self, col: TransparencyCollection) -> TransparencyCollectionEnumerator:...
class TransparencyMethod(_n_2_t_4, _n_2_t_1, _n_2_t_5, _n_2_t_6):
    ByAlpha: int
    ByBlock: int
    ByLayer: int
    ErrorValue: int
    value__: int
