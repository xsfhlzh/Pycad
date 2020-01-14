from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DBObject as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LayerTable as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import BlockTableRecord as _n_0_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Extents3d as _n_0_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import BlockReference as _n_0_t_5
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3d as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2dCollection as _n_1_t_3
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector2d as _n_1_t_4
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXClass as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_2_t_1
from __clrclasses__.System import IDisposable as _n_3_t_0
from __clrclasses__.System import ICloneable as _n_3_t_1
from __clrclasses__.System import DateTime as _n_3_t_2
from __clrclasses__.System import IntPtr as _n_3_t_3
from __clrclasses__.System import Byte as _n_3_t_4
from __clrclasses__.System import ValueType as _n_3_t_5
import typing
class Filter(_n_0_t_0, _n_3_t_0, _n_3_t_1):
    @property
    def IndexClass(self) -> _n_2_t_0:"""IndexClass { get; } -> RXClass"""
class FilteredBlockIterator(_n_2_t_1, _n_3_t_0):
    @property
    def BuffersForComposition(self) -> bool:"""BuffersForComposition { get; } -> bool"""
    @property
    def EstimatedHitFraction(self) -> float:"""EstimatedHitFraction { get; } -> float"""
    @property
    def Id(self) -> _n_0_t_1:"""Id { get; } -> ObjectId"""
    @property
    def Next(self) -> _n_0_t_1:"""Next { get; } -> ObjectId"""
    def Accepts(self, id: _n_0_t_1) -> bool:...
    def AddToBuffer(self, id: _n_0_t_1):...
    def Seek(self, id: _n_0_t_1):...
    def Start(self):...
class Index(_n_0_t_0, _n_3_t_0, _n_3_t_1):
    @property
    def IsUptoDate(self) -> bool:"""IsUptoDate { get; } -> bool"""
    @property
    def LastUpdatedAt(self) -> _n_3_t_2:"""LastUpdatedAt { get; set; } -> DateTime"""
    @property
    def LastUpdatedAtU(self) -> _n_3_t_2:"""LastUpdatedAtU { get; set; } -> DateTime"""
    @property
    def ObjectBeingIndexedId(self) -> _n_0_t_1:"""ObjectBeingIndexedId { get; } -> ObjectId"""
    def GetIterator(self, filter: Filter) -> FilteredBlockIterator:...
    def RebuildFull(self, indexData: IndexUpdateData):...
class IndexUpdateData(_n_2_t_1, _n_3_t_0):
    def AddId(self, id: _n_0_t_1):...
    def GetIdData(self, id: _n_0_t_1) -> int:...
    def GetIdDataPtr(self, id: _n_0_t_1) -> _n_3_t_3:...
    def GetIdFlags(self, id: _n_0_t_1) -> _n_3_t_4:...
    def SetIdData(self, id: _n_0_t_1, data: int):...
    def SetIdData(self, id: _n_0_t_1, data: _n_3_t_3):...
    def SetIdFlags(self, id: _n_0_t_1, flags: _n_3_t_4):...
class LayerFilter(Filter, _n_3_t_0, _n_3_t_1):
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def LayerCount(self) -> int:"""LayerCount { get; } -> int"""
    def __init__(self) -> LayerFilter:...
    def Add(self, layer: str):...
    def GetAt(self, index: int, name: str):...
    def Remove(self, layer: str):...
class LayerIndex(Index, _n_3_t_0, _n_3_t_1):
    def __init__(self) -> LayerIndex:...
    def Compute(self, pLT: _n_0_t_2, record: _n_0_t_3):...
class SpatialFilter(Filter, _n_3_t_0, _n_3_t_1):
    @property
    def ClipSpaceToWorldCoordinateSystemTransform(self) -> _n_1_t_0:"""ClipSpaceToWorldCoordinateSystemTransform { get; } -> Matrix3d"""
    @property
    def Definition(self) -> SpatialFilterDefinition:"""Definition { get; set; } -> SpatialFilterDefinition"""
    @property
    def HasPerspectiveCamera(self) -> bool:"""HasPerspectiveCamera { get; } -> bool"""
    @property
    def Inverted(self) -> bool:"""Inverted { get; set; } -> bool"""
    @property
    def OriginalInverseBlockTransform(self) -> _n_1_t_0:"""OriginalInverseBlockTransform { get; } -> Matrix3d"""
    def __init__(self) -> SpatialFilter:...
    def ClipVolumeIntersectsExtents(self, ext: _n_0_t_4) -> bool:...
    def GetQueryBounds(self, blockReference: _n_0_t_5) -> _n_0_t_4:...
    def GetQueryBounds(self) -> _n_0_t_4:...
    def GetVolume(self) -> SpatialFilterVolume:...
    def SetPerspectiveCamera(self, fromPoint: _n_1_t_1):...
class SpatialFilterDefinition(_n_3_t_5):
    @property
    def BackClip(self) -> float:"""BackClip { get; } -> float"""
    @property
    def Elevation(self) -> float:"""Elevation { get; } -> float"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; } -> bool"""
    @property
    def FrontClip(self) -> float:"""FrontClip { get; } -> float"""
    @property
    def Normal(self) -> _n_1_t_2:"""Normal { get; } -> Vector3d"""
    def __init__(self, pts: _n_1_t_3, normal: _n_1_t_2, elevation: float, frontClip: float, backClip: float, enabled: bool) -> SpatialFilterDefinition:...
    def GetPoints(self) -> _n_1_t_3:...
class SpatialFilterVolume(_n_3_t_5):
    @property
    def FromPoint(self) -> _n_1_t_1:"""FromPoint { get; } -> Point3d"""
    @property
    def ToPoint(self) -> _n_1_t_1:"""ToPoint { get; } -> Point3d"""
    @property
    def UpDirection(self) -> _n_1_t_2:"""UpDirection { get; } -> Vector3d"""
    @property
    def ViewField(self) -> _n_1_t_4:"""ViewField { get; } -> Vector2d"""
    def __init__(self, fromPoint: _n_1_t_1, toPoint: _n_1_t_1, upDir: _n_1_t_2, viewField: _n_1_t_4) -> SpatialFilterVolume:...
class SpatialIndex(Index, _n_3_t_0, _n_3_t_1):
    def __init__(self) -> SpatialIndex:...
