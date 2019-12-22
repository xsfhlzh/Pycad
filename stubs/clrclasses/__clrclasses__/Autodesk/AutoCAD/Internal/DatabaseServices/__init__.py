from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DBObject as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import OpenMode as _n_0_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Transaction as _n_0_t_4
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_2_t_1
from __clrclasses__.System import IDisposable as _n_3_t_0
from __clrclasses__.System import ICloneable as _n_3_t_1
from __clrclasses__.System import Enum as _n_3_t_2
from __clrclasses__.System import IComparable as _n_3_t_3
from __clrclasses__.System import IFormattable as _n_3_t_4
from __clrclasses__.System import IConvertible as _n_3_t_5
from __clrclasses__.System import Array as _n_3_t_6
from __clrclasses__.System import UInt32 as _n_3_t_7
from __clrclasses__.System.Collections import ICollection as _n_4_t_0
import typing
class Block1PointParameter(BlockParameter, _n_3_t_0, _n_3_t_1):
    pass
class Block2PointParameter(BlockParameter, _n_3_t_0, _n_3_t_1):
    pass
class BlockAction(BlockElement, _n_3_t_0, _n_3_t_1):
    pass
class BlockActionEntity(BlockElementEntity, _n_3_t_0, _n_3_t_1):
    pass
class BlockElement(EvalConnectable, _n_3_t_0, _n_3_t_1):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
class BlockElementEntity(_n_0_t_0, _n_3_t_0, _n_3_t_1):
    @property
    def Element(self) -> _n_0_t_1:"""Element { get; } -> ObjectId"""
class BlockFlipParameter(Block2PointParameter, _n_3_t_0, _n_3_t_1):
    @property
    def BaseStateLabel(self) -> str:"""BaseStateLabel { get; } -> str"""
    @property
    def FlippedStateLabel(self) -> str:"""FlippedStateLabel { get; } -> str"""
    class FlipState(_n_3_t_2, _n_3_t_3, _n_3_t_4, _n_3_t_5):
        Flipped: int
        NotFlipped: int
        value__: int
class BlockLookupAction(BlockAction, _n_3_t_0, _n_3_t_1):
    @property
    def NumberOfInputColumns(self) -> int:"""NumberOfInputColumns { get; } -> int"""
    @property
    def NumberOfOutputColumns(self) -> int:"""NumberOfOutputColumns { get; } -> int"""
    @property
    def NumberOfRows(self) -> int:"""NumberOfRows { get; } -> int"""
    @staticmethod
    def DuplicateCellsInLookupColumn(aryTable: _n_3_t_6, descArray: LookupColumnDescriptorCollection, colIdx: int, outArray: _n_3_t_6) -> bool:...
    @staticmethod
    def DuplicateRowsOverInputColumns(aryTable: _n_3_t_6, descArray: LookupColumnDescriptorCollection, outArray: _n_3_t_6) -> bool:...
    def GetLookupTable(self, pDataTable: _n_3_t_6, descArray: LookupColumnDescriptorCollection):...
    @staticmethod
    def NonSingletonRangeInInputColumns(aryTable: _n_3_t_6, descArray: LookupColumnDescriptorCollection, outArray: _n_3_t_6) -> bool:...
    @staticmethod
    def NullsInInputColumns(aryTable: _n_3_t_6, descArray: LookupColumnDescriptorCollection, outArray: _n_3_t_6) -> bool:...
    def SetLookupTable(self, aryTable: _n_3_t_6, descArray: LookupColumnDescriptorCollection):...
class BlockLookupActionEntity(BlockActionEntity, _n_3_t_0, _n_3_t_1):
    pass
class BlockLookupParameter(Block1PointParameter, _n_3_t_0, _n_3_t_1):
    pass
class BlockParameter(BlockElement, _n_3_t_0, _n_3_t_1):
    @property
    def PropertyDescription(self) -> BlockParameterPropertyDescriptorCollection:"""PropertyDescription { get; } -> BlockParameterPropertyDescriptorCollection"""
    def GetPropertyConnectionName(self, propName: str) -> str:...
    def GetPropertyValue(self, name: str) -> object:...
    def GetPropertyValue(self, name: str, xform: _n_1_t_0) -> object:...
class BlockParameterPropertyDescriptor(object):
    @property
    def ConnectionName(self) -> str:"""ConnectionName { get; } -> str"""
    @property
    def HasValueSet(self) -> bool:"""HasValueSet { get; } -> bool"""
    @property
    def PropertyDescription(self) -> str:"""PropertyDescription { get; } -> str"""
    @property
    def PropertyName(self) -> str:"""PropertyName { get; } -> str"""
    @property
    def PropertyType(self) -> int:"""PropertyType { get; } -> int"""
    @property
    def ReadOnly(self) -> bool:"""ReadOnly { get; } -> bool"""
    @property
    def UnitsType(self) -> UnitsType:"""UnitsType { get; } -> UnitsType"""
    @property
    def ValueSetValues(self) -> _n_3_t_6:"""ValueSetValues { get; } -> Array"""
    @property
    def Visible(self) -> bool:"""Visible { get; } -> bool"""
class BlockParameterPropertyDescriptorCollection(_n_2_t_0, _n_3_t_0, _n_4_t_0, typing.Iterable[BlockParameterPropertyDescriptor]):
    @property
    def Item(self) -> BlockParameterPropertyDescriptor:"""Item { get; } -> BlockParameterPropertyDescriptor"""
    def __init__(self) -> BlockParameterPropertyDescriptorCollection:...
    def ICollectionCopyTo(self, array: _n_3_t_6, size: int):...
class BlockUserParameter(Block1PointParameter, _n_3_t_0, _n_3_t_1):
    @property
    def UserParamType(self) -> UserParameterType:"""UserParamType { get; } -> UserParameterType"""
class EvalConnectable(EvalExpr, _n_3_t_0, _n_3_t_1):
    pass
class EvalExpr(_n_0_t_2, _n_3_t_0, _n_3_t_1):
    pass
class EvalGraph(_n_0_t_2, _n_3_t_0, _n_3_t_1):
    def GetAllNodes(self) -> _n_3_t_6[int]:...
    def GetNode(self, nodeId: _n_3_t_7, mode: _n_0_t_3, pTrans: _n_0_t_4) -> _n_0_t_2:...
class LookupColumnDescriptor(_n_2_t_1, _n_3_t_0, _n_3_t_1):
    @property
    def ConnectableId(self) -> _n_3_t_7:"""ConnectableId { get; set; } -> UInt32"""
    @property
    def ConnectionName(self) -> str:"""ConnectionName { get; set; } -> str"""
    @property
    def IsInvertible(self) -> bool:"""IsInvertible { get; set; } -> bool"""
    @property
    def IsOutputColumn(self) -> bool:"""IsOutputColumn { get; set; } -> bool"""
    @property
    def PropertyType(self) -> int:"""PropertyType { get; set; } -> int"""
    @property
    def PropertyUnits(self) -> UnitsType:"""PropertyUnits { get; set; } -> UnitsType"""
    @property
    def UnmatchedValue(self) -> str:"""UnmatchedValue { get; set; } -> str"""
    def __init__(self) -> LookupColumnDescriptor:...
class LookupColumnDescriptorCollection(_n_2_t_0, _n_3_t_0, _n_4_t_0, typing.Iterable[LookupColumnDescriptor]):
    @property
    def Item(self) -> LookupColumnDescriptor:"""Item { get; set; } -> LookupColumnDescriptor"""
    def __init__(self) -> LookupColumnDescriptorCollection:...
    def Add(self, value: LookupColumnDescriptor) -> int:...
    def Clear(self):...
    def ICollectionCopyTo(self, array: _n_3_t_6, size: int):...
    def Insert(self, index: int, value: LookupColumnDescriptor):...
    def Remove(self, value: LookupColumnDescriptor):...
    def RemoveAt(self, index: int):...
class UnitsType(_n_3_t_2, _n_3_t_3, _n_3_t_4, _n_3_t_5):
    Angular: int
    Area: int
    Distance: int
    NoUnits: int
    value__: int
class UserParameterType(_n_3_t_2, _n_3_t_3, _n_3_t_4, _n_3_t_5):
    Angle: int
    Area: int
    Distance: int
    Scalar: int
    String: int
    value__: int
    Volume: int
