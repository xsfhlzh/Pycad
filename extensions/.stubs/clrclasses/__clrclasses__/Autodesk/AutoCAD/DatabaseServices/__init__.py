import __clrclasses__.Autodesk.AutoCAD.DatabaseServices.Filters as Filters
from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Transparency as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.Colors import EntityColor as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.Colors import EntityColorCollection as _n_0_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices.Filters import SpatialFilter as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices.Filters import LayerFilter as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2d as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import CoordinateSystem3d as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3d as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.Geometry import Plane as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.Geometry import Tolerance as _n_2_t_5
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_2_t_6
from __clrclasses__.Autodesk.AutoCAD.Geometry import Curve3d as _n_2_t_7
from __clrclasses__.Autodesk.AutoCAD.Geometry import Surface as _n_2_t_8
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3dCollection as _n_2_t_9
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3dCollection as _n_2_t_10
from __clrclasses__.Autodesk.AutoCAD.Geometry import Scale3d as _n_2_t_11
from __clrclasses__.Autodesk.AutoCAD.Geometry import NurbCurve3d as _n_2_t_12
from __clrclasses__.Autodesk.AutoCAD.Geometry import DoubleCollection as _n_2_t_13
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector2d as _n_2_t_14
from __clrclasses__.Autodesk.AutoCAD.Geometry import IntPtrCollection as _n_2_t_15
from __clrclasses__.Autodesk.AutoCAD.Geometry import IntegerCollection as _n_2_t_16
from __clrclasses__.Autodesk.AutoCAD.Geometry import KnotParameterizationEnum as _n_2_t_17
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2dCollection as _n_2_t_18
from __clrclasses__.Autodesk.AutoCAD.Geometry import GeoDataLonLatAltInfo as _n_2_t_19
from __clrclasses__.Autodesk.AutoCAD.Geometry import Curve2dCollection as _n_2_t_20
from __clrclasses__.Autodesk.AutoCAD.Geometry import Line2d as _n_2_t_21
from __clrclasses__.Autodesk.AutoCAD.Geometry import Line2dCollection as _n_2_t_22
from __clrclasses__.Autodesk.AutoCAD.Geometry import Scale2d as _n_2_t_23
from __clrclasses__.Autodesk.AutoCAD.Geometry import Int32Collection as _n_2_t_24
from __clrclasses__.Autodesk.AutoCAD.Geometry import KnotCollection as _n_2_t_25
from __clrclasses__.Autodesk.AutoCAD.Geometry import Curve3dCollection as _n_2_t_26
from __clrclasses__.Autodesk.AutoCAD.Geometry import CircularArc2d as _n_2_t_27
from __clrclasses__.Autodesk.AutoCAD.Geometry import CircularArc3d as _n_2_t_28
from __clrclasses__.Autodesk.AutoCAD.Geometry import LineSegment2d as _n_2_t_29
from __clrclasses__.Autodesk.AutoCAD.Geometry import LineSegment3d as _n_2_t_30
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ToneOperatorParameters as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import Glyph as _n_3_t_1
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import Drawable as _n_3_t_2
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import VisualStyleType as _n_3_t_3
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import VisualStyle as _n_3_t_4
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import VisualStyleProperty as _n_3_t_5
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import VisualStyleOperation as _n_3_t_6
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import Mapper as _n_3_t_7
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import HighlightStyle as _n_3_t_8
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import WorldDraw as _n_3_t_9
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ViewportDraw as _n_3_t_10
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import LightAttenuation as _n_3_t_11
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import AttenuationType as _n_3_t_12
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ColorRGB as _n_3_t_13
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import DrawableType as _n_3_t_14
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ShadowParameters as _n_3_t_15
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ShadowType as _n_3_t_16
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialColor as _n_3_t_17
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialMap as _n_3_t_18
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ChannelFlags as _n_3_t_19
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialDiffuseComponent as _n_3_t_20
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import FinalGatherMode as _n_3_t_21
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import GlobalIlluminationMode as _n_3_t_22
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import IlluminationModel as _n_3_t_23
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import LuminanceMode as _n_3_t_24
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import Mode as _n_3_t_25
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialNormalMapComponent as _n_3_t_26
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialOpacityComponent as _n_3_t_27
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialRefractionComponent as _n_3_t_28
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MaterialSpecularComponent as _n_3_t_29
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import DiagnosticBSPMode as _n_3_t_30
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsDiagnosticGridModeParameter as _n_3_t_31
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import DiagnosticMode as _n_3_t_32
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import DiagnosticPhotonMode as _n_3_t_33
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsDoubleRangeParameter as _n_3_t_34
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsBoolParameter as _n_3_t_35
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import FinalGatheringMode as _n_3_t_36
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsTraceParameter as _n_3_t_37
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsIntegerRangeParameter as _n_3_t_38
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsFloatParameter as _n_3_t_39
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import MentalRayRenderSettingsTraitsSamplingParameter as _n_3_t_40
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ShadowMode as _n_3_t_41
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import TileOrder as _n_3_t_42
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import RapidRTFilterType as _n_3_t_43
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import RapidRTLightingMode as _n_3_t_44
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ImageOrg as _n_3_t_45
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ExposureType as _n_3_t_46
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import SkyParameters as _n_3_t_47
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import FontDescriptor as _n_3_t_48
from __clrclasses__.Autodesk.AutoCAD.LayerManager import LayerFilterTree as _n_4_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXClass as _n_5_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import ErrorStatus as _n_5_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_5_t_2
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_5_t_3
from __clrclasses__.Autodesk.AutoCAD.Runtime import Exception as _n_5_t_4
from __clrclasses__.Autodesk.AutoCAD.Runtime import Overrule as _n_5_t_5
from __clrclasses__.Autodesk.AutoCAD.Runtime import IMenuItem as _n_5_t_6
from __clrclasses__.System import IDisposable as _n_6_t_0
from __clrclasses__.System import ICloneable as _n_6_t_1
from __clrclasses__.System import MulticastDelegate as _n_6_t_2
from __clrclasses__.System import IntPtr as _n_6_t_3
from __clrclasses__.System import IAsyncResult as _n_6_t_4
from __clrclasses__.System import AsyncCallback as _n_6_t_5
from __clrclasses__.System import Enum as _n_6_t_6
from __clrclasses__.System import IComparable as _n_6_t_7
from __clrclasses__.System import IFormattable as _n_6_t_8
from __clrclasses__.System import IConvertible as _n_6_t_9
from __clrclasses__.System import Array as _n_6_t_10
from __clrclasses__.System import UInt32 as _n_6_t_11
from __clrclasses__.System import ValueType as _n_6_t_12
from __clrclasses__.System import EventArgs as _n_6_t_13
from __clrclasses__.System import Nullable as _n_6_t_14
from __clrclasses__.System import Attribute as _n_6_t_15
from __clrclasses__.System import Exception as _n_6_t_16
from __clrclasses__.System import EventHandler as _n_6_t_17
from __clrclasses__.System import Char as _n_6_t_18
from __clrclasses__.System import Byte as _n_6_t_19
from __clrclasses__.System import DateTime as _n_6_t_20
from __clrclasses__.System import TimeSpan as _n_6_t_21
from __clrclasses__.System import Guid as _n_6_t_22
from __clrclasses__.System import UInt16 as _n_6_t_23
from __clrclasses__.System import UInt64 as _n_6_t_24
from __clrclasses__.System import Type as _n_6_t_25
from __clrclasses__.System import Uri as _n_6_t_26
from __clrclasses__.System import Tuple as _n_6_t_27
from __clrclasses__.System.Collections import IEnumerable as _n_7_t_0
from __clrclasses__.System.Collections import ArrayList as _n_7_t_1
from __clrclasses__.System.Collections import ICollection as _n_7_t_2
from __clrclasses__.System.Collections import IEnumerator as _n_7_t_3
from __clrclasses__.System.Collections import CollectionBase as _n_7_t_4
from __clrclasses__.System.Collections import IList as _n_7_t_5
from __clrclasses__.System.Collections import IDictionaryEnumerator as _n_7_t_6
from __clrclasses__.System.Collections import IDictionary as _n_7_t_7
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_8_t_0
from __clrclasses__.System.Collections.Generic import List as _n_8_t_1
from __clrclasses__.System.Collections.Generic import ICollection as _n_8_t_2
from __clrclasses__.System.Collections.Generic import IList as _n_8_t_3
from __clrclasses__.System.Collections.Generic import IEnumerator as _n_8_t_4
from __clrclasses__.System.Collections.Specialized import StringCollection as _n_9_t_0
from __clrclasses__.System.Collections.Specialized import StringDictionary as _n_9_t_1
from __clrclasses__.System.ComponentModel import EnumConverter as _n_10_t_0
from __clrclasses__.System.ComponentModel import TypeConverter as _n_10_t_1
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_10_t_2
from __clrclasses__.System.Drawing import Bitmap as _n_11_t_0
from __clrclasses__.System.Drawing import Rectangle as _n_11_t_1
from __clrclasses__.System.Dynamic import IDynamicMetaObjectProvider as _n_12_t_0
from __clrclasses__.System.IO import FileShare as _n_13_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_14_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_14_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_15_t_0
import typing
class AbstractViewTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class AbstractViewTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def AmbientLightColor(self) -> _n_0_t_0:"""AmbientLightColor { get; set; } -> Color"""
    @property
    def BackClipDistance(self) -> float:"""BackClipDistance { get; set; } -> float"""
    @property
    def BackClipEnabled(self) -> bool:"""BackClipEnabled { get; set; } -> bool"""
    @property
    def Background(self) -> ObjectId:"""Background { get; set; } -> ObjectId"""
    @property
    def Brightness(self) -> float:"""Brightness { get; set; } -> float"""
    @property
    def CenterPoint(self) -> _n_2_t_0:"""CenterPoint { get; set; } -> Point2d"""
    @property
    def Contrast(self) -> float:"""Contrast { get; set; } -> float"""
    @property
    def DefaultLightingOn(self) -> bool:"""DefaultLightingOn { get; set; } -> bool"""
    @property
    def DefaultLightingType(self) -> DefaultLightingType:"""DefaultLightingType { get; set; } -> DefaultLightingType"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def FrontClipAtEye(self) -> bool:"""FrontClipAtEye { get; set; } -> bool"""
    @property
    def FrontClipDistance(self) -> float:"""FrontClipDistance { get; set; } -> float"""
    @property
    def FrontClipEnabled(self) -> bool:"""FrontClipEnabled { get; set; } -> bool"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def LensLength(self) -> float:"""LensLength { get; set; } -> float"""
    @property
    def PerspectiveEnabled(self) -> bool:"""PerspectiveEnabled { get; set; } -> bool"""
    @property
    def SunId(self) -> ObjectId:"""SunId { get; } -> ObjectId"""
    @property
    def Target(self) -> _n_2_t_1:"""Target { get; set; } -> Point3d"""
    @property
    def ToneOperatorParameters(self) -> _n_3_t_0:"""ToneOperatorParameters { get; set; } -> ToneOperatorParameters"""
    @property
    def Ucs(self) -> _n_2_t_2:"""Ucs { get; } -> CoordinateSystem3d"""
    @property
    def UcsName(self) -> ObjectId:"""UcsName { get; } -> ObjectId"""
    @property
    def UcsOrthographic(self) -> OrthographicView:"""UcsOrthographic { get; } -> OrthographicView"""
    @property
    def ViewDirection(self) -> _n_2_t_3:"""ViewDirection { get; set; } -> Vector3d"""
    @property
    def ViewOrthographic(self) -> OrthographicView:"""ViewOrthographic { get; } -> OrthographicView"""
    @property
    def ViewTwist(self) -> float:"""ViewTwist { get; set; } -> float"""
    @property
    def VisualStyleId(self) -> ObjectId:"""VisualStyleId { get; set; } -> ObjectId"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
    def SetSun(self, sun: DBObject) -> ObjectId:...
    def SetUcs(self, id: ObjectId):...
    def SetUcs(self, view: OrthographicView):...
    def SetUcs(self, origin: _n_2_t_1, x: _n_2_t_3, y: _n_2_t_3):...
    def SetUcsToWorld(self):...
    def SetViewDirection(self, view: OrthographicView):...
class ActionsToEvaluateCallback(_n_6_t_0):
    def __init__(self) -> ActionsToEvaluateCallback:...
    def NeedsToEvaluate(self, objectId: ObjectId, newStatus: AssocStatus, ownedActionsAlso: bool):...
class AddObjectSnapInfo(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> AddObjectSnapInfo:...
    def BeginInvoke(self, context: ObjectSnapContext, result: ObjectSnapInfo, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, context: ObjectSnapContext, result: ObjectSnapInfo):...
class AlignedDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def DimLinePoint(self) -> _n_2_t_1:"""DimLinePoint { get; set; } -> Point3d"""
    @property
    def Oblique(self) -> float:"""Oblique { get; set; } -> float"""
    @property
    def XLine1Point(self) -> _n_2_t_1:"""XLine1Point { get; set; } -> Point3d"""
    @property
    def XLine2Point(self) -> _n_2_t_1:"""XLine2Point { get; set; } -> Point3d"""
    def __init__(self, line1Point: _n_2_t_1, line2Point: _n_2_t_1, dimensionLinePoint: _n_2_t_1, dimensionText: str, dimensionStyle: ObjectId) -> AlignedDimension:...
    def __init__(self) -> AlignedDimension:...
class AngleConstraint(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Degrees015: int
    Degrees030: int
    Degrees045: int
    Degrees060: int
    Degrees090: int
    DegreesAny: int
    DegreesHorz: int
    value__: int
class AngularConstraint(ExplicitConstraint, _n_6_t_0, _n_6_t_1):
    @property
    def SectorType(self) -> AngularConstraint.AngularSectorType:"""SectorType { get; } -> AngularConstraint.AngularSectorType"""
    def __init__(self, type: AngularConstraint.AngularSectorType) -> AngularConstraint:...
    def __init__(self) -> AngularConstraint:...
    @staticmethod
    def AngleMultiplier() -> float:...
    @staticmethod
    def SetAngleMultiplier(multiplier: float):...
    class AngularSectorType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        AntiParallelAntiClockwise: int
        AntiParallelClockwise: int
        ParallelAntiClockwise: int
        ParallelClockwise: int
        value__: int
class AnnotationScale(ObjectContext, _n_6_t_0, _n_6_t_1):
    @property
    def DrawingUnits(self) -> float:"""DrawingUnits { get; set; } -> float"""
    @property
    def IsTemporaryScale(self) -> bool:"""IsTemporaryScale { get; } -> bool"""
    @property
    def PaperUnits(self) -> float:"""PaperUnits { get; set; } -> float"""
    @property
    def Scale(self) -> float:"""Scale { get; } -> float"""
    def __init__(self) -> AnnotationScale:...
class AnnotationType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BlockRef: int
    FeatureControlFrame: int
    MText: int
    NoAnnotation: int
    value__: int
class AnnotativeStates(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    _False: int
    NotApplicable: int
    _True: int
    value__: int
class ApplicationLoadReasons(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    LoadDisabled: int
    OnAutoCADStartup: int
    OnCommandInvocation: int
    OnLoadRequest: int
    OnProxyDetection: int
    TransparentlyLoadable: int
    value__: int
class Arc(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def Center(self) -> _n_2_t_1:"""Center { get; set; } -> Point3d"""
    @property
    def EndAngle(self) -> float:"""EndAngle { get; set; } -> float"""
    @property
    def Length(self) -> float:"""Length { get; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Radius(self) -> float:"""Radius { get; set; } -> float"""
    @property
    def StartAngle(self) -> float:"""StartAngle { get; set; } -> float"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    @property
    def TotalAngle(self) -> float:"""TotalAngle { get; } -> float"""
    def __init__(self, center: _n_2_t_1, normal: _n_2_t_3, radius: float, startAngle: float, endAngle: float) -> Arc:...
    def __init__(self, center: _n_2_t_1, radius: float, startAngle: float, endAngle: float) -> Arc:...
    def __init__(self) -> Arc:...
class ArcDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def ArcEndParam(self) -> float:"""ArcEndParam { get; set; } -> float"""
    @property
    def ArcPoint(self) -> _n_2_t_1:"""ArcPoint { get; set; } -> Point3d"""
    @property
    def ArcStartParam(self) -> float:"""ArcStartParam { get; set; } -> float"""
    @property
    def ArcSymbolType(self) -> int:"""ArcSymbolType { get; set; } -> int"""
    @property
    def CenterPoint(self) -> _n_2_t_1:"""CenterPoint { get; set; } -> Point3d"""
    @property
    def HasLeader(self) -> bool:"""HasLeader { get; set; } -> bool"""
    @property
    def IsPartial(self) -> bool:"""IsPartial { get; set; } -> bool"""
    @property
    def Leader1Point(self) -> _n_2_t_1:"""Leader1Point { get; set; } -> Point3d"""
    @property
    def Leader2Point(self) -> _n_2_t_1:"""Leader2Point { get; set; } -> Point3d"""
    @property
    def XLine1Point(self) -> _n_2_t_1:"""XLine1Point { get; set; } -> Point3d"""
    @property
    def XLine2Point(self) -> _n_2_t_1:"""XLine2Point { get; set; } -> Point3d"""
    def __init__(self, centerPoint: _n_2_t_1, xLine1Point: _n_2_t_1, xLine2Point: _n_2_t_1, arcPoint: _n_2_t_1, dimensionText: str, dimensionStyle: ObjectId) -> ArcDimension:...
class Assoc2dConstraintCallback(_n_6_t_0):
    def __init__(self, impObj: object, autoDelete: bool) -> Assoc2dConstraintCallback:...
    def __init__(self) -> Assoc2dConstraintCallback:...
    def CanBeRelaxed(self, constraint: ExplicitConstraint) -> bool:...
    def ConstraintDeactivated(self, constraint: ExplicitConstraint, deactivated: bool):...
class Assoc2dConstraintGroup(AssocAction, _n_6_t_0, _n_6_t_1):
    @property
    def ConstrainedGeometries(self) -> _n_6_t_10[ConstrainedGeometry]:"""ConstrainedGeometries { get; } -> Array"""
    @property
    def Constraints(self) -> _n_6_t_10[GeometricalConstraint]:"""Constraints { get; } -> Array"""
    @property
    def GetDOF(self) -> int:"""GetDOF { get; } -> int"""
    @property
    def WorkPlane(self) -> _n_2_t_4:"""WorkPlane { get; set; } -> Plane"""
    def __init__(self, plane: _n_2_t_4) -> Assoc2dConstraintGroup:...
    def Add3PointAngularConstraint(self, consPoint1: ConstrainedPoint, consPoint2: ConstrainedPoint, consPoint3: ConstrainedPoint, sectorType: AngularConstraint.AngularSectorType, valueDependencyId: ObjectId, dimDependencyId: ObjectId) -> ThreePointAngleConstraint:...
    def AddAngularConstraint(self, consLine1: ConstrainedLine, consLine2: ConstrainedLine, sectorType: AngularConstraint.AngularSectorType, valueDependencyId: ObjectId, dimDependencyId: ObjectId) -> AngularConstraint:...
    def AddConstrainedGeometry(self, subentPath: FullSubentityPath) -> ConstrainedGeometry:...
    def AddDistanceConstraint(self, consGeom1: ConstrainedGeometry, consGeom2: ConstrainedGeometry, directionType: DistanceConstraint.DistanceDirectionType, valueDependencyId: ObjectId, dimDependencyId: ObjectId, fixedDirection: _n_2_t_3, directionLine: ConstrainedLine) -> DistanceConstraint:...
    def AddGeometricalConstraint(self, type: GeometricalConstraint.ConstraintType, consGeoms: _n_6_t_10[ConstrainedGeometry]) -> GeometricalConstraint:...
    @staticmethod
    def AddGlobalCallback(callback: Assoc2dConstraintCallback):...
    def AddRadiusDiameterConstraint(self, consGeom: ConstrainedGeometry, type: RadiusDiameterConstraint.RadDiaConstrType, valueDependencyId: ObjectId, dimDependencyId: ObjectId) -> RadiusDiameterConstraint:...
    def AutoConstrain(self, paths: _n_6_t_10[FullSubentityPath], tol: _n_2_t_5, callback: AutoConstrainEvaluationCallback):...
    def ConstraintStatus(self, constraint: GeometricalConstraint) -> Assoc2dConstraintGroup.SolutionStatusType:...
    def DeleteConstrainedGeometry(self, geomDependencyId: ObjectId):...
    def DeleteConstraint(self, geomConst: GeometricalConstraint):...
    def GeometryMirrored(self, geomDependency: AssocGeomDependency):...
    def GeometryStatus(self, consGeom: ConstrainedGeometry) -> Assoc2dConstraintGroup.SolutionStatusType:...
    def GetAllConnectedGeomDependencies(self, srcGeomDependencyIds: ObjectIdCollection) -> ObjectIdCollection:...
    def GetConstrainedGeometry(self, geomDependency: AssocGeomDependency, ptType: ImplicitPointType, defPtIndex: int, bCreateArcLineMid: bool) -> ConstrainedGeometry:...
    def GetConstrainedGeometry(self, geomDependency: AssocGeomDependency) -> ConstrainedGeometry:...
    def GetConstrainedGeometry(self, subentPath: FullSubentityPath, createArcLineMid: bool) -> ConstrainedGeometry:...
    def GetGroupNode(self, nodeId: _n_6_t_11) -> ConstraintGroupNode:...
    @staticmethod
    def GlobalCallback() -> Assoc2dConstraintCallback:...
    def RegenDimensionSystem(self):...
    @staticmethod
    def RemoveGlobalCallback(callback: Assoc2dConstraintCallback):...
    def SolutionStatus(self, alsoCheckForConstraints: bool) -> Assoc2dConstraintGroup.SolutionStatusType:...
    class SolutionStatusType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Inconsistent: int
        NotAvailable: int
        NotEvaluated: int
        OverConstrained: int
        RejectedByClient: int
        UnderConstrained: int
        value__: int
        WellDefined: int
class AssocAction(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ActionBody(self) -> ObjectId:"""ActionBody { get; set; } -> ObjectId"""
    @property
    def CurrentEvaluationCallback(self) -> AssocEvaluationCallback:"""CurrentEvaluationCallback { get; } -> AssocEvaluationCallback"""
    @property
    def IsActionBodyAProxy(self) -> bool:"""IsActionBodyAProxy { get; } -> bool"""
    @property
    def IsActionEvaluationInProgress(self) -> bool:"""IsActionEvaluationInProgress { get; } -> bool"""
    @property
    def OwningNetwork(self) -> ObjectId:"""OwningNetwork { get; } -> ObjectId"""
    @property
    def Status(self) -> AssocStatus:"""Status { get; set; } -> AssocStatus"""
    def __init__(self) -> AssocAction:...
    def AddDependency(self, dependencyId: ObjectId, setThisActionAsOwningAction: bool):...
    def AddMoreObjectsToDeepClone(self, idMap: IdMapping, additionalObjectsToClone: ObjectIdCollection):...
    def AreDependenciesEqual(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool:...
    def AreDependenciesOnTheSameThing(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool:...
    def DependentObjectCloned(self, dependency: AssocDependency, dbObj: DBObject, newObj: DBObject):...
    def DragStatus(self, status: DragStatus):...
    def Evaluate(self, evaluationCallback: AssocEvaluationCallback):...
    def EvaluateDependencies(self):...
    def EvaluateDependency(self, dependency: AssocDependency):...
    def EvaluationPriority(self) -> AssocEvaluationPriority:...
    @staticmethod
    def GetActionBody(actionId: ObjectId) -> ObjectId:...
    @staticmethod
    def GetActionsDependentOnObject(dbObj: DBObject, readDependenciesWanted: bool, writeDependenciesWanted: bool, actionIds: ObjectIdCollection):...
    @staticmethod
    def GetActionsDependentOnObject(dbObj: DBObject, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    def GetDependencies(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    def GetDependentActionsToEvaluate(self, actionsToEvaluateCallback: ActionsToEvaluateCallback):...
    def GetDependentObjects(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    def HasDependencyCachedValue(self, dependency: AssocDependency) -> bool:...
    def IsEqualTo(self, otherAction: AssocAction) -> bool:...
    def IsExternalDependency(self, dependency: AssocDependency) -> bool:...
    def IsOwnedDependency(self, dependency: AssocDependency) -> bool:...
    def IsRelevantDependencyChange(self, dependency: AssocDependency) -> bool:...
    def ObjectThatOwnsNetworkInstance(self) -> ObjectId:...
    def OwnedDependencyStatusChanged(self, ownedDependency: AssocDependency, previousStatus: AssocStatus):...
    def PostProcessAfterDeepClone(self, idMap: IdMapping):...
    def PostProcessAfterDeepCloneCancel(self, idMap: IdMapping):...
    @staticmethod
    def RemoveActionsControllingObject(objID: ObjectId, readOnlyDependencyHandling: int, objectToRedirectReadOnlyDependenciesTo: ObjectId):...
    @staticmethod
    def RemoveActionsControllingObject(objID: ObjectId, readOnlyDependencyHandling: int):...
    @staticmethod
    def RemoveActionsControllingObject(objID: ObjectId):...
    def RemoveAllDependencies(self, alsoEraseThem: bool):...
    def RemoveDependency(self, dependencyId: ObjectId, alsoEraseIt: bool):...
    def SetOwningNetwork(self, networkId: ObjectId, alsoSetAsDatabaseOwner: bool):...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningNetwork: bool, setInOwnedActions: bool):...
    def TransformActionBy(self, transform: _n_2_t_6):...
class AssocActionBody(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def OwnedParams(self) -> ObjectIdCollection:"""OwnedParams { get; } -> ObjectIdCollection"""
    @property
    def OwningNetwork(self) -> ObjectId:"""OwningNetwork { get; } -> ObjectId"""
    @property
    def ParamCount(self) -> int:"""ParamCount { get; } -> int"""
    @property
    def ParentAction(self) -> ObjectId:"""ParentAction { get; } -> ObjectId"""
    @property
    def Status(self) -> AssocStatus:"""Status { get; set; } -> AssocStatus"""
    def __init__(self) -> AssocActionBody:...
    def AddDependency(self, dependencyId: ObjectId, setThisActionAsOwningAction: bool):...
    def AddMoreObjectsToDeepCloneOverride(self, idMap: IdMapping, additionalObjectsToClone: ObjectIdCollection):...
    def AddParam(self, paramId: ObjectId, paramIndex: int):...
    def AreDependenciesEqualOverride(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool:...
    def AreDependenciesOnTheSameThingOverride(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool:...
    @staticmethod
    def CreateActionAndActionBodyAndPostToDatabase(pActionBodyClass: _n_5_t_0, objectId: ObjectId, createdActionId: ObjectId, createdActionBodyId: ObjectId):...
    def currentEvaluationCallback(self) -> AssocEvaluationCallback:...
    def DependentObjectClonedOverride(self, pDependency: AssocDependency, dbObj: DBObject, dbNewObj: DBObject):...
    def DragStatusOverride(self, status: DragStatus):...
    def DwgInFields(self, filer: DwgFiler) -> _n_5_t_1:...
    def DwgOutFields(self, filer: DwgFiler) -> _n_5_t_1:...
    def DxfInFields(self, filer: DxfFiler) -> _n_5_t_1:...
    def DxfOutFields(self, filer: DxfFiler) -> _n_5_t_1:...
    def EvaluateDependencies(self):...
    def EvaluateDependencyOverride(self, dependency: AssocDependency) -> bool:...
    def EvaluateOverride(self):...
    def EvaluationPriorityOverride(self, priority: AssocEvaluationPriority):...
    @staticmethod
    def GetActionBodiesOnObject(pObject: DBObject, ignoreInternalActions: bool, ignoreSuppressedActions: bool, creationActionBodyId: ObjectId, modificationActionBodyIds: ObjectIdCollection, readOnlyActionBodyIds: ObjectIdCollection):...
    def GetDependencies(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    def GetDependenciesOverride(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    def GetDependentActionsToEvaluateOverride(self, actionsToEvaluateCallback: ActionsToEvaluateCallback):...
    def GetDependentObjectsOverride(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    @staticmethod
    def GetParentAction(actionBodyId: ObjectId) -> ObjectId:...
    def GetValueParam(self, paramName: str, paramIndex: int) -> AssocActionBody.ValueParam:...
    def GetValueParam(self, paramName: str) -> AssocActionBody.ValueParam:...
    def GetValueParamArray(self, paramName: str) -> _n_6_t_10[AssocActionBody.ValueParam]:...
    def GetValueParamUnitType(self, paramName: str) -> UnitType:...
    def HasAnyErasedOrBrokenDependencies(self) -> bool:...
    def HasDependencyCachedValueOverride(self, dependency: AssocDependency) -> bool:...
    def IsActionEvaluationInProgress(self) -> bool:...
    def IsEqualToOverride(self, otherAction: AssocAction) -> bool:...
    def IsExternalDependencyOverride(self, dependency: AssocDependency) -> bool:...
    def IsOwnedDependencyOverride(self, dependency: AssocDependency) -> bool:...
    def IsRelevantDependencyChangeOverride(self, dependency: AssocDependency) -> bool:...
    def OwnedDependencyStatusChangedOverride(self, ownedDependency: AssocDependency, previousStatus: AssocStatus):...
    def OwnedValueParamNames(self) -> _n_6_t_10[str]:...
    def ParamAtIndex(self, paramIndex: int) -> ObjectId:...
    def ParamAtName(self, paramName: str, index: int) -> ObjectId:...
    def ParamAtName(self, paramName: str) -> ObjectId:...
    def ParamsAtName(self, paramName: str) -> ObjectIdCollection:...
    def PostProcessAfterDeepCloneCancelOverride(self, idMap: IdMapping):...
    def PostProcessAfterDeepCloneOverride(self, idMap: IdMapping):...
    def RemoveAllDependencies(self, alsoEraseThem: bool):...
    def RemoveAllDependenciesOverride(self, alsoEraseThem: bool):...
    def RemoveAllParams(self, alsoEraseThem: bool):...
    def RemoveDependency(self, dependencyId: ObjectId, alsoEraseIt: bool):...
    def RemoveParam(self, paramId: ObjectId, alsoEraseIt: bool):...
    def RemoveValueParam(self, paramName: str):...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningNetwork: bool, setInOwnedActions: bool):...
    def SetValueParam(self, paramName: str, param: AssocActionBody.ValueParam, silentMode: bool) -> str:...
    def SetValueParam(self, paramName: str, param: AssocActionBody.ValueParam, silentMode: bool, paramIndex: int) -> str:...
    def SetValueParamArray(self, paramName: str, valueParams: _n_6_t_10[AssocActionBody.ValueParam], silentMode: bool) -> _n_6_t_10[str]:...
    def SetValueParamUnitType(self, paramName: str, unitType: UnitType):...
    def TransformActionByOverride(self, A_0: _n_2_t_6):...
    def ValueParamInputVariables(self, paramName: str) -> ObjectIdCollection:...
    class ValueParam(_n_6_t_12):
        @property
        def EvaluatorId(self) -> str:"""EvaluatorId { get; set; } -> str"""
        @property
        def Expression(self) -> str:"""Expression { get; set; } -> str"""
        @property
        def Value(self) -> ResultBuffer:"""Value { get; set; } -> ResultBuffer"""
        def __init__(self, expression: str, evaluatorId: str, value: ResultBuffer) -> AssocActionBody.ValueParam:...
class AssocActionParam(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ParentAction(self) -> ObjectId:"""ParentAction { get; } -> ObjectId"""
    def __init__(self) -> AssocActionParam:...
    def DetachDependencies(self):...
    def GetDependencies(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    def MakeParamConstant(self):...
    def MakeParamEmpty(self, alsoEraseOwnedObjects: bool):...
    def TransformConstantGeometry(self, transform: _n_2_t_6):...
class AssocArray(object):
    @property
    def EntityId(self) -> ObjectId:"""EntityId { get; } -> ObjectId"""
    @property
    def SourceEntities(self) -> ObjectIdCollection:"""SourceEntities { get; } -> ObjectIdCollection"""
    def AddSourceEntity(self, sourceEntity: ObjectId, basePoint: _n_2_t_1):...
    @staticmethod
    def CreateArray(sourceEntities: ObjectIdCollection, basePoint: VertexRef, parameters: AssocArrayParameters) -> AssocArray:...
    def DeleteItem(self, index: ItemLocator, bErase: bool):...
    @staticmethod
    def Explode(entity: ObjectId) -> ObjectIdCollection:...
    @staticmethod
    def GetAssociativeArray(entity: ObjectId) -> AssocArray:...
    @staticmethod
    def getItemLocators(subPaths: _n_6_t_10[FullSubentityPath]) -> _n_6_t_10[ItemLocator]:...
    def getItems(self, skipErased: bool) -> _n_6_t_10[ItemLocator]:...
    def GetItemTransform(self, index: ItemLocator) -> _n_2_t_6:...
    def GetParameters(self) -> AssocArrayParameters:...
    @staticmethod
    def IsAssociativeArray(entity: ObjectId) -> bool:...
    def IsErased(self, index: ItemLocator) -> bool:...
    def RemoveSourceEntity(self, sourceEntity: ObjectId):...
    def ReplaceItems(self, indices: _n_6_t_10[ItemLocator], substEntities: ObjectIdCollection, basePoint: VertexRef):...
    def ResetItems(self):...
    def TransformItemBy(self, index: ItemLocator, transform: _n_2_t_6):...
class AssocArrayCommonParameters(AssocArrayParameters, _n_6_t_0, _n_6_t_1):
    @property
    def BaseNormal(self) -> _n_2_t_3:"""BaseNormal { get; set; } -> Vector3d"""
    @property
    def BasePlane(self) -> FaceRef:"""BasePlane { get; set; } -> FaceRef"""
    @property
    def BasePoint(self) -> VertexRef:"""BasePoint { get; set; } -> VertexRef"""
    @property
    def LevelCount(self) -> int:"""LevelCount { get; set; } -> int"""
    @property
    def LevelSpacing(self) -> float:"""LevelSpacing { get; set; } -> float"""
    @property
    def RowCount(self) -> int:"""RowCount { get; set; } -> int"""
    @property
    def RowElevation(self) -> float:"""RowElevation { get; set; } -> float"""
    @property
    def RowSpacing(self) -> float:"""RowSpacing { get; set; } -> float"""
    def GetLevelCount(self, expression: str, evaluatorId: str) -> int:...
    def GetLevelSpacing(self, expression: str, evaluatorId: str) -> float:...
    def GetRowCount(self, expression: str, evaluatorId: str) -> int:...
    def GetRowElevation(self, expression: str, evaluatorId: str) -> float:...
    def GetRowSpacing(self, expression: str, evaluatorId: str) -> float:...
    def SetLevelCount(self, count: int, expression: str, evaluatorId: str):...
    def SetLevelSpacing(self, spacing: float, expression: str, evaluatorId: str):...
    def SetRowCount(self, count: int, expression: str, evaluatorId: str):...
    def SetRowElevation(self, value: float, expression: str, evaluatorId: str):...
    def SetRowSpacing(self, spacing: float, expression: str, evaluatorId: str):...
class AssocArrayParameters(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def Owner(self) -> AssocArray:"""Owner { get; } -> AssocArray"""
    def Commit(self):...
class AssocArrayPathParameters(AssocArrayCommonParameters, _n_6_t_0, _n_6_t_1):
    @property
    def AlignItems(self) -> bool:"""AlignItems { get; set; } -> bool"""
    @property
    def EndOffset(self) -> float:"""EndOffset { get; set; } -> float"""
    @property
    def ItemCount(self) -> int:"""ItemCount { get; set; } -> int"""
    @property
    def ItemSpacing(self) -> float:"""ItemSpacing { get; set; } -> float"""
    @property
    def Method(self) -> AssocArrayPathParameters.MethodType:"""Method { get; set; } -> AssocArrayPathParameters.MethodType"""
    @property
    def Path(self) -> EdgeRef:"""Path { get; set; } -> EdgeRef"""
    @property
    def PathDirection(self) -> bool:"""PathDirection { set; } -> bool"""
    @property
    def StartOffset(self) -> float:"""StartOffset { get; set; } -> float"""
    def __init__(self, itemSpacing: float, rowSpacing: float, levelSpacing: float, itemCount: int, rowCount: int, levelCount: int, rowElevation: float) -> AssocArrayPathParameters:...
    def __init__(self) -> AssocArrayPathParameters:...
    def GetEndOffset(self, expression: str, evaluatorId: str) -> float:...
    def GetItemCount(self, expression: str, evaluatorId: str) -> int:...
    def GetItemSpacing(self, expression: str, evaluatorId: str) -> float:...
    def GetStartOffset(self, expression: str, evaluatorId: str) -> float:...
    def SetEndOffset(self, offset: float, expression: str, evaluatorId: str):...
    def SetItemCount(self, count: int, expression: str, evaluatorId: str):...
    def SetItemSpacing(self, spacing: float, expression: str, evaluatorId: str):...
    def SetStartOffset(self, offset: float, expression: str, evaluatorId: str):...
    class MethodType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Divide: int
        Measure: int
        value__: int
class AssocArrayPolarParameters(AssocArrayCommonParameters, _n_6_t_0, _n_6_t_1):
    @property
    def AngleBetweenItems(self) -> float:"""AngleBetweenItems { get; set; } -> float"""
    @property
    def Direction(self) -> AssocArrayPolarParameters.ArcDirection:"""Direction { get; set; } -> AssocArrayPolarParameters.ArcDirection"""
    @property
    def FillAngle(self) -> float:"""FillAngle { get; set; } -> float"""
    @property
    def ItemCount(self) -> int:"""ItemCount { get; set; } -> int"""
    @property
    def Radius(self) -> float:"""Radius { get; set; } -> float"""
    @property
    def RotateItems(self) -> bool:"""RotateItems { get; set; } -> bool"""
    @property
    def StartAngle(self) -> float:"""StartAngle { get; set; } -> float"""
    def __init__(self, angle: float, rowSpacing: float, levelSpacing: float, itemCount: int, rowCount: int, levelCount: int, rowElevation: float) -> AssocArrayPolarParameters:...
    def __init__(self) -> AssocArrayPolarParameters:...
    def GetAngleBetweenItems(self, expression: str, evaluatorId: str) -> float:...
    def GetFillAngle(self, expression: str, evaluatorId: str) -> float:...
    def GetItemCount(self, expression: str, evaluatorId: str) -> int:...
    def GetRadius(self, expression: str, evaluatorId: str) -> float:...
    def GetStartAngle(self, expression: str, evaluatorId: str) -> float:...
    def SetAngleBetweenItems(self, val: float, expression: str, evaluatorId: str):...
    def SetFillAngle(self, val: float, expression: str, evaluatorId: str):...
    def SetItemCount(self, count: int, expression: str, evaluatorId: str):...
    def SetRadius(self, val: float, expression: str, evaluatorId: str):...
    def SetStartAngle(self, val: float, expression: str, evaluatorId: str):...
    class ArcDirection(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Clockwise: int
        CounterClockwise: int
        value__: int
class AssocArrayRectangularParameters(AssocArrayCommonParameters, _n_6_t_0, _n_6_t_1):
    @property
    def AxesAngle(self) -> float:"""AxesAngle { get; set; } -> float"""
    @property
    def ColumnCount(self) -> int:"""ColumnCount { get; set; } -> int"""
    @property
    def ColumnSpacing(self) -> float:"""ColumnSpacing { get; set; } -> float"""
    @property
    def XAxisDirection(self) -> _n_2_t_3:"""XAxisDirection { get; set; } -> Vector3d"""
    @property
    def YAxisDirection(self) -> _n_2_t_3:"""YAxisDirection { get; set; } -> Vector3d"""
    def __init__(self, columnSpacing: float, rowSpacing: float, levelSpacing: float, columnCount: int, rowCount: int, levelCount: int, rowElevation: float, axesAngle: float) -> AssocArrayRectangularParameters:...
    def __init__(self) -> AssocArrayRectangularParameters:...
    def GetAxesAngle(self, expression: str, evaluatorId: str) -> float:...
    def GetColumnCount(self, expression: str, evaluatorId: str) -> int:...
    def GetColumnSpacing(self, expression: str, evaluatorId: str) -> float:...
    def SetAxesAngle(self, val: float, expression: str, evaluatorId: str):...
    def SetColumnCount(self, count: int, expression: str, evaluatorId: str):...
    def SetColumnSpacing(self, spacing: float, expression: str, evaluatorId: str):...
class AssocAsmBodyActionParam(AssocActionParam, _n_6_t_0, _n_6_t_1):
    @property
    def DependentOnCompoundObject(self) -> CompoundObjectId:"""DependentOnCompoundObject { get; } -> CompoundObjectId"""
    def __init__(self) -> AssocAsmBodyActionParam:...
    def SetBody(self, bodyId: ObjectId, isReadDep: bool, isWriteDep: bool):...
    def SetBody(self, entity: Entity, isReadDep: bool, isWriteDep: bool):...
class AssocBlendSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def BlendOption(self) -> BlendOptions:"""BlendOption { get; set; } -> BlendOptions"""
    @property
    def EndEdgeBulge(self) -> float:"""EndEdgeBulge { get; set; } -> float"""
    @property
    def EndEdgeContinuity(self) -> int:"""EndEdgeContinuity { get; set; } -> int"""
    @property
    def StartEdgeBulge(self) -> float:"""StartEdgeBulge { get; set; } -> float"""
    @property
    def StartEdgeContinuity(self) -> int:"""StartEdgeContinuity { get; set; } -> int"""
    def __init__(self) -> AssocBlendSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, startProfile: LoftProfile, endProfile: LoftProfile, blendOptions: BlendOptions, enable: bool) -> ObjectId:...
    def GetContinuityGripPoints(self, startEdgePt: _n_2_t_1, endEdgePt: _n_2_t_1):...
    def GetEndEdgeBulge(self, expression: str, evaluatorId: str) -> float:...
    def GetEndEdgeContinuity(self, expression: str, evaluatorId: str) -> int:...
    def GetProfiles(self, startProfile: LoftProfile, endProfile: LoftProfile):...
    def GetStartEdgeBulge(self, expression: str, evaluatorId: str) -> float:...
    def GetStartEdgeContinuity(self, expression: str, evaluatorId: str) -> int:...
    def SetEndEdgeBulge(self, value: float, expression: str, evaluatorId: str):...
    def SetEndEdgeContinuity(self, value: int, expression: str, evaluatorId: str):...
    def SetStartEdgeBulge(self, value: float, expression: str, evaluatorId: str):...
    def SetStartEdgeContinuity(self, value: int, expression: str, evaluatorId: str):...
class AssocCompoundActionParam(AssocActionParam, _n_6_t_0, _n_6_t_1, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> ObjectId:"""Item { get; } -> ObjectId"""
    @property
    def OwnedParams(self) -> ObjectIdCollection:"""OwnedParams { get; } -> ObjectIdCollection"""
    @property
    def ParamCount(self) -> int:"""ParamCount { get; } -> int"""
    def __init__(self) -> AssocCompoundActionParam:...
    def AddParam(self, paramId: ObjectId) -> int:...
    def ParamAtIndex(self, index: int) -> ObjectId:...
    def ParamAtName(self, paramName: str, index: int) -> ObjectId:...
    def ParamAtName(self, paramName: str) -> ObjectId:...
    def ParamsAtName(self, paramName: str) -> ObjectIdCollection:...
    def RemoveAllParams(self, alsoEraseThem: bool):...
    def RemoveParam(self, paramId: ObjectId, alsoEraseIt: bool):...
class AssocConstraintType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Angle0AssocConstraintType: int
    Angle1AssocConstraintType: int
    Angle2AssocConstraintType: int
    Angle3AssocConstraintType: int
    DiameterAssocConstraintType: int
    DistanceAssocConstraintType: int
    HorizontalDistanceAssocConstraintType: int
    NoneAssocConstraintType: int
    RadiusAssocConstraintType: int
    value__: int
    VerticalDistanceAssocConstraintType: int
class AssocDependency(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def CurrentEvaluationCallback(self) -> AssocEvaluationCallback:"""CurrentEvaluationCallback { get; } -> AssocEvaluationCallback"""
    @property
    def DependencyBody(self) -> ObjectId:"""DependencyBody { get; set; } -> ObjectId"""
    @property
    def DependentOnCompoundObject(self) -> CompoundObjectId:"""DependentOnCompoundObject { get; } -> CompoundObjectId"""
    @property
    def DependentOnObject(self) -> ObjectId:"""DependentOnObject { get; } -> ObjectId"""
    @property
    def DependentOnObjectStatus(self) -> _n_5_t_1:"""DependentOnObjectStatus { get; } -> ErrorStatus"""
    @property
    def HasCachedValue(self) -> bool:"""HasCachedValue { get; } -> bool"""
    @property
    def IsActionEvaluationInProgress(self) -> bool:"""IsActionEvaluationInProgress { get; } -> bool"""
    @property
    def IsAttachedToObject(self) -> bool:"""IsAttachedToObject { get; } -> bool"""
    @property
    def IsDelegatingToOwningAction(self) -> bool:"""IsDelegatingToOwningAction { get; set; } -> bool"""
    @property
    def IsDependentOnCompoundObject(self) -> bool:"""IsDependentOnCompoundObject { get; } -> bool"""
    @property
    def IsDependentOnObjectReadOnly(self) -> bool:"""IsDependentOnObjectReadOnly { get; } -> bool"""
    @property
    def IsObjectStateDependent(self) -> bool:"""IsObjectStateDependent { get; set; } -> bool"""
    @property
    def IsReadDependency(self) -> bool:"""IsReadDependency { get; set; } -> bool"""
    @property
    def IsRelevantChange(self) -> bool:"""IsRelevantChange { get; } -> bool"""
    @property
    def IsWriteDependency(self) -> bool:"""IsWriteDependency { get; set; } -> bool"""
    @property
    def NextDependencyOnObject(self) -> ObjectId:"""NextDependencyOnObject { get; } -> ObjectId"""
    @property
    def Order(self) -> int:"""Order { get; set; } -> int"""
    @property
    def OwningAction(self) -> ObjectId:"""OwningAction { get; set; } -> ObjectId"""
    @property
    def PrevDependencyOnObject(self) -> ObjectId:"""PrevDependencyOnObject { get; } -> ObjectId"""
    @property
    def Status(self) -> AssocStatus:"""Status { get; set; } -> AssocStatus"""
    def __init__(self) -> AssocDependency:...
    def AttachToObject(self, compoundId: CompoundObjectId):...
    def DetachFromObject(self):...
    def Evaluate(self):...
    @staticmethod
    def GetDependenciesOnObject(dbObj: DBObject, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection:...
    @staticmethod
    def GetFirstDependencyOnObject(dbObj: DBObject) -> ObjectId:...
    def IsDependentOnTheSameThingAs(self, otherDependency: AssocDependency) -> bool:...
    def IsEqualTo(self, otherDependency: AssocDependency) -> bool:...
    @staticmethod
    def NotifyDependenciesOnObject(dbObj: DBObject, newStatus: AssocStatus):...
    def SetDependentOnObject(self, compoundId: CompoundObjectId):...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningNetwork: bool):...
    def UpdateDependentOnObject(self):...
class AssocDependencyBody(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def DependentOnObject(self) -> ObjectId:"""DependentOnObject { get; } -> ObjectId"""
    @property
    def HasCachedValueOverride(self) -> bool:"""HasCachedValueOverride { get; } -> bool"""
    @property
    def IsActionEvaluationInProgress(self) -> bool:"""IsActionEvaluationInProgress { get; } -> bool"""
    @property
    def IsAttachedToObject(self) -> bool:"""IsAttachedToObject { get; } -> bool"""
    @property
    def IsRelevantChangeOverride(self) -> bool:"""IsRelevantChangeOverride { get; } -> bool"""
    @property
    def OwningAction(self) -> ObjectId:"""OwningAction { get; } -> ObjectId"""
    @property
    def ParentDependency(self) -> ObjectId:"""ParentDependency { get; } -> ObjectId"""
    @property
    def Status(self) -> AssocStatus:"""Status { get; } -> AssocStatus"""
    def __init__(self) -> AssocDependencyBody:...
    def ClonedOverride(self, dbObj: DBObject, newObj: DBObject):...
    def currentEvaluationCallback(self) -> AssocEvaluationCallback:...
    def DwgInFields(self, filer: DwgFiler) -> _n_5_t_1:...
    def DwgOutFields(self, filer: DwgFiler) -> _n_5_t_1:...
    def DxfInFields(self, filer: DxfFiler) -> _n_5_t_1:...
    def DxfOutFields(self, filer: DxfFiler) -> _n_5_t_1:...
    def ErasedOverride(self, dbObj: DBObject, IsErasing: int):...
    def EvaluateOverride(self):...
    def IsDependentOnTheSameThingAsOverride(self, otherDependency: AssocDependency) -> bool:...
    def IsEqualToOverride(self, otherDependency: AssocDependency) -> bool:...
    def ModifiedOverride(self, dbObj: DBObject):...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningAction: bool):...
    def UpdateDependentOnObjectOverride(self):...
class AssocDependencyPE(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocDependencyPE:...
    def AllowsDependencies(self, dbObj: DBObject, isWriteDependency: bool) -> bool:...
class AssocDimDependencyBody(AssocDimDependencyBodyBase, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocDimDependencyBody:...
    @staticmethod
    def CreateAndPostToDatabase(dimId: ObjectId, dimDepId: ObjectId, dimDepBodyId: ObjectId):...
class AssocDimDependencyBodyBase(AssocDependencyBody, _n_6_t_0, _n_6_t_1):
    @property
    def ConstrainedGeoms(self) -> _n_6_t_10[ConstrainedGeometry]:"""ConstrainedGeoms { get; } -> Array"""
    @property
    def EntityMeasurementOverride(self) -> float:"""EntityMeasurementOverride { get; } -> float"""
    @property
    def EntityTextOverride(self) -> str:"""EntityTextOverride { get; set; } -> str"""
    @property
    def GetCurrentlyUsedEntityNameFormat(self) -> int:"""GetCurrentlyUsedEntityNameFormat { get; } -> int"""
    @property
    def GetMeasuredValue(self) -> float:"""GetMeasuredValue { get; } -> float"""
    @property
    def IsConstraintActive(self) -> bool:"""IsConstraintActive { get; } -> bool"""
    @property
    def IsEntityAttachmentChangedOverride(self) -> bool:"""IsEntityAttachmentChangedOverride { get; } -> bool"""
    @property
    def IsReferenceOnly(self) -> bool:"""IsReferenceOnly { set; } -> bool"""
    @property
    def SubentityConstrainedGeoms(self) -> _n_6_t_10[FullSubentityPath]:"""SubentityConstrainedGeoms { get; } -> Array"""
    @property
    def Variable(self) -> ObjectId:"""Variable { get; } -> ObjectId"""
    def __init__(self) -> AssocDimDependencyBodyBase:...
    def ComposeEntityText(self, requiredNameFormat: int) -> str:...
    def Constraint(self) -> ExplicitConstraint:...
    def DeactivateConstraint(self):...
    def DragStatus(self, status: DragStatus):...
    def EntityAttachmentPointMoved(self, newAttachedGeometries: _n_6_t_10[SubentityGeometry], measurement: float):...
    @staticmethod
    def FormatToCurrentPrecision(expression: str, isAngular: bool) -> str:...
    def GetEntityNameAndExpression(self, name: str, expression: str):...
    @staticmethod
    def GetEraseDimensionIfDependencyIsErased() -> bool:...
    @staticmethod
    def GetFromEntity(entityId: ObjectId) -> ObjectId:...
    @staticmethod
    def GetNameAndExpressionFromEntityText(entityText: str, useMeasurementIfNoText: bool, measurement: float, isAngular: bool, name: str, expression: str):...
    def GetSubentityGeoms(self, distanceDirection: _n_2_t_3) -> _n_6_t_10[SubentityGeometry]:...
    def GetVariableNameAndExpression(self, name: str, expression: str, value: str):...
    def ReactivateConstraint(self):...
    def SetEntityNameAndExpression(self, name: str, expression: str, value: str):...
    @staticmethod
    def SetEraseDimensionIfDependencyIsErased(yesNo: bool) -> bool:...
    def SetNameAndExpression(self, name: str, expression: str):...
    def SetVariableNameAndExpression(self, name: str, expression: str):...
    def SetVariableValueToMeasuredValue(self):...
    def SubErase(self, erasing: int):...
    def ValidateEntityText(self, entityTextToValidate: str) -> str:...
    class NotificationIgnorerDotNet(object):
        def __init__(self) -> AssocDimDependencyBodyBase.NotificationIgnorerDotNet:...
        @staticmethod
        def IsIgnoringNotifications() -> bool:...
class AssocDraggingState(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    FirstSampleAssocDraggingState: int
    IntermediateSampleAssocDraggingState: int
    LastSampleAssocDraggingState: int
    NotDraggingAssocDraggingState: int
    value__: int
class AssocEdgeActionParam(AssocActionParam, _n_6_t_0, _n_6_t_1):
    @property
    def DependentOnCompoundObject(self) -> CompoundObjectId:"""DependentOnCompoundObject { get; } -> CompoundObjectId"""
    def __init__(self) -> AssocEdgeActionParam:...
    def GetEdgeRef(self) -> _n_6_t_10[EdgeRef]:...
    def SetEdgeRef(self, edgeRef: EdgeRef, isReadDep: bool, isWriteDep: bool):...
    def SetEdgeRef(self, edgeRef: EdgeRef):...
class AssocEdgeChamferActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def BaseDistance(self) -> float:"""BaseDistance { get; set; } -> float"""
    @property
    def OtherDistance(self) -> float:"""OtherDistance { get; set; } -> float"""
    def __init__(self) -> AssocEdgeChamferActionBody:...
    @staticmethod
    def CreateInstance(chamferEdges: _n_6_t_10[FullSubentityPath], baseFace: SubentityId, baseDistance: float, otherDistance: float, enable: bool) -> ObjectId:...
    def GetBaseDistance(self, expression: str, evaluatorId: str) -> float:...
    def GetOtherDistance(self, expression: str, evaluatorId: str) -> float:...
    def SetBaseDistance(self, distance: float, expression: str, evaluatorId: str):...
    def SetOtherDistance(self, distance: float, expression: str, evaluatorId: str):...
class AssocEdgeFilletActionBody(AssocSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def Radius(self) -> float:"""Radius { get; set; } -> float"""
    def __init__(self) -> AssocEdgeFilletActionBody:...
    @staticmethod
    def CreateInstance(filletEdges: _n_6_t_10[FullSubentityPath], radius: float, enable: bool) -> ObjectId:...
    def GetRadius(self, expression: str, evaluatorId: str) -> float:...
    def SetRadius(self, radius: float, expression: str, evaluatorId: str):...
class AssocEvaluationCallback(_n_6_t_0):
    def __init__(self) -> AssocEvaluationCallback:...
    def BeginActionEvaluation(self, action: AssocAction):...
    def BeginActionEvaluationUsingObject(self, pAction: AssocAction, objectId: ObjectId, objectIsGoingToBeUsed: bool, objectIsGoingToBeModified: bool, substituteObject: DBObject):...
    def CancelActionEvaluation(self) -> bool:...
    def DraggingState(self) -> AssocDraggingState:...
    def EndActionEvaluation(self, action: AssocAction):...
    def EndActionEvaluationUsingObject(self, action: AssocAction, objectId: ObjectId, obj: DBObject):...
    def EvaluationMode(self) -> AssocEvaluationMode:...
    def GetTransformationType(self) -> AssocTransformationType:...
    def SetActionEvaluationErrorStatus(self, action: AssocAction, errorStatus: _n_5_t_1, objectId: ObjectId, obj: DBObject, errorInfo: _n_6_t_3):...
    def SetActionEvaluationErrorStatus(self, action: AssocAction, errorStatus: _n_5_t_1):...
class AssocEvaluationMode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ModifyActionAssocEvaluationMode: int
    ModifyObjectsAssocEvaluationMode: int
    value__: int
class AssocEvaluationPriority(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CanBeEvaluatedAssocEvaluationPriority: int
    CannotBeEvaluatedAssocEvaluationPriority: int
    CannotDermineAssocEvaluationPriority: int
    value__: int
class AssocExtendSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def Distance(self) -> float:"""Distance { get; set; } -> float"""
    def __init__(self) -> AssocExtendSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, extendEdges: _n_6_t_10[EdgeRef], distance: float, extendOption: Surface.EdgeExtensionType, enabled: bool) -> ObjectId:...
    def GetDistance(self, expression: str, evaluatorId: str) -> float:...
    def SetDistance(self, distance: float, expression: str, evaluatorId: str):...
class AssocExtrudedSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def TaperAngle(self) -> float:"""TaperAngle { get; set; } -> float"""
    def __init__(self) -> AssocExtrudedSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputPath: PathRef, directionVec: _n_2_t_3, sweepOptions: SweepOptions, enable: bool) -> ObjectId:...
    def GetHeight(self, expression: str, evaluatorId: str) -> float:...
    def GetTaperAngle(self, expression: str, evaluatorId: str) -> float:...
    def SetHeight(self, height: float, expression: str, evaluatorId: str):...
    def SetTaperAngle(self, taperAngle: float, expression: str, evaluatorId: str):...
class AssocFaceActionParam(AssocActionParam, _n_6_t_0, _n_6_t_1):
    @property
    def DependentOnCompoundObject(self) -> CompoundObjectId:"""DependentOnCompoundObject { get; } -> CompoundObjectId"""
    def __init__(self) -> AssocFaceActionParam:...
    def GetFaceRef(self) -> _n_6_t_10[FaceRef]:...
    def SetFaceRef(self, faceRef: FaceRef, isReadDependency: bool, isWriteDependency: bool):...
    def SetFaceRef(self, faceRef: FaceRef):...
class AssocFilletSurfaceActionBody(AssocSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def Radius(self) -> float:"""Radius { get; set; } -> float"""
    @property
    def TrimMode(self) -> FilletTrimMode:"""TrimMode { get; set; } -> FilletTrimMode"""
    def __init__(self) -> AssocFilletSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputSurfaceId1: ObjectId, pickPt1: _n_2_t_1, inputSurfaceId2: ObjectId, pickPt2: _n_2_t_1, radius: float, trimMode: FilletTrimMode, viewDir: _n_2_t_3, bEnable: bool) -> ObjectId:...
    def GetFilletHandleData(self, pt: _n_2_t_1, dir: _n_2_t_3, cenPt: _n_2_t_1, normal: _n_2_t_3):...
    def GetHintPoints(self) -> _n_6_t_10[_n_2_t_1]:...
    def GetRadius(self, expression: str, evaluatorId: str) -> float:...
    def SetHintPoints(self, hintPoints: _n_6_t_10[_n_2_t_1], viewDir: _n_2_t_3):...
    def SetRadius(self, radius: float, expression: str, evaluatorId: str):...
class AssocGeomDependency(AssocDependency, _n_6_t_0, _n_6_t_1):
    @property
    def EdgeSubentityGeometry(self) -> _n_6_t_10[_n_2_t_7]:"""EdgeSubentityGeometry { get; set; } -> Array"""
    @property
    def FaceSubentityGeometry(self) -> _n_6_t_10[_n_2_t_8]:"""FaceSubentityGeometry { get; set; } -> Array"""
    @property
    def IsCachingSubentityGeometry(self) -> bool:"""IsCachingSubentityGeometry { get; set; } -> bool"""
    @property
    def PersistentSubentId(self) -> AssocPersSubentityId:"""PersistentSubentId { get; } -> AssocPersSubentityId"""
    @property
    def Subentity(self) -> SubentityId:"""Subentity { set; } -> SubentityId"""
    @property
    def SubentityType(self) -> _n_6_t_11:"""SubentityType { get; } -> UInt32"""
    @property
    def TransientSubentCount(self) -> int:"""TransientSubentCount { get; } -> int"""
    @property
    def TransientSubentIds(self) -> _n_6_t_10[SubentityId]:"""TransientSubentIds { get; } -> Array"""
    @property
    def VertexSubentityGeometry(self) -> _n_6_t_10[_n_2_t_1]:"""VertexSubentityGeometry { get; set; } -> Array"""
    def __init__(self) -> AssocGeomDependency:...
    def DependentOnObjectMirrored(self):...
    @staticmethod
    def RedirectToAnotherSubentity(oldObjectId: ObjectId, oldSubentId: SubentityId, newObjectId: ObjectId, newSubentId: SubentityId):...
class AssocGlobalUtility(object):
    def __init__(self) -> AssocGlobalUtility:...
    @staticmethod
    def EvaluationRequestSeverityLevel(status: AssocStatus) -> int:...
    @staticmethod
    def IsDraggingProvidingSubstituteObjects(evaluationCallback: AssocEvaluationCallback) -> bool:...
    @staticmethod
    def IsEvaluationRequest(status: AssocStatus) -> bool:...
    @staticmethod
    def IsToBeSkipped(status: AssocStatus) -> bool:...
class AssocLoftedSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocLoftedSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, crossSections: _n_6_t_10[SubentRef], guideCurves: _n_6_t_10[PathRef], pathCurve: PathRef, loftOptions: LoftOptions, continuityArray: _n_6_t_10[int], bulgeArray: _n_6_t_10[float], bEnable: bool) -> ObjectId:...
    def GetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType, expression: str, evaluatorId: str) -> float:...
    def GetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType) -> float:...
    def GetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType, expression: str, evaluatorId: str) -> int:...
    def GetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType) -> int:...
    def SetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: float, expression: str, evaluatorId: str):...
    def SetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: float):...
    def SetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: int, expression: str, evaluatorId: str):...
    def SetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: int):...
    class ProfileType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        EndCrossSection: int
        EndGuide: int
        StartCrossSection: int
        StartGuide: int
        value__: int
class AssocManager(DBObject, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocManager:...
    @staticmethod
    def AddGlobalEvaluationCallback(callback: AssocEvaluationCallback, order: int):...
    @staticmethod
    def AuditAssociativeData(database: Database, traverseWholeDatabase: bool):...
    @staticmethod
    def EvaluateTopLevelNetwork(database: Database, callback: AssocEvaluationCallback, callbackOrder: int) -> bool:...
    @staticmethod
    def GetGlobalEvaluationCallbacks(callbacks: _n_7_t_1, orders: _n_7_t_1):...
    @staticmethod
    def GlobalEvaluationMultiCallback() -> AssocEvaluationCallback:...
    @staticmethod
    def HasAssocNetwork(database: Database) -> bool:...
    @staticmethod
    def Initialize():...
    @staticmethod
    def RemoveGlobalEvaluationCallback(callback: AssocEvaluationCallback):...
class AssocNetwork(AssocAction, _n_6_t_0, _n_6_t_1):
    @property
    def GetActions(self) -> ObjectIdCollection:"""GetActions { get; } -> ObjectIdCollection"""
    def __init__(self) -> AssocNetwork:...
    def AddAction(self, actionId: ObjectId, alsoSetAsDatabaseOwner: bool):...
    def AddActions(self, actionIds: ObjectIdCollection, alsoSetAsDatabaseOwner: bool):...
    @staticmethod
    def GetInstanceFromDatabase(database: Database, createIfDoesNotExist: bool, dictionaryKey: str) -> ObjectId:...
    @staticmethod
    def GetInstanceFromObject(owningObjectId: ObjectId, createIfDoesNotExist: bool, addToTopLevelNetwork: bool, dictionaryKey: str) -> ObjectId:...
    def OwnedActionStatusChanged(self, ownedAction: AssocAction, previousStatus: AssocStatus):...
    def RemoveAction(self, actionId: ObjectId, alsoEraseIt: bool):...
    def RemoveAllActions(self, alsoEraseThem: bool):...
    @staticmethod
    def RemoveInstanceFromDatabase(database: Database, alsoEraseIt: bool, dictionaryKey: str):...
    @staticmethod
    def RemoveInstanceFromObject(owningObjectId: ObjectId, alsoEraseIt: bool, dictionaryKey: str):...
class AssocNetworkSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocNetworkSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, crossSections: _n_6_t_10[PathRef], guideCurves: _n_6_t_10[PathRef], continuityArray: _n_6_t_10[int], bulgeArray: _n_6_t_10[float], bEnable: bool) -> ObjectId:...
    def GetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType, expression: str, evaluatorId: str) -> float:...
    def GetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType) -> float:...
    def GetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType, expression: str, evaluatorId: str) -> int:...
    def GetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType) -> int:...
    def SetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: float, expression: str, evaluatorId: str):...
    def SetBulge(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: float):...
    def SetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: int, expression: str, evaluatorId: str):...
    def SetContinuity(self, type: AssocLoftedSurfaceActionBody.ProfileType, value: int):...
class AssocObjectTransaction(_n_6_t_0):
    def __init__(self, dependencyBodyBeingEvaluated: AssocDependencyBody) -> AssocObjectTransaction:...
    def __init__(self, dependencyBeingEvaluated: AssocDependency) -> AssocObjectTransaction:...
    def __init__(self, actionBodyBeingEvaluated: AssocActionBody) -> AssocObjectTransaction:...
    def __init__(self, actionBeingEvaluated: AssocAction) -> AssocObjectTransaction:...
    def GetDBObject(self, objectId: ObjectId, openMode: OpenMode, openErased: bool, openOnLockedLayer: bool) -> DBObject:...
    def IsSubstituteObject(self, dbObject: DBObject) -> bool:...
class AssocOffsetSurfaceActionBody(AssocSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def Distance(self) -> float:"""Distance { get; set; } -> float"""
    def __init__(self) -> AssocOffsetSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputSurfaceId: ObjectId, distance: float, bEnable: bool) -> ObjectId:...
    def GetDistance(self, expression: str, evaluatorId: str) -> float:...
    def SetDistance(self, distance: float, expression: str, evaluatorId: str):...
class AssocParamBasedActionBody(AssocActionBody, _n_6_t_0, _n_6_t_1):
    pass
class AssocPatchSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def Bulge(self) -> float:"""Bulge { get; set; } -> float"""
    @property
    def Continuity(self) -> int:"""Continuity { get; set; } -> int"""
    @property
    def ContinuityGripPoint(self) -> _n_2_t_1:"""ContinuityGripPoint { get; } -> Point3d"""
    def __init__(self) -> AssocPatchSurfaceActionBody:...
    @staticmethod
    def CreateInstance(patchSurfaceId: ObjectId, profileCurves: _n_6_t_10[EdgeRef], constraintCurves: _n_6_t_10[EdgeRef], constraintPoints: _n_6_t_10[VertexRef], enable: bool) -> ObjectId:...
    @staticmethod
    def CreateInstance(patchSurfaceId: ObjectId, edgeCurves: _n_6_t_10[EdgeRef], constraintCurves: _n_6_t_10[EdgeRef], constraintPoints: _n_6_t_10[VertexRef], nContinuity: int, dBulge: float, bEnabled: bool) -> ObjectId:...
    def GetBulge(self, expression: str, evaluatorId: str) -> float:...
    def GetContinuity(self, expression: str, evaluatorId: str) -> int:...
    def SetBulge(self, value: float, expression: str, evaluatorId: str):...
    def SetConstraintCurves(self, constraintCurves: _n_6_t_10[EdgeRef]):...
    def SetConstraintPoints(self, constraintPoints: _n_6_t_10[VertexRef]):...
    def SetContinuity(self, value: int, expression: str, evaluatorId: str):...
class AssocPathActionParam(AssocCompoundActionParam, _n_6_t_0, _n_6_t_1, typing.Iterable[typing.Any]):
    def __init__(self) -> AssocPathActionParam:...
    def GetEdgeRefArray(self) -> _n_6_t_10[_n_6_t_10[EdgeRef]]:...
    def SetEdgeRefArray(self, edgeRef: _n_6_t_10[EdgeRef]):...
    def UpdateEdgeRef(self, index: int, edge: EdgeRef):...
class AssocPathBasedSurfaceActionBody(AssocSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def InputPathParams(self) -> ObjectIdCollection:"""InputPathParams { get; } -> ObjectIdCollection"""
    @property
    def InputVertexParams(self) -> ObjectIdCollection:"""InputVertexParams { get; } -> ObjectIdCollection"""
    def __init__(self) -> AssocPathBasedSurfaceActionBody:...
    def GetInputPaths(self, paths: _n_6_t_10[_n_6_t_10[_n_6_t_10[EdgeRef]]]):...
    def GetInputPoints(self) -> _n_6_t_10[VertexRef]:...
    def MakeInputPathsDrawOnTopOfResultingSurface(self):...
    def RemoveAllPathParams(self):...
    def RemoveAllVertexParams(self):...
    def SetInputPaths(self, paths: _n_6_t_10[PathRef]):...
    def SetInputPoints(self, points: _n_6_t_10[VertexRef]):...
    def UpdateInputPath(self, index: int, pathRef: PathRef):...
class AssocPersSubentityId(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    def __init__(self) -> AssocPersSubentityId:...
    def Audit(self, auditInfo: AuditInfo):...
    @staticmethod
    def CreateObjectAndDwgInFields(database: Database, filer: DwgFiler, createdPersSubentId: AssocPersSubentityId):...
    @staticmethod
    def CreateObjectAndDxfInFields(filer: DxfFiler, createdPersSubentId: AssocPersSubentityId):...
    def DwgInFields(self, filer: DwgFiler):...
    def DwgOutFields(self, filer: DwgFiler):...
    def DxfInFields(self, filer: DxfFiler):...
    def DxfOutFields(self, filer: DxfFiler):...
    def GetTransientSubentIds(self, entity: Entity) -> _n_6_t_10[SubentityId]:...
    def IsEqualTo(self, entity: Entity, other: AssocPersSubentityId) -> bool:...
    def Mirror(self, mirroredEntity: Entity):...
    def SubentType(self, entity: Entity) -> SubentityType:...
    def TransientSubentCount(self, entity: Entity) -> int:...
class AssocPersSubentityIdPE(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocPersSubentityIdPE:...
    def CreateNewPersSubent(self, entity: Entity, compId: CompoundObjectId, subentId: SubentityId) -> AssocPersSubentityId:...
    def GetAllSubentities(self, entity: Entity, subentType: SubentityType) -> _n_6_t_10[SubentityId]:...
    def GetEdgeSubentityGeometry(self, entity: Entity, edgeSubentId: SubentityId) -> _n_2_t_7:...
    def GetEdgeVertexSubentities(self, entity: Entity, edgeSubentId: SubentityId, startVertexSubentId: SubentityId, endVertexSubentId: SubentityId, otherVertexSubentIds: _n_6_t_10[SubentityId]):...
    def GetFaceSubentityGeometry(self, entity: Entity, faceSubentId: SubentityId) -> _n_2_t_8:...
    def GetRigidSetState(self, entity: Entity) -> int:...
    def GetRigidSetTransform(self, entity: Entity) -> _n_2_t_6:...
    def GetSplineEdgeVertexSubentities(self, entity: Entity, edgeSubentId: SubentityId, startVertexSubentId: SubentityId, endVertexSubentId: SubentityId, controlPointSubentIds: _n_6_t_10[SubentityId], fitPointSubentIds: _n_6_t_10[SubentityId]):...
    def GetSubentGeometryXform(self, entity: Entity, fullSubentPath: _n_6_t_10[ObjectId]) -> _n_2_t_6:...
    def GetTransientSubentityIds(self, entity: Entity, perSubentId: AssocPersSubentityId) -> _n_6_t_10[SubentityId]:...
    def GetVertexSubentityGeometry(self, entity: Entity, vertexSubentId: SubentityId) -> _n_2_t_1:...
    def MirrorPersSubent(self, mirroredEntity: Entity, persSubentIdToMirror: AssocPersSubentityId):...
    def SetEdgeSubentityGeometry(self, entity: Entity, edgeSubentId: SubentityId, newEdgeCurve: _n_2_t_7):...
    def SetFaceSubentityGeometry(self, entity: Entity, faceSubentId: SubentityId, newFaceSurface: _n_2_t_8):...
    def SetRigidSetTransform(self, entity: Entity, trans: _n_2_t_6):...
    def SetVertexSubentityGeometry(self, entity: Entity, vertexSubentId: SubentityId, newVertexPosition: _n_2_t_1):...
class AssocPlaneSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocPlaneSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputPath: PathRef, enable: bool) -> ObjectId:...
class AssocRevolvedSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def RevolveAngle(self) -> float:"""RevolveAngle { get; set; } -> float"""
    def __init__(self) -> AssocRevolvedSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, revolvePath: PathRef, axisPath: PathRef, angle: float, startAngle: float, revolveOptions: RevolveOptions, flipAxisDirection: bool, enable: bool) -> ObjectId:...
    def GetRevolveAngle(self, expression: str, evaluatorId: str) -> float:...
    def SetRevolveAngle(self, value: float, expression: str, evaluatorId: str):...
class AssocSimplePersSubentId(AssocPersSubentityId, _n_6_t_0, _n_6_t_1):
    def __init__(self, SubentityId: SubentityId) -> AssocSimplePersSubentId:...
    def SubentId(self, entity: Entity) -> SubentityId:...
class AssocSingleEdgePersSubentId(AssocPersSubentityId, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocSingleEdgePersSubentId:...
class AssocStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ChangedDirectlyAssocStatus: int
    ChangedNoDifferenceAssocStatus: int
    ChangedTransitivelyAssocStatus: int
    ErasedAssocStatus: int
    FailedToEvaluateAssocStatus: int
    IsUpToDateAssocStatus: int
    SuppressedAssocStatus: int
    value__: int
class AssocSurfaceActionBody(AssocParamBasedActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def IsSemiAssociative(self) -> bool:"""IsSemiAssociative { get; } -> bool"""
    @property
    def ResultingSurface(self) -> ObjectId:"""ResultingSurface { get; set; } -> ObjectId"""
    def __init__(self) -> AssocSurfaceActionBody:...
    @staticmethod
    def FindActionsThatAffectedTopologicalSubentity(entity: Entity, subEntityId: SubentityId) -> ObjectIdCollection:...
    def ResultingSurfaceDep(self, createIfDoesNotExist: bool, isWriteOnlyDependency: bool) -> ObjectId:...
    def ResultingSurfaceDep(self, createIfDoesNotExist: bool) -> ObjectId:...
    def SetResultingSurface(self, surfaceId: ObjectId, isWriteOnlyDependency: bool):...
class AssocSweptSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def AlignAngle(self) -> float:"""AlignAngle { get; set; } -> float"""
    @property
    def ScaleFactor(self) -> float:"""ScaleFactor { get; set; } -> float"""
    @property
    def TwistAngle(self) -> float:"""TwistAngle { get; set; } -> float"""
    def __init__(self) -> AssocSweptSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, sweptPath: PathRef, path: PathRef, sweptOptions: SweepOptions, enable: bool) -> ObjectId:...
    def GetAlignAngle(self, expression: str, evaluatorId: str) -> float:...
    def GetScaleFactor(self, expression: str, evaluatorId: str) -> float:...
    def GetTwistAngle(self, expression: str, evaluatorId: str) -> float:...
    def SetAlignAngle(self, value: float, expression: str, evaluatorId: str):...
    def SetScaleFactor(self, value: float, expression: str, evaluatorId: str):...
    def SetTwistAngle(self, value: float, expression: str, evaluatorId: str):...
class AssocTransformationType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Move: int
    NotSpecified: int
    Rotate: int
    Stretch: int
    value__: int
class AssocTrimSurfaceActionBody(AssocPathBasedSurfaceActionBody, _n_6_t_0, _n_6_t_1):
    @property
    def TrimmedArea(self) -> float:"""TrimmedArea { get; } -> float"""
    def __init__(self) -> AssocTrimSurfaceActionBody:...
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, trimInfo: _n_6_t_10[SurfaceTrimInfo], autoExtend: bool, enable: bool) -> ObjectIdCollection:...
    def MakeTrimPermanent(self):...
    def SetTrimInfo(self, trimInfoArray: _n_6_t_10[SurfaceTrimInfo], autoExtend: bool):...
    def Untrim(self):...
class AssocValueDependency(AssocDependency, _n_6_t_0, _n_6_t_1):
    @property
    def DependentOnObjectValue(self) -> ResultBuffer:"""DependentOnObjectValue { get; set; } -> ResultBuffer"""
    @property
    def ValueName(self) -> str:"""ValueName { get; set; } -> str"""
    def __init__(self) -> AssocValueDependency:...
class AssocValueProviderPE(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> AssocValueProviderPE:...
    def CanGetValue(self, dbObj: DBObject, valueName: str) -> bool:...
    def CanSetValue(self, dbObj: DBObject, valueName: str) -> bool:...
    def GetValue(self, dbObj: DBObject, valueName: str) -> ResultBuffer:...
    def SetValue(self, dbObj: DBObject, valueName: str, newValue: ResultBuffer):...
class AssocVariable(AssocAction, _n_6_t_0, _n_6_t_1):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def EvaluatorId(self) -> str:"""EvaluatorId { get; set; } -> str"""
    @property
    def Expression(self) -> str:"""Expression { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> ResultBuffer:"""Value { get; set; } -> ResultBuffer"""
    def __init__(self) -> AssocVariable:...
    @staticmethod
    def AddGlobalCallback(callback: AssocVariableCallback):...
    def EvaluateExpression(self, objectIds: ObjectIdCollection, objectValues: _n_6_t_10[ResultBuffer], evaluatedExpressionValue: ResultBuffer) -> str:...
    def EvaluateExpression(self, evaluatedExpressionValue: ResultBuffer) -> str:...
    def FindObjectByName(self, objectName: str, pObjectClass: _n_5_t_0) -> ObjectId:...
    @staticmethod
    def globalCallback() -> AssocVariableCallback:...
    @staticmethod
    def RemoveGlobalCallback(callback: AssocVariableCallback):...
    def SetExpression(self, newExpression: str, evaluatorId: str, checkForCyclicalDependencies: bool, updateDependenciesOnReferencedSymbols: bool, errorMessage: str, silentMode: bool):...
    def SetName(self, newName: str, updateReferencingExpressions: bool):...
    def ValidateNameAndExpression(self, nameToValidate: str, expressionToValidate: str, errorMessage: str):...
class AssocVariableCallback(_n_6_t_0):
    def __init__(self) -> AssocVariableCallback:...
    def CanBeErased(self, variable: AssocVariable) -> bool:...
    def ValidateNameAndExpression(self, variable: AssocVariable, nameToValidate: str, expressionToValidate: str) -> str:...
class AssocVertexActionParam(AssocActionParam, _n_6_t_0, _n_6_t_1):
    @property
    def DependentOnCompoundObject(self) -> CompoundObjectId:"""DependentOnCompoundObject { get; } -> CompoundObjectId"""
    def __init__(self) -> AssocVertexActionParam:...
    def GetVertexRef(self) -> VertexRef:...
    def SetVertexRef(self, pointRef: VertexRef, isReadDep: bool, isWriteDep: bool):...
class AttachmentPoint(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BaseAlign: int
    BaseCenter: int
    BaseFit: int
    BaseLeft: int
    BaseMid: int
    BaseRight: int
    BottomAlign: int
    BottomCenter: int
    BottomFit: int
    BottomLeft: int
    BottomMid: int
    BottomRight: int
    MiddleAlign: int
    MiddleCenter: int
    MiddleFit: int
    MiddleLeft: int
    MiddleMid: int
    MiddleRight: int
    TopAlign: int
    TopCenter: int
    TopFit: int
    TopLeft: int
    TopMid: int
    TopRight: int
    value__: int
class AttributeCollection(_n_7_t_2, ISubObject, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> ObjectId:"""Item { get; } -> ObjectId"""
    def AppendAttribute(self, attributeToAddToBlockReference: AttributeReference) -> ObjectId:...
class AttributeDefinition(DBText, _n_6_t_0, _n_6_t_1):
    @property
    def Constant(self) -> bool:"""Constant { get; set; } -> bool"""
    @property
    def FieldLength(self) -> int:"""FieldLength { get; set; } -> int"""
    @property
    def Invisible(self) -> bool:"""Invisible { get; set; } -> bool"""
    @property
    def IsMTextAttributeDefinition(self) -> bool:"""IsMTextAttributeDefinition { get; set; } -> bool"""
    @property
    def LockPositionInBlock(self) -> bool:"""LockPositionInBlock { get; set; } -> bool"""
    @property
    def MTextAttributeDefinition(self) -> MText:"""MTextAttributeDefinition { get; set; } -> MText"""
    @property
    def Preset(self) -> bool:"""Preset { get; set; } -> bool"""
    @property
    def Prompt(self) -> str:"""Prompt { get; set; } -> str"""
    @property
    def Tag(self) -> str:"""Tag { get; set; } -> str"""
    @property
    def Verifiable(self) -> bool:"""Verifiable { get; set; } -> bool"""
    def __init__(self, position: _n_2_t_1, value: str, tag: str, prompt: str, style: ObjectId) -> AttributeDefinition:...
    def __init__(self) -> AttributeDefinition:...
    def UpdateMTextAttributeDefinition(self):...
class AttributeReference(DBText, _n_6_t_0, _n_6_t_1):
    @property
    def FieldLength(self) -> int:"""FieldLength { get; set; } -> int"""
    @property
    def Invisible(self) -> bool:"""Invisible { get; set; } -> bool"""
    @property
    def IsConstant(self) -> bool:"""IsConstant { get; } -> bool"""
    @property
    def IsMTextAttribute(self) -> bool:"""IsMTextAttribute { get; set; } -> bool"""
    @property
    def IsPreset(self) -> bool:"""IsPreset { get; } -> bool"""
    @property
    def IsVerifiable(self) -> bool:"""IsVerifiable { get; } -> bool"""
    @property
    def LockPositionInBlock(self) -> bool:"""LockPositionInBlock { get; set; } -> bool"""
    @property
    def MTextAttribute(self) -> MText:"""MTextAttribute { get; set; } -> MText"""
    @property
    def Tag(self) -> str:"""Tag { get; set; } -> str"""
    def __init__(self, position: _n_2_t_1, value: str, tag: str, style: ObjectId) -> AttributeReference:...
    def __init__(self) -> AttributeReference:...
    def SetAttributeFromBlock(self, definition: AttributeDefinition, blockTransform: _n_2_t_6):...
    def SetAttributeFromBlock(self, blockTransform: _n_2_t_6):...
    def UpdateMTextAttribute(self):...
class AuditInfo(_n_5_t_3, _n_6_t_0):
    @property
    def AuditPass(self) -> AuditPass:"""AuditPass { get; } -> AuditPass"""
    @property
    def FixErrors(self) -> bool:"""FixErrors { get; } -> bool"""
    @property
    def NumEntities(self) -> int:"""NumEntities { get; } -> int"""
    @property
    def NumErrors(self) -> int:"""NumErrors { get; } -> int"""
    @property
    def NumFixes(self) -> int:"""NumFixes { get; } -> int"""
    def ErrorsFixed(self, count: int):...
    def ErrorsFound(self, count: int):...
    def IncNumEntities(self):...
    def PrintError(self, value: DBObject, value2: str, validation: str, defaultValue: str):...
    def PrintError(self, name: str, value: str, validation: str, defaultValue: str):...
    def PrintNumEntities(self, msg: str):...
    def RequestRegen(self):...
    def ResetNumEntities(self):...
class AuditPass(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Pass1: int
    Pass2: int
    value__: int
class AutoConstrainEvaluationCallback(_n_6_t_0):
    @property
    def IsEvaluationCancelled(self) -> bool:"""IsEvaluationCancelled { get; } -> bool"""
    def __init__(self) -> AutoConstrainEvaluationCallback:...
    def GetAutoConstrainPriority(self) -> _n_6_t_10[GeometricalConstraint.ConstraintType]:...
    def GetConstraintPriorityOverride(self, type: GeometricalConstraint.ConstraintType, geometries: _n_6_t_10[ConstrainedGeometry]) -> int:...
    def GetTotalConstraints(self, constraints: _n_6_t_10[GeometricalConstraint]) -> int:...
class Background(DBObject, _n_6_t_0, _n_6_t_1):
    @staticmethod
    def GetBackgroundDictionaryId(database: Database, createIfNotPresent: bool) -> ObjectId:...
class BeginInsertEventArgs(_n_6_t_13):
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
class BeginInsertEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> BeginInsertEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginInsertEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: BeginInsertEventArgs):...
class BeginWblockBlockEventArgs(_n_6_t_13):
    @property
    def BlockId(self) -> ObjectId:"""BlockId { get; } -> ObjectId"""
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
class BeginWblockBlockEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> BeginWblockBlockEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginWblockBlockEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: BeginWblockBlockEventArgs):...
class BeginWblockEntireDatabaseEventArgs(_n_6_t_13):
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
class BeginWblockEntireDatabaseEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> BeginWblockEntireDatabaseEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginWblockEntireDatabaseEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: BeginWblockEntireDatabaseEventArgs):...
class BeginWblockObjectsEventArgs(_n_6_t_13):
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
    @property
    def IdMapping(self) -> IdMapping:"""IdMapping { get; } -> IdMapping"""
class BeginWblockObjectsEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> BeginWblockObjectsEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginWblockObjectsEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: BeginWblockObjectsEventArgs):...
class BeginWblockSelectedObjectsEventArgs(_n_6_t_13):
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
    @property
    def InsertionPoint(self) -> _n_2_t_1:"""InsertionPoint { get; } -> Point3d"""
class BeginWblockSelectedObjectsEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> BeginWblockSelectedObjectsEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginWblockSelectedObjectsEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: BeginWblockSelectedObjectsEventArgs):...
class BlendOptions(_n_5_t_3, _n_6_t_0, _n_6_t_1):
    @property
    def CoplanarDirection(self) -> _n_6_t_14[_n_2_t_3]:"""CoplanarDirection { get; } -> Nullable"""
    @property
    def CoplanarPoint(self) -> _n_6_t_14[_n_2_t_1]:"""CoplanarPoint { get; } -> Nullable"""
    @property
    def DriveMode(self) -> BlendOptions.DriveModeType:"""DriveMode { get; } -> BlendOptions.DriveModeType"""
    @property
    def Quality(self) -> _n_6_t_11:"""Quality { get; } -> UInt32"""
    @property
    def Simplify(self) -> bool:"""Simplify { get; } -> bool"""
    @property
    def Solid(self) -> bool:"""Solid { get; } -> bool"""
    def __init__(self) -> BlendOptions:...
    class DriveModeType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        DriveModeBoth: int
        DriveModeFirst: int
        DriveModeSecond: int
        value__: int
class BlendOptionsBuilder(object):
    @property
    def CoplanarDirection(self) -> _n_6_t_14[_n_2_t_3]:"""CoplanarDirection { get; set; } -> Nullable"""
    @property
    def CoplanarPoint(self) -> _n_6_t_14[_n_2_t_1]:"""CoplanarPoint { get; set; } -> Nullable"""
    @property
    def DriveMode(self) -> BlendOptions.DriveModeType:"""DriveMode { get; set; } -> BlendOptions.DriveModeType"""
    @property
    def Quality(self) -> _n_6_t_11:"""Quality { get; set; } -> UInt32"""
    @property
    def Simplify(self) -> bool:"""Simplify { get; set; } -> bool"""
    @property
    def Solid(self) -> bool:"""Solid { get; set; } -> bool"""
    def __init__(self, value: BlendOptions) -> BlendOptionsBuilder:...
    def __init__(self) -> BlendOptionsBuilder:...
    def ToBlendOptions(self) -> BlendOptions:...
class BlockBegin(Entity, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> BlockBegin:...
class BlockConnectionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ConnectBase: int
    ConnectExtents: int
    value__: int
class BlockEnd(Entity, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> BlockEnd:...
class BlockInsertionPointsEventArgs(_n_6_t_13):
    @property
    def AlignmentVectors(self) -> _n_2_t_9:"""AlignmentVectors { get; } -> Vector3dCollection"""
    @property
    def BlockTableRecord(self) -> BlockTableRecord:"""BlockTableRecord { get; } -> BlockTableRecord"""
    @property
    def InsertionPoints(self) -> _n_2_t_10:"""InsertionPoints { get; } -> Point3dCollection"""
    def __init__(self, blockTableRecord: BlockTableRecord, points: _n_2_t_10, alignmentVectors: _n_2_t_9) -> BlockInsertionPointsEventArgs:...
class BlockInsertionPointsEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> BlockInsertionPointsEventHandler:...
    def BeginInvoke(self, sender: object, e: BlockInsertionPointsEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: BlockInsertionPointsEventArgs):...
class BlockPropertiesTable(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Columns(self) -> BlockPropertiesTableColumnCollection:"""Columns { get; } -> BlockPropertiesTableColumnCollection"""
    @property
    def ContainsRuntimeParametersOnly(self) -> bool:"""ContainsRuntimeParametersOnly { get; set; } -> bool"""
    @property
    def DefaultActiveRowIndex(self) -> int:"""DefaultActiveRowIndex { get; set; } -> int"""
    @property
    def IsDisabledInDrawingEditor(self) -> bool:"""IsDisabledInDrawingEditor { get; } -> bool"""
    @property
    def MustMatch(self) -> bool:"""MustMatch { get; set; } -> bool"""
    @property
    def Rows(self) -> BlockPropertiesTableRowCollection:"""Rows { get; } -> BlockPropertiesTableRowCollection"""
    def __init__(self, unmanagedPointer: _n_6_t_3, autoDelete: bool) -> BlockPropertiesTable:...
    class AuditError(_n_5_t_3, _n_6_t_0):
        @property
        def ColumnIndex(self) -> int:"""ColumnIndex { get; } -> int"""
        @property
        def RowIndex(self) -> int:"""RowIndex { get; } -> int"""
        @property
        def RowIndices(self) -> _n_6_t_10[int]:"""RowIndices { get; } -> Array"""
        @property
        def Type(self) -> BlockPropertiesTable.AuditErrorType:"""Type { get; } -> BlockPropertiesTable.AuditErrorType"""
    class AuditErrorType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        CellEvalError: int
        DuplicateRows: int
        Empty: int
        ExprExternRef: int
        InvalidCell: int
        InvalidUnmatchedValue: int
        NoMatchingRow: int
        NonConstAttDef: int
        NotInValueSet: int
        value__: int
class BlockPropertiesTableColumn(object):
    @property
    def Constant(self) -> bool:"""Constant { get; set; } -> bool"""
    @property
    def CustomProperties(self) -> ObjectId:"""CustomProperties { get; set; } -> ObjectId"""
    @property
    def DefaultValue(self) -> ResultBuffer:"""DefaultValue { get; set; } -> ResultBuffer"""
    @property
    def Editable(self) -> bool:"""Editable { get; set; } -> bool"""
    @property
    def Format(self) -> str:"""Format { get; set; } -> str"""
    @property
    def Parameter(self) -> IParameter:"""Parameter { get; } -> IParameter"""
    @property
    def Removable(self) -> bool:"""Removable { get; set; } -> bool"""
    @property
    def Table(self) -> BlockPropertiesTable:"""Table { get; set; } -> BlockPropertiesTable"""
    @property
    def UnmatchedValue(self) -> ResultBuffer:"""UnmatchedValue { get; set; } -> ResultBuffer"""
class BlockPropertiesTableColumnCollection(_n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> BlockPropertiesTableColumn:"""Item { get; } -> BlockPropertiesTableColumn"""
    def AddAt(self, id: ObjectId, parameterName: str, index: int):...
    def AddItem(self, id: ObjectId, parameterName: str):...
    def Clear(self):...
    def ContainsColumn(self, id: ObjectId, parameterName: str) -> bool:...
    def GetIndex(self, column: BlockPropertiesTableColumn) -> int:...
    def Move(self, index: int, newIndex: int):...
    def Move(self, column: BlockPropertiesTableColumn, newIndex: int):...
    def Remove(self, column: BlockPropertiesTableColumn):...
    def Remove(self, index: int):...
class BlockPropertiesTableRow(_n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> ResultBuffer:"""Item { get; set; } -> ResultBuffer"""
    @property
    def Table(self) -> BlockPropertiesTable:"""Table { get; set; } -> BlockPropertiesTable"""
class BlockPropertiesTableRowCollection(_n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> BlockPropertiesTableRow:"""Item { get; } -> BlockPropertiesTableRow"""
    def AddAt(self, index: int):...
    def AddItem(self):...
    def Clear(self):...
    def GetIndex(self, row: BlockPropertiesTableRow) -> int:...
    def Move(self, index: int, newIndex: int):...
    def Move(self, row: BlockPropertiesTableRow, newIndex: int):...
    def Remove(self, row: BlockPropertiesTableRow):...
    def Remove(self, index: int):...
    def Sort(self, column: BlockPropertiesTableColumn, ascending: bool):...
class BlockReference(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def AnonymousBlockTableRecord(self) -> ObjectId:"""AnonymousBlockTableRecord { get; } -> ObjectId"""
    @property
    def AttributeCollection(self) -> AttributeCollection:"""AttributeCollection { get; } -> AttributeCollection"""
    @property
    def BlockTableRecord(self) -> ObjectId:"""BlockTableRecord { get; set; } -> ObjectId"""
    @property
    def BlockTransform(self) -> _n_2_t_6:"""BlockTransform { get; set; } -> Matrix3d"""
    @property
    def BlockUnit(self) -> UnitsValue:"""BlockUnit { get; set; } -> UnitsValue"""
    @property
    def DynamicBlockReferencePropertyCollection(self) -> DynamicBlockReferencePropertyCollection:"""DynamicBlockReferencePropertyCollection { get; } -> DynamicBlockReferencePropertyCollection"""
    @property
    def DynamicBlockTableRecord(self) -> ObjectId:"""DynamicBlockTableRecord { get; } -> ObjectId"""
    @property
    def IsDynamicBlock(self) -> bool:"""IsDynamicBlock { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def ScaleFactors(self) -> _n_2_t_11:"""ScaleFactors { get; set; } -> Scale3d"""
    @property
    def TreatAsBlockRefForExplode(self) -> bool:"""TreatAsBlockRefForExplode { get; } -> bool"""
    @property
    def UnitFactor(self) -> float:"""UnitFactor { get; } -> float"""
    def __init__(self, position: _n_2_t_1, blockTableRecord: ObjectId) -> BlockReference:...
    def ConvertToStaticBlock(self, newBlockName: str):...
    def ConvertToStaticBlock(self):...
    def ExplodeToOwnerSpace(self):...
    def GeometryExtentsBestFit(self) -> Extents3d:...
    def GeometryExtentsBestFit(self, parentTransform: _n_2_t_6) -> Extents3d:...
    def ResetBlock(self):...
class BlockScaling(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Any: int
    Uniform: int
    value__: int
class BlockTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class BlockTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    ModelSpace: int
    PaperSpace: int
    @property
    def BlockBeginId(self) -> ObjectId:"""BlockBeginId { get; } -> ObjectId"""
    @property
    def BlockEndId(self) -> ObjectId:"""BlockEndId { get; } -> ObjectId"""
    @property
    def BlockScaling(self) -> BlockScaling:"""BlockScaling { get; set; } -> BlockScaling"""
    @property
    def Comments(self) -> str:"""Comments { get; set; } -> str"""
    @property
    def DrawOrderTableId(self) -> ObjectId:"""DrawOrderTableId { get; } -> ObjectId"""
    @property
    def Explodable(self) -> bool:"""Explodable { get; set; } -> bool"""
    @property
    def HasAttributeDefinitions(self) -> bool:"""HasAttributeDefinitions { get; } -> bool"""
    @property
    def HasPreviewIcon(self) -> bool:"""HasPreviewIcon { get; } -> bool"""
    @property
    def Hyperlinks(self) -> HyperLinkCollection:"""Hyperlinks { get; } -> HyperLinkCollection"""
    @property
    def IncludingErased(self) -> BlockTableRecord:"""IncludingErased { get; } -> BlockTableRecord"""
    @property
    def IsAnonymous(self) -> bool:"""IsAnonymous { get; } -> bool"""
    @property
    def IsDynamicBlock(self) -> bool:"""IsDynamicBlock { get; } -> bool"""
    @property
    def IsFromExternalReference(self) -> bool:"""IsFromExternalReference { get; } -> bool"""
    @property
    def IsFromOverlayReference(self) -> bool:"""IsFromOverlayReference { get; set; } -> bool"""
    @property
    def IsLayout(self) -> bool:"""IsLayout { get; } -> bool"""
    @property
    def IsUnloaded(self) -> bool:"""IsUnloaded { get; set; } -> bool"""
    @property
    def LayoutId(self) -> ObjectId:"""LayoutId { get; set; } -> ObjectId"""
    @property
    def Origin(self) -> _n_2_t_1:"""Origin { get; set; } -> Point3d"""
    @property
    def PathName(self) -> str:"""PathName { get; set; } -> str"""
    @property
    def PreviewIcon(self) -> _n_11_t_0:"""PreviewIcon { get; set; } -> Bitmap"""
    @property
    def Units(self) -> UnitsValue:"""Units { get; set; } -> UnitsValue"""
    @property
    def XrefStatus(self) -> XrefStatus:"""XrefStatus { get; } -> XrefStatus"""
    @property
    def BlockInsertionPoints(self) -> BlockInsertionPointsEventHandler:
        """BlockInsertionPoints Event: BlockInsertionPointsEventHandler"""
    def __init__(self) -> BlockTableRecord:...
    def AppendEntity(self, entity: Entity) -> ObjectId:...
    def AssumeOwnershipOf(self, entitiesToMove: ObjectIdCollection):...
    def GetAnonymousBlockIds(self) -> ObjectIdCollection:...
    def GetBlockReferenceIds(self, directOnly: bool, forceValidity: bool) -> ObjectIdCollection:...
    def GetErasedBlockReferenceIds(self) -> ObjectIdCollection:...
    def GetXrefDatabase(self, incrementUnresolved: bool) -> Database:...
    def UpdateAnonymousBlocks(self):...
class BlockTableRecordEnumerator(_n_5_t_3, _n_6_t_0, _n_7_t_3):
    pass
class Body(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def NumChanges(self) -> int:"""NumChanges { get; } -> int"""
    @property
    def UsesGraphicsCache(self) -> bool:"""UsesGraphicsCache { get; } -> bool"""
    def __init__(self) -> Body:...
    @staticmethod
    def AcisIn(fileName: str) -> DBObjectCollection:...
    @staticmethod
    def AcisOut(fileName: str, entitiesOutToFile: DBObjectCollection):...
class BooleanOperationType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BoolIntersect: int
    BoolSubtract: int
    BoolUnite: int
    value__: int
class BulgeVertex(object):
    @property
    def Bulge(self) -> float:"""Bulge { get; set; } -> float"""
    @property
    def Vertex(self) -> _n_2_t_0:"""Vertex { get; set; } -> Point2d"""
    def __init__(self, point: _n_2_t_0, bulge: float) -> BulgeVertex:...
class BulgeVertexCollection(_n_7_t_4, _n_7_t_5, typing.Iterable[typing.Any]):
    def __init__(self) -> BulgeVertexCollection:...
class CallerMustCloseAttribute(_n_6_t_15, _n_14_t_0):
    def __init__(self) -> CallerMustCloseAttribute:...
class Cell(CellRange, ISubObject, _n_8_t_0[CellReference], typing.Iterable[typing.Any]):
    @property
    def AttachmentPoint(self) -> _n_2_t_1:"""AttachmentPoint { get; } -> Point3d"""
    @property
    def BlockTableRecordId(self) -> ObjectId:"""BlockTableRecordId { get; set; } -> ObjectId"""
    @property
    def CellType(self) -> TableCellType:"""CellType { get; } -> TableCellType"""
    @property
    def Column(self) -> int:"""Column { get; } -> int"""
    @property
    def Contents(self) -> CellContentsCollection:"""Contents { get; } -> CellContentsCollection"""
    @property
    def ContentTypes(self) -> CellContentTypes:"""ContentTypes { get; } -> CellContentTypes"""
    @property
    def DataLink(self) -> ObjectId:"""DataLink { get; set; } -> ObjectId"""
    @property
    def FieldId(self) -> ObjectId:"""FieldId { get; set; } -> ObjectId"""
    @property
    def Row(self) -> int:"""Row { get; } -> int"""
    @property
    def TextString(self) -> str:"""TextString { get; set; } -> str"""
    @property
    def ToolTip(self) -> str:"""ToolTip { get; set; } -> str"""
    @property
    def Value(self) -> object:"""Value { get; set; } -> object"""
    def __init__(self, table: Table, row: int, column: int) -> Cell:...
    def GetBlockAttributeValue(self, attDefId: ObjectId) -> str:...
    def GetDataLinkRange(self) -> CellRange:...
    def GetExtents(self) -> _n_2_t_10:...
    def GetMergeRange(self) -> CellRange:...
    def GetTextString(self, formatOption: FormatOption) -> str:...
    def GetValue(self, formatOption: FormatOption) -> object:...
    def RemoveDataLink(self):...
    def ResetValue(self):...
    def SetBlockAttributeValue(self, attDefId: ObjectId, value: str):...
    def SetValue(self, value: object, parseOption: ParseOption):...
    def UpdateDataLink(self, dir: UpdateDirection, option: UpdateOption):...
class CellAlignment(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BottomCenter: int
    BottomLeft: int
    BottomRight: int
    MiddleCenter: int
    MiddleLeft: int
    MiddleRight: int
    TopCenter: int
    TopLeft: int
    TopRight: int
    value__: int
class CellBorder(object):
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; set; } -> Color"""
    @property
    def DoubleLineSpacing(self) -> _n_6_t_14[float]:"""DoubleLineSpacing { get; set; } -> Nullable"""
    @property
    def IsVisible(self) -> _n_6_t_14[bool]:"""IsVisible { get; set; } -> Nullable"""
    @property
    def LineStyle(self) -> _n_6_t_14[GridLineStyle]:"""LineStyle { get; set; } -> Nullable"""
    @property
    def Linetype(self) -> _n_6_t_14[ObjectId]:"""Linetype { get; set; } -> Nullable"""
    @property
    def LineWeight(self) -> _n_6_t_14[LineWeight]:"""LineWeight { get; set; } -> Nullable"""
    @property
    def Margin(self) -> _n_6_t_14[float]:"""Margin { get; set; } -> Nullable"""
    @property
    def Overrides(self) -> _n_6_t_14[GridProperties]:"""Overrides { get; set; } -> Nullable"""
class CellBorders(object):
    @property
    def Bottom(self) -> CellBorder:"""Bottom { get; } -> CellBorder"""
    @property
    def Horizontal(self) -> CellBorder:"""Horizontal { get; } -> CellBorder"""
    @property
    def Left(self) -> CellBorder:"""Left { get; } -> CellBorder"""
    @property
    def Right(self) -> CellBorder:"""Right { get; } -> CellBorder"""
    @property
    def Top(self) -> CellBorder:"""Top { get; } -> CellBorder"""
    @property
    def Vertical(self) -> CellBorder:"""Vertical { get; } -> CellBorder"""
class CellClass(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Data: int
    Label: int
    _None: int
    value__: int
class CellContent(object):
    @property
    def BlockTableRecordId(self) -> ObjectId:"""BlockTableRecordId { get; set; } -> ObjectId"""
    @property
    def ContentColor(self) -> _n_0_t_0:"""ContentColor { get; set; } -> Color"""
    @property
    def ContentTypes(self) -> CellContentTypes:"""ContentTypes { get; } -> CellContentTypes"""
    @property
    def DataFormat(self) -> str:"""DataFormat { get; set; } -> str"""
    @property
    def DataType(self) -> DataTypeParameter:"""DataType { get; set; } -> DataTypeParameter"""
    @property
    def FieldId(self) -> ObjectId:"""FieldId { get; set; } -> ObjectId"""
    @property
    def Formula(self) -> str:"""Formula { get; set; } -> str"""
    @property
    def HasFormula(self) -> bool:"""HasFormula { get; } -> bool"""
    @property
    def IsAutoScale(self) -> bool:"""IsAutoScale { get; set; } -> bool"""
    @property
    def Overrides(self) -> CellProperties:"""Overrides { get; set; } -> CellProperties"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def TextHeight(self) -> float:"""TextHeight { get; set; } -> float"""
    @property
    def TextString(self) -> str:"""TextString { get; set; } -> str"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    @property
    def Value(self) -> object:"""Value { get; set; } -> object"""
    def DeleteContent(self):...
    def GetBlockAttributeValue(self, attDefId: ObjectId) -> str:...
    def GetTextString(self, formatOption: FormatOption) -> str:...
    def GetValue(self, formatOption: FormatOption) -> object:...
    def SetBlockAttributeValue(self, attDefId: ObjectId, value: str):...
    def SetValue(self, value: object, parseOption: ParseOption):...
class CellContentLayout(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Flow: int
    StackedHorizontal: int
    StackedVertical: int
    value__: int
class CellContentsCollection(_n_8_t_0[CellContent], typing.Iterable[typing.Any]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def Item(self) -> CellContent:"""Item { get; } -> CellContent"""
    def Add(self):...
    def Clear(self):...
    def InsertAt(self, index: int):...
    def Move(self, fromIndex: int, toIndex: int):...
    def RemoveAt(self, index: int):...
class CellContentTypes(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Block: int
    Field: int
    Unknown: int
    Value: int
    value__: int
class CellEdgeMasks(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BottomMask: int
    LeftMask: int
    RightMask: int
    TopMask: int
    value__: int
class CellMargins(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Bottom: int
    Left: int
    Right: int
    Top: int
    value__: int
class CellOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    InheritCellFormat: int
    _None: int
    value__: int
class CellProperties(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Alignment: int
    AutoScale: int
    BackgroundColor: int
    ContentColor: int
    ContentLayout: int
    DataFormat: int
    DataType: int
    FlowDirBtoT: int
    Invalid: int
    MarginBottom: int
    MarginHorzSpacing: int
    MarginLeft: int
    MarginRight: int
    MarginTop: int
    MarginVertSpacing: int
    MergeAll: int
    Rotation: int
    Scale: int
    TextHeight: int
    TextStyle: int
    value__: int
class CellRange(ISubObject, _n_8_t_0[CellReference], typing.Iterable[typing.Any]):
    @property
    def Alignment(self) -> _n_6_t_14[CellAlignment]:"""Alignment { get; set; } -> Nullable"""
    @property
    def BackgroundColor(self) -> _n_0_t_0:"""BackgroundColor { get; set; } -> Color"""
    @property
    def Borders(self) -> CellBorders:"""Borders { get; } -> CellBorders"""
    @property
    def BottomRight(self) -> Cell:"""BottomRight { get; } -> Cell"""
    @property
    def BottomRightPlusOne(self) -> Cell:"""BottomRightPlusOne { get; } -> Cell"""
    @property
    def BottomRow(self) -> int:"""BottomRow { get; } -> int"""
    @property
    def CanDeleteColumns(self) -> bool:"""CanDeleteColumns { get; } -> bool"""
    @property
    def CanDeleteRows(self) -> bool:"""CanDeleteRows { get; } -> bool"""
    @property
    def CanInsertColumn(self) -> bool:"""CanInsertColumn { get; } -> bool"""
    @property
    def CanInsertRow(self) -> bool:"""CanInsertRow { get; } -> bool"""
    @property
    def ContentColor(self) -> _n_0_t_0:"""ContentColor { get; set; } -> Color"""
    @property
    def ContentLayout(self) -> _n_6_t_14[CellContentLayout]:"""ContentLayout { get; set; } -> Nullable"""
    @property
    def DataFormat(self) -> str:"""DataFormat { get; set; } -> str"""
    @property
    def DataType(self) -> _n_6_t_14[DataTypeParameter]:"""DataType { get; set; } -> Nullable"""
    @property
    def IsBackgroundColorNone(self) -> _n_6_t_14[bool]:"""IsBackgroundColorNone { get; set; } -> Nullable"""
    @property
    def IsContentEditable(self) -> _n_6_t_14[bool]:"""IsContentEditable { get; } -> Nullable"""
    @property
    def IsEmpty(self) -> _n_6_t_14[bool]:"""IsEmpty { get; } -> Nullable"""
    @property
    def IsFormatEditable(self) -> _n_6_t_14[bool]:"""IsFormatEditable { get; } -> Nullable"""
    @property
    def IsLinked(self) -> _n_6_t_14[bool]:"""IsLinked { get; } -> Nullable"""
    @property
    def IsMergeAllEnabled(self) -> _n_6_t_14[bool]:"""IsMergeAllEnabled { get; set; } -> Nullable"""
    @property
    def IsMerged(self) -> _n_6_t_14[bool]:"""IsMerged { get; } -> Nullable"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def IsSingleCell(self) -> bool:"""IsSingleCell { get; } -> bool"""
    @property
    def Item(self) -> Cell:"""Item { get; } -> Cell"""
    @property
    def LeftColumn(self) -> int:"""LeftColumn { get; } -> int"""
    @property
    def ParentTable(self) -> Table:"""ParentTable { get; } -> Table"""
    @property
    def RightColumn(self) -> int:"""RightColumn { get; } -> int"""
    @property
    def State(self) -> _n_6_t_14[CellStates]:"""State { get; set; } -> Nullable"""
    @property
    def Style(self) -> str:"""Style { get; set; } -> str"""
    @property
    def TextHeight(self) -> _n_6_t_14[float]:"""TextHeight { get; set; } -> Nullable"""
    @property
    def TextStyleId(self) -> _n_6_t_14[ObjectId]:"""TextStyleId { get; set; } -> Nullable"""
    @property
    def TopLeft(self) -> Cell:"""TopLeft { get; } -> Cell"""
    @property
    def TopRow(self) -> int:"""TopRow { get; } -> int"""
    def ClearStyleOverrides(self):...
    @staticmethod
    def Create(table: Table, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> CellRange:...
    def DeleteContent(self):...
    def GetCustomData(self, key: str) -> object:...
    def GetDataLink(self) -> ObjectIdCollection:...
    def GetStyleOverrides(self) -> _n_6_t_10[TableStyleOverride]:...
    def IEnumerableGetEnumerator(self) -> _n_7_t_3:...
    def SetCustomData(self, key: str, value: object):...
    def SetDataLink(self, dataLinkId: ObjectId, bUpdate: bool):...
class CellReference(_n_6_t_12):
    @property
    def Column(self) -> int:"""Column { get; set; } -> int"""
    @property
    def Row(self) -> int:"""Row { get; set; } -> int"""
class CellStates(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ContentLocked: int
    ContentModifiedAfterUpdate: int
    ContentReadOnly: int
    FormatLocked: int
    FormatModifiedAfterUpdate: int
    FormatReadOnly: int
    Linked: int
    _None: int
    value__: int
class CellType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Bool: int
    CharPtr: int
    Double: int
    HardOwnerId: int
    HardPtrId: int
    Integer: int
    ObjectId: int
    Point: int
    SoftOwnerId: int
    SoftPtrId: int
    Unknown: int
    value__: int
    Vector: int
class CenterPointConstraint(ConcentricConstraint, _n_6_t_0, _n_6_t_1):
    pass
class Circle(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def Center(self) -> _n_2_t_1:"""Center { get; set; } -> Point3d"""
    @property
    def Circumference(self) -> float:"""Circumference { get; set; } -> float"""
    @property
    def Diameter(self) -> float:"""Diameter { get; set; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Radius(self) -> float:"""Radius { get; set; } -> float"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, center: _n_2_t_1, normal: _n_2_t_3, radius: float) -> Circle:...
    def __init__(self) -> Circle:...
class ClipBoundaryType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Invalid: int
    Poly: int
    Rectangle: int
    value__: int
class ColinearConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> ColinearConstraint:...
class CollisionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    _None: int
    Solid: int
    value__: int
class Column(CellRange, ISubObject, _n_8_t_0[CellReference], typing.Iterable[typing.Any]):
    @property
    def MinimumWidth(self) -> float:"""MinimumWidth { get; } -> float"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
class ColumnsCollection(_n_8_t_0[Column], typing.Iterable[typing.Any]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def Item(self) -> Column:"""Item { get; } -> Column"""
class ColumnType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DynamicColumns: int
    NoColumns: int
    StaticColumns: int
    value__: int
class CompositeConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    @property
    def OwnedConstraints(self) -> _n_6_t_10[GeometricalConstraint]:"""OwnedConstraints { get; } -> Array"""
class CompoundObjectId(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def FullPath(self) -> ObjectIdCollection:"""FullPath { get; } -> ObjectIdCollection"""
    @property
    def IsEmpty(self) -> bool:"""IsEmpty { get; } -> bool"""
    @property
    def IsExternal(self) -> bool:"""IsExternal { get; } -> bool"""
    @property
    def IsSimpleObjectId(self) -> bool:"""IsSimpleObjectId { get; } -> bool"""
    @property
    def LeafId(self) -> ObjectId:"""LeafId { get; } -> ObjectId"""
    @property
    def Path(self) -> ObjectIdCollection:"""Path { get; } -> ObjectIdCollection"""
    @property
    def Status(self) -> CompoundObjectId.StatusType:"""Status { get; } -> CompoundObjectId.StatusType"""
    @property
    def TopId(self) -> ObjectId:"""TopId { get; } -> ObjectId"""
    @property
    def Transform(self) -> _n_2_t_6:"""Transform { get; } -> Matrix3d"""
    def __init__(self, id: ObjectId, path: ObjectIdCollection, hostDatabase: Database) -> CompoundObjectId:...
    def __init__(self, A_0: CompoundObjectId) -> CompoundObjectId:...
    def __init__(self, id: ObjectId, hostDatabase: Database) -> CompoundObjectId:...
    def __init__(self, id: ObjectId) -> CompoundObjectId:...
    def __init__(self) -> CompoundObjectId:...
    def DwgInFields(self, filer: DwgFiler, ownerVersion: int):...
    def DwgOutFields(self, filer: DwgFiler, hostDatabase: Database):...
    def DxfInFields(self, filer: DxfFiler, hostDatabase: Database, ownerVersion: int):...
    def DxfOutFields(self, filer: DxfFiler, hostDatabase: Database):...
    def IsValid(self, validityCheckingLevel: int) -> bool:...
    @staticmethod
    def NullId() -> CompoundObjectId:...
    def op_Assign(self, A_0: CompoundObjectId) -> CompoundObjectId:...
    def op_Assign(self, A_0: ObjectId) -> CompoundObjectId:...
    def op_Equality(self, A_0: CompoundObjectId) -> bool:...
    def op_Inequality(self, other: CompoundObjectId) -> bool:...
    def Remap(self, idMap: IdMapping) -> bool:...
    def Set(self, id: ObjectId, path: ObjectIdCollection, hostDatabase: Database):...
    def Set(self, compoundID: CompoundObjectId, hostDatabase: Database):...
    def Set(self, id: ObjectId, hostDatabase: Database):...
    def SetEmpty(self):...
    def SetFullPath(self, fullPath: ObjectIdCollection, hostDatabase: Database):...
    class StatusType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        CouldNotResolveNonTerminal: int
        CouldNotResolveTerminal: int
        CouldNotResolveTooEarly: int
        IncompatibleIdType: int
        Valid: int
        value__: int
        WasLoadedNowUnloaded: int
class ConcentricConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> ConcentricConstraint:...
class Constrained2PointsConstructionLine(ConstrainedConstructionLine, _n_6_t_0, _n_6_t_1):
    def __init__(self, point1: _n_2_t_1, point2: _n_2_t_1) -> Constrained2PointsConstructionLine:...
    def __init__(self) -> Constrained2PointsConstructionLine:...
class ConstrainedArc(ConstrainedCircle, _n_6_t_0, _n_6_t_1):
    @property
    def EndPoint(self) -> _n_2_t_1:"""EndPoint { get; } -> Point3d"""
    @property
    def MidPoint(self) -> _n_2_t_1:"""MidPoint { get; } -> Point3d"""
    @property
    def StartPoint(self) -> _n_2_t_1:"""StartPoint { get; } -> Point3d"""
    def __init__(self, geomDependencyId: ObjectId) -> ConstrainedArc:...
    def __init__(self) -> ConstrainedArc:...
class ConstrainedBoundedEllipse(ConstrainedEllipse, _n_6_t_0, _n_6_t_1):
    @property
    def EndPoint(self) -> _n_2_t_1:"""EndPoint { get; } -> Point3d"""
    @property
    def StartPoint(self) -> _n_2_t_1:"""StartPoint { get; } -> Point3d"""
    def __init__(self, geomDependencyId: ObjectId) -> ConstrainedBoundedEllipse:...
    def __init__(self) -> ConstrainedBoundedEllipse:...
class ConstrainedBoundedLine(ConstrainedLine, _n_6_t_0, _n_6_t_1):
    @property
    def EndPoint(self) -> _n_2_t_1:"""EndPoint { get; } -> Point3d"""
    @property
    def IsRay(self) -> bool:"""IsRay { get; } -> bool"""
    @property
    def MidPoint(self) -> _n_2_t_1:"""MidPoint { get; } -> Point3d"""
    @property
    def StartPoint(self) -> _n_2_t_1:"""StartPoint { get; } -> Point3d"""
    def __init__(self, geomDependencyId: ObjectId, ray: bool) -> ConstrainedBoundedLine:...
    def __init__(self) -> ConstrainedBoundedLine:...
class ConstrainedCircle(ConstrainedCurve, _n_6_t_0, _n_6_t_1):
    @property
    def CenterPoint(self) -> _n_2_t_1:"""CenterPoint { get; } -> Point3d"""
    @property
    def Radius(self) -> float:"""Radius { get; } -> float"""
    def __init__(self, geomDependencyId: ObjectId) -> ConstrainedCircle:...
    def __init__(self) -> ConstrainedCircle:...
class ConstrainedConstructionLine(ConstrainedLine, _n_6_t_0, _n_6_t_1):
    pass
class ConstrainedCurve(ConstrainedGeometry, _n_6_t_0, _n_6_t_1):
    @property
    def ConstrainedImplicitPoints(self) -> _n_6_t_10[ConstrainedImplicitPoint]:"""ConstrainedImplicitPoints { get; } -> Array"""
    @property
    def IsBounded(self) -> bool:"""IsBounded { get; } -> bool"""
class ConstrainedDatumLine(ConstrainedConstructionLine, _n_6_t_0, _n_6_t_1):
    def __init__(self, pointOnLine: _n_2_t_1, direction: _n_2_t_3) -> ConstrainedDatumLine:...
    def __init__(self) -> ConstrainedDatumLine:...
class ConstrainedEllipse(ConstrainedCurve, _n_6_t_0, _n_6_t_1):
    @property
    def CenterPoint(self) -> _n_2_t_1:"""CenterPoint { get; } -> Point3d"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; } -> Vector3d"""
    @property
    def MajorRadius(self) -> float:"""MajorRadius { get; } -> float"""
    @property
    def MinorRadius(self) -> float:"""MinorRadius { get; } -> float"""
    def __init__(self, geomDependencyId: ObjectId) -> ConstrainedEllipse:...
    def __init__(self) -> ConstrainedEllipse:...
class ConstrainedGeometry(ConstraintGroupNode, _n_6_t_0, _n_6_t_1):
    @property
    def ConnectedConstraints(self) -> _n_6_t_10[GeometricalConstraint]:"""ConnectedConstraints { get; } -> Array"""
    @property
    def ConnectedGeometries(self) -> _n_6_t_10[ConstrainedGeometry]:"""ConnectedGeometries { get; } -> Array"""
    @property
    def FullSubentityPaths(self) -> _n_6_t_10[FullSubentityPath]:"""FullSubentityPaths { get; } -> Array"""
    @property
    def GeomDependencyId(self) -> ObjectId:"""GeomDependencyId { get; } -> ObjectId"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def OwningRigidSet(self) -> ConstrainedRigidSet:"""OwningRigidSet { get; } -> ConstrainedRigidSet"""
    def CommonConstraints(self, otherConsGeom: ConstrainedGeometry) -> _n_6_t_10[GeometricalConstraint]:...
class ConstrainedImplicitPoint(ConstrainedPoint, _n_6_t_0, _n_6_t_1):
    @property
    def ConstrainedCurveId(self) -> _n_6_t_11:"""ConstrainedCurveId { get; } -> UInt32"""
    @property
    def PointIndex(self) -> int:"""PointIndex { get; } -> int"""
    @property
    def PointType(self) -> ImplicitPointType:"""PointType { get; } -> ImplicitPointType"""
    def __init__(self, constrCurvId: _n_6_t_11, ptype: ImplicitPointType, index: int) -> ConstrainedImplicitPoint:...
    def __init__(self) -> ConstrainedImplicitPoint:...
class ConstrainedLine(ConstrainedCurve, _n_6_t_0, _n_6_t_1):
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; } -> Vector3d"""
    @property
    def PointOnLine(self) -> _n_2_t_1:"""PointOnLine { get; } -> Point3d"""
    def __init__(self, geomDependencyId: ObjectId) -> ConstrainedLine:...
    def __init__(self) -> ConstrainedLine:...
class ConstrainedPoint(ConstrainedGeometry, _n_6_t_0, _n_6_t_1):
    @property
    def Point(self) -> _n_2_t_1:"""Point { get; } -> Point3d"""
    def __init__(self, geomDependencyId: ObjectId) -> ConstrainedPoint:...
    def __init__(self) -> ConstrainedPoint:...
class ConstrainedRigidSet(ConstrainedGeometry, _n_6_t_0, _n_6_t_1):
    @property
    def NumOfConstrainedGeoms(self) -> int:"""NumOfConstrainedGeoms { get; } -> int"""
    @property
    def Transform(self) -> _n_2_t_6:"""Transform { get; } -> Matrix3d"""
    def __init__(self, bScalable: bool, trans: _n_2_t_6) -> ConstrainedRigidSet:...
    def __init__(self) -> ConstrainedRigidSet:...
    def GetConstrainedGeomAt(self, index: int) -> ConstrainedGeometry:...
class ConstrainedSpline(ConstrainedCurve, _n_6_t_0, _n_6_t_1):
    @property
    def NumOfDefinePoints(self) -> int:"""NumOfDefinePoints { get; } -> int"""
    @property
    def NurbSpline(self) -> _n_2_t_12:"""NurbSpline { get; } -> NurbCurve3d"""
    def __init__(self, geomDependencyId: ObjectId, spline: _n_2_t_12) -> ConstrainedSpline:...
    def __init__(self) -> ConstrainedSpline:...
    def DefinePointAt(self, index: int) -> _n_2_t_1:...
class ConstraintGroupNode(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def NodeId(self) -> _n_6_t_11:"""NodeId { get; } -> UInt32"""
    @property
    def OwningConstraintGroupId(self) -> ObjectId:"""OwningConstraintGroupId { get; } -> ObjectId"""
class ConstrainType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Height: int
    TurnHeight: int
    Turns: int
    value__: int
class ContentType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BlockContent: int
    MTextContent: int
    NoneContent: int
    ToleranceContent: int
    value__: int
class Curve(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Area(self) -> float:"""Area { get; } -> float"""
    @property
    def Closed(self) -> bool:"""Closed { get; } -> bool"""
    @property
    def EndParam(self) -> float:"""EndParam { get; } -> float"""
    @property
    def EndPoint(self) -> _n_2_t_1:"""EndPoint { get; set; } -> Point3d"""
    @property
    def IsPeriodic(self) -> bool:"""IsPeriodic { get; } -> bool"""
    @property
    def Spline(self) -> Spline:"""Spline { get; } -> Spline"""
    @property
    def StartParam(self) -> float:"""StartParam { get; } -> float"""
    @property
    def StartPoint(self) -> _n_2_t_1:"""StartPoint { get; set; } -> Point3d"""
    @staticmethod
    def CreateFromGeCurve(geCurve: _n_2_t_7) -> Curve:...
    @staticmethod
    def CreateFromGeCurve(geCurve: _n_2_t_7, tolerance: _n_2_t_5) -> Curve:...
    @staticmethod
    def CreateFromGeCurve(geCurve: _n_2_t_7, __unnamed001: _n_2_t_3) -> Curve:...
    @staticmethod
    def CreateFromGeCurve(geCurve: _n_2_t_7, __unnamed001: _n_2_t_3, tolerance: _n_2_t_5) -> Curve:...
    def Extend(self, extendStart: bool, toPoint: _n_2_t_1):...
    def Extend(self, newParameter: float):...
    def GetClosestPointTo(self, givenPoint: _n_2_t_1, direction: _n_2_t_3, extend: bool) -> _n_2_t_1:...
    def GetClosestPointTo(self, givenPoint: _n_2_t_1, extend: bool) -> _n_2_t_1:...
    def GetDistanceAtParameter(self, value: float) -> float:...
    def GetDistAtPoint(self, point: _n_2_t_1) -> float:...
    def GetFirstDerivative(self, point: _n_2_t_1) -> _n_2_t_3:...
    def GetFirstDerivative(self, value: float) -> _n_2_t_3:...
    def GetGeCurve(self) -> _n_2_t_7:...
    def GetGeCurve(self, tolerance: _n_2_t_5) -> _n_2_t_7:...
    def GetOffsetCurves(self, offsetDist: float) -> DBObjectCollection:...
    def GetOffsetCurvesGivenPlaneNormal(self, normal: _n_2_t_3, offsetDist: float) -> DBObjectCollection:...
    def GetOrthoProjectedCurve(self, planeToProjectOn: _n_2_t_4) -> Curve:...
    def GetParameterAtDistance(self, dist: float) -> float:...
    def GetParameterAtPoint(self, point: _n_2_t_1) -> float:...
    def GetPointAtDist(self, value: float) -> _n_2_t_1:...
    def GetPointAtParameter(self, value: float) -> _n_2_t_1:...
    def GetProjectedCurve(self, planeToProjectOn: _n_2_t_4, projectionDirection: _n_2_t_3) -> Curve:...
    def GetSecondDerivative(self, point: _n_2_t_1) -> _n_2_t_3:...
    def GetSecondDerivative(self, value: float) -> _n_2_t_3:...
    def GetSplitCurves(self, points: _n_2_t_10) -> DBObjectCollection:...
    def GetSplitCurves(self, value: _n_2_t_13) -> DBObjectCollection:...
    def ReverseCurve(self):...
    def SetFromGeCurve(self, geCurve: _n_2_t_7):...
    def SetFromGeCurve(self, geCurve: _n_2_t_7, tolerance: _n_2_t_5):...
    def SetFromGeCurve(self, geCurve: _n_2_t_7, __unnamed001: _n_2_t_3):...
    def SetFromGeCurve(self, geCurve: _n_2_t_7, __unnamed001: _n_2_t_3, tolerance: _n_2_t_5):...
class CustomObjectSnapMode(_n_5_t_3, _n_6_t_0):
    @property
    def Bitmap(self) -> _n_11_t_0:"""Bitmap { get; } -> Bitmap"""
    @property
    def DisplayString(self) -> str:"""DisplayString { get; } -> str"""
    @property
    def GlobalModeString(self) -> str:"""GlobalModeString { get; } -> str"""
    @property
    def Glyph(self) -> _n_3_t_1:"""Glyph { get; } -> Glyph"""
    @property
    def GlyphSize(self) -> int:"""GlyphSize { get; } -> int"""
    @property
    def LocalModeString(self) -> str:"""LocalModeString { get; } -> str"""
    @property
    def ToolTipText(self) -> str:"""ToolTipText { get; } -> str"""
    def __init__(self, localModeString: str, globalModeString: str, toolTipText: str, glyph: _n_3_t_1, bitmap: _n_11_t_0, displayString: str) -> CustomObjectSnapMode:...
    def __init__(self, localModeString: str, globalModeString: str, toolTipText: str, glyph: _n_3_t_1) -> CustomObjectSnapMode:...
    @staticmethod
    def Activate(mode: str):...
    def ApplyToEntityType(self, entity: _n_5_t_0, callback: AddObjectSnapInfo):...
    @staticmethod
    def Deactivate(mode: str):...
    @staticmethod
    def IsActive(mode: str) -> bool:...
    def RemoveFromEntityType(self, entity: _n_5_t_0):...
class CustomScale(_n_6_t_12):
    @property
    def Denominator(self) -> float:"""Denominator { get; } -> float"""
    @property
    def Numerator(self) -> float:"""Numerator { get; } -> float"""
    def __init__(self, numerator: float, denominator: float) -> CustomScale:...
    def IsEqualTo(self, a: CustomScale) -> bool:...
    def IsEqualTo(self, a: CustomScale, tolerance: _n_2_t_5) -> bool:...
class DataAdapter(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def DataAdapterId(self) -> str:"""DataAdapterId { get; } -> str"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def CreateDataObject(self, dataLink: DataLink) -> LinkedData:...
    def GetSourceFiles(self, dataLink: DataLink, nContext: DataLinkGetSourceContext) -> _n_7_t_1:...
    def IsValid(self, dataLink: DataLink) -> bool:...
    def RepathSourceFiles(self, dataLink: DataLink, sBasePath: str, nOption: PathOption):...
    def SourceFileModified(self, dataLink: DataLink, sModifiedFile: str, pAction: UpdateAction):...
    def Update(self, dataLink: DataLink, data: LinkedData, direction: UpdateDirection, option: UpdateOption):...
class DataAdapterManager(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def AdapterProviderCount(self) -> int:"""AdapterProviderCount { get; } -> int"""
    @staticmethod
    def GetAdapterProvider(index: int) -> DataAdapterProvider:...
    @staticmethod
    def GetDataAdapter(adapterId: str) -> DataAdapter:...
    @staticmethod
    def RegisterAdapterProvider(provider: DataAdapterProvider):...
    @staticmethod
    def UnregisterAdapterProvider(provider: DataAdapterProvider):...
class DataAdapterProvider(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def GetDataAdapter(self, adapterId: str) -> DataAdapter:...
class DataAdapterSourceFilesException(_n_5_t_4, _n_15_t_0, _n_14_t_1):
    @property
    def FileNameList(self) -> _n_7_t_1:"""FileNameList { get; set; } -> ArrayList"""
    def __init__(self, es: _n_5_t_1, message: str, innerException: _n_6_t_16, filelist: _n_7_t_1) -> DataAdapterSourceFilesException:...
    def __init__(self, es: _n_5_t_1, message: str, filelist: _n_7_t_1) -> DataAdapterSourceFilesException:...
    def __init__(self, es: _n_5_t_1, filelist: _n_7_t_1) -> DataAdapterSourceFilesException:...
    def __init__(self, filelist: _n_7_t_1) -> DataAdapterSourceFilesException:...
class Database(_n_5_t_2, _n_6_t_0, _n_6_t_1, _n_12_t_0):
    @property
    def AcadDatabase(self) -> object:"""AcadDatabase { get; } -> object"""
    @property
    def AllowExtendedNames(self) -> bool:"""AllowExtendedNames { get; set; } -> bool"""
    @property
    def Angbase(self) -> float:"""Angbase { get; set; } -> float"""
    @property
    def Angdir(self) -> bool:"""Angdir { get; set; } -> bool"""
    @property
    def AnnoAllVisible(self) -> bool:"""AnnoAllVisible { get; set; } -> bool"""
    @property
    def AnnotativeDwg(self) -> bool:"""AnnotativeDwg { get; set; } -> bool"""
    @property
    def ApproxNumObjects(self) -> int:"""ApproxNumObjects { get; } -> int"""
    @property
    def Attmode(self) -> int:"""Attmode { get; set; } -> int"""
    @property
    def Aunits(self) -> int:"""Aunits { get; set; } -> int"""
    @property
    def Auprec(self) -> int:"""Auprec { get; set; } -> int"""
    @property
    def BlockTableId(self) -> ObjectId:"""BlockTableId { get; } -> ObjectId"""
    @property
    def ByBlockLinetype(self) -> ObjectId:"""ByBlockLinetype { get; } -> ObjectId"""
    @property
    def ByLayerLinetype(self) -> ObjectId:"""ByLayerLinetype { get; } -> ObjectId"""
    @property
    def CameraDisplay(self) -> bool:"""CameraDisplay { get; set; } -> bool"""
    @property
    def CameraHeight(self) -> float:"""CameraHeight { get; set; } -> float"""
    @property
    def Cannoscale(self) -> AnnotationScale:"""Cannoscale { get; set; } -> AnnotationScale"""
    @property
    def Cecolor(self) -> _n_0_t_0:"""Cecolor { get; set; } -> Color"""
    @property
    def Celtscale(self) -> float:"""Celtscale { get; set; } -> float"""
    @property
    def Celtype(self) -> ObjectId:"""Celtype { get; set; } -> ObjectId"""
    @property
    def Celweight(self) -> LineWeight:"""Celweight { get; set; } -> LineWeight"""
    @property
    def Cetransparency(self) -> _n_0_t_1:"""Cetransparency { get; set; } -> Transparency"""
    @property
    def Chamfera(self) -> float:"""Chamfera { get; set; } -> float"""
    @property
    def Chamferb(self) -> float:"""Chamferb { get; set; } -> float"""
    @property
    def Chamferc(self) -> float:"""Chamferc { get; set; } -> float"""
    @property
    def Chamferd(self) -> float:"""Chamferd { get; set; } -> float"""
    @property
    def Clayer(self) -> ObjectId:"""Clayer { get; set; } -> ObjectId"""
    @property
    def Cmaterial(self) -> ObjectId:"""Cmaterial { get; set; } -> ObjectId"""
    @property
    def Cmljust(self) -> int:"""Cmljust { get; set; } -> int"""
    @property
    def Cmlscale(self) -> float:"""Cmlscale { get; set; } -> float"""
    @property
    def CmlstyleID(self) -> ObjectId:"""CmlstyleID { get; set; } -> ObjectId"""
    @property
    def ColorDictionaryId(self) -> ObjectId:"""ColorDictionaryId { get; } -> ObjectId"""
    @property
    def ContinuousLinetype(self) -> ObjectId:"""ContinuousLinetype { get; } -> ObjectId"""
    @property
    def Cshadow(self) -> int:"""Cshadow { get; set; } -> int"""
    @property
    def CurrentSpaceId(self) -> ObjectId:"""CurrentSpaceId { get; } -> ObjectId"""
    @property
    def CurrentViewportTableRecordId(self) -> ObjectId:"""CurrentViewportTableRecordId { get; } -> ObjectId"""
    @property
    def DataLinkDictionaryId(self) -> ObjectId:"""DataLinkDictionaryId { get; } -> ObjectId"""
    @property
    def DataLinkManager(self) -> DataLinkManager:"""DataLinkManager { get; } -> DataLinkManager"""
    @property
    def DetailViewStyle(self) -> ObjectId:"""DetailViewStyle { get; set; } -> ObjectId"""
    @property
    def DetailViewStyleDictionaryId(self) -> ObjectId:"""DetailViewStyleDictionaryId { get; } -> ObjectId"""
    @property
    def DgnFrame(self) -> int:"""DgnFrame { get; set; } -> int"""
    @property
    def Dimadec(self) -> int:"""Dimadec { get; set; } -> int"""
    @property
    def Dimalt(self) -> bool:"""Dimalt { get; set; } -> bool"""
    @property
    def Dimaltd(self) -> int:"""Dimaltd { get; set; } -> int"""
    @property
    def Dimaltf(self) -> float:"""Dimaltf { get; set; } -> float"""
    @property
    def Dimaltrnd(self) -> float:"""Dimaltrnd { get; set; } -> float"""
    @property
    def Dimalttd(self) -> int:"""Dimalttd { get; set; } -> int"""
    @property
    def Dimalttz(self) -> int:"""Dimalttz { get; set; } -> int"""
    @property
    def Dimaltu(self) -> int:"""Dimaltu { get; set; } -> int"""
    @property
    def Dimaltz(self) -> int:"""Dimaltz { get; set; } -> int"""
    @property
    def Dimapost(self) -> str:"""Dimapost { get; set; } -> str"""
    @property
    def Dimarcsym(self) -> int:"""Dimarcsym { get; set; } -> int"""
    @property
    def Dimaso(self) -> bool:"""Dimaso { get; set; } -> bool"""
    @property
    def DimAssoc(self) -> int:"""DimAssoc { get; set; } -> int"""
    @property
    def Dimasz(self) -> float:"""Dimasz { get; set; } -> float"""
    @property
    def Dimatfit(self) -> int:"""Dimatfit { get; set; } -> int"""
    @property
    def Dimaunit(self) -> int:"""Dimaunit { get; set; } -> int"""
    @property
    def Dimazin(self) -> int:"""Dimazin { get; set; } -> int"""
    @property
    def Dimblk(self) -> ObjectId:"""Dimblk { get; set; } -> ObjectId"""
    @property
    def Dimblk1(self) -> ObjectId:"""Dimblk1 { get; set; } -> ObjectId"""
    @property
    def Dimblk2(self) -> ObjectId:"""Dimblk2 { get; set; } -> ObjectId"""
    @property
    def Dimcen(self) -> float:"""Dimcen { get; set; } -> float"""
    @property
    def Dimclrd(self) -> _n_0_t_0:"""Dimclrd { get; set; } -> Color"""
    @property
    def Dimclre(self) -> _n_0_t_0:"""Dimclre { get; set; } -> Color"""
    @property
    def Dimclrt(self) -> _n_0_t_0:"""Dimclrt { get; set; } -> Color"""
    @property
    def Dimdec(self) -> int:"""Dimdec { get; set; } -> int"""
    @property
    def Dimdle(self) -> float:"""Dimdle { get; set; } -> float"""
    @property
    def Dimdli(self) -> float:"""Dimdli { get; set; } -> float"""
    @property
    def Dimdsep(self) -> _n_6_t_18:"""Dimdsep { get; set; } -> Char"""
    @property
    def Dimexe(self) -> float:"""Dimexe { get; set; } -> float"""
    @property
    def Dimexo(self) -> float:"""Dimexo { get; set; } -> float"""
    @property
    def Dimfrac(self) -> int:"""Dimfrac { get; set; } -> int"""
    @property
    def Dimfxlen(self) -> float:"""Dimfxlen { get; set; } -> float"""
    @property
    def DimfxlenOn(self) -> bool:"""DimfxlenOn { get; set; } -> bool"""
    @property
    def Dimgap(self) -> float:"""Dimgap { get; set; } -> float"""
    @property
    def Dimjogang(self) -> float:"""Dimjogang { get; set; } -> float"""
    @property
    def Dimjust(self) -> int:"""Dimjust { get; set; } -> int"""
    @property
    def Dimldrblk(self) -> ObjectId:"""Dimldrblk { get; set; } -> ObjectId"""
    @property
    def Dimlfac(self) -> float:"""Dimlfac { get; set; } -> float"""
    @property
    def Dimlim(self) -> bool:"""Dimlim { get; set; } -> bool"""
    @property
    def Dimltex1(self) -> ObjectId:"""Dimltex1 { get; set; } -> ObjectId"""
    @property
    def Dimltex2(self) -> ObjectId:"""Dimltex2 { get; set; } -> ObjectId"""
    @property
    def Dimltype(self) -> ObjectId:"""Dimltype { get; set; } -> ObjectId"""
    @property
    def Dimlunit(self) -> int:"""Dimlunit { get; set; } -> int"""
    @property
    def Dimlwd(self) -> LineWeight:"""Dimlwd { get; set; } -> LineWeight"""
    @property
    def Dimlwe(self) -> LineWeight:"""Dimlwe { get; set; } -> LineWeight"""
    @property
    def Dimpost(self) -> str:"""Dimpost { get; set; } -> str"""
    @property
    def Dimrnd(self) -> float:"""Dimrnd { get; set; } -> float"""
    @property
    def Dimsah(self) -> bool:"""Dimsah { get; set; } -> bool"""
    @property
    def Dimscale(self) -> float:"""Dimscale { get; set; } -> float"""
    @property
    def Dimsd1(self) -> bool:"""Dimsd1 { get; set; } -> bool"""
    @property
    def Dimsd2(self) -> bool:"""Dimsd2 { get; set; } -> bool"""
    @property
    def Dimse1(self) -> bool:"""Dimse1 { get; set; } -> bool"""
    @property
    def Dimse2(self) -> bool:"""Dimse2 { get; set; } -> bool"""
    @property
    def Dimsho(self) -> bool:"""Dimsho { get; set; } -> bool"""
    @property
    def Dimsoxd(self) -> bool:"""Dimsoxd { get; set; } -> bool"""
    @property
    def Dimstyle(self) -> ObjectId:"""Dimstyle { get; set; } -> ObjectId"""
    @property
    def DimStyleTableId(self) -> ObjectId:"""DimStyleTableId { get; } -> ObjectId"""
    @property
    def Dimtad(self) -> int:"""Dimtad { get; set; } -> int"""
    @property
    def Dimtdec(self) -> int:"""Dimtdec { get; set; } -> int"""
    @property
    def Dimtfac(self) -> float:"""Dimtfac { get; set; } -> float"""
    @property
    def Dimtfill(self) -> int:"""Dimtfill { get; set; } -> int"""
    @property
    def Dimtfillclr(self) -> _n_0_t_0:"""Dimtfillclr { get; set; } -> Color"""
    @property
    def Dimtih(self) -> bool:"""Dimtih { get; set; } -> bool"""
    @property
    def Dimtix(self) -> bool:"""Dimtix { get; set; } -> bool"""
    @property
    def Dimtm(self) -> float:"""Dimtm { get; set; } -> float"""
    @property
    def Dimtmove(self) -> int:"""Dimtmove { get; set; } -> int"""
    @property
    def Dimtofl(self) -> bool:"""Dimtofl { get; set; } -> bool"""
    @property
    def Dimtoh(self) -> bool:"""Dimtoh { get; set; } -> bool"""
    @property
    def Dimtol(self) -> bool:"""Dimtol { get; set; } -> bool"""
    @property
    def Dimtolj(self) -> int:"""Dimtolj { get; set; } -> int"""
    @property
    def Dimtp(self) -> float:"""Dimtp { get; set; } -> float"""
    @property
    def Dimtsz(self) -> float:"""Dimtsz { get; set; } -> float"""
    @property
    def Dimtvp(self) -> float:"""Dimtvp { get; set; } -> float"""
    @property
    def Dimtxsty(self) -> ObjectId:"""Dimtxsty { get; set; } -> ObjectId"""
    @property
    def Dimtxt(self) -> float:"""Dimtxt { get; set; } -> float"""
    @property
    def Dimtxtdirection(self) -> bool:"""Dimtxtdirection { get; set; } -> bool"""
    @property
    def Dimtzin(self) -> int:"""Dimtzin { get; set; } -> int"""
    @property
    def Dimupt(self) -> bool:"""Dimupt { get; set; } -> bool"""
    @property
    def Dimzin(self) -> int:"""Dimzin { get; set; } -> int"""
    @property
    def DispSilh(self) -> bool:"""DispSilh { get; set; } -> bool"""
    @property
    def dragvs(self) -> ObjectId:"""dragvs { get; set; } -> ObjectId"""
    @property
    def DrawOrderCtl(self) -> _n_6_t_19:"""DrawOrderCtl { get; set; } -> Byte"""
    @property
    def DwfFrame(self) -> int:"""DwfFrame { get; set; } -> int"""
    @property
    def DwgFileWasSavedByAutodeskSoftware(self) -> bool:"""DwgFileWasSavedByAutodeskSoftware { get; } -> bool"""
    @property
    def DxEval(self) -> int:"""DxEval { get; set; } -> int"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def EndCaps(self) -> EndCap:"""EndCaps { get; set; } -> EndCap"""
    @property
    def Extmax(self) -> _n_2_t_1:"""Extmax { get; set; } -> Point3d"""
    @property
    def Extmin(self) -> _n_2_t_1:"""Extmin { get; set; } -> Point3d"""
    @property
    def Facetres(self) -> float:"""Facetres { get; set; } -> float"""
    @property
    def FileDependencyManager(self) -> FileDependencyManager:"""FileDependencyManager { get; } -> FileDependencyManager"""
    @property
    def Filename(self) -> str:"""Filename { get; } -> str"""
    @property
    def Filletrad(self) -> float:"""Filletrad { get; set; } -> float"""
    @property
    def Fillmode(self) -> bool:"""Fillmode { get; set; } -> bool"""
    @property
    def FingerprintGuid(self) -> str:"""FingerprintGuid { get; set; } -> str"""
    @property
    def GeoDataObject(self) -> ObjectId:"""GeoDataObject { get; } -> ObjectId"""
    @property
    def GroupDictionaryId(self) -> ObjectId:"""GroupDictionaryId { get; } -> ObjectId"""
    @property
    def HaloGap(self) -> int:"""HaloGap { get; set; } -> int"""
    @property
    def Handseed(self) -> Handle:"""Handseed { get; set; } -> Handle"""
    @property
    def HideText(self) -> int:"""HideText { get; set; } -> int"""
    @property
    def HomeView(self) -> DbHomeView:"""HomeView { get; set; } -> DbHomeView"""
    @property
    def HpInherit(self) -> bool:"""HpInherit { get; set; } -> bool"""
    @property
    def HpOrigin(self) -> _n_2_t_0:"""HpOrigin { get; set; } -> Point2d"""
    @property
    def HyperlinkBase(self) -> str:"""HyperlinkBase { get; set; } -> str"""
    @property
    def Indexctl(self) -> int:"""Indexctl { get; set; } -> int"""
    @property
    def Insbase(self) -> _n_2_t_1:"""Insbase { get; set; } -> Point3d"""
    @property
    def Insunits(self) -> UnitsValue:"""Insunits { get; set; } -> UnitsValue"""
    @property
    def Interferecolor(self) -> _n_0_t_0:"""Interferecolor { get; set; } -> Color"""
    @property
    def Interfereobjvs(self) -> ObjectId:"""Interfereobjvs { get; set; } -> ObjectId"""
    @property
    def Interferevpvs(self) -> ObjectId:"""Interferevpvs { get; set; } -> ObjectId"""
    @property
    def IntersectColor(self) -> int:"""IntersectColor { get; set; } -> int"""
    @property
    def IntersectDisplay(self) -> int:"""IntersectDisplay { get; set; } -> int"""
    @property
    def Isolines(self) -> int:"""Isolines { get; set; } -> int"""
    @property
    def IsPartiallyOpened(self) -> bool:"""IsPartiallyOpened { get; } -> bool"""
    @property
    def JoinStyle(self) -> JoinStyle:"""JoinStyle { get; set; } -> JoinStyle"""
    @property
    def LastSavedAsMaintenanceVersion(self) -> MaintenanceReleaseVersion:"""LastSavedAsMaintenanceVersion { get; } -> MaintenanceReleaseVersion"""
    @property
    def LastSavedAsVersion(self) -> DwgVersion:"""LastSavedAsVersion { get; } -> DwgVersion"""
    @property
    def Latitude(self) -> float:"""Latitude { get; set; } -> float"""
    @property
    def LayerEval(self) -> int:"""LayerEval { get; set; } -> int"""
    @property
    def LayerFilters(self) -> _n_4_t_0:"""LayerFilters { get; set; } -> LayerFilterTree"""
    @property
    def LayerNotify(self) -> int:"""LayerNotify { get; set; } -> int"""
    @property
    def LayerStateManager(self) -> LayerStateManager:"""LayerStateManager { get; } -> LayerStateManager"""
    @property
    def LayerTableId(self) -> ObjectId:"""LayerTableId { get; } -> ObjectId"""
    @property
    def LayerZero(self) -> ObjectId:"""LayerZero { get; } -> ObjectId"""
    @property
    def LayoutDictionaryId(self) -> ObjectId:"""LayoutDictionaryId { get; } -> ObjectId"""
    @property
    def LensLength(self) -> float:"""LensLength { get; set; } -> float"""
    @property
    def LightGlyphDisplay(self) -> int:"""LightGlyphDisplay { get; set; } -> int"""
    @property
    def LightingUnits(self) -> _n_6_t_19:"""LightingUnits { get; set; } -> Byte"""
    @property
    def LightsInBlocks(self) -> bool:"""LightsInBlocks { get; set; } -> bool"""
    @property
    def Limcheck(self) -> bool:"""Limcheck { get; set; } -> bool"""
    @property
    def Limmax(self) -> _n_2_t_0:"""Limmax { get; set; } -> Point2d"""
    @property
    def Limmin(self) -> _n_2_t_0:"""Limmin { get; set; } -> Point2d"""
    @property
    def LinetypeTableId(self) -> ObjectId:"""LinetypeTableId { get; } -> ObjectId"""
    @property
    def LineWeightDisplay(self) -> bool:"""LineWeightDisplay { get; set; } -> bool"""
    @property
    def LoftAng1(self) -> float:"""LoftAng1 { get; set; } -> float"""
    @property
    def LoftAng2(self) -> float:"""LoftAng2 { get; set; } -> float"""
    @property
    def LoftMag1(self) -> float:"""LoftMag1 { get; set; } -> float"""
    @property
    def LoftMag2(self) -> float:"""LoftMag2 { get; set; } -> float"""
    @property
    def LoftNormals(self) -> int:"""LoftNormals { get; set; } -> int"""
    @property
    def LoftParam(self) -> int:"""LoftParam { get; set; } -> int"""
    @property
    def Longitude(self) -> float:"""Longitude { get; set; } -> float"""
    @property
    def Ltscale(self) -> float:"""Ltscale { get; set; } -> float"""
    @property
    def Lunits(self) -> int:"""Lunits { get; set; } -> int"""
    @property
    def Luprec(self) -> int:"""Luprec { get; set; } -> int"""
    @property
    def MaintenanceReleaseVersion(self) -> int:"""MaintenanceReleaseVersion { get; } -> int"""
    @property
    def MaterialDictionaryId(self) -> ObjectId:"""MaterialDictionaryId { get; } -> ObjectId"""
    @property
    def Maxactvp(self) -> int:"""Maxactvp { get; set; } -> int"""
    @property
    def Measurement(self) -> MeasurementValue:"""Measurement { get; set; } -> MeasurementValue"""
    @property
    def Menu(self) -> str:"""Menu { get; } -> str"""
    @property
    def Mirrtext(self) -> bool:"""Mirrtext { get; set; } -> bool"""
    @property
    def MLeaderstyle(self) -> ObjectId:"""MLeaderstyle { get; set; } -> ObjectId"""
    @property
    def MLeaderStyleDictionaryId(self) -> ObjectId:"""MLeaderStyleDictionaryId { get; } -> ObjectId"""
    @property
    def MLStyleDictionaryId(self) -> ObjectId:"""MLStyleDictionaryId { get; } -> ObjectId"""
    @property
    def MsLtScale(self) -> bool:"""MsLtScale { get; set; } -> bool"""
    @property
    def MsOleScale(self) -> float:"""MsOleScale { get; set; } -> float"""
    @property
    def NamedObjectsDictionaryId(self) -> ObjectId:"""NamedObjectsDictionaryId { get; } -> ObjectId"""
    @property
    def NorthDirection(self) -> float:"""NorthDirection { get; set; } -> float"""
    @property
    def NumberOfSaves(self) -> int:"""NumberOfSaves { get; } -> int"""
    @property
    def ObjectContextManager(self) -> ObjectContextManager:"""ObjectContextManager { get; } -> ObjectContextManager"""
    @property
    def ObscuredColor(self) -> int:"""ObscuredColor { get; set; } -> int"""
    @property
    def ObscuredLineType(self) -> int:"""ObscuredLineType { get; set; } -> int"""
    @property
    def OleStartUp(self) -> bool:"""OleStartUp { get; set; } -> bool"""
    @property
    def OriginalFileMaintenanceVersion(self) -> MaintenanceReleaseVersion:"""OriginalFileMaintenanceVersion { get; } -> MaintenanceReleaseVersion"""
    @property
    def OriginalFileName(self) -> str:"""OriginalFileName { get; } -> str"""
    @property
    def OriginalFileSavedByMaintenanceVersion(self) -> MaintenanceReleaseVersion:"""OriginalFileSavedByMaintenanceVersion { get; } -> MaintenanceReleaseVersion"""
    @property
    def OriginalFileSavedByVersion(self) -> DwgVersion:"""OriginalFileSavedByVersion { get; } -> DwgVersion"""
    @property
    def OriginalFileVersion(self) -> DwgVersion:"""OriginalFileVersion { get; } -> DwgVersion"""
    @property
    def Orthomode(self) -> bool:"""Orthomode { get; set; } -> bool"""
    @property
    def PaperSpaceVportId(self) -> ObjectId:"""PaperSpaceVportId { get; } -> ObjectId"""
    @property
    def PdfFrame(self) -> int:"""PdfFrame { get; set; } -> int"""
    @property
    def Pdmode(self) -> int:"""Pdmode { get; set; } -> int"""
    @property
    def Pdsize(self) -> float:"""Pdsize { get; set; } -> float"""
    @property
    def Pelevation(self) -> float:"""Pelevation { get; set; } -> float"""
    @property
    def Pextmax(self) -> _n_2_t_1:"""Pextmax { get; set; } -> Point3d"""
    @property
    def Pextmin(self) -> _n_2_t_1:"""Pextmin { get; set; } -> Point3d"""
    @property
    def Pinsbase(self) -> _n_2_t_1:"""Pinsbase { get; set; } -> Point3d"""
    @property
    def Plimcheck(self) -> bool:"""Plimcheck { get; set; } -> bool"""
    @property
    def Plimmax(self) -> _n_2_t_0:"""Plimmax { get; set; } -> Point2d"""
    @property
    def Plimmin(self) -> _n_2_t_0:"""Plimmin { get; set; } -> Point2d"""
    @property
    def PlineEllipse(self) -> bool:"""PlineEllipse { get; set; } -> bool"""
    @property
    def Plinegen(self) -> bool:"""Plinegen { get; set; } -> bool"""
    @property
    def Plinewid(self) -> float:"""Plinewid { get; set; } -> float"""
    @property
    def PlotSettingsDictionaryId(self) -> ObjectId:"""PlotSettingsDictionaryId { get; } -> ObjectId"""
    @property
    def PlotStyleMode(self) -> bool:"""PlotStyleMode { get; } -> bool"""
    @property
    def PlotStyleNameDictionaryId(self) -> ObjectId:"""PlotStyleNameDictionaryId { get; } -> ObjectId"""
    @property
    def PlotStyleNameId(self) -> PlotStyleDescriptor:"""PlotStyleNameId { get; set; } -> PlotStyleDescriptor"""
    @property
    def ProjectName(self) -> str:"""ProjectName { get; set; } -> str"""
    @property
    def Psltscale(self) -> bool:"""Psltscale { get; set; } -> bool"""
    @property
    def PsolHeight(self) -> float:"""PsolHeight { get; set; } -> float"""
    @property
    def PsolWidth(self) -> float:"""PsolWidth { get; set; } -> float"""
    @property
    def Pucs(self) -> _n_2_t_2:"""Pucs { set; } -> CoordinateSystem3d"""
    @property
    def PucsBase(self) -> ObjectId:"""PucsBase { get; set; } -> ObjectId"""
    @property
    def Pucsname(self) -> ObjectId:"""Pucsname { get; set; } -> ObjectId"""
    @property
    def Pucsorg(self) -> _n_2_t_1:"""Pucsorg { get; } -> Point3d"""
    @property
    def PucsOrthographic(self) -> OrthographicView:"""PucsOrthographic { get; } -> OrthographicView"""
    @property
    def Pucsxdir(self) -> _n_2_t_3:"""Pucsxdir { get; } -> Vector3d"""
    @property
    def Pucsydir(self) -> _n_2_t_3:"""Pucsydir { get; } -> Vector3d"""
    @property
    def Qtextmode(self) -> bool:"""Qtextmode { get; set; } -> bool"""
    @property
    def RegAppTableId(self) -> ObjectId:"""RegAppTableId { get; } -> ObjectId"""
    @property
    def Regenmode(self) -> bool:"""Regenmode { get; set; } -> bool"""
    @property
    def RetainOriginalThumbnailBitmap(self) -> bool:"""RetainOriginalThumbnailBitmap { get; set; } -> bool"""
    @property
    def Saveproxygraphics(self) -> int:"""Saveproxygraphics { get; set; } -> int"""
    @property
    def SectionManagerId(self) -> ObjectId:"""SectionManagerId { get; } -> ObjectId"""
    @property
    def SectionViewStyle(self) -> ObjectId:"""SectionViewStyle { get; set; } -> ObjectId"""
    @property
    def SectionViewStyleDictionaryId(self) -> ObjectId:"""SectionViewStyleDictionaryId { get; } -> ObjectId"""
    @property
    def SecurityParameters(self) -> SecurityParameters:"""SecurityParameters { get; set; } -> SecurityParameters"""
    @property
    def Shadedge(self) -> int:"""Shadedge { get; set; } -> int"""
    @property
    def Shadedif(self) -> int:"""Shadedif { get; set; } -> int"""
    @property
    def ShadowPlaneLocation(self) -> float:"""ShadowPlaneLocation { get; set; } -> float"""
    @property
    def ShowHist(self) -> int:"""ShowHist { get; set; } -> int"""
    @property
    def Sketchinc(self) -> float:"""Sketchinc { get; set; } -> float"""
    @property
    def Skpoly(self) -> bool:"""Skpoly { get; set; } -> bool"""
    @property
    def SolidHist(self) -> int:"""SolidHist { get; set; } -> int"""
    @property
    def SortEnts(self) -> int:"""SortEnts { get; set; } -> int"""
    @property
    def Splframe(self) -> bool:"""Splframe { get; set; } -> bool"""
    @property
    def Splinesegs(self) -> int:"""Splinesegs { get; set; } -> int"""
    @property
    def Splinetype(self) -> int:"""Splinetype { get; set; } -> int"""
    @property
    def StepSize(self) -> float:"""StepSize { get; set; } -> float"""
    @property
    def StepsPerSec(self) -> float:"""StepsPerSec { get; set; } -> float"""
    @property
    def StyleSheet(self) -> str:"""StyleSheet { get; set; } -> str"""
    @property
    def SummaryInfo(self) -> DatabaseSummaryInfo:"""SummaryInfo { get; set; } -> DatabaseSummaryInfo"""
    @property
    def Surftab1(self) -> int:"""Surftab1 { get; set; } -> int"""
    @property
    def Surftab2(self) -> int:"""Surftab2 { get; set; } -> int"""
    @property
    def Surftype(self) -> int:"""Surftype { get; set; } -> int"""
    @property
    def Surfu(self) -> int:"""Surfu { get; set; } -> int"""
    @property
    def Surfv(self) -> int:"""Surfv { get; set; } -> int"""
    @property
    def Tablestyle(self) -> ObjectId:"""Tablestyle { get; set; } -> ObjectId"""
    @property
    def TableStyleDictionaryId(self) -> ObjectId:"""TableStyleDictionaryId { get; } -> ObjectId"""
    @property
    def Tdcreate(self) -> _n_6_t_20:"""Tdcreate { get; } -> DateTime"""
    @property
    def Tdindwg(self) -> _n_6_t_21:"""Tdindwg { get; } -> TimeSpan"""
    @property
    def Tducreate(self) -> _n_6_t_20:"""Tducreate { get; } -> DateTime"""
    @property
    def Tdupdate(self) -> _n_6_t_20:"""Tdupdate { get; } -> DateTime"""
    @property
    def Tdusrtimer(self) -> _n_6_t_21:"""Tdusrtimer { get; } -> TimeSpan"""
    @property
    def Tduupdate(self) -> _n_6_t_20:"""Tduupdate { get; } -> DateTime"""
    @property
    def Textsize(self) -> float:"""Textsize { get; set; } -> float"""
    @property
    def Textstyle(self) -> ObjectId:"""Textstyle { get; set; } -> ObjectId"""
    @property
    def TextStyleTableId(self) -> ObjectId:"""TextStyleTableId { get; } -> ObjectId"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    @property
    def ThumbnailBitmap(self) -> _n_11_t_0:"""ThumbnailBitmap { get; set; } -> Bitmap"""
    @property
    def TileMode(self) -> bool:"""TileMode { get; set; } -> bool"""
    @property
    def TileModeLightSynch(self) -> int:"""TileModeLightSynch { get; set; } -> int"""
    @property
    def TimeZone(self) -> TimeZone:"""TimeZone { get; set; } -> TimeZone"""
    @property
    def Tracewid(self) -> float:"""Tracewid { get; set; } -> float"""
    @property
    def TransactionManager(self) -> TransactionManager:"""TransactionManager { get; } -> TransactionManager"""
    @property
    def Treedepth(self) -> int:"""Treedepth { get; set; } -> int"""
    @property
    def TStackAlign(self) -> int:"""TStackAlign { get; set; } -> int"""
    @property
    def TstackSize(self) -> int:"""TstackSize { get; set; } -> int"""
    @property
    def Ucs(self) -> _n_2_t_2:"""Ucs { set; } -> CoordinateSystem3d"""
    @property
    def UcsBase(self) -> ObjectId:"""UcsBase { get; set; } -> ObjectId"""
    @property
    def Ucsname(self) -> ObjectId:"""Ucsname { get; set; } -> ObjectId"""
    @property
    def Ucsorg(self) -> _n_2_t_1:"""Ucsorg { get; } -> Point3d"""
    @property
    def UcsOrthographic(self) -> OrthographicView:"""UcsOrthographic { get; } -> OrthographicView"""
    @property
    def UcsTableId(self) -> ObjectId:"""UcsTableId { get; } -> ObjectId"""
    @property
    def Ucsxdir(self) -> _n_2_t_3:"""Ucsxdir { get; } -> Vector3d"""
    @property
    def Ucsydir(self) -> _n_2_t_3:"""Ucsydir { get; } -> Vector3d"""
    @property
    def UndoRecording(self) -> bool:"""UndoRecording { get; } -> bool"""
    @property
    def Unitmode(self) -> int:"""Unitmode { get; set; } -> int"""
    @property
    def UpdateThumbnail(self) -> int:"""UpdateThumbnail { get; set; } -> int"""
    @property
    def Useri1(self) -> int:"""Useri1 { get; set; } -> int"""
    @property
    def Useri2(self) -> int:"""Useri2 { get; set; } -> int"""
    @property
    def Useri3(self) -> int:"""Useri3 { get; set; } -> int"""
    @property
    def Useri4(self) -> int:"""Useri4 { get; set; } -> int"""
    @property
    def Useri5(self) -> int:"""Useri5 { get; set; } -> int"""
    @property
    def Userr1(self) -> float:"""Userr1 { get; set; } -> float"""
    @property
    def Userr2(self) -> float:"""Userr2 { get; set; } -> float"""
    @property
    def Userr3(self) -> float:"""Userr3 { get; set; } -> float"""
    @property
    def Userr4(self) -> float:"""Userr4 { get; set; } -> float"""
    @property
    def Userr5(self) -> float:"""Userr5 { get; set; } -> float"""
    @property
    def Usrtimer(self) -> bool:"""Usrtimer { get; set; } -> bool"""
    @property
    def VersionGuid(self) -> str:"""VersionGuid { get; set; } -> str"""
    @property
    def ViewportScaleDefault(self) -> float:"""ViewportScaleDefault { get; set; } -> float"""
    @property
    def ViewportTableId(self) -> ObjectId:"""ViewportTableId { get; } -> ObjectId"""
    @property
    def ViewTableId(self) -> ObjectId:"""ViewTableId { get; } -> ObjectId"""
    @property
    def Visretain(self) -> bool:"""Visretain { get; set; } -> bool"""
    @property
    def VisualStyleDictionaryId(self) -> ObjectId:"""VisualStyleDictionaryId { get; } -> ObjectId"""
    @property
    def Worldview(self) -> bool:"""Worldview { get; set; } -> bool"""
    @property
    def XclipFrame(self) -> int:"""XclipFrame { get; set; } -> int"""
    @property
    def XrefBlockId(self) -> ObjectId:"""XrefBlockId { get; } -> ObjectId"""
    @property
    def XrefEditEnabled(self) -> bool:"""XrefEditEnabled { get; set; } -> bool"""
    @property
    def AbortDxfIn(self) -> _n_6_t_17:
        """AbortDxfIn Event: EventHandler"""
    @property
    def AbortDxfOut(self) -> _n_6_t_17:
        """AbortDxfOut Event: EventHandler"""
    @property
    def AbortSave(self) -> _n_6_t_17:
        """AbortSave Event: EventHandler"""
    @property
    def BeginDeepClone(self) -> IdMappingEventHandler:
        """BeginDeepClone Event: IdMappingEventHandler"""
    @property
    def BeginDeepCloneTranslation(self) -> IdMappingEventHandler:
        """BeginDeepCloneTranslation Event: IdMappingEventHandler"""
    @property
    def BeginDxfIn(self) -> _n_6_t_17:
        """BeginDxfIn Event: EventHandler"""
    @property
    def BeginDxfOut(self) -> _n_6_t_17:
        """BeginDxfOut Event: EventHandler"""
    @property
    def BeginInsert(self) -> BeginInsertEventHandler:
        """BeginInsert Event: BeginInsertEventHandler"""
    @property
    def BeginSave(self) -> DatabaseIOEventHandler:
        """BeginSave Event: DatabaseIOEventHandler"""
    @property
    def BeginWblockBlock(self) -> BeginWblockBlockEventHandler:
        """BeginWblockBlock Event: BeginWblockBlockEventHandler"""
    @property
    def BeginWblockEntireDatabase(self) -> BeginWblockEntireDatabaseEventHandler:
        """BeginWblockEntireDatabase Event: BeginWblockEntireDatabaseEventHandler"""
    @property
    def BeginWblockObjects(self) -> BeginWblockObjectsEventHandler:
        """BeginWblockObjects Event: BeginWblockObjectsEventHandler"""
    @property
    def BeginWblockSelectedObjects(self) -> BeginWblockSelectedObjectsEventHandler:
        """BeginWblockSelectedObjects Event: BeginWblockSelectedObjectsEventHandler"""
    @property
    def DatabaseConstructed(self) -> _n_6_t_17:
        """DatabaseConstructed Event: EventHandler"""
    @property
    def DatabaseToBeDestroyed(self) -> _n_6_t_17:
        """DatabaseToBeDestroyed Event: EventHandler"""
    @property
    def DeepCloneAborted(self) -> _n_6_t_17:
        """DeepCloneAborted Event: EventHandler"""
    @property
    def DeepCloneEnded(self) -> _n_6_t_17:
        """DeepCloneEnded Event: EventHandler"""
    @property
    def Disposed(self) -> _n_6_t_17:
        """Disposed Event: EventHandler"""
    @property
    def DwgFileOpened(self) -> DatabaseIOEventHandler:
        """DwgFileOpened Event: DatabaseIOEventHandler"""
    @property
    def DxfInComplete(self) -> _n_6_t_17:
        """DxfInComplete Event: EventHandler"""
    @property
    def DxfOutComplete(self) -> _n_6_t_17:
        """DxfOutComplete Event: EventHandler"""
    @property
    def InitialDwgFileOpenComplete(self) -> _n_6_t_17:
        """InitialDwgFileOpenComplete Event: EventHandler"""
    @property
    def InsertAborted(self) -> _n_6_t_17:
        """InsertAborted Event: EventHandler"""
    @property
    def InsertEnded(self) -> _n_6_t_17:
        """InsertEnded Event: EventHandler"""
    @property
    def InsertMappingAvailable(self) -> IdMappingEventHandler:
        """InsertMappingAvailable Event: IdMappingEventHandler"""
    @property
    def ObjectAppended(self) -> ObjectEventHandler:
        """ObjectAppended Event: ObjectEventHandler"""
    @property
    def ObjectErased(self) -> ObjectErasedEventHandler:
        """ObjectErased Event: ObjectErasedEventHandler"""
    @property
    def ObjectModified(self) -> ObjectEventHandler:
        """ObjectModified Event: ObjectEventHandler"""
    @property
    def ObjectOpenedForModify(self) -> ObjectEventHandler:
        """ObjectOpenedForModify Event: ObjectEventHandler"""
    @property
    def ObjectReappended(self) -> ObjectEventHandler:
        """ObjectReappended Event: ObjectEventHandler"""
    @property
    def ObjectUnappended(self) -> ObjectEventHandler:
        """ObjectUnappended Event: ObjectEventHandler"""
    @property
    def PartialOpenNotice(self) -> _n_6_t_17:
        """PartialOpenNotice Event: EventHandler"""
    @property
    def ProxyResurrectionCompleted(self) -> ProxyResurrectionCompletedEventHandler:
        """ProxyResurrectionCompleted Event: ProxyResurrectionCompletedEventHandler"""
    @property
    def SaveComplete(self) -> DatabaseIOEventHandler:
        """SaveComplete Event: DatabaseIOEventHandler"""
    @property
    def SystemVariableChanged(self) -> SystemVariableChangedEventHandler:
        """SystemVariableChanged Event: SystemVariableChangedEventHandler"""
    @property
    def SystemVariableWillChange(self) -> SystemVariableChangingEventHandler:
        """SystemVariableWillChange Event: SystemVariableChangingEventHandler"""
    @property
    def WblockAborted(self) -> _n_6_t_17:
        """WblockAborted Event: EventHandler"""
    @property
    def WblockEnded(self) -> _n_6_t_17:
        """WblockEnded Event: EventHandler"""
    @property
    def WblockMappingAvailable(self) -> IdMappingEventHandler:
        """WblockMappingAvailable Event: IdMappingEventHandler"""
    @property
    def WblockNotice(self) -> WblockNoticeEventHandler:
        """WblockNotice Event: WblockNoticeEventHandler"""
    @property
    def XrefAttachAborted(self) -> _n_6_t_17:
        """XrefAttachAborted Event: EventHandler"""
    @property
    def XrefAttachEnded(self) -> _n_6_t_17:
        """XrefAttachEnded Event: EventHandler"""
    @property
    def XrefBeginAttached(self) -> XrefBeginOperationEventHandler:
        """XrefBeginAttached Event: XrefBeginOperationEventHandler"""
    @property
    def XrefBeginOtherAttached(self) -> XrefBeginOperationEventHandler:
        """XrefBeginOtherAttached Event: XrefBeginOperationEventHandler"""
    @property
    def XrefBeginRestore(self) -> XrefBeginOperationEventHandler:
        """XrefBeginRestore Event: XrefBeginOperationEventHandler"""
    @property
    def XrefComandeered(self) -> XrefComandeeredEventHandler:
        """XrefComandeered Event: XrefComandeeredEventHandler"""
    @property
    def XrefPreXrefLockFile(self) -> XrefPreXrefLockFileEventHandler:
        """XrefPreXrefLockFile Event: XrefPreXrefLockFileEventHandler"""
    @property
    def XrefRedirected(self) -> XrefRedirectedEventHandler:
        """XrefRedirected Event: XrefRedirectedEventHandler"""
    @property
    def XrefRestoreAborted(self) -> _n_6_t_17:
        """XrefRestoreAborted Event: EventHandler"""
    @property
    def XrefRestoreEnded(self) -> _n_6_t_17:
        """XrefRestoreEnded Event: EventHandler"""
    @property
    def XrefSubCommandAborted(self) -> XrefSubCommandAbortedEventHandler:
        """XrefSubCommandAborted Event: XrefSubCommandAbortedEventHandler"""
    @property
    def XrefSubCommandEnd(self) -> XrefSubCommandEndEventHandler:
        """XrefSubCommandEnd Event: XrefSubCommandEndEventHandler"""
    @property
    def XrefSubCommandStart(self) -> XrefSubCommandStartEventHandler:
        """XrefSubCommandStart Event: XrefSubCommandStartEventHandler"""
    def __init__(self, buildDefaultDrawing: bool, noDocument: bool) -> Database:...
    def __init__(self) -> Database:...
    def AbortDeepClone(self, idMap: IdMapping):...
    def AddDBObject(self, appendIt: DBObject) -> ObjectId:...
    def ApplyPartialOpenFilters(self, spatialFilter: _n_1_t_0, layerFilter: _n_1_t_1):...
    def AttachXref(self, fileName: str, blockName: str) -> ObjectId:...
    def AuditXData(self, info: AuditInfo):...
    def BindXrefs(self, xrefIds: ObjectIdCollection, insertBind: bool):...
    def ClassDxfName(self, getMyDxfName: _n_5_t_0) -> str:...
    def CloseInput(self, closeFile: bool):...
    def CountEmptyObjects(self, flags: int) -> int:...
    def CountHardReferences(self, ids: ObjectIdCollection, count: _n_6_t_10[int]):...
    def DeepCloneObjects(self, identifiers: ObjectIdCollection, id: ObjectId, mapping: IdMapping, deferTranslation: bool):...
    def DetachXref(self, xrefId: ObjectId):...
    def DisablePartialOpen(self):...
    def DisableUndoRecording(self, disable: bool):...
    def DxfIn(self, fileName: str, logFilename: str):...
    def DxfOut(self, fileName: str, precision: int, version: DwgVersion):...
    def DxfOut(self, fileName: str, precision: int, saveThumbnailImage: bool):...
    def EraseEmptyObjects(self, flags: int) -> int:...
    def EvaluateFields(self, context: FieldEvaluationContext, prop: str) -> FieldEvaluationResult:...
    def EvaluateFields(self, context: FieldEvaluationContext) -> FieldEvaluationResult:...
    def EvaluateFields(self) -> FieldEvaluationResult:...
    def ForceWblockDatabaseCopy(self):...
    @staticmethod
    def FromAcadDatabase(acadDatabase: object) -> Database:...
    @staticmethod
    def GetAllDatabases() -> _n_8_t_1[Database]:...
    def GetDimensionStyleChildData(self, classDescriptor: _n_5_t_0) -> DimStyleTableRecord:...
    def GetDimensionStyleChildId(self, classDescriptor: _n_5_t_0, parentStyle: ObjectId) -> ObjectId:...
    def GetDimensionStyleParentId(self, childStyle: ObjectId) -> ObjectId:...
    def GetDimRecentStyleList(self) -> ObjectIdCollection:...
    def GetDimstyleData(self) -> DimStyleTableRecord:...
    def GetHostDwgXrefGraph(self, includeGhosts: bool) -> XrefGraph:...
    def GetNearestLineWeight(self, weight: int) -> LineWeight:...
    def GetObjectId(self, createIfNotFound: bool, objHandle: Handle, identifier: int) -> ObjectId:...
    def GetSupportedDxfOutVersions(self) -> _n_6_t_10[DwgVersion]:...
    def GetSupportedSaveVersions(self) -> _n_6_t_10[DwgVersion]:...
    def GetViewports(self, bGetPaperspaceVports: bool) -> ObjectIdCollection:...
    def GetVisualStyleList(self) -> _n_9_t_0:...
    def Insert(self, sourceBlockName: str, destinationBlockName: str, dataBase: Database, preserveSourceDatabase: bool) -> ObjectId:...
    def Insert(self, transform: _n_2_t_6, dataBase: Database, preserveSourceDatabase: bool):...
    def Insert(self, blockName: str, dataBase: Database, preserveSourceDatabase: bool) -> ObjectId:...
    @staticmethod
    def IsObjectNonPersistent(id: ObjectId) -> bool:...
    def IsValidLineWeight(self, weight: int) -> bool:...
    def LoadLineTypeFile(self, lineTypeName: str, filename: str):...
    def LoadMlineStyleFile(self, mlineStyleName: str, fileName: str):...
    @staticmethod
    def MarkObjectNonPersistent(id: ObjectId, value: bool):...
    def OverlayXref(self, fileName: str, blockName: str) -> ObjectId:...
    def Purge(self, idGraph: ObjectIdGraph):...
    def Purge(self, ids: ObjectIdCollection):...
    def ReadDwgFile(self, drawingFile: _n_6_t_3, allowCPConversion: bool, password: str):...
    def ReadDwgFile(self, fileName: str, mode: FileOpenMode, allowCPConversion: bool, password: str):...
    def ReadDwgFile(self, fileName: str, fileSharing: _n_13_t_0, allowCPConversion: bool, password: str):...
    def ReclaimMemoryFromErasedObjects(self, ids: ObjectIdCollection):...
    def ReloadXrefs(self, xrefIds: ObjectIdCollection):...
    def ResetTimes(self):...
    def ResolveXrefs(self, useThreadEngine: bool, doNewOnly: bool):...
    def RestoreForwardingXrefSymbols(self):...
    def RestoreOriginalXrefSymbols(self):...
    def Save(self):...
    def SaveAs(self, fileName: str, version: DwgVersion):...
    def SaveAs(self, fileName: str, bBakAndRename: bool, version: DwgVersion, security: SecurityParameters):...
    def SaveAs(self, fileName: str, security: SecurityParameters):...
    def SetDimstyleData(self, style: DimStyleTableRecord):...
    def SetTimeZoneAsUtcOffset(self, offset: float) -> TimeZone:...
    def SetWorldPaperspaceUcsBaseOrigin(self, origin: _n_2_t_1, orthoView: OrthographicView):...
    def SetWorldUcsBaseOrigin(self, origin: _n_2_t_1, orthoView: OrthographicView):...
    def TimeZoneDescription(self, tz: TimeZone) -> str:...
    def TimeZoneOffset(self, tz: TimeZone) -> float:...
    def TryGetObjectId(self, objHandle: Handle, id: ObjectId) -> bool:...
    def UnloadXrefs(self, xrefIds: ObjectIdCollection):...
    def UpdateExt(self, doBestFit: bool):...
    def Wblock(self) -> Database:...
    def Wblock(self, blockId: ObjectId) -> Database:...
    def Wblock(self, outputDataBase: Database, outObjIds: ObjectIdCollection, basePoint: _n_2_t_1, cloning: DuplicateRecordCloning):...
    def Wblock(self, outObjIds: ObjectIdCollection, basePoint: _n_2_t_1) -> Database:...
    def WblockCloneObjects(self, identifiers: ObjectIdCollection, id: ObjectId, mapping: IdMapping, cloning: DuplicateRecordCloning, deferTranslation: bool):...
    def WorldPaperspaceUcsBaseOrigin(self, orthoView: OrthographicView) -> _n_2_t_1:...
    def WorldUcsBaseOrigin(self, orthoView: OrthographicView) -> _n_2_t_1:...
    def XBindXrefs(self, xrefSymbolIds: ObjectIdCollection, insertBind: bool):...
    def Audit(self, bFixErrors: bool, bCmdLnEcho: bool):
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DatabaseExtension"""
class DatabaseIOEventArgs(_n_6_t_13):
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
class DatabaseIOEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> DatabaseIOEventHandler:...
    def BeginInvoke(self, sender: object, e: DatabaseIOEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: DatabaseIOEventArgs):...
class DatabaseSummaryInfo(_n_6_t_12):
    @property
    def Author(self) -> str:"""Author { get; } -> str"""
    @property
    def Comments(self) -> str:"""Comments { get; } -> str"""
    @property
    def CustomProperties(self) -> _n_7_t_6:"""CustomProperties { get; } -> IDictionaryEnumerator"""
    @property
    def HyperlinkBase(self) -> str:"""HyperlinkBase { get; } -> str"""
    @property
    def Keywords(self) -> str:"""Keywords { get; } -> str"""
    @property
    def LastSavedBy(self) -> str:"""LastSavedBy { get; } -> str"""
    @property
    def RevisionNumber(self) -> str:"""RevisionNumber { get; } -> str"""
    @property
    def Subject(self) -> str:"""Subject { get; } -> str"""
    @property
    def Title(self) -> str:"""Title { get; } -> str"""
class DatabaseSummaryInfoBuilder(object):
    @property
    def Author(self) -> str:"""Author { get; set; } -> str"""
    @property
    def Comments(self) -> str:"""Comments { get; set; } -> str"""
    @property
    def CustomProperties(self) -> _n_9_t_1:"""CustomProperties { get; } -> StringDictionary"""
    @property
    def CustomPropertyTable(self) -> _n_7_t_7:"""CustomPropertyTable { get; } -> IDictionary"""
    @property
    def HyperlinkBase(self) -> str:"""HyperlinkBase { get; set; } -> str"""
    @property
    def Keywords(self) -> str:"""Keywords { get; set; } -> str"""
    @property
    def LastSavedBy(self) -> str:"""LastSavedBy { get; set; } -> str"""
    @property
    def RevisionNumber(self) -> str:"""RevisionNumber { get; set; } -> str"""
    @property
    def Subject(self) -> str:"""Subject { get; set; } -> str"""
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    def __init__(self, value: DatabaseSummaryInfo) -> DatabaseSummaryInfoBuilder:...
    def __init__(self) -> DatabaseSummaryInfoBuilder:...
    def ToDatabaseSummaryInfo(self) -> DatabaseSummaryInfo:...
class DataCell(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def CellType(self) -> CellType:"""CellType { get; } -> CellType"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
    def __init__(self) -> DataCell:...
    def Init(self):...
    def SetBool(self, value: bool):...
    def SetDouble(self, value: float):...
    def SetHardOwnershipId(self, value: ObjectId):...
    def SetHardPointerId(self, value: ObjectId):...
    def SetInteger(self, value: int):...
    def SetObjectId(self, value: ObjectId):...
    def SetPoint(self, value: _n_2_t_1):...
    def SetSoftOwnershipId(self, value: ObjectId):...
    def SetSoftPointerId(self, value: ObjectId):...
    def SetString(self, value: str):...
    def SetVector(self, value: _n_2_t_3):...
class DataCellCollection(_n_5_t_3, _n_6_t_0, _n_7_t_5, typing.Iterable[typing.Any]):
    def __init__(self) -> DataCellCollection:...
class DataColumn(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def ColumnName(self) -> str:"""ColumnName { get; set; } -> str"""
    @property
    def ColumnType(self) -> CellType:"""ColumnType { get; set; } -> CellType"""
    @property
    def GrowLength(self) -> int:"""GrowLength { get; set; } -> int"""
    @property
    def NumCells(self) -> int:"""NumCells { get; } -> int"""
    @property
    def PhysicalLength(self) -> int:"""PhysicalLength { get; set; } -> int"""
    def __init__(self, type: CellType, columnName: str) -> DataColumn:...
    def __init__(self, column: DataColumn) -> DataColumn:...
    def __init__(self) -> DataColumn:...
    def AppendCell(self, cell: DataCell):...
    def Assign(self, col: DataColumn):...
    def GetCellAt(self, index: int) -> DataCell:...
    def GetIndexAtCell(self, cell: DataCell) -> int:...
    def InsertCellAt(self, index: int, cell: DataCell):...
    def RemoveCellAt(self, index: int):...
    def SetCellAt(self, index: int, cell: DataCell):...
class DataLink(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ConnectionString(self) -> str:"""ConnectionString { get; set; } -> str"""
    @property
    def DataAdapterId(self) -> str:"""DataAdapterId { get; set; } -> str"""
    @property
    def DataLinkOption(self) -> DataLinkOption:"""DataLinkOption { get; set; } -> DataLinkOption"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ToolTip(self) -> str:"""ToolTip { get; set; } -> str"""
    @property
    def UpdateOption(self) -> int:"""UpdateOption { get; set; } -> int"""
    def __init__(self) -> DataLink:...
    def GetSourceFiles(self, nContext: DataLinkGetSourceContext) -> _n_7_t_1:...
    def GetTargets(self) -> ObjectIdCollection:...
    def GetUpdateStatus(self, pDir: UpdateDirection, pTime: _n_6_t_20, errMessage: str) -> _n_5_t_1:...
    def RepathSourceFiles(self, sBasePath: str, nOption: PathOption):...
    def Update(self, dir: UpdateDirection, option: UpdateOption):...
class DataLinkGetSourceContext(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Etransmit: int
    FileWatcher: int
    OrignalPath: int
    Other: int
    Unknown: int
    value__: int
    XrefManager: int
class DataLinkManager(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def DataLinkCount(self) -> int:"""DataLinkCount { get; } -> int"""
    def AddDataLink(self, dataLink: DataLink) -> ObjectId:...
    def GetDataLink(self) -> ObjectIdCollection:...
    def GetDataLink(self, name: str) -> ObjectId:...
    def RemoveDataLink(self, idDataLink: ObjectId):...
    def RemoveDataLink(self, name: str) -> ObjectId:...
    def Update(self, direction: UpdateDirection, option: UpdateOption):...
    def Update(self, dataIds: ObjectIdCollection, direction: UpdateDirection, option: UpdateOption):...
class DataLinkOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Anonymous: int
    _None: int
    PersistCache: int
    value__: int
class DataTable(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def NumColsGrowSize(self) -> int:"""NumColsGrowSize { get; set; } -> int"""
    @property
    def NumColsPhysicalSize(self) -> int:"""NumColsPhysicalSize { get; set; } -> int"""
    @property
    def NumColumns(self) -> int:"""NumColumns { get; } -> int"""
    @property
    def NumRows(self) -> int:"""NumRows { get; } -> int"""
    @property
    def NumRowsGrowSize(self) -> int:"""NumRowsGrowSize { get; set; } -> int"""
    @property
    def NumRowsPhysicalSize(self) -> int:"""NumRowsPhysicalSize { get; set; } -> int"""
    @property
    def TableName(self) -> str:"""TableName { get; set; } -> str"""
    def __init__(self) -> DataTable:...
    def AppendColumn(self, type: CellType, columnName: str):...
    def AppendRow(self, row: DataCellCollection, validate: bool):...
    def Assign(self, other: DataTable):...
    def GetCellAt(self, row: int, col: int) -> DataCell:...
    def GetColumnAt(self, index: int) -> DataColumn:...
    def GetColumnIndexAtName(self, name: str) -> int:...
    def GetColumnNameAt(self, index: int) -> str:...
    def GetColumnTypeAt(self, index: int) -> CellType:...
    def GetRowAt(self, index: int) -> DataCellCollection:...
    def InsertColumnAt(self, index: int, type: CellType, columnName: str):...
    def InsertRowAt(self, index: int, row: DataCellCollection, validate: bool):...
    def RemoveColumnAt(self, index: int):...
    def RemoveRowAt(self, index: int):...
    def SetCellAt(self, row: int, col: int, cell: DataCell):...
    def SetRowAt(self, index: int, row: DataCellCollection, validate: bool):...
class DataType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Buffer: int
    Date: int
    Double: int
    General: int
    Long: int
    ObjectId: int
    Point: int
    Point3d: int
    Resbuf: int
    String: int
    Unknown: int
    value__: int
class DataTypeParameter(_n_6_t_12):
    @property
    def DataType(self) -> DataType:"""DataType { get; set; } -> DataType"""
    @property
    def UnitType(self) -> UnitType:"""UnitType { get; set; } -> UnitType"""
    def __init__(self, dataType: DataType, unitType: UnitType) -> DataTypeParameter:...
class DBDictionary(DBObject, _n_6_t_0, _n_6_t_1, _n_7_t_7):
    @property
    def IncludingErased(self) -> DBDictionary:"""IncludingErased { get; } -> DBDictionary"""
    @property
    def TreatElementsAsHard(self) -> bool:"""TreatElementsAsHard { get; set; } -> bool"""
    def __init__(self) -> DBDictionary:...
    def GetAt(self, entryName: str) -> ObjectId:...
    def NameAt(self, objId: ObjectId) -> str:...
    def SetAt(self, searchKey: str, newValue: DBObject) -> ObjectId:...
    def SetName(self, oldName: str, newName: str):...
class DBDictionaryEntry(_n_6_t_12):
    m_key: int
    m_value: int
    @property
    def Key(self) -> str:"""Key { get; set; } -> str"""
    @property
    def Value(self) -> ObjectId:"""Value { get; set; } -> ObjectId"""
    def __init__(self, key: str, value: ObjectId) -> DBDictionaryEntry:...
class DbDictionaryEnumerator(_n_5_t_2, _n_6_t_0, _n_6_t_1, _n_7_t_6):
    pass
class DbHomeView(_n_5_t_3, _n_6_t_0, _n_6_t_1):
    @property
    def Center(self) -> _n_2_t_1:"""Center { get; set; } -> Point3d"""
    @property
    def Eye(self) -> _n_2_t_1:"""Eye { get; set; } -> Point3d"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def Perspective(self) -> bool:"""Perspective { get; set; } -> bool"""
    @property
    def Up(self) -> _n_2_t_3:"""Up { get; set; } -> Vector3d"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
    def __init__(self) -> DbHomeView:...
    def __init__(self, unmanagedPointer: _n_6_t_3, autoDelete: bool) -> DbHomeView:...
    def ToggleDefaultSettings(self):...
class DBObject(_n_3_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def AcadObject(self) -> object:"""AcadObject { get; } -> object"""
    @property
    def Annotative(self) -> AnnotativeStates:"""Annotative { get; set; } -> AnnotativeStates"""
    @property
    def ClassID(self) -> _n_6_t_22:"""ClassID { get; } -> Guid"""
    @property
    def Database(self) -> Database:"""Database { get; } -> Database"""
    @property
    def Drawable(self) -> _n_3_t_2:"""Drawable { get; } -> Drawable"""
    @property
    def ExtensionDictionary(self) -> ObjectId:"""ExtensionDictionary { get; } -> ObjectId"""
    @property
    def Handle(self) -> Handle:"""Handle { get; } -> Handle"""
    @property
    def HasFields(self) -> bool:"""HasFields { get; } -> bool"""
    @property
    def HasSaveVersionOverride(self) -> bool:"""HasSaveVersionOverride { get; set; } -> bool"""
    @property
    def IsAProxy(self) -> bool:"""IsAProxy { get; } -> bool"""
    @property
    def IsCancelling(self) -> bool:"""IsCancelling { get; } -> bool"""
    @property
    def IsErased(self) -> bool:"""IsErased { get; } -> bool"""
    @property
    def IsEraseStatusToggled(self) -> bool:"""IsEraseStatusToggled { get; } -> bool"""
    @property
    def IsModified(self) -> bool:"""IsModified { get; } -> bool"""
    @property
    def IsModifiedGraphics(self) -> bool:"""IsModifiedGraphics { get; } -> bool"""
    @property
    def IsModifiedXData(self) -> bool:"""IsModifiedXData { get; } -> bool"""
    @property
    def IsNewObject(self) -> bool:"""IsNewObject { get; } -> bool"""
    @property
    def IsNotifyEnabled(self) -> bool:"""IsNotifyEnabled { get; } -> bool"""
    @property
    def IsNotifying(self) -> bool:"""IsNotifying { get; } -> bool"""
    @property
    def IsObjectIdsInFlux(self) -> bool:"""IsObjectIdsInFlux { get; } -> bool"""
    @property
    def IsReadEnabled(self) -> bool:"""IsReadEnabled { get; } -> bool"""
    @property
    def IsReallyClosing(self) -> bool:"""IsReallyClosing { get; } -> bool"""
    @property
    def IsTransactionResident(self) -> bool:"""IsTransactionResident { get; } -> bool"""
    @property
    def IsUndoing(self) -> bool:"""IsUndoing { get; } -> bool"""
    @property
    def IsWriteEnabled(self) -> bool:"""IsWriteEnabled { get; } -> bool"""
    @property
    def MergeStyle(self) -> DuplicateRecordCloning:"""MergeStyle { get; set; } -> DuplicateRecordCloning"""
    @property
    def ObjectBirthVersion(self) -> FullDwgVersion:"""ObjectBirthVersion { get; } -> FullDwgVersion"""
    @property
    def ObjectId(self) -> ObjectId:"""ObjectId { get; } -> ObjectId"""
    @property
    def OwnerId(self) -> ObjectId:"""OwnerId { get; set; } -> ObjectId"""
    @property
    def PaperOrientation(self) -> PaperOrientationStates:"""PaperOrientation { get; } -> PaperOrientationStates"""
    @property
    def UndoFiler(self) -> DwgFiler:"""UndoFiler { get; } -> DwgFiler"""
    @property
    def XData(self) -> ResultBuffer:"""XData { get; set; } -> ResultBuffer"""
    @property
    def Cancelled(self) -> _n_6_t_17:
        """Cancelled Event: EventHandler"""
    @property
    def Copied(self) -> ObjectEventHandler:
        """Copied Event: ObjectEventHandler"""
    @property
    def Erased(self) -> ObjectErasedEventHandler:
        """Erased Event: ObjectErasedEventHandler"""
    @property
    def Goodbye(self) -> _n_6_t_17:
        """Goodbye Event: EventHandler"""
    @property
    def Modified(self) -> _n_6_t_17:
        """Modified Event: EventHandler"""
    @property
    def ModifiedXData(self) -> _n_6_t_17:
        """ModifiedXData Event: EventHandler"""
    @property
    def ModifyUndone(self) -> _n_6_t_17:
        """ModifyUndone Event: EventHandler"""
    @property
    def ObjectClosed(self) -> ObjectClosedEventHandler:
        """ObjectClosed Event: ObjectClosedEventHandler"""
    @property
    def OpenedForModify(self) -> _n_6_t_17:
        """OpenedForModify Event: EventHandler"""
    @property
    def Reappended(self) -> _n_6_t_17:
        """Reappended Event: EventHandler"""
    @property
    def SubObjectModified(self) -> ObjectEventHandler:
        """SubObjectModified Event: ObjectEventHandler"""
    @property
    def Unappended(self) -> _n_6_t_17:
        """Unappended Event: EventHandler"""
    def AddContext(self, context: ObjectContext):...
    def ApplyPaperOrientationTransform(self, viewport: Viewport):...
    def ApplyPartialUndo(self, undoFiler: DwgFiler, classObj: _n_5_t_0):...
    def Audit(self, auditInfo: AuditInfo):...
    def Cancel(self):...
    def Close(self):...
    def CloseAndPage(self, onlyWhenClean: bool):...
    def CreateExtensionDictionary(self):...
    def DecomposeForSave(self, version: DwgVersion) -> DecomposeForSaveReplacementRecord:...
    def DeepClone(self, ownerPointer: DBObject, idMap: IdMapping, isPrimary: bool) -> DBObject:...
    def DisableUndoRecording(self, disable: bool):...
    def DowngradeOpen(self):...
    def DowngradeToNotify(self, wasWritable: bool):...
    def DwgIn(self, filer: DwgFiler):...
    def DwgOut(self, filer: DwgFiler):...
    def DxfIn(self, filer: DxfFiler):...
    def DxfOut(self, filer: DxfFiler):...
    def Erase(self):...
    def Erase(self, erasing: bool):...
    @staticmethod
    def FromAcadObject(acadObj: object) -> ObjectId:...
    def GetEventExtender(self, create: bool) -> DBObjectEventExtender:...
    def GetField(self, propertyName: str) -> ObjectId:...
    def GetField(self) -> ObjectId:...
    def GetObjectSaveVersion(self, filer: DxfFiler) -> FullDwgVersion:...
    def GetObjectSaveVersion(self, filer: DwgFiler) -> FullDwgVersion:...
    def GetParameterInterface(self, name: str, runtimeInterface: bool) -> IParameter:...
    def GetPersistentReactorIds(self) -> ObjectIdCollection:...
    def GetReactors(self) -> _n_8_t_1[_n_5_t_2]:...
    def GetTransientReactors(self) -> _n_8_t_1[_n_5_t_2]:...
    def GetXDataForApplication(self, applicationName: str) -> ResultBuffer:...
    def HandOverTo(self, newPointer: DBObject, keepXData: bool, keepExtensionDictionary: bool):...
    def HasContext(self, context: ObjectContext) -> bool:...
    def HasPersistentReactor(self, objId: ObjectId) -> bool:...
    @staticmethod
    def IsCustomObject(id: ObjectId) -> bool:...
    def ReleaseExtensionDictionary(self):...
    def RemoveContext(self, context: ObjectContext):...
    def RemoveField(self, id: ObjectId):...
    def RemoveField(self, propertyName: str) -> ObjectId:...
    def RemoveField(self) -> ObjectId:...
    def ResetScaleDependentProperties(self):...
    def SetField(self, propertyName: str, field: Field) -> ObjectId:...
    def SetField(self, field: Field) -> ObjectId:...
    def SetFromStyle(self) -> bool:...
    def SetObjectIdsInFlux(self):...
    def SetPaperOrientation(self, bPaperOrientation: bool):...
    def SupportsCollection(self, collectionName: str) -> bool:...
    def SwapIdWith(self, otherId: ObjectId, swapExtendedData: bool, swapExtensionDictionary: bool):...
    def SwapReferences(self, idMap: IdMapping):...
    def UpgradeFromNotify(self) -> bool:...
    def UpgradeOpen(self):...
    def WblockClone(self, ownerPointer: _n_5_t_2, idMap: IdMapping, isPrimary: bool) -> DBObject:...
    def XDataTransformBy(self, transform: _n_2_t_6):...
class DBObjectCollection(_n_5_t_3, _n_6_t_0, _n_7_t_5, typing.Iterable[typing.Any]):
    def __init__(self) -> DBObjectCollection:...
class DBObjectReference(_n_6_t_12):
    @property
    def Kind(self) -> int:"""Kind { get; } -> int"""
    @property
    def ObjectId(self) -> ObjectId:"""ObjectId { get; } -> ObjectId"""
    def __init__(self, id: ObjectId, kind: int) -> DBObjectReference:...
class DBObjectReferenceCollection(_n_7_t_4, _n_7_t_5, typing.Iterable[typing.Any]):
    pass
class DBPoint(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def EcsRotation(self) -> float:"""EcsRotation { get; set; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, position: _n_2_t_1) -> DBPoint:...
    def __init__(self) -> DBPoint:...
class DBText(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def AlignmentPoint(self) -> _n_2_t_1:"""AlignmentPoint { get; set; } -> Point3d"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def HorizontalMode(self) -> TextHorizontalMode:"""HorizontalMode { get; set; } -> TextHorizontalMode"""
    @property
    def IsDefaultAlignment(self) -> bool:"""IsDefaultAlignment { get; } -> bool"""
    @property
    def IsMirroredInX(self) -> bool:"""IsMirroredInX { get; set; } -> bool"""
    @property
    def IsMirroredInY(self) -> bool:"""IsMirroredInY { get; set; } -> bool"""
    @property
    def Justify(self) -> AttachmentPoint:"""Justify { get; set; } -> AttachmentPoint"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Oblique(self) -> float:"""Oblique { get; set; } -> float"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def TextString(self) -> str:"""TextString { get; set; } -> str"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    @property
    def TextStyleName(self) -> str:"""TextStyleName { get; } -> str"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    @property
    def VerticalMode(self) -> TextVerticalMode:"""VerticalMode { get; set; } -> TextVerticalMode"""
    @property
    def WidthFactor(self) -> float:"""WidthFactor { get; set; } -> float"""
    def __init__(self) -> DBText:...
    def AdjustAlignment(self, alternateDatabaseToUse: Database):...
    def ConvertFieldToText(self):...
    def CorrectSpelling(self) -> int:...
    def getTextWithFieldCodes(self) -> str:...
class DBVisualStyle(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def InternalUseOnly(self) -> bool:"""InternalUseOnly { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Type(self) -> _n_3_t_3:"""Type { get; set; } -> VisualStyleType"""
    def __init__(self) -> DBVisualStyle:...
    def CopyTo(self, pDest: _n_3_t_4):...
    def GetTrait(self, prop: _n_3_t_5) -> object:...
    def GetTraitFlag(self, prop: _n_3_t_5, flagVal: _n_6_t_11) -> bool:...
    def SetTrait(self, prop: _n_3_t_5, color: _n_0_t_0, __unnamed002: _n_3_t_6):...
    def SetTrait(self, prop: _n_3_t_5, red: float, green: float, blue: float, op: _n_3_t_6):...
    def SetTrait(self, prop: _n_3_t_5, dVal: float, op: _n_3_t_6):...
    def SetTrait(self, prop: _n_3_t_5, bVal: bool, __unnamed002: _n_3_t_6):...
    def SetTrait(self, prop: _n_3_t_5, nVal: int, op: _n_3_t_6):...
    def SetTrait(self, prop: _n_3_t_5, val: object, op: _n_3_t_6):...
    def SetTraitFlag(self, prop: _n_3_t_5, flagVal: _n_6_t_11, bEnable: bool):...
class DecomposeForSaveReplacementRecord(_n_6_t_12):
    @property
    def ExchangeXData(self) -> bool:"""ExchangeXData { get; } -> bool"""
    @property
    def ReplacementId(self) -> ObjectId:"""ReplacementId { get; } -> ObjectId"""
    @property
    def ReplacementObject(self) -> DBObject:"""ReplacementObject { get; } -> DBObject"""
    def __init__(self, replacement: ObjectId, exchangeXData: bool) -> DecomposeForSaveReplacementRecord:...
    def __init__(self, replacement: DBObject, exchangeXData: bool) -> DecomposeForSaveReplacementRecord:...
class DeepCloneType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Block: int
    Copy: int
    Explode: int
    Insert: int
    InsertCopy: int
    Objects: int
    SymbolTableMerge: int
    value__: int
    Wblock: int
    WblockObjects: int
    XrefBind: int
    XrefInsert: int
class DefaultLightingType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    OneDistantLight: int
    TwoDistantLights: int
    value__: int
class DetailSymbol(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def BoundarySize(self) -> _n_2_t_14:"""BoundarySize { get; } -> Vector2d"""
    @property
    def BoundaryType(self) -> DetailSymbolBoundaryType:"""BoundaryType { get; } -> DetailSymbolBoundaryType"""
    @property
    def DetailViewScale(self) -> float:"""DetailViewScale { get; } -> float"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; } -> Vector3d"""
    @property
    def DisplayIdentifier(self) -> bool:"""DisplayIdentifier { get; } -> bool"""
    @property
    def Identifier(self) -> str:"""Identifier { get; set; } -> str"""
    @property
    def IdentifierPosition(self) -> _n_2_t_1:"""IdentifierPosition { get; } -> Point3d"""
    @property
    def ModelEdgeDirection(self) -> _n_2_t_3:"""ModelEdgeDirection { get; } -> Vector3d"""
    @property
    def ModelEdgeOrigin(self) -> _n_2_t_1:"""ModelEdgeOrigin { get; } -> Point3d"""
    @property
    def ModelEdgeType(self) -> DetailViewModelEdge:"""ModelEdgeType { get; } -> DetailViewModelEdge"""
    @property
    def Origin(self) -> _n_2_t_1:"""Origin { get; } -> Point3d"""
    @property
    def OwningViewScale(self) -> float:"""OwningViewScale { get; } -> float"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def SymbolStyleId(self) -> ObjectId:"""SymbolStyleId { get; set; } -> ObjectId"""
    def __init__(self) -> DetailSymbol:...
    def IsOverriddenProperty(self, propertyToCheck: DetailSymbolOverriddenProperty) -> bool:...
class DetailSymbolBoundaryType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CircularBoundary: int
    CustomBoundary: int
    RectangularBoundary: int
    value__: int
class DetailSymbolOverriddenProperty(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    IdentifierPosition: int
    ModelEdge: int
    value__: int
class DetailViewIdentifierPlacement(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    OnBoundary: int
    OnBoundaryWithLeader: int
    OutsideBoundary: int
    OutsideBoundaryWithLeader: int
    value__: int
class DetailViewModelEdge(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Jagged: int
    Smooth: int
    SmoothWithBorder: int
    SmoothWithConnectionLine: int
    value__: int
class DetailViewStyle(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ArrowSymbolColor(self) -> _n_0_t_0:"""ArrowSymbolColor { get; set; } -> Color"""
    @property
    def ArrowSymbolId(self) -> ObjectId:"""ArrowSymbolId { get; set; } -> ObjectId"""
    @property
    def ArrowSymbolSize(self) -> float:"""ArrowSymbolSize { get; set; } -> float"""
    @property
    def BorderLineColor(self) -> _n_0_t_0:"""BorderLineColor { get; set; } -> Color"""
    @property
    def BorderLineTypeId(self) -> ObjectId:"""BorderLineTypeId { get; set; } -> ObjectId"""
    @property
    def BorderLineWeight(self) -> LineWeight:"""BorderLineWeight { get; set; } -> LineWeight"""
    @property
    def BoundaryLineColor(self) -> _n_0_t_0:"""BoundaryLineColor { get; set; } -> Color"""
    @property
    def BoundaryLineTypeId(self) -> ObjectId:"""BoundaryLineTypeId { get; set; } -> ObjectId"""
    @property
    def BoundaryLineWeight(self) -> LineWeight:"""BoundaryLineWeight { get; set; } -> LineWeight"""
    @property
    def ConnectionLineColor(self) -> _n_0_t_0:"""ConnectionLineColor { get; set; } -> Color"""
    @property
    def ConnectionLineTypeId(self) -> ObjectId:"""ConnectionLineTypeId { get; set; } -> ObjectId"""
    @property
    def ConnectionLineWeight(self) -> LineWeight:"""ConnectionLineWeight { get; set; } -> LineWeight"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def IdentifierColor(self) -> _n_0_t_0:"""IdentifierColor { get; set; } -> Color"""
    @property
    def IdentifierHeight(self) -> float:"""IdentifierHeight { get; set; } -> float"""
    @property
    def IdentifierOffset(self) -> float:"""IdentifierOffset { get; set; } -> float"""
    @property
    def IdentifierPlacement(self) -> DetailViewIdentifierPlacement:"""IdentifierPlacement { get; set; } -> DetailViewIdentifierPlacement"""
    @property
    def IdentifierStyleId(self) -> ObjectId:"""IdentifierStyleId { get; set; } -> ObjectId"""
    @property
    def IsModifiedForRecompute(self) -> bool:"""IsModifiedForRecompute { get; } -> bool"""
    @property
    def ModelEdge(self) -> DetailViewModelEdge:"""ModelEdge { get; set; } -> DetailViewModelEdge"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ShowArrowheads(self) -> bool:"""ShowArrowheads { get; set; } -> bool"""
    @property
    def ShowViewLabel(self) -> bool:"""ShowViewLabel { get; set; } -> bool"""
    @property
    def ViewLabelAlignment(self) -> ModelDocViewLabelAlignmentType:"""ViewLabelAlignment { get; set; } -> ModelDocViewLabelAlignmentType"""
    @property
    def ViewLabelAttachment(self) -> ModelDocViewLabelAttachmentPoint:"""ViewLabelAttachment { get; set; } -> ModelDocViewLabelAttachmentPoint"""
    @property
    def ViewLabelOffset(self) -> float:"""ViewLabelOffset { get; set; } -> float"""
    @property
    def ViewLabelPattern(self) -> str:"""ViewLabelPattern { get; set; } -> str"""
    @property
    def ViewLabelTextColor(self) -> _n_0_t_0:"""ViewLabelTextColor { get; set; } -> Color"""
    @property
    def ViewLabelTextHeight(self) -> float:"""ViewLabelTextHeight { get; set; } -> float"""
    @property
    def ViewLabelTextStyleId(self) -> ObjectId:"""ViewLabelTextStyleId { get; set; } -> ObjectId"""
    def __init__(self) -> DetailViewStyle:...
    def DefaultViewName(self, index: int) -> str:...
    def GetViewLabelPattern(self, field: Field) -> str:...
    def PostViewStyleToDb(self, dataBasePointer: Database, styleName: str) -> ObjectId:...
    def SetDatabaseDefaults(self, dataBasePointer: Database):...
    def SetViewLabelPattern(self, pattern: str, field: Field):...
    def ValidateViewName(self, name: str) -> bool:...
class DgnDefinition(UnderlayDefinition, _n_6_t_0, _n_6_t_1):
    @property
    def SetShowRasterRef(self) -> bool:"""SetShowRasterRef { set; } -> bool"""
    @property
    def ShowRasterRef(self) -> bool:"""ShowRasterRef { get; } -> bool"""
    @property
    def UseMasterUnits(self) -> bool:"""UseMasterUnits { get; set; } -> bool"""
    @property
    def XrefDepth(self) -> int:"""XrefDepth { get; set; } -> int"""
    def __init__(self) -> DgnDefinition:...
class DgnReference(UnderlayReference, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> DgnReference:...
class DgnUnderlayItem(UnderlayItem, _n_6_t_0):
    @property
    def SetShowRasterRef(self) -> bool:"""SetShowRasterRef { set; } -> bool"""
    @property
    def ShowRasterRef(self) -> bool:"""ShowRasterRef { get; } -> bool"""
    @property
    def UseMasterUnits(self) -> bool:"""UseMasterUnits { get; set; } -> bool"""
class DiametricDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def ChordPoint(self) -> _n_2_t_1:"""ChordPoint { get; set; } -> Point3d"""
    @property
    def FarChordPoint(self) -> _n_2_t_1:"""FarChordPoint { get; set; } -> Point3d"""
    @property
    def LeaderLength(self) -> float:"""LeaderLength { get; set; } -> float"""
    def __init__(self, chordPoint: _n_2_t_1, farChordPoint: _n_2_t_1, leaderLength: float, dimensionText: str, dimensionStyle: ObjectId) -> DiametricDimension:...
    def __init__(self) -> DiametricDimension:...
class DictionaryWithDefaultDictionary(DBDictionary, _n_6_t_0, _n_6_t_1, _n_7_t_7):
    @property
    def DefaultId(self) -> ObjectId:"""DefaultId { get; set; } -> ObjectId"""
    def __init__(self) -> DictionaryWithDefaultDictionary:...
class DimArrowFlag(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    FirstArrow: int
    SecondArrow: int
    value__: int
class Dimension(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def AlternatePrefix(self) -> str:"""AlternatePrefix { get; set; } -> str"""
    @property
    def AlternateSuffix(self) -> str:"""AlternateSuffix { get; set; } -> str"""
    @property
    def AltSuppressLeadingZeros(self) -> bool:"""AltSuppressLeadingZeros { get; set; } -> bool"""
    @property
    def AltSuppressTrailingZeros(self) -> bool:"""AltSuppressTrailingZeros { get; set; } -> bool"""
    @property
    def AltSuppressZeroFeet(self) -> bool:"""AltSuppressZeroFeet { get; set; } -> bool"""
    @property
    def AltSuppressZeroInches(self) -> bool:"""AltSuppressZeroInches { get; set; } -> bool"""
    @property
    def AltToleranceSuppressLeadingZeros(self) -> bool:"""AltToleranceSuppressLeadingZeros { get; set; } -> bool"""
    @property
    def AltToleranceSuppressTrailingZeros(self) -> bool:"""AltToleranceSuppressTrailingZeros { get; set; } -> bool"""
    @property
    def AltToleranceSuppressZeroFeet(self) -> bool:"""AltToleranceSuppressZeroFeet { get; set; } -> bool"""
    @property
    def AltToleranceSuppressZeroInches(self) -> bool:"""AltToleranceSuppressZeroInches { get; set; } -> bool"""
    @property
    def CenterMarkSize(self) -> float:"""CenterMarkSize { get; } -> float"""
    @property
    def CenterMarkType(self) -> DimensionCenterMarkType:"""CenterMarkType { get; } -> DimensionCenterMarkType"""
    @property
    def Dimadec(self) -> int:"""Dimadec { get; set; } -> int"""
    @property
    def Dimalt(self) -> bool:"""Dimalt { get; set; } -> bool"""
    @property
    def Dimaltd(self) -> int:"""Dimaltd { get; set; } -> int"""
    @property
    def Dimaltf(self) -> float:"""Dimaltf { get; set; } -> float"""
    @property
    def Dimaltmzf(self) -> float:"""Dimaltmzf { get; set; } -> float"""
    @property
    def Dimaltmzs(self) -> str:"""Dimaltmzs { get; set; } -> str"""
    @property
    def Dimaltrnd(self) -> float:"""Dimaltrnd { get; set; } -> float"""
    @property
    def Dimalttd(self) -> int:"""Dimalttd { get; set; } -> int"""
    @property
    def Dimalttz(self) -> int:"""Dimalttz { get; set; } -> int"""
    @property
    def Dimaltu(self) -> int:"""Dimaltu { get; set; } -> int"""
    @property
    def Dimaltz(self) -> int:"""Dimaltz { get; set; } -> int"""
    @property
    def Dimapost(self) -> str:"""Dimapost { get; set; } -> str"""
    @property
    def Dimarcsym(self) -> int:"""Dimarcsym { get; set; } -> int"""
    @property
    def Dimasz(self) -> float:"""Dimasz { get; set; } -> float"""
    @property
    def Dimatfit(self) -> int:"""Dimatfit { get; set; } -> int"""
    @property
    def Dimaunit(self) -> int:"""Dimaunit { get; set; } -> int"""
    @property
    def Dimazin(self) -> int:"""Dimazin { get; set; } -> int"""
    @property
    def Dimblk(self) -> ObjectId:"""Dimblk { get; set; } -> ObjectId"""
    @property
    def Dimblk1(self) -> ObjectId:"""Dimblk1 { get; set; } -> ObjectId"""
    @property
    def Dimblk2(self) -> ObjectId:"""Dimblk2 { get; set; } -> ObjectId"""
    @property
    def DimBlockId(self) -> ObjectId:"""DimBlockId { get; set; } -> ObjectId"""
    @property
    def DimBlockPosition(self) -> _n_2_t_1:"""DimBlockPosition { get; } -> Point3d"""
    @property
    def Dimcen(self) -> float:"""Dimcen { get; set; } -> float"""
    @property
    def Dimclrd(self) -> _n_0_t_0:"""Dimclrd { get; set; } -> Color"""
    @property
    def Dimclre(self) -> _n_0_t_0:"""Dimclre { get; set; } -> Color"""
    @property
    def Dimclrt(self) -> _n_0_t_0:"""Dimclrt { get; set; } -> Color"""
    @property
    def Dimdec(self) -> int:"""Dimdec { get; set; } -> int"""
    @property
    def Dimdle(self) -> float:"""Dimdle { get; set; } -> float"""
    @property
    def Dimdli(self) -> float:"""Dimdli { get; set; } -> float"""
    @property
    def Dimdsep(self) -> _n_6_t_18:"""Dimdsep { get; set; } -> Char"""
    @property
    def DimensionStyle(self) -> ObjectId:"""DimensionStyle { get; set; } -> ObjectId"""
    @property
    def DimensionStyleName(self) -> str:"""DimensionStyleName { get; set; } -> str"""
    @property
    def DimensionText(self) -> str:"""DimensionText { get; set; } -> str"""
    @property
    def Dimexe(self) -> float:"""Dimexe { get; set; } -> float"""
    @property
    def Dimexo(self) -> float:"""Dimexo { get; set; } -> float"""
    @property
    def Dimfrac(self) -> int:"""Dimfrac { get; set; } -> int"""
    @property
    def Dimfxlen(self) -> float:"""Dimfxlen { get; set; } -> float"""
    @property
    def DimfxlenOn(self) -> bool:"""DimfxlenOn { get; set; } -> bool"""
    @property
    def Dimgap(self) -> float:"""Dimgap { get; set; } -> float"""
    @property
    def Dimjogang(self) -> float:"""Dimjogang { get; set; } -> float"""
    @property
    def Dimjust(self) -> int:"""Dimjust { get; set; } -> int"""
    @property
    def Dimldrblk(self) -> ObjectId:"""Dimldrblk { get; set; } -> ObjectId"""
    @property
    def Dimlfac(self) -> float:"""Dimlfac { get; set; } -> float"""
    @property
    def Dimlim(self) -> bool:"""Dimlim { get; set; } -> bool"""
    @property
    def Dimltex1(self) -> ObjectId:"""Dimltex1 { get; set; } -> ObjectId"""
    @property
    def Dimltex2(self) -> ObjectId:"""Dimltex2 { get; set; } -> ObjectId"""
    @property
    def Dimltype(self) -> ObjectId:"""Dimltype { get; set; } -> ObjectId"""
    @property
    def Dimlunit(self) -> int:"""Dimlunit { get; set; } -> int"""
    @property
    def Dimlwd(self) -> LineWeight:"""Dimlwd { get; set; } -> LineWeight"""
    @property
    def Dimlwe(self) -> LineWeight:"""Dimlwe { get; set; } -> LineWeight"""
    @property
    def Dimmzf(self) -> float:"""Dimmzf { get; set; } -> float"""
    @property
    def Dimmzs(self) -> str:"""Dimmzs { get; set; } -> str"""
    @property
    def Dimpost(self) -> str:"""Dimpost { get; set; } -> str"""
    @property
    def Dimrnd(self) -> float:"""Dimrnd { get; set; } -> float"""
    @property
    def Dimsah(self) -> bool:"""Dimsah { get; set; } -> bool"""
    @property
    def Dimscale(self) -> float:"""Dimscale { get; set; } -> float"""
    @property
    def Dimsd1(self) -> bool:"""Dimsd1 { get; set; } -> bool"""
    @property
    def Dimsd2(self) -> bool:"""Dimsd2 { get; set; } -> bool"""
    @property
    def Dimse1(self) -> bool:"""Dimse1 { get; set; } -> bool"""
    @property
    def Dimse2(self) -> bool:"""Dimse2 { get; set; } -> bool"""
    @property
    def Dimsoxd(self) -> bool:"""Dimsoxd { get; set; } -> bool"""
    @property
    def Dimtad(self) -> int:"""Dimtad { get; set; } -> int"""
    @property
    def Dimtdec(self) -> int:"""Dimtdec { get; set; } -> int"""
    @property
    def Dimtfac(self) -> float:"""Dimtfac { get; set; } -> float"""
    @property
    def Dimtfill(self) -> int:"""Dimtfill { get; set; } -> int"""
    @property
    def Dimtfillclr(self) -> _n_0_t_0:"""Dimtfillclr { get; set; } -> Color"""
    @property
    def Dimtih(self) -> bool:"""Dimtih { get; set; } -> bool"""
    @property
    def Dimtix(self) -> bool:"""Dimtix { get; set; } -> bool"""
    @property
    def Dimtm(self) -> float:"""Dimtm { get; set; } -> float"""
    @property
    def Dimtmove(self) -> int:"""Dimtmove { get; set; } -> int"""
    @property
    def Dimtofl(self) -> bool:"""Dimtofl { get; set; } -> bool"""
    @property
    def Dimtoh(self) -> bool:"""Dimtoh { get; set; } -> bool"""
    @property
    def Dimtol(self) -> bool:"""Dimtol { get; set; } -> bool"""
    @property
    def Dimtolj(self) -> int:"""Dimtolj { get; set; } -> int"""
    @property
    def Dimtp(self) -> float:"""Dimtp { get; set; } -> float"""
    @property
    def Dimtsz(self) -> float:"""Dimtsz { get; set; } -> float"""
    @property
    def Dimtvp(self) -> float:"""Dimtvp { get; set; } -> float"""
    @property
    def Dimtxt(self) -> float:"""Dimtxt { get; set; } -> float"""
    @property
    def Dimtxtdirection(self) -> bool:"""Dimtxtdirection { get; set; } -> bool"""
    @property
    def Dimtzin(self) -> int:"""Dimtzin { get; set; } -> int"""
    @property
    def Dimupt(self) -> bool:"""Dimupt { get; set; } -> bool"""
    @property
    def Dimzin(self) -> int:"""Dimzin { get; set; } -> int"""
    @property
    def DynamicDimension(self) -> bool:"""DynamicDimension { get; set; } -> bool"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def HorizontalRotation(self) -> float:"""HorizontalRotation { get; set; } -> float"""
    @property
    def Measurement(self) -> float:"""Measurement { get; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Prefix(self) -> str:"""Prefix { get; set; } -> str"""
    @property
    def Suffix(self) -> str:"""Suffix { get; set; } -> str"""
    @property
    def SuppressAngularLeadingZeros(self) -> bool:"""SuppressAngularLeadingZeros { get; set; } -> bool"""
    @property
    def SuppressAngularTrailingZeros(self) -> bool:"""SuppressAngularTrailingZeros { get; set; } -> bool"""
    @property
    def SuppressLeadingZeros(self) -> bool:"""SuppressLeadingZeros { get; set; } -> bool"""
    @property
    def SuppressTrailingZeros(self) -> bool:"""SuppressTrailingZeros { get; set; } -> bool"""
    @property
    def SuppressZeroFeet(self) -> bool:"""SuppressZeroFeet { get; set; } -> bool"""
    @property
    def SuppressZeroInches(self) -> bool:"""SuppressZeroInches { get; set; } -> bool"""
    @property
    def TextAttachment(self) -> AttachmentPoint:"""TextAttachment { get; set; } -> AttachmentPoint"""
    @property
    def TextDefinedSize(self) -> _n_2_t_14:"""TextDefinedSize { get; set; } -> Vector2d"""
    @property
    def TextLineSpacingFactor(self) -> float:"""TextLineSpacingFactor { get; set; } -> float"""
    @property
    def TextLineSpacingStyle(self) -> LineSpacingStyle:"""TextLineSpacingStyle { get; set; } -> LineSpacingStyle"""
    @property
    def TextPosition(self) -> _n_2_t_1:"""TextPosition { get; set; } -> Point3d"""
    @property
    def TextRotation(self) -> float:"""TextRotation { get; set; } -> float"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    @property
    def ToleranceSuppressLeadingZeros(self) -> bool:"""ToleranceSuppressLeadingZeros { get; set; } -> bool"""
    @property
    def ToleranceSuppressTrailingZeros(self) -> bool:"""ToleranceSuppressTrailingZeros { get; set; } -> bool"""
    @property
    def ToleranceSuppressZeroFeet(self) -> bool:"""ToleranceSuppressZeroFeet { get; set; } -> bool"""
    @property
    def ToleranceSuppressZeroInches(self) -> bool:"""ToleranceSuppressZeroInches { get; set; } -> bool"""
    @property
    def UsingDefaultTextPosition(self) -> bool:"""UsingDefaultTextPosition { get; set; } -> bool"""
    def FieldFromMText(self, dimMText: MText):...
    def FieldToMText(self, dimMText: MText):...
    def FormatMeasurement(self, measurement: float, dimensionText: str) -> str:...
    def GenerateLayout(self):...
    def GetDimstyleData(self) -> DimStyleTableRecord:...
    def RecomputeDimensionBlock(self, forceUpdate: bool):...
    def RemoveTextField(self):...
    def ResetTextDefinedSize(self):...
    def SetDimstyleData(self, style: DimStyleTableRecord):...
class DimensionCenterMarkType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Line: int
    Mark: int
    _None: int
    value__: int
class DimensionStyleOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def DimensionStyle(self, dimension: Dimension) -> ObjectId:...
    def GetDimstyleData(self, dimension: Dimension, style: DimStyleTableRecord):...
    def SetDimensionStyle(self, dimension: Dimension, id: ObjectId):...
    def SetDimstyleData(self, dimension: Dimension, dimstyleId: ObjectId):...
    def SetDimstyleData(self, dimension: Dimension, style: DimStyleTableRecord):...
class DimStyleTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class DimStyleTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def Dimadec(self) -> int:"""Dimadec { get; set; } -> int"""
    @property
    def Dimalt(self) -> bool:"""Dimalt { get; set; } -> bool"""
    @property
    def Dimaltd(self) -> int:"""Dimaltd { get; set; } -> int"""
    @property
    def Dimaltf(self) -> float:"""Dimaltf { get; set; } -> float"""
    @property
    def Dimaltrnd(self) -> float:"""Dimaltrnd { get; set; } -> float"""
    @property
    def Dimalttd(self) -> int:"""Dimalttd { get; set; } -> int"""
    @property
    def Dimalttz(self) -> int:"""Dimalttz { get; set; } -> int"""
    @property
    def Dimaltu(self) -> int:"""Dimaltu { get; set; } -> int"""
    @property
    def Dimaltz(self) -> int:"""Dimaltz { get; set; } -> int"""
    @property
    def Dimapost(self) -> str:"""Dimapost { get; set; } -> str"""
    @property
    def Dimarcsym(self) -> int:"""Dimarcsym { get; set; } -> int"""
    @property
    def Dimasz(self) -> float:"""Dimasz { get; set; } -> float"""
    @property
    def Dimatfit(self) -> int:"""Dimatfit { get; set; } -> int"""
    @property
    def Dimaunit(self) -> int:"""Dimaunit { get; set; } -> int"""
    @property
    def Dimazin(self) -> int:"""Dimazin { get; set; } -> int"""
    @property
    def Dimblk(self) -> ObjectId:"""Dimblk { get; set; } -> ObjectId"""
    @property
    def Dimblk1(self) -> ObjectId:"""Dimblk1 { get; set; } -> ObjectId"""
    @property
    def Dimblk2(self) -> ObjectId:"""Dimblk2 { get; set; } -> ObjectId"""
    @property
    def Dimcen(self) -> float:"""Dimcen { get; set; } -> float"""
    @property
    def Dimclrd(self) -> _n_0_t_0:"""Dimclrd { get; set; } -> Color"""
    @property
    def Dimclre(self) -> _n_0_t_0:"""Dimclre { get; set; } -> Color"""
    @property
    def Dimclrt(self) -> _n_0_t_0:"""Dimclrt { get; set; } -> Color"""
    @property
    def Dimdec(self) -> int:"""Dimdec { get; set; } -> int"""
    @property
    def Dimdle(self) -> float:"""Dimdle { get; set; } -> float"""
    @property
    def Dimdli(self) -> float:"""Dimdli { get; set; } -> float"""
    @property
    def Dimdsep(self) -> _n_6_t_18:"""Dimdsep { get; set; } -> Char"""
    @property
    def Dimexe(self) -> float:"""Dimexe { get; set; } -> float"""
    @property
    def Dimexo(self) -> float:"""Dimexo { get; set; } -> float"""
    @property
    def Dimfrac(self) -> int:"""Dimfrac { get; set; } -> int"""
    @property
    def Dimfxlen(self) -> float:"""Dimfxlen { get; set; } -> float"""
    @property
    def DimfxlenOn(self) -> bool:"""DimfxlenOn { get; set; } -> bool"""
    @property
    def Dimgap(self) -> float:"""Dimgap { get; set; } -> float"""
    @property
    def Dimjogang(self) -> float:"""Dimjogang { get; set; } -> float"""
    @property
    def Dimjust(self) -> int:"""Dimjust { get; set; } -> int"""
    @property
    def Dimldrblk(self) -> ObjectId:"""Dimldrblk { get; set; } -> ObjectId"""
    @property
    def Dimlfac(self) -> float:"""Dimlfac { get; set; } -> float"""
    @property
    def Dimlim(self) -> bool:"""Dimlim { get; set; } -> bool"""
    @property
    def Dimltex1(self) -> ObjectId:"""Dimltex1 { get; set; } -> ObjectId"""
    @property
    def Dimltex2(self) -> ObjectId:"""Dimltex2 { get; set; } -> ObjectId"""
    @property
    def Dimltype(self) -> ObjectId:"""Dimltype { get; set; } -> ObjectId"""
    @property
    def Dimlunit(self) -> int:"""Dimlunit { get; set; } -> int"""
    @property
    def Dimlwd(self) -> LineWeight:"""Dimlwd { get; set; } -> LineWeight"""
    @property
    def Dimlwe(self) -> LineWeight:"""Dimlwe { get; set; } -> LineWeight"""
    @property
    def Dimpost(self) -> str:"""Dimpost { get; set; } -> str"""
    @property
    def Dimrnd(self) -> float:"""Dimrnd { get; set; } -> float"""
    @property
    def Dimsah(self) -> bool:"""Dimsah { get; set; } -> bool"""
    @property
    def Dimscale(self) -> float:"""Dimscale { get; set; } -> float"""
    @property
    def Dimsd1(self) -> bool:"""Dimsd1 { get; set; } -> bool"""
    @property
    def Dimsd2(self) -> bool:"""Dimsd2 { get; set; } -> bool"""
    @property
    def Dimse1(self) -> bool:"""Dimse1 { get; set; } -> bool"""
    @property
    def Dimse2(self) -> bool:"""Dimse2 { get; set; } -> bool"""
    @property
    def Dimsoxd(self) -> bool:"""Dimsoxd { get; set; } -> bool"""
    @property
    def Dimtad(self) -> int:"""Dimtad { get; set; } -> int"""
    @property
    def Dimtdec(self) -> int:"""Dimtdec { get; set; } -> int"""
    @property
    def Dimtfac(self) -> float:"""Dimtfac { get; set; } -> float"""
    @property
    def Dimtfill(self) -> int:"""Dimtfill { get; set; } -> int"""
    @property
    def Dimtfillclr(self) -> _n_0_t_0:"""Dimtfillclr { get; set; } -> Color"""
    @property
    def Dimtih(self) -> bool:"""Dimtih { get; set; } -> bool"""
    @property
    def Dimtix(self) -> bool:"""Dimtix { get; set; } -> bool"""
    @property
    def Dimtm(self) -> float:"""Dimtm { get; set; } -> float"""
    @property
    def Dimtmove(self) -> int:"""Dimtmove { get; set; } -> int"""
    @property
    def Dimtofl(self) -> bool:"""Dimtofl { get; set; } -> bool"""
    @property
    def Dimtoh(self) -> bool:"""Dimtoh { get; set; } -> bool"""
    @property
    def Dimtol(self) -> bool:"""Dimtol { get; set; } -> bool"""
    @property
    def Dimtolj(self) -> int:"""Dimtolj { get; set; } -> int"""
    @property
    def Dimtp(self) -> float:"""Dimtp { get; set; } -> float"""
    @property
    def Dimtsz(self) -> float:"""Dimtsz { get; set; } -> float"""
    @property
    def Dimtvp(self) -> float:"""Dimtvp { get; set; } -> float"""
    @property
    def Dimtxsty(self) -> ObjectId:"""Dimtxsty { get; set; } -> ObjectId"""
    @property
    def Dimtxt(self) -> float:"""Dimtxt { get; set; } -> float"""
    @property
    def Dimtxtdirection(self) -> bool:"""Dimtxtdirection { get; set; } -> bool"""
    @property
    def Dimtzin(self) -> int:"""Dimtzin { get; set; } -> int"""
    @property
    def Dimupt(self) -> bool:"""Dimupt { get; set; } -> bool"""
    @property
    def Dimzin(self) -> int:"""Dimzin { get; set; } -> int"""
    @property
    def IsModifiedForRecompute(self) -> bool:"""IsModifiedForRecompute { get; } -> bool"""
    def __init__(self) -> DimStyleTableRecord:...
    def GetArrowId(self, whichArrow: DimArrowFlag) -> ObjectId:...
class DistanceConstraint(ExplicitConstraint, _n_6_t_0, _n_6_t_1):
    @property
    def ConstrainedLineId(self) -> _n_6_t_11:"""ConstrainedLineId { get; } -> UInt32"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; } -> Vector3d"""
    @property
    def DirectionType(self) -> DistanceConstraint.DistanceDirectionType:"""DirectionType { get; } -> DistanceConstraint.DistanceDirectionType"""
    def __init__(self, consLineId: _n_6_t_11, type: DistanceConstraint.DistanceDirectionType) -> DistanceConstraint:...
    def __init__(self, direction: _n_2_t_3) -> DistanceConstraint:...
    def __init__(self) -> DistanceConstraint:...
    class DistanceDirectionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        FixedDirection: int
        NotDirected: int
        ParallelToLine: int
        PerpendicularToLine: int
        value__: int
class DragStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DragAbort: int
    DragEnd: int
    DragStart: int
    value__: int
class DrawLeaderOrderType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DrawLeaderHeadFirst: int
    DrawLeaderTailFirst: int
    value__: int
class DrawMLeaderOrderType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DrawContentFirst: int
    DrawLeaderFirst: int
    value__: int
class DrawOrderTable(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def BlockId(self) -> ObjectId:"""BlockId { get; set; } -> ObjectId"""
    def FirstEntityIsDrawnBeforeSecond(self, first: ObjectId, second: ObjectId) -> bool:...
    def GetFullDrawOrder(self, honorSortEntitiesMask: _n_6_t_19) -> ObjectIdCollection:...
    def GetRelativeDrawOrder(self, honorSortEntitiesMask: _n_6_t_19) -> ObjectIdCollection:...
    def GetSortHandle(self, id: ObjectId) -> Handle:...
    def MoveAbove(self, collection: ObjectIdCollection, target: ObjectId):...
    def MoveBelow(self, collection: ObjectIdCollection, target: ObjectId):...
    def MoveToBottom(self, collection: ObjectIdCollection):...
    def MoveToTop(self, collection: ObjectIdCollection):...
    def SetRelativeDrawOrder(self, collection: ObjectIdCollection):...
    def SwapOrder(self, id1: ObjectId, id2: ObjectId):...
class DuplicateRecordCloning(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Ignore: int
    MangleName: int
    NotApplicable: int
    RefMangleName: int
    Replace: int
    UnmangleName: int
    value__: int
class DwfDefinition(UnderlayDefinition, _n_6_t_0, _n_6_t_1):
    @property
    def isDWFx(self) -> bool:"""isDWFx { get; } -> bool"""
    def __init__(self) -> DwfDefinition:...
class DwfReference(UnderlayReference, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> DwfReference:...
class DwgFiler(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def DwgVersion(self) -> FullDwgVersion:"""DwgVersion { get; } -> FullDwgVersion"""
    @property
    def FilerStatus(self) -> _n_5_t_1:"""FilerStatus { get; set; } -> ErrorStatus"""
    @property
    def FilerType(self) -> FilerType:"""FilerType { get; } -> FilerType"""
    @property
    def Position(self) -> int:"""Position { get; } -> int"""
    def ReadAddress(self) -> _n_6_t_3:...
    def ReadBinaryChunk(self) -> _n_6_t_10[_n_6_t_19]:...
    def ReadBoolean(self) -> bool:...
    def ReadByte(self) -> _n_6_t_19:...
    def ReadBytes(self, value: _n_6_t_10[_n_6_t_19]):...
    def ReadDouble(self) -> float:...
    def ReadHandle(self) -> Handle:...
    def ReadHardOwnershipId(self) -> ObjectId:...
    def ReadHardPointerId(self) -> ObjectId:...
    def ReadInt16(self) -> int:...
    def ReadInt32(self) -> int:...
    def ReadInt64(self) -> int:...
    def ReadPoint2d(self) -> _n_2_t_0:...
    def ReadPoint3d(self) -> _n_2_t_1:...
    def ReadScale3d(self) -> _n_2_t_11:...
    def ReadSoftOwnershipId(self) -> ObjectId:...
    def ReadSoftPointerId(self) -> ObjectId:...
    def ReadString(self) -> str:...
    def ReadUInt16(self) -> _n_6_t_23:...
    def ReadUInt32(self) -> _n_6_t_11:...
    def ReadUInt64(self) -> _n_6_t_24:...
    def ReadVector2d(self) -> _n_2_t_14:...
    def ReadVector3d(self) -> _n_2_t_3:...
    def ResetFilerStatus(self):...
    def Seek(self, offset: int, method: int):...
    def WriteAddress(self, value: _n_6_t_3):...
    def WriteBinaryChunk(self, chunk: _n_6_t_10[_n_6_t_19]):...
    def WriteBoolean(self, value: bool):...
    def WriteByte(self, value: _n_6_t_19):...
    def WriteBytes(self, value: _n_6_t_10[_n_6_t_19]):...
    def WriteDouble(self, value: float):...
    def WriteHandle(self, handle: Handle):...
    def WriteHardOwnershipId(self, value: ObjectId):...
    def WriteHardPointerId(self, value: ObjectId):...
    def WriteInt16(self, value: int):...
    def WriteInt32(self, value: int):...
    def WriteInt64(self, value: int):...
    def WritePoint2d(self, value: _n_2_t_0):...
    def WritePoint3d(self, value: _n_2_t_1):...
    def WriteScale3d(self, value: _n_2_t_11):...
    def WriteSoftOwnershipId(self, value: ObjectId):...
    def WriteSoftPointerId(self, value: ObjectId):...
    def WriteString(self, value: str):...
    def WriteUInt16(self, value: _n_6_t_23):...
    def WriteUInt32(self, value: _n_6_t_11):...
    def WriteUInt64(self, value: _n_6_t_24):...
    def WriteVector2d(self, value: _n_2_t_14):...
    def WriteVector3d(self, value: _n_2_t_3):...
class DwgVersion(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AC1001: int
    AC1002: int
    AC1003: int
    AC1004: int
    AC1005: int
    AC1006: int
    AC1007: int
    AC1008: int
    AC1009: int
    AC1010: int
    AC1011: int
    AC1012: int
    AC1013: int
    AC1014: int
    AC1015: int
    AC1021: int
    AC1024: int
    AC1027: int
    AC1500: int
    AC1800: int
    AC1800a: int
    AC1To2: int
    AC1To40: int
    AC1To50: int
    AC2100a: int
    AC2400a: int
    AC2700a: int
    AC2To10: int
    AC2To20: int
    AC2To21: int
    AC2To22: int
    Current: int
    Max: int
    MC0To0: int
    Newest: int
    Unknown: int
    value__: int
class DxfCode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Alpha: int
    Angle: int
    ArbitraryHandle: int
    AttributePrompt: int
    AttributeTag: int
    BinaryChunk: int
    BlockName: int
    Bool: int
    CircleSides: int
    CLShapeName: int
    CLShapeText: int
    Color: int
    ColorName: int
    ColorRgb: int
    Comment: int
    ControlString: int
    DashLength: int
    Description: int
    DimBlk1: int
    DimBlk2: int
    DimensionAlternativePrefixSuffix: int
    DimensionBlock: int
    DimPostString: int
    DimStyleName: int
    DimVarHandle: int
    Elevation: int
    EmbeddedObjectStart: int
    End: int
    ExtendedDataAsciiString: int
    ExtendedDataBinaryChunk: int
    ExtendedDataControlString: int
    ExtendedDataDist: int
    ExtendedDataHandle: int
    ExtendedDataInteger16: int
    ExtendedDataInteger32: int
    ExtendedDataLayerName: int
    ExtendedDataReal: int
    ExtendedDataRegAppName: int
    ExtendedDataScale: int
    ExtendedDataWorldXCoordinate: int
    ExtendedDataWorldXDir: int
    ExtendedDataWorldXDisp: int
    ExtendedDataWorldYCoordinate: int
    ExtendedDataWorldYDir: int
    ExtendedDataWorldYDisp: int
    ExtendedDataWorldZCoordinate: int
    ExtendedDataWorldZDir: int
    ExtendedDataWorldZDisp: int
    ExtendedDataXCoordinate: int
    ExtendedDataYCoordinate: int
    ExtendedDataZCoordinate: int
    ExtendedInt16: int
    FirstEntityId: int
    GradientAngle: int
    GradientColCount: int
    GradientColVal: int
    GradientName: int
    GradientObjType: int
    GradientPatType: int
    GradientShift: int
    GradientTintType: int
    GradientTintVal: int
    Handle: int
    HardOwnershipId: int
    HardPointerId: int
    HasSubentities: int
    HeaderId: int
    Int16: int
    Int32: int
    Int64: int
    Int8: int
    Invalid: int
    LayerLinetype: int
    LayerName: int
    LayoutName: int
    LinetypeAlign: int
    LinetypeElement: int
    LinetypeName: int
    LinetypePdc: int
    LinetypeProse: int
    LinetypeScale: int
    LineWeight: int
    MlineOffset: int
    MlineStyleName: int
    NormalX: int
    NormalY: int
    NormalZ: int
    Operator: int
    PixelScale: int
    PlotStyleNameId: int
    PlotStyleNameType: int
    PReactors: int
    Real: int
    RegAppFlags: int
    RenderMode: int
    ShapeName: int
    ShapeScale: int
    ShapeXOffset: int
    ShapeYOffset: int
    SoftOwnershipId: int
    SoftPointerId: int
    Start: int
    Subclass: int
    SymbolTableName: int
    SymbolTableRecordComments: int
    SymbolTableRecordName: int
    Text: int
    TextBigFontFile: int
    TextFontFile: int
    TextStyleName: int
    Thickness: int
    TxtSize: int
    TxtStyleFlags: int
    TxtStylePSize: int
    TxtStyleXScale: int
    UcsOrg: int
    UcsOrientationX: int
    UcsOrientationY: int
    value__: int
    ViewBackClip: int
    ViewBrightness: int
    ViewContrast: int
    ViewFrontClip: int
    ViewHeight: int
    ViewLensLength: int
    ViewMode: int
    ViewportActive: int
    ViewportAspect: int
    ViewportGrid: int
    ViewportHeight: int
    ViewportIcon: int
    ViewportNumber: int
    ViewportSnap: int
    ViewportSnapAngle: int
    ViewportSnapPair: int
    ViewportSnapStyle: int
    ViewportTwist: int
    ViewportVisibility: int
    ViewportZoom: int
    ViewWidth: int
    Visibility: int
    XCoordinate: int
    XDataStart: int
    XDictionary: int
    XInt16: int
    XReal: int
    XRefPath: int
    XTextString: int
    XXInt16: int
    YCoordinate: int
    ZCoordinate: int
class DxfFiler(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def AtEmbeddedObjectStart(self) -> bool:"""AtEmbeddedObjectStart { get; } -> bool"""
    @property
    def AtEndOfFile(self) -> bool:"""AtEndOfFile { get; } -> bool"""
    @property
    def AtEndOfObject(self) -> bool:"""AtEndOfObject { get; } -> bool"""
    @property
    def AtExtendedData(self) -> bool:"""AtExtendedData { get; } -> bool"""
    @property
    def Database(self) -> Database:"""Database { get; } -> Database"""
    @property
    def DwgVersion(self) -> FullDwgVersion:"""DwgVersion { get; } -> FullDwgVersion"""
    @property
    def Elevation(self) -> float:"""Elevation { get; } -> float"""
    @property
    def ErrorMessage(self) -> str:"""ErrorMessage { get; } -> str"""
    @property
    def FilerType(self) -> FilerType:"""FilerType { get; } -> FilerType"""
    @property
    def IncludesDefaultValues(self) -> bool:"""IncludesDefaultValues { get; } -> bool"""
    @property
    def IsModifyingExistingObject(self) -> bool:"""IsModifyingExistingObject { get; } -> bool"""
    @property
    def Precision(self) -> int:"""Precision { get; set; } -> int"""
    @property
    def Thickness(self) -> float:"""Thickness { get; } -> float"""
    def AtSubclassData(self, value: str) -> bool:...
    def FilerStatus(self):...
    def HaltAtClassBoundaries(self, value: bool):...
    def PushBackItem(self):...
    def ReadResultBuffer(self) -> ResultBuffer:...
    def ResetFilerStatus(self):...
    def RewindFiler(self) -> int:...
    def SetError(self, format: str, values: _n_6_t_10[str]):...
    def SetError(self, value: _n_5_t_1, format: str, values: _n_6_t_10[str]):...
    def WriteBool(self, opCode: DxfCode, value: bool):...
    def WriteBoolean(self, opCode: DxfCode, value: bool):...
    def WriteByte(self, opCode: DxfCode, value: _n_6_t_19):...
    def WriteBytes(self, opCode: DxfCode, chunk: _n_6_t_10[_n_6_t_19]):...
    def WriteDouble(self, opCode: DxfCode, value: float, precision: int):...
    def WriteEmbeddedObjectStart(self):...
    def WriteHandle(self, opCode: DxfCode, value: Handle):...
    def WriteInt16(self, opCode: DxfCode, value: int):...
    def WriteInt32(self, opCode: DxfCode, value: int):...
    def WriteInt64(self, opCode: DxfCode, value: int):...
    def WriteObjectId(self, opCode: DxfCode, value: ObjectId):...
    def WritePoint2d(self, opCode: DxfCode, value: _n_2_t_0, precision: int):...
    def WritePoint3d(self, opCode: DxfCode, value: _n_2_t_1, precision: int):...
    def WriteResultBuffer(self, buffer: ResultBuffer):...
    def WriteScale3d(self, opCode: DxfCode, value: _n_2_t_11, precision: int):...
    def WriteString(self, opCode: DxfCode, value: str):...
    def WriteUInt16(self, opCode: DxfCode, value: _n_6_t_23):...
    def WriteUInt32(self, opCode: DxfCode, value: _n_6_t_11):...
    def WriteUInt64(self, opCode: DxfCode, value: _n_6_t_24):...
    def WriteVector2d(self, opCode: DxfCode, value: _n_2_t_14, precision: int):...
    def WriteVector3d(self, opCode: DxfCode, value: _n_2_t_3, precision: int):...
    def WriteXDataStart(self):...
class DynamicBlockReferenceProperty(object):
    @property
    def BlockId(self) -> ObjectId:"""BlockId { get; } -> ObjectId"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def PropertyName(self) -> str:"""PropertyName { get; } -> str"""
    @property
    def PropertyTypeCode(self) -> int:"""PropertyTypeCode { get; } -> int"""
    @property
    def ReadOnly(self) -> bool:"""ReadOnly { get; } -> bool"""
    @property
    def Show(self) -> bool:"""Show { get; } -> bool"""
    @property
    def UnitsType(self) -> DynamicBlockReferencePropertyUnitsType:"""UnitsType { get; } -> DynamicBlockReferencePropertyUnitsType"""
    @property
    def Value(self) -> object:"""Value { get; set; } -> object"""
    @property
    def VisibleInCurrentVisibilityState(self) -> bool:"""VisibleInCurrentVisibilityState { get; } -> bool"""
    def GetAllowedValues(self) -> _n_6_t_10[object]:...
class DynamicBlockReferencePropertyCollection(_n_5_t_3, _n_6_t_0, _n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> DynamicBlockReferenceProperty:"""Item { get; } -> DynamicBlockReferenceProperty"""
class DynamicBlockReferencePropertyCollectionEnumerator(_n_7_t_3):
    pass
class DynamicBlockReferencePropertyUnitsType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Angular: int
    Area: int
    Distance: int
    NoUnits: int
    value__: int
class DynamicDimensionChangedEventArgs(_n_6_t_13):
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def Value(self) -> float:"""Value { get; } -> float"""
    def __init__(self, index: int, value: float) -> DynamicDimensionChangedEventArgs:...
class DynamicDimensionData(_n_5_t_3, _n_6_t_0):
    @property
    def ApplicationData(self) -> object:"""ApplicationData { get; set; } -> object"""
    @property
    def Dimension(self) -> Dimension:"""Dimension { get; set; } -> Dimension"""
    @property
    def Editable(self) -> bool:"""Editable { get; set; } -> bool"""
    @property
    def Focal(self) -> bool:"""Focal { get; set; } -> bool"""
    @property
    def HideIfValueIsZero(self) -> bool:"""HideIfValueIsZero { get; set; } -> bool"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    def __init__(self) -> DynamicDimensionData:...
    def __init__(self, dimension: Dimension) -> DynamicDimensionData:...
    def __init__(self, dimension: Dimension, editable: bool) -> DynamicDimensionData:...
    def __init__(self, dimension: Dimension, editable: bool, hideIfValueIsZero: bool) -> DynamicDimensionData:...
class DynamicDimensionDataCollection(_n_5_t_3, _n_6_t_0, _n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> DynamicDimensionData:"""Item { get; set; } -> DynamicDimensionData"""
    def __init__(self) -> DynamicDimensionDataCollection:...
    def Add(self, data: DynamicDimensionData) -> int:...
    def Clear(self):...
    def RemoveAt(self, i: int):...
class EdgeRef(SubentRef, _n_6_t_0, _n_6_t_1):
    @property
    def Curve(self) -> _n_2_t_7:"""Curve { get; } -> Curve3d"""
    @property
    def FaceSubentity(self) -> SubentityId:"""FaceSubentity { get; set; } -> SubentityId"""
    def __init__(self, curve: _n_2_t_7) -> EdgeRef:...
    def __init__(self, entity: Entity) -> EdgeRef:...
    def __init__(self, path: FullSubentityPath) -> EdgeRef:...
    def __init__(self, compoundObjectId: CompoundObjectId, edgeSubentId: SubentityId, faceSubentId: SubentityId, curve: _n_2_t_7) -> EdgeRef:...
    def __init__(self, compoundObjectId: CompoundObjectId, edgeSubentId: SubentityId, faceSubentId: SubentityId) -> EdgeRef:...
    def __init__(self, compoundObjectId: CompoundObjectId, edgeSubentId: SubentityId) -> EdgeRef:...
    def __init__(self, compoundObjectId: CompoundObjectId) -> EdgeRef:...
    def __init__(self) -> EdgeRef:...
class Ellipse(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def Center(self) -> _n_2_t_1:"""Center { get; set; } -> Point3d"""
    @property
    def EndAngle(self) -> float:"""EndAngle { get; set; } -> float"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def MajorAxis(self) -> _n_2_t_3:"""MajorAxis { get; } -> Vector3d"""
    @property
    def MajorRadius(self) -> float:"""MajorRadius { get; } -> float"""
    @property
    def MinorAxis(self) -> _n_2_t_3:"""MinorAxis { get; } -> Vector3d"""
    @property
    def MinorRadius(self) -> float:"""MinorRadius { get; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def RadiusRatio(self) -> float:"""RadiusRatio { get; set; } -> float"""
    @property
    def StartAngle(self) -> float:"""StartAngle { get; set; } -> float"""
    def __init__(self, center: _n_2_t_1, unitNormal: _n_2_t_3, majorAxis: _n_2_t_3, radiusRatio: float, startAngle: float, endAngle: float) -> Ellipse:...
    def __init__(self) -> Ellipse:...
    def GetAngleAtParameter(self, value: float) -> float:...
    def GetParameterAtAngle(self, angle: float) -> float:...
    def Set(self, center: _n_2_t_1, unitNormal: _n_2_t_3, majorAxis: _n_2_t_3, radiusRatio: float, startAngle: float, endAngle: float):...
class EndCap(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Angle: int
    _None: int
    Round: int
    Square: int
    value__: int
class Entity(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def BlockId(self) -> ObjectId:"""BlockId { get; } -> ObjectId"""
    @property
    def BlockName(self) -> str:"""BlockName { get; } -> str"""
    @property
    def CastShadows(self) -> bool:"""CastShadows { get; set; } -> bool"""
    @property
    def CloneMeForDragging(self) -> bool:"""CloneMeForDragging { get; } -> bool"""
    @property
    def CollisionType(self) -> CollisionType:"""CollisionType { get; } -> CollisionType"""
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; set; } -> Color"""
    @property
    def ColorIndex(self) -> int:"""ColorIndex { get; set; } -> int"""
    @property
    def CompoundObjectTransform(self) -> _n_2_t_6:"""CompoundObjectTransform { get; } -> Matrix3d"""
    @property
    def Ecs(self) -> _n_2_t_6:"""Ecs { get; } -> Matrix3d"""
    @property
    def EdgeStyleId(self) -> ObjectId:"""EdgeStyleId { get; set; } -> ObjectId"""
    @property
    def EntityColor(self) -> _n_0_t_2:"""EntityColor { get; } -> EntityColor"""
    @property
    def FaceStyleId(self) -> ObjectId:"""FaceStyleId { get; set; } -> ObjectId"""
    @property
    def ForceAnnoAllVisible(self) -> bool:"""ForceAnnoAllVisible { get; set; } -> bool"""
    @property
    def GeometricExtents(self) -> Extents3d:"""GeometricExtents { get; } -> Extents3d"""
    @property
    def Hyperlinks(self) -> HyperLinkCollection:"""Hyperlinks { get; } -> HyperLinkCollection"""
    @property
    def IsPlanar(self) -> bool:"""IsPlanar { get; } -> bool"""
    @property
    def Layer(self) -> str:"""Layer { get; set; } -> str"""
    @property
    def LayerId(self) -> ObjectId:"""LayerId { get; set; } -> ObjectId"""
    @property
    def Linetype(self) -> str:"""Linetype { get; set; } -> str"""
    @property
    def LinetypeId(self) -> ObjectId:"""LinetypeId { get; set; } -> ObjectId"""
    @property
    def LinetypeScale(self) -> float:"""LinetypeScale { get; set; } -> float"""
    @property
    def LineWeight(self) -> LineWeight:"""LineWeight { get; set; } -> LineWeight"""
    @property
    def Material(self) -> str:"""Material { get; set; } -> str"""
    @property
    def MaterialId(self) -> ObjectId:"""MaterialId { get; set; } -> ObjectId"""
    @property
    def MaterialMapper(self) -> _n_3_t_7:"""MaterialMapper { get; set; } -> Mapper"""
    @property
    def PlotStyleName(self) -> str:"""PlotStyleName { get; set; } -> str"""
    @property
    def PlotStyleNameId(self) -> PlotStyleDescriptor:"""PlotStyleNameId { get; set; } -> PlotStyleDescriptor"""
    @property
    def ReceiveShadows(self) -> bool:"""ReceiveShadows { get; set; } -> bool"""
    @property
    def Transparency(self) -> _n_0_t_1:"""Transparency { get; set; } -> Transparency"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    @property
    def VisualStyleId(self) -> ObjectId:"""VisualStyleId { get; set; } -> ObjectId"""
    def AddSubentityPaths(self, subPaths: _n_6_t_10[FullSubentityPath]):...
    def BoundingBoxIntersectWith(self, entityPointer: Entity, intersectType: Intersect, points: _n_2_t_10, thisGraphicSystemMarker: _n_6_t_3, otherGraphicSystemMarker: _n_6_t_3):...
    def BoundingBoxIntersectWith(self, entityPointer: Entity, intersectType: Intersect, projectionPlane: _n_2_t_4, points: _n_2_t_10, thisGraphicSystemMarker: _n_6_t_3, otherGraphicSystemMarker: _n_6_t_3):...
    def BoundingBoxIntersectWith(self, entityPointer: Entity, intersectType: Intersect, points: _n_2_t_10, thisGraphicSystemMarker: int, otherGraphicSystemMarker: int):...
    def BoundingBoxIntersectWith(self, entityPointer: Entity, intersectType: Intersect, projectionPlane: _n_2_t_4, points: _n_2_t_10, thisGraphicSystemMarker: int, otherGraphicSystemMarker: int):...
    def DeleteSubentityPaths(self, subPaths: _n_6_t_10[FullSubentityPath]):...
    def Draw(self):...
    def Explode(self, entitySet: DBObjectCollection):...
    def GetGraphicsMarkersAtSubentityPathIntPtr(self, subPath: FullSubentityPath) -> _n_2_t_15:...
    def GetGripPoints(self, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: _n_2_t_3, bitFlags: GetGripPointsFlags) -> bool:...
    def GetGripPoints(self, gripPoints: _n_2_t_10, snapModes: _n_2_t_16, geometryIds: _n_2_t_16):...
    def GetGripPointsAtSubentityPath(self, subPath: FullSubentityPath, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: _n_2_t_3, bitFlags: GetGripPointsFlags) -> bool:...
    def GetObjectSnapPoints(self, snapMode: ObjectSnapModes, gsSelectionMark: int, pickPoint: _n_2_t_1, lastPoint: _n_2_t_1, viewTransform: _n_2_t_6, snapPoints: _n_2_t_10, geometryIds: _n_2_t_16, insertionMat: _n_2_t_6):...
    def GetObjectSnapPoints(self, snapMode: ObjectSnapModes, gsSelectionMark: int, pickPoint: _n_2_t_1, lastPoint: _n_2_t_1, viewTransform: _n_2_t_6, snapPoints: _n_2_t_10, geometryIds: _n_2_t_16):...
    def GetPlane(self) -> _n_2_t_4:...
    def GetStretchPoints(self, stretchPoints: _n_2_t_10):...
    def GetSubentity(self, id: FullSubentityPath) -> Entity:...
    def GetSubentityGeometricExtents(self, subPath: FullSubentityPath) -> Extents3d:...
    def GetSubentityPathsAtGraphicsMarker(self, type: SubentityType, gsMark: _n_6_t_3, pickPoint: _n_2_t_1, viewTransform: _n_2_t_6, entityAndInsertStack: _n_6_t_10[ObjectId]) -> _n_6_t_10[FullSubentityPath]:...
    def GetSubentityPathsAtGraphicsMarker(self, type: SubentityType, gsMark: int, pickPoint: _n_2_t_1, viewTransform: _n_2_t_6, numInserts: int, entityAndInsertStack: _n_6_t_10[ObjectId]) -> _n_6_t_10[FullSubentityPath]:...
    def GetTransformedCopy(self, transform: _n_2_t_6) -> Entity:...
    def Highlight(self, subId: FullSubentityPath, highlightAll: bool):...
    def Highlight(self):...
    def HighlightState(self, subId: FullSubentityPath) -> _n_3_t_8:...
    def IntersectWith(self, entityPointer: Entity, intersectType: Intersect, projectionPlane: _n_2_t_4, points: _n_2_t_10, thisGraphicSystemMarker: _n_6_t_3, otherGraphicSystemMarker: _n_6_t_3):...
    def IntersectWith(self, entityPointer: Entity, intersectType: Intersect, points: _n_2_t_10, thisGraphicSystemMarker: _n_6_t_3, otherGraphicSystemMarker: _n_6_t_3):...
    def IntersectWith(self, entityPointer: Entity, intersectType: Intersect, projectionPlane: _n_2_t_4, points: _n_2_t_10, thisGraphicSystemMarker: int, otherGraphicSystemMarker: int):...
    def IntersectWith(self, entityPointer: Entity, intersectType: Intersect, points: _n_2_t_10, thisGraphicSystemMarker: int, otherGraphicSystemMarker: int):...
    def IsContentSnappable(self) -> bool:...
    def JoinEntities(self, otherEntities: _n_6_t_10[Entity]) -> _n_2_t_16:...
    def JoinEntity(self, secondaryEntity: Entity):...
    def List(self):...
    def MoveGripPointsAt(self, grips: GripDataCollection, offset: _n_2_t_3, bitFlags: MoveGripPointsFlags):...
    def MoveGripPointsAt(self, indices: _n_2_t_16, offset: _n_2_t_3):...
    def MoveGripPointsAtSubentityPaths(self, subPaths: _n_6_t_10[FullSubentityPath], appData: _n_6_t_10[_n_6_t_3], offset: _n_2_t_3, bitFlags: MoveGripPointsFlags):...
    def MoveStretchPointsAt(self, indices: _n_2_t_16, offset: _n_2_t_3):...
    def PopHighlight(self, subId: FullSubentityPath):...
    def PushHighlight(self, subId: FullSubentityPath, highlightStyle: _n_3_t_8):...
    def RecordGraphicsModified(self, setModified: bool):...
    def SaveAs(self, mode: _n_3_t_9, st: SaveType):...
    def SetDatabaseDefaults(self, sourceDatabase: Database):...
    def SetDatabaseDefaults(self):...
    def SetDragStatus(self, status: DragStatus):...
    def SetGripStatus(self, status: GripStatus):...
    def SetLayerId(self, newValue: ObjectId, allowHidden: bool):...
    def SetPropertiesFrom(self, entityPointer: Entity):...
    def SetSubentityGripStatus(self, status: GripStatus, subentity: FullSubentityPath):...
    def TransformBy(self, transform: _n_2_t_6):...
    def TransformSubentityPathsBy(self, subPaths: _n_6_t_10[FullSubentityPath], transform: _n_2_t_6):...
    def Unhighlight(self, subId: FullSubentityPath, highlightAll: bool):...
    def Unhighlight(self):...
class EntityAlignmentEventArgs(_n_6_t_13):
    @property
    def ClosestPoint(self) -> _n_2_t_1:"""ClosestPoint { get; set; } -> Point3d"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; set; } -> Vector3d"""
    @property
    def Entity(self) -> Entity:"""Entity { get; } -> Entity"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def PickPoint(self) -> _n_2_t_1:"""PickPoint { get; } -> Point3d"""
    def __init__(self, Entity: Entity, PickPoint: _n_2_t_1, Normal: _n_2_t_3, ClosestPoint: _n_2_t_1, Direction: _n_2_t_3, Path: _n_6_t_10[FullSubentityPath]) -> EntityAlignmentEventArgs:...
    def GetPickedEntities(self) -> _n_6_t_10[FullSubentityPath]:...
class EntityAlignmentEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> EntityAlignmentEventHandler:...
    def BeginInvoke(self, sender: object, e: EntityAlignmentEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: EntityAlignmentEventArgs):...
class EntityVisualStyleType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    EdgeVisualStyle: int
    FaceVisualStyle: int
    FullVisualStyle: int
    value__: int
class EnumConverter(_n_10_t_0):
    def __init__(self, type: _n_6_t_25) -> EnumConverter:...
class EqualCurvatureConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> EqualCurvatureConstraint:...
class EqualDistanceConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> EqualDistanceConstraint:...
class EqualHelpParameterConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> EqualHelpParameterConstraint:...
    def GetEqualHelpParameters(self, helpParameter1: HelpParameter, helpParameter2: HelpParameter):...
class EqualLengthConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> EqualLengthConstraint:...
class EqualRadiusConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> EqualRadiusConstraint:...
class EraseFlags(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AllEmptyObj: int
    EmptyText: int
    value__: int
    ZeroLengthCurve: int
class ExplicitConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    @property
    def DimDependencyId(self) -> ObjectId:"""DimDependencyId { get; set; } -> ObjectId"""
    @property
    def MeasuredValue(self) -> float:"""MeasuredValue { get; } -> float"""
    @property
    def ValueDependencyId(self) -> ObjectId:"""ValueDependencyId { get; } -> ObjectId"""
class Extents2d(_n_6_t_12, _n_6_t_8):
    @property
    def MaxPoint(self) -> _n_2_t_0:"""MaxPoint { get; } -> Point2d"""
    @property
    def MinPoint(self) -> _n_2_t_0:"""MinPoint { get; } -> Point2d"""
    def __init__(self, minimum: _n_2_t_0, maximum: _n_2_t_0) -> Extents2d:...
    def __init__(self, minX: float, minY: float, maxX: float, maxY: float) -> Extents2d:...
    def IsEqualTo(self, a: Extents2d) -> bool:...
    def IsEqualTo(self, a: Extents2d, tolerance: _n_2_t_5) -> bool:...
class Extents3d(_n_6_t_12, _n_6_t_8):
    @property
    def MaxPoint(self) -> _n_2_t_1:"""MaxPoint { get; } -> Point3d"""
    @property
    def MinPoint(self) -> _n_2_t_1:"""MinPoint { get; } -> Point3d"""
    def __init__(self, min: _n_2_t_1, max: _n_2_t_1) -> Extents3d:...
    def __init__(self) -> Extents3d:...
    def AddBlockExtents(self, pointerToBlockTableRecord: BlockTableRecord):...
    def AddExtents(self, source: Extents3d):...
    def AddPoint(self, pt: _n_2_t_1):...
    def ExpandBy(self, vector: _n_2_t_3):...
    def IsEqualTo(self, a: Extents3d) -> bool:...
    def IsEqualTo(self, a: Extents3d, tolerance: _n_2_t_5) -> bool:...
    def Set(self, min: _n_2_t_1, max: _n_2_t_1):...
    def TransformBy(self, mat: _n_2_t_6):...
class ExtrudedSurface(Surface, _n_6_t_0, _n_6_t_1):
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def SweepEntity(self) -> Entity:"""SweepEntity { get; } -> Entity"""
    @property
    def SweepOptions(self) -> SweepOptions:"""SweepOptions { get; set; } -> SweepOptions"""
    @property
    def SweepProfile(self) -> Profile3d:"""SweepProfile { get; } -> Profile3d"""
    @property
    def SweepVec(self) -> _n_2_t_3:"""SweepVec { get; set; } -> Vector3d"""
    @property
    def TaperAngle(self) -> float:"""TaperAngle { get; set; } -> float"""
    def __init__(self) -> ExtrudedSurface:...
    def SetExtrude(self, sweepVec: _n_2_t_3, sweepOptions: SweepOptions):...
class Face(Entity, _n_6_t_0, _n_6_t_1):
    def __init__(self, pointer1: _n_2_t_1, pointer2: _n_2_t_1, pointer3: _n_2_t_1, value1: bool, value2: bool, value3: bool, value4: bool) -> Face:...
    def __init__(self, pointer1: _n_2_t_1, pointer2: _n_2_t_1, pointer3: _n_2_t_1, pointer4: _n_2_t_1, value1: bool, value2: bool, value3: bool, value4: bool) -> Face:...
    def __init__(self) -> Face:...
    def GetVertexAt(self, value: int) -> _n_2_t_1:...
    def IsEdgeVisibleAt(self, vertexIndex: int) -> bool:...
    def MakeEdgeInvisibleAt(self, vertexIndex: int):...
    def MakeEdgeVisibleAt(self, vertexIndex: int):...
    def SetVertexAt(self, vertexIndex: int, vertexPosition: _n_2_t_1):...
class FaceRecord(Vertex, _n_6_t_0, _n_6_t_1):
    def __init__(self, vertex0: int, vertex1: int, vertex2: int, vertex3: int) -> FaceRecord:...
    def __init__(self) -> FaceRecord:...
    def GetVertexAt(self, faceIndex: int) -> int:...
    def IsEdgeVisibleAt(self, faceIndex: int) -> bool:...
    def MakeEdgeInvisibleAt(self, faceIndex: int):...
    def MakeEdgeVisibleAt(self, faceIndex: int):...
    def SetVertexAt(self, faceIndex: int, vertexIndex: int):...
class FaceRef(SubentRef, _n_6_t_0, _n_6_t_1):
    def __init__(self, compoundObjectId: CompoundObjectId, subentId: SubentityId) -> FaceRef:...
    def __init__(self, compoundObjectId: CompoundObjectId) -> FaceRef:...
    def __init__(self) -> FaceRef:...
class FeatureControlFrame(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Dimclrd(self) -> _n_0_t_0:"""Dimclrd { get; set; } -> Color"""
    @property
    def Dimclrt(self) -> _n_0_t_0:"""Dimclrt { get; set; } -> Color"""
    @property
    def DimensionStyle(self) -> ObjectId:"""DimensionStyle { get; set; } -> ObjectId"""
    @property
    def DimensionStyleName(self) -> str:"""DimensionStyleName { get; set; } -> str"""
    @property
    def Dimgap(self) -> float:"""Dimgap { get; set; } -> float"""
    @property
    def Dimscale(self) -> float:"""Dimscale { get; set; } -> float"""
    @property
    def Dimtxsty(self) -> ObjectId:"""Dimtxsty { get; set; } -> ObjectId"""
    @property
    def Dimtxt(self) -> float:"""Dimtxt { get; set; } -> float"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; } -> Vector3d"""
    @property
    def Location(self) -> _n_2_t_1:"""Location { get; set; } -> Point3d"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    @property
    def TextStyleName(self) -> str:"""TextStyleName { get; set; } -> str"""
    def __init__(self, codes: str, insertionPoint: _n_2_t_1, normalVector: _n_2_t_3, x: _n_2_t_3) -> FeatureControlFrame:...
    def __init__(self) -> FeatureControlFrame:...
    def GetBoundingPoints(self) -> _n_2_t_10:...
    def GetBoundingPolyline(self) -> _n_2_t_10:...
    def GetDimstyleData(self) -> DimStyleTableRecord:...
    def SetDimstyleData(self, style: DimStyleTableRecord):...
    def SetOrientation(self, norm: _n_2_t_3, dir: _n_2_t_3):...
class Field(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def DataType(self) -> DataType:"""DataType { get; } -> DataType"""
    @property
    def EvaluationOption(self) -> FieldEvaluationOptions:"""EvaluationOption { get; set; } -> FieldEvaluationOptions"""
    @property
    def EvaluationStatus(self) -> FieldEvaluationStatusResult:"""EvaluationStatus { get; } -> FieldEvaluationStatusResult"""
    @property
    def EvaluatorId(self) -> str:"""EvaluatorId { get; set; } -> str"""
    @property
    def FilingOption(self) -> FieldFilingOptions:"""FilingOption { get; set; } -> FieldFilingOptions"""
    @property
    def Format(self) -> str:"""Format { get; set; } -> str"""
    @property
    def HyperLink(self) -> HyperLink:"""HyperLink { get; set; } -> HyperLink"""
    @property
    def IsTextField(self) -> bool:"""IsTextField { get; } -> bool"""
    @property
    def State(self) -> FieldState:"""State { get; } -> FieldState"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
    def __init__(self, fieldCode: str, textField: bool) -> Field:...
    def __init__(self, fieldCode: str) -> Field:...
    def __init__(self) -> Field:...
    def ConvertToTextField(self):...
    def Evaluate(self):...
    def Evaluate(self, evaluationOptions: int, database: Database):...
    @staticmethod
    def FindField(text: str, iSearchFrom: int, nStartPos: int, nEndPos: int) -> bool:...
    def GetChildren(self) -> _n_6_t_10[Field]:...
    def GetChildrenIds(self) -> _n_6_t_10[ObjectId]:...
    def GetData(self, key: str) -> object:...
    def GetFieldCode(self, flags: FieldCodeFlags) -> str:...
    def GetFieldCode(self) -> str:...
    def GetFieldCodeWithChildren(self, flags: FieldCodeFlags) -> FieldCodeWithChildren:...
    def GetFieldCodeWithChildren(self) -> FieldCodeWithChildren:...
    def GetStringValue(self) -> str:...
    def SetData(self, key: str, data: object, recursive: bool):...
    def SetData(self, key: str, data: object):...
    def SetFieldCode(self, fieldCode: str):...
    def SetFieldCodeWithChildren(self, flag: FieldCodeFlags, fieldCode: FieldCodeWithChildren):...
    def SetFieldCodeWithChildren(self, fieldCode: FieldCodeWithChildren):...
class FieldCodeFlags(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AddMarkers: int
    EscapeBackslash: int
    EvaluatedChildren: int
    EvaluatedText: int
    FieldCode: int
    ObjectReference: int
    PreserveFields: int
    StripOptions: int
    TextField: int
    value__: int
class FieldCodeWithChildren(_n_6_t_0):
    @property
    def Children(self) -> _n_6_t_10[Field]:"""Children { get; } -> Array"""
    @property
    def FieldCode(self) -> str:"""FieldCode { get; set; } -> str"""
    def Add(self, i: int, field: Field):...
class FieldEvaluationContext(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Demand: int
    Etransmit: int
    Open: int
    Plot: int
    Preview: int
    Regen: int
    Save: int
    value__: int
class FieldEvaluationOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Automatic: int
    Disable: int
    OnDemand: int
    OnEtransmit: int
    OnOpen: int
    OnPlot: int
    OnRegen: int
    OnSave: int
    value__: int
class FieldEvaluationResult(_n_6_t_12):
    @property
    def Evaluated(self) -> int:"""Evaluated { get; } -> int"""
    @property
    def Found(self) -> int:"""Found { get; } -> int"""
class FieldEvaluationStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    EvaluatorNotFound: int
    InvalidCode: int
    InvalidContext: int
    NotYetEvaluated: int
    OtherError: int
    Success: int
    SyntaxError: int
    value__: int
class FieldEvaluationStatusResult(_n_6_t_12):
    @property
    def ErrorCode(self) -> int:"""ErrorCode { get; } -> int"""
    @property
    def ErrorMessage(self) -> str:"""ErrorMessage { get; } -> str"""
    @property
    def Status(self) -> FieldEvaluationStatus:"""Status { get; } -> FieldEvaluationStatus"""
    def __init__(self, s: FieldEvaluationStatus, e: int, m: str) -> FieldEvaluationStatusResult:...
class FieldFilingOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    SkipFilingResult: int
    value__: int
class FieldState(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Compiled: int
    Evaluated: int
    HasCache: int
    HasFormattedString: int
    Initialized: int
    Modified: int
    value__: int
class FileDependencyInfo(object):
    @property
    def Feature(self) -> str:"""Feature { get; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def FileSize(self) -> int:"""FileSize { get; } -> int"""
    @property
    def FingerprintGuid(self) -> str:"""FingerprintGuid { get; } -> str"""
    @property
    def FoundPath(self) -> str:"""FoundPath { get; } -> str"""
    @property
    def FullFileName(self) -> str:"""FullFileName { get; } -> str"""
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def IsAffectsGraphics(self) -> bool:"""IsAffectsGraphics { get; } -> bool"""
    @property
    def IsModified(self) -> bool:"""IsModified { get; } -> bool"""
    @property
    def ReferenceCount(self) -> int:"""ReferenceCount { get; } -> int"""
    @property
    def TimeStamp(self) -> int:"""TimeStamp { get; } -> int"""
    @property
    def VersionGuid(self) -> str:"""VersionGuid { get; } -> str"""
class FileDependencyManager(_n_5_t_3, _n_6_t_0):
    @property
    def CountEntries(self) -> int:"""CountEntries { get; } -> int"""
    @property
    def IteratorNext(self) -> int:"""IteratorNext { get; } -> int"""
    def CreateEntry(self, feature: str, fullFileName: str, affectsGraphics: bool, noIncrement: bool) -> int:...
    def EraseEntry(self, index: int, forceRemove: bool):...
    def EraseEntry(self, feature: str, fullFileName: str, forceRemove: bool):...
    def GetEntry(self, index: int, useCachedInfo: bool) -> FileDependencyInfo:...
    def GetEntry(self, feature: str, fullFileName: str, useCachedInfo: bool) -> FileDependencyInfo:...
    def IteratorInitialize(self, feature: str, modifiedOnly: bool, affectsGraphicsOnly: bool, walkXRefTree: bool):...
    def UpdateEntry(self, index: int):...
    def UpdateEntry(self, feature: str, fullFileName: str):...
class FileOpenMode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    OpenForReadAndAllShare: int
    OpenForReadAndReadShare: int
    OpenForReadAndWriteNoShare: int
    OpenTryForReadShare: int
    value__: int
class FilerType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BagFiler: int
    CopyFiler: int
    DeepCloneFiler: int
    FileFiler: int
    IdFiler: int
    IdTranslateFiler: int
    PageFiler: int
    PurgeFiler: int
    UndoFiler: int
    value__: int
    WblockCloneFiler: int
class FilletTrimMode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    TrimBoth: int
    TrimNone: int
    TrimSecond: int
    TrimStart: int
    value__: int
class FindFileHint(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ArxApplication: int
    CompiledShapeFile: int
    Default: int
    EmbeddedImageFile: int
    FontFile: int
    FontMapFile: int
    PatternFile: int
    TrueTypeFontFile: int
    UnderlayFile: int
    value__: int
    XRefDrawing: int
class FitData(_n_6_t_12):
    @property
    def Degree(self) -> int:"""Degree { get; set; } -> int"""
    @property
    def EndTangent(self) -> _n_2_t_3:"""EndTangent { get; set; } -> Vector3d"""
    @property
    def FitTolerance(self) -> float:"""FitTolerance { get; set; } -> float"""
    @property
    def KnotParam(self) -> _n_2_t_17:"""KnotParam { get; set; } -> KnotParameterizationEnum"""
    @property
    def Periodic(self) -> bool:"""Periodic { get; set; } -> bool"""
    @property
    def StartTangent(self) -> _n_2_t_3:"""StartTangent { get; set; } -> Vector3d"""
    @property
    def TangentsExist(self) -> bool:"""TangentsExist { get; set; } -> bool"""
    def __init__(self) -> FitData:...
    def GetFitPoints(self) -> _n_2_t_10:...
    def IsEqualTo(self, other: FitData) -> bool:...
    def IsEqualTo(self, other: FitData, tolerance: _n_2_t_5) -> bool:...
class FixedConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> FixedConstraint:...
class FlowDirection(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BottomToTop: int
    ByStyle: int
    LeftToRight: int
    NotSet: int
    RightToLeft: int
    TopToBottom: int
    value__: int
class Font(_n_6_t_12):
    @property
    def IsTrueType(self) -> bool:"""IsTrueType { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, name: str, isTrueType: bool) -> Font:...
class FormatOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ForEditing: int
    ForExpression: int
    FormatOptionNone: int
    IgnoreMtextFormat: int
    UseMaximumPrecision: int
    value__: int
class FormattedTableData(LinkedTableData, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> FormattedTableData:...
    def GetAlignment(self, row: int, column: int) -> CellAlignment:...
    def GetBackgroundColor(self, row: int, column: int) -> _n_0_t_0:...
    def GetContentColor(self, row: int, column: int) -> _n_0_t_0:...
    def GetGridColor(self, row: int, column: int, gridLinetype: GridLineType) -> _n_0_t_0:...
    def GetGridLinetype(self, row: int, column: int, gridLinetype: GridLineType) -> ObjectId:...
    def GetGridLineWeight(self, row: int, column: int, gridLinetype: GridLineType) -> LineWeight:...
    def GetGridVisibility(self, row: int, column: int, gridLinetype: GridLineType) -> Visibility:...
    def GetMargin(self, row: int, column: int, margin: CellMargins) -> float:...
    def GetMergeRange(self, row: int, column: int) -> CellRange:...
    def GetOverride(self, row: int, column: int, gridLinetype: GridLineType) -> GridProperties:...
    def GetOverride(self, row: int, column: int, content: int) -> CellProperties:...
    def GetRotation(self, row: int, column: int) -> float:...
    def GetScale(self, row: int, column: int) -> float:...
    def GetTextHeight(self, row: int, column: int) -> float:...
    def GetTextStyle(self, row: int, column: int) -> ObjectId:...
    def IsFormatEditable(self, row: int, column: int) -> bool:...
    def IsMerged(self, row: int, column: int) -> bool:...
    def Merge(self, range: CellRange):...
    def RemoveAllOverrides(self, row: int, column: int):...
    def SetAlignment(self, row: int, column: int, value: CellAlignment):...
    def SetBackgroundColor(self, row: int, column: int, value: _n_0_t_0):...
    def SetContentColor(self, row: int, column: int, value: _n_0_t_0):...
    def SetGridColor(self, row: int, column: int, gridLinetype: GridLineType, value: _n_0_t_0):...
    def SetGridLinetype(self, row: int, column: int, gridLinetype: GridLineType, value: ObjectId):...
    def SetGridLineWeight(self, row: int, column: int, gridLinetype: GridLineType, value: LineWeight):...
    def SetGridVisibility(self, row: int, column: int, gridLinetype: GridLineType, value: Visibility):...
    def SetMargin(self, row: int, column: int, margin: CellMargins, value: float):...
    def SetOverride(self, row: int, column: int, gridLinetype: GridLineType, gridProperty: GridProperties):...
    def SetOverride(self, row: int, column: int, content: int, cellProperty: CellProperties):...
    def SetRotation(self, row: int, column: int, value: float):...
    def SetScale(self, row: int, column: int, value: float):...
    def SetTextHeight(self, row: int, column: int, value: float):...
    def SetTextStyle(self, row: int, column: int, value: ObjectId):...
    def Unmerge(self, range: CellRange):...
class FrameSetting(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ImageFrameAbove: int
    ImageFrameBelow: int
    ImageFrameInvalid: int
    ImageFrameOff: int
    ImageFrameOnNoPlot: int
    value__: int
class FullDwgVersion(_n_6_t_12):
    @property
    def MajorVersion(self) -> DwgVersion:"""MajorVersion { get; } -> DwgVersion"""
    @property
    def MinorVersion(self) -> MaintenanceReleaseVersion:"""MinorVersion { get; } -> MaintenanceReleaseVersion"""
    def __init__(self, majorVersion: DwgVersion, minorVersion: MaintenanceReleaseVersion) -> FullDwgVersion:...
class FullSubentityPath(_n_6_t_12):
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def Null(self) -> FullSubentityPath:"""Null { get; } -> FullSubentityPath"""
    @property
    def SubentId(self) -> SubentityId:"""SubentId { get; } -> SubentityId"""
    def __init__(self, ids: _n_6_t_10[ObjectId], index: SubentityId) -> FullSubentityPath:...
    def CopyToUnmanagedObject(self, unmanagedPointer: _n_6_t_3):...
    def GetObjectIds(self) -> _n_6_t_10[ObjectId]:...
class G2SmoothConstraint(CompositeConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> G2SmoothConstraint:...
class GeoCoordinateCategory(_n_5_t_3, _n_6_t_0):
    @property
    def ID(self) -> str:"""ID { get; } -> str"""
    @staticmethod
    def CreateAll() -> _n_6_t_10[GeoCoordinateCategory]:...
    def GetCoordinateAt(self, index: int) -> GeoCoordinateSystem:...
    def NumOfCoordinate(self) -> int:...
class GeoCoordinateSystem(_n_5_t_3, _n_6_t_0):
    @property
    def CartesianExtents(self) -> Extents2d:"""CartesianExtents { get; } -> Extents2d"""
    @property
    def Datum(self) -> object:"""Datum { get; } -> object"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def Ellipsoid(self) -> object:"""Ellipsoid { get; } -> object"""
    @property
    def EPSGcode(self) -> int:"""EPSGcode { get; } -> int"""
    @property
    def GeodeticExtents(self) -> Extents2d:"""GeodeticExtents { get; } -> Extents2d"""
    @property
    def GeoUnit(self) -> GeoCSUnit:"""GeoUnit { get; } -> GeoCSUnit"""
    @property
    def ID(self) -> str:"""ID { get; } -> str"""
    @property
    def Offset(self) -> _n_2_t_14:"""Offset { get; } -> Vector2d"""
    @property
    def ProjectionCode(self) -> GeoCSProjectionCode:"""ProjectionCode { get; } -> GeoCSProjectionCode"""
    @property
    def Type(self) -> GeoCSType:"""Type { get; } -> GeoCSType"""
    @property
    def Unit(self) -> UnitsValue:"""Unit { get; } -> UnitsValue"""
    @property
    def UnitScale(self) -> float:"""UnitScale { get; } -> float"""
    @property
    def WktRepresentation(self) -> str:"""WktRepresentation { get; } -> str"""
    @property
    def XmlRepresentation(self) -> str:"""XmlRepresentation { get; } -> str"""
    @staticmethod
    def CreateAll(coordCategory: GeoCoordinateCategory) -> _n_6_t_10[GeoCoordinateSystem]:...
    @staticmethod
    def CreateAll(geoPt: _n_6_t_12) -> _n_6_t_10[GeoCoordinateSystem]:...
    @staticmethod
    def CreateAll() -> _n_6_t_10[GeoCoordinateSystem]:...
    def GetProjectionParamList(self, includeSpecialParams: bool) -> object:...
class GeoCoordinateTransformer(_n_5_t_3, _n_6_t_0):
    @property
    def SourceCSid(self) -> str:"""SourceCSid { get; } -> str"""
    @property
    def TargetCSid(self) -> str:"""TargetCSid { get; } -> str"""
    @staticmethod
    def TransformPoint(source: str, target: str, sourcePt: _n_2_t_1) -> _n_2_t_1:...
    def TransformPoint(self, sourcePt: _n_2_t_1) -> _n_2_t_1:...
    @staticmethod
    def TransformPoints(source: str, target: str, sourcePts: _n_2_t_10) -> _n_2_t_10:...
    def TransformPoints(self, sourcePts: _n_2_t_10) -> _n_2_t_10:...
class GeoCSProjectionCode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Alber: int
    Azede: int
    Azmea: int
    Azmed: int
    Bipolar: int
    Bonne: int
    Cassini: int
    Eckert4: int
    Eckert6: int
    Edcnc: int
    Edcyl: int
    EdcylE: int
    GaussK: int
    Gnomonic: int
    Goode: int
    Hom1uv: int
    Hom1xy: int
    Hom2uv: int
    Hom2xy: int
    Krovak: int
    Krvk95: int
    LL: int
    Lm1sp: int
    Lm2sp: int
    Lmblg: int
    Lmbrtaf: int
    Lmtan: int
    Miller: int
    Mndotl: int
    Mndott: int
    Modpc: int
    Mollweid: int
    Mrcat: int
    MrcatK: int
    Mstero: int
    Neacyl: int
    Nerth: int
    Nrthsrt: int
    Nzealand: int
    OblqM: int
    Obqcyl: int
    Ortho: int
    Ostn02: int
    Ostn97: int
    Ostro: int
    PlateCarree: int
    Plycn: int
    Pstro: int
    Pstrosl: int
    PvMercator: int
    Robinson: int
    Rskew: int
    Rskewc: int
    Rskewo: int
    Sinus: int
    Sotrm: int
    Sstro: int
    Swiss: int
    Sys34: int
    Sys34_01: int
    Sys34_99: int
    Teacyl: int
    Tm: int
    Trmeraf: int
    Trmrkrg: int
    Trmrs: int
    Unknown: int
    Utm: int
    value__: int
    Vdgrntn: int
    Wccsl: int
    Wccst: int
    Winkl: int
class GeoCSType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Arbitrary: int
    Geographic: int
    Projected: int
    Unknown: int
    value__: int
class GeoCSUnit(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BenoitChain: int
    BenoitLink: int
    Brealey: int
    CaGrid: int
    CapeRood: int
    Centimeter: int
    Centisec: int
    ClarkeChain: int
    ClarkeFoot: int
    ClarkeLink: int
    Decameter: int
    Decimeter: int
    Decisec: int
    Degree: int
    Dekameter: int
    Foot: int
    Furlong: int
    GermanMeter: int
    GoldCoastFoot: int
    Grad: int
    Grade: int
    GunterChain: int
    GunterLink: int
    Hectometer: int
    IFoot: int
    IInch: int
    IMile: int
    Inch: int
    IndianFoot: int
    IndianFt37: int
    IndianFt62: int
    IndianFt75: int
    IndianYard: int
    IndianYd37: int
    InternationalChain: int
    InternationalLink: int
    IYard: int
    Kilometer: int
    Knot: int
    Lat66: int
    Lat83: int
    MapInfo: int
    Meter: int
    MicroInch: int
    Mil: int
    Mile: int
    Millimeter: int
    Millisec: int
    Minute: int
    NautM: int
    Perch: int
    Pole: int
    Radian: int
    Rod: int
    Rood: int
    SearsChain: int
    SearsFoot: int
    SearsLink: int
    SearsYard: int
    Second: int
    Unknown: int
    value__: int
    Yard: int
class GeoLocationData(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def BlockTableRecordId(self) -> ObjectId:"""BlockTableRecordId { get; set; } -> ObjectId"""
    @property
    def CoordinateProjectionRadius(self) -> float:"""CoordinateProjectionRadius { get; set; } -> float"""
    @property
    def CoordinateSystem(self) -> str:"""CoordinateSystem { get; set; } -> str"""
    @property
    def DesignPoint(self) -> _n_2_t_1:"""DesignPoint { get; set; } -> Point3d"""
    @property
    def DoSeaLevelCorrection(self) -> bool:"""DoSeaLevelCorrection { get; set; } -> bool"""
    @property
    def GeoRSSTag(self) -> str:"""GeoRSSTag { get; set; } -> str"""
    @property
    def HorizontalUnits(self) -> UnitsValue:"""HorizontalUnits { get; set; } -> UnitsValue"""
    @property
    def HorizontalUnitsScale(self) -> float:"""HorizontalUnitsScale { get; set; } -> float"""
    @property
    def NorthDirection(self) -> float:"""NorthDirection { get; } -> float"""
    @property
    def NorthDirectionVector(self) -> _n_2_t_14:"""NorthDirectionVector { get; set; } -> Vector2d"""
    @property
    def NumMeshPoints(self) -> int:"""NumMeshPoints { get; } -> int"""
    @property
    def ReferencePoint(self) -> _n_2_t_1:"""ReferencePoint { get; set; } -> Point3d"""
    @property
    def ScaleEstimationMethod(self) -> ScaleEstimationMethod:"""ScaleEstimationMethod { get; set; } -> ScaleEstimationMethod"""
    @property
    def ScaleFactor(self) -> float:"""ScaleFactor { get; set; } -> float"""
    @property
    def SeaLevelElevation(self) -> float:"""SeaLevelElevation { get; set; } -> float"""
    @property
    def TypeOfCoordinates(self) -> TypeOfCoordinates:"""TypeOfCoordinates { get; set; } -> TypeOfCoordinates"""
    @property
    def UpDirection(self) -> _n_2_t_3:"""UpDirection { get; set; } -> Vector3d"""
    @property
    def VerticalUnits(self) -> UnitsValue:"""VerticalUnits { get; set; } -> UnitsValue"""
    @property
    def VerticalUnitsScale(self) -> float:"""VerticalUnitsScale { get; set; } -> float"""
    def __init__(self) -> GeoLocationData:...
    def AddMeshPointMap(self, index: int, sourcePt: _n_2_t_0, destPt: _n_2_t_0):...
    def EraseFromDb(self):...
    def GetMeshPointMap(self, index: int) -> MeshPointMap:...
    def GetMeshPointMaps(self) -> MeshPointMaps:...
    def PostToDb(self) -> ObjectId:...
    def ResetMeshPointMaps(self):...
    def SetMeshPointMaps(self, sourcePts: _n_2_t_18, destPts: _n_2_t_18):...
    def TransformFromLonLatAlt(self, geoPt: _n_2_t_1) -> _n_2_t_1:...
    def TransformToLonLatAlt(self, x: float, y: float, z: float) -> _n_2_t_19:...
    def TransformToLonLatAlt(self, dwgPt: _n_2_t_1) -> _n_2_t_1:...
    def UpdateTransformationMatrix(self):...
class GeomapImage(RasterImage, _n_6_t_0, _n_6_t_1):
    @property
    def BottomLeftPoint(self) -> _n_2_t_1:"""BottomLeftPoint { get; } -> Point3d"""
    @property
    def ImageBottomLeftPoint(self) -> _n_2_t_1:"""ImageBottomLeftPoint { get; } -> Point3d"""
    @property
    def IsOutOfDate(self) -> bool:"""IsOutOfDate { get; } -> bool"""
    @property
    def LOD(self) -> _n_6_t_11:"""LOD { get; } -> UInt32"""
    @property
    def MapType(self) -> object:"""MapType { get; set; } -> object"""
    @property
    def Resolution(self) -> object:"""Resolution { get; set; } -> object"""
    def __init__(self) -> GeomapImage:...
    def GetImageVertices(self) -> _n_2_t_10:...
    def UpdateMapImage(self, Reset: bool) -> bool:...
class GeometricalConstraint(ConstraintGroupNode, _n_6_t_0, _n_6_t_1):
    @property
    def ConnectedGeometries(self) -> _n_6_t_10[ConstrainedGeometry]:"""ConnectedGeometries { get; } -> Array"""
    @property
    def ConnectedHelpParameters(self) -> _n_6_t_10[HelpParameter]:"""ConnectedHelpParameters { get; } -> Array"""
    @property
    def IsActive(self) -> bool:"""IsActive { get; } -> bool"""
    @property
    def IsEnabled(self) -> bool:"""IsEnabled { get; } -> bool"""
    @property
    def IsImplied(self) -> bool:"""IsImplied { get; } -> bool"""
    @property
    def IsInternal(self) -> bool:"""IsInternal { get; } -> bool"""
    @property
    def OwningCompositeConstraint(self) -> CompositeConstraint:"""OwningCompositeConstraint { get; } -> CompositeConstraint"""
    def Deactivate(self):...
    def GetConnectedHelpParameterFor(self, consGeom: ConstrainedGeometry) -> HelpParameter:...
    def Reactivate(self):...
    class ConstraintType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Coincident: int
        Collinear: int
        Concentric: int
        EqualLength: int
        EqualRadius: int
        Fix: int
        Horizontal: int
        Normal: int
        Parallel: int
        Perpendicular: int
        Smooth: int
        Symmetric: int
        Tangent: int
        value__: int
        Vertical: int
class GeometryOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def GetGeomExtents(self, entity: Entity) -> Extents3d:...
    def IntersectWith(self, entity: Entity, ent: Entity, intType: Intersect, projPlane: _n_2_t_4, points: _n_2_t_10, thisGsMarker: _n_6_t_3, otherGsMarker: _n_6_t_3):...
    def IntersectWith(self, entity: Entity, ent: Entity, intType: Intersect, points: _n_2_t_10, thisGsMarker: _n_6_t_3, otherGsMarker: _n_6_t_3):...
class GeomRef(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def IsEmpty(self) -> bool:"""IsEmpty { get; } -> bool"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    def Reset(self):...
class GeoPositionMarker(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def EnableFrameText(self) -> bool:"""EnableFrameText { get; set; } -> bool"""
    @property
    def GeoPosition(self) -> _n_2_t_1:"""GeoPosition { get; set; } -> Point3d"""
    @property
    def LandingGap(self) -> float:"""LandingGap { get; set; } -> float"""
    @property
    def MText(self) -> MText:"""MText { get; set; } -> MText"""
    @property
    def MTextVisible(self) -> bool:"""MTextVisible { get; set; } -> bool"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def Notes(self) -> str:"""Notes { get; set; } -> str"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Radius(self) -> float:"""Radius { get; set; } -> float"""
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    @property
    def TextAlignmentType(self) -> TextAlignment:"""TextAlignmentType { get; set; } -> TextAlignment"""
    @property
    def TextStyle(self) -> ObjectId:"""TextStyle { get; } -> ObjectId"""
    def __init__(self, pos: _n_2_t_1, radius: float, landingGap: float) -> GeoPositionMarker:...
    def __init__(self) -> GeoPositionMarker:...
class GetGripPointsFlags(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CyclableGripsOnly: int
    DynamicDimensionMode: int
    GripPointsOnly: int
    value__: int
class GradientBackground(Background, _n_6_t_0, _n_6_t_1):
    @property
    def ColorBottom(self) -> _n_0_t_2:"""ColorBottom { get; set; } -> EntityColor"""
    @property
    def ColorMiddle(self) -> _n_0_t_2:"""ColorMiddle { get; set; } -> EntityColor"""
    @property
    def ColorTop(self) -> _n_0_t_2:"""ColorTop { get; set; } -> EntityColor"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def Horizon(self) -> float:"""Horizon { get; set; } -> float"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    def __init__(self) -> GradientBackground:...
class GradientColor(_n_6_t_12):
    def __init__(self, color: _n_0_t_0, value: float) -> GradientColor:...
    def get_Color(self) -> _n_0_t_0:...
    def get_Value(self) -> float:...
class GradientPatternType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    PreDefinedGradient: int
    UserDefinedGradient: int
    value__: int
class Graph(_n_5_t_3, _n_6_t_0):
    @property
    def IsEmpty(self) -> bool:"""IsEmpty { get; } -> bool"""
    @property
    def NumNodes(self) -> int:"""NumNodes { get; } -> int"""
    @property
    def RootNode(self) -> GraphNode:"""RootNode { get; } -> GraphNode"""
    def __init__(self, root: GraphNode) -> Graph:...
    def AddEdge(self, _from: GraphNode, toPointer: GraphNode):...
    def AddNode(self, nodeToAdd: GraphNode):...
    def BreakCycleEdge(self, _from: GraphNode, toPointer: GraphNode):...
    def ClearAll(self, flags: _n_6_t_19):...
    def DelNode(self, nodeToDelete: GraphNode):...
    def FindCycles(self, start: GraphNode) -> bool:...
    def GetOutgoing(self) -> GraphNodeCollection:...
    def Node(self, index: int) -> GraphNode:...
    def Reset(self):...
    def SetNodeGrowthRate(self, rate: int):...
class GraphicsMetafileType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BoundingBox: int
    FullGraphics: int
    NoMetafile: int
    value__: int
class GraphNode(_n_5_t_3, _n_6_t_0):
    @property
    def Data(self) -> _n_6_t_3:"""Data { get; set; } -> IntPtr"""
    @property
    def IsCycleNode(self) -> bool:"""IsCycleNode { get; } -> bool"""
    @property
    def NextCycleNode(self) -> GraphNode:"""NextCycleNode { get; } -> GraphNode"""
    @property
    def NumCycleIn(self) -> int:"""NumCycleIn { get; } -> int"""
    @property
    def NumCycleOut(self) -> int:"""NumCycleOut { get; } -> int"""
    @property
    def NumIn(self) -> int:"""NumIn { get; } -> int"""
    @property
    def NumOut(self) -> int:"""NumOut { get; } -> int"""
    @property
    def Owner(self) -> Graph:"""Owner { get; } -> Graph"""
    def __init__(self) -> GraphNode:...
    def AddRefTo(self, outGoingNode: GraphNode):...
    def Clear(self, flags: _n_6_t_19):...
    def CycleIn(self, index: int) -> GraphNode:...
    def CycleOut(self, index: int) -> GraphNode:...
    def DisconnectAll(self):...
    def In(self, index: int) -> GraphNode:...
    def IsMarkedAs(self, flag: int) -> bool:...
    def MarkAs(self, flags: _n_6_t_19):...
    def MarkTree(self, flags: _n_6_t_19, appendedTo: GraphNodeCollection):...
    def Out(self, index: int) -> GraphNode:...
    def RemoveRefTo(self, nodeToRemoveReference: GraphNode):...
    def SetEdgeGrowthRate(self, outEdgeRate: int, inEdgeRate: int):...
class GraphNodeCollection(_n_5_t_3, _n_6_t_0, _n_7_t_5, typing.Iterable[typing.Any]):
    def __init__(self) -> GraphNodeCollection:...
class GridLineStyle(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Double: int
    Single: int
    value__: int
class GridLineType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AllGridLines: int
    HorizontalBottom: int
    HorizontalGridLines: int
    HorizontalInside: int
    HorizontalTop: int
    InnerGridLines: int
    InvalidGridLine: int
    OuterGridLines: int
    value__: int
    VerticalGridLines: int
    VerticalInside: int
    VerticalLeft: int
    VerticalRight: int
class GridProperties(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Color: int
    DoubleLineSpacing: int
    Invalid: int
    LineStyle: int
    Linetype: int
    LineWeight: int
    value__: int
    Visibility: int
class GridPropertyParameter(_n_6_t_12):
    Color: int
    DoubleLineSpacing: int
    LineStyle: int
    Linetype: int
    LineWeight: int
    PropertyMask: int
    Visibility: int
class GripData(_n_5_t_3, _n_6_t_0):
    @property
    def AlternateBasePoint(self) -> _n_6_t_14[_n_2_t_1]:"""AlternateBasePoint { get; set; } -> Nullable"""
    @property
    def DrawAtDragImageGripPoint(self) -> bool:"""DrawAtDragImageGripPoint { get; set; } -> bool"""
    @property
    def ForcedPickOn(self) -> bool:"""ForcedPickOn { get; set; } -> bool"""
    @property
    def GizmosEnabled(self) -> bool:"""GizmosEnabled { get; set; } -> bool"""
    @property
    def GripPoint(self) -> _n_2_t_1:"""GripPoint { get; set; } -> Point3d"""
    @property
    def HotGripInvokesRightClick(self) -> bool:"""HotGripInvokesRightClick { get; set; } -> bool"""
    @property
    def IsPerViewport(self) -> bool:"""IsPerViewport { get; set; } -> bool"""
    @property
    def ModeKeywordsDisabled(self) -> bool:"""ModeKeywordsDisabled { get; set; } -> bool"""
    @property
    def RubberBandLineDisabled(self) -> bool:"""RubberBandLineDisabled { get; set; } -> bool"""
    @property
    def SkipWhenShared(self) -> bool:"""SkipWhenShared { get; set; } -> bool"""
    @property
    def TriggerGrip(self) -> bool:"""TriggerGrip { get; set; } -> bool"""
    def GetHotGripDimensionData(self, id: ObjectId, dimScale: float) -> DynamicDimensionDataCollection:...
    def GetHoverDimensionData(self, id: ObjectId, dimScale: float) -> DynamicDimensionDataCollection:...
    def GetTooltip(self) -> str:...
    def OnGripStatusChanged(self, entityId: ObjectId, newStatus: GripData.Status):...
    def OnHotGrip(self, entityId: ObjectId, contextFlags: GripData.Context) -> GripData.ReturnValue:...
    def OnHover(self, entityId: ObjectId, contextFlags: GripData.Context) -> GripData.ReturnValue:...
    def OnRightClick(self, hotGrips: GripDataCollection, entities: ObjectIdCollection) -> _n_8_t_0[_n_5_t_6]:...
    def ViewportDraw(self, worldDraw: _n_3_t_10, entityId: ObjectId, type: GripData.DrawType, imageGripPoint: _n_6_t_14[_n_2_t_1], gripSizeInPixels: int) -> bool:...
    def WorldDraw(self, worldDraw: _n_3_t_9, entityId: ObjectId, type: GripData.DrawType, imageGripPoint: _n_6_t_14[_n_2_t_1], dGripSize: float) -> bool:...
    class Context(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        MultiHotGrip: int
        SharedGrip: int
        value__: int
    class DrawType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        DragImageGrip: int
        HotGrip: int
        HoverGrip: int
        value__: int
        WarmGrip: int
    class ReturnValue(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Failure: int
        GetNewGripPoints: int
        GripHotToWarm: int
        NoRedrawGrip: int
        Ok: int
        value__: int
    class Status(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        DimFocusChanged: int
        GripAbort: int
        GripEnd: int
        GripStart: int
        Mirror: int
        Move: int
        PopUpMenu: int
        Rotate: int
        Scale: int
        Stretch: int
        value__: int
class GripDataCollection(_n_5_t_3, _n_6_t_0, _n_8_t_2[GripData], typing.Iterable[typing.Any]):
    @property
    def Item(self) -> GripData:"""Item { get; } -> GripData"""
    def __init__(self) -> GripDataCollection:...
class GripMode(_n_5_t_3, _n_6_t_0):
    @property
    def Action(self) -> GripMode.ActionType:"""Action { get; set; } -> GripMode.ActionType"""
    @property
    def CLIDisplayString(self) -> str:"""CLIDisplayString { get; set; } -> str"""
    @property
    def CLIKeywordList(self) -> str:"""CLIKeywordList { get; set; } -> str"""
    @property
    def CLIPromptString(self) -> str:"""CLIPromptString { get; set; } -> str"""
    @property
    def CommandString(self) -> str:"""CommandString { get; set; } -> str"""
    @property
    def Cursor(self) -> GripMode.CursorType:"""Cursor { get; set; } -> GripMode.CursorType"""
    @property
    def DisplayString(self) -> str:"""DisplayString { get; set; } -> str"""
    @property
    def ModeId(self) -> _n_6_t_11:"""ModeId { get; set; } -> UInt32"""
    @property
    def ToolTip(self) -> str:"""ToolTip { get; set; } -> str"""
    def __init__(self) -> GripMode:...
    class ActionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Command: int
        DragOn: int
        Immediate: int
        value__: int
    class CursorType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        CursorCrosshairAngle: int
        CursorCrosshairCurve: int
        CursorCrosshairLine: int
        CursorCrosshairMinus: int
        CursorCrosshairPlus: int
        CursorNone: int
        value__: int
    class ModeIdentifier(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        CustomStart: int
        Move: int
        _None: int
        value__: int
class GripModeCollection(_n_5_t_3, _n_6_t_0, _n_8_t_2[GripMode], typing.Iterable[typing.Any]):
    @property
    def Item(self) -> GripMode:"""Item { get; } -> GripMode"""
    def __init__(self) -> GripModeCollection:...
class GripOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def GetGripPoints(self, entity: Entity, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: _n_2_t_3, bitFlags: GetGripPointsFlags):...
    def GetGripPoints(self, entity: Entity, gripPoints: _n_2_t_10, snapModes: _n_2_t_16, geometryIds: _n_2_t_16):...
    def GetStretchPoints(self, entity: Entity, stretchPoints: _n_2_t_10):...
    def MoveGripPointsAt(self, entity: Entity, grips: GripDataCollection, offset: _n_2_t_3, bitFlags: MoveGripPointsFlags):...
    def MoveGripPointsAt(self, entity: Entity, indices: _n_2_t_16, offset: _n_2_t_3):...
    def MoveStretchPointsAt(self, entity: Entity, indices: _n_2_t_16, offset: _n_2_t_3):...
    def OnGripStatusChanged(self, entity: Entity, status: GripStatus):...
class GripStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DimDataToBeDeleted: int
    GripsDone: int
    GripsToBeDeleted: int
    value__: int
class GroundPlaneBackground(Background, _n_6_t_0, _n_6_t_1):
    @property
    def ColorGroundPlaneFar(self) -> _n_0_t_2:"""ColorGroundPlaneFar { get; set; } -> EntityColor"""
    @property
    def ColorGroundPlaneNear(self) -> _n_0_t_2:"""ColorGroundPlaneNear { get; set; } -> EntityColor"""
    @property
    def ColorSkyHorizon(self) -> _n_0_t_2:"""ColorSkyHorizon { get; set; } -> EntityColor"""
    @property
    def ColorSkyZenith(self) -> _n_0_t_2:"""ColorSkyZenith { get; set; } -> EntityColor"""
    @property
    def ColorUndergroundAzimuth(self) -> _n_0_t_2:"""ColorUndergroundAzimuth { get; set; } -> EntityColor"""
    @property
    def ColorUndergroundHorizon(self) -> _n_0_t_2:"""ColorUndergroundHorizon { get; set; } -> EntityColor"""
    def __init__(self) -> GroundPlaneBackground:...
class Group(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def IsAnonymous(self) -> bool:"""IsAnonymous { get; } -> bool"""
    @property
    def IsNotAccessible(self) -> bool:"""IsNotAccessible { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NumEntities(self) -> int:"""NumEntities { get; } -> int"""
    @property
    def Selectable(self) -> bool:"""Selectable { get; set; } -> bool"""
    def __init__(self, description: str, selectable: bool) -> Group:...
    def __init__(self) -> Group:...
    def Append(self, ids: ObjectIdCollection):...
    def Append(self, id: ObjectId):...
    def Clear(self):...
    def GetAllEntityIds(self) -> _n_6_t_10[ObjectId]:...
    def GetIndex(self, id: ObjectId) -> int:...
    def Has(self, entity: Entity) -> bool:...
    def InsertAt(self, index: int, ids: ObjectIdCollection):...
    def InsertAt(self, index: int, id: ObjectId):...
    def Prepend(self, ids: ObjectIdCollection):...
    def Prepend(self, id: ObjectId):...
    def Remove(self, ids: ObjectIdCollection):...
    def Remove(self, id: ObjectId):...
    def RemoveAt(self, index: int, ids: ObjectIdCollection):...
    def RemoveAt(self, index: int):...
    def Replace(self, oldId: ObjectId, newId: ObjectId):...
    def Reverse(self):...
    def SetAnonymous(self):...
    def SetColor(self, color: _n_0_t_0):...
    def SetColorIndex(self, color: int):...
    def SetHighlight(self, value: bool):...
    def SetLayer(self, value: ObjectId):...
    def SetLayer(self, value: str):...
    def SetLinetype(self, value: ObjectId):...
    def SetLinetype(self, value: str):...
    def SetLinetypeScale(self, value: float):...
    def SetVisibility(self, value: bool):...
    def Transfer(self, fromIndex: int, toIndex: int, numItems: int):...
class GsMarkType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ArrowMark: int
    BlockMark: int
    DoglegMark: int
    LeaderLineMark: int
    MTextMark: int
    MTextUnderLineMark: int
    _None: int
    ToleranceMark: int
    value__: int
class Handle(_n_6_t_12):
    @property
    def IsOne(self) -> bool:"""IsOne { get; } -> bool"""
    @property
    def Value(self) -> int:"""Value { get; } -> int"""
    def __init__(self, value: int) -> Handle:...
class Hatch(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Area(self) -> float:"""Area { get; } -> float"""
    @property
    def Associative(self) -> bool:"""Associative { get; set; } -> bool"""
    @property
    def BackgroundColor(self) -> _n_0_t_0:"""BackgroundColor { get; set; } -> Color"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def GradientAngle(self) -> float:"""GradientAngle { get; set; } -> float"""
    @property
    def GradientName(self) -> str:"""GradientName { get; } -> str"""
    @property
    def GradientOneColorMode(self) -> bool:"""GradientOneColorMode { get; set; } -> bool"""
    @property
    def GradientShift(self) -> float:"""GradientShift { get; set; } -> float"""
    @property
    def GradientType(self) -> GradientPatternType:"""GradientType { get; } -> GradientPatternType"""
    @property
    def HatchObjectType(self) -> HatchObjectType:"""HatchObjectType { get; set; } -> HatchObjectType"""
    @property
    def HatchStyle(self) -> HatchStyle:"""HatchStyle { get; set; } -> HatchStyle"""
    @property
    def IsGradient(self) -> bool:"""IsGradient { get; } -> bool"""
    @property
    def IsHatch(self) -> bool:"""IsHatch { get; } -> bool"""
    @property
    def IsSolidFill(self) -> bool:"""IsSolidFill { get; } -> bool"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def NumberOfHatchLines(self) -> int:"""NumberOfHatchLines { get; } -> int"""
    @property
    def NumberOfLoops(self) -> int:"""NumberOfLoops { get; } -> int"""
    @property
    def NumberOfPatternDefinitions(self) -> int:"""NumberOfPatternDefinitions { get; } -> int"""
    @property
    def Origin(self) -> _n_2_t_0:"""Origin { get; set; } -> Point2d"""
    @property
    def PatternAngle(self) -> float:"""PatternAngle { get; set; } -> float"""
    @property
    def PatternDouble(self) -> bool:"""PatternDouble { get; set; } -> bool"""
    @property
    def PatternName(self) -> str:"""PatternName { get; } -> str"""
    @property
    def PatternScale(self) -> float:"""PatternScale { get; set; } -> float"""
    @property
    def PatternSpace(self) -> float:"""PatternSpace { get; set; } -> float"""
    @property
    def PatternType(self) -> HatchPatternType:"""PatternType { get; } -> HatchPatternType"""
    @property
    def ShadeTintValue(self) -> float:"""ShadeTintValue { get; set; } -> float"""
    def __init__(self) -> Hatch:...
    def AppendLoop(self, loopType: HatchLoopTypes, vertexCollection: _n_2_t_18, bulgeCollection: _n_2_t_13):...
    def AppendLoop(self, loopType: HatchLoopTypes, edgePtrCollection: _n_2_t_20, edgeTypeCollection: _n_2_t_16):...
    def AppendLoop(self, loopType: HatchLoopTypes, dbObjIds: ObjectIdCollection):...
    def AppendLoop(self, hatchLoop: HatchLoop):...
    def EvaluateGradientColorAt(self, value: float) -> _n_0_t_0:...
    def EvaluateHatch(self, underEstimateNumLines: bool):...
    def GetAssociatedObjectIds(self) -> ObjectIdCollection:...
    def GetAssociatedObjectIdsAt(self, loopIndex: int) -> ObjectIdCollection:...
    def GetGradientColors(self) -> _n_6_t_10[GradientColor]:...
    def GetHatchLineDataAt(self, index: int) -> _n_2_t_21:...
    def GetHatchLinesData(self) -> _n_2_t_22:...
    def GetLoopAt(self, loopIndex: int) -> HatchLoop:...
    def GetPatternDefinitionAt(self, index: int) -> PatternDefinition:...
    def InsertLoopAt(self, loopIndex: int, loopType: HatchLoopTypes, dbObjIds: ObjectIdCollection):...
    def InsertLoopAt(self, loopIndex: int, hatchLoop: HatchLoop):...
    def LoopTypeAt(self, loopIndex: int) -> HatchLoopTypes:...
    def RemoveAssociatedObjectIds(self):...
    def RemoveLoopAt(self, loopIndex: int):...
    def SetGradient(self, gradientType: GradientPatternType, gradientName: str):...
    def SetGradientColors(self, value: _n_6_t_10[GradientColor]):...
    def SetHatchPattern(self, patternType: HatchPatternType, patternName: str):...
class HatchEdgeType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CircularArc: int
    EllipticalArc: int
    Line: int
    Spline: int
    value__: int
class HatchLoop(object):
    @property
    def Curves(self) -> _n_2_t_20:"""Curves { get; } -> Curve2dCollection"""
    @property
    def IsPolyline(self) -> bool:"""IsPolyline { get; } -> bool"""
    @property
    def LoopType(self) -> HatchLoopTypes:"""LoopType { get; } -> HatchLoopTypes"""
    @property
    def Polyline(self) -> BulgeVertexCollection:"""Polyline { get; } -> BulgeVertexCollection"""
    def __init__(self, loopType: HatchLoopTypes) -> HatchLoop:...
class HatchLoopTypes(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Default: int
    Derived: int
    Duplicate: int
    External: int
    NotClosed: int
    Outermost: int
    Polyline: int
    SelfIntersecting: int
    Textbox: int
    TextIsland: int
    value__: int
class HatchObjectType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    GradientObject: int
    HatchObject: int
    value__: int
class HatchPatternType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CustomDefined: int
    PreDefined: int
    UserDefined: int
    value__: int
class HatchStyle(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Ignore: int
    Normal: int
    Outer: int
    value__: int
class Helix(Spline, _n_6_t_0, _n_6_t_1):
    @property
    def AxisVector(self) -> _n_2_t_3:"""AxisVector { get; set; } -> Vector3d"""
    @property
    def BaseRadius(self) -> float:"""BaseRadius { get; set; } -> float"""
    @property
    def Constrain(self) -> ConstrainType:"""Constrain { get; set; } -> ConstrainType"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def TopRadius(self) -> float:"""TopRadius { get; set; } -> float"""
    @property
    def TotalLength(self) -> float:"""TotalLength { get; } -> float"""
    @property
    def TurnHeight(self) -> float:"""TurnHeight { get; set; } -> float"""
    @property
    def Turns(self) -> float:"""Turns { get; set; } -> float"""
    @property
    def TurnSlope(self) -> float:"""TurnSlope { get; } -> float"""
    @property
    def Twist(self) -> bool:"""Twist { get; set; } -> bool"""
    def __init__(self) -> Helix:...
    def CreateHelix(self):...
    def GetAxisPoint(self) -> _n_2_t_1:...
    def SetAxisPoint(self, axisPoint: _n_2_t_1, moveStartPoint: bool):...
class HelpParameter(ConstraintGroupNode, _n_6_t_0, _n_6_t_1):
    @property
    def ConnectedConstraint(self) -> GeometricalConstraint:"""ConnectedConstraint { get; } -> GeometricalConstraint"""
    @property
    def ConnectedEqualparamConstraints(self) -> _n_6_t_10[EqualHelpParameterConstraint]:"""ConnectedEqualparamConstraints { get; } -> Array"""
    @property
    def ConnectedGeometry(self) -> ConstrainedGeometry:"""ConnectedGeometry { get; } -> ConstrainedGeometry"""
    @property
    def Value(self) -> float:"""Value { get; } -> float"""
    def __init__(self) -> HelpParameter:...
class HighlightOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def Highlight(self, entity: Entity, subId: FullSubentityPath, highlightAll: bool):...
    def Unhighlight(self, entity: Entity, subId: FullSubentityPath, highlightAll: bool):...
class HighlightStateOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def HighlightState(self, entity: Entity, subId: FullSubentityPath) -> _n_3_t_8:...
    def PopHighlight(self, entity: Entity, subId: FullSubentityPath):...
    def PushHighlight(self, entity: Entity, subId: FullSubentityPath, highlightStyle: _n_3_t_8):...
class HorizontalConstraint(ParallelConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> HorizontalConstraint:...
class HostApplicationServices(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def AllUsersRootFolder(self) -> str:"""AllUsersRootFolder { get; } -> str"""
    @property
    def AlternateFontName(self) -> str:"""AlternateFontName { get; } -> str"""
    @property
    def ColorBookLocation(self) -> str:"""ColorBookLocation { get; } -> str"""
    @property
    def CompanyName(self) -> str:"""CompanyName { get; } -> str"""
    @property
    def Current(self) -> HostApplicationServices:"""Current { get; set; } -> HostApplicationServices"""
    @property
    def FontMapFileName(self) -> str:"""FontMapFileName { get; } -> str"""
    @property
    def LocalRootFolder(self) -> str:"""LocalRootFolder { get; } -> str"""
    @property
    def MachineRegistryProductRootKey(self) -> str:"""MachineRegistryProductRootKey { get; } -> str"""
    @property
    def ModelerFlavor(self) -> ModelerFlavor:"""ModelerFlavor { get; } -> ModelerFlavor"""
    @property
    def Product(self) -> str:"""Product { get; } -> str"""
    @property
    def Program(self) -> str:"""Program { get; } -> str"""
    @property
    def releaseMarketVersion(self) -> str:"""releaseMarketVersion { get; } -> str"""
    @property
    def RoamableRootFolder(self) -> str:"""RoamableRootFolder { get; } -> str"""
    @property
    def UserRegistryProductRootKey(self) -> str:"""UserRegistryProductRootKey { get; } -> str"""
    @property
    def WorkingDatabase(self) -> Database:"""WorkingDatabase { get; set; } -> Database"""
    def FatalError(self, message: str):...
    def FindFile(self, fileName: str, database: Database, hint: FindFileHint) -> str:...
    def GetEnvironmentVariable(self, name: str) -> str:...
    def GetPassword(self, dwgName: str, options: PasswordOptions) -> str:...
    def GetRemoteFile(self, url: _n_6_t_26, ignoreCache: bool) -> str:...
    def GetUrl(self, localFile: str) -> _n_6_t_26:...
    def IsCloudFile(self, filePath: str) -> bool:...
    def IsUrl(self, filePath: str) -> bool:...
    def LoadApplication(self, appName: str, why: ApplicationLoadReasons, printIt: bool, asCmd: bool):...
    def NotifyCorruptDrawingFoundOnOpen(self, id: ObjectId, es: _n_5_t_1) -> bool:...
    def PutRemoteFile(self, url: _n_6_t_26, localFile: str):...
    def UserBreak(self) -> bool:...
class HyperLink(_n_5_t_3, _n_6_t_0):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def DisplayString(self) -> str:"""DisplayString { get; } -> str"""
    @property
    def IsOutermostContainer(self) -> bool:"""IsOutermostContainer { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NestedLevel(self) -> int:"""NestedLevel { get; } -> int"""
    @property
    def SubLocation(self) -> str:"""SubLocation { get; set; } -> str"""
    def __init__(self) -> HyperLink:...
class HyperLinkCollection(_n_5_t_3, _n_6_t_0, _n_7_t_5, typing.Iterable[typing.Any]):
    pass
class IBLBackground(Background, _n_6_t_0, _n_6_t_1):
    @property
    def DisplayImage(self) -> bool:"""DisplayImage { get; set; } -> bool"""
    @property
    def Enable(self) -> bool:"""Enable { get; set; } -> bool"""
    @property
    def IBLImageName(self) -> str:"""IBLImageName { get; set; } -> str"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def SecondaryBackground(self) -> ObjectId:"""SecondaryBackground { get; set; } -> ObjectId"""
    def __init__(self) -> IBLBackground:...
class IdMapping(_n_5_t_2, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    @property
    def DeepCloneContext(self) -> DeepCloneType:"""DeepCloneContext { get; } -> DeepCloneType"""
    @property
    def DestinationDatabase(self) -> Database:"""DestinationDatabase { get; set; } -> Database"""
    @property
    def DuplicateRecordCloning(self) -> DuplicateRecordCloning:"""DuplicateRecordCloning { get; } -> DuplicateRecordCloning"""
    @property
    def Item(self) -> IdPair:"""Item { get; set; } -> IdPair"""
    @property
    def OriginalDatabase(self) -> Database:"""OriginalDatabase { get; } -> Database"""
    def __init__(self) -> IdMapping:...
    def Add(self, pairToAdd: IdPair):...
    def Change(self, pairToChange: IdPair):...
    def Contains(self, key: ObjectId) -> bool:...
    def Delete(self, key: ObjectId):...
    def Lookup(self, key: ObjectId) -> IdPair:...
class IdMappingEventArgs(_n_6_t_13):
    @property
    def IdMapping(self) -> IdMapping:"""IdMapping { get; } -> IdMapping"""
class IdMappingEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> IdMappingEventHandler:...
    def BeginInvoke(self, sender: object, e: IdMappingEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: IdMappingEventArgs):...
class IdPair(_n_6_t_12):
    @property
    def IsCloned(self) -> bool:"""IsCloned { get; } -> bool"""
    @property
    def IsOwnerTranslated(self) -> bool:"""IsOwnerTranslated { get; } -> bool"""
    @property
    def IsPrimary(self) -> bool:"""IsPrimary { get; } -> bool"""
    @property
    def Key(self) -> ObjectId:"""Key { get; } -> ObjectId"""
    @property
    def Value(self) -> ObjectId:"""Value { get; } -> ObjectId"""
    def __init__(self, key: ObjectId, value: ObjectId, isCloned: bool, isPrimary: bool, isOwnerTranslated: bool) -> IdPair:...
class Image(Entity, _n_6_t_0, _n_6_t_1):
    pass
class ImageBackground(Background, _n_6_t_0, _n_6_t_1):
    @property
    def FitToScreen(self) -> bool:"""FitToScreen { get; set; } -> bool"""
    @property
    def ImageFileName(self) -> str:"""ImageFileName { get; set; } -> str"""
    @property
    def MaintainAspectRatio(self) -> bool:"""MaintainAspectRatio { get; set; } -> bool"""
    @property
    def Offset(self) -> _n_2_t_14:"""Offset { get; set; } -> Vector2d"""
    @property
    def Scale(self) -> _n_2_t_23:"""Scale { get; set; } -> Scale2d"""
    @property
    def UseTiling(self) -> bool:"""UseTiling { get; set; } -> bool"""
    def __init__(self) -> ImageBackground:...
class ImageDisplayOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Clip: int
    Show: int
    ShowUnaligned: int
    Transparent: int
    value__: int
class ImageQuality(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Draft: int
    High: int
    Invalid: int
    value__: int
class ImplicitPointType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CenterImplicit: int
    DefineImplicit: int
    EndImplicit: int
    MidImplicit: int
    StartImplicit: int
    value__: int
class IndexCreation(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    IndexByLayer: int
    IndexSpatially: int
    NoIndex: int
    value__: int
class InterferenceProtocolExtension(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def CreateInterferenceObjects(self, ent1: Entity, ent2: Entity, flags: int) -> _n_6_t_10[Entity]:...
class Intersect(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ExtendArgument: int
    ExtendBoth: int
    ExtendThis: int
    OnBothOperands: int
    value__: int
class IParameter(_n_6_t_0):
    @property
    def Angular(self) -> bool:"""Angular { get; } -> bool"""
    @property
    def DataType(self) -> DxfCode:"""DataType { get; } -> DxfCode"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def Expression(self) -> str:"""Expression { get; set; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ParameterObject(self) -> DBObject:"""ParameterObject { get; } -> DBObject"""
    @property
    def ReadOnly(self) -> bool:"""ReadOnly { get; } -> bool"""
    @property
    def Value(self) -> ResultBuffer:"""Value { get; set; } -> ResultBuffer"""
    @property
    def ValueSet(self) -> ParameterValueSet:"""ValueSet { get; } -> ParameterValueSet"""
    def IsNameUnique(self, name: str) -> bool:...
class ISpecialValueConverter():
    def ConvertToGlobal(self, o: object, value: str, converted: bool) -> str:...
    def ConvertToLocal(self, o: object, value: str, converted: bool) -> str:...
    def GetSpecialValues(self) -> _n_6_t_10[str]:...
class ISubObject():
    @property
    def Parent(self) -> object:"""Parent { get; set; } -> object"""
class ItemLocator(_n_6_t_12):
    @property
    def ItemIndex(self) -> int:"""ItemIndex { get; set; } -> int"""
    @property
    def LevelIndex(self) -> int:"""LevelIndex { get; set; } -> int"""
    @property
    def RowIndex(self) -> int:"""RowIndex { get; set; } -> int"""
    def __init__(self, itemIndex: int, rowIndex: int, levelIndex: int) -> ItemLocator:...
class ITextEditorSelectable():
    @property
    def EndOfText(self) -> TextEditorLocation:"""EndOfText { get; } -> TextEditorLocation"""
    @property
    def StartOfText(self) -> TextEditorLocation:"""StartOfText { get; } -> TextEditorLocation"""
class JoinStyle(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    StyleAngle: int
    StyleFlat: int
    StyleNone: int
    StyleRound: int
    value__: int
class LampColorPreset(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CoolWhite: int
    Custom: int
    D65White: int
    DaylightFluorescent: int
    Fluorescent: int
    Halogen: int
    HighPressureSodium: int
    Incandescent: int
    LowPressureSodium: int
    Mercury: int
    MetalHalide: int
    PhosphorMercury: int
    Quartz: int
    value__: int
    WhiteFluorescent: int
    Xenon: int
class LampColorType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Kelvin: int
    Preset: int
    value__: int
class LayerEvaluation(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    EvalAllNewLayers: int
    EvalNewXrefLayers: int
    NoNewLayerEvaluation: int
    value__: int
class LayerStateDeletedEventArgs(_n_6_t_13):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class LayerStateDeletedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> LayerStateDeletedEventHandler:...
    def BeginInvoke(self, sender: object, e: LayerStateDeletedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: LayerStateDeletedEventArgs):...
class LayerStateEventArgs(_n_6_t_13):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class LayerStateEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> LayerStateEventHandler:...
    def BeginInvoke(self, sender: object, e: LayerStateEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: LayerStateEventArgs):...
class LayerStateManager(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def LastRestoredLayerState(self) -> str:"""LastRestoredLayerState { get; } -> str"""
    @property
    def AbortLayerStateDelete(self) -> LayerStateEventHandler:
        """AbortLayerStateDelete Event: LayerStateEventHandler"""
    @property
    def AbortLayerStateRename(self) -> LayerStateRenameEventHandler:
        """AbortLayerStateRename Event: LayerStateRenameEventHandler"""
    @property
    def AbortLayerStateRestore(self) -> LayerStateEventHandler:
        """AbortLayerStateRestore Event: LayerStateEventHandler"""
    @property
    def LayerStateCompareFailed(self) -> LayerStateEventHandler:
        """LayerStateCompareFailed Event: LayerStateEventHandler"""
    @property
    def LayerStateCreated(self) -> LayerStateEventHandler:
        """LayerStateCreated Event: LayerStateEventHandler"""
    @property
    def LayerStateDeleted(self) -> LayerStateDeletedEventHandler:
        """LayerStateDeleted Event: LayerStateDeletedEventHandler"""
    @property
    def LayerStateRenamed(self) -> LayerStateRenameEventHandler:
        """LayerStateRenamed Event: LayerStateRenameEventHandler"""
    @property
    def LayerStateRestored(self) -> LayerStateEventHandler:
        """LayerStateRestored Event: LayerStateEventHandler"""
    @property
    def LayerStateToBeDeleted(self) -> LayerStateEventHandler:
        """LayerStateToBeDeleted Event: LayerStateEventHandler"""
    @property
    def LayerStateToBeRenamed(self) -> LayerStateRenameEventHandler:
        """LayerStateToBeRenamed Event: LayerStateRenameEventHandler"""
    @property
    def LayerStateToBeRestored(self) -> LayerStateEventHandler:
        """LayerStateToBeRestored Event: LayerStateEventHandler"""
    def __init__(self, database: Database) -> LayerStateManager:...
    def CompareLayerStateToDb(self, name: str, idVp: ObjectId) -> bool:...
    def DeleteLayerState(self, name: str):...
    def ExportLayerState(self, nameToExport: str, fileName: str):...
    def GetLayerStateDescription(self, name: str) -> str:...
    def GetLayerStateLayers(self, name: str, bInvert: bool) -> _n_7_t_1:...
    def GetLayerStateMask(self, name: str) -> LayerStateMasks:...
    def GetLayerStateNames(self, bIncludeHidden: bool, bIncludeXref: bool) -> _n_7_t_1:...
    def HasLayerState(self, name: str) -> bool:...
    def ImportLayerState(self, fileName: str):...
    def ImportLayerStateFromDb(self, name: str, database: Database):...
    def LayerStateHasViewportData(self, name: str) -> bool:...
    def LayerStatesDictionaryId(self, createIfNotPresent: bool) -> ObjectId:...
    def RenameLayerState(self, name: str, newName: str):...
    def RestoreLayerState(self, name: str, id: ObjectId, undefinedLayerStatePolicy: int, clientMask: LayerStateMasks):...
    def SaveLayerState(self, name: str, mask: LayerStateMasks, id: ObjectId):...
    def SetLayerStateDescription(self, name: str, description: str):...
    def SetLayerStateMask(self, name: str, mask: LayerStateMasks):...
class LayerStateMasks(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Color: int
    CurrentViewport: int
    Frozen: int
    LastRestored: int
    LineType: int
    LineWeight: int
    Locked: int
    NewViewport: int
    _None: int
    On: int
    Plot: int
    PlotStyle: int
    Transparency: int
    value__: int
class LayerStateRenameEventArgs(_n_6_t_13):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def NewName(self) -> str:"""NewName { get; } -> str"""
class LayerStateRenameEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> LayerStateRenameEventHandler:...
    def BeginInvoke(self, sender: object, e: LayerStateRenameEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: LayerStateRenameEventArgs):...
class LayerTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    @property
    def HasUnreconciledLayers(self) -> bool:"""HasUnreconciledLayers { get; } -> bool"""
    @property
    def IncludingHidden(self) -> LayerTable:"""IncludingHidden { get; } -> LayerTable"""
    @property
    def SkippingReconciled(self) -> LayerTable:"""SkippingReconciled { get; } -> LayerTable"""
    def GenerateUsageData(self):...
    def GetUnreconciledLayers(self) -> ObjectIdCollection:...
class LayerTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; set; } -> Color"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def EntityColor(self) -> _n_0_t_2:"""EntityColor { get; } -> EntityColor"""
    @property
    def HasOverrides(self) -> bool:"""HasOverrides { get; } -> bool"""
    @property
    def IsFrozen(self) -> bool:"""IsFrozen { get; set; } -> bool"""
    @property
    def IsHidden(self) -> bool:"""IsHidden { get; set; } -> bool"""
    @property
    def IsLocked(self) -> bool:"""IsLocked { get; set; } -> bool"""
    @property
    def IsOff(self) -> bool:"""IsOff { get; set; } -> bool"""
    @property
    def IsPlottable(self) -> bool:"""IsPlottable { get; set; } -> bool"""
    @property
    def IsReconciled(self) -> bool:"""IsReconciled { get; set; } -> bool"""
    @property
    def IsUsed(self) -> bool:"""IsUsed { get; } -> bool"""
    @property
    def LinetypeObjectId(self) -> ObjectId:"""LinetypeObjectId { get; set; } -> ObjectId"""
    @property
    def LineWeight(self) -> LineWeight:"""LineWeight { get; set; } -> LineWeight"""
    @property
    def MaterialId(self) -> ObjectId:"""MaterialId { get; set; } -> ObjectId"""
    @property
    def PlotStyleName(self) -> str:"""PlotStyleName { get; set; } -> str"""
    @property
    def PlotStyleNameId(self) -> ObjectId:"""PlotStyleNameId { get; set; } -> ObjectId"""
    @property
    def Transparency(self) -> _n_0_t_1:"""Transparency { get; set; } -> Transparency"""
    @property
    def ViewportVisibilityDefault(self) -> bool:"""ViewportVisibilityDefault { get; set; } -> bool"""
    def __init__(self) -> LayerTableRecord:...
    def GetViewportOverrides(self, viewportId: ObjectId) -> LayerViewportProperties:...
    def HasViewportOverrides(self, viewportId: ObjectId) -> bool:...
    def RemoveAllOverrides(self):...
class LayerViewportProperties(object):
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; set; } -> Color"""
    @property
    def IsColorOverridden(self) -> bool:"""IsColorOverridden { get; set; } -> bool"""
    @property
    def IsLinetypeOverridden(self) -> bool:"""IsLinetypeOverridden { get; set; } -> bool"""
    @property
    def IsLineWeightOverridden(self) -> bool:"""IsLineWeightOverridden { get; set; } -> bool"""
    @property
    def IsPlotStyleOverridden(self) -> bool:"""IsPlotStyleOverridden { get; set; } -> bool"""
    @property
    def IsTransparencyOverridden(self) -> bool:"""IsTransparencyOverridden { get; set; } -> bool"""
    @property
    def LinetypeObjectId(self) -> ObjectId:"""LinetypeObjectId { get; set; } -> ObjectId"""
    @property
    def LineWeight(self) -> LineWeight:"""LineWeight { get; set; } -> LineWeight"""
    @property
    def PlotStyleName(self) -> str:"""PlotStyleName { get; set; } -> str"""
    @property
    def PlotStyleNameId(self) -> ObjectId:"""PlotStyleNameId { get; set; } -> ObjectId"""
    @property
    def Transparency(self) -> _n_0_t_1:"""Transparency { get; set; } -> Transparency"""
    def RemoveOverrides(self):...
class Layout(PlotSettings, _n_6_t_0, _n_6_t_1):
    @property
    def AnnoAllVisible(self) -> bool:"""AnnoAllVisible { get; set; } -> bool"""
    @property
    def BlockTableRecordId(self) -> ObjectId:"""BlockTableRecordId { get; set; } -> ObjectId"""
    @property
    def Extents(self) -> Extents3d:"""Extents { get; } -> Extents3d"""
    @property
    def LayoutName(self) -> str:"""LayoutName { get; set; } -> str"""
    @property
    def Limits(self) -> Extents2d:"""Limits { get; } -> Extents2d"""
    @property
    def TabOrder(self) -> int:"""TabOrder { get; set; } -> int"""
    @property
    def TabSelected(self) -> bool:"""TabSelected { get; set; } -> bool"""
    @property
    def Thumbnail(self) -> _n_11_t_0:"""Thumbnail { get; set; } -> Bitmap"""
    def __init__(self) -> Layout:...
    def AddToLayoutDictionary(self, toWhichDatabase: Database, blockTableRecordId: ObjectId):...
    def GetViewports(self) -> ObjectIdCollection:...
    def Initialize(self) -> ObjectId:...
class LayoutCopiedEventArgs(_n_6_t_13):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def NewId(self) -> ObjectId:"""NewId { get; } -> ObjectId"""
    @property
    def NewName(self) -> str:"""NewName { get; } -> str"""
class LayoutCopiedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> LayoutCopiedEventHandler:...
    def BeginInvoke(self, sender: object, e: LayoutCopiedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: LayoutCopiedEventArgs):...
class LayoutEventArgs(_n_6_t_13):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class LayoutEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> LayoutEventHandler:...
    def BeginInvoke(self, sender: object, e: LayoutEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: LayoutEventArgs):...
class LayoutManager(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def Current(self) -> LayoutManager:"""Current { get; } -> LayoutManager"""
    @property
    def CurrentLayout(self) -> str:"""CurrentLayout { get; set; } -> str"""
    @property
    def LayoutCount(self) -> int:"""LayoutCount { get; } -> int"""
    @property
    def AbortLayoutCopied(self) -> LayoutEventHandler:
        """AbortLayoutCopied Event: LayoutEventHandler"""
    @property
    def AbortLayoutRemoved(self) -> LayoutEventHandler:
        """AbortLayoutRemoved Event: LayoutEventHandler"""
    @property
    def AbortLayoutRename(self) -> LayoutRenamedEventHandler:
        """AbortLayoutRename Event: LayoutRenamedEventHandler"""
    @property
    def LayoutCopied(self) -> LayoutCopiedEventHandler:
        """LayoutCopied Event: LayoutCopiedEventHandler"""
    @property
    def LayoutCreated(self) -> LayoutEventHandler:
        """LayoutCreated Event: LayoutEventHandler"""
    @property
    def LayoutRemoved(self) -> LayoutEventHandler:
        """LayoutRemoved Event: LayoutEventHandler"""
    @property
    def LayoutRenamed(self) -> LayoutRenamedEventHandler:
        """LayoutRenamed Event: LayoutRenamedEventHandler"""
    @property
    def LayoutsRefresh(self) -> _n_6_t_17:
        """LayoutsRefresh Event: EventHandler"""
    @property
    def LayoutsReordered(self) -> _n_6_t_17:
        """LayoutsReordered Event: EventHandler"""
    @property
    def LayoutSwitched(self) -> LayoutEventHandler:
        """LayoutSwitched Event: LayoutEventHandler"""
    @property
    def LayoutToBeCopied(self) -> LayoutEventHandler:
        """LayoutToBeCopied Event: LayoutEventHandler"""
    @property
    def LayoutToBeRemoved(self) -> LayoutEventHandler:
        """LayoutToBeRemoved Event: LayoutEventHandler"""
    @property
    def LayoutToBeRenamed(self) -> LayoutRenamedEventHandler:
        """LayoutToBeRenamed Event: LayoutRenamedEventHandler"""
    @property
    def PlotStyleTableChanged(self) -> PlotStyleTableChangedEventHandler:
        """PlotStyleTableChanged Event: PlotStyleTableChangedEventHandler"""
    def CloneLayout(self, copyName: str, newName: str, newTabOrder: int):...
    def CopyLayout(self, copyName: str, newName: str):...
    def CreateLayout(self, newName: str) -> ObjectId:...
    def DeleteLayout(self, deleteName: str):...
    def GetLayoutId(self, name: str) -> ObjectId:...
    def GetNonRectangularViewportIdFromClipId(self, clipId: ObjectId) -> ObjectId:...
    def RenameLayout(self, oldName: str, newName: str):...
    def SetCurrentLayoutId(self, layoutId: ObjectId):...
class LayoutRenamedEventArgs(_n_6_t_13):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def NewName(self) -> str:"""NewName { get; } -> str"""
class LayoutRenamedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> LayoutRenamedEventHandler:...
    def BeginInvoke(self, sender: object, e: LayoutRenamedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: LayoutRenamedEventArgs):...
class Leader(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def AnnoHeight(self) -> float:"""AnnoHeight { get; } -> float"""
    @property
    def Annotation(self) -> ObjectId:"""Annotation { get; set; } -> ObjectId"""
    @property
    def AnnotationOffset(self) -> _n_2_t_3:"""AnnotationOffset { get; set; } -> Vector3d"""
    @property
    def AnnoType(self) -> AnnotationType:"""AnnoType { get; } -> AnnotationType"""
    @property
    def AnnoWidth(self) -> float:"""AnnoWidth { get; } -> float"""
    @property
    def Dimasz(self) -> float:"""Dimasz { get; set; } -> float"""
    @property
    def Dimclrd(self) -> _n_0_t_0:"""Dimclrd { get; set; } -> Color"""
    @property
    def DimensionStyle(self) -> ObjectId:"""DimensionStyle { get; set; } -> ObjectId"""
    @property
    def DimensionStyleName(self) -> str:"""DimensionStyleName { get; set; } -> str"""
    @property
    def Dimgap(self) -> float:"""Dimgap { get; set; } -> float"""
    @property
    def Dimldrblk(self) -> ObjectId:"""Dimldrblk { get; set; } -> ObjectId"""
    @property
    def Dimlwd(self) -> LineWeight:"""Dimlwd { get; set; } -> LineWeight"""
    @property
    def Dimsah(self) -> bool:"""Dimsah { get; set; } -> bool"""
    @property
    def Dimscale(self) -> float:"""Dimscale { get; set; } -> float"""
    @property
    def Dimtad(self) -> int:"""Dimtad { get; set; } -> int"""
    @property
    def Dimtxt(self) -> float:"""Dimtxt { get; set; } -> float"""
    @property
    def FirstVertex(self) -> _n_2_t_1:"""FirstVertex { get; } -> Point3d"""
    @property
    def HasArrowHead(self) -> bool:"""HasArrowHead { get; set; } -> bool"""
    @property
    def HasHookLine(self) -> bool:"""HasHookLine { get; } -> bool"""
    @property
    def IsSplined(self) -> bool:"""IsSplined { get; set; } -> bool"""
    @property
    def LastVertex(self) -> _n_2_t_1:"""LastVertex { get; } -> Point3d"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def NumVertices(self) -> int:"""NumVertices { get; } -> int"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    def __init__(self) -> Leader:...
    def AppendVertex(self, pointToAdd: _n_2_t_1) -> bool:...
    def EvaluateLeader(self):...
    def GetDimstyleData(self) -> DimStyleTableRecord:...
    def RemoveLastVertex(self):...
    def SetDimstyleData(self, style: DimStyleTableRecord):...
    def SetPlane(self, value: _n_2_t_4):...
    def SetVertexAt(self, index: int, pointValue: _n_2_t_1) -> bool:...
    def VertexAt(self, value: int) -> _n_2_t_1:...
class LeaderDirectionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BottomLeader: int
    LeftLeader: int
    RightLeader: int
    TopLeader: int
    UnknownLeader: int
    value__: int
class LeaderType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    InVisibleLeader: int
    SplineLeader: int
    StraightLeader: int
    value__: int
class Light(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Attenuation(self) -> _n_3_t_11:"""Attenuation { get; set; } -> LightAttenuation"""
    @property
    def AttenuationType(self) -> _n_3_t_12:"""AttenuationType { get; set; } -> AttenuationType"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; set; } -> Vector3d"""
    @property
    def EndLimitOffset(self) -> float:"""EndLimitOffset { get; set; } -> float"""
    @property
    def FalloffAngle(self) -> float:"""FalloffAngle { get; } -> float"""
    @property
    def HasTarget(self) -> bool:"""HasTarget { get; set; } -> bool"""
    @property
    def HotspotAngle(self) -> float:"""HotspotAngle { get; } -> float"""
    @property
    def IlluminanceDistance(self) -> float:"""IlluminanceDistance { get; set; } -> float"""
    @property
    def Intensity(self) -> float:"""Intensity { get; set; } -> float"""
    @property
    def IsOn(self) -> bool:"""IsOn { get; set; } -> bool"""
    @property
    def IsPlottable(self) -> bool:"""IsPlottable { get; set; } -> bool"""
    @property
    def LampColorPreset(self) -> LampColorPreset:"""LampColorPreset { get; set; } -> LampColorPreset"""
    @property
    def LampColorRGB(self) -> _n_3_t_13:"""LampColorRGB { get; set; } -> ColorRGB"""
    @property
    def LampColorTemp(self) -> float:"""LampColorTemp { get; set; } -> float"""
    @property
    def LampColorType(self) -> LampColorType:"""LampColorType { get; set; } -> LampColorType"""
    @property
    def LightColor(self) -> _n_0_t_0:"""LightColor { get; set; } -> Color"""
    @property
    def LightType(self) -> _n_3_t_14:"""LightType { get; set; } -> DrawableType"""
    @property
    def MapSize(self) -> int:"""MapSize { get; set; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PhysicalIntensity(self) -> float:"""PhysicalIntensity { get; set; } -> float"""
    @property
    def PhysicalIntensityMethod(self) -> PhysicalIntensityMethod:"""PhysicalIntensityMethod { get; set; } -> PhysicalIntensityMethod"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Shadow(self) -> _n_3_t_15:"""Shadow { get; set; } -> ShadowParameters"""
    @property
    def ShadowType(self) -> _n_3_t_16:"""ShadowType { get; set; } -> ShadowType"""
    @property
    def Softness(self) -> _n_6_t_19:"""Softness { get; set; } -> Byte"""
    @property
    def StartLimitOffset(self) -> float:"""StartLimitOffset { get; set; } -> float"""
    @property
    def TargetLocation(self) -> _n_2_t_1:"""TargetLocation { get; set; } -> Point3d"""
    @property
    def UseLimits(self) -> bool:"""UseLimits { get; set; } -> bool"""
    @property
    def WebFile(self) -> str:"""WebFile { get; set; } -> str"""
    @property
    def WebRotation(self) -> _n_2_t_3:"""WebRotation { get; set; } -> Vector3d"""
    def __init__(self) -> Light:...
    def ResultingColor(self) -> _n_0_t_0:...
    def SetHotspotAndFalloff(self, hotspot: float, falloff: float):...
class LightingUnits(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    LightingUnitsAmerican: int
    LightingUnitsGeneric: int
    LightingUnitsInternational: int
    value__: int
class Line(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def Angle(self) -> float:"""Angle { get; } -> float"""
    @property
    def Delta(self) -> _n_2_t_3:"""Delta { get; } -> Vector3d"""
    @property
    def Length(self) -> float:"""Length { get; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, pointer1: _n_2_t_1, pointer2: _n_2_t_1) -> Line:...
    def __init__(self) -> Line:...
class LineAngularDimension2(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def ArcPoint(self) -> _n_2_t_1:"""ArcPoint { get; set; } -> Point3d"""
    @property
    def XLine1End(self) -> _n_2_t_1:"""XLine1End { get; set; } -> Point3d"""
    @property
    def XLine1Start(self) -> _n_2_t_1:"""XLine1Start { get; set; } -> Point3d"""
    @property
    def XLine2End(self) -> _n_2_t_1:"""XLine2End { get; set; } -> Point3d"""
    @property
    def XLine2Start(self) -> _n_2_t_1:"""XLine2Start { get; set; } -> Point3d"""
    def __init__(self, line1Start: _n_2_t_1, line1End: _n_2_t_1, line2Start: _n_2_t_1, line2End: _n_2_t_1, arcPoint: _n_2_t_1, dimensionText: str, dimensionStyle: ObjectId) -> LineAngularDimension2:...
    def __init__(self) -> LineAngularDimension2:...
class LineSpacingStyle(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AtLeast: int
    Exactly: int
    value__: int
class LinetypeTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class LinetypeTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def AsciiDescription(self) -> str:"""AsciiDescription { get; set; } -> str"""
    @property
    def Comments(self) -> str:"""Comments { get; set; } -> str"""
    @property
    def IsScaledToFit(self) -> bool:"""IsScaledToFit { get; set; } -> bool"""
    @property
    def NumDashes(self) -> int:"""NumDashes { get; set; } -> int"""
    @property
    def PatternLength(self) -> float:"""PatternLength { get; set; } -> float"""
    def __init__(self) -> LinetypeTableRecord:...
    def DashLengthAt(self, index: int) -> float:...
    def SetDashLengthAt(self, index: int, value: float):...
    def SetShapeIsUcsOrientedAt(self, index: int, isOriented: bool):...
    def SetShapeNumberAt(self, index: int, shapeNumber: int):...
    def SetShapeOffsetAt(self, index: int, offset: _n_2_t_14):...
    def SetShapeRotationAt(self, index: int, rotation: float):...
    def SetShapeScaleAt(self, index: int, scale: float):...
    def SetShapeStyleAt(self, index: int, id: ObjectId):...
    def SetTextAt(self, index: int, value: str):...
    def ShapeIsUcsOrientedAt(self, index: int) -> bool:...
    def ShapeNumberAt(self, index: int) -> int:...
    def ShapeOffsetAt(self, index: int) -> _n_2_t_14:...
    def ShapeRotationAt(self, index: int) -> float:...
    def ShapeScaleAt(self, index: int) -> float:...
    def ShapeStyleAt(self, index: int) -> ObjectId:...
    def TextAt(self, index: int) -> str:...
class LineWeight(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ByBlock: int
    ByLayer: int
    ByLineWeightDefault: int
    LineWeight000: int
    LineWeight005: int
    LineWeight009: int
    LineWeight013: int
    LineWeight015: int
    LineWeight018: int
    LineWeight020: int
    LineWeight025: int
    LineWeight030: int
    LineWeight035: int
    LineWeight040: int
    LineWeight050: int
    LineWeight053: int
    LineWeight060: int
    LineWeight070: int
    LineWeight080: int
    LineWeight090: int
    LineWeight100: int
    LineWeight106: int
    LineWeight120: int
    LineWeight140: int
    LineWeight158: int
    LineWeight200: int
    LineWeight211: int
    value__: int
class LineWeightConverter(_n_10_t_1):
    def __init__(self) -> LineWeightConverter:...
class LinkedData(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def IsEmpty(self) -> bool:"""IsEmpty { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    def Clear(self):...
class LinkedTableData(LinkedData, _n_6_t_0, _n_6_t_1):
    @property
    def NumberOfColumns(self) -> int:"""NumberOfColumns { get; } -> int"""
    @property
    def NumberOfRows(self) -> int:"""NumberOfRows { get; } -> int"""
    def __init__(self) -> LinkedTableData:...
    def AppendColumn(self, columnsNumber: int) -> int:...
    def AppendRow(self, rowsNumber: int) -> int:...
    def DataType(self, row: int, column: int) -> DataType:...
    def DeleteColumn(self, index: int, columnsNumberToDelete: int):...
    def DeleteContent(self, row: int, column: int):...
    def DeleteRow(self, index: int, rowsNumberToDelete: int):...
    def GetBlockAttributeValue(self, row: int, column: int, attributeDefinitionId: ObjectId) -> str:...
    def GetBlockTableRecordId(self, row: int, column: int) -> ObjectId:...
    def GetCellState(self, row: int, column: int) -> CellStates:...
    def GetColumnName(self, index: int) -> str:...
    def GetContentTypes(self, row: int, column: int) -> CellContentTypes:...
    def GetCustomData(self, row: int, column: int, key: str) -> object:...
    def GetDataFormat(self, row: int, column: int) -> str:...
    def GetDataLink(self, range: CellRange) -> ObjectIdCollection:...
    def GetDataLink(self) -> ObjectIdCollection:...
    def GetDataLink(self, row: int, column: int) -> ObjectId:...
    def GetEnumerator(self, option: TableEnumeratorOption) -> TableEnumerator:...
    def GetEnumerator(self) -> TableEnumerator:...
    def GetFieldId(self, row: int, column: int) -> ObjectId:...
    def GetToolTip(self, row: int, column: int) -> str:...
    def GetValue(self, row: int, column: int, content: int, formatOption: FormatOption) -> object:...
    def GetValue(self, row: int, column: int) -> object:...
    def InsertColumn(self, index: int, columnsNumber: int) -> int:...
    def InsertRow(self, index: int, rowsNumber: int) -> int:...
    def IsContentEditable(self, row: int, column: int) -> bool:...
    def IsLinked(self, row: int, column: int) -> bool:...
    def SetBlockAttributeValue(self, row: int, column: int, attributeDefinitionId: ObjectId, value: str):...
    def SetBlockTableRecordId(self, row: int, column: int, value: ObjectId):...
    def SetCellState(self, row: int, column: int, value: CellStates):...
    def SetColumnName(self, index: int, name: str):...
    def SetCustomData(self, row: int, column: int, key: str, value: object):...
    def SetDataFormat(self, row: int, column: int, format: str):...
    def SetDataLink(self, range: CellRange, dataLinkId: ObjectId, bUpdate: bool):...
    def SetDataLink(self, row: int, column: int, dataLinkId: ObjectId, bUpdate: bool):...
    def SetDataType(self, row: int, column: int, dataType: DataType, unitType: UnitType):...
    def SetFieldId(self, row: int, column: int, value: ObjectId):...
    def SetSize(self, numRows: int, numCols: int):...
    def SetToolTip(self, row: int, column: int, value: str):...
    def SetValue(self, row: int, column: int, content: int, value: object, parseOption: ParseOption):...
    def SetValue(self, row: int, column: int, value: object):...
    def UnitType(self, row: int, column: int) -> UnitType:...
    def UpdateDataLink(self, dir: UpdateDirection, option: UpdateOption):...
    def UpdateDataLink(self, row: int, column: int, dir: UpdateDirection, option: UpdateOption):...
class LoftedSurface(Surface, _n_6_t_0, _n_6_t_1):
    @property
    def Closed(self) -> bool:"""Closed { get; set; } -> bool"""
    @property
    def CrossSectionProfiles(self) -> _n_6_t_10[LoftProfile]:"""CrossSectionProfiles { get; } -> Array"""
    @property
    def CrossSections(self) -> _n_6_t_10[Entity]:"""CrossSections { get; } -> Array"""
    @property
    def EndCrossSectionContinuity(self) -> int:"""EndCrossSectionContinuity { get; set; } -> int"""
    @property
    def EndCrossSectionMagnitude(self) -> float:"""EndCrossSectionMagnitude { get; set; } -> float"""
    @property
    def EndGuideCurveContinuity(self) -> int:"""EndGuideCurveContinuity { get; set; } -> int"""
    @property
    def EndGuideCurveMagnitude(self) -> float:"""EndGuideCurveMagnitude { get; set; } -> float"""
    @property
    def GuideCurves(self) -> _n_6_t_10[Entity]:"""GuideCurves { get; } -> Array"""
    @property
    def GuideProfiles(self) -> _n_6_t_10[LoftProfile]:"""GuideProfiles { get; } -> Array"""
    @property
    def LoftOptions(self) -> LoftOptions:"""LoftOptions { get; set; } -> LoftOptions"""
    @property
    def NumberOfCrossSections(self) -> int:"""NumberOfCrossSections { get; } -> int"""
    @property
    def NumberOfGuideCurves(self) -> int:"""NumberOfGuideCurves { get; } -> int"""
    @property
    def PathEntity(self) -> Entity:"""PathEntity { get; } -> Entity"""
    @property
    def PathProfile(self) -> LoftProfile:"""PathProfile { get; } -> LoftProfile"""
    @property
    def StartCrossSectionContinuity(self) -> int:"""StartCrossSectionContinuity { get; set; } -> int"""
    @property
    def StartCrossSectionMagnitude(self) -> float:"""StartCrossSectionMagnitude { get; set; } -> float"""
    @property
    def StartGuideCurveContinuity(self) -> int:"""StartGuideCurveContinuity { get; set; } -> int"""
    @property
    def StartGuideCurveMagnitude(self) -> float:"""StartGuideCurveMagnitude { get; set; } -> float"""
    @property
    def SurfaceType(self) -> LoftedSurface.LoftSurfaceType:"""SurfaceType { get; } -> LoftedSurface.LoftSurfaceType"""
    def __init__(self) -> LoftedSurface:...
    def GetCrossSectionProfile(self, idx: int) -> LoftProfile:...
    def GetGuideProfile(self, idx: int) -> LoftProfile:...
    class LoftSurfaceType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        BlendSurface: int
        LoftSurface: int
        NetworkSurface: int
        value__: int
class LoftOptions(_n_5_t_3, _n_6_t_0, _n_6_t_1):
    @property
    def AlignDirection(self) -> bool:"""AlignDirection { get; } -> bool"""
    @property
    def ArcLengthParam(self) -> bool:"""ArcLengthParam { get; } -> bool"""
    @property
    def Closed(self) -> bool:"""Closed { get; } -> bool"""
    @property
    def DraftEnd(self) -> float:"""DraftEnd { get; } -> float"""
    @property
    def DraftEndMag(self) -> float:"""DraftEndMag { get; } -> float"""
    @property
    def DraftStart(self) -> float:"""DraftStart { get; } -> float"""
    @property
    def DraftStartMag(self) -> float:"""DraftStartMag { get; } -> float"""
    @property
    def NormalOption(self) -> LoftOptionsNormalOption:"""NormalOption { get; } -> LoftOptionsNormalOption"""
    @property
    def NoTwist(self) -> bool:"""NoTwist { get; } -> bool"""
    @property
    def Ruled(self) -> bool:"""Ruled { get; } -> bool"""
    @property
    def Simplify(self) -> bool:"""Simplify { get; } -> bool"""
    @property
    def VirtualGuide(self) -> bool:"""VirtualGuide { get; } -> bool"""
    def __init__(self, opts: LoftOptions) -> LoftOptions:...
    def __init__(self) -> LoftOptions:...
    def CheckCrossSectionCurves(self, crossSectionCurves: _n_6_t_10[Entity], displayErrorMessages: bool) -> LoftOptionsCheckCurvesOut:...
    def CheckGuideCurves(self, guideCurves: _n_6_t_10[Entity], displayErrorMessages: bool):...
    def CheckLoftCurves(self, crossSectionCurves: _n_6_t_10[Entity], guideCurves: _n_6_t_10[Entity], pPathCurve: Entity, displayErrorMessages: bool) -> LoftOptionsCheckCurvesOut:...
    def CheckPathCurve(self, pathCurve: Entity, displayErrorMessages: bool):...
class LoftOptionsBuilder(object):
    @property
    def AlignDirection(self) -> bool:"""AlignDirection { get; set; } -> bool"""
    @property
    def ArcLengthParam(self) -> bool:"""ArcLengthParam { get; set; } -> bool"""
    @property
    def Closed(self) -> bool:"""Closed { get; set; } -> bool"""
    @property
    def DraftEnd(self) -> float:"""DraftEnd { get; set; } -> float"""
    @property
    def DraftEndMag(self) -> float:"""DraftEndMag { get; set; } -> float"""
    @property
    def DraftStart(self) -> float:"""DraftStart { get; set; } -> float"""
    @property
    def DraftStartMag(self) -> float:"""DraftStartMag { get; set; } -> float"""
    @property
    def NormalOption(self) -> LoftOptionsNormalOption:"""NormalOption { get; set; } -> LoftOptionsNormalOption"""
    @property
    def NoTwist(self) -> bool:"""NoTwist { get; set; } -> bool"""
    @property
    def Ruled(self) -> bool:"""Ruled { get; set; } -> bool"""
    @property
    def Simplify(self) -> bool:"""Simplify { get; set; } -> bool"""
    @property
    def VirtualGuide(self) -> bool:"""VirtualGuide { get; set; } -> bool"""
    def __init__(self, value: LoftOptions) -> LoftOptionsBuilder:...
    def __init__(self) -> LoftOptionsBuilder:...
    def SetOptionsFromSysvars(self):...
    def ToLoftOptions(self) -> LoftOptions:...
class LoftOptionsCheckCurvesOut(object):
    @property
    def AllClosed(self) -> bool:"""AllClosed { get; } -> bool"""
    @property
    def AllOpen(self) -> bool:"""AllOpen { get; } -> bool"""
    @property
    def AllPlanar(self) -> bool:"""AllPlanar { get; } -> bool"""
    def __init__(self) -> LoftOptionsCheckCurvesOut:...
class LoftOptionsNormalOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AllNormal: int
    EndsNormal: int
    FirstNormal: int
    LastNormal: int
    NoNormal: int
    UseDraftAngles: int
    value__: int
class LoftProfile(Profile3d, _n_6_t_0, _n_6_t_1):
    @property
    def Continuity(self) -> int:"""Continuity { get; set; } -> int"""
    @property
    def Magnitude(self) -> float:"""Magnitude { get; set; } -> float"""
    def __init__(self, LoftProfile: LoftProfile) -> LoftProfile:...
    def __init__(self, pnt: _n_2_t_1) -> LoftProfile:...
    def __init__(self, entity: Entity) -> LoftProfile:...
    def __init__(self, pathRef: PathRef) -> LoftProfile:...
    def __init__(self) -> LoftProfile:...
class LongTransaction(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ActiveIdMap(self) -> IdMapping:"""ActiveIdMap { get; } -> IdMapping"""
    @property
    def DestinationBlock(self) -> ObjectId:"""DestinationBlock { get; } -> ObjectId"""
    @property
    def DisallowDrawOrder(self) -> bool:"""DisallowDrawOrder { get; } -> bool"""
    @property
    def LongTransactionName(self) -> str:"""LongTransactionName { get; } -> str"""
    @property
    def OriginBlock(self) -> ObjectId:"""OriginBlock { get; } -> ObjectId"""
    @property
    def Type(self) -> LongTransactionType:"""Type { get; } -> LongTransactionType"""
    def __init__(self) -> LongTransaction:...
    def __init__(self, unmanagedPointer: _n_6_t_3, autoDelete: bool) -> LongTransaction:...
    def AddToWorkSet(self, id: ObjectId):...
    def OriginObject(self, id: ObjectId) -> ObjectId:...
    def RegenWorkSetWithDrawOrder(self):...
    def RemoveFromWorkSet(self, id: ObjectId):...
    def SyncWorkSet(self):...
    def WorkSetHas(self, id: ObjectId, includeErased: bool) -> bool:...
class LongTransactionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    SameDb: int
    UnrelatedDb: int
    value__: int
    XRefDb: int
class MaintenanceReleaseVersion(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Release0: int
    Release1: int
    Release10: int
    Release100: int
    Release101: int
    Release102: int
    Release103: int
    Release104: int
    Release105: int
    Release106: int
    Release107: int
    Release108: int
    Release109: int
    Release11: int
    Release110: int
    Release111: int
    Release112: int
    Release113: int
    Release114: int
    Release115: int
    Release116: int
    Release117: int
    Release118: int
    Release119: int
    Release12: int
    Release120: int
    Release121: int
    Release122: int
    Release123: int
    Release124: int
    Release125: int
    Release126: int
    Release127: int
    Release128: int
    Release129: int
    Release13: int
    Release130: int
    Release131: int
    Release132: int
    Release133: int
    Release134: int
    Release135: int
    Release136: int
    Release137: int
    Release138: int
    Release139: int
    Release14: int
    Release140: int
    Release141: int
    Release142: int
    Release143: int
    Release144: int
    Release145: int
    Release146: int
    Release147: int
    Release148: int
    Release149: int
    Release15: int
    Release150: int
    Release151: int
    Release152: int
    Release153: int
    Release154: int
    Release155: int
    Release156: int
    Release157: int
    Release158: int
    Release159: int
    Release16: int
    Release160: int
    Release17: int
    Release18: int
    Release19: int
    Release2: int
    Release20: int
    Release2010Max: int
    Release2010Newest: int
    Release21: int
    Release22: int
    Release23: int
    Release24: int
    Release25: int
    Release26: int
    Release27: int
    Release28: int
    Release29: int
    Release3: int
    Release30: int
    Release31: int
    Release32: int
    Release33: int
    Release34: int
    Release35: int
    Release36: int
    Release37: int
    Release38: int
    Release39: int
    Release4: int
    Release40: int
    Release41: int
    Release42: int
    Release43: int
    Release44: int
    Release45: int
    Release46: int
    Release47: int
    Release48: int
    Release49: int
    Release5: int
    Release50: int
    Release51: int
    Release52: int
    Release53: int
    Release54: int
    Release55: int
    Release56: int
    Release57: int
    Release58: int
    Release59: int
    Release6: int
    Release60: int
    Release61: int
    Release62: int
    Release63: int
    Release64: int
    Release65: int
    Release66: int
    Release67: int
    Release68: int
    Release69: int
    Release7: int
    Release70: int
    Release71: int
    Release72: int
    Release73: int
    Release74: int
    Release75: int
    Release76: int
    Release77: int
    Release78: int
    Release79: int
    Release8: int
    Release80: int
    Release81: int
    Release82: int
    Release83: int
    Release84: int
    Release85: int
    Release86: int
    Release87: int
    Release88: int
    Release89: int
    Release9: int
    Release90: int
    Release91: int
    Release92: int
    Release93: int
    Release94: int
    Release95: int
    Release96: int
    Release97: int
    Release98: int
    Release99: int
    ReleaseCurrent: int
    ReleaseKnown: int
    ReleaseMax: int
    value__: int
class MatchProperties(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def CopyProperties(self, sourceEntity: Entity, targetEntity: Entity, flag: int):...
class Material(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Ambient(self) -> _n_3_t_17:"""Ambient { get; set; } -> MaterialColor"""
    @property
    def Anonymous(self) -> bool:"""Anonymous { get; set; } -> bool"""
    @property
    def Bump(self) -> _n_3_t_18:"""Bump { get; set; } -> MaterialMap"""
    @property
    def ChannelFlags(self) -> _n_3_t_19:"""ChannelFlags { get; set; } -> ChannelFlags"""
    @property
    def ColorBleedScale(self) -> float:"""ColorBleedScale { get; set; } -> float"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def Diffuse(self) -> _n_3_t_20:"""Diffuse { get; set; } -> MaterialDiffuseComponent"""
    @property
    def FinalGather(self) -> _n_3_t_21:"""FinalGather { get; set; } -> FinalGatherMode"""
    @property
    def GlobalIllumination(self) -> _n_3_t_22:"""GlobalIllumination { get; set; } -> GlobalIlluminationMode"""
    @property
    def IlluminationModel(self) -> _n_3_t_23:"""IlluminationModel { get; set; } -> IlluminationModel"""
    @property
    def IndirectBumpScale(self) -> float:"""IndirectBumpScale { get; set; } -> float"""
    @property
    def Luminance(self) -> float:"""Luminance { get; set; } -> float"""
    @property
    def LuminanceMode(self) -> _n_3_t_24:"""LuminanceMode { get; set; } -> LuminanceMode"""
    @property
    def Mode(self) -> _n_3_t_25:"""Mode { get; set; } -> Mode"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NormalMap(self) -> _n_3_t_26:"""NormalMap { get; set; } -> MaterialNormalMapComponent"""
    @property
    def Opacity(self) -> _n_3_t_27:"""Opacity { get; set; } -> MaterialOpacityComponent"""
    @property
    def ReflectanceScale(self) -> float:"""ReflectanceScale { get; set; } -> float"""
    @property
    def Reflection(self) -> _n_3_t_18:"""Reflection { get; set; } -> MaterialMap"""
    @property
    def Reflectivity(self) -> float:"""Reflectivity { get; set; } -> float"""
    @property
    def Refraction(self) -> _n_3_t_28:"""Refraction { get; set; } -> MaterialRefractionComponent"""
    @property
    def SelfIllumination(self) -> float:"""SelfIllumination { get; set; } -> float"""
    @property
    def Specular(self) -> _n_3_t_29:"""Specular { get; set; } -> MaterialSpecularComponent"""
    @property
    def Translucence(self) -> float:"""Translucence { get; set; } -> float"""
    @property
    def TransmittanceScale(self) -> float:"""TransmittanceScale { get; set; } -> float"""
    @property
    def TwoSided(self) -> bool:"""TwoSided { get; set; } -> bool"""
    def __init__(self) -> Material:...
class MeasurementValue(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    English: int
    Metric: int
    value__: int
class MentalRayRenderSettings(RenderSettings, _n_6_t_0, _n_6_t_1):
    @property
    def DiagnosticBSPMode(self) -> _n_3_t_30:"""DiagnosticBSPMode { get; set; } -> DiagnosticBSPMode"""
    @property
    def DiagnosticGridMode(self) -> _n_3_t_31:"""DiagnosticGridMode { get; set; } -> MentalRayRenderSettingsTraitsDiagnosticGridModeParameter"""
    @property
    def DiagnosticMode(self) -> _n_3_t_32:"""DiagnosticMode { get; set; } -> DiagnosticMode"""
    @property
    def DiagnosticPhotonMode(self) -> _n_3_t_33:"""DiagnosticPhotonMode { get; set; } -> DiagnosticPhotonMode"""
    @property
    def EnergyMultiplier(self) -> float:"""EnergyMultiplier { get; set; } -> float"""
    @property
    def ExportMIEnabled(self) -> bool:"""ExportMIEnabled { get; set; } -> bool"""
    @property
    def ExportMIFileName(self) -> str:"""ExportMIFileName { get; set; } -> str"""
    @property
    def FGRayCount(self) -> int:"""FGRayCount { get; set; } -> int"""
    @property
    def FGSampleRadius(self) -> _n_3_t_34:"""FGSampleRadius { get; set; } -> MentalRayRenderSettingsTraitsDoubleRangeParameter"""
    @property
    def FGSampleRadiusState(self) -> _n_3_t_35:"""FGSampleRadiusState { get; set; } -> MentalRayRenderSettingsTraitsBoolParameter"""
    @property
    def FinalGatheringEnabled(self) -> bool:"""FinalGatheringEnabled { get; set; } -> bool"""
    @property
    def FinalGatheringMode(self) -> _n_3_t_36:"""FinalGatheringMode { get; set; } -> FinalGatheringMode"""
    @property
    def GIPhotonsPerLight(self) -> int:"""GIPhotonsPerLight { get; set; } -> int"""
    @property
    def GISampleCount(self) -> int:"""GISampleCount { get; set; } -> int"""
    @property
    def GISampleRadius(self) -> float:"""GISampleRadius { get; set; } -> float"""
    @property
    def GISampleRadiusEnabled(self) -> bool:"""GISampleRadiusEnabled { get; set; } -> bool"""
    @property
    def GlobalIlluminationEnabled(self) -> bool:"""GlobalIlluminationEnabled { get; set; } -> bool"""
    @property
    def LightLuminanceScale(self) -> float:"""LightLuminanceScale { get; set; } -> float"""
    @property
    def MemoryLimit(self) -> int:"""MemoryLimit { get; set; } -> int"""
    @property
    def PhotonTraceDepth(self) -> _n_3_t_37:"""PhotonTraceDepth { get; set; } -> MentalRayRenderSettingsTraitsTraceParameter"""
    @property
    def RayTraceDepth(self) -> _n_3_t_37:"""RayTraceDepth { get; set; } -> MentalRayRenderSettingsTraitsTraceParameter"""
    @property
    def RayTracingEnabled(self) -> bool:"""RayTracingEnabled { get; set; } -> bool"""
    @property
    def Sampling(self) -> _n_3_t_38:"""Sampling { get; set; } -> MentalRayRenderSettingsTraitsIntegerRangeParameter"""
    @property
    def SamplingContrastColor(self) -> _n_3_t_39:"""SamplingContrastColor { get; set; } -> MentalRayRenderSettingsTraitsFloatParameter"""
    @property
    def SamplingFilter(self) -> _n_3_t_40:"""SamplingFilter { get; set; } -> MentalRayRenderSettingsTraitsSamplingParameter"""
    @property
    def ShadowMapsEnabled(self) -> bool:"""ShadowMapsEnabled { get; set; } -> bool"""
    @property
    def ShadowMode(self) -> _n_3_t_41:"""ShadowMode { get; set; } -> ShadowMode"""
    @property
    def ShadowSamplingMultiplier(self) -> ShadowSamplingMultiplier:"""ShadowSamplingMultiplier { get; set; } -> ShadowSamplingMultiplier"""
    @property
    def TileOrder(self) -> _n_3_t_42:"""TileOrder { get; set; } -> TileOrder"""
    @property
    def TileSize(self) -> int:"""TileSize { get; set; } -> int"""
    def __init__(self) -> MentalRayRenderSettings:...
class MergeCellStyleOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ConvertDuplicatesToOverrrides: int
    CopyDuplicates: int
    IgnoreNewStyles: int
    _None: int
    OverwriteDuplicates: int
    value__: int
class MeshDataCollection(_n_6_t_12):
    @property
    def ColorArray(self) -> _n_0_t_3:"""ColorArray { get; set; } -> EntityColorCollection"""
    @property
    def FaceArray(self) -> _n_2_t_24:"""FaceArray { get; set; } -> Int32Collection"""
    @property
    def MaterialIdArray(self) -> ObjectIdCollection:"""MaterialIdArray { get; set; } -> ObjectIdCollection"""
    @property
    def VertexArray(self) -> _n_2_t_10:"""VertexArray { get; set; } -> Point3dCollection"""
    def __init__(self, pts: _n_2_t_10, faces: _n_2_t_24, colors: _n_0_t_3, materialIds: ObjectIdCollection) -> MeshDataCollection:...
class MeshFaceterData(_n_6_t_12):
    @property
    def FaceterDevNormal(self) -> float:"""FaceterDevNormal { get; set; } -> float"""
    @property
    def FaceterDevSurface(self) -> float:"""FaceterDevSurface { get; set; } -> float"""
    @property
    def FaceterGridRatio(self) -> float:"""FaceterGridRatio { get; set; } -> float"""
    @property
    def FaceterMaxEdgeLength(self) -> float:"""FaceterMaxEdgeLength { get; set; } -> float"""
    @property
    def FaceterMaxGrid(self) -> _n_6_t_23:"""FaceterMaxGrid { get; set; } -> UInt16"""
    @property
    def FaceterMeshType(self) -> int:"""FaceterMeshType { get; set; } -> int"""
    @property
    def FaceterMinUGrid(self) -> _n_6_t_23:"""FaceterMinUGrid { get; set; } -> UInt16"""
    @property
    def FaceterMinVGrid(self) -> _n_6_t_23:"""FaceterMinVGrid { get; set; } -> UInt16"""
    def __init__(self, surface: float, normal: float, gRatio: float, eLength: float, numGrid: _n_6_t_23, uGrid: _n_6_t_23, vGrid: _n_6_t_23, mType: int) -> MeshFaceterData:...
class MeshPointMap(_n_6_t_12):
    @property
    def DestPoint(self) -> _n_2_t_0:"""DestPoint { get; set; } -> Point2d"""
    @property
    def SourcePoint(self) -> _n_2_t_0:"""SourcePoint { get; set; } -> Point2d"""
    def __init__(self, sourcePt: _n_2_t_0, destPt: _n_2_t_0) -> MeshPointMap:...
class MeshPointMaps(_n_6_t_12):
    @property
    def DestPonints(self) -> _n_2_t_18:"""DestPonints { get; set; } -> Point2dCollection"""
    @property
    def SourcePonints(self) -> _n_2_t_18:"""SourcePonints { get; set; } -> Point2dCollection"""
    def __init__(self, sourcePts: _n_2_t_18, destPts: _n_2_t_18) -> MeshPointMaps:...
class MidPointConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> MidPointConstraint:...
class MInsertBlock(BlockReference, _n_6_t_0, _n_6_t_1):
    @property
    def Columns(self) -> int:"""Columns { get; set; } -> int"""
    @property
    def ColumnSpacing(self) -> float:"""ColumnSpacing { get; set; } -> float"""
    @property
    def Rows(self) -> int:"""Rows { get; set; } -> int"""
    @property
    def RowSpacing(self) -> float:"""RowSpacing { get; set; } -> float"""
    def __init__(self, position: _n_2_t_1, blockTableRecord: ObjectId, columns: int, rows: int, colSpacing: float, rowSpacing: float) -> MInsertBlock:...
    def __init__(self) -> MInsertBlock:...
class MLeader(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def ArrowSize(self) -> float:"""ArrowSize { get; set; } -> float"""
    @property
    def ArrowSymbolId(self) -> ObjectId:"""ArrowSymbolId { get; set; } -> ObjectId"""
    @property
    def BlockColor(self) -> _n_0_t_0:"""BlockColor { get; set; } -> Color"""
    @property
    def BlockConnectionType(self) -> BlockConnectionType:"""BlockConnectionType { get; set; } -> BlockConnectionType"""
    @property
    def BlockContentId(self) -> ObjectId:"""BlockContentId { get; set; } -> ObjectId"""
    @property
    def BlockPosition(self) -> _n_2_t_1:"""BlockPosition { get; set; } -> Point3d"""
    @property
    def BlockRotation(self) -> float:"""BlockRotation { get; set; } -> float"""
    @property
    def BlockScale(self) -> _n_2_t_11:"""BlockScale { get; set; } -> Scale3d"""
    @property
    def ContentType(self) -> ContentType:"""ContentType { get; set; } -> ContentType"""
    @property
    def DoglegLength(self) -> float:"""DoglegLength { get; set; } -> float"""
    @property
    def EnableAnnotationScale(self) -> bool:"""EnableAnnotationScale { get; set; } -> bool"""
    @property
    def EnableDogleg(self) -> bool:"""EnableDogleg { get; set; } -> bool"""
    @property
    def EnableFrameText(self) -> bool:"""EnableFrameText { get; set; } -> bool"""
    @property
    def EnableLanding(self) -> bool:"""EnableLanding { get; set; } -> bool"""
    @property
    def ExtendLeaderToText(self) -> bool:"""ExtendLeaderToText { get; set; } -> bool"""
    @property
    def LandingGap(self) -> float:"""LandingGap { get; set; } -> float"""
    @property
    def LeaderCount(self) -> int:"""LeaderCount { get; } -> int"""
    @property
    def LeaderLineColor(self) -> _n_0_t_0:"""LeaderLineColor { get; set; } -> Color"""
    @property
    def LeaderLineCount(self) -> int:"""LeaderLineCount { get; } -> int"""
    @property
    def LeaderLineType(self) -> LeaderType:"""LeaderLineType { get; set; } -> LeaderType"""
    @property
    def LeaderLineTypeId(self) -> ObjectId:"""LeaderLineTypeId { get; set; } -> ObjectId"""
    @property
    def LeaderLineWeight(self) -> LineWeight:"""LeaderLineWeight { get; set; } -> LineWeight"""
    @property
    def MLeaderStyle(self) -> ObjectId:"""MLeaderStyle { get; set; } -> ObjectId"""
    @property
    def MText(self) -> MText:"""MText { get; set; } -> MText"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def TextAlignmentType(self) -> TextAlignmentType:"""TextAlignmentType { get; set; } -> TextAlignmentType"""
    @property
    def TextAngleType(self) -> TextAngleType:"""TextAngleType { get; set; } -> TextAngleType"""
    @property
    def TextAttachmentDirection(self) -> TextAttachmentDirection:"""TextAttachmentDirection { get; set; } -> TextAttachmentDirection"""
    @property
    def TextAttachmentType(self) -> TextAttachmentType:"""TextAttachmentType { get; set; } -> TextAttachmentType"""
    @property
    def TextColor(self) -> _n_0_t_0:"""TextColor { get; set; } -> Color"""
    @property
    def TextHeight(self) -> float:"""TextHeight { get; set; } -> float"""
    @property
    def TextLocation(self) -> _n_2_t_1:"""TextLocation { get; set; } -> Point3d"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    @property
    def ToleranceLocation(self) -> _n_2_t_1:"""ToleranceLocation { get; set; } -> Point3d"""
    def __init__(self) -> MLeader:...
    def AddFirstVertex(self, leaderLineIndex: int, point: _n_2_t_1):...
    def AddLastVertex(self, leaderLineIndex: int, point: _n_2_t_1):...
    def AddLeader(self) -> int:...
    def AddLeaderLine(self, point: _n_2_t_1) -> int:...
    def AddLeaderLine(self, leaderIndex: int) -> int:...
    def ConnectionPoint(self, direction: _n_2_t_3, textAttachmentDirection: TextAttachmentDirection) -> _n_2_t_1:...
    def ConnectionPoint(self, direction: _n_2_t_3) -> _n_2_t_1:...
    def GetArrowSize(self, leaderLineIndex: int) -> float:...
    def GetArrowSymbolId(self, leaderLineIndex: int) -> ObjectId:...
    def GetBlockAttribute(self, attDefId: ObjectId) -> AttributeReference:...
    def GetContentGeomExtents(self) -> Extents3d:...
    def getContextDataManager(self) -> _n_6_t_3:...
    def GetDogleg(self, leaderIndex: int) -> _n_2_t_3:...
    def GetDoglegLength(self, leaderIndex: int) -> float:...
    def GetFirstVertex(self, leaderLineIndex: int) -> _n_2_t_1:...
    def GetLastVertex(self, leaderLineIndex: int) -> _n_2_t_1:...
    def GetLeaderIndex(self, leaderLineIndex: int) -> int:...
    def GetLeaderIndexes(self) -> _n_7_t_1:...
    def GetLeaderLineColor(self, leaderLineIndex: int) -> _n_0_t_0:...
    def GetLeaderLineIndexes(self, leaderIndex: int) -> _n_7_t_1:...
    def GetLeaderLineType(self, leaderLineIndex: int) -> LeaderType:...
    def GetLeaderLineTypeId(self, leaderLineIndex: int) -> ObjectId:...
    def GetLeaderLineWeight(self, leaderLineIndex: int) -> LineWeight:...
    def getOverridedMLeaderStyle(self, mleaderStyle: MLeaderStyle):...
    def GetTextAttachmentType(self, leaderDirection: LeaderDirectionType) -> TextAttachmentType:...
    def GetVertex(self, leaderLineIndex: int, index: int) -> _n_2_t_1:...
    def HasContent(self) -> bool:...
    def MoveMLeader(self, vec: _n_2_t_3, type: MoveType):...
    def PostMLeaderToDb(self, db: Database):...
    def recomputeBreakPoints(self):...
    def RemoveFirstVertex(self, leaderLineIndex: int):...
    def RemoveLastVertex(self, leaderLineIndex: int):...
    def RemoveLeader(self, index: int):...
    def RemoveLeaderLine(self, leaderLineIndex: int):...
    def SetArrowSize(self, leaderLineIndex: int, arrowSize: float):...
    def SetArrowSymbolId(self, leaderLineIndex: int, id: ObjectId):...
    def SetBlockAttribute(self, attDefId: ObjectId, attributeValue: AttributeReference):...
    def SetContextDataManager(self, contextDataManager: _n_6_t_3):...
    def SetDogleg(self, leaderIndex: int, vector: _n_2_t_3):...
    def SetDoglegLength(self, leaderIndex: int, doglegLength: float):...
    def SetFirstVertex(self, leaderLineIndex: int, point: _n_2_t_1):...
    def SetLastVertex(self, leaderLineIndex: int, point: _n_2_t_1):...
    def SetLeaderLineColor(self, leaderLineIndex: int, leaderLineTypeId: _n_0_t_0):...
    def SetLeaderLineType(self, leaderLineIndex: int, leaderLineType: LeaderType):...
    def SetLeaderLineTypeId(self, leaderLineIndex: int, leaderLineTypeId: ObjectId):...
    def SetLeaderLineWeight(self, leaderLineIndex: int, leaderLineWeight: LineWeight):...
    def SetPlane(self, value: _n_2_t_4):...
    def SetTextAttachmentType(self, textAttachmentType: TextAttachmentType, leaderDirection: LeaderDirectionType):...
    def SetVertex(self, leaderLineIndex: int, index: int, point: _n_2_t_1):...
    def VerticesCount(self, leaderLineIndex: int) -> int:...
class MLeaderStyle(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ArrowSize(self) -> float:"""ArrowSize { get; set; } -> float"""
    @property
    def ArrowSymbolId(self) -> ObjectId:"""ArrowSymbolId { get; set; } -> ObjectId"""
    @property
    def BlockColor(self) -> _n_0_t_0:"""BlockColor { get; set; } -> Color"""
    @property
    def BlockConnectionType(self) -> BlockConnectionType:"""BlockConnectionType { get; set; } -> BlockConnectionType"""
    @property
    def BlockId(self) -> ObjectId:"""BlockId { get; set; } -> ObjectId"""
    @property
    def BlockRotation(self) -> float:"""BlockRotation { get; set; } -> float"""
    @property
    def BlockScale(self) -> _n_2_t_11:"""BlockScale { get; set; } -> Scale3d"""
    @property
    def BreakSize(self) -> float:"""BreakSize { get; set; } -> float"""
    @property
    def ContentType(self) -> ContentType:"""ContentType { get; set; } -> ContentType"""
    @property
    def DefaultMText(self) -> MText:"""DefaultMText { get; set; } -> MText"""
    @property
    def DoglegLength(self) -> float:"""DoglegLength { get; set; } -> float"""
    @property
    def DrawLeaderOrderType(self) -> DrawLeaderOrderType:"""DrawLeaderOrderType { get; set; } -> DrawLeaderOrderType"""
    @property
    def DrawMLeaderOrderType(self) -> DrawMLeaderOrderType:"""DrawMLeaderOrderType { get; set; } -> DrawMLeaderOrderType"""
    @property
    def EnableBlockRotation(self) -> bool:"""EnableBlockRotation { get; set; } -> bool"""
    @property
    def EnableBlockScale(self) -> bool:"""EnableBlockScale { get; set; } -> bool"""
    @property
    def EnableDogleg(self) -> bool:"""EnableDogleg { get; set; } -> bool"""
    @property
    def EnableFrameText(self) -> bool:"""EnableFrameText { get; set; } -> bool"""
    @property
    def EnableLanding(self) -> bool:"""EnableLanding { get; set; } -> bool"""
    @property
    def ExtendLeaderToText(self) -> bool:"""ExtendLeaderToText { get; set; } -> bool"""
    @property
    def FirstSegmentAngleConstraint(self) -> AngleConstraint:"""FirstSegmentAngleConstraint { get; set; } -> AngleConstraint"""
    @property
    def LandingGap(self) -> float:"""LandingGap { get; set; } -> float"""
    @property
    def LeaderLineColor(self) -> _n_0_t_0:"""LeaderLineColor { get; set; } -> Color"""
    @property
    def LeaderLineType(self) -> LeaderType:"""LeaderLineType { get; set; } -> LeaderType"""
    @property
    def LeaderLineTypeId(self) -> ObjectId:"""LeaderLineTypeId { get; set; } -> ObjectId"""
    @property
    def LeaderLineWeight(self) -> LineWeight:"""LeaderLineWeight { get; set; } -> LineWeight"""
    @property
    def MaxLeaderSegmentsPoints(self) -> int:"""MaxLeaderSegmentsPoints { get; set; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def SecondSegmentAngleConstraint(self) -> AngleConstraint:"""SecondSegmentAngleConstraint { get; set; } -> AngleConstraint"""
    @property
    def TextAlignAlwaysLeft(self) -> bool:"""TextAlignAlwaysLeft { get; set; } -> bool"""
    @property
    def TextAlignmentType(self) -> TextAlignmentType:"""TextAlignmentType { get; set; } -> TextAlignmentType"""
    @property
    def TextAngleType(self) -> TextAngleType:"""TextAngleType { get; set; } -> TextAngleType"""
    @property
    def TextAttachmentDirection(self) -> TextAttachmentDirection:"""TextAttachmentDirection { get; set; } -> TextAttachmentDirection"""
    @property
    def TextAttachmentType(self) -> TextAttachmentType:"""TextAttachmentType { get; set; } -> TextAttachmentType"""
    @property
    def TextColor(self) -> _n_0_t_0:"""TextColor { get; set; } -> Color"""
    @property
    def TextHeight(self) -> float:"""TextHeight { get; set; } -> float"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    def __init__(self, mleaderStyle: MLeaderStyle) -> MLeaderStyle:...
    def __init__(self) -> MLeaderStyle:...
    def GetTextAttachmentType(self, leaderDirection: LeaderDirectionType) -> TextAttachmentType:...
    def OverwritePropChanged(self) -> bool:...
    def PostMLeaderStyleToDb(self, db: Database, styleName: str) -> ObjectId:...
    def SetTextAttachmentType(self, textAttachmentType: TextAttachmentType, leaderDirection: LeaderDirectionType):...
class Mline(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def IsClosed(self) -> bool:"""IsClosed { get; set; } -> bool"""
    @property
    def Justification(self) -> MlineJustification:"""Justification { get; set; } -> MlineJustification"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def NumberOfVertices(self) -> int:"""NumberOfVertices { get; } -> int"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def Style(self) -> ObjectId:"""Style { get; set; } -> ObjectId"""
    @property
    def SupressEndCaps(self) -> bool:"""SupressEndCaps { get; set; } -> bool"""
    @property
    def SupressStartCaps(self) -> bool:"""SupressStartCaps { get; set; } -> bool"""
    def __init__(self) -> Mline:...
    def AppendSegment(self, newVertex: _n_2_t_1):...
    def Element(self, pt: _n_2_t_1) -> int:...
    def GetClosestPointTo(self, givenPoint: _n_2_t_1, normal: _n_2_t_3, extend: bool, excludeCaps: bool) -> _n_2_t_1:...
    def GetClosestPointTo(self, givenPoint: _n_2_t_1, extend: bool, excludeCaps: bool) -> _n_2_t_1:...
    def MoveVertexAt(self, index: int, newPosition: _n_2_t_1):...
    def RemoveLastSegment(self, lastVertex: _n_2_t_1):...
    def VertexAt(self, index: int) -> _n_2_t_1:...
class MlineJustification(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Bottom: int
    Top: int
    value__: int
    Zero: int
class MlineStyle(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def Elements(self) -> MlineStyleElementCollection:"""Elements { get; } -> MlineStyleElementCollection"""
    @property
    def EndAngle(self) -> float:"""EndAngle { get; set; } -> float"""
    @property
    def EndInnerArcs(self) -> bool:"""EndInnerArcs { get; set; } -> bool"""
    @property
    def EndRoundCap(self) -> bool:"""EndRoundCap { get; set; } -> bool"""
    @property
    def EndSquareCap(self) -> bool:"""EndSquareCap { get; set; } -> bool"""
    @property
    def FillColor(self) -> _n_0_t_0:"""FillColor { get; set; } -> Color"""
    @property
    def Filled(self) -> bool:"""Filled { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ShowMiters(self) -> bool:"""ShowMiters { get; set; } -> bool"""
    @property
    def StartAngle(self) -> float:"""StartAngle { get; set; } -> float"""
    @property
    def StartInnerArcs(self) -> bool:"""StartInnerArcs { get; set; } -> bool"""
    @property
    def StartRoundCap(self) -> bool:"""StartRoundCap { get; set; } -> bool"""
    @property
    def StartSquareCap(self) -> bool:"""StartSquareCap { get; set; } -> bool"""
    def __init__(self) -> MlineStyle:...
    def Reset(self):...
    def Set(self, source: MlineStyle, checkIfReferenced: bool):...
class MlineStyleElement(_n_6_t_12):
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; } -> Color"""
    @property
    def LinetypeId(self) -> ObjectId:"""LinetypeId { get; } -> ObjectId"""
    @property
    def Offset(self) -> float:"""Offset { get; } -> float"""
    def __init__(self, offset: float, color: _n_0_t_0, linetypeId: ObjectId) -> MlineStyleElement:...
class MlineStyleElementCollection(_n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> MlineStyleElement:"""Item { get; set; } -> MlineStyleElement"""
    def Add(self, element: MlineStyleElement, checkIfReferenced: bool) -> int:...
    def RemoveAt(self, index: int):...
class MlineStyleElementCollectionEnumerator(_n_7_t_3):
    def __init__(self, col: MlineStyleElementCollection) -> MlineStyleElementCollectionEnumerator:...
class ModelDocViewLabelAlignmentType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AlignmentCenter: int
    AlignmentLeft: int
    AlignmentRight: int
    value__: int
class ModelDocViewLabelAttachmentPoint(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AboveView: int
    BelowView: int
    value__: int
class ModelerFlavor(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Full: int
    ObjectsOnly: int
    RegionsOnly: int
    value__: int
class ModifiesOwnerAttribute(_n_6_t_15, _n_14_t_0):
    def __init__(self) -> ModifiesOwnerAttribute:...
class MoveGripPointsFlags(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Keyboard: int
    ObjectTrack: int
    Osnapped: int
    Polar: int
    value__: int
    ZDir: int
class MoveType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    MoveAllExceptArrowHeaderPoints: int
    MoveAllPoints: int
    MoveContentAndDoglegPoints: int
    value__: int
class MText(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def ActualHeight(self) -> float:"""ActualHeight { get; } -> float"""
    @property
    def ActualWidth(self) -> float:"""ActualWidth { get; } -> float"""
    @property
    def AlignChange(self) -> str:"""AlignChange { get; } -> str"""
    @property
    def Ascent(self) -> float:"""Ascent { get; } -> float"""
    @property
    def Attachment(self) -> AttachmentPoint:"""Attachment { get; set; } -> AttachmentPoint"""
    @property
    def BackgroundFill(self) -> bool:"""BackgroundFill { get; set; } -> bool"""
    @property
    def BackgroundFillColor(self) -> _n_0_t_0:"""BackgroundFillColor { get; set; } -> Color"""
    @property
    def BackgroundScaleFactor(self) -> float:"""BackgroundScaleFactor { get; set; } -> float"""
    @property
    def BackgroundTransparency(self) -> _n_0_t_1:"""BackgroundTransparency { get; set; } -> Transparency"""
    @property
    def BlockBegin(self) -> str:"""BlockBegin { get; } -> str"""
    @property
    def BlockEnd(self) -> str:"""BlockEnd { get; } -> str"""
    @property
    def ColorChange(self) -> str:"""ColorChange { get; } -> str"""
    @property
    def ColumnAutoHeight(self) -> bool:"""ColumnAutoHeight { get; set; } -> bool"""
    @property
    def ColumnCount(self) -> int:"""ColumnCount { get; set; } -> int"""
    @property
    def ColumnFlowReversed(self) -> bool:"""ColumnFlowReversed { get; set; } -> bool"""
    @property
    def ColumnGutterWidth(self) -> float:"""ColumnGutterWidth { get; set; } -> float"""
    @property
    def ColumnType(self) -> ColumnType:"""ColumnType { get; set; } -> ColumnType"""
    @property
    def ColumnWidth(self) -> float:"""ColumnWidth { get; set; } -> float"""
    @property
    def Contents(self) -> str:"""Contents { get; set; } -> str"""
    @property
    def ContentsRTF(self) -> str:"""ContentsRTF { get; set; } -> str"""
    @property
    def Descent(self) -> float:"""Descent { get; } -> float"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; set; } -> Vector3d"""
    @property
    def FlowDirection(self) -> FlowDirection:"""FlowDirection { get; set; } -> FlowDirection"""
    @property
    def FontChange(self) -> str:"""FontChange { get; } -> str"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def HeightChange(self) -> str:"""HeightChange { get; } -> str"""
    @property
    def LineBreak(self) -> str:"""LineBreak { get; } -> str"""
    @property
    def LineSpaceDistance(self) -> float:"""LineSpaceDistance { get; set; } -> float"""
    @property
    def LineSpacingFactor(self) -> float:"""LineSpacingFactor { get; set; } -> float"""
    @property
    def LineSpacingStyle(self) -> LineSpacingStyle:"""LineSpacingStyle { get; set; } -> LineSpacingStyle"""
    @property
    def Location(self) -> _n_2_t_1:"""Location { get; set; } -> Point3d"""
    @property
    def NonBreakSpace(self) -> str:"""NonBreakSpace { get; } -> str"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def ObliqueChange(self) -> str:"""ObliqueChange { get; } -> str"""
    @property
    def OverlineOff(self) -> str:"""OverlineOff { get; } -> str"""
    @property
    def OverlineOn(self) -> str:"""OverlineOn { get; } -> str"""
    @property
    def ParagraphBreak(self) -> str:"""ParagraphBreak { get; } -> str"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def ShowBorders(self) -> bool:"""ShowBorders { get; set; } -> bool"""
    @property
    def StackStart(self) -> str:"""StackStart { get; } -> str"""
    @property
    def StrikethroughOff(self) -> str:"""StrikethroughOff { get; } -> str"""
    @property
    def StrikethroughOn(self) -> str:"""StrikethroughOn { get; } -> str"""
    @property
    def Text(self) -> str:"""Text { get; } -> str"""
    @property
    def TextHeight(self) -> float:"""TextHeight { get; set; } -> float"""
    @property
    def TextStyleId(self) -> ObjectId:"""TextStyleId { get; set; } -> ObjectId"""
    @property
    def TextStyleName(self) -> str:"""TextStyleName { get; } -> str"""
    @property
    def TrackChange(self) -> str:"""TrackChange { get; } -> str"""
    @property
    def UnderlineOff(self) -> str:"""UnderlineOff { get; } -> str"""
    @property
    def UnderlineOn(self) -> str:"""UnderlineOn { get; } -> str"""
    @property
    def UseBackgroundColor(self) -> bool:"""UseBackgroundColor { get; set; } -> bool"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
    @property
    def WidthChange(self) -> str:"""WidthChange { get; } -> str"""
    def __init__(self) -> MText:...
    def ConvertFieldToText(self):...
    def CorrectSpelling(self) -> int:...
    def ExplodeFragments(self, enumerator: MTextFragmentCallback):...
    def ExplodeFragments(self, enumerator: MTextFragmentCallback, userData: object):...
    def ExplodeFragments(self, enumerator: MTextFragmentCallback, userData: object, context: _n_3_t_9):...
    def GetBoundingPoints(self) -> _n_2_t_10:...
    def GetColumnHeight(self, index: int) -> float:...
    def getMTextWithFieldCodes(self) -> str:...
    def SetAttachmentMovingLocation(self, value: AttachmentPoint):...
    def SetColumnHeight(self, index: int, height: float):...
    def SetContentsRtf(self, value: str) -> int:...
    def SetDynamicColumns(self, width: float, gutter: float, auto_height: bool):...
    def SetStaticColumns(self, width: float, gutter: float, count: int):...
class MTextFragment(_n_5_t_3, _n_6_t_0):
    @property
    def BigFont(self) -> str:"""BigFont { get; } -> str"""
    @property
    def Bold(self) -> bool:"""Bold { get; } -> bool"""
    @property
    def CapsHeight(self) -> float:"""CapsHeight { get; } -> float"""
    @property
    def Color(self) -> _n_0_t_2:"""Color { get; } -> EntityColor"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; } -> Vector3d"""
    @property
    def Extents(self) -> _n_2_t_0:"""Extents { get; } -> Point2d"""
    @property
    def Italic(self) -> bool:"""Italic { get; } -> bool"""
    @property
    def Location(self) -> _n_2_t_1:"""Location { get; } -> Point3d"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def ObliqueAngle(self) -> float:"""ObliqueAngle { get; } -> float"""
    @property
    def Overlined(self) -> bool:"""Overlined { get; } -> bool"""
    @property
    def ShxFont(self) -> str:"""ShxFont { get; } -> str"""
    @property
    def StackBottom(self) -> bool:"""StackBottom { get; } -> bool"""
    @property
    def StackTop(self) -> bool:"""StackTop { get; } -> bool"""
    @property
    def Strikethrough(self) -> bool:"""Strikethrough { get; } -> bool"""
    @property
    def Text(self) -> str:"""Text { get; } -> str"""
    @property
    def TrackingFactor(self) -> float:"""TrackingFactor { get; } -> float"""
    @property
    def TrueTypeFont(self) -> str:"""TrueTypeFont { get; } -> str"""
    @property
    def Underlined(self) -> bool:"""Underlined { get; } -> bool"""
    @property
    def WidthFactor(self) -> float:"""WidthFactor { get; } -> float"""
    def GetOverLinePoints(self) -> _n_6_t_10[_n_2_t_1]:...
    def GetStrikethroughPoints(self) -> _n_6_t_10[_n_2_t_1]:...
    def GetUnderLinePoints(self) -> _n_6_t_10[_n_2_t_1]:...
class MTextFragmentCallback(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> MTextFragmentCallback:...
    def BeginInvoke(self, __unnamed000: MTextFragment, __unnamed001: object, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4) -> MTextFragmentCallbackStatus:...
    def Invoke(self, A_0: MTextFragment, A_1: object) -> MTextFragmentCallbackStatus:...
class MTextFragmentCallbackStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Continue: int
    Terminate: int
    value__: int
class MultiModesGripPE(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> MultiModesGripPE:...
    def CurrentMode(self, entity: Entity, gripData: GripData) -> GripMode:...
    def CurrentModeId(self, entity: Entity, gripData: GripData) -> _n_6_t_11:...
    def GetGripModes(self, entity: Entity, gripData: GripData, modes: GripModeCollection, curMode: _n_6_t_11) -> bool:...
    def GetGripType(self, entity: Entity, gripData: GripData) -> MultiModesGripPE.GripType:...
    def Reset(self, entity: Entity):...
    def SetCurrentMode(self, entity: Entity, gripData: GripData, curMode: _n_6_t_11) -> bool:...
    class GripType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Primary: int
        Secondary: int
        value__: int
class NewLayerNotification(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    NoNewLayerNotification: int
    NotifyOnInsert: int
    NotifyOnLayerStateRestore: int
    NotifyOnOpen: int
    NotifyOnPlot: int
    NotifyOnSave: int
    NotifyOnXrefAttachAndReload: int
    value__: int
class NormalConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> NormalConstraint:...
class Notifier(_n_10_t_2):
    def __init__(self) -> Notifier:...
    def OnPropertyChanged(self, propertyName: str):...
class NurbsData(_n_6_t_12):
    @property
    def Closed(self) -> bool:"""Closed { get; } -> bool"""
    @property
    def ControlPointTolerance(self) -> float:"""ControlPointTolerance { get; } -> float"""
    @property
    def Degree(self) -> int:"""Degree { get; } -> int"""
    @property
    def KnotTolerance(self) -> float:"""KnotTolerance { get; } -> float"""
    @property
    def Periodic(self) -> bool:"""Periodic { get; } -> bool"""
    @property
    def Rational(self) -> bool:"""Rational { get; } -> bool"""
    def GetControlPoints(self) -> _n_2_t_10:...
    def GetKnots(self) -> _n_2_t_13:...
    def GetWeights(self) -> _n_2_t_13:...
    def IsEqualTo(self, other: NurbsData) -> bool:...
    def IsEqualTo(self, other: NurbsData, tolerance: _n_2_t_5) -> bool:...
class NurbSurface(Surface, _n_6_t_0, _n_6_t_1):
    @property
    def ControlPoints(self) -> _n_2_t_10:"""ControlPoints { get; } -> Point3dCollection"""
    @property
    def DegreeInU(self) -> int:"""DegreeInU { get; } -> int"""
    @property
    def DegreeInV(self) -> int:"""DegreeInV { get; } -> int"""
    @property
    def IsClosedInU(self) -> bool:"""IsClosedInU { get; } -> bool"""
    @property
    def IsClosedInV(self) -> bool:"""IsClosedInV { get; } -> bool"""
    @property
    def IsPeriodicInU(self) -> bool:"""IsPeriodicInU { get; } -> bool"""
    @property
    def IsPeriodicInV(self) -> bool:"""IsPeriodicInV { get; } -> bool"""
    @property
    def IsRational(self) -> bool:"""IsRational { get; } -> bool"""
    @property
    def NumberOfControlPointsInU(self) -> int:"""NumberOfControlPointsInU { get; } -> int"""
    @property
    def NumberOfControlPointsInV(self) -> int:"""NumberOfControlPointsInV { get; } -> int"""
    @property
    def NumberOfKnotsInU(self) -> int:"""NumberOfKnotsInU { get; } -> int"""
    @property
    def NumberOfKnotsInV(self) -> int:"""NumberOfKnotsInV { get; } -> int"""
    @property
    def NumberOfSpansInU(self) -> int:"""NumberOfSpansInU { get; } -> int"""
    @property
    def NumberOfSpansInV(self) -> int:"""NumberOfSpansInV { get; } -> int"""
    @property
    def PeriodInU(self) -> float:"""PeriodInU { get; } -> float"""
    @property
    def PeriodInV(self) -> float:"""PeriodInV { get; } -> float"""
    @property
    def UKnots(self) -> _n_2_t_25:"""UKnots { get; } -> KnotCollection"""
    @property
    def VKnots(self) -> _n_2_t_25:"""VKnots { get; } -> KnotCollection"""
    def __init__(self, uDegree: int, vDegree: int, rational: bool, uNumControlPoints: int, vNumControlPoints: int, ctrlPts: _n_2_t_10, weights: _n_2_t_13, uKnots: _n_2_t_25, vKnots: _n_2_t_25) -> NurbSurface:...
    def __init__(self) -> NurbSurface:...
    def Evaluate(self, u: float, v: float, derivDegree: int, point: _n_2_t_1, derivatives: _n_2_t_9):...
    def Evaluate(self, u: float, v: float, pos: _n_2_t_1, uDeriv: _n_2_t_3, vDeriv: _n_2_t_3, uuDeriv: _n_2_t_3, uvDeriv: _n_2_t_3, vvDeriv: _n_2_t_3):...
    def Evaluate(self, u: float, v: float, pos: _n_2_t_1, uDeriv: _n_2_t_3, vDeriv: _n_2_t_3):...
    def Evaluate(self, u: float, v: float) -> _n_2_t_1:...
    def GetControlPointAt(self, uIndex: int, vIndex: int) -> _n_2_t_1:...
    def GetIsolineAtU(self, u: float) -> _n_6_t_10[Curve]:...
    def GetIsolineAtV(self, v: float) -> _n_6_t_10[Curve]:...
    def GetNormal(self, u: float, v: float) -> _n_2_t_3:...
    def GetParameterOfPoint(self, point: _n_2_t_1, u: float, v: float):...
    def GetWeight(self, uIndex: int, vIndex: int) -> float:...
    def InsertControlPointsAtU(self, u: float, vCtrlPts: _n_2_t_10, vWeights: _n_2_t_13):...
    def InsertControlPointsAtV(self, v: float, uCtrlPts: _n_2_t_10, uWeights: _n_2_t_13):...
    def InsertKnotAtU(self, u: float):...
    def InsertKnotAtV(self, v: float):...
    def IsPlanar(self, ptOnSurface: _n_2_t_1, normal: _n_2_t_3) -> bool:...
    def IsPointOnSurface(self, point: _n_2_t_1) -> bool:...
    def ModifyPosition(self, u: float, v: float, point: _n_2_t_1):...
    def ModifyPositionAndTangent(self, u: float, v: float, point: _n_2_t_1, uDeriv: _n_2_t_3, vDeriv: _n_2_t_3):...
    def Rebuild(self, uDegree: int, vDegree: int, numUCtrlPts: int, numVCtrlPts: int, bRestore: bool):...
    def Rebuild(self, uDegree: int, vDegree: int, numUCtrlPts: int, numVCtrlPts: int):...
    def RemoveControlPointsAtU(self, uIndex: int):...
    def RemoveControlPointsAtV(self, vIndex: int):...
    def Set(self, uDegree: int, vDegree: int, rational: bool, uNumControlPoints: int, vNumControlPoints: int, ctrlPts: _n_2_t_10, weights: _n_2_t_13, uKnots: _n_2_t_25, vKnots: _n_2_t_25):...
    def SetControlPointAt(self, uIndex: int, vIndex: int, point: _n_2_t_1):...
    def SetControlPoints(self, uCount: int, vCount: int, points: _n_2_t_10):...
    def SetWeight(self, uIndex: int, vIndex: int, weight: float):...
class ObjectClosedEventArgs(_n_6_t_13):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
class ObjectClosedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> ObjectClosedEventHandler:...
    def BeginInvoke(self, sender: object, e: ObjectClosedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: ObjectClosedEventArgs):...
class ObjectContext(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def CollectionName(self) -> str:"""CollectionName { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def UniqueIdentifier(self) -> _n_6_t_3:"""UniqueIdentifier { get; } -> IntPtr"""
class ObjectContextCollection(_n_5_t_2, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def CurrentContext(self) -> ObjectContext:"""CurrentContext { get; set; } -> ObjectContext"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def AddContext(self, ctxt: ObjectContext):...
    def GetContext(self, contextName: str) -> ObjectContext:...
    def HasContext(self, contextName: str) -> bool:...
    def RemoveContext(self, contextName: str):...
class ObjectContextCollectionEnumerator(_n_5_t_2, _n_6_t_0, _n_6_t_1, _n_7_t_3):
    pass
class ObjectContextManager(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> ObjectContextManager:...
    def GetContextCollection(self, collectionName: str) -> ObjectContextCollection:...
    def RegisterContextCollection(self, collectionName: str, collection: ObjectContextCollection):...
    def UnregisterContextCollection(self, collectionName: str):...
class ObjectErasedEventArgs(_n_6_t_13):
    @property
    def DBObject(self) -> DBObject:"""DBObject { get; } -> DBObject"""
    @property
    def Erased(self) -> bool:"""Erased { get; } -> bool"""
class ObjectErasedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> ObjectErasedEventHandler:...
    def BeginInvoke(self, sender: object, e: ObjectErasedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: ObjectErasedEventArgs):...
class ObjectEventArgs(_n_6_t_13):
    @property
    def DBObject(self) -> DBObject:"""DBObject { get; } -> DBObject"""
class ObjectEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> ObjectEventHandler:...
    def BeginInvoke(self, sender: object, e: ObjectEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: ObjectEventArgs):...
class ObjectId(_n_6_t_12, _n_6_t_7[ObjectId], _n_12_t_0):
    @property
    def Database(self) -> Database:"""Database { get; } -> Database"""
    @property
    def Handle(self) -> Handle:"""Handle { get; } -> Handle"""
    @property
    def IsEffectivelyErased(self) -> bool:"""IsEffectivelyErased { get; } -> bool"""
    @property
    def IsErased(self) -> bool:"""IsErased { get; } -> bool"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def IsResident(self) -> bool:"""IsResident { get; } -> bool"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def NonForwardedHandle(self) -> Handle:"""NonForwardedHandle { get; } -> Handle"""
    @property
    def Null(self) -> ObjectId:"""Null { get; } -> ObjectId"""
    @property
    def ObjectClass(self) -> _n_5_t_0:"""ObjectClass { get; } -> RXClass"""
    @property
    def ObjectLeftOnDisk(self) -> bool:"""ObjectLeftOnDisk { get; } -> bool"""
    @property
    def OldId(self) -> int:"""OldId { get; } -> int"""
    @property
    def OldIdPtr(self) -> _n_6_t_3:"""OldIdPtr { get; } -> IntPtr"""
    @property
    def OriginalDatabase(self) -> Database:"""OriginalDatabase { get; } -> Database"""
    def __init__(self, oldId: _n_6_t_3) -> ObjectId:...
    def Compare(self, value1: ObjectId) -> bool:...
    def ConvertToRedirectedId(self) -> ObjectId:...
    def GetObject(self, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject:...
    def GetObject(self, mode: OpenMode, openErased: bool) -> DBObject:...
    def GetObject(self, mode: OpenMode) -> DBObject:...
    def Open(self, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject:...
    def Open(self, mode: OpenMode, openErased: bool) -> DBObject:...
    def Open(self, mode: OpenMode) -> DBObject:...
class ObjectIdCollection(_n_5_t_3, _n_6_t_0, _n_7_t_5, typing.Iterable[typing.Any]):
    def __init__(self, values: _n_6_t_10[ObjectId]) -> ObjectIdCollection:...
    def __init__(self) -> ObjectIdCollection:...
class ObjectIdGraph(Graph, _n_6_t_0):
    def __init__(self) -> ObjectIdGraph:...
    def FindNode(self, id: ObjectId) -> ObjectIdGraphNode:...
    def IdNode(self, index: int) -> ObjectIdGraphNode:...
class ObjectIdGraphNode(GraphNode, _n_6_t_0):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    def __init__(self, id: ObjectId) -> ObjectIdGraphNode:...
class ObjectOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def Cancel(self, dbObject: DBObject):...
    def Close(self, dbObject: DBObject):...
    def DeepClone(self, dbObject: DBObject, ownerObject: DBObject, idMap: IdMapping, isPrimary: bool) -> DBObject:...
    def Erase(self, dbObject: DBObject, erasing: bool):...
    def Open(self, dbObject: DBObject, mode: OpenMode):...
    def WblockClone(self, dbObject: DBObject, ownerObject: _n_5_t_2, idMap: IdMapping, isPrimary: bool) -> DBObject:...
class ObjectSnapContext(object):
    @property
    def GraphicsSystemSelectionMark(self) -> int:"""GraphicsSystemSelectionMark { get; } -> int"""
    @property
    def LastPoint(self) -> _n_2_t_1:"""LastPoint { get; } -> Point3d"""
    @property
    def PickedObject(self) -> Entity:"""PickedObject { get; } -> Entity"""
    @property
    def PickPoint(self) -> _n_2_t_1:"""PickPoint { get; } -> Point3d"""
    @property
    def ViewTransform(self) -> _n_2_t_6:"""ViewTransform { get; } -> Matrix3d"""
class ObjectSnapInfo(object):
    @property
    def SnapCurves(self) -> _n_2_t_26:"""SnapCurves { get; } -> Curve3dCollection"""
    @property
    def SnapPoints(self) -> _n_2_t_10:"""SnapPoints { get; } -> Point3dCollection"""
class ObjectSnapModes(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ModeCenter: int
    ModeEnd: int
    ModeIns: int
    ModeMid: int
    ModeNear: int
    ModeNode: int
    ModePerpendicular: int
    ModeQuad: int
    ModeTangent: int
    value__: int
class ObjectTypeAttribute(_n_6_t_15, _n_14_t_0):
    @property
    def ObjectType(self) -> _n_6_t_25:"""ObjectType { get; } -> Type"""
    def __init__(self, type: _n_6_t_25) -> ObjectTypeAttribute:...
class Ole2Frame(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def AutoOutputQuality(self) -> _n_6_t_19:"""AutoOutputQuality { get; set; } -> Byte"""
    @property
    def IsLinked(self) -> bool:"""IsLinked { get; } -> bool"""
    @property
    def LinkName(self) -> str:"""LinkName { get; } -> str"""
    @property
    def LinkPath(self) -> str:"""LinkPath { get; } -> str"""
    @property
    def Location(self) -> _n_2_t_1:"""Location { get; } -> Point3d"""
    @property
    def LockAspect(self) -> bool:"""LockAspect { get; set; } -> bool"""
    @property
    def OleObject(self) -> object:"""OleObject { get; } -> object"""
    @property
    def OutputQuality(self) -> _n_6_t_19:"""OutputQuality { get; set; } -> Byte"""
    @property
    def Position2d(self) -> _n_11_t_1:"""Position2d { get; set; } -> Rectangle"""
    @property
    def Position3d(self) -> Rectangle3d:"""Position3d { get; set; } -> Rectangle3d"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def ScaleHeight(self) -> float:"""ScaleHeight { get; set; } -> float"""
    @property
    def ScaleWidth(self) -> float:"""ScaleWidth { get; set; } -> float"""
    @property
    def Type(self) -> Ole2Frame.ItemType:"""Type { get; } -> Ole2Frame.ItemType"""
    @property
    def UserType(self) -> str:"""UserType { get; } -> str"""
    @property
    def WcsHeight(self) -> float:"""WcsHeight { get; set; } -> float"""
    @property
    def WcsWidth(self) -> float:"""WcsWidth { get; set; } -> float"""
    def __init__(self) -> Ole2Frame:...
    class ItemType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Embedded: int
        Link: int
        Static: int
        value__: int
class OpenCloseTransaction(Transaction, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> OpenCloseTransaction:...
class OpenMode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ForNotify: int
    ForRead: int
    ForWrite: int
    value__: int
class OpenModeAttribute(_n_6_t_15, _n_14_t_0):
    @property
    def OpenMode(self) -> OpenMode:"""OpenMode { get; } -> OpenMode"""
    def __init__(self, mode: OpenMode) -> OpenModeAttribute:...
class OrdinateDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def DefiningPoint(self) -> _n_2_t_1:"""DefiningPoint { get; set; } -> Point3d"""
    @property
    def LeaderEndPoint(self) -> _n_2_t_1:"""LeaderEndPoint { get; set; } -> Point3d"""
    @property
    def Origin(self) -> _n_2_t_1:"""Origin { get; set; } -> Point3d"""
    @property
    def UsingXAxis(self) -> bool:"""UsingXAxis { get; set; } -> bool"""
    @property
    def UsingYAxis(self) -> bool:"""UsingYAxis { get; } -> bool"""
    def __init__(self, useXAxis: bool, definingPoint: _n_2_t_1, leaderEndPoint: _n_2_t_1, dimText: str, dimStyle: ObjectId) -> OrdinateDimension:...
    def __init__(self) -> OrdinateDimension:...
class OrthographicView(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BackView: int
    BottomView: int
    FrontView: int
    LeftView: int
    NonOrthoView: int
    RightView: int
    TopView: int
    value__: int
class OsnapOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def GetObjectSnapPoints(self, entity: Entity, snapMode: ObjectSnapModes, gsSelectionMark: _n_6_t_3, pickPoint: _n_2_t_1, lastPoint: _n_2_t_1, viewTransform: _n_2_t_6, snapPoints: _n_2_t_10, geometryIds: _n_2_t_16, insertionMat: _n_2_t_6):...
    def GetObjectSnapPoints(self, entity: Entity, snapMode: ObjectSnapModes, gsSelectionMark: _n_6_t_3, pickPoint: _n_2_t_1, lastPoint: _n_2_t_1, viewTransform: _n_2_t_6, snapPoints: _n_2_t_10, geometryIds: _n_2_t_16):...
    def IsContentSnappable(self, entity: Entity) -> bool:...
class PaperOrientationStates(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    _False: int
    NotApplicable: int
    _True: int
    value__: int
class ParallelConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> ParallelConstraint:...
class ParameterValueSet(_n_5_t_3, _n_6_t_0):
    @property
    def DataType(self) -> DataType:"""DataType { get; } -> DataType"""
    def CopyFrom(self, obj: _n_5_t_2):...
    def GetClosestLegalValue(self, value: ResultBuffer) -> ResultBuffer:...
    def ValueIsLegal(self, value: ResultBuffer) -> bool:...
class ParameterValueSetIncrement(ParameterValueSetMinMax, _n_6_t_0):
    @property
    def Increment(self) -> float:"""Increment { get; set; } -> float"""
    def __init__(self, other: ParameterValueSetIncrement) -> ParameterValueSetIncrement:...
    def __init__(self) -> ParameterValueSetIncrement:...
class ParameterValueSetList(ParameterValueSet, _n_6_t_0):
    @property
    def Values(self) -> _n_6_t_10[ResultBuffer]:"""Values { get; set; } -> Array"""
    def __init__(self, other: ParameterValueSetList) -> ParameterValueSetList:...
    def __init__(self) -> ParameterValueSetList:...
class ParameterValueSetMinMax(ParameterValueSet, _n_6_t_0):
    @property
    def Maximum(self) -> float:"""Maximum { get; set; } -> float"""
    @property
    def Minimum(self) -> float:"""Minimum { get; set; } -> float"""
    def __init__(self, other: ParameterValueSetMinMax) -> ParameterValueSetMinMax:...
    def __init__(self) -> ParameterValueSetMinMax:...
class ParseOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ParseOptionNone: int
    PreserveMtextFormat: int
    SetDefaultFormat: int
    value__: int
class PasswordOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Default: int
    IsExternalReference: int
    UpperCase: int
    value__: int
class PathOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AbsolutePath: int
    NoPath: int
    PathAndFile: int
    RelativePath: int
    value__: int
class PathRef(GeomRef, _n_6_t_0, _n_6_t_1):
    @property
    def EdgeRefs(self) -> _n_6_t_10[EdgeRef]:"""EdgeRefs { get; set; } -> Array"""
    def __init__(self, edgeSubentPathArr: _n_6_t_10[FullSubentityPath], faceSubentPathArr: _n_6_t_10[FullSubentityPath]) -> PathRef:...
    def __init__(self, edges: _n_6_t_10[EdgeRef]) -> PathRef:...
    def __init__(self) -> PathRef:...
    def GetEntityArray(self, bConcatenate: bool) -> _n_6_t_10[Entity]:...
    def IsEqualTo(self, curve: _n_2_t_7) -> bool:...
    def IsReferencePath(self) -> bool:...
class PatternDefinition(_n_6_t_12):
    @property
    def Angle(self) -> float:"""Angle { get; } -> float"""
    @property
    def BaseX(self) -> float:"""BaseX { get; } -> float"""
    @property
    def BaseY(self) -> float:"""BaseY { get; } -> float"""
    @property
    def OffsetX(self) -> float:"""OffsetX { get; } -> float"""
    @property
    def OffsetY(self) -> float:"""OffsetY { get; } -> float"""
    def __init__(self, patternAngle: float, basePoint: _n_2_t_0, offsetVector: _n_2_t_0, dashOffsets: _n_2_t_13) -> PatternDefinition:...
    def GetDashes(self) -> _n_2_t_13:...
class PCAdsName(_n_6_t_12):
    name1: int
    name2: int
class PdfDefinition(UnderlayDefinition, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PdfDefinition:...
class PdfReference(UnderlayReference, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PdfReference:...
class PerpendicularConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PerpendicularConstraint:...
class PhysicalIntensityMethod(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Flux: int
    Illuminance: int
    PeakIntensity: int
    value__: int
class PlaceHolder(DBObject, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PlaceHolder:...
class Planarity(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Linear: int
    NonPlanar: int
    Planar: int
    value__: int
class PlaneSurface(Surface, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PlaneSurface:...
    def CreateFromRegion(self, region: Region):...
class PlotPaperUnit(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Inches: int
    Millimeters: int
    Pixels: int
    value__: int
class PlotRotation(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Degrees000: int
    Degrees090: int
    Degrees180: int
    Degrees270: int
    value__: int
class PlotSettings(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def CanonicalMediaName(self) -> str:"""CanonicalMediaName { get; } -> str"""
    @property
    def CurrentStyleSheet(self) -> str:"""CurrentStyleSheet { get; } -> str"""
    @property
    def CustomPrintScale(self) -> CustomScale:"""CustomPrintScale { get; } -> CustomScale"""
    @property
    def DrawViewportsFirst(self) -> bool:"""DrawViewportsFirst { get; set; } -> bool"""
    @property
    def ModelType(self) -> bool:"""ModelType { get; } -> bool"""
    @property
    def PlotAsRaster(self) -> bool:"""PlotAsRaster { get; } -> bool"""
    @property
    def PlotCentered(self) -> bool:"""PlotCentered { get; } -> bool"""
    @property
    def PlotConfigurationName(self) -> str:"""PlotConfigurationName { get; } -> str"""
    @property
    def PlotHidden(self) -> bool:"""PlotHidden { get; set; } -> bool"""
    @property
    def PlotOrigin(self) -> _n_2_t_0:"""PlotOrigin { get; } -> Point2d"""
    @property
    def PlotPaperMargins(self) -> Extents2d:"""PlotPaperMargins { get; } -> Extents2d"""
    @property
    def PlotPaperSize(self) -> _n_2_t_0:"""PlotPaperSize { get; } -> Point2d"""
    @property
    def PlotPaperUnits(self) -> PlotPaperUnit:"""PlotPaperUnits { get; } -> PlotPaperUnit"""
    @property
    def PlotPlotStyles(self) -> bool:"""PlotPlotStyles { get; set; } -> bool"""
    @property
    def PlotRotation(self) -> PlotRotation:"""PlotRotation { get; } -> PlotRotation"""
    @property
    def PlotSettingsName(self) -> str:"""PlotSettingsName { get; set; } -> str"""
    @property
    def PlotTransparency(self) -> bool:"""PlotTransparency { get; set; } -> bool"""
    @property
    def PlotType(self) -> PlotType:"""PlotType { get; } -> PlotType"""
    @property
    def PlotViewName(self) -> str:"""PlotViewName { get; } -> str"""
    @property
    def PlotViewportBorders(self) -> bool:"""PlotViewportBorders { get; set; } -> bool"""
    @property
    def PlotWindowArea(self) -> Extents2d:"""PlotWindowArea { get; } -> Extents2d"""
    @property
    def PlotWireframe(self) -> bool:"""PlotWireframe { get; } -> bool"""
    @property
    def PrintLineweights(self) -> bool:"""PrintLineweights { get; set; } -> bool"""
    @property
    def ScaleLineweights(self) -> bool:"""ScaleLineweights { get; set; } -> bool"""
    @property
    def ShadePlot(self) -> PlotSettingsShadePlotType:"""ShadePlot { get; set; } -> PlotSettingsShadePlotType"""
    @property
    def ShadePlotCustomDpi(self) -> int:"""ShadePlotCustomDpi { get; set; } -> int"""
    @property
    def ShadePlotId(self) -> ObjectId:"""ShadePlotId { get; } -> ObjectId"""
    @property
    def ShadePlotResLevel(self) -> ShadePlotResLevel:"""ShadePlotResLevel { get; set; } -> ShadePlotResLevel"""
    @property
    def ShowPlotStyles(self) -> bool:"""ShowPlotStyles { get; set; } -> bool"""
    @property
    def StdScale(self) -> float:"""StdScale { get; } -> float"""
    @property
    def StdScaleType(self) -> StdScaleType:"""StdScaleType { get; } -> StdScaleType"""
    @property
    def UseStandardScale(self) -> bool:"""UseStandardScale { get; } -> bool"""
    def __init__(self, modelType: bool) -> PlotSettings:...
    def AddToPlotSettingsDictionary(self, toWhichDatabase: Database):...
    def SetShadePlot(self, type: PlotSettingsShadePlotType, shadePlotId: ObjectId):...
class PlotSettingsShadePlotType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AsDisplayed: int
    Hidden: int
    Rendered: int
    RenderPreset: int
    value__: int
    VisualStyle: int
    Wireframe: int
class PlotSettingsValidator(_n_5_t_3, _n_6_t_0):
    @property
    def Current(self) -> PlotSettingsValidator:"""Current { get; } -> PlotSettingsValidator"""
    def GetCanonicalMediaNameList(self, plotSet: PlotSettings) -> _n_9_t_0:...
    def GetLocaleMediaName(self, plotSet: PlotSettings, index: int) -> str:...
    def GetLocaleMediaName(self, plotSet: PlotSettings, canonicalName: str) -> str:...
    def GetPlotDeviceList(self) -> _n_9_t_0:...
    def GetPlotStyleSheetList(self) -> _n_9_t_0:...
    def RefreshLists(self, plotSet: PlotSettings):...
    def SetCanonicalMediaName(self, plotSet: PlotSettings, mediaName: str):...
    def SetClosestMediaName(self, plotSet: PlotSettings, paperWidth: float, paperHeight: float, units: PlotPaperUnit, matchPrintableArea: bool):...
    def SetCurrentStyleSheet(self, plotSet: PlotSettings, styleSheetName: str):...
    def SetCustomPrintScale(self, plotSet: PlotSettings, scale: CustomScale):...
    def SetDefaultPlotConfig(self, plotSet: PlotSettings):...
    def SetPlotCentered(self, plotSet: PlotSettings, isCentered: bool):...
    def SetPlotConfigurationName(self, plotSet: PlotSettings, plotDeviceName: str, mediaName: str):...
    def SetPlotOrigin(self, plotSet: PlotSettings, origin: _n_2_t_0):...
    def SetPlotPaperUnits(self, plotSet: PlotSettings, units: PlotPaperUnit):...
    def SetPlotRotation(self, plotSet: PlotSettings, rotationType: PlotRotation):...
    def SetPlotType(self, plotSet: PlotSettings, plotAreaType: PlotType):...
    def SetPlotViewName(self, plotSet: PlotSettings, viewName: str):...
    def SetPlotWindowArea(self, plotSet: PlotSettings, windowArea: Extents2d):...
    def SetStdScale(self, plotSet: PlotSettings, standardScale: float):...
    def SetStdScaleType(self, plotSet: PlotSettings, scaleType: StdScaleType):...
    def SetUseStandardScale(self, plotSet: PlotSettings, useStandard: bool):...
    def SetZoomToPaperOnUpdate(self, plotSet: PlotSettings, doZoom: bool):...
class PlotStyleDescriptor(_n_6_t_12):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    @property
    def Type(self) -> PlotStyleNameType:"""Type { get; } -> PlotStyleNameType"""
    def __init__(self, id: ObjectId, type: PlotStyleNameType) -> PlotStyleDescriptor:...
class PlotStyleNameType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    PlotStyleNameByBlock: int
    PlotStyleNameById: int
    PlotStyleNameByLayer: int
    PlotStyleNameIsDictionaryDefault: int
    value__: int
class PlotStyleTableChangedEventArgs(_n_6_t_13):
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
    @property
    def NewName(self) -> str:"""NewName { get; } -> str"""
class PlotStyleTableChangedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> PlotStyleTableChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: PlotStyleTableChangedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: PlotStyleTableChangedEventArgs):...
class PlotType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Display: int
    Extents: int
    Layout: int
    Limits: int
    value__: int
    View: int
    Window: int
class Point3AngularDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def ArcPoint(self) -> _n_2_t_1:"""ArcPoint { get; set; } -> Point3d"""
    @property
    def CenterPoint(self) -> _n_2_t_1:"""CenterPoint { get; set; } -> Point3d"""
    @property
    def XLine1Point(self) -> _n_2_t_1:"""XLine1Point { get; set; } -> Point3d"""
    @property
    def XLine2Point(self) -> _n_2_t_1:"""XLine2Point { get; set; } -> Point3d"""
    def __init__(self, centerPoint: _n_2_t_1, line1Point: _n_2_t_1, line2Point: _n_2_t_1, arcPoint: _n_2_t_1, dimensionText: str, dimensionStyle: ObjectId) -> Point3AngularDimension:...
    def __init__(self) -> Point3AngularDimension:...
class PointCloud(Entity, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PointCloud:...
    @staticmethod
    def RegenPointClouds():...
class PointCloudClassificationColorRamp(_n_5_t_3, _n_6_t_0):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NumColors(self) -> int:"""NumColors { get; } -> int"""
    def __init__(self) -> PointCloudClassificationColorRamp:...
    def Color(self, c: int) -> _n_0_t_2:...
    def SetColor(self, c: int, color: _n_0_t_2):...
    def SetFrom(self, source: PointCloudClassificationColorRamp):...
    def SetVisibility(self, c: int, bVisible: bool):...
    def Visibility(self, c: int) -> bool:...
class PointCloudColorMap(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ClassificationSchemeGUIDs(self) -> _n_6_t_10[str]:"""ClassificationSchemeGUIDs { get; } -> Array"""
    @property
    def ColorSchemeGUIDs(self) -> _n_6_t_10[str]:"""ColorSchemeGUIDs { get; } -> Array"""
    @property
    def DefaultClassificationColorScheme(self) -> str:"""DefaultClassificationColorScheme { get; set; } -> str"""
    @property
    def DefaultElevationColorScheme(self) -> str:"""DefaultElevationColorScheme { get; set; } -> str"""
    @property
    def DefaultIntensityColorScheme(self) -> str:"""DefaultIntensityColorScheme { get; set; } -> str"""
    @property
    def PointCloudColorSchemeChanged(self) -> PointCloudColorSchemeChangedEventHandler:
        """PointCloudColorSchemeChanged Event: PointCloudColorSchemeChangedEventHandler"""
    def ClassificationColorSchemeInUse(self) -> _n_6_t_10[str]:...
    def ClassificationScheme(self, name: str, target: PointCloudClassificationColorRamp) -> bool:...
    def ColorScheme(self, name: str, target: PointCloudColorRamp) -> bool:...
    def ColorSchemeInUse(self) -> _n_6_t_10[str]:...
    def DeleteClassificationScheme(self, name: str) -> bool:...
    def DeleteColorScheme(self, name: str) -> bool:...
    @staticmethod
    def GetColorMapId(hostDatabase: Database) -> ObjectId:...
    def HasClassificationScheme(self, name: str) -> bool:...
    def HasColorScheme(self, name: str) -> bool:...
    def SetClassificationScheme(self, name: str, source: PointCloudClassificationColorRamp) -> bool:...
    def SetColorScheme(self, name: str, source: PointCloudColorRamp) -> bool:...
class PointCloudColorRamp(_n_5_t_3, _n_6_t_0):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NumColors(self) -> int:"""NumColors { get; set; } -> int"""
    def __init__(self) -> PointCloudColorRamp:...
    def Color(self, c: int) -> _n_0_t_2:...
    def SetColor(self, c: int, color: _n_0_t_2):...
    def SetFrom(self, source: PointCloudColorRamp):...
    def SetVisibility(self, c: int, bVisible: bool):...
    def Visibility(self, c: int) -> bool:...
class PointCloudColorSchemeChangedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> PointCloudColorSchemeChangedEventHandler:...
    def BeginInvoke(self, __unnamed000: PointCloudColorMap, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, A_0: PointCloudColorMap):...
class PointCloudCrop(_n_6_t_0):
    @property
    def CropPlane(self) -> _n_2_t_4:"""CropPlane { get; set; } -> Plane"""
    @property
    def CropType(self) -> PointCloudCropType:"""CropType { get; set; } -> PointCloudCropType"""
    @property
    def Inside(self) -> bool:"""Inside { get; set; } -> bool"""
    @property
    def Inverted(self) -> bool:"""Inverted { get; set; } -> bool"""
    @property
    def Vertices(self) -> _n_2_t_10:"""Vertices { get; set; } -> Point3dCollection"""
    def Clear(self):...
    @staticmethod
    def Create(unmanagedObjPtr: _n_6_t_3) -> PointCloudCrop:...
    def IsValid(self) -> bool:...
class PointCloudCropType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Circular: int
    Invalid: int
    Polygonal: int
    Rectangular: int
    value__: int
class PointCloudDefEx(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ActiveFileName(self) -> str:"""ActiveFileName { get; set; } -> str"""
    @property
    def defaultHeight(self) -> float:"""defaultHeight { get; } -> float"""
    @property
    def defaultLength(self) -> float:"""defaultLength { get; } -> float"""
    @property
    def defaultWidth(self) -> float:"""defaultWidth { get; } -> float"""
    @property
    def EntityCount(self) -> int:"""EntityCount { get; } -> int"""
    @property
    def extents(self) -> Extents3d:"""extents { get; } -> Extents3d"""
    @property
    def FileType(self) -> str:"""FileType { get; } -> str"""
    @property
    def SourceFileName(self) -> str:"""SourceFileName { get; set; } -> str"""
    @property
    def totalPointsCount(self) -> int:"""totalPointsCount { get; } -> int"""
    @property
    def totalRegionsCount(self) -> int:"""totalRegionsCount { get; } -> int"""
    @property
    def totalScansCount(self) -> int:"""totalScansCount { get; } -> int"""
    def __init__(self) -> PointCloudDefEx:...
    @staticmethod
    def classVersion() -> int:...
    def getAllRcsFilePaths(self) -> _n_6_t_10[str]:...
    def getRcsFilePath(self, guid: str) -> str:...
    def load(self) -> bool:...
    def unload(self) -> bool:...
class PointCloudDispOptionOutOfRange(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    HidePoints: int
    UseMinMaxColors: int
    UseRGBScanColors: int
    value__: int
class PointCloudEx(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def ActiveFileName(self) -> str:"""ActiveFileName { get; } -> str"""
    @property
    def CroppingInverted(self) -> bool:"""CroppingInverted { get; set; } -> bool"""
    @property
    def CurrentColorScheme(self) -> str:"""CurrentColorScheme { get; set; } -> str"""
    @property
    def ElevationApplyToFixedRange(self) -> bool:"""ElevationApplyToFixedRange { get; set; } -> bool"""
    @property
    def ElevationGradient(self) -> bool:"""ElevationGradient { get; set; } -> bool"""
    @property
    def ElevationOutOfRangeBehavior(self) -> PointCloudDispOptionOutOfRange:"""ElevationOutOfRangeBehavior { get; set; } -> PointCloudDispOptionOutOfRange"""
    @property
    def GeomExtents(self) -> Extents3d:"""GeomExtents { get; } -> Extents3d"""
    @property
    def IntensityGradient(self) -> bool:"""IntensityGradient { get; set; } -> bool"""
    @property
    def IntensityOutOfRangeBehavior(self) -> PointCloudDispOptionOutOfRange:"""IntensityOutOfRangeBehavior { get; set; } -> PointCloudDispOptionOutOfRange"""
    @property
    def LimitBoxBound(self) -> _n_6_t_27[float, float]:"""LimitBoxBound { get; } -> Tuple"""
    @property
    def Location(self) -> _n_2_t_1:"""Location { get; set; } -> Point3d"""
    @property
    def MinMaxElevation(self) -> _n_6_t_27[float, float]:"""MinMaxElevation { get; set; } -> Tuple"""
    @property
    def MinMaxIntensity(self) -> _n_6_t_27[int, int]:"""MinMaxIntensity { get; set; } -> Tuple"""
    @property
    def NativeExtents(self) -> Extents3d:"""NativeExtents { get; } -> Extents3d"""
    @property
    def PointCloudDefExId(self) -> ObjectId:"""PointCloudDefExId { get; set; } -> ObjectId"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def ShowCropped(self) -> bool:"""ShowCropped { get; set; } -> bool"""
    @property
    def Stylization(self) -> PointCloudStylizationType:"""Stylization { get; set; } -> PointCloudStylizationType"""
    def __init__(self) -> PointCloudEx:...
    def addCroppingBoundary(self, cropping: PointCloudCrop):...
    @staticmethod
    def AttachPointCloud(filename: str, location: _n_2_t_1, scale: float, rotation: float, db: Database) -> ObjectId:...
    def clearCropping(self) -> bool:...
    def findRegionItem(self, regionId: int) -> PointCloudItem:...
    def findScanItem(self, scanGuid: str) -> PointCloudItem:...
    def GetColorSchemeForStylization(self, type: PointCloudStylizationType) -> str:...
    def getCroppingCount(self) -> int:...
    def getPointCloudCropping(self, index: int) -> PointCloudCrop:...
    def getPointCloudDataList(self) -> _n_8_t_1[PointCloudItem]:...
    def GetScanViewInfo(self, scanGuid: str, origin: _n_6_t_12, extent: _n_6_t_12) -> bool:...
    def HasProperty(self, prop: PointCloudProperty) -> PointCloudPropertyState:...
    def removeLastCropping(self) -> bool:...
    def setAllRegionsVisibility(self, visible: bool, includeUnassigned: bool):...
    def setAllScansVisibility(self, visible: bool):...
    def SetColorSchemeForStylization(self, name: str, type: PointCloudStylizationType):...
    def setRegionVisibility(self, regionId: int, visible: bool):...
    def setScanVisibility(self, scanGuid: str, visible: bool):...
class PointCloudItem(Notifier, _n_10_t_2):
    @property
    def CategoryId(self) -> PointCloudItemType:"""CategoryId { get; set; } -> PointCloudItemType"""
    @property
    def CurrentAdsName(self) -> _n_6_t_12:"""CurrentAdsName { get; set; } -> ValueType"""
    @property
    def Guid(self) -> str:"""Guid { get; set; } -> str"""
    @property
    def ItemId(self) -> int:"""ItemId { get; set; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ProjectName(self) -> str:"""ProjectName { get; set; } -> str"""
    @property
    def Visibility(self) -> bool:"""Visibility { get; set; } -> bool"""
    def __init__(self) -> PointCloudItem:...
    def Clone(self) -> PointCloudItem:...
    def CompareTo(self, other: PointCloudItem) -> bool:...
    @staticmethod
    def CreatePointCloudDataItemCollection(unmanagedObjPtr: _n_6_t_3) -> _n_8_t_1[PointCloudItem]:...
    def ToCmdString(self) -> str:...
class PointCloudItemType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    IndividualScan: int
    LegacyPointCloud: int
    PointCloudProject: int
    Region: int
    RegionRootGroup: int
    Scan: int
    ScanRootGroup: int
    UnassignedPoint: int
    value__: int
class PointCloudProperty(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Classification: int
    Color: int
    Intensity: int
    Normal: int
    value__: int
class PointCloudPropertyState(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    All: int
    _None: int
    Some: int
    value__: int
class PointCloudStylizationType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ClassificationRamp: int
    HeightRamp: int
    IntensityRamp: int
    NormalRamp: int
    SingleColor: int
    TrueColor: int
    value__: int
class PointCoincidenceConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PointCoincidenceConstraint:...
class PointCurveConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> PointCurveConstraint:...
class Poly2dType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CubicSplinePoly: int
    FitCurvePoly: int
    QuadSplinePoly: int
    SimplePoly: int
    value__: int
class Poly3dType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CubicSplinePoly: int
    QuadSplinePoly: int
    SimplePoly: int
    value__: int
class PolyFaceMesh(Entity, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def NumFaces(self) -> int:"""NumFaces { get; } -> int"""
    @property
    def NumVertices(self) -> int:"""NumVertices { get; } -> int"""
    def __init__(self) -> PolyFaceMesh:...
    def AppendFaceRecord(self, toAppend: FaceRecord) -> ObjectId:...
    def AppendVertex(self, vertexToAppend: PolyFaceMeshVertex) -> ObjectId:...
class PolyFaceMeshVertex(Vertex, _n_6_t_0, _n_6_t_1):
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    def __init__(self, position: _n_2_t_1) -> PolyFaceMeshVertex:...
    def __init__(self) -> PolyFaceMeshVertex:...
class PolygonMesh(Entity, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def IsMClosed(self) -> bool:"""IsMClosed { get; } -> bool"""
    @property
    def IsNClosed(self) -> bool:"""IsNClosed { get; } -> bool"""
    @property
    def MSize(self) -> int:"""MSize { get; set; } -> int"""
    @property
    def MSurfaceDensity(self) -> int:"""MSurfaceDensity { get; set; } -> int"""
    @property
    def NSize(self) -> int:"""NSize { get; set; } -> int"""
    @property
    def NSurfaceDensity(self) -> int:"""NSurfaceDensity { get; set; } -> int"""
    @property
    def PolyMeshType(self) -> PolyMeshType:"""PolyMeshType { get; set; } -> PolyMeshType"""
    def __init__(self, type: PolyMeshType, size: int, sizeValue: int, vertices: _n_2_t_10, closedValue: bool, closed: bool) -> PolygonMesh:...
    def __init__(self) -> PolygonMesh:...
    def AppendVertex(self, toAppend: PolygonMeshVertex) -> ObjectId:...
    def ConvertToPolyMeshType(self, newVal: PolyMeshType):...
    def MakeMClosed(self):...
    def MakeMOpen(self):...
    def MakeNClosed(self):...
    def MakeNOpen(self):...
    def Straighten(self):...
    def SurfaceFit(self, surfType: PolyMeshType, surfU: int, surfV: int):...
    def SurfaceFit(self):...
class PolygonMeshVertex(Vertex, _n_6_t_0, _n_6_t_1):
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def VertexType(self) -> Vertex3dType:"""VertexType { get; } -> Vertex3dType"""
    def __init__(self, point: _n_2_t_1) -> PolygonMeshVertex:...
    def __init__(self) -> PolygonMeshVertex:...
class Polyline(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def ConstantWidth(self) -> float:"""ConstantWidth { get; set; } -> float"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def HasBulges(self) -> bool:"""HasBulges { get; } -> bool"""
    @property
    def HasWidth(self) -> bool:"""HasWidth { get; } -> bool"""
    @property
    def IsOnlyLines(self) -> bool:"""IsOnlyLines { get; } -> bool"""
    @property
    def Length(self) -> float:"""Length { get; } -> float"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def NumberOfVertices(self) -> int:"""NumberOfVertices { get; } -> int"""
    @property
    def Plinegen(self) -> bool:"""Plinegen { get; set; } -> bool"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, vertices: int) -> Polyline:...
    def __init__(self) -> Polyline:...
    def AddVertexAt(self, index: int, pt: _n_2_t_0, bulge: float, startWidth: float, endWidth: float):...
    def ConvertFrom(self, entity: Entity, transferId: bool):...
    def ConvertTo(self, transferId: bool) -> Polyline2d:...
    def GetArcSegment2dAt(self, index: int) -> _n_2_t_27:...
    def GetArcSegmentAt(self, index: int) -> _n_2_t_28:...
    def GetBulgeAt(self, index: int) -> float:...
    def GetEndWidthAt(self, index: int) -> float:...
    def GetLineSegment2dAt(self, index: int) -> _n_2_t_29:...
    def GetLineSegmentAt(self, index: int) -> _n_2_t_30:...
    def GetPoint2dAt(self, index: int) -> _n_2_t_0:...
    def GetPoint3dAt(self, value: int) -> _n_2_t_1:...
    def GetSegmentType(self, index: int) -> SegmentType:...
    def GetStartWidthAt(self, index: int) -> float:...
    def MaximizeMemory(self):...
    def MinimizeMemory(self):...
    def OnSegmentAt(self, index: int, pt2d: _n_2_t_0, value: float) -> bool:...
    def RemoveVertexAt(self, index: int):...
    def Reset(self, reuse: bool, vertices: int):...
    def SetBulgeAt(self, index: int, bulge: float):...
    def SetEndWidthAt(self, index: int, endWidth: float):...
    def SetPointAt(self, index: int, pt: _n_2_t_0):...
    def SetStartWidthAt(self, index: int, startWidth: float):...
class Polyline2d(Curve, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def ConstantWidth(self) -> float:"""ConstantWidth { get; set; } -> float"""
    @property
    def DefaultEndWidth(self) -> float:"""DefaultEndWidth { get; set; } -> float"""
    @property
    def DefaultStartWidth(self) -> float:"""DefaultStartWidth { get; set; } -> float"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def Length(self) -> float:"""Length { get; } -> float"""
    @property
    def LinetypeGenerationOn(self) -> bool:"""LinetypeGenerationOn { get; set; } -> bool"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def PolyType(self) -> Poly2dType:"""PolyType { get; set; } -> Poly2dType"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, type: Poly2dType, vertices: _n_2_t_10, elevation: float, closed: bool, startWidth: float, endWidth: float, bulges: _n_2_t_13) -> Polyline2d:...
    def __init__(self) -> Polyline2d:...
    def AppendVertex(self, vertexToAppend: Vertex2d) -> ObjectId:...
    def ConvertToPolyType(self, newVal: Poly2dType):...
    def CurveFit(self):...
    def InsertVertexAt(self, vertexId: ObjectId, newVertex: Vertex2d) -> ObjectId:...
    def InsertVertexAt(self, indexVertex: Vertex2d, newVertex: Vertex2d):...
    def NonDBAppendVertex(self, vertexToAppend: Vertex2d):...
    def SplineFit(self, value: Poly2dType, segments: int):...
    def SplineFit(self):...
    def Straighten(self):...
    def VertexPosition(self, vertex: Vertex2d) -> _n_2_t_1:...
class Polyline3d(Curve, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def Length(self) -> float:"""Length { get; } -> float"""
    @property
    def PolyType(self) -> Poly3dType:"""PolyType { get; set; } -> Poly3dType"""
    def __init__(self, type: Poly3dType, vertices: _n_2_t_10, closed: bool) -> Polyline3d:...
    def __init__(self) -> Polyline3d:...
    def AppendVertex(self, vertexToAppend: PolylineVertex3d) -> ObjectId:...
    def ConvertToPolyType(self, newVal: Poly3dType):...
    def InsertVertexAt(self, indexVertexId: ObjectId, newVertex: PolylineVertex3d) -> ObjectId:...
    def InsertVertexAt(self, indexVertex: PolylineVertex3d, newVertex: PolylineVertex3d):...
    def SplineFit(self, value: Poly3dType, segments: int):...
    def SplineFit(self):...
    def Straighten(self):...
class PolylineVertex3d(Vertex, _n_6_t_0, _n_6_t_1):
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def VertexType(self) -> Vertex3dType:"""VertexType { get; } -> Vertex3dType"""
    def __init__(self, param0: _n_2_t_1) -> PolylineVertex3d:...
    def __init__(self) -> PolylineVertex3d:...
class PolyMeshType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BezierSurfaceMesh: int
    CubicSurfaceMesh: int
    QuadSurfaceMesh: int
    SimpleMesh: int
    value__: int
class Profile3d(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def Entity(self) -> Entity:"""Entity { get; set; } -> Entity"""
    @property
    def IsClosed(self) -> bool:"""IsClosed { get; } -> bool"""
    @property
    def IsEdge(self) -> bool:"""IsEdge { get; } -> bool"""
    @property
    def IsFace(self) -> bool:"""IsFace { get; } -> bool"""
    @property
    def IsPlanar(self) -> bool:"""IsPlanar { get; } -> bool"""
    @property
    def IsSubent(self) -> bool:"""IsSubent { get; } -> bool"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def ProfilePathRef(self) -> PathRef:"""ProfilePathRef { get; set; } -> PathRef"""
    @property
    def ProfileVertexRef(self) -> VertexRef:"""ProfileVertexRef { get; set; } -> VertexRef"""
    def __init__(self, profile3d: Profile3d) -> Profile3d:...
    def __init__(self, vertexRef: VertexRef) -> Profile3d:...
    def __init__(self, pathRef: PathRef) -> Profile3d:...
    def __init__(self, faceSubentPath: FullSubentityPath) -> Profile3d:...
    def __init__(self, entity: Entity) -> Profile3d:...
    def __init__(self) -> Profile3d:...
    @staticmethod
    def ConvertProfile(pathRefArray: _n_6_t_10[PathRef]) -> Profile3d:...
    def ConvertProfile(self, explodeMultiFaceRegions: bool, convertSurfaceToEdges: bool, nonPlanarOnly: bool, outerLoopOnly: bool) -> _n_6_t_10[Profile3d]:...
    @staticmethod
    def MergeProfiles(profiles: _n_6_t_10[Profile3d], mergeEdges: bool, mergeCurves: bool) -> _n_6_t_10[Profile3d]:...
class PropertiesOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def GetClassID(self, entity: DBObject) -> _n_6_t_22:...
    def List(self, entity: Entity):...
class ProxyEntity(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def ApplicationDescription(self) -> str:"""ApplicationDescription { get; } -> str"""
    @property
    def GraphicsMetafileType(self) -> GraphicsMetafileType:"""GraphicsMetafileType { get; } -> GraphicsMetafileType"""
    @property
    def OriginalClassName(self) -> str:"""OriginalClassName { get; } -> str"""
    @property
    def OriginalDxfName(self) -> str:"""OriginalDxfName { get; } -> str"""
    @property
    def ProxyFlags(self) -> int:"""ProxyFlags { get; } -> int"""
    def GetReferences(self) -> DBObjectReferenceCollection:...
class ProxyObject(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ApplicationDescription(self) -> str:"""ApplicationDescription { get; } -> str"""
    @property
    def OriginalClassName(self) -> str:"""OriginalClassName { get; } -> str"""
    @property
    def OriginalDxfName(self) -> str:"""OriginalDxfName { get; } -> str"""
    @property
    def ProxyFlags(self) -> int:"""ProxyFlags { get; } -> int"""
    def GetReferences(self) -> DBObjectReferenceCollection:...
    @staticmethod
    def ResurrectMeNow(id: ObjectId):...
class ProxyResurrectionCompletedEventArgs(_n_6_t_13):
    @property
    def ApplicationName(self) -> str:"""ApplicationName { get; } -> str"""
    @property
    def Ids(self) -> ObjectIdCollection:"""Ids { get; } -> ObjectIdCollection"""
class ProxyResurrectionCompletedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> ProxyResurrectionCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: ProxyResurrectionCompletedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: ProxyResurrectionCompletedEventArgs):...
class RadialDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def Center(self) -> _n_2_t_1:"""Center { get; set; } -> Point3d"""
    @property
    def ChordPoint(self) -> _n_2_t_1:"""ChordPoint { get; set; } -> Point3d"""
    @property
    def LeaderLength(self) -> float:"""LeaderLength { get; set; } -> float"""
    def __init__(self, center: _n_2_t_1, chordPoint: _n_2_t_1, leaderLength: float, dimensionText: str, dimensionStyle: ObjectId) -> RadialDimension:...
    def __init__(self) -> RadialDimension:...
class RadialDimensionLarge(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def Center(self) -> _n_2_t_1:"""Center { get; set; } -> Point3d"""
    @property
    def ChordPoint(self) -> _n_2_t_1:"""ChordPoint { get; set; } -> Point3d"""
    @property
    def JogAngle(self) -> float:"""JogAngle { get; set; } -> float"""
    @property
    def JogPoint(self) -> _n_2_t_1:"""JogPoint { get; set; } -> Point3d"""
    @property
    def OverrideCenter(self) -> _n_2_t_1:"""OverrideCenter { get; set; } -> Point3d"""
    def __init__(self, center: _n_2_t_1, chordPoint: _n_2_t_1, overrideCenter: _n_2_t_1, jogPoint: _n_2_t_1, jogAngle: float, dimensionText: str, dimensionStyle: ObjectId) -> RadialDimensionLarge:...
    def __init__(self) -> RadialDimensionLarge:...
class RadiusDiameterConstraint(ExplicitConstraint, _n_6_t_0, _n_6_t_1):
    @property
    def ConstrType(self) -> RadiusDiameterConstraint.RadDiaConstrType:"""ConstrType { get; } -> RadiusDiameterConstraint.RadDiaConstrType"""
    def __init__(self, type: RadiusDiameterConstraint.RadDiaConstrType) -> RadiusDiameterConstraint:...
    def __init__(self) -> RadiusDiameterConstraint:...
    class RadDiaConstrType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        CircleDiameter: int
        CircleRadius: int
        MajorRadius: int
        MinorRadius: int
        value__: int
class RapidRTRenderSettings(RenderSettings, _n_6_t_0, _n_6_t_1):
    @property
    def FilterHeight(self) -> float:"""FilterHeight { get; set; } -> float"""
    @property
    def FilterType(self) -> _n_3_t_43:"""FilterType { get; set; } -> RapidRTFilterType"""
    @property
    def FilterWidth(self) -> float:"""FilterWidth { get; set; } -> float"""
    @property
    def LightingModel(self) -> _n_3_t_44:"""LightingModel { get; set; } -> RapidRTLightingMode"""
    @property
    def RenderLevel(self) -> int:"""RenderLevel { get; set; } -> int"""
    @property
    def RenderTarget(self) -> RapidRTRenderTarget:"""RenderTarget { get; set; } -> RapidRTRenderTarget"""
    @property
    def RenderTime(self) -> int:"""RenderTime { get; set; } -> int"""
    def __init__(self) -> RapidRTRenderSettings:...
class RapidRTRenderTarget(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Infinite: int
    Level: int
    Time: int
    value__: int
class RasterImage(Image, _n_6_t_0, _n_6_t_1):
    @property
    def Brightness(self) -> _n_6_t_19:"""Brightness { get; set; } -> Byte"""
    @property
    def ClipBoundaryType(self) -> ClipBoundaryType:"""ClipBoundaryType { get; } -> ClipBoundaryType"""
    @property
    def Contrast(self) -> _n_6_t_19:"""Contrast { get; set; } -> Byte"""
    @property
    def DisplayOptions(self) -> ImageDisplayOptions:"""DisplayOptions { get; set; } -> ImageDisplayOptions"""
    @property
    def Fade(self) -> _n_6_t_19:"""Fade { get; set; } -> Byte"""
    @property
    def Height(self) -> float:"""Height { get; } -> float"""
    @property
    def ImageDefId(self) -> ObjectId:"""ImageDefId { get; set; } -> ObjectId"""
    @property
    def ImageHeight(self) -> float:"""ImageHeight { get; } -> float"""
    @property
    def ImageTransparency(self) -> bool:"""ImageTransparency { get; set; } -> bool"""
    @property
    def ImageWidth(self) -> float:"""ImageWidth { get; } -> float"""
    @property
    def IsClipped(self) -> bool:"""IsClipped { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Orientation(self) -> _n_2_t_2:"""Orientation { get; set; } -> CoordinateSystem3d"""
    @property
    def Path(self) -> str:"""Path { get; } -> str"""
    @property
    def PixelToModelTransform(self) -> _n_2_t_6:"""PixelToModelTransform { get; } -> Matrix3d"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; } -> Point3d"""
    @property
    def ReactorId(self) -> ObjectId:"""ReactorId { get; set; } -> ObjectId"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def Scale(self) -> _n_2_t_14:"""Scale { get; } -> Vector2d"""
    @property
    def ShowImage(self) -> bool:"""ShowImage { get; set; } -> bool"""
    @property
    def Width(self) -> float:"""Width { get; } -> float"""
    def __init__(self) -> RasterImage:...
    def AssociateRasterDef(self, definition: RasterImageDef):...
    @staticmethod
    def EnableReactors(enable: bool):...
    def GetClipBoundary(self) -> _n_2_t_18:...
    def GetVertices(self) -> _n_2_t_10:...
    def ImageSize(self, getCachedValue: bool) -> _n_2_t_14:...
    def SetClipBoundary(self, type: ClipBoundaryType, clipBoundaryVertices: _n_2_t_18):...
    def SetClipBoundary(self, size: _n_2_t_14):...
    def SetClipBoundaryToWholeImage(self):...
class RasterImageDef(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ActiveFileName(self) -> str:"""ActiveFileName { get; set; } -> str"""
    @property
    def ColorDepth(self) -> int:"""ColorDepth { get; } -> int"""
    @property
    def FileDescCopy(self) -> _n_6_t_3:"""FileDescCopy { get; } -> IntPtr"""
    @property
    def FileType(self) -> str:"""FileType { get; } -> str"""
    @property
    def ImageModified(self) -> bool:"""ImageModified { get; set; } -> bool"""
    @property
    def IsEmbedded(self) -> bool:"""IsEmbedded { get; } -> bool"""
    @property
    def IsLoaded(self) -> bool:"""IsLoaded { get; } -> bool"""
    @property
    def Organization(self) -> _n_3_t_45:"""Organization { get; } -> ImageOrg"""
    @property
    def ResolutionMMPerPixel(self) -> _n_2_t_14:"""ResolutionMMPerPixel { get; set; } -> Vector2d"""
    @property
    def ResolutionUnits(self) -> Unit:"""ResolutionUnits { get; set; } -> Unit"""
    @property
    def SearchForActivePath(self) -> str:"""SearchForActivePath { get; } -> str"""
    @property
    def Size(self) -> _n_2_t_14:"""Size { get; } -> Vector2d"""
    @property
    def SourceFileName(self) -> str:"""SourceFileName { get; set; } -> str"""
    @property
    def UndoStoreSize(self) -> int:"""UndoStoreSize { get; set; } -> int"""
    def __init__(self) -> RasterImageDef:...
    def CloseImage(self):...
    @staticmethod
    def CreateImageDictionary(database: Database) -> ObjectId:...
    def Embed(self):...
    def GetEntityCount(self, locked: bool) -> int:...
    @staticmethod
    def GetImageDictionary(database: Database) -> ObjectId:...
    def ImageCopy(self, forceImageLoad: bool) -> _n_6_t_3:...
    def Load(self):...
    def LocateActivePath(self) -> str:...
    def OpenImage(self) -> _n_6_t_3:...
    def SetImage(self, image: _n_6_t_3, fileDescription: _n_6_t_3, modifyDatabase: bool):...
    @staticmethod
    def SuggestName(imageDictionary: DBDictionary, newImagePathName: str) -> str:...
    def Unload(self, modifyDatabase: bool):...
    def UpdateEntities(self):...
class RasterVariables(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ImageFrame(self) -> FrameSetting:"""ImageFrame { get; set; } -> FrameSetting"""
    @property
    def ImageQuality(self) -> ImageQuality:"""ImageQuality { get; set; } -> ImageQuality"""
    @property
    def UserScale(self) -> Unit:"""UserScale { get; set; } -> Unit"""
    def __init__(self) -> RasterVariables:...
class Ray(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def BasePoint(self) -> _n_2_t_1:"""BasePoint { get; set; } -> Point3d"""
    @property
    def SecondPoint(self) -> _n_2_t_1:"""SecondPoint { get; set; } -> Point3d"""
    @property
    def UnitDir(self) -> _n_2_t_3:"""UnitDir { get; set; } -> Vector3d"""
    def __init__(self) -> Ray:...
class Rectangle3d(_n_6_t_12):
    @property
    def LowerLeft(self) -> _n_2_t_1:"""LowerLeft { get; } -> Point3d"""
    @property
    def LowerRight(self) -> _n_2_t_1:"""LowerRight { get; } -> Point3d"""
    @property
    def UpperLeft(self) -> _n_2_t_1:"""UpperLeft { get; } -> Point3d"""
    @property
    def UpperRight(self) -> _n_2_t_1:"""UpperRight { get; } -> Point3d"""
    def __init__(self, upperLeft: _n_2_t_1, upperRight: _n_2_t_1, lowerLeft: _n_2_t_1, lowerRight: _n_2_t_1) -> Rectangle3d:...
class RegAppTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class RegAppTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> RegAppTableRecord:...
class Region(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Area(self) -> float:"""Area { get; } -> float"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def NumChanges(self) -> int:"""NumChanges { get; } -> int"""
    @property
    def Perimeter(self) -> float:"""Perimeter { get; } -> float"""
    @property
    def UsesGraphicsCache(self) -> bool:"""UsesGraphicsCache { get; } -> bool"""
    def __init__(self) -> Region:...
    def AreaProperties(self, origin: _n_2_t_1, xAxis: _n_2_t_3, yAxis: _n_2_t_3) -> RegionAreaProperties:...
    def BooleanOperation(self, operation: BooleanOperationType, otherRegion: Region):...
    @staticmethod
    def CreateFromCurves(curveSegments: DBObjectCollection) -> DBObjectCollection:...
class RegionAreaProperties(_n_6_t_12):
    @property
    def Area(self) -> float:"""Area { get; } -> float"""
    @property
    def Centroid(self) -> _n_2_t_0:"""Centroid { get; } -> Point2d"""
    @property
    def Extents(self) -> Extents2d:"""Extents { get; } -> Extents2d"""
    @property
    def MomentsOfInertia(self) -> _n_2_t_14:"""MomentsOfInertia { get; } -> Vector2d"""
    @property
    def Perimeter(self) -> float:"""Perimeter { get; } -> float"""
    @property
    def PrincipalAxes(self) -> _n_2_t_14:"""PrincipalAxes { get; } -> Vector2d"""
    @property
    def PrincipalMoments(self) -> _n_2_t_14:"""PrincipalMoments { get; } -> Vector2d"""
    @property
    def ProductOfInertia(self) -> float:"""ProductOfInertia { get; } -> float"""
    @property
    def RadiiOfGyration(self) -> _n_2_t_14:"""RadiiOfGyration { get; } -> Vector2d"""
class RenderEnvironment(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Distances(self) -> RenderEnvironment.DoubleRangeParameter:"""Distances { get; set; } -> RenderEnvironment.DoubleRangeParameter"""
    @property
    def EnvironmentImageEnabled(self) -> bool:"""EnvironmentImageEnabled { get; set; } -> bool"""
    @property
    def EnvironmentImageFileName(self) -> str:"""EnvironmentImageFileName { get; set; } -> str"""
    @property
    def FogBackgroundEnabled(self) -> bool:"""FogBackgroundEnabled { get; set; } -> bool"""
    @property
    def FogColor(self) -> _n_0_t_2:"""FogColor { get; set; } -> EntityColor"""
    @property
    def FogDensity(self) -> RenderEnvironment.DoubleRangeParameter:"""FogDensity { get; set; } -> RenderEnvironment.DoubleRangeParameter"""
    @property
    def FogEnabled(self) -> bool:"""FogEnabled { get; set; } -> bool"""
    def __init__(self) -> RenderEnvironment:...
    class DoubleRangeParameter(_n_6_t_12):
        @property
        def Far(self) -> float:"""Far { get; } -> float"""
        @property
        def Near(self) -> float:"""Near { get; } -> float"""
        def __init__(self, n: float, f: float) -> RenderEnvironment.DoubleRangeParameter:...
class RenderGlobal(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Dimensions(self) -> RenderGlobal.DimensionsParameter:"""Dimensions { get; set; } -> RenderGlobal.DimensionsParameter"""
    @property
    def ExposureType(self) -> _n_3_t_46:"""ExposureType { get; set; } -> ExposureType"""
    @property
    def HighInfoLevel(self) -> bool:"""HighInfoLevel { get; set; } -> bool"""
    @property
    def PredefinedPresetsFirst(self) -> bool:"""PredefinedPresetsFirst { get; set; } -> bool"""
    @property
    def ProcedureAndDestination(self) -> RenderGlobal.ProcedureAndDestinationParameter:"""ProcedureAndDestination { get; set; } -> RenderGlobal.ProcedureAndDestinationParameter"""
    @property
    def SaveEnabled(self) -> bool:"""SaveEnabled { get; set; } -> bool"""
    @property
    def SaveFileName(self) -> str:"""SaveFileName { get; set; } -> str"""
    def __init__(self) -> RenderGlobal:...
    class Destination(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        value__: int
        Viewport: int
        Window: int
    class DimensionsParameter(_n_6_t_12):
        @property
        def Height(self) -> int:"""Height { get; } -> int"""
        @property
        def Width(self) -> int:"""Width { get; } -> int"""
        def __init__(self, w: int, h: int) -> RenderGlobal.DimensionsParameter:...
    class Procedure(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Crop: int
        Selected: int
        value__: int
        View: int
    class ProcedureAndDestinationParameter(_n_6_t_12):
        @property
        def Destination(self) -> RenderGlobal.Destination:"""Destination { get; } -> RenderGlobal.Destination"""
        @property
        def Procedure(self) -> RenderGlobal.Procedure:"""Procedure { get; } -> RenderGlobal.Procedure"""
        def __init__(self, p: RenderGlobal.Procedure, d: RenderGlobal.Destination) -> RenderGlobal.ProcedureAndDestinationParameter:...
class RenderSettings(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def BackFacesEnabled(self) -> bool:"""BackFacesEnabled { get; set; } -> bool"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def DiagnosticBackgroundEnabled(self) -> bool:"""DiagnosticBackgroundEnabled { get; set; } -> bool"""
    @property
    def DisplayIndex(self) -> int:"""DisplayIndex { get; set; } -> int"""
    @property
    def IsPredefined(self) -> bool:"""IsPredefined { get; set; } -> bool"""
    @property
    def MaterialsEnabled(self) -> bool:"""MaterialsEnabled { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PreviewImageFileName(self) -> str:"""PreviewImageFileName { get; set; } -> str"""
    @property
    def ShadowsEnabled(self) -> bool:"""ShadowsEnabled { get; set; } -> bool"""
    @property
    def TextureSampling(self) -> bool:"""TextureSampling { get; set; } -> bool"""
    def __init__(self) -> RenderSettings:...
class ReservedStringEnumType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ByBlock: int
    ByColor: int
    ByLayer: int
    Continuous: int
    Data: int
    Default: int
    DefPoints: int
    Global: int
    Header: int
    Missing: int
    Model: int
    _None: int
    Normal: int
    Standard: int
    Title: int
    value__: int
    VS2DWireframe: int
    VS3DHidden: int
    VS3DWireframe: int
    VSConceptual: int
    VSRealistic: int
    VSShaded: int
    VSShadedWithEdges: int
    VSShadesOfGray: int
    VSSketchy: int
    VSXRay: int
class ResultBuffer(_n_5_t_3, _n_6_t_0, _n_7_t_0, _n_6_t_8):
    def __init__(self, values: _n_6_t_10[TypedValue]) -> ResultBuffer:...
    def __init__(self) -> ResultBuffer:...
    def Add(self, value: object):...
    def Add(self, value: TypedValue):...
    def AsArray(self) -> _n_6_t_10[TypedValue]:...
class ResultBufferEnumerator(_n_7_t_3):
    pass
class RevolvedSurface(Surface, _n_6_t_0, _n_6_t_1):
    @property
    def AxisDirection(self) -> _n_2_t_3:"""AxisDirection { get; set; } -> Vector3d"""
    @property
    def AxisPoint(self) -> _n_2_t_1:"""AxisPoint { get; set; } -> Point3d"""
    @property
    def RevolveAngle(self) -> float:"""RevolveAngle { get; set; } -> float"""
    @property
    def RevolveEntity(self) -> Entity:"""RevolveEntity { get; } -> Entity"""
    @property
    def RevolveOptions(self) -> RevolveOptions:"""RevolveOptions { get; set; } -> RevolveOptions"""
    @property
    def RevolveProfile(self) -> Profile3d:"""RevolveProfile { get; } -> Profile3d"""
    @property
    def StartAngle(self) -> float:"""StartAngle { get; } -> float"""
    def __init__(self) -> RevolvedSurface:...
    def SetRevolve(self, axisPoint: _n_2_t_1, axisDirection: _n_2_t_3, revolveAngle: float, revolveOptions: RevolveOptions):...
class RevolveOptions(_n_5_t_3, _n_6_t_0, _n_6_t_1):
    @property
    def CloseToAxis(self) -> bool:"""CloseToAxis { get; } -> bool"""
    @property
    def DraftAngle(self) -> float:"""DraftAngle { get; } -> float"""
    @property
    def TwistAngle(self) -> float:"""TwistAngle { get; } -> float"""
    def __init__(self, opts: RevolveOptions) -> RevolveOptions:...
    def __init__(self) -> RevolveOptions:...
    def CheckRevolveCurve(self, __unnamed000: Entity, axisPnt: _n_2_t_1, axisDir: _n_2_t_3, displayErrorMessages: bool) -> RevolveOptionsCheckRevolveCurveOut:...
class RevolveOptionsBuilder(object):
    @property
    def CloseToAxis(self) -> bool:"""CloseToAxis { get; set; } -> bool"""
    @property
    def DraftAngle(self) -> float:"""DraftAngle { get; set; } -> float"""
    @property
    def TwistAngle(self) -> float:"""TwistAngle { get; set; } -> float"""
    def __init__(self, value: RevolveOptions) -> RevolveOptionsBuilder:...
    def __init__(self) -> RevolveOptionsBuilder:...
    def ToRevolveOptions(self) -> RevolveOptions:...
class RevolveOptionsCheckRevolveCurveOut(object):
    @property
    def Closed(self) -> bool:"""Closed { get; } -> bool"""
    @property
    def EndPointsOnAxis(self) -> bool:"""EndPointsOnAxis { get; } -> bool"""
    @property
    def Planar(self) -> bool:"""Planar { get; } -> bool"""
    def __init__(self) -> RevolveOptionsCheckRevolveCurveOut:...
class RigidSetTypeInfo(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    NonScalableRigidSet: int
    NotRigidSet: int
    ScalableRigidSet: int
    value__: int
class RotatedDimension(Dimension, _n_6_t_0, _n_6_t_1):
    @property
    def DimLinePoint(self) -> _n_2_t_1:"""DimLinePoint { get; set; } -> Point3d"""
    @property
    def Oblique(self) -> float:"""Oblique { get; set; } -> float"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def XLine1Point(self) -> _n_2_t_1:"""XLine1Point { get; set; } -> Point3d"""
    @property
    def XLine2Point(self) -> _n_2_t_1:"""XLine2Point { get; set; } -> Point3d"""
    def __init__(self, rotation: float, line1Point: _n_2_t_1, line2Point: _n_2_t_1, dimensionLinePoint: _n_2_t_1, dimensionText: str, dimensionStyle: ObjectId) -> RotatedDimension:...
    def __init__(self) -> RotatedDimension:...
class RotationAngle(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Degrees000: int
    Degrees090: int
    Degrees180: int
    Degrees270: int
    DegreesUnknown: int
    value__: int
class Row(CellRange, ISubObject, _n_8_t_0[CellReference], typing.Iterable[typing.Any]):
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def MinimumHeight(self) -> float:"""MinimumHeight { get; } -> float"""
class RowsCollection(_n_8_t_0[Row], typing.Iterable[typing.Any]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def Item(self) -> Row:"""Item { get; } -> Row"""
class RowType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DataRow: int
    HeaderRow: int
    TitleRow: int
    UnknownRow: int
    value__: int
class SaveType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    NoSave: int
    Save12: int
    Save13: int
    Save14: int
    Save2000: int
    Save2004: int
    Save2007: int
    Save2010: int
    value__: int
class ScaleEstimationMethod(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ScaleEstMethodPrismoidal: int
    ScaleEstMethodReferencePoint: int
    ScaleEstMethodUnity: int
    ScaleEstMethodUserDefined: int
    value__: int
class Section(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def BottomPlane(self) -> float:"""BottomPlane { get; set; } -> float"""
    @property
    def Boundary(self) -> _n_8_t_3[_n_2_t_1]:"""Boundary { get; } -> IList"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def HasJogs(self) -> bool:"""HasJogs { get; } -> bool"""
    @property
    def IndicatorFillColor(self) -> _n_0_t_0:"""IndicatorFillColor { get; set; } -> Color"""
    @property
    def IndicatorTransparency(self) -> int:"""IndicatorTransparency { get; set; } -> int"""
    @property
    def IsLiveSectionEnabled(self) -> bool:"""IsLiveSectionEnabled { get; set; } -> bool"""
    @property
    def IsSlice(self) -> bool:"""IsSlice { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; } -> Vector3d"""
    @property
    def NumVertices(self) -> int:"""NumVertices { get; } -> int"""
    @property
    def SectionPlaneOffset(self) -> float:"""SectionPlaneOffset { get; set; } -> float"""
    @property
    def Settings(self) -> ObjectId:"""Settings { get; } -> ObjectId"""
    @property
    def State(self) -> SectionState:"""State { get; set; } -> SectionState"""
    @property
    def ThicknessDepth(self) -> float:"""ThicknessDepth { get; set; } -> float"""
    @property
    def TopPlane(self) -> float:"""TopPlane { get; set; } -> float"""
    @property
    def VerticalDirection(self) -> _n_2_t_3:"""VerticalDirection { get; set; } -> Vector3d"""
    @property
    def Vertices(self) -> _n_2_t_10:"""Vertices { set; } -> Point3dCollection"""
    @property
    def ViewingDirection(self) -> _n_2_t_3:"""ViewingDirection { get; set; } -> Vector3d"""
    def __init__(self, pts: _n_2_t_10, verticalDir: _n_2_t_3, vecViewingDir: _n_2_t_3) -> Section:...
    def __init__(self, pts: _n_2_t_10, verticalDir: _n_2_t_3) -> Section:...
    def __init__(self) -> Section:...
    def AddVertex(self, nInsertAt: int, pt: _n_2_t_1):...
    def CreateJog(self, ptOnSection: _n_2_t_1):...
    def GenerateSectionGeometry(self, pEnt: Entity, pIntFillEnts: _n_6_t_10, pBackgroundEnts: _n_6_t_10, pForegroundEnts: _n_6_t_10, pFurveTangencyEnts: _n_6_t_10, pCurveTangencyEnts: _n_6_t_10):...
    def GetVertex(self, nIndex: int) -> _n_2_t_1:...
    def GetVertices(self, pts: _n_2_t_10):...
    def Height(self, nHeightType: SectionHeight) -> float:...
    def HitTest(self, ptHit: _n_2_t_1) -> SectionHitTestInfo:...
    def RemoveVertex(self, nIndex: int):...
    def SetHeight(self, nHeightType: SectionHeight, fHeight: float):...
    def SetVertex(self, nIndex: int, pt: _n_2_t_1):...
class SectionGeneration(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DestinationFile: int
    DestinationNewBlock: int
    DestinationReplaceBlock: int
    SourceAllObjects: int
    SourceSelectedObjects: int
    value__: int
class SectionGeometry(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BackgroundGeometry: int
    CurveTangencyLines: int
    ForegroundGeometry: int
    IntersectionBoundary: int
    IntersectionFill: int
    value__: int
class SectionHeight(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    HeightAboveSectionLine: int
    HeightBelowSectionLine: int
    value__: int
class SectionHitTestInfo(_n_6_t_12):
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def PtOnSegment(self) -> _n_2_t_1:"""PtOnSegment { get; } -> Point3d"""
    @property
    def SubItem(self) -> SectionSubItem:"""SubItem { get; } -> SectionSubItem"""
    def __init__(self) -> SectionHitTestInfo:...
class SectionManager(DBObject, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def LiveSection(self) -> ObjectId:"""LiveSection { get; } -> ObjectId"""
    @property
    def NumSections(self) -> int:"""NumSections { get; } -> int"""
    def __init__(self) -> SectionManager:...
    def GetSection(self, pszName: str) -> ObjectId:...
    def GetUniqueSectionName(self, pszBaseName: str) -> str:...
class SectionSettings(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def CurrentSectionType(self) -> SectionType:"""CurrentSectionType { get; set; } -> SectionType"""
    def __init__(self) -> SectionSettings:...
    def Color(self, nSecType: SectionType, nGeometry: SectionGeometry) -> _n_0_t_0:...
    def DestinationBlock(self, nSecType: SectionType) -> ObjectId:...
    def DestinationFile(self, nSecType: SectionType) -> str:...
    def DivisionLines(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool:...
    def EdgeTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry) -> int:...
    def FaceTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry) -> int:...
    def GenerationOptions(self, nSecType: SectionType) -> SectionGeneration:...
    def GetHatchPatternName(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str:...
    def GetHatchPatternType(self, nSecType: SectionType, nGeometry: SectionGeometry) -> HatchPatternType:...
    def GetSourceObjects(self, nSecType: SectionType, ids: ObjectIdCollection):...
    def HatchAngle(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float:...
    def HatchScale(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float:...
    def HatchSpacing(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float:...
    def HatchVisibility(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool:...
    def HiddenLine(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool:...
    def Layer(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str:...
    def Linetype(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str:...
    def LinetypeScale(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float:...
    def LineWeight(self, nSecType: SectionType, nGeometry: SectionGeometry) -> LineWeight:...
    def PlotStyleName(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str:...
    def Reset(self, nSecType: SectionType):...
    def Reset(self):...
    def SetColor(self, nSecType: SectionType, nGeometry: SectionGeometry, color: _n_0_t_0):...
    def SetDestinationBlock(self, nSecType: SectionType, id: ObjectId):...
    def SetDestinationFile(self, nSecType: SectionType, pszFileName: str):...
    def SetDivisionLines(self, nSecType: SectionType, nGeometry: SectionGeometry, bShow: bool):...
    def SetEdgeTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry, nTransparency: int):...
    def SetFaceTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry, nTransparency: int):...
    def SetGenerationOptions(self, nSecType: SectionType, nOptions: SectionGeneration):...
    def SetHatchAngle(self, nSecType: SectionType, nGeometry: SectionGeometry, fAngle: float):...
    def SetHatchPatternName(self, nSecType: SectionType, nGeometry: SectionGeometry, sNewName: str):...
    def SetHatchPatternType(self, nSecType: SectionType, nGeometry: SectionGeometry, nPatternType: HatchPatternType):...
    def SetHatchScale(self, nSecType: SectionType, nGeometry: SectionGeometry, fScale: float):...
    def SetHatchSpacing(self, nSecType: SectionType, nGeometry: SectionGeometry, fSpacing: float):...
    def SetHatchVisibility(self, nSecType: SectionType, nGeometry: SectionGeometry, bVisible: bool):...
    def SetHiddenLine(self, nSecType: SectionType, nGeometry: SectionGeometry, bHiddenLine: bool):...
    def SetLayer(self, nSecType: SectionType, nGeometry: SectionGeometry, pszLayer: str):...
    def SetLinetype(self, nSecType: SectionType, nGeometry: SectionGeometry, pszLinetype: str):...
    def SetLinetypeScale(self, nSecType: SectionType, nGeometry: SectionGeometry, fScale: float):...
    def SetLineWeight(self, nSecType: SectionType, nGeometry: SectionGeometry, nLineWeight: LineWeight):...
    def SetPlotStyleName(self, nSecType: SectionType, nGeometry: SectionGeometry, pszPlotStyleName: str):...
    def SetSourceObjects(self, nSecType: SectionType, ids: ObjectIdCollection):...
    def SetVisibility(self, nSecType: SectionType, nGeometry: SectionGeometry, bVisible: bool):...
    def Visibility(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool:...
class SectionState(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Boundary: int
    Plane: int
    value__: int
    Volume: int
class SectionSubItem(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BackLine: int
    BackLineBottom: int
    BackLineTop: int
    SectionLine: int
    SectionLineBottom: int
    SectionLineTop: int
    SectionSubItemNone: int
    value__: int
    VerticalLineBottom: int
    VerticalLineTop: int
class SectionSymbol(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Identifier(self) -> str:"""Identifier { get; set; } -> str"""
    @property
    def IsHalfSection(self) -> bool:"""IsHalfSection { get; set; } -> bool"""
    @property
    def IsViewDirectionLeft(self) -> bool:"""IsViewDirectionLeft { get; set; } -> bool"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def SectionPointsCount(self) -> int:"""SectionPointsCount { get; } -> int"""
    @property
    def SymbolStyleId(self) -> ObjectId:"""SymbolStyleId { get; set; } -> ObjectId"""
    def __init__(self) -> SectionSymbol:...
    def AddSectionPoint(self, pt: _n_2_t_1, bulge: float):...
    def GetBulgeAt(self, index: int) -> float:...
    def GetLabelNameAt(self, index: int) -> str:...
    def GetLabelOffsetAt(self, index: int) -> _n_2_t_3:...
    def GetLabelOffsets(self) -> _n_2_t_9:...
    def GetSectionPointAt(self, index: int) -> _n_2_t_1:...
    def GetSectionPoints(self) -> _n_2_t_10:...
    def RemoveSectionPointAt(self, index: int):...
    def SetLabelNameAt(self, index: int, name: str):...
    def SetLabelOffsetAt(self, index: int, offset: _n_2_t_3):...
    def SetLabelOffsets(self, offsets: _n_2_t_9):...
    def SetSectionPointAt(self, index: int, pt: _n_2_t_1, bulge: float):...
    def SetSectionPoints(self, points: _n_2_t_10, bulges: _n_2_t_13):...
    def SetSectionPoints(self, points: _n_2_t_10):...
class SectionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    LiveSection: int
    Section2d: int
    Section3d: int
    value__: int
class SectionViewArrowDirection(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AwayFromCuttingPlane: int
    TowardsCuttingPlane: int
    value__: int
class SectionViewIdentifierPosition(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AboveDirectionArrowLine: int
    AboveDirectionArrowSymbol: int
    EndCuttingPlane: int
    EndDirectionArrow: int
    StartDirectionArrow: int
    value__: int
class SectionViewStyle(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ArrowEndSymbolId(self) -> ObjectId:"""ArrowEndSymbolId { get; set; } -> ObjectId"""
    @property
    def ArrowPosition(self) -> SectionViewArrowDirection:"""ArrowPosition { get; set; } -> SectionViewArrowDirection"""
    @property
    def ArrowStartSymbolId(self) -> ObjectId:"""ArrowStartSymbolId { get; set; } -> ObjectId"""
    @property
    def ArrowSymbolColor(self) -> _n_0_t_0:"""ArrowSymbolColor { get; set; } -> Color"""
    @property
    def ArrowSymbolExtensionLength(self) -> float:"""ArrowSymbolExtensionLength { get; set; } -> float"""
    @property
    def ArrowSymbolSize(self) -> float:"""ArrowSymbolSize { get; set; } -> float"""
    @property
    def BendLineColor(self) -> _n_0_t_0:"""BendLineColor { get; set; } -> Color"""
    @property
    def BendLineLength(self) -> float:"""BendLineLength { get; set; } -> float"""
    @property
    def BendLineTypeId(self) -> ObjectId:"""BendLineTypeId { get; set; } -> ObjectId"""
    @property
    def BendLineWeight(self) -> LineWeight:"""BendLineWeight { get; set; } -> LineWeight"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def EndLineLength(self) -> float:"""EndLineLength { get; set; } -> float"""
    @property
    def EndLineOvershoot(self) -> float:"""EndLineOvershoot { get; set; } -> float"""
    @property
    def HatchAngles(self) -> _n_2_t_13:"""HatchAngles { get; set; } -> DoubleCollection"""
    @property
    def HatchBackgroundColor(self) -> _n_0_t_0:"""HatchBackgroundColor { get; set; } -> Color"""
    @property
    def HatchColor(self) -> _n_0_t_0:"""HatchColor { get; set; } -> Color"""
    @property
    def HatchPattern(self) -> str:"""HatchPattern { get; set; } -> str"""
    @property
    def HatchScale(self) -> float:"""HatchScale { get; set; } -> float"""
    @property
    def HatchTransparency(self) -> _n_0_t_1:"""HatchTransparency { get; set; } -> Transparency"""
    @property
    def IdentifierColor(self) -> _n_0_t_0:"""IdentifierColor { get; set; } -> Color"""
    @property
    def IdentifierExcludeCharacters(self) -> str:"""IdentifierExcludeCharacters { get; set; } -> str"""
    @property
    def IdentifierHeight(self) -> float:"""IdentifierHeight { get; set; } -> float"""
    @property
    def IdentifierOffset(self) -> float:"""IdentifierOffset { get; set; } -> float"""
    @property
    def IdentifierPosition(self) -> SectionViewIdentifierPosition:"""IdentifierPosition { get; set; } -> SectionViewIdentifierPosition"""
    @property
    def IdentifierStyleId(self) -> ObjectId:"""IdentifierStyleId { get; set; } -> ObjectId"""
    @property
    def IsContinuousLabeling(self) -> bool:"""IsContinuousLabeling { get; set; } -> bool"""
    @property
    def IsModifiedForRecompute(self) -> bool:"""IsModifiedForRecompute { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PlaneLineColor(self) -> _n_0_t_0:"""PlaneLineColor { get; set; } -> Color"""
    @property
    def PlaneLineTypeId(self) -> ObjectId:"""PlaneLineTypeId { get; set; } -> ObjectId"""
    @property
    def PlaneLineWeight(self) -> LineWeight:"""PlaneLineWeight { get; set; } -> LineWeight"""
    @property
    def ShowAllBendIndentifiers(self) -> bool:"""ShowAllBendIndentifiers { get; set; } -> bool"""
    @property
    def ShowAllPlaneLines(self) -> bool:"""ShowAllPlaneLines { get; set; } -> bool"""
    @property
    def ShowArrowheads(self) -> bool:"""ShowArrowheads { get; set; } -> bool"""
    @property
    def ShowEndAndBendLines(self) -> bool:"""ShowEndAndBendLines { get; set; } -> bool"""
    @property
    def ShowHatching(self) -> bool:"""ShowHatching { get; set; } -> bool"""
    @property
    def ShowViewLabel(self) -> bool:"""ShowViewLabel { get; set; } -> bool"""
    @property
    def ViewLabelAlignment(self) -> ModelDocViewLabelAlignmentType:"""ViewLabelAlignment { get; set; } -> ModelDocViewLabelAlignmentType"""
    @property
    def ViewLabelAttachment(self) -> ModelDocViewLabelAttachmentPoint:"""ViewLabelAttachment { get; set; } -> ModelDocViewLabelAttachmentPoint"""
    @property
    def ViewLabelOffset(self) -> float:"""ViewLabelOffset { get; set; } -> float"""
    @property
    def ViewLabelPattern(self) -> str:"""ViewLabelPattern { get; set; } -> str"""
    @property
    def ViewLabelTextColor(self) -> _n_0_t_0:"""ViewLabelTextColor { get; set; } -> Color"""
    @property
    def ViewLabelTextHeight(self) -> float:"""ViewLabelTextHeight { get; set; } -> float"""
    @property
    def ViewLabelTextStyleId(self) -> ObjectId:"""ViewLabelTextStyleId { get; set; } -> ObjectId"""
    def __init__(self) -> SectionViewStyle:...
    def DefaultViewName(self, index: int) -> str:...
    def GetViewLabelPattern(self, field: Field) -> str:...
    def PostViewStyleToDb(self, dataBasePointer: Database, styleName: str) -> ObjectId:...
    def SetDatabaseDefaults(self, dataBasePointer: Database):...
    def SetViewLabelPattern(self, pattern: str, field: Field):...
    def ValidateIdentifierExcludeCharacters(self, characters: str) -> bool:...
    def ValidateViewName(self, name: str) -> bool:...
class SecurityActions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AddTimeStamp: int
    EncryptData: int
    EncryptProperties: int
    SignData: int
    value__: int
class SecurityAlgorithm(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    RC4: int
    value__: int
class SecurityParameters(object):
    @property
    def Action(self) -> SecurityActions:"""Action { get; set; } -> SecurityActions"""
    @property
    def Algorithm(self) -> SecurityAlgorithm:"""Algorithm { get; set; } -> SecurityAlgorithm"""
    @property
    def Comment(self) -> str:"""Comment { get; set; } -> str"""
    @property
    def Issuer(self) -> str:"""Issuer { get; set; } -> str"""
    @property
    def KeyLength(self) -> int:"""KeyLength { get; set; } -> int"""
    @property
    def Password(self) -> str:"""Password { get; set; } -> str"""
    @property
    def ProviderName(self) -> str:"""ProviderName { get; set; } -> str"""
    @property
    def ProviderType(self) -> int:"""ProviderType { get; set; } -> int"""
    @property
    def SerialNumber(self) -> str:"""SerialNumber { get; set; } -> str"""
    @property
    def Subject(self) -> str:"""Subject { get; set; } -> str"""
    @property
    def TimeServer(self) -> str:"""TimeServer { get; set; } -> str"""
    def __init__(self, password: str, providerName: str, subject: str, issuer: str, serialNumber: str, comment: str, timeServer: str, actions: SecurityActions, algorithm: SecurityAlgorithm, keyLength: _n_6_t_11, providerType: _n_6_t_11) -> SecurityParameters:...
    def __init__(self) -> SecurityParameters:...
class SegmentType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Arc: int
    Coincident: int
    Empty: int
    Line: int
    Point: int
    value__: int
class SelectType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Crossing: int
    value__: int
    Window: int
class SequenceEnd(Entity, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> SequenceEnd:...
class ShadePlotResLevel(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Custom: int
    Draft: int
    Maximum: int
    Normal: int
    Presentation: int
    Preview: int
    value__: int
class ShadePlotType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AsDisplayed: int
    Hidden: int
    Rendered: int
    RenderPreset: int
    value__: int
    VisualStyle: int
    Wireframe: int
class ShadowSamplingMultiplier(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    SamplingMultiplierOne: int
    SamplingMultiplierOneEighth: int
    SamplingMultiplierOneFourth: int
    SamplingMultiplierOneHalf: int
    SamplingMultiplierTwo: int
    SamplingMultiplierZero: int
    value__: int
class Shape(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Oblique(self) -> float:"""Oblique { get; set; } -> float"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def ShapeIndex(self) -> ObjectId:"""ShapeIndex { get; set; } -> ObjectId"""
    @property
    def ShapeNumber(self) -> int:"""ShapeNumber { get; set; } -> int"""
    @property
    def Size(self) -> float:"""Size { get; set; } -> float"""
    @property
    def StyleId(self) -> ObjectId:"""StyleId { get; set; } -> ObjectId"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    @property
    def WidthFactor(self) -> float:"""WidthFactor { get; set; } -> float"""
    def __init__(self, position: _n_2_t_1, size: float, rotation: float, widthFactor: float) -> Shape:...
    def __init__(self) -> Shape:...
class SkyBackground(Background, _n_6_t_0, _n_6_t_1):
    @property
    def SunId(self) -> ObjectId:"""SunId { get; set; } -> ObjectId"""
    def __init__(self) -> SkyBackground:...
    def GetDrawableType(self) -> _n_3_t_14:...
class Solid(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, pointer1: _n_2_t_1, pointer2: _n_2_t_1, pointer3: _n_2_t_1) -> Solid:...
    def __init__(self, pointer1: _n_2_t_1, pointer2: _n_2_t_1, pointer3: _n_2_t_1, pointer4: _n_2_t_1) -> Solid:...
    def __init__(self) -> Solid:...
    def GetPointAt(self, index: int) -> _n_2_t_1:...
    def SetPointAt(self, index: int, pointValue: _n_2_t_1):...
class Solid3d(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Area(self) -> float:"""Area { get; } -> float"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def MassProperties(self) -> Solid3dMassProperties:"""MassProperties { get; } -> Solid3dMassProperties"""
    @property
    def NumChanges(self) -> int:"""NumChanges { get; } -> int"""
    @property
    def RecordHistory(self) -> bool:"""RecordHistory { get; set; } -> bool"""
    @property
    def ShowHistory(self) -> bool:"""ShowHistory { get; set; } -> bool"""
    @property
    def UsesGraphicsCache(self) -> bool:"""UsesGraphicsCache { get; } -> bool"""
    def __init__(self) -> Solid3d:...
    def BooleanOperation(self, operation: BooleanOperationType, solid: Solid3d):...
    def ChamferEdges(self, subentityIds: _n_6_t_10[SubentityId], baseSubentityId: SubentityId, baseDist: float, otherDist: float):...
    def CheckInterference(self, otherSolid: Solid3d) -> bool:...
    def CleanBody(self):...
    def ConvertToBrepAtSubentPaths(self, paths: _n_6_t_10[FullSubentityPath]):...
    def CopyEdge(self, subEntityId: SubentityId) -> Entity:...
    def CopyFace(self, subEntityId: SubentityId) -> Entity:...
    def CreateBox(self, lengthAlongX: float, lengthAlongY: float, lengthAlongZ: float):...
    def CreateExtrudedSolid(self, sweepEntity: Entity, faceSubEntityId: SubentityId, height: float, sweepOptions: SweepOptions):...
    def CreateExtrudedSolid(self, sweepEntity: Entity, faceSubEntityId: SubentityId, directionVector: _n_2_t_3, sweepOptions: SweepOptions):...
    def CreateExtrudedSolid(self, sweepEntity: Entity, directionVector: _n_2_t_3, sweepOptions: SweepOptions):...
    def CreateFrom(self, fromEntity: Entity):...
    def CreateFrustum(self, height: float, radiusAlongX: float, radiusAlongY: float, topRadius: float):...
    def CreateLoftedSolid(self, crossSections: _n_6_t_10[LoftProfile], guides: _n_6_t_10[LoftProfile], path: LoftProfile, loftOptions: LoftOptions):...
    def CreateLoftedSolid(self, crossSectionCurves: _n_6_t_10[Entity], guideCurves: _n_6_t_10[Entity], pathCurve: Entity, loftOptions: LoftOptions):...
    def CreatePyramid(self, height: float, sides: int, radius: float, topRadius: float):...
    def CreateRevolvedSolid(self, profileEntity: Entity, faceSubEntityId: SubentityId, axisPoint: _n_2_t_1, axisDir: _n_2_t_3, angleOfRevolution: float, startAngle: float, revolveOptions: RevolveOptions):...
    def CreateRevolvedSolid(self, profileEntity: Entity, axisPoint: _n_2_t_1, axisDir: _n_2_t_3, angleOfRevolution: float, startAngle: float, revolveOptions: RevolveOptions):...
    def CreateSculptedSolid(self, limitingBodies: _n_6_t_10[Entity], limitingFlags: _n_2_t_16):...
    def CreateSphere(self, radius: float):...
    def CreateSweptSolid(self, sweepEntity: Entity, faceSubEntityId: SubentityId, pathEntity: Entity, sweepOptions: SweepOptions):...
    def CreateSweptSolid(self, sweepEntity: Entity, pathEntity: Entity, sweepOptions: SweepOptions):...
    def CreateTorus(self, majorRadius: float, minorRadius: float):...
    def CreateWedge(self, lengthAlongX: float, lengthAlongY: float, lengthAlongZ: float):...
    def Extrude(self, region: Region, height: float, taperAngle: float):...
    def ExtrudeAlongPath(self, region: Region, path: Curve, taperAngle: float):...
    def ExtrudeFaces(self, subentityIds: _n_6_t_10[SubentityId], height: float, taper: float):...
    def ExtrudeFacesAlongPath(self, subentityIds: _n_6_t_10[SubentityId], path: Curve):...
    def FilletEdges(self, subentityIds: _n_6_t_10[SubentityId], radius: _n_2_t_13, startSetback: _n_2_t_13, endSetback: _n_2_t_13):...
    def GetSection(self, plane: _n_2_t_4) -> Region:...
    def GetSubentityColor(self, subEntityId: SubentityId) -> _n_0_t_0:...
    def GetSubentityMaterial(self, subEntityId: SubentityId) -> ObjectId:...
    def GetSubentityMaterialMapper(self, subEntityId: SubentityId) -> _n_3_t_7:...
    def ImprintEntity(self, entity: Entity):...
    def OffsetBody(self, offsetDistance: float):...
    def OffsetFaces(self, subentityIds: _n_6_t_10[SubentityId], offsetDistance: float):...
    def ProjectOnToSolid(self, entityToProject: Entity, projectionDirection: _n_2_t_3) -> _n_6_t_10[Entity]:...
    def RemoveFaces(self, subentityIds: _n_6_t_10[SubentityId]):...
    def Revolve(self, region: Region, axisPoint: _n_2_t_1, axisDir: _n_2_t_3, angleOfRevolution: float):...
    def SeparateBody(self) -> _n_6_t_10[Solid3d]:...
    def SetSubentityColor(self, subEntityId: SubentityId, color: _n_0_t_0):...
    def SetSubentityMaterial(self, subEntityId: SubentityId, materialId: ObjectId):...
    def SetSubentityMaterialMapper(self, subEntityId: SubentityId, mapper: _n_3_t_7):...
    def ShellBody(self, subentityIds: _n_6_t_10[SubentityId], offsetDistance: float):...
    def Slice(self, surface: Surface, negativeHalfToo: bool) -> Solid3d:...
    def Slice(self, surface: Surface):...
    def Slice(self, plane: _n_2_t_4, negativeHalfToo: bool) -> Solid3d:...
    def Slice(self, plane: _n_2_t_4):...
    def StlOut(self, fileName: str, asciiFormat: bool):...
    def TaperFaces(self, subentityIds: _n_6_t_10[SubentityId], basePoint: _n_2_t_1, draftVector: _n_2_t_3, draftAngle: float):...
    def TransformFaces(self, subentityIds: _n_6_t_10[SubentityId], matrix: _n_2_t_6):...
class Solid3dMassProperties(_n_6_t_12):
    @property
    def Centroid(self) -> _n_2_t_1:"""Centroid { get; } -> Point3d"""
    @property
    def Extents(self) -> Extents3d:"""Extents { get; } -> Extents3d"""
    @property
    def MomentsOfIntertia(self) -> _n_2_t_3:"""MomentsOfIntertia { get; } -> Vector3d"""
    @property
    def PrincipalAxes(self) -> _n_2_t_3:"""PrincipalAxes { get; } -> Vector3d"""
    @property
    def PrincipalMoments(self) -> _n_2_t_3:"""PrincipalMoments { get; } -> Vector3d"""
    @property
    def ProductsOfIntertia(self) -> _n_2_t_3:"""ProductsOfIntertia { get; } -> Vector3d"""
    @property
    def RadiiOfGyration(self) -> _n_2_t_3:"""RadiiOfGyration { get; } -> Vector3d"""
    @property
    def Volume(self) -> float:"""Volume { get; } -> float"""
    def __init__(self, dummy: int) -> Solid3dMassProperties:...
class SolidBackground(Background, _n_6_t_0, _n_6_t_1):
    @property
    def Color(self) -> _n_0_t_2:"""Color { get; set; } -> EntityColor"""
    def __init__(self) -> SolidBackground:...
class SourceType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    FusionSource: int
    InventorSource: int
    ModelSpaceSource: int
    SourceNotDefined: int
    value__: int
class Spline(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def Degree(self) -> int:"""Degree { get; } -> int"""
    @property
    def EndFitTangent(self) -> _n_2_t_3:"""EndFitTangent { get; } -> Vector3d"""
    @property
    def FitData(self) -> FitData:"""FitData { get; set; } -> FitData"""
    @property
    def FitTolerance(self) -> float:"""FitTolerance { get; set; } -> float"""
    @property
    def HasFitData(self) -> bool:"""HasFitData { get; } -> bool"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def IsRational(self) -> bool:"""IsRational { get; } -> bool"""
    @property
    def NumControlPoints(self) -> int:"""NumControlPoints { get; } -> int"""
    @property
    def NumFitPoints(self) -> int:"""NumFitPoints { get; } -> int"""
    @property
    def NurbsData(self) -> NurbsData:"""NurbsData { get; set; } -> NurbsData"""
    @property
    def StartFitTangent(self) -> _n_2_t_3:"""StartFitTangent { get; } -> Vector3d"""
    @property
    def Type(self) -> SplineType:"""Type { get; set; } -> SplineType"""
    def __init__(self, fitPoints: _n_2_t_10, startTangent: _n_2_t_3, endTangent: _n_2_t_3, knotParam: _n_2_t_17, degree: int, fitTolerance: float) -> Spline:...
    def __init__(self, fitPoints: _n_2_t_10, isPeriodic: bool, knotParam: _n_2_t_17, degree: int, fitTolerance: float) -> Spline:...
    def __init__(self, fitPoints: _n_2_t_10, knotParam: _n_2_t_17, degree: int, fitTolerance: float) -> Spline:...
    def __init__(self, center: _n_2_t_1, unitNormal: _n_2_t_3, majorAxis: _n_2_t_3, radiusRatio: float, startAngle: float, endAngle: float) -> Spline:...
    def __init__(self, degree: int, rational: bool, closed: bool, periodic: bool, controlPoints: _n_2_t_10, knots: _n_2_t_13, weights: _n_2_t_13, controlPointTolerance: float, knotTolerance: float) -> Spline:...
    def __init__(self, point: _n_2_t_10, startTangent: _n_2_t_3, endTangent: _n_2_t_3, order: int, fitTolerance: float) -> Spline:...
    def __init__(self, point: _n_2_t_10, order: int, fitTolerance: float) -> Spline:...
    def __init__(self) -> Spline:...
    def ElevateDegree(self, newDegree: int):...
    def GetControlPointAt(self, index: int) -> _n_2_t_1:...
    def GetFitPointAt(self, index: int) -> _n_2_t_1:...
    def InsertControlPointAt(self, knotParam: float, controlPoint: _n_2_t_1, weight: float) -> _n_5_t_1:...
    def InsertFitPointAt(self, index: int, point: _n_2_t_1):...
    def InsertKnot(self, value: float):...
    def ModifyPositionAndTangent(self, param: float, point: _n_2_t_1, deriv: _n_2_t_3) -> _n_5_t_1:...
    def PurgeFitData(self):...
    def Rebuild(self, degree: int, numCtrlPts: int) -> _n_5_t_1:...
    def RemoveControlPointAt(self, index: int) -> _n_5_t_1:...
    def RemoveFitPointAt(self, index: int):...
    def SetControlPointAt(self, index: int, point: _n_2_t_1):...
    def SetFitPointAt(self, index: int, point: _n_2_t_1):...
    def SetWeightAt(self, index: int, weight: float):...
    def ToPolyline(self, numOfVertices: _n_6_t_11, bConvertAsArcs: bool, bToLWPolyline: bool) -> Curve:...
    def ToPolyline(self, bConvertAsArcs: bool, bToLWPolyline: bool) -> Curve:...
    def ToPolyline(self, numOfVertices: _n_6_t_11) -> Curve:...
    def ToPolyline(self) -> Curve:...
    def ToPolylineWithPrecision(self, precision: int, bConvertAsArcs: bool, bToLWPolyline: bool) -> Curve:...
    def ToPolylineWithPrecision(self, precision: int) -> Curve:...
    def UpdateFitData(self):...
    def WeightAt(self, index: int) -> float:...
class SplineType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ControlPoints: int
    FitPoints: int
    value__: int
class StandardScaleType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CustomScale: int
    Scale100To1: int
    Scale10To1: int
    Scale1ftAnd1ft: int
    Scale1inAnd1ft: int
    Scale1To1: int
    Scale1To10: int
    Scale1To100: int
    Scale1To128inAnd1ft: int
    Scale1To16: int
    Scale1To16inchAnd1ft: int
    Scale1To2: int
    Scale1To20: int
    Scale1To2inchAnd1ft: int
    Scale1To30: int
    Scale1To32inchAnd1ft: int
    Scale1To4: int
    Scale1To40: int
    Scale1To4inchAnd1ft: int
    Scale1To5: int
    Scale1To50: int
    Scale1To64inchAnd1ft: int
    Scale1To8: int
    Scale1To8inchAnd1ft: int
    Scale2To1: int
    Scale3inAnd1ft: int
    Scale3To16inchAnd1ft: int
    Scale3To32inchAnd1ft: int
    Scale3To4inchAnd1ft: int
    Scale3To8inchAnd1ft: int
    Scale4To1: int
    Scale6inAnd1ft: int
    Scale8To1: int
    ScaleToFit: int
    value__: int
class StdScaleType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ScaleToFit: int
    StdScale1000To1: int
    StdScale100To1: int
    StdScale10To1: int
    StdScale1ftIs1ft: int
    StdScale1InchIs1ft: int
    StdScale1To1: int
    StdScale1To10: int
    StdScale1To100: int
    StdScale1To128InchIs1ft: int
    StdScale1To16: int
    StdScale1To16InchIs1ft: int
    StdScale1To2: int
    StdScale1To20: int
    StdScale1To2InchIs1ft: int
    StdScale1To30: int
    StdScale1To32InchIs1ft: int
    StdScale1To4: int
    StdScale1To40: int
    StdScale1To4InchIs1ft: int
    StdScale1To5: int
    StdScale1To50: int
    StdScale1To64InchIs1ft: int
    StdScale1To8: int
    StdScale1To8InchIs1ft: int
    StdScale2To1: int
    StdScale3InchIs1ft: int
    StdScale3To16InchIs1ft: int
    StdScale3To32InchIs1ft: int
    StdScale3To4InchIs1ft: int
    StdScale3To8InchIs1ft: int
    StdScale4To1: int
    StdScale6InchIs1ft: int
    StdScale8To1: int
    value__: int
class SubDMesh(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def EdgeArray(self) -> _n_2_t_24:"""EdgeArray { get; } -> Int32Collection"""
    @property
    def FaceArray(self) -> _n_2_t_24:"""FaceArray { get; } -> Int32Collection"""
    @property
    def NormalArray(self) -> _n_2_t_9:"""NormalArray { get; } -> Vector3dCollection"""
    @property
    def NumberOfEdges(self) -> int:"""NumberOfEdges { get; } -> int"""
    @property
    def NumberOfFaces(self) -> int:"""NumberOfFaces { get; } -> int"""
    @property
    def NumberOfSubDividedFaces(self) -> int:"""NumberOfSubDividedFaces { get; } -> int"""
    @property
    def NumberOfSubDividedVertices(self) -> int:"""NumberOfSubDividedVertices { get; } -> int"""
    @property
    def NumberOfVertices(self) -> int:"""NumberOfVertices { get; } -> int"""
    @property
    def SmoothLevel(self) -> int:"""SmoothLevel { get; } -> int"""
    @property
    def SubDividedFaceArray(self) -> _n_2_t_24:"""SubDividedFaceArray { get; } -> Int32Collection"""
    @property
    def SubDividedNormalArray(self) -> _n_2_t_9:"""SubDividedNormalArray { get; } -> Vector3dCollection"""
    @property
    def SubDividedVertices(self) -> _n_2_t_10:"""SubDividedVertices { get; } -> Point3dCollection"""
    @property
    def VertexColorArray(self) -> _n_6_t_10[_n_0_t_2]:"""VertexColorArray { get; set; } -> Array"""
    @property
    def VertexNormalArray(self) -> _n_2_t_9:"""VertexNormalArray { get; set; } -> Vector3dCollection"""
    @property
    def VertexTextureArray(self) -> _n_2_t_10:"""VertexTextureArray { get; set; } -> Point3dCollection"""
    @property
    def Vertices(self) -> _n_2_t_10:"""Vertices { get; } -> Point3dCollection"""
    @property
    def Watertight(self) -> bool:"""Watertight { get; } -> bool"""
    def __init__(self) -> SubDMesh:...
    def Cap(self, edges: _n_6_t_10[FullSubentityPath]):...
    def Collapse(self, subentityId: SubentityId):...
    def ComputeSurfaceArea(self) -> float:...
    def ComputeVolume(self) -> float:...
    def ConvertToSolid(self, convertAsSmooth: bool, optimize: bool) -> Solid3d:...
    def ConvertToSurface(self, convertAsSmooth: bool, optimize: bool) -> Surface:...
    def ConvertToSurface(self, convertAsSmooth: bool, subentId: SubentityId) -> Surface:...
    def ExtrudeConnectedFaces(self, paths: _n_6_t_10[FullSubentityPath], alongPath: _n_2_t_10, taper: float):...
    def ExtrudeConnectedFaces(self, paths: _n_6_t_10[FullSubentityPath], length: float, dir: _n_2_t_3, taper: float):...
    def ExtrudeFaces(self, paths: _n_6_t_10[FullSubentityPath], alongPath: _n_2_t_10, taper: float):...
    def ExtrudeFaces(self, paths: _n_6_t_10[FullSubentityPath], length: float, dir: _n_2_t_3, taper: float):...
    def GetAdjacentSubentPath(self, path: FullSubentityPath, type: SubentityType) -> _n_6_t_10[FullSubentityPath]:...
    def GetCrease(self, subentPaths: _n_6_t_10[FullSubentityPath]) -> _n_2_t_13:...
    def GetCrease(self, id: SubentityId) -> float:...
    def GetFacePlane(self, subentId: SubentityId) -> _n_2_t_4:...
    def GetNumberOfSubDividedFacesAt(self, paths: _n_6_t_10[FullSubentityPath]) -> int:...
    @staticmethod
    def GetObjectMesh(dbObj: DBObject, faceterData: MeshFaceterData) -> MeshDataCollection:...
    def GetSubDividedVertexAt(self, subentId: SubentityId) -> _n_2_t_1:...
    def GetSubDividedVertexAt(self, index: int) -> _n_2_t_1:...
    def GetSubentColor(self, subentId: SubentityId) -> _n_0_t_0:...
    def GetSubentMaterial(self, subentId: SubentityId) -> ObjectId:...
    def GetSubentMaterialMapper(self, subentId: SubentityId) -> _n_3_t_7:...
    def GetSubentPath(self, index: int, type: SubentityType) -> _n_6_t_10[FullSubentityPath]:...
    def GetVertexAt(self, subentId: SubentityId) -> _n_2_t_1:...
    def GetVertexAt(self, index: int) -> _n_2_t_1:...
    def MergeFaces(self, faces: _n_6_t_10[FullSubentityPath]):...
    def Setbox(self, xlen: float, ylen: float, zlen: float, divx: int, divy: int, divz: int, smoothLevel: int):...
    def SetCone(self, majorRadius: float, minorRadius: float, height: float, divAxis: int, divHeight: int, divCap: int, radiusRatio: float, smoothLevel: int):...
    def SetCrease(self, subentPaths: _n_6_t_10[FullSubentityPath], creaseVal: float):...
    def SetCrease(self, creaseVal: float):...
    def SetCylinder(self, majorRadius: float, minorRadius: float, height: float, divAxis: int, divHeight: int, divCap: int, smoothLevel: int):...
    def SetPyramid(self, radius: float, height: float, divLength: int, divHeight: int, divCap: int, nSides: int, radiusRatio: float, smoothLevel: int):...
    def SetSphere(self, radius: float, divAxis: int, divHeight: int, smoothLevel: int):...
    def SetSubDMesh(self, vertexArray: _n_2_t_10, indexArray: _n_2_t_24, smoothLevel: int):...
    def SetSubentColor(self, subentId: SubentityId, color: _n_0_t_0):...
    def SetSubentMaterial(self, subentId: SubentityId, matId: ObjectId):...
    def SetSubentMaterialMapper(self, subentId: SubentityId, mapper: _n_3_t_7):...
    def SetTorus(self, majorRadius: float, divSection: int, divSweepPath: int, sectionRadiusRatio: float, sectionRotate: float, smoothLevel: int):...
    def SetVertexAt(self, subentId: SubentityId, position: _n_2_t_1):...
    def SetVertexAt(self, index: int, position: _n_2_t_1):...
    def SetWedge(self, xLen: float, yLen: float, zLen: float, divLength: int, divWidth: int, divHeight: int, divSlope: int, divCap: int, smoothLevel: int):...
    def Spin(self, subentFaceId: SubentityId):...
    def SplitFace(self, subentFaceId: SubentityId, subent0: SubentityId, point0: _n_2_t_1, subent1: SubentityId, point1: _n_2_t_1):...
    def SubdDivideDown(self):...
    def SubdDivideUp(self):...
    def SubdRefine(self, paths: _n_6_t_10[FullSubentityPath]):...
    def SubdRefine(self):...
class SubentityGeometry(object):
    @property
    def Curve(self) -> _n_2_t_7:"""Curve { get; } -> Curve3d"""
    @property
    def Point(self) -> _n_2_t_1:"""Point { get; } -> Point3d"""
    @property
    def Type(self) -> SubentityType:"""Type { get; } -> SubentityType"""
    def __init__(self, curve: _n_2_t_7) -> SubentityGeometry:...
    def __init__(self, pnt: _n_2_t_1) -> SubentityGeometry:...
    def __init__(self) -> SubentityGeometry:...
class SubentityId(_n_6_t_12):
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def IndexPtr(self) -> _n_6_t_3:"""IndexPtr { get; } -> IntPtr"""
    @property
    def Null(self) -> SubentityId:"""Null { get; } -> SubentityId"""
    @property
    def Type(self) -> SubentityType:"""Type { get; } -> SubentityType"""
    @property
    def TypeClass(self) -> _n_5_t_0:"""TypeClass { get; } -> RXClass"""
    def __init__(self, classType: _n_5_t_0, i: _n_6_t_3) -> SubentityId:...
    def __init__(self, type: SubentityType, i: _n_6_t_3) -> SubentityId:...
    def __init__(self, classType: _n_5_t_0, i: int) -> SubentityId:...
    def __init__(self, type: SubentityType, i: int) -> SubentityId:...
class SubentityOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def AddSubentPaths(self, entity: Entity, paths: _n_6_t_10[FullSubentityPath]):...
    def DeleteSubentPaths(self, entity: Entity, paths: _n_6_t_10[FullSubentityPath]):...
    def GetCompoundObjectTransform(self, entity: Entity) -> _n_2_t_6:...
    def GetGripPointsAtSubentPath(self, entity: Entity, subPath: FullSubentityPath, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: _n_2_t_3, bitFlags: GetGripPointsFlags):...
    def GetGsMarkersAtSubentPath(self, entity: Entity, subPath: FullSubentityPath) -> _n_6_t_10[_n_6_t_3]:...
    def GetSubentClassId(self, entity: Entity, path: FullSubentityPath) -> _n_6_t_22:...
    def GetSubentPathGeomExtents(self, entity: Entity, path: FullSubentityPath) -> Extents3d:...
    def GetSubentPathsAtGsMarker(self, entity: Entity, type: SubentityType, gsMark: _n_6_t_3, pickPoint: _n_2_t_1, viewXform: _n_2_t_6, entAndInsertStack: _n_6_t_10[ObjectId]) -> _n_6_t_10[FullSubentityPath]:...
    def MoveGripPointsAtSubentPaths(self, entity: Entity, path: _n_6_t_10[FullSubentityPath], grips: GripDataCollection, offset: _n_2_t_3, bitFlags: MoveGripPointsFlags):...
    def OnSubentGripStatusChanged(self, entity: Entity, status: GripStatus, subentity: FullSubentityPath):...
    def SubentPtr(self, entity: Entity, id: FullSubentityPath) -> Entity:...
    def TransformSubentPathsBy(self, entity: Entity, paths: _n_6_t_10[FullSubentityPath], xform: _n_2_t_6):...
class SubentityType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Class: int
    Edge: int
    Face: int
    MlineCache: int
    Null: int
    value__: int
    Vertex: int
class SubentRef(GeomRef, _n_6_t_0, _n_6_t_1):
    @property
    def Entity(self) -> CompoundObjectId:"""Entity { get; } -> CompoundObjectId"""
    @property
    def SubentId(self) -> SubentityId:"""SubentId { get; } -> SubentityId"""
    def CreateEntity(self) -> Entity:...
class Sun(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def Altitude(self) -> float:"""Altitude { get; set; } -> float"""
    @property
    def Azimuth(self) -> float:"""Azimuth { get; set; } -> float"""
    @property
    def DateTime(self) -> _n_6_t_20:"""DateTime { get; set; } -> DateTime"""
    @property
    def Intensity(self) -> float:"""Intensity { get; set; } -> float"""
    @property
    def IsDaylightSavingsOn(self) -> bool:"""IsDaylightSavingsOn { get; set; } -> bool"""
    @property
    def IsOn(self) -> bool:"""IsOn { get; set; } -> bool"""
    @property
    def ShadowParameters(self) -> _n_3_t_15:"""ShadowParameters { get; set; } -> ShadowParameters"""
    @property
    def SkyParameters(self) -> _n_3_t_47:"""SkyParameters { get; set; } -> SkyParameters"""
    @property
    def SunColor(self) -> _n_0_t_0:"""SunColor { get; set; } -> Color"""
    @property
    def SunDirection(self) -> _n_2_t_3:"""SunDirection { get; set; } -> Vector3d"""
    def __init__(self) -> Sun:...
class Surface(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def CreationActionBodyId(self) -> ObjectId:"""CreationActionBodyId { get; } -> ObjectId"""
    @property
    def ModificationActionBodyIds(self) -> ObjectIdCollection:"""ModificationActionBodyIds { get; } -> ObjectIdCollection"""
    @property
    def Perimeter(self) -> float:"""Perimeter { get; } -> float"""
    @property
    def UIsoLineDensity(self) -> int:"""UIsoLineDensity { get; set; } -> int"""
    @property
    def UsesGraphicsCache(self) -> bool:"""UsesGraphicsCache { get; } -> bool"""
    @property
    def VIsoLineDensity(self) -> int:"""VIsoLineDensity { get; set; } -> int"""
    @property
    def WireframeType(self) -> Surface.WireframeTypeEnum:"""WireframeType { get; set; } -> Surface.WireframeTypeEnum"""
    def __init__(self) -> Surface:...
    def BooleanIntersect(self, solid: Solid3d) -> _n_6_t_10[Entity]:...
    def BooleanIntersect(self, surface2: Surface) -> _n_6_t_10[Entity]:...
    def BooleanSubtract(self, solid: Solid3d) -> Surface:...
    def BooleanSubtract(self, surface2: Surface) -> Surface:...
    def BooleanUnion(self, surface2: Surface) -> Surface:...
    def ChamferEdges(self, subentityIds: _n_6_t_10[SubentityId], baseSubentityId: SubentityId, baseDist: float, otherDist: float, associativeEnabled: bool):...
    def ChamferEdges(self, edgeSubentIds: _n_6_t_10[SubentityId], baseFaceSubentId: SubentityId, baseDist: float, otherDist: float):...
    def ConvertToNurbSurface(self) -> _n_6_t_10[NurbSurface]:...
    def ConvertToRegion(self) -> _n_6_t_10[Entity]:...
    @staticmethod
    def CreateBlendSurface(startProfile: LoftProfile, endProfile: LoftProfile, blendOptionsd: BlendOptions) -> Surface:...
    @staticmethod
    def CreateBlendSurface(startProfile: LoftProfile, endProfile: LoftProfile, blendOptions: BlendOptions, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateExtendSurface(sourceSurface: ObjectId, edges: _n_6_t_10[SubentityId], extension: float, extOption: Surface.EdgeExtensionType, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateExtrudedSurface(pSweep: Profile3d, directionVec: _n_2_t_3, sweepOptions: SweepOptions) -> ExtrudedSurface:...
    @staticmethod
    def CreateExtrudedSurface(pSweep: Profile3d, directionVec: _n_2_t_3, sweepOptions: SweepOptions, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateFilletSurface(surfId1: ObjectId, pickPt1: _n_2_t_1, surfId2: ObjectId, pickPt2: _n_2_t_1, radius: float, trimMode: FilletTrimMode, projDir: _n_2_t_3) -> Surface:...
    @staticmethod
    def CreateFilletSurface(surfId1: ObjectId, pickPt1: _n_2_t_1, surfId2: ObjectId, pickPt2: _n_2_t_1, radius: float, trimMode: FilletTrimMode, projDir: _n_2_t_3, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateFrom(fromEntity: Entity) -> Surface:...
    def CreateInterferenceObjects(self, ent: Entity, flags: int) -> _n_6_t_10[Entity]:...
    @staticmethod
    def CreateLoftedSurface(crossSections: _n_6_t_10[LoftProfile], guides: _n_6_t_10[LoftProfile], path: LoftProfile, loftOptions: LoftOptions) -> Surface:...
    @staticmethod
    def CreateLoftedSurface(crossSections: _n_6_t_10[LoftProfile], guides: _n_6_t_10[LoftProfile], path: LoftProfile, loftOptions: LoftOptions, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateNetworkSurface(uProfiles: _n_6_t_10[Profile3d], vProfiles: _n_6_t_10[Profile3d]) -> Surface:...
    @staticmethod
    def CreateNetworkSurface(uProfiles: _n_6_t_10[Profile3d], vProfiles: _n_6_t_10[Profile3d], associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateOffsetSurface(entity: Entity, offsetDistance: float) -> Entity:...
    @staticmethod
    def CreateOffsetSurface(entity: Entity, offsetDistance: float, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreatePatchSurface(inputPathRef: PathRef, constraintIds: ObjectIdCollection, continuity: int, bulge: float) -> Surface:...
    @staticmethod
    def CreatePatchSurface(inputPathRef: PathRef, constraintIds: ObjectIdCollection, continuity: int, bulge: float, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateRevolvedSurface(rev: Profile3d, axisEnt: Profile3d, flipAxisDirection: bool, revAngle: float, startAngle: float, revolveOptions: RevolveOptions) -> RevolvedSurface:...
    @staticmethod
    def CreateRevolvedSurface(rev: Profile3d, axisEnt: Profile3d, flipAxisDirection: bool, revAngle: float, startAngle: float, revolveOptions: RevolveOptions, associativeEnabled: bool) -> ObjectId:...
    @staticmethod
    def CreateRevolvedSurface(rev: Profile3d, axisPnt: _n_2_t_1, axisDir: _n_2_t_3, revAngle: float, startAngle: float, revolveOptions: RevolveOptions) -> RevolvedSurface:...
    @staticmethod
    def CreateRevolvedSurface(rev: Profile3d, axisPnt: _n_2_t_1, axisDir: _n_2_t_3, revAngle: float, startAngle: float, revolveOptions: RevolveOptions, associativeEnabled: bool) -> ObjectId:...
    def CreateSectionObjects(self, sectionPlane: _n_2_t_4) -> _n_6_t_10[Entity]:...
    @staticmethod
    def CreateSweptSurface(sweep: Profile3d, path: Profile3d, sweepOptions: SweepOptions) -> SweptSurface:...
    @staticmethod
    def CreateSweptSurface(sweep: Profile3d, path: Profile3d, sweepOptions: SweepOptions, associativeEnabled: bool) -> ObjectId:...
    def ExtendEdges(self, edges: _n_6_t_10[FullSubentityPath], extension: float, extOption: Surface.EdgeExtensionType, associativeEnabled: bool):...
    def FilletEdges(self, subentityIds: _n_6_t_10[SubentityId], radius: float, associativeEnabled: bool):...
    def FilletEdges(self, subentityIds: _n_6_t_10[SubentityId], radius: _n_2_t_13, startSetback: _n_2_t_13, endSetback: _n_2_t_13):...
    def GetArea(self) -> float:...
    def GetSubentityColor(self, subEntityId: SubentityId) -> _n_0_t_0:...
    def GetSubentityMaterial(self, subEntityId: SubentityId) -> ObjectId:...
    def GetSubentityMaterialMapper(self, subEntityId: SubentityId) -> _n_3_t_7:...
    def ImprintEntity(self, entityToImprint: Entity):...
    def ProjectOnToSurface(self, entityToProject: Entity, projectionDirection: _n_2_t_3) -> _n_6_t_10[Entity]:...
    def RayTest(self, rayBasePoint: _n_2_t_1, rayDir: _n_2_t_3, rayRadius: float, subEntIds: _n_6_t_10[SubentityId], parameters: _n_2_t_13):...
    def SetSubentityColor(self, subEntityId: SubentityId, color: _n_0_t_0):...
    def SetSubentityMaterial(self, subEntityId: SubentityId, materialId: ObjectId):...
    def SetSubentityMaterialMapper(self, subEntityId: SubentityId, mapper: _n_3_t_7):...
    def SliceByPlane(self, slicePlane: _n_2_t_4) -> SurfaceSliceResults:...
    def SliceBySurface(self, slicingSurface: Surface) -> SurfaceSliceResults:...
    def Thicken(self, thickness: float, bothSides: bool) -> Solid3d:...
    @staticmethod
    def TrimSurface(blankSurfaceId: ObjectId, toolSurfaceIds: ObjectIdCollection, toolCurveIds: ObjectIdCollection, projVectors: _n_2_t_9, pickPoint: _n_2_t_1, viewVector: _n_2_t_3, bAutoExtend: bool, associativeEnabled: bool):...
    class EdgeExtensionType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        ExtendEdge: int
        StretchEdge: int
        value__: int
    class WireframeTypeEnum(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Isolines: int
        IsoParms: int
        value__: int
class SurfaceSliceResults(_n_6_t_12):
    @property
    def NegativeHalfSurface(self) -> Surface:"""NegativeHalfSurface { get; set; } -> Surface"""
    @property
    def NewSurface(self) -> Surface:"""NewSurface { get; set; } -> Surface"""
    def __init__(self, negativeHalfSurface: Surface, newSurface: Surface) -> SurfaceSliceResults:...
class SurfaceTrimInfo(_n_5_t_3, _n_6_t_0):
    @property
    def IsCurve(self) -> bool:"""IsCurve { get; } -> bool"""
    @property
    def ProjVector(self) -> _n_2_t_3:"""ProjVector { get; set; } -> Vector3d"""
    @property
    def Relation(self) -> SurfaceTrimInfo.TrimRelation:"""Relation { get; set; } -> SurfaceTrimInfo.TrimRelation"""
    @property
    def ToolBodyId(self) -> CompoundObjectId:"""ToolBodyId { get; set; } -> CompoundObjectId"""
    def __init__(self) -> SurfaceTrimInfo:...
    def SetTrimInfo(self, surfaceId: CompoundObjectId, relation: SurfaceTrimInfo.TrimRelation, subEntityId: SubentityId):...
    def SetTrimInfo(self, curveId: CompoundObjectId, projVector: _n_2_t_3, relation: SurfaceTrimInfo.TrimRelation):...
    class TrimRelation(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        InsideTool: int
        OutsideTool: int
        value__: int
class SweepOptions(_n_5_t_3, _n_6_t_0, _n_6_t_1):
    @property
    def Align(self) -> SweepOptionsAlignOption:"""Align { get; } -> SweepOptionsAlignOption"""
    @property
    def AlignAngle(self) -> float:"""AlignAngle { get; } -> float"""
    @property
    def AlignStart(self) -> bool:"""AlignStart { get; } -> bool"""
    @property
    def Bank(self) -> bool:"""Bank { get; } -> bool"""
    @property
    def BasePoint(self) -> _n_2_t_1:"""BasePoint { get; } -> Point3d"""
    @property
    def CheckIntersections(self) -> bool:"""CheckIntersections { get; } -> bool"""
    @property
    def DraftAngle(self) -> float:"""DraftAngle { get; } -> float"""
    @property
    def EndDraftDist(self) -> float:"""EndDraftDist { get; } -> float"""
    @property
    def PathEntityTransform(self) -> _n_2_t_6:"""PathEntityTransform { get; } -> Matrix3d"""
    @property
    def ScaleFactor(self) -> float:"""ScaleFactor { get; } -> float"""
    @property
    def StartDraftDist(self) -> float:"""StartDraftDist { get; } -> float"""
    @property
    def SweepEntityTransform(self) -> _n_2_t_6:"""SweepEntityTransform { get; } -> Matrix3d"""
    @property
    def TwistAngle(self) -> float:"""TwistAngle { get; } -> float"""
    def __init__(self, opts: SweepOptions) -> SweepOptions:...
    def __init__(self) -> SweepOptions:...
    def CheckPathCurve(self, pathEnt: Entity, displayErrorMessages: bool):...
    def CheckSweepCurve(self, sweepEnt: Entity, displayErrorMessages: bool) -> SweepOptionsCheckSweepCurveOut:...
class SweepOptionsAlignOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AlignSweepEntityToPath: int
    NoAlignment: int
    TranslatePathToSweepEntity: int
    TranslateSweepEntityToPath: int
    value__: int
class SweepOptionsBuilder(object):
    @property
    def Align(self) -> SweepOptionsAlignOption:"""Align { get; set; } -> SweepOptionsAlignOption"""
    @property
    def AlignAngle(self) -> float:"""AlignAngle { get; set; } -> float"""
    @property
    def AlignStart(self) -> bool:"""AlignStart { get; set; } -> bool"""
    @property
    def Bank(self) -> bool:"""Bank { get; set; } -> bool"""
    @property
    def BasePoint(self) -> _n_2_t_1:"""BasePoint { get; set; } -> Point3d"""
    @property
    def CheckIntersections(self) -> bool:"""CheckIntersections { get; set; } -> bool"""
    @property
    def DraftAngle(self) -> float:"""DraftAngle { get; set; } -> float"""
    @property
    def EndDraftDist(self) -> float:"""EndDraftDist { get; set; } -> float"""
    @property
    def PathEntityTransform(self) -> _n_2_t_6:"""PathEntityTransform { get; set; } -> Matrix3d"""
    @property
    def ScaleFactor(self) -> float:"""ScaleFactor { get; set; } -> float"""
    @property
    def StartDraftDist(self) -> float:"""StartDraftDist { get; set; } -> float"""
    @property
    def SweepEntityTransform(self) -> _n_2_t_6:"""SweepEntityTransform { get; set; } -> Matrix3d"""
    @property
    def TwistAngle(self) -> float:"""TwistAngle { get; set; } -> float"""
    def __init__(self, value: SweepOptions) -> SweepOptionsBuilder:...
    def __init__(self) -> SweepOptionsBuilder:...
    def SetPathEntityTransform(self, pathEnt: Entity, displayErrorMessages: bool):...
    def SetSweepEntityTransform(self, sweepEntities: _n_6_t_10[Entity], displayErrorMessages: bool):...
    def ToSweepOptions(self) -> SweepOptions:...
class SweepOptionsCheckSweepCurveOut(object):
    @property
    def ApproximateArcLength(self) -> float:"""ApproximateArcLength { get; } -> float"""
    @property
    def Closed(self) -> bool:"""Closed { get; } -> bool"""
    @property
    def Planarity(self) -> Planarity:"""Planarity { get; } -> Planarity"""
    @property
    def Point(self) -> _n_2_t_1:"""Point { get; } -> Point3d"""
    @property
    def Vector(self) -> _n_2_t_3:"""Vector { get; } -> Vector3d"""
    def __init__(self) -> SweepOptionsCheckSweepCurveOut:...
class SweptSurface(Surface, _n_6_t_0, _n_6_t_1):
    @property
    def Bank(self) -> bool:"""Bank { get; set; } -> bool"""
    @property
    def PathEntity(self) -> Entity:"""PathEntity { get; } -> Entity"""
    @property
    def PathLength(self) -> float:"""PathLength { get; } -> float"""
    @property
    def PathProfile(self) -> Profile3d:"""PathProfile { get; } -> Profile3d"""
    @property
    def ProfileRotation(self) -> float:"""ProfileRotation { get; set; } -> float"""
    @property
    def ScaleAlongPath(self) -> float:"""ScaleAlongPath { get; set; } -> float"""
    @property
    def SweepEntity(self) -> Entity:"""SweepEntity { get; } -> Entity"""
    @property
    def SweepOptions(self) -> SweepOptions:"""SweepOptions { get; set; } -> SweepOptions"""
    @property
    def SweepProfile(self) -> Profile3d:"""SweepProfile { get; } -> Profile3d"""
    @property
    def TwistAlongPath(self) -> float:"""TwistAlongPath { get; set; } -> float"""
    def __init__(self) -> SweptSurface:...
class SymbolTable(DBObject, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    @property
    def IncludingErased(self) -> SymbolTable:"""IncludingErased { get; } -> SymbolTable"""
    @property
    def Item(self) -> ObjectId:"""Item { get; } -> ObjectId"""
    def Add(self, value: SymbolTableRecord) -> ObjectId:...
    def Has(self, id: ObjectId) -> bool:...
    def Has(self, key: str) -> bool:...
class SymbolTableEnumerator(_n_5_t_3, _n_6_t_0, _n_7_t_3):
    pass
class SymbolTableRecord(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def IsDependent(self) -> bool:"""IsDependent { get; } -> bool"""
    @property
    def IsResolved(self) -> bool:"""IsResolved { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
class SymbolUtilityServices(object):
    @property
    def BlockModelSpaceName(self) -> str:"""BlockModelSpaceName { get; } -> str"""
    @property
    def BlockPaperSpaceName(self) -> str:"""BlockPaperSpaceName { get; } -> str"""
    @property
    def LayerDefpointsName(self) -> str:"""LayerDefpointsName { get; } -> str"""
    @property
    def LayerZeroName(self) -> str:"""LayerZeroName { get; } -> str"""
    @property
    def LinetypeByBlockName(self) -> str:"""LinetypeByBlockName { get; } -> str"""
    @property
    def LinetypeByLayerName(self) -> str:"""LinetypeByLayerName { get; } -> str"""
    @property
    def LinetypeContinuousName(self) -> str:"""LinetypeContinuousName { get; } -> str"""
    @property
    def RegAppAcadName(self) -> str:"""RegAppAcadName { get; } -> str"""
    @property
    def TextStyleStandardName(self) -> str:"""TextStyleStandardName { get; } -> str"""
    @property
    def ViewportActiveName(self) -> str:"""ViewportActiveName { get; } -> str"""
    def __init__(self) -> SymbolUtilityServices:...
    @staticmethod
    def GetBlockModelSpaceId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def GetBlockNameFromInsertPathName(pathName: str) -> str:...
    @staticmethod
    def GetBlockPaperSpaceId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def GetInsertPathNameFromBlockName(blockName: str) -> str:...
    @staticmethod
    def GetLayerDefpointsId(database: Database) -> ObjectId:...
    @staticmethod
    def GetLayerZeroId(database: Database) -> ObjectId:...
    @staticmethod
    def GetLinetypeByBlockId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def GetLinetypeByLayerId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def GetLinetypeContinuousId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def GetMaxSymbolNameLength(isNewName: bool, compatibilityMode: bool) -> int:...
    @staticmethod
    def GetPathNameFromSymbolName(symbolName: str, extensions: str) -> str:...
    @staticmethod
    def GetRegAppAcadId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def GetSymbolNameFromPathName(pathName: str, extensions: str) -> str:...
    @staticmethod
    def GetTextStyleStandardId(databasePointer: Database) -> ObjectId:...
    @staticmethod
    def IsBlockLayoutName(name: str) -> bool:...
    @staticmethod
    def IsBlockModelSpaceName(name: str) -> bool:...
    @staticmethod
    def IsBlockPaperSpaceName(name: str) -> bool:...
    @staticmethod
    def IsCompatibilityMode(database: Database) -> bool:...
    @staticmethod
    def IsLayerDefpointsName(name: str) -> bool:...
    @staticmethod
    def IsLayerZeroName(name: str) -> bool:...
    @staticmethod
    def IsLinetypeByBlockName(name: str) -> bool:...
    @staticmethod
    def IsLinetypeByLayerName(name: str) -> bool:...
    @staticmethod
    def IsLinetypeContinuousName(name: str) -> bool:...
    @staticmethod
    def IsRegAppAcadName(name: str) -> bool:...
    @staticmethod
    def IsTextStyleStandardName(name: str) -> bool:...
    @staticmethod
    def IsViewportActiveName(name: str) -> bool:...
    @staticmethod
    def MakeDependentName(dwgName: str, symbolName: str) -> str:...
    @staticmethod
    def PreValidateSymbolName(symbolName: str, preserveCase: bool) -> str:...
    @staticmethod
    def RepairPreExtendedSymbolName(oldName: str, allowVerticalBar: bool) -> str:...
    @staticmethod
    def RepairSymbolName(oldName: str, allowVerticalBar: bool) -> str:...
    @staticmethod
    def ValidateCompatibleSymbolName(name: str, isNewName: bool, allowVerticalBar: bool, compatibilityMode: bool) -> _n_5_t_1:...
    @staticmethod
    def ValidatePreExtendedSymbolName(name: str, allowVerticalBar: bool):...
    @staticmethod
    def ValidateSymbolName(name: str, allowVerticalBar: bool):...
class SymmetricConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> SymmetricConstraint:...
class SystemVariableChangedEventArgs(_n_6_t_13):
    @property
    def Changed(self) -> bool:"""Changed { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class SystemVariableChangedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> SystemVariableChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: SystemVariableChangedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: SystemVariableChangedEventArgs):...
class SystemVariableChangingEventArgs(_n_6_t_13):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class SystemVariableChangingEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> SystemVariableChangingEventHandler:...
    def BeginInvoke(self, sender: object, e: SystemVariableChangingEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: SystemVariableChangingEventArgs):...
class Table(BlockReference, _n_6_t_0, _n_6_t_1, _n_7_t_0):
    @property
    def BreakEnabled(self) -> bool:"""BreakEnabled { get; set; } -> bool"""
    @property
    def BreakFlowDirection(self) -> TableBreakFlowDirection:"""BreakFlowDirection { get; set; } -> TableBreakFlowDirection"""
    @property
    def BreakOptions(self) -> TableBreakOptions:"""BreakOptions { get; set; } -> TableBreakOptions"""
    @property
    def Cells(self) -> CellRange:"""Cells { get; } -> CellRange"""
    @property
    def Columns(self) -> ColumnsCollection:"""Columns { get; } -> ColumnsCollection"""
    @property
    def Direction(self) -> _n_2_t_3:"""Direction { get; set; } -> Vector3d"""
    @property
    def FlowDirection(self) -> FlowDirection:"""FlowDirection { get; set; } -> FlowDirection"""
    @property
    def HasSubSelection(self) -> bool:"""HasSubSelection { get; } -> bool"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def HorizontalCellMargin(self) -> float:"""HorizontalCellMargin { get; set; } -> float"""
    @property
    def IsHeaderSuppressed(self) -> bool:"""IsHeaderSuppressed { get; set; } -> bool"""
    @property
    def IsTitleSuppressed(self) -> bool:"""IsTitleSuppressed { get; set; } -> bool"""
    @property
    def MinimumTableHeight(self) -> float:"""MinimumTableHeight { get; } -> float"""
    @property
    def MinimumTableWidth(self) -> float:"""MinimumTableWidth { get; } -> float"""
    @property
    def NumColumns(self) -> int:"""NumColumns { get; set; } -> int"""
    @property
    def NumRows(self) -> int:"""NumRows { get; set; } -> int"""
    @property
    def Rows(self) -> RowsCollection:"""Rows { get; } -> RowsCollection"""
    @property
    def SubSelection(self) -> CellRange:"""SubSelection { get; set; } -> CellRange"""
    @property
    def TableStyle(self) -> ObjectId:"""TableStyle { get; set; } -> ObjectId"""
    @property
    def TableStyleName(self) -> str:"""TableStyleName { get; } -> str"""
    @property
    def VerticalCellMargin(self) -> float:"""VerticalCellMargin { get; set; } -> float"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
    def __init__(self) -> Table:...
    def Alignment(self, row: int, col: int) -> CellAlignment:...
    def Alignment(self, type: RowType) -> CellAlignment:...
    def AttachmentPoint(self, row: int, col: int) -> _n_2_t_1:...
    def BackgroundColor(self, row: int, col: int) -> _n_0_t_0:...
    def BackgroundColor(self, type: RowType) -> _n_0_t_0:...
    def BlockRotation(self, row: int, col: int) -> float:...
    def BlockScale(self, row: int, col: int) -> float:...
    def BlockTableRecordId(self, row: int, col: int) -> ObjectId:...
    def CanDeleteColumns(self, index: int, nCount: int) -> bool:...
    def CanDeleteRows(self, index: int, nCount: int) -> bool:...
    def CanInsertColumn(self, index: int) -> bool:...
    def CanInsertRow(self, index: int) -> bool:...
    def CellStyleOverrides(self, row: int, col: int) -> _n_6_t_10[TableStyleOverride]:...
    def CellType(self, row: int, col: int) -> TableCellType:...
    def ClearSubSelection(self):...
    def ClearTableStyleOverrides(self, options: int):...
    def ColumnWidth(self, col: int) -> float:...
    def ContentColor(self, row: int, col: int) -> _n_0_t_0:...
    def ContentColor(self, type: RowType) -> _n_0_t_0:...
    def CreateContent(self, row: int, column: int, contentIndex: int) -> int:...
    def DataType(self, row: int, col: int) -> DataType:...
    def DataType(self, type: RowType) -> DataType:...
    def DeleteCellContent(self, row: int, col: int):...
    def DeleteColumns(self, col: int, columns: int):...
    def DeleteContent(self, A_0: CellRange):...
    def DeleteContent(self, row: int, column: int, contentIndex: int):...
    def DeleteContent(self, row: int, column: int):...
    def DeleteRows(self, row: int, rows: int):...
    def FieldId(self, row: int, col: int) -> ObjectId:...
    def Fill(self, fillRange: CellRange, sourceRange: CellRange, options: TableFillOptions):...
    def Format(self, row: int, col: int) -> str:...
    def Format(self, type: RowType) -> str:...
    def GenerateLayout(self):...
    def GetBlockAttributeValue(self, row: int, column: int, contentIndex: int, attDefId: ObjectId) -> str:...
    def GetBlockAttributeValue(self, row: int, col: int, attributeDefinitionId: ObjectId) -> str:...
    def GetBlockTableRecordId(self, row: int, column: int, contentIndex: int) -> ObjectId:...
    def GetBreakHeight(self, index: int) -> float:...
    def GetBreakOffset(self, index: int) -> _n_2_t_3:...
    def GetBreakSpacing(self) -> float:...
    def GetCellExtents(self, row: int, col: int, isOuterCell: bool, pts: _n_2_t_10):...
    def GetCellState(self, row: int, column: int) -> CellStates:...
    def GetCellStyle(self, row: int, column: int) -> str:...
    def GetColumnName(self, index: int) -> str:...
    def GetContentColor(self, row: int, column: int, contentIndex: int) -> _n_0_t_0:...
    def GetContentLayout(self, row: int, column: int) -> CellContentLayout:...
    def GetContentTypes(self, row: int, column: int, contentIndex: int) -> CellContentTypes:...
    def GetContentTypes(self, row: int, column: int) -> CellContentTypes:...
    def GetCustomData(self, row: int, column: int, key: str) -> object:...
    def GetCustomData(self, row: int, column: int) -> int:...
    def GetDataFormat(self, row: int, column: int, contentIndex: int) -> str:...
    def GetDataFormat(self, row: int, column: int) -> str:...
    def GetDataLink(self, range: CellRange) -> ObjectIdCollection:...
    def GetDataLink(self) -> ObjectIdCollection:...
    def GetDataLink(self, row: int, column: int) -> ObjectId:...
    def GetDataLinkRange(self, row: int, column: int) -> CellRange:...
    def GetDataType(self, row: int, column: int, contentIndex: int) -> DataTypeParameter:...
    def GetFieldId(self, row: int, column: int, contentIndex: int) -> ObjectId:...
    def GetFormula(self, row: int, column: int, contentIndex: int) -> str:...
    def GetGridColor(self, row: int, column: int, gridLineType: GridLineType) -> _n_0_t_0:...
    def GetGridDoubleLineSpacing(self, row: int, column: int, gridLineType: GridLineType) -> float:...
    def GetGridLineStyle(self, row: int, column: int, gridLineType: GridLineType) -> GridLineStyle:...
    def GetGridLinetype(self, row: int, column: int, gridLineType: GridLineType) -> ObjectId:...
    def GetGridLineWeight(self, row: int, column: int, gridLineType: GridLineType) -> LineWeight:...
    def GetGridProperty(self, row: int, column: int, gridLineType: GridLineType) -> GridPropertyParameter:...
    def GetGridVisibility(self, row: int, column: int, gridLineType: GridLineType) -> Visibility:...
    def GetIsAutoScale(self, row: int, column: int, contentIndex: int) -> bool:...
    def GetMargin(self, row: int, column: int, margin: CellMargins) -> float:...
    def GetMergeAllEnabled(self, row: int, column: int) -> bool:...
    def GetMergeRange(self, row: int, column: int) -> CellRange:...
    def GetNumberOfContents(self, row: int, column: int) -> int:...
    def GetOverrides(self, row: int, column: int, gridLineType: GridLineType) -> CellProperties:...
    def GetOverrides(self, row: int, column: int, contentIndex: int) -> CellProperties:...
    def GetRotation(self, row: int, column: int, contentIndex: int) -> float:...
    def GetScale(self, row: int, column: int, contentIndex: int) -> float:...
    def GetTextHeight(self, row: int, column: int, contentIndex: int) -> float:...
    def GetTextString(self, row: int, column: int, contentIndex: int, formatOption: FormatOption) -> str:...
    def GetTextString(self, row: int, column: int, contentIndex: int) -> str:...
    def GetTextStyleId(self, row: int, column: int, contentIndex: int) -> ObjectId:...
    def GetToolTip(self, row: int, column: int) -> str:...
    def GetValue(self, row: int, column: int, contentIndex: int, formatOption: FormatOption) -> object:...
    def GetValue(self, row: int, column: int, contentIndex: int) -> object:...
    def GridColor(self, row: int, col: int, edge: CellEdgeMasks) -> _n_0_t_0:...
    def GridColor(self, gridlineType: GridLineType, type: RowType) -> _n_0_t_0:...
    def GridLineWeight(self, row: int, col: int, edge: CellEdgeMasks) -> LineWeight:...
    def GridLineWeight(self, gridlineType: GridLineType, type: RowType) -> LineWeight:...
    def GridVisibility(self, row: int, col: int, edge: CellEdgeMasks) -> bool:...
    def GridVisibility(self, gridlineType: GridLineType, type: RowType) -> bool:...
    def HasFormula(self, row: int, column: int, contentIndex: int) -> bool:...
    def HitTest(self, point: _n_2_t_1, viewVector: _n_2_t_3) -> TableHitTestInfo:...
    def InsertColumns(self, col: int, width: float, columns: int):...
    def InsertColumnsAndInherit(self, col: int, inheritFrom: int, numCols: int):...
    def InsertRows(self, row: int, height: float, rows: int):...
    def InsertRowsAndInherit(self, index: int, inheritFrom: int, numRows: int):...
    def IsAutoScale(self, row: int, col: int) -> bool:...
    def IsBackgroundColorNone(self, row: int, col: int) -> bool:...
    def IsBackgroundColorNone(self, type: RowType) -> bool:...
    def IsContentEditable(self, row: int, column: int) -> bool:...
    def IsEmpty(self, row: int, column: int) -> bool:...
    def IsFormatEditable(self, row: int, column: int) -> bool:...
    def IsLinked(self, row: int, column: int) -> bool:...
    def IsMergedCell(self, row: int, col: int, range: CellRange) -> bool:...
    def MergeCells(self, range: CellRange):...
    def MinimumColumnWidth(self, col: int) -> float:...
    def MinimumRowHeight(self, row: int) -> float:...
    def MoveContent(self, row: int, column: int, fromIndex: int, toIndex: int):...
    def RecomputeTableBlock(self, forceUpdate: bool):...
    def RemoveAllOverrides(self, row: int, column: int):...
    def RemoveDataLink(self):...
    def RemoveDataLink(self, row: int, column: int):...
    def ReselectSubRegion(self, paths: _n_6_t_10[FullSubentityPath]):...
    def ResetValue(self, row: int, col: int):...
    def RowHeight(self, row: int) -> float:...
    def RowType(self, row: int) -> RowType:...
    def Select(self, pickingPoint: _n_2_t_1, hitTestViewDirection: _n_2_t_3, hitTestViewOrientation: _n_2_t_3, allowOutside: bool, inPickFirst: bool, paths: _n_6_t_10[FullSubentityPath]) -> TableHitTestInfo:...
    def SelectSubRegion(self, cornerPoint1: _n_2_t_1, cornerPoint2: _n_2_t_1, selectionViewDirection: _n_2_t_3, hitTestViewDirection: _n_2_t_3, selectionType: SelectType, includeCurrentSelection: bool, inPickFirst: bool, paths: _n_6_t_10[FullSubentityPath]) -> CellRange:...
    def SetAlignment(self, row: int, col: int, align: CellAlignment):...
    def SetAlignment(self, align: CellAlignment, rowTypes: int):...
    def SetAutoScale(self, row: int, col: int, autoFit: bool):...
    def SetBackgroundColor(self, row: int, col: int, color: _n_0_t_0):...
    def SetBackgroundColor(self, color: _n_0_t_0, rowTypes: int):...
    def SetBackgroundColorNone(self, row: int, col: int, value: bool):...
    def SetBackgroundColorNone(self, value: bool, rowTypes: int):...
    def SetBlockAttributeValue(self, row: int, column: int, contentIndex: int, attDefId: ObjectId, value: str):...
    def SetBlockAttributeValue(self, row: int, col: int, attributeDefinitionId: ObjectId, value: str):...
    def SetBlockRotation(self, row: int, col: int, rotationalAngle: float):...
    def SetBlockScale(self, row: int, col: int, scale: float):...
    def SetBlockTableRecordId(self, row: int, column: int, contentIndex: int, blockId: ObjectId, autoFit: bool):...
    def SetBlockTableRecordId(self, row: int, col: int, blockId: ObjectId, autoFit: bool):...
    def SetBreakHeight(self, index: int, height: float):...
    def SetBreakOffset(self, index: int, offset: _n_2_t_3):...
    def SetBreakSpacing(self, spacing: float):...
    def SetCellState(self, row: int, column: int, cellState: CellStates):...
    def SetCellStyle(self, row: int, column: int, styleName: str):...
    def SetCellType(self, row: int, col: int, type: TableCellType):...
    def SetColumnName(self, index: int, name: str):...
    def SetColumnWidth(self, width: float):...
    def SetColumnWidth(self, col: int, width: float):...
    def SetContentColor(self, row: int, column: int, contentIndex: int, color: _n_0_t_0):...
    def SetContentColor(self, row: int, col: int, color: _n_0_t_0):...
    def SetContentColor(self, color: _n_0_t_0, rowType: int):...
    def SetContentLayout(self, row: int, column: int, layout: CellContentLayout):...
    def SetCustomData(self, row: int, column: int, key: str, value: object):...
    def SetCustomData(self, row: int, column: int, data: int):...
    def SetDataFormat(self, row: int, column: int, contentIndex: int, format: str):...
    def SetDataFormat(self, row: int, column: int, format: str):...
    def SetDataLink(self, range: CellRange, dataLinkId: ObjectId, bUpdate: bool):...
    def SetDataLink(self, row: int, column: int, dataLinkId: ObjectId, bUpdate: bool):...
    def SetDataType(self, row: int, column: int, contentIndex: int, dataType: DataTypeParameter):...
    def SetDataType(self, row: int, col: int, nDataType: DataType, nUnitType: UnitType):...
    def SetDataType(self, nDataType: DataType, nUnitType: UnitType, rowTypes: int):...
    def SetFieldId(self, row: int, column: int, contentIndex: int, fieldId: ObjectId, option: CellOption):...
    def SetFieldId(self, row: int, col: int, fieldId: ObjectId):...
    def SetFormat(self, row: int, col: int, pFormat: str):...
    def SetFormat(self, pFormat: str, rowTypes: int):...
    def SetFormula(self, row: int, column: int, contentIndex: int, formula: str):...
    def SetGridColor(self, row: int, column: int, gridLineType: GridLineType, color: _n_0_t_0):...
    def SetGridColor(self, row: int, col: int, edges: int, color: _n_0_t_0):...
    def SetGridColor(self, color: _n_0_t_0, borders: int, rows: int):...
    def SetGridDoubleLineSpacing(self, row: int, column: int, gridLineType: GridLineType, spacing: float):...
    def SetGridLineStyle(self, row: int, column: int, gridLineType: GridLineType, lineStyle: GridLineStyle):...
    def SetGridLinetype(self, row: int, column: int, gridLineType: GridLineType, linetype: ObjectId):...
    def SetGridLineWeight(self, row: int, column: int, gridLineType: GridLineType, lineWeight: LineWeight):...
    def SetGridLineWeight(self, row: int, col: int, edges: int, value: LineWeight):...
    def SetGridLineWeight(self, lineWeight: LineWeight, borders: int, rows: int):...
    def SetGridProperty(self, rangeIn: CellRange, gridLineTypes: GridLineType, gridProp: GridPropertyParameter):...
    def SetGridProperty(self, row: int, column: int, gridLineType: GridLineType, gridProperty: GridPropertyParameter):...
    def SetGridVisibility(self, row: int, column: int, gridLineType: GridLineType, visibility: Visibility):...
    def SetGridVisibility(self, row: int, col: int, edges: int, value: bool):...
    def SetGridVisibility(self, visible: bool, borders: int, rows: int):...
    def SetIsAutoScale(self, row: int, column: int, contentIndex: int, autoFit: bool):...
    def SetMargin(self, row: int, column: int, margin: CellMargins, value: float):...
    def SetMergeAllEnabled(self, row: int, column: int, enable: bool):...
    def SetOverrides(self, row: int, column: int, gridLineType: GridLineType, override: CellProperties):...
    def SetOverrides(self, row: int, column: int, contentIndex: int, override: CellProperties):...
    def SetRotation(self, row: int, column: int, contentIndex: int, angle: float):...
    def SetRowHeight(self, height: float):...
    def SetRowHeight(self, row: int, height: float):...
    def SetScale(self, row: int, column: int, contentIndex: int, scale: float):...
    def SetSize(self, numRows: int, numCols: int):...
    def SetTextHeight(self, row: int, column: int, contentIndex: int, height: float):...
    def SetTextHeight(self, row: int, col: int, height: float):...
    def SetTextHeight(self, height: float, rowTypes: int):...
    def SetTextRotation(self, row: int, col: int, rot: RotationAngle):...
    def SetTextString(self, row: int, column: int, contentIndex: int, text: str):...
    def SetTextString(self, row: int, col: int, value: str):...
    def SetTextStyle(self, row: int, col: int, id: ObjectId):...
    def SetTextStyle(self, id: ObjectId, rowTypes: int):...
    def SetTextStyleId(self, row: int, column: int, contentIndex: int, id: ObjectId):...
    def SetToolTip(self, row: int, column: int, toolTip: str):...
    def SetValue(self, row: int, column: int, contentIndex: int, value: str, parseOption: ParseOption):...
    def SetValue(self, row: int, column: int, contentIndex: int, value: object, parseOption: ParseOption):...
    def SetValue(self, row: int, column: int, contentIndex: int, value: object):...
    def SetValue(self, row: int, col: int, pText: str, nOption: ParseOption):...
    def SetValue(self, row: int, col: int, pValue: object):...
    def SuppressRegenerateTable(self, suppress: bool):...
    def TableStyleOverrides(self) -> _n_6_t_10[TableStyleOverride]:...
    def TextHeight(self, row: int, col: int) -> float:...
    def TextHeight(self, type: RowType) -> float:...
    def TextRotation(self, row: int, col: int) -> RotationAngle:...
    def TextString(self, row: int, col: int, nOption: FormatOption) -> str:...
    def TextString(self, row: int, col: int) -> str:...
    def TextStringConst(self, row: int, col: int) -> str:...
    def TextStyle(self, row: int, col: int) -> ObjectId:...
    def TextStyle(self, type: RowType) -> ObjectId:...
    def UnitType(self, row: int, col: int) -> UnitType:...
    def UnitType(self, type: RowType) -> UnitType:...
    def UnmergeCells(self, range: CellRange):...
    def UpdateDataLink(self, dir: UpdateDirection, option: UpdateOption):...
    def UpdateDataLink(self, row: int, column: int, dir: UpdateDirection, option: UpdateOption):...
    def Value(self, row: int, col: int) -> object:...
class TableBreakFlowDirection(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DownOrUp: int
    Left: int
    Right: int
    value__: int
class TableBreakOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AllowManualHeights: int
    AllowManualPositions: int
    EnableBreaking: int
    _None: int
    RepeatBottomLabels: int
    RepeatTopLabels: int
    value__: int
class TableCellType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    BlockCell: int
    MultipleContentCell: int
    TextCell: int
    UnknownCell: int
    value__: int
class TableContent(FormattedTableData, _n_6_t_0, _n_6_t_1):
    @property
    def TableStyleId(self) -> ObjectId:"""TableStyleId { get; set; } -> ObjectId"""
    def __init__(self) -> TableContent:...
    def GetCellStyle(self, row: int, column: int) -> str:...
    def GetColumnWidth(self, column: int) -> float:...
    def GetRowHeight(self, row: int) -> float:...
    def SetCellStyle(self, row: int, column: int, cellStyle: str):...
    def SetColumnWidth(self, column: int, width: float):...
    def SetRowHeight(self, row: int, height: float):...
class TableCopyOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ConvertFormatToOverrides: int
    ExpandOrContractTable: int
    FillTarget: int
    _None: int
    OnlyContentModifiedAfterUpdate: int
    OnlyFormatModifiedAfterUpdate: int
    OverwriteContentModifiedAfterUpdate: int
    OverwriteFormatModifiedAfterUpdate: int
    OverwriteReadOnlyContent: int
    OverwriteReadOnlyFormat: int
    SkipBlock: int
    SkipCellState: int
    SkipCellStyle: int
    SkipContent: int
    SkipContentFormat: int
    SkipDataCell: int
    SkipDataLink: int
    SkipDissimilarContentFormat: int
    SkipField: int
    SkipFormat: int
    SkipFormula: int
    SkipGeometry: int
    SkipLabelCell: int
    SkipMerges: int
    SkipValue: int
    TableCopyColumnWidth: int
    TableCopyRowHeight: int
    value__: int
class TableEnumerator(_n_5_t_3, _n_6_t_0, _n_7_t_3):
    pass
class TableEnumeratorOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    IterateColumns: int
    IterateRows: int
    IterateSelection: int
    _None: int
    SkipMerged: int
    SkipReadOnlyContent: int
    SkipReadOnlyFormat: int
    value__: int
class TableFillOptions(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CopyContent: int
    CopyFormat: int
    GenerateSeries: int
    _None: int
    OverwriteReadOnlyContent: int
    OverwriteReadOnlyFormat: int
    Reverse: int
    Row: int
    value__: int
class TableHitTestInfo(_n_6_t_12):
    @property
    def Column(self) -> int:"""Column { get; } -> int"""
    @property
    def Row(self) -> int:"""Row { get; } -> int"""
    @property
    def Type(self) -> TableHitTestType:"""Type { get; } -> TableHitTestType"""
class TableHitTestType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Cell: int
    _None: int
    value__: int
class TableStyle(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def BitFlags(self) -> int:"""BitFlags { get; set; } -> int"""
    @property
    def CellStyles(self) -> _n_7_t_1:"""CellStyles { get; } -> ArrayList"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def FlowDirection(self) -> FlowDirection:"""FlowDirection { get; set; } -> FlowDirection"""
    @property
    def HorizontalCellMargin(self) -> float:"""HorizontalCellMargin { get; set; } -> float"""
    @property
    def IsHeaderSuppressed(self) -> bool:"""IsHeaderSuppressed { get; set; } -> bool"""
    @property
    def IsTitleSuppressed(self) -> bool:"""IsTitleSuppressed { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Template(self) -> ObjectId:"""Template { get; set; } -> ObjectId"""
    @property
    def VerticalCellMargin(self) -> float:"""VerticalCellMargin { get; set; } -> float"""
    def __init__(self) -> TableStyle:...
    def Alignment(self, rowType: RowType) -> CellAlignment:...
    def BackgroundColor(self, rowType: RowType) -> _n_0_t_0:...
    def CellClass(self, styleName: str) -> CellClass:...
    def Color(self, rowType: RowType) -> _n_0_t_0:...
    def DataType(self, rowType: RowType) -> DataType:...
    def Format(self, rowType: RowType) -> str:...
    def GridColor(self, gridLineType: GridLineType, rowType: RowType) -> _n_0_t_0:...
    def GridDoubleLineSpacing(self, gridLineType: GridLineType, styleName: str) -> float:...
    def GridLineStyle(self, gridLineType: GridLineType, styleName: str) -> GridLineStyle:...
    def GridLinetype(self, gridLineType: GridLineType, styleName: str) -> ObjectId:...
    def GridLineWeight(self, gridLineType: GridLineType, rowType: RowType) -> LineWeight:...
    def GridVisibility(self, gridLineType: GridLineType, rowType: RowType) -> bool:...
    def IsBackgroundColorNone(self, rowType: RowType) -> bool:...
    def Margin(self, cellMargin: CellMargins, styleName: str) -> float:...
    def PostTableStyleToDatabase(self, databasePointer: Database, styleName: str) -> ObjectId:...
    def SetAlignment(self, alignment: CellAlignment, rowTypes: int):...
    def SetBackgroundColor(self, color: _n_0_t_0, rowTypes: int):...
    def SetBackgroundColorNone(self, value: bool, rowTypes: int):...
    def SetCellClass(self, cellClass: CellClass, styleName: str):...
    def SetColor(self, color: _n_0_t_0, rowTypes: int):...
    def SetDataType(self, nDataType: DataType, nUnitType: UnitType, rowTypes: RowType):...
    def SetFormat(self, pFormat: str, rowTypes: RowType):...
    def SetGridColor(self, color: _n_0_t_0, gridLineTypes: int, rowTypes: int):...
    def SetGridDoubleLineSpacing(self, spacing: float, gridLineTypes: GridLineType, styleName: str):...
    def SetGridLineStyle(self, lineStyle: GridLineStyle, gridLineTypes: GridLineType, styleName: str):...
    def SetGridLinetype(self, linetype: ObjectId, gridLineTypes: GridLineType, styleName: str):...
    def SetGridLineWeight(self, lineWeight: LineWeight, gridLineTypes: int, rowTypes: int):...
    def SetGridVisibility(self, visible: bool, gridLineTypes: int, rowTypes: int):...
    def SetMargin(self, cellMargin: CellMargins, margin: float, styleName: str):...
    def SetTextHeight(self, value: float, cellStyle: str):...
    def SetTextHeight(self, height: float, rowTypes: int):...
    def SetTextStyle(self, id: ObjectId, styleName: str):...
    def SetTextStyle(self, id: ObjectId, rowTypes: int):...
    def TextHeight(self, cellStyle: str) -> float:...
    def TextHeight(self, rowType: RowType) -> float:...
    def TextStyle(self, styleName: str) -> ObjectId:...
    def TextStyle(self, rowType: RowType) -> ObjectId:...
    def UnitType(self, rowType: RowType) -> UnitType:...
class TableStyleFlags(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    HorizontalInsideLineFirst: int
    HorizontalInsideLineSecond: int
    HorizontalInsideLineThird: int
    TableStyleModified: int
    value__: int
class TableStyleOverride(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CellAlignment: int
    CellBackgroundColor: int
    CellBackgroundFillNone: int
    CellBottomGridColor: int
    CellBottomGridLineWeight: int
    CellBottomVisibility: int
    CellContentColor: int
    CellDataType: int
    CellLeftGridColor: int
    CellLeftGridLineWeight: int
    CellLeftVisibility: int
    CellRightGridColor: int
    CellRightGridLineWeight: int
    CellRightVisibility: int
    CellTextHeight: int
    CellTextStyle: int
    CellTopGridColor: int
    CellTopGridLineWeight: int
    CellTopVisibility: int
    DataHorizontalBottomColor: int
    DataHorizontalBottomLineWeight: int
    DataHorizontalBottomVisibility: int
    DataHorizontalInsideColor: int
    DataHorizontalInsideLineWeight: int
    DataHorizontalInsideVisibility: int
    DataHorizontalTopColor: int
    DataHorizontalTopLineWeight: int
    DataHorizontalTopVisibility: int
    DataRowAlignment: int
    DataRowColor: int
    DataRowDataType: int
    DataRowFillColor: int
    DataRowFillNone: int
    DataRowTextHeight: int
    DataRowTextStyle: int
    DataVerticalInsideColor: int
    DataVerticalInsideLineWeight: int
    DataVerticalInsideVisibility: int
    DataVerticalLeftColor: int
    DataVerticalLeftLineWeight: int
    DataVerticalLeftVisibility: int
    DataVerticalRightColor: int
    DataVerticalRightLineWeight: int
    DataVerticalRightVisibility: int
    FlowDirection: int
    HeaderHorizontalBottomColor: int
    HeaderHorizontalBottomLineWeight: int
    HeaderHorizontalBottomVisibility: int
    HeaderHorizontalInsideColor: int
    HeaderHorizontalInsideLineWeight: int
    HeaderHorizontalInsideVisibility: int
    HeaderHorizontalTopColor: int
    HeaderHorizontalTopLineWeight: int
    HeaderHorizontalTopVisibility: int
    HeaderRowAlignment: int
    HeaderRowColor: int
    HeaderRowDataType: int
    HeaderRowFillColor: int
    HeaderRowFillNone: int
    HeaderRowTextHeight: int
    HeaderRowTextStyle: int
    HeaderSuppressed: int
    HeaderVerticalInsideColor: int
    HeaderVerticalInsideLineWeight: int
    HeaderVerticalInsideVisibility: int
    HeaderVerticalLeftColor: int
    HeaderVerticalLeftLineWeight: int
    HeaderVerticalLeftVisibility: int
    HeaderVerticalRightColor: int
    HeaderVerticalRightLineWeight: int
    HeaderVerticalRightVisibility: int
    HorizontalCellMargin: int
    TitleHorizontalBottomColor: int
    TitleHorizontalBottomLineWeight: int
    TitleHorizontalBottomVisibility: int
    TitleHorizontalInsideColor: int
    TitleHorizontalInsideLineWeight: int
    TitleHorizontalInsideVisibility: int
    TitleHorizontalTopColor: int
    TitleHorizontalTopLineWeight: int
    TitleHorizontalTopVisibility: int
    TitleRowAlignment: int
    TitleRowColor: int
    TitleRowDataType: int
    TitleRowFillColor: int
    TitleRowFillNone: int
    TitleRowTextHeight: int
    TitleRowTextStyle: int
    TitleSuppressed: int
    TitleVerticalInsideColor: int
    TitleVerticalInsideLineWeight: int
    TitleVerticalInsideVisibility: int
    TitleVerticalLeftColor: int
    TitleVerticalLeftLineWeight: int
    TitleVerticalLeftVisibility: int
    TitleVerticalRightColor: int
    TitleVerticalRightLineWeight: int
    TitleVerticalRightVisibility: int
    value__: int
    VerticalCellMargin: int
class TableTemplate(TableContent, _n_6_t_0, _n_6_t_1):
    def __init__(self, table: Table, copyOption: TableCopyOptions) -> TableTemplate:...
    def Capture(self, table: Table, copyOption: TableCopyOptions):...
    def CreateTable(self, copyOption: TableCopyOptions) -> Table:...
class TangentConstraint(GeometricalConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> TangentConstraint:...
class TextAlignment(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CenterAlignment: int
    LeftAlignment: int
    RightAlignment: int
    value__: int
class TextAlignmentType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CenterAlignment: int
    LeftAlignment: int
    RightAlignment: int
    value__: int
class TextAngleType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AlwaysRightReadingAngle: int
    HorizontalAngle: int
    InsertAngle: int
    value__: int
class TextAttachmentDirection(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AttachmentHorizontal: int
    AttachmentVertical: int
    value__: int
class TextAttachmentType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AttachmentAllLine: int
    AttachmentBottomLine: int
    AttachmentBottomOfBottom: int
    AttachmentBottomOfTop: int
    AttachmentBottomOfTopLine: int
    AttachmentCenter: int
    AttachmentLinedCenter: int
    AttachmentMiddle: int
    AttachmentMiddleOfBottom: int
    AttachmentMiddleOfTop: int
    AttachmentTopOfTop: int
    value__: int
class TextEditor(_n_5_t_3, _n_6_t_0, ITextEditorSelectable):
    @property
    def ActualHeight(self) -> float:"""ActualHeight { get; } -> float"""
    @property
    def ActualWidth(self) -> float:"""ActualWidth { get; } -> float"""
    @property
    def Attachment(self) -> AttachmentPoint:"""Attachment { get; set; } -> AttachmentPoint"""
    @property
    def AutoCAPS(self) -> bool:"""AutoCAPS { get; set; } -> bool"""
    @property
    def AutoListEnabled(self) -> bool:"""AutoListEnabled { get; set; } -> bool"""
    @property
    def Columns(self) -> TextEditorColumns:"""Columns { get; } -> TextEditorColumns"""
    @property
    def Cursor(self) -> TextEditorCursor:"""Cursor { get; } -> TextEditorCursor"""
    @property
    def DefaultStackAlignment(self) -> TextEditorSelectionbase.FlowAlign:"""DefaultStackAlignment { get; set; } -> TextEditorSelectionbase.FlowAlign"""
    @property
    def DefaultStackScale(self) -> float:"""DefaultStackScale { get; set; } -> float"""
    @property
    def DefinedHeight(self) -> float:"""DefinedHeight { get; set; } -> float"""
    @property
    def DefinedWidth(self) -> float:"""DefinedWidth { get; set; } -> float"""
    @property
    def FontCount(self) -> int:"""FontCount { get; } -> int"""
    @property
    def IsAnnotativeStyle(self) -> bool:"""IsAnnotativeStyle { get; } -> bool"""
    @property
    def NumberingEnabled(self) -> bool:"""NumberingEnabled { get; set; } -> bool"""
    @property
    def Paragraphs(self) -> _n_6_t_10[TextEditorParagraph]:"""Paragraphs { get; } -> Array"""
    @property
    def Selection(self) -> TextEditorSelection:"""Selection { get; } -> TextEditorSelection"""
    @property
    def StackCount(self) -> int:"""StackCount { get; } -> int"""
    @property
    def Style(self) -> ObjectId:"""Style { get; set; } -> ObjectId"""
    @property
    def StyleCount(self) -> int:"""StyleCount { get; } -> int"""
    @property
    def TabOnlyDelimiter(self) -> bool:"""TabOnlyDelimiter { get; set; } -> bool"""
    @property
    def TextHeight(self) -> float:"""TextHeight { get; set; } -> float"""
    @property
    def VerticalSHX(self) -> bool:"""VerticalSHX { get; } -> bool"""
    @property
    def VerticalTTF(self) -> bool:"""VerticalTTF { get; } -> bool"""
    @property
    def Wipeout(self) -> TextEditorWipeout:"""Wipeout { get; } -> TextEditorWipeout"""
    def ClearSelection(self):...
    def Close(self, stat: TextEditor.ExitStatus):...
    @staticmethod
    def CreateTextEditor(mtext: MText) -> TextEditor:...
    def FindTextW(self, findString: str, findFlags: TextEditor.TextFindFlags, start: TextEditorLocation, end: TextEditorLocation):...
    def GetFont(self, index: int) -> Font:...
    def MakeSelection(self, start: TextEditorLocation, end: TextEditorLocation):...
    def Redraw(self):...
    def SelectAll(self):...
    class ExitStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        ExitQuit: int
        ExitSave: int
        value__: int
    class TextFindFlags(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        HalfFullForm: int
        IgnoreAccent: int
        MatchCase: int
        UseWildcards: int
        value__: int
        WholeWord: int
class TextEditorColumn(_n_5_t_3, _n_6_t_0, ITextEditorSelectable):
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
class TextEditorColumns(_n_5_t_3, _n_6_t_0, typing.Iterable[typing.Any]):
    @property
    def AutoHeight(self) -> bool:"""AutoHeight { get; set; } -> bool"""
    @property
    def Count(self) -> int:"""Count { get; set; } -> int"""
    @property
    def Gutter(self) -> float:"""Gutter { get; set; } -> float"""
    @property
    def IsFlowReversed(self) -> bool:"""IsFlowReversed { get; set; } -> bool"""
    @property
    def Item(self) -> TextEditorColumn:"""Item { get; } -> TextEditorColumn"""
    @property
    def MaxCount(self) -> int:"""MaxCount { get; } -> int"""
    @property
    def TotalWidth(self) -> float:"""TotalWidth { get; set; } -> float"""
    @property
    def Type(self) -> ColumnType:"""Type { get; set; } -> ColumnType"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
class TextEditorCursor(TextEditorSelectionbase, _n_6_t_0):
    @property
    def Column(self) -> TextEditorColumn:"""Column { get; } -> TextEditorColumn"""
    @property
    def Location(self) -> TextEditorLocation:"""Location { get; set; } -> TextEditorLocation"""
    @property
    def Paragraph(self) -> TextEditorParagraph:"""Paragraph { get; } -> TextEditorParagraph"""
class TextEditorLocation(_n_5_t_3, _n_6_t_0):
    pass
class TextEditorParagraph(_n_5_t_3, _n_6_t_0, ITextEditorSelectable):
    @property
    def Alignment(self) -> TextEditorParagraph.AlignmentType:"""Alignment { get; set; } -> TextEditorParagraph.AlignmentType"""
    @property
    def FirstIndent(self) -> float:"""FirstIndent { get; set; } -> float"""
    @property
    def LeftIndent(self) -> float:"""LeftIndent { get; set; } -> float"""
    @property
    def LineSpaceFactor(self) -> float:"""LineSpaceFactor { get; set; } -> float"""
    @property
    def LineSpaceStyle(self) -> TextEditorParagraph.LineSpacingStyle:"""LineSpaceStyle { get; set; } -> TextEditorParagraph.LineSpacingStyle"""
    @property
    def MaxLineSpacingFactor(self) -> float:"""MaxLineSpacingFactor { get; } -> float"""
    @property
    def MaxSpacingValue(self) -> float:"""MaxSpacingValue { get; } -> float"""
    @property
    def MinLineSpacingFactor(self) -> float:"""MinLineSpacingFactor { get; } -> float"""
    @property
    def MinSpacingValue(self) -> float:"""MinSpacingValue { get; } -> float"""
    @property
    def ParaNumberingType(self) -> TextEditorParagraph.NumberingType:"""ParaNumberingType { get; set; } -> TextEditorParagraph.NumberingType"""
    @property
    def RightIndent(self) -> float:"""RightIndent { get; set; } -> float"""
    @property
    def SpaceAfter(self) -> float:"""SpaceAfter { get; set; } -> float"""
    @property
    def SpaceBefore(self) -> float:"""SpaceBefore { get; set; } -> float"""
    @property
    def TabsCount(self) -> int:"""TabsCount { get; } -> int"""
    def AddTab(self, tab: TextEditorParagraphTab):...
    def ContinueNumbering(self):...
    def GetTab(self, idx: int) -> TextEditorParagraphTab:...
    def RemoveTab(self, tab: TextEditorParagraphTab):...
    def RestartNumbering(self):...
    class AlignmentType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        AlignmentCenter: int
        AlignmentDefault: int
        AlignmentDistribute: int
        AlignmentJustify: int
        AlignmentLeft: int
        AlignmentRight: int
        value__: int
    class LineSpacingStyle(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        LineSpacingAtLeast: int
        LineSpacingDefault: int
        LineSpacingExactly: int
        LineSpacingMultiple: int
        value__: int
    class NumberingType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        Bullet: int
        LetterLower: int
        LetterLowerWide: int
        LetterUpper: int
        LetterUpperWide: int
        Number: int
        NumberWide: int
        Off: int
        value__: int
class TextEditorParagraphTab(_n_6_t_12):
    @property
    def DecimalChar(self) -> _n_6_t_18:"""DecimalChar { get; set; } -> Char"""
    @property
    def Offset(self) -> float:"""Offset { get; set; } -> float"""
    @property
    def Type(self) -> TextEditorParagraphTab.ParagraphTabType:"""Type { get; set; } -> TextEditorParagraphTab.ParagraphTabType"""
    def __init__(self) -> TextEditorParagraphTab:...
    class ParagraphTabType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        CenterTab: int
        DecimalTab: int
        LeftTab: int
        RightTab: int
        value__: int
class TextEditorSelection(TextEditorSelectionbase, _n_6_t_0):
    @property
    def CanChangeCase(self) -> bool:"""CanChangeCase { get; } -> bool"""
    @property
    def CanStack(self) -> bool:"""CanStack { get; } -> bool"""
    @property
    def CanUnStack(self) -> bool:"""CanUnStack { get; } -> bool"""
    @property
    def FieldObject(self) -> Field:"""FieldObject { get; } -> Field"""
    @property
    def Paragraphs(self) -> _n_6_t_10[TextEditorParagraph]:"""Paragraphs { get; } -> Array"""
    @property
    def SelectionString(self) -> str:"""SelectionString { get; } -> str"""
    @property
    def SingleFieldSelected(self) -> bool:"""SingleFieldSelected { get; } -> bool"""
    @property
    def SingleStackSelected(self) -> bool:"""SingleStackSelected { get; } -> bool"""
    @property
    def StackSettings(self) -> TextEditorStack:"""StackSettings { get; set; } -> TextEditorStack"""
    def CanSupportFont(self, font: Font) -> bool:...
    def CanSupportLanguage(self, charset: int) -> bool:...
    def ChangeToLowercase(self) -> bool:...
    def ChangeToUppercase(self) -> bool:...
    def CombineParagraphs(self):...
    def ConvertToPlainText(self):...
    def RemoveAllFormatting(self):...
    def RemoveCharacterFormatting(self):...
    def RemoveParagraphFormatting(self):...
    def Stack(self):...
    def UnStack(self):...
    def UpdateField(self):...
class TextEditorSelectionbase(_n_5_t_3, _n_6_t_0):
    @property
    def Bold(self) -> bool:"""Bold { get; set; } -> bool"""
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; set; } -> Color"""
    @property
    def FlowAlignment(self) -> TextEditorSelectionbase.FlowAlign:"""FlowAlignment { get; set; } -> TextEditorSelectionbase.FlowAlign"""
    @property
    def Font(self) -> Font:"""Font { get; set; } -> Font"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def Italic(self) -> bool:"""Italic { get; set; } -> bool"""
    @property
    def Language(self) -> int:"""Language { get; set; } -> int"""
    @property
    def MaxObliqueAngle(self) -> float:"""MaxObliqueAngle { get; } -> float"""
    @property
    def MaxTrackingFactor(self) -> float:"""MaxTrackingFactor { get; } -> float"""
    @property
    def MaxWidthScale(self) -> float:"""MaxWidthScale { get; } -> float"""
    @property
    def MinObliqueAngle(self) -> float:"""MinObliqueAngle { get; } -> float"""
    @property
    def MinTrackingFactor(self) -> float:"""MinTrackingFactor { get; } -> float"""
    @property
    def MinWidthScale(self) -> float:"""MinWidthScale { get; } -> float"""
    @property
    def ObliqueAngle(self) -> float:"""ObliqueAngle { get; set; } -> float"""
    @property
    def Overline(self) -> bool:"""Overline { get; set; } -> bool"""
    @property
    def Strikethrough(self) -> bool:"""Strikethrough { get; set; } -> bool"""
    @property
    def TrackingFactor(self) -> float:"""TrackingFactor { get; set; } -> float"""
    @property
    def Underline(self) -> bool:"""Underline { get; set; } -> bool"""
    @property
    def WidthScale(self) -> float:"""WidthScale { get; set; } -> float"""
    def InputSpecialChar(self, ch: _n_6_t_18):...
    def InsertColumnBreak(self):...
    def InsertImportedText(self, type: TextEditorSelectionbase.InsertTextType, data: _n_6_t_10[_n_6_t_19]):...
    def InsertString(self, string: str):...
    def InsertSymbol(self, ch: _n_6_t_18, langId: int):...
    class FlowAlign(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        FlowBase: int
        FlowCenter: int
        FlowTop: int
        value__: int
    class InsertTextType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        DTextFormat: int
        MTextFormat: int
        MultibyteTextFormat: int
        RichTextFormat: int
        UnicodeDTextFormat: int
        UnicodeMTextFormat: int
        UnicodeTextFormat: int
        value__: int
class TextEditorStack(_n_6_t_12):
    @property
    def Bottom(self) -> str:"""Bottom { get; set; } -> str"""
    @property
    def DecimalChar(self) -> _n_6_t_18:"""DecimalChar { get; set; } -> Char"""
    @property
    def FlowAlign(self) -> TextEditorSelectionbase.FlowAlign:"""FlowAlign { get; set; } -> TextEditorSelectionbase.FlowAlign"""
    @property
    def MaxStackScale(self) -> float:"""MaxStackScale { get; } -> float"""
    @property
    def MinStackScale(self) -> float:"""MinStackScale { get; } -> float"""
    @property
    def Scale(self) -> float:"""Scale { get; set; } -> float"""
    @property
    def Top(self) -> str:"""Top { get; set; } -> str"""
    @property
    def Type(self) -> TextEditorStack.StackType:"""Type { get; set; } -> TextEditorStack.StackType"""
    def __init__(self) -> TextEditorStack:...
    class StackType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
        DecimalStack: int
        DiagonalStack: int
        HorizontalStack: int
        ToleranceStack: int
        value__: int
class TextEditorWipeout(_n_5_t_3, _n_6_t_0):
    @property
    def BackgroundFillColor(self) -> _n_0_t_0:"""BackgroundFillColor { get; set; } -> Color"""
    @property
    def BackgroundFillEnabled(self) -> bool:"""BackgroundFillEnabled { get; set; } -> bool"""
    @property
    def BackgroundScaleFactor(self) -> float:"""BackgroundScaleFactor { get; set; } -> float"""
    @property
    def MaxBackgroundScaleFactor(self) -> float:"""MaxBackgroundScaleFactor { get; } -> float"""
    @property
    def MinBackgroundScaleFactor(self) -> float:"""MinBackgroundScaleFactor { get; } -> float"""
    @property
    def UseBackgroundColor(self) -> bool:"""UseBackgroundColor { get; set; } -> bool"""
class TextHorizontalMode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    TextAlign: int
    TextCenter: int
    TextFit: int
    TextLeft: int
    TextMid: int
    TextRight: int
    value__: int
class TextStyleTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class TextStyleTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def BigFontFileName(self) -> str:"""BigFontFileName { get; set; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; set; } -> str"""
    @property
    def FlagBits(self) -> _n_6_t_19:"""FlagBits { get; set; } -> Byte"""
    @property
    def Font(self) -> _n_3_t_48:"""Font { get; set; } -> FontDescriptor"""
    @property
    def IsShapeFile(self) -> bool:"""IsShapeFile { get; set; } -> bool"""
    @property
    def IsVertical(self) -> bool:"""IsVertical { get; set; } -> bool"""
    @property
    def ObliquingAngle(self) -> float:"""ObliquingAngle { get; set; } -> float"""
    @property
    def PriorSize(self) -> float:"""PriorSize { get; set; } -> float"""
    @property
    def TextSize(self) -> float:"""TextSize { get; set; } -> float"""
    @property
    def XScale(self) -> float:"""XScale { get; set; } -> float"""
    def __init__(self) -> TextStyleTableRecord:...
class TextVerticalMode(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    TextBase: int
    TextBottom: int
    TextTop: int
    TextVerticalMid: int
    value__: int
class ThreePointAngleConstraint(AngularConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self, type: AngularConstraint.AngularSectorType) -> ThreePointAngleConstraint:...
    def __init__(self) -> ThreePointAngleConstraint:...
class TimeZone(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AbuDhabi: int
    Adelaide: int
    Alaska: int
    Almaty: int
    Arizona: int
    Athens: int
    AtlanticCanada: int
    Azores: int
    Baghdad: int
    Bangkok: int
    Beijing: int
    Berlin: int
    Bogota: int
    Brasilia: int
    Brisbane: int
    BuenosAires: int
    Cairo: int
    CapeVerde: int
    Caracas: int
    Caucasus: int
    Central: int
    CentralAmerica: int
    Darwin: int
    Dhaka: int
    EastAfrica: int
    Eastern: int
    EasternEurope: int
    Ekaterinburg: int
    Fiji: int
    GMT: int
    Greenland: int
    Guam: int
    Harare: int
    Hawaii: int
    Helsinki: int
    Hobart: int
    Indiana: int
    InternationalDateLine: int
    Irkutsk: int
    Islamabad: int
    Jerusalem: int
    Kabul: int
    Kathmandu: int
    Kolkata: int
    Krasnoyarsk: int
    Magadan: int
    Mazatlan: int
    MexicoCity: int
    MidAtlantic: int
    MidwayIsland: int
    Monrovia: int
    Moscow: int
    Mountain: int
    Newfoundland: int
    Pacific: int
    Paris: int
    Perth: int
    Prague: int
    Rangoon: int
    Riyadh: int
    Santiago: int
    Sarajevo: int
    Saskatchewan: int
    Seoul: int
    Singapore: int
    SriLanka: int
    Sydney: int
    Taipei: int
    Tehran: int
    Tokyo: int
    Tonga: int
    UTC: int
    value__: int
    Vladivostock: int
    Wellington: int
    WestCentralAfrica: int
    Yakutsk: int
class Trace(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    def __init__(self, pointer1: _n_2_t_1, pointer2: _n_2_t_1, pointer3: _n_2_t_1, pointer4: _n_2_t_1) -> Trace:...
    def __init__(self) -> Trace:...
    def GetPointAt(self, index: int) -> _n_2_t_1:...
    def SetPointAt(self, index: int, pointValue: _n_2_t_1):...
class Transaction(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def TransactionManager(self) -> TransactionManager:"""TransactionManager { get; } -> TransactionManager"""
    def Abort(self):...
    def AddNewlyCreatedDBObject(self, obj: DBObject, add: bool):...
    def Commit(self):...
    def GetAllObjects(self) -> DBObjectCollection:...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject:...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool) -> DBObject:...
    def GetObject(self, id: ObjectId, mode: OpenMode) -> DBObject:...
class TransactionManager(_n_5_t_2, _n_6_t_0, _n_6_t_1):
    @property
    def NumberOfActiveTransactions(self) -> int:"""NumberOfActiveTransactions { get; } -> int"""
    @property
    def TopTransaction(self) -> Transaction:"""TopTransaction { get; } -> Transaction"""
    def AddNewlyCreatedDBObject(self, obj: DBObject, add: bool):...
    def GetAllObjects(self) -> DBObjectCollection:...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject:...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool) -> DBObject:...
    def GetObject(self, id: ObjectId, mode: OpenMode) -> DBObject:...
    def QueueForGraphicsFlush(self):...
    def StartOpenCloseTransaction(self) -> OpenCloseTransaction:...
    def StartTransaction(self) -> Transaction:...
class TransformOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def CloneMeForDragging(self, entity: Entity) -> bool:...
    def Explode(self, entity: Entity, entitySet: DBObjectCollection):...
    def GetTransformedCopy(self, entity: Entity, transform: _n_2_t_6) -> Entity:...
    def HideMeForDragging(self, entity: Entity) -> bool:...
    def TransformBy(self, entity: Entity, transform: _n_2_t_6):...
class TypedValue(_n_6_t_12):
    @property
    def TypeCode(self) -> int:"""TypeCode { get; } -> int"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
    def __init__(self, typeCode: int, value: object) -> TypedValue:...
    def __init__(self, typeCode: int) -> TypedValue:...
class TypeOfCoordinates(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CoordinateTypeGeographic: int
    CoordinateTypeGrid: int
    CoordinateTypeLocal: int
    CoordinateTypeUnknown: int
    value__: int
class UcsTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class UcsTableRecord(SymbolTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def Origin(self) -> _n_2_t_1:"""Origin { get; set; } -> Point3d"""
    @property
    def XAxis(self) -> _n_2_t_3:"""XAxis { get; set; } -> Vector3d"""
    @property
    def YAxis(self) -> _n_2_t_3:"""YAxis { get; set; } -> Vector3d"""
    def __init__(self) -> UcsTableRecord:...
    def GetUcsBaseOrigin(self, view: OrthographicView) -> _n_2_t_1:...
    def SetUcsBaseOrigin(self, origin: _n_2_t_1, view: OrthographicView):...
class UnderlayDefinition(DBObject, _n_6_t_0, _n_6_t_1):
    @property
    def ActiveFileName(self) -> str:"""ActiveFileName { get; } -> str"""
    @property
    def ItemName(self) -> str:"""ItemName { get; set; } -> str"""
    @property
    def Loaded(self) -> bool:"""Loaded { get; } -> bool"""
    @property
    def SourceFileName(self) -> str:"""SourceFileName { get; set; } -> str"""
    @property
    def UnderlayItem(self) -> UnderlayItem:"""UnderlayItem { get; } -> UnderlayItem"""
    @staticmethod
    def GetDictionaryKey(underlayDefinitionType: _n_6_t_25) -> str:...
    def Load(self, password: str):...
    def SetUnderlayItem(self, sourceFileName: str, activeFileName: str, item: UnderlayItem):...
    def Unload(self):...
class UnderlayFile(_n_5_t_3, _n_6_t_0):
    @property
    def Items(self) -> UnderlayItemCollection:"""Items { get; } -> UnderlayItemCollection"""
class UnderlayHost(object):
    @property
    def DgnDocHost(self) -> UnderlayHost:"""DgnDocHost { get; } -> UnderlayHost"""
    @property
    def DgnHost(self) -> UnderlayHost:"""DgnHost { get; } -> UnderlayHost"""
    @property
    def DwfHost(self) -> UnderlayHost:"""DwfHost { get; } -> UnderlayHost"""
    @property
    def PdfHost(self) -> UnderlayHost:"""PdfHost { get; } -> UnderlayHost"""
    def GetFile(self, path: str, password: str) -> UnderlayFile:...
class UnderlayItem(_n_5_t_3, _n_6_t_0):
    @property
    def Extents(self) -> Extents2d:"""Extents { get; } -> Extents2d"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Thumbnail(self) -> _n_11_t_0:"""Thumbnail { get; } -> Bitmap"""
    @property
    def Units(self) -> UnitsValue:"""Units { get; } -> UnitsValue"""
    @property
    def UsingPartialContent(self) -> bool:"""UsingPartialContent { get; } -> bool"""
class UnderlayItemCollection(_n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> UnderlayItem:"""Item { get; } -> UnderlayItem"""
class UnderlayLayer(_n_5_t_3, _n_6_t_0):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def State(self) -> UnderlayLayerState:"""State { get; set; } -> UnderlayLayerState"""
    def __init__(self) -> UnderlayLayer:...
class UnderlayLayerCollection(_n_7_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> UnderlayLayer:"""Item { get; set; } -> UnderlayLayer"""
class UnderlayLayerState(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Off: int
    On: int
    value__: int
class UnderlayReference(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def AdjustColorForBackground(self) -> bool:"""AdjustColorForBackground { get; set; } -> bool"""
    @property
    def Contrast(self) -> int:"""Contrast { get; set; } -> int"""
    @property
    def ContrastLowerLimit(self) -> int:"""ContrastLowerLimit { get; } -> int"""
    @property
    def ContrastUpperLimit(self) -> int:"""ContrastUpperLimit { get; } -> int"""
    @property
    def DefaultContrast(self) -> int:"""DefaultContrast { get; } -> int"""
    @property
    def DefaultFade(self) -> int:"""DefaultFade { get; } -> int"""
    @property
    def DefinitionId(self) -> ObjectId:"""DefinitionId { get; set; } -> ObjectId"""
    @property
    def Fade(self) -> int:"""Fade { get; set; } -> int"""
    @property
    def FadeLowerLimit(self) -> int:"""FadeLowerLimit { get; } -> int"""
    @property
    def FadeUpperLimit(self) -> int:"""FadeUpperLimit { get; } -> int"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def IsClipInverted(self) -> bool:"""IsClipInverted { get; set; } -> bool"""
    @property
    def IsClipped(self) -> bool:"""IsClipped { get; set; } -> bool"""
    @property
    def IsOn(self) -> bool:"""IsOn { get; set; } -> bool"""
    @property
    def Monochrome(self) -> bool:"""Monochrome { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NameOfSheet(self) -> str:"""NameOfSheet { get; set; } -> str"""
    @property
    def Normal(self) -> _n_2_t_3:"""Normal { get; set; } -> Vector3d"""
    @property
    def Path(self) -> str:"""Path { get; set; } -> str"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def ScaleFactors(self) -> _n_2_t_11:"""ScaleFactors { get; set; } -> Scale3d"""
    @property
    def Transform(self) -> _n_2_t_6:"""Transform { get; set; } -> Matrix3d"""
    @property
    def UnderlayLayerCollection(self) -> UnderlayLayerCollection:"""UnderlayLayerCollection { get; } -> UnderlayLayerCollection"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
    def GenerateClipBoundaryFromPline(self, polyId: ObjectId):...
    def GetClipBoundary(self) -> _n_6_t_10[_n_2_t_0]:...
    def SetClipBoundary(self, points: _n_6_t_10[_n_2_t_0]):...
class Unit(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Angstroms: int
    Astronomical: int
    Centimeter: int
    Decimeters: int
    Dekameters: int
    Foot: int
    GigaMeters: int
    Hectometers: int
    Inch: int
    Kilometer: int
    LightYears: int
    Meter: int
    Microinches: int
    Microns: int
    Mile: int
    Millimeter: int
    Mils: int
    Nanometers: int
    _None: int
    Parsecs: int
    value__: int
    Yard: int
class UnitsConverter(_n_10_t_1):
    def __init__(self) -> UnitsConverter:...
    @staticmethod
    def GetConversionFactor(_from: UnitsValue, to: UnitsValue) -> float:...
class UnitsValue(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Angstroms: int
    Astronomical: int
    Centimeters: int
    Decimeters: int
    Dekameters: int
    Feet: int
    Gigameters: int
    Hectometers: int
    Inches: int
    Kilometers: int
    LightYears: int
    Meters: int
    MicroInches: int
    Microns: int
    Miles: int
    Millimeters: int
    Mils: int
    Nanometers: int
    Parsecs: int
    Undefined: int
    value__: int
    Yards: int
class UnitType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Angle: int
    AngleNotTransformed: int
    Area: int
    Currency: int
    Distance: int
    Percentage: int
    Unitless: int
    value__: int
    Volume: int
class UnitTypeAttribute(_n_6_t_15, _n_14_t_0):
    @property
    def UnitType(self) -> UnitType:"""UnitType { get; } -> UnitType"""
    def __init__(self, flags: UnitType) -> UnitTypeAttribute:...
class UpdateAction(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Ignore: int
    _None: int
    UpdateRequired: int
    value__: int
class UpdateDirection(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    DataToSource: int
    SourceToData: int
    value__: int
class UpdateOption(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    AllowSourceUpdate: int
    ForceFullSourceUpdate: int
    ForPreview: int
    IncludeXrefs: int
    _None: int
    OverwriteContentModifiedAfterUpdate: int
    OverwriteFormatModifiedAfterUpdate: int
    SkipFormat: int
    UpdateColumnWidth: int
    UpdateRowHeight: int
    value__: int
class Vertex(Entity, _n_6_t_0, _n_6_t_1):
    pass
class Vertex2d(Vertex, _n_6_t_0, _n_6_t_1):
    @property
    def Bulge(self) -> float:"""Bulge { get; set; } -> float"""
    @property
    def EndWidth(self) -> float:"""EndWidth { get; set; } -> float"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def StartWidth(self) -> float:"""StartWidth { get; set; } -> float"""
    @property
    def Tangent(self) -> float:"""Tangent { get; set; } -> float"""
    @property
    def TangentUsed(self) -> bool:"""TangentUsed { get; set; } -> bool"""
    @property
    def VertexType(self) -> Vertex2dType:"""VertexType { get; } -> Vertex2dType"""
    def __init__(self, position: _n_2_t_1, bulge: float, startWidth: float, endWidth: float, tangent: float) -> Vertex2d:...
    def __init__(self) -> Vertex2d:...
class Vertex2dType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    CurveFitVertex: int
    SimpleVertex: int
    SplineControlVertex: int
    SplineFitVertex: int
    value__: int
class Vertex3dType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    ControlVertex: int
    FitVertex: int
    SimpleVertex: int
    value__: int
class VertexRef(SubentRef, _n_6_t_0, _n_6_t_1):
    @property
    def Point(self) -> _n_2_t_1:"""Point { get; } -> Point3d"""
    def __init__(self, point: _n_2_t_1) -> VertexRef:...
    def __init__(self, entity: Entity) -> VertexRef:...
    def __init__(self, path: FullSubentityPath) -> VertexRef:...
    def __init__(self, compoundObjectId: CompoundObjectId, subentId: SubentityId, point: _n_2_t_1) -> VertexRef:...
    def __init__(self, compoundObjectId: CompoundObjectId, subentId: SubentityId) -> VertexRef:...
    def __init__(self, compoundObjectId: CompoundObjectId) -> VertexRef:...
    def __init__(self) -> VertexRef:...
class VerticalConstraint(ParallelConstraint, _n_6_t_0, _n_6_t_1):
    def __init__(self) -> VerticalConstraint:...
class ViewBorder(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def Height(self) -> float:"""Height { get; } -> float"""
    @property
    def InsertionPoint(self) -> _n_2_t_1:"""InsertionPoint { get; } -> Point3d"""
    @property
    def InventorFileReference(self) -> str:"""InventorFileReference { get; } -> str"""
    @property
    def IsFirstAngleProjection(self) -> bool:"""IsFirstAngleProjection { get; } -> bool"""
    @property
    def RotationAngle(self) -> float:"""RotationAngle { get; } -> float"""
    @property
    def Scale(self) -> float:"""Scale { get; } -> float"""
    @property
    def ShadedDPI(self) -> _n_6_t_11:"""ShadedDPI { get; } -> UInt32"""
    @property
    def ViewportId(self) -> ObjectId:"""ViewportId { get; } -> ObjectId"""
    @property
    def Width(self) -> float:"""Width { get; } -> float"""
    def __init__(self) -> ViewBorder:...
    def GetSourceType(self) -> SourceType:...
    def GetViewStyleType(self) -> ViewStyleType:...
class Viewport(Entity, _n_6_t_0, _n_6_t_1):
    @property
    def AmbientLightColor(self) -> _n_0_t_0:"""AmbientLightColor { get; set; } -> Color"""
    @property
    def AnnotationScale(self) -> AnnotationScale:"""AnnotationScale { get; set; } -> AnnotationScale"""
    @property
    def BackClipDistance(self) -> float:"""BackClipDistance { get; set; } -> float"""
    @property
    def BackClipOn(self) -> bool:"""BackClipOn { get; set; } -> bool"""
    @property
    def Background(self) -> ObjectId:"""Background { get; set; } -> ObjectId"""
    @property
    def Brightness(self) -> float:"""Brightness { get; set; } -> float"""
    @property
    def CenterPoint(self) -> _n_2_t_1:"""CenterPoint { get; set; } -> Point3d"""
    @property
    def CircleSides(self) -> int:"""CircleSides { get; set; } -> int"""
    @property
    def Contrast(self) -> float:"""Contrast { get; set; } -> float"""
    @property
    def CustomScale(self) -> float:"""CustomScale { get; set; } -> float"""
    @property
    def DefaultLightingOn(self) -> bool:"""DefaultLightingOn { get; set; } -> bool"""
    @property
    def DefaultLightingType(self) -> DefaultLightingType:"""DefaultLightingType { get; set; } -> DefaultLightingType"""
    @property
    def EffectivePlotStyleSheet(self) -> str:"""EffectivePlotStyleSheet { get; } -> str"""
    @property
    def Elevation(self) -> float:"""Elevation { get; set; } -> float"""
    @property
    def FastZoomOn(self) -> bool:"""FastZoomOn { get; set; } -> bool"""
    @property
    def FrontClipAtEyeOn(self) -> bool:"""FrontClipAtEyeOn { get; set; } -> bool"""
    @property
    def FrontClipDistance(self) -> float:"""FrontClipDistance { get; set; } -> float"""
    @property
    def FrontClipOn(self) -> bool:"""FrontClipOn { get; set; } -> bool"""
    @property
    def GridAdaptive(self) -> bool:"""GridAdaptive { get; set; } -> bool"""
    @property
    def GridBoundToLimits(self) -> bool:"""GridBoundToLimits { get; set; } -> bool"""
    @property
    def GridFollow(self) -> bool:"""GridFollow { get; set; } -> bool"""
    @property
    def GridIncrement(self) -> _n_2_t_14:"""GridIncrement { get; set; } -> Vector2d"""
    @property
    def GridMajor(self) -> int:"""GridMajor { get; set; } -> int"""
    @property
    def GridOn(self) -> bool:"""GridOn { get; set; } -> bool"""
    @property
    def GridSubdivisionRestricted(self) -> bool:"""GridSubdivisionRestricted { get; set; } -> bool"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def HiddenLinesRemoved(self) -> bool:"""HiddenLinesRemoved { get; set; } -> bool"""
    @property
    def LensLength(self) -> float:"""LensLength { get; set; } -> float"""
    @property
    def LinkedToSheetView(self) -> bool:"""LinkedToSheetView { get; } -> bool"""
    @property
    def Locked(self) -> bool:"""Locked { get; set; } -> bool"""
    @property
    def NonRectClipEntityId(self) -> ObjectId:"""NonRectClipEntityId { get; set; } -> ObjectId"""
    @property
    def NonRectClipOn(self) -> bool:"""NonRectClipOn { get; set; } -> bool"""
    @property
    def Number(self) -> int:"""Number { get; } -> int"""
    @property
    def On(self) -> bool:"""On { get; set; } -> bool"""
    @property
    def PerspectiveOn(self) -> bool:"""PerspectiveOn { get; set; } -> bool"""
    @property
    def PlotAsRaster(self) -> bool:"""PlotAsRaster { get; } -> bool"""
    @property
    def PlotStyleSheet(self) -> str:"""PlotStyleSheet { get; set; } -> str"""
    @property
    def PlotWireframe(self) -> bool:"""PlotWireframe { get; } -> bool"""
    @property
    def ShadePlot(self) -> ShadePlotType:"""ShadePlot { get; set; } -> ShadePlotType"""
    @property
    def ShadePlotId(self) -> ObjectId:"""ShadePlotId { get; } -> ObjectId"""
    @property
    def SnapAngle(self) -> float:"""SnapAngle { get; set; } -> float"""
    @property
    def SnapBasePoint(self) -> _n_2_t_0:"""SnapBasePoint { get; set; } -> Point2d"""
    @property
    def SnapIncrement(self) -> _n_2_t_14:"""SnapIncrement { get; set; } -> Vector2d"""
    @property
    def SnapIsometric(self) -> bool:"""SnapIsometric { get; set; } -> bool"""
    @property
    def SnapIsoPair(self) -> int:"""SnapIsoPair { get; set; } -> int"""
    @property
    def SnapOn(self) -> bool:"""SnapOn { get; set; } -> bool"""
    @property
    def StandardScale(self) -> StandardScaleType:"""StandardScale { get; set; } -> StandardScaleType"""
    @property
    def SunId(self) -> ObjectId:"""SunId { get; } -> ObjectId"""
    @property
    def Thumbnail(self) -> _n_11_t_0:"""Thumbnail { get; set; } -> Bitmap"""
    @property
    def ToneOperatorParameters(self) -> _n_3_t_0:"""ToneOperatorParameters { get; set; } -> ToneOperatorParameters"""
    @property
    def Transparent(self) -> bool:"""Transparent { get; set; } -> bool"""
    @property
    def TwistAngle(self) -> float:"""TwistAngle { get; set; } -> float"""
    @property
    def UcsFollowModeOn(self) -> bool:"""UcsFollowModeOn { get; set; } -> bool"""
    @property
    def UcsIconAtOrigin(self) -> bool:"""UcsIconAtOrigin { get; set; } -> bool"""
    @property
    def UcsIconVisible(self) -> bool:"""UcsIconVisible { get; set; } -> bool"""
    @property
    def UcsName(self) -> ObjectId:"""UcsName { get; } -> ObjectId"""
    @property
    def UcsOrthographic(self) -> OrthographicView:"""UcsOrthographic { get; } -> OrthographicView"""
    @property
    def UcsPerViewport(self) -> bool:"""UcsPerViewport { get; set; } -> bool"""
    @property
    def ViewCenter(self) -> _n_2_t_0:"""ViewCenter { get; set; } -> Point2d"""
    @property
    def ViewDirection(self) -> _n_2_t_3:"""ViewDirection { get; set; } -> Vector3d"""
    @property
    def ViewHeight(self) -> float:"""ViewHeight { get; set; } -> float"""
    @property
    def ViewOrthographic(self) -> OrthographicView:"""ViewOrthographic { get; } -> OrthographicView"""
    @property
    def ViewTarget(self) -> _n_2_t_1:"""ViewTarget { get; set; } -> Point3d"""
    @property
    def Width(self) -> float:"""Width { get; set; } -> float"""
    def __init__(self) -> Viewport:...
    def FreezeLayersInViewport(self, layerIds: _n_7_t_3):...
    def GetFrozenLayers(self) -> ObjectIdCollection:...
    def GetPreviousBackground(self, type: _n_3_t_14) -> ObjectId:...
    def GetUcs(self, origin: _n_2_t_1, x: _n_2_t_3, y: _n_2_t_3):...
    def IsLayerFrozenInViewport(self, layerId: ObjectId) -> bool:...
    def SetPreviousBackground(self, value: ObjectId, type: _n_3_t_14):...
    def SetShadePlot(self, type: ShadePlotType, shadePlotId: ObjectId):...
    def SetSun(self, sun: DBObject) -> ObjectId:...
    def SetUcs(self, userCoordinateSystemId: ObjectId):...
    def SetUcs(self, view: OrthographicView):...
    def SetUcs(self, origin: _n_2_t_1, x: _n_2_t_3, y: _n_2_t_3):...
    def SetUcsToWorld(self):...
    def SetViewDirection(self, view: OrthographicView):...
    def ThawAllLayersInViewport(self):...
    def ThawLayersInViewport(self, layerIds: _n_7_t_3):...
    def UpdateDisplay(self):...
class ViewportTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class ViewportTableRecord(AbstractViewTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def CircleSides(self) -> int:"""CircleSides { get; set; } -> int"""
    @property
    def FastZoomsEnabled(self) -> bool:"""FastZoomsEnabled { get; set; } -> bool"""
    @property
    def GridAdaptive(self) -> bool:"""GridAdaptive { get; set; } -> bool"""
    @property
    def GridBoundToLimits(self) -> bool:"""GridBoundToLimits { get; set; } -> bool"""
    @property
    def GridEnabled(self) -> bool:"""GridEnabled { get; set; } -> bool"""
    @property
    def GridFollow(self) -> bool:"""GridFollow { get; set; } -> bool"""
    @property
    def GridIncrements(self) -> _n_2_t_0:"""GridIncrements { get; set; } -> Point2d"""
    @property
    def GridMajor(self) -> int:"""GridMajor { get; set; } -> int"""
    @property
    def GridSubdivisionRestricted(self) -> bool:"""GridSubdivisionRestricted { get; set; } -> bool"""
    @property
    def IconAtOrigin(self) -> bool:"""IconAtOrigin { get; set; } -> bool"""
    @property
    def IconEnabled(self) -> bool:"""IconEnabled { get; set; } -> bool"""
    @property
    def IsometricSnapEnabled(self) -> bool:"""IsometricSnapEnabled { get; set; } -> bool"""
    @property
    def LowerLeftCorner(self) -> _n_2_t_0:"""LowerLeftCorner { get; set; } -> Point2d"""
    @property
    def Number(self) -> int:"""Number { get; } -> int"""
    @property
    def SnapAngle(self) -> float:"""SnapAngle { get; set; } -> float"""
    @property
    def SnapBase(self) -> _n_2_t_0:"""SnapBase { get; set; } -> Point2d"""
    @property
    def SnapEnabled(self) -> bool:"""SnapEnabled { get; set; } -> bool"""
    @property
    def SnapIncrements(self) -> _n_2_t_0:"""SnapIncrements { get; set; } -> Point2d"""
    @property
    def SnapPair(self) -> int:"""SnapPair { get; set; } -> int"""
    @property
    def UcsFollowMode(self) -> bool:"""UcsFollowMode { get; set; } -> bool"""
    @property
    def UcsSavedWithViewport(self) -> bool:"""UcsSavedWithViewport { get; set; } -> bool"""
    @property
    def UpperRightCorner(self) -> _n_2_t_0:"""UpperRightCorner { get; set; } -> Point2d"""
    def __init__(self) -> ViewportTableRecord:...
    def GetPreviousBackground(self, type: _n_3_t_14) -> ObjectId:...
    def SetPreviousBackground(self, value: ObjectId, type: _n_3_t_14):...
class ViewRepBlockReference(BlockReference, _n_6_t_0, _n_6_t_1):
    @property
    def OwnerViewportId(self) -> ObjectId:"""OwnerViewportId { get; } -> ObjectId"""
    def __init__(self) -> ViewRepBlockReference:...
class ViewStyleType(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    FromBase: int
    ShadedHiddenEdges: int
    ShadedVisibleEdges: int
    value__: int
    WireframeHiddenEdges: int
    WireframeVisibleEdges: int
class ViewTable(SymbolTable, _n_6_t_0, _n_6_t_1, _n_7_t_0, typing.Iterable[typing.Any]):
    pass
class ViewTableRecord(AbstractViewTableRecord, _n_6_t_0, _n_6_t_1):
    @property
    def AnnotationScale(self) -> AnnotationScale:"""AnnotationScale { get; set; } -> AnnotationScale"""
    @property
    def CategoryName(self) -> str:"""CategoryName { get; set; } -> str"""
    @property
    def IsPaperspaceView(self) -> bool:"""IsPaperspaceView { get; set; } -> bool"""
    @property
    def IsUcsAssociatedToView(self) -> bool:"""IsUcsAssociatedToView { get; } -> bool"""
    @property
    def LayerState(self) -> str:"""LayerState { get; set; } -> str"""
    @property
    def Layout(self) -> ObjectId:"""Layout { get; set; } -> ObjectId"""
    @property
    def LiveSection(self) -> ObjectId:"""LiveSection { get; set; } -> ObjectId"""
    @property
    def Thumbnail(self) -> _n_11_t_0:"""Thumbnail { get; set; } -> Bitmap"""
    @property
    def ViewAssociatedToViewport(self) -> bool:"""ViewAssociatedToViewport { get; set; } -> bool"""
    def __init__(self) -> ViewTableRecord:...
    def DisassociateUcsFromView(self):...
class Visibility(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    Invisible: int
    value__: int
    Visible: int
class VisibilityOverrule(_n_5_t_5, _n_6_t_0, _n_6_t_1):
    def SetVisibility(self, entity: Entity, newVal: Visibility, doSubents: bool):...
    def Visibility(self, entity: Entity) -> Visibility:...
class WblockNoticeEventArgs(_n_6_t_13):
    @property
    def To(self) -> Database:"""To { get; } -> Database"""
class WblockNoticeEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> WblockNoticeEventHandler:...
    def BeginInvoke(self, sender: object, e: WblockNoticeEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: WblockNoticeEventArgs):...
class Wipeout(RasterImage, _n_6_t_0, _n_6_t_1):
    @property
    def HasFrame(self) -> bool:"""HasFrame { get; } -> bool"""
    def __init__(self) -> Wipeout:...
    def SetFrom(self, points: _n_2_t_18, normal: _n_2_t_3):...
class Xline(Curve, _n_6_t_0, _n_6_t_1):
    @property
    def BasePoint(self) -> _n_2_t_1:"""BasePoint { get; set; } -> Point3d"""
    @property
    def SecondPoint(self) -> _n_2_t_1:"""SecondPoint { get; set; } -> Point3d"""
    @property
    def UnitDir(self) -> _n_2_t_3:"""UnitDir { get; set; } -> Vector3d"""
    def __init__(self) -> Xline:...
class Xrecord(DBObject, _n_6_t_0, _n_6_t_1, _n_8_t_0[TypedValue]):
    @property
    def Data(self) -> ResultBuffer:"""Data { get; set; } -> ResultBuffer"""
    @property
    def XlateReferences(self) -> bool:"""XlateReferences { get; set; } -> bool"""
    def __init__(self) -> Xrecord:...
    def Append(self, data: ResultBuffer):...
    def IEnumerableGetEnumerator(self) -> _n_7_t_3:...
    def IEnumerableTypedValueGetEnumerator(self) -> _n_8_t_4[TypedValue]:...
class XrecordEnumerator(_n_5_t_2, _n_6_t_0, _n_6_t_1, _n_8_t_4[TypedValue]):
    @property
    def CurrentTypeCode(self) -> int:"""CurrentTypeCode { get; } -> int"""
    @property
    def IEnumeratorCurrent(self) -> object:"""IEnumeratorCurrent { get; } -> object"""
    def InsertAtCurrent(self, data: ResultBuffer):...
    def RemoveCurrent(self):...
class XrefBeginOperationEventArgs(_n_6_t_13):
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
class XrefBeginOperationEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefBeginOperationEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefBeginOperationEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefBeginOperationEventArgs):...
class XrefComandeeredEventArgs(_n_6_t_13):
    @property
    def From(self) -> Database:"""From { get; } -> Database"""
    @property
    def Id(self) -> ObjectId:"""Id { get; } -> ObjectId"""
class XrefComandeeredEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefComandeeredEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefComandeeredEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefComandeeredEventArgs):...
class XrefGraph(Graph, _n_6_t_0):
    @property
    def HostDrawing(self) -> XrefGraphNode:"""HostDrawing { get; } -> XrefGraphNode"""
    def GetXrefNode(self, idx: int) -> XrefGraphNode:...
    def GetXrefNode(self, db: Database) -> XrefGraphNode:...
    def GetXrefNode(self, btrId: ObjectId) -> XrefGraphNode:...
    def GetXrefNode(self, name: str) -> XrefGraphNode:...
    def MarkUnresolvedTrees(self) -> bool:...
class XrefGraphNode(GraphNode, _n_6_t_0):
    @property
    def BlockTableRecordId(self) -> ObjectId:"""BlockTableRecordId { get; } -> ObjectId"""
    @property
    def Database(self) -> Database:"""Database { get; } -> Database"""
    @property
    def IsNested(self) -> bool:"""IsNested { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def XrefNotificationStatus(self) -> XrefNotificationStatus:"""XrefNotificationStatus { get; } -> XrefNotificationStatus"""
    @property
    def XrefStatus(self) -> XrefStatus:"""XrefStatus { get; } -> XrefStatus"""
class XrefNotificationStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    _None: int
    ResolvedElsewhere: int
    ResolvedMatch: int
    ResolvedUpdateAvailable: int
    ResolvedWithUpdate: int
    value__: int
class XrefObjectId(_n_6_t_12):
    @property
    def Handle(self) -> Handle:"""Handle { get; } -> Handle"""
    @property
    def IsNull(self) -> bool:"""IsNull { get; } -> bool"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def IsXref(self) -> bool:"""IsXref { get; } -> bool"""
    @property
    def ObjectId(self) -> ObjectId:"""ObjectId { get; } -> ObjectId"""
    def __init__(self, XrefBlockTableRecordId: ObjectId, hand: Handle) -> XrefObjectId:...
    def __init__(self, LocalId: ObjectId) -> XrefObjectId:...
    @staticmethod
    def Deserialize(rbStart: ResultBuffer, rbEnd: ResultBuffer) -> XrefObjectId:...
    def ResolveObjectId(self) -> ObjectId:...
    def Serialize(self) -> ResultBuffer:...
class XrefOperation(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    value__: int
    XrefAttachOperation: int
    XrefBindOperation: int
    XrefDetachOperation: int
    XrefOverlayOperation: int
    XrefPathOperation: int
    XrefReloadOperation: int
    XrefResolveOperation: int
    XrefUnloadOperation: int
    XrefXBindOperation: int
class XrefPreXrefLockFileEventArgs(_n_6_t_13):
    @property
    def btrId(self) -> ObjectId:"""btrId { get; } -> ObjectId"""
class XrefPreXrefLockFileEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefPreXrefLockFileEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefPreXrefLockFileEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefPreXrefLockFileEventArgs):...
class XrefRedirectedEventArgs(_n_6_t_13):
    @property
    def NewId(self) -> ObjectId:"""NewId { get; } -> ObjectId"""
    @property
    def OldId(self) -> ObjectId:"""OldId { get; } -> ObjectId"""
class XrefRedirectedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefRedirectedEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefRedirectedEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefRedirectedEventArgs):...
class XrefStatus(_n_6_t_6, _n_6_t_7, _n_6_t_8, _n_6_t_9):
    FileNotFound: int
    NotAnXref: int
    Resolved: int
    Unloaded: int
    Unreferenced: int
    Unresolved: int
    value__: int
class XrefSubCommandAbortedEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefSubCommandAbortedEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefSubCommandEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefSubCommandEventArgs):...
class XrefSubCommandEndEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefSubCommandEndEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefSubCommandEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefSubCommandEventArgs):...
class XrefSubCommandEventArgs(_n_6_t_13):
    @property
    def btrIds(self) -> ObjectIdCollection:"""btrIds { get; } -> ObjectIdCollection"""
    @property
    def btrNames(self) -> _n_6_t_10[str]:"""btrNames { get; } -> Array"""
    @property
    def paths(self) -> _n_6_t_10[str]:"""paths { get; } -> Array"""
    @property
    def xrefOp(self) -> XrefOperation:"""xrefOp { get; } -> XrefOperation"""
class XrefSubCommandStartEventHandler(_n_6_t_2, _n_6_t_1, _n_15_t_0):
    def __init__(self, A_0: object, A_1: _n_6_t_3) -> XrefSubCommandStartEventHandler:...
    def BeginInvoke(self, sender: object, e: XrefVetoableSubCommandEventArgs, callback: _n_6_t_5, obj: object) -> _n_6_t_4:...
    def EndInvoke(self, result: _n_6_t_4):...
    def Invoke(self, sender: object, e: XrefVetoableSubCommandEventArgs):...
class XrefVetoableSubCommandEventArgs(XrefSubCommandEventArgs):
    @property
    def abortOp(self) -> bool:"""abortOp { get; set; } -> bool"""
