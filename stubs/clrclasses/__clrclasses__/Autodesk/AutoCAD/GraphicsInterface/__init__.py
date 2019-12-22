from __clrclasses__.Autodesk.AutoCAD.Colors import EntityColor as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.Colors import Transparency as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.Colors import EntityColorCollection as _n_0_t_3
from __clrclasses__.Autodesk.AutoCAD.Colors import TransparencyCollection as _n_0_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LineWeight as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Database as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Extents3d as _n_1_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_1_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Polyline as _n_1_t_5
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import PlotStyleDescriptor as _n_1_t_6
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Extents2d as _n_1_t_7
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3d as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2dCollection as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.Geometry import Tolerance as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.Geometry import Curve2dCollection as _n_2_t_5
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3dCollection as _n_2_t_6
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3dCollection as _n_2_t_7
from __clrclasses__.Autodesk.AutoCAD.Geometry import IntPtrCollection as _n_2_t_8
from __clrclasses__.Autodesk.AutoCAD.Geometry import UInt32Collection as _n_2_t_9
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2d as _n_2_t_10
from __clrclasses__.Autodesk.AutoCAD.Geometry import IntegerCollection as _n_2_t_11
from __clrclasses__.Autodesk.AutoCAD.Geometry import DoubleCollection as _n_2_t_12
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix2d as _n_2_t_13
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_3_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import Overrule as _n_3_t_2
from __clrclasses__.System import Enum as _n_4_t_0
from __clrclasses__.System import IComparable as _n_4_t_1
from __clrclasses__.System import IFormattable as _n_4_t_2
from __clrclasses__.System import IConvertible as _n_4_t_3
from __clrclasses__.System import IDisposable as _n_4_t_4
from __clrclasses__.System import ValueType as _n_4_t_5
from __clrclasses__.System import ICloneable as _n_4_t_6
from __clrclasses__.System import Nullable as _n_4_t_7
from __clrclasses__.System import Array as _n_4_t_8
from __clrclasses__.System import IntPtr as _n_4_t_9
from __clrclasses__.System import Byte as _n_4_t_10
from __clrclasses__.System import UInt32 as _n_4_t_11
from __clrclasses__.System.Collections import IList as _n_5_t_0
from __clrclasses__.System.Drawing import Rectangle as _n_6_t_0
import typing
class ArcType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ArcChord: int
    ArcSector: int
    ArcSimple: int
    value__: int
class AttenuationType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    InverseLinear: int
    InverseSquare: int
    _None: int
    value__: int
class AutoTransform(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    InheritAutoTransform: int
    Model: int
    _None: int
    TransformObject: int
    value__: int
class ChannelFlags(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    _None: int
    UseAll: int
    UseBump: int
    UseDiffuse: int
    UseOpacity: int
    UseReflection: int
    UseRefraction: int
    UseSpecular: int
    value__: int
class ClipBoundary(_n_3_t_0, _n_4_t_4):
    @property
    def BackClipZ(self) -> float:"""BackClipZ { get; set; } -> float"""
    @property
    def ClippingBack(self) -> bool:"""ClippingBack { get; set; } -> bool"""
    @property
    def ClippingFront(self) -> bool:"""ClippingFront { get; set; } -> bool"""
    @property
    def DrawBoundary(self) -> bool:"""DrawBoundary { get; set; } -> bool"""
    @property
    def FrontClipZ(self) -> float:"""FrontClipZ { get; set; } -> float"""
    @property
    def NormalVector(self) -> _n_2_t_0:"""NormalVector { get; set; } -> Vector3d"""
    @property
    def Point(self) -> _n_2_t_1:"""Point { get; set; } -> Point3d"""
    @property
    def TransformInverseBlockRefXForm(self) -> _n_2_t_2:"""TransformInverseBlockRefXForm { get; set; } -> Matrix3d"""
    @property
    def TransformToClipSpace(self) -> _n_2_t_2:"""TransformToClipSpace { get; set; } -> Matrix3d"""
    def __init__(self) -> ClipBoundary:...
    def GetAptPoints(self) -> _n_2_t_3:...
    def SetAptPoints(self, point: _n_2_t_3):...
class ColorRGB(_n_4_t_5):
    @property
    def Blue(self) -> float:"""Blue { get; set; } -> float"""
    @property
    def Green(self) -> float:"""Green { get; set; } -> float"""
    @property
    def Red(self) -> float:"""Red { get; set; } -> float"""
    def __init__(self) -> ColorRGB:...
    def __init__(self, red: float, green: float, blue: float) -> ColorRGB:...
class ColorRGBA(_n_4_t_5):
    @property
    def Alpha(self) -> float:"""Alpha { get; set; } -> float"""
    @property
    def Blue(self) -> float:"""Blue { get; set; } -> float"""
    @property
    def Green(self) -> float:"""Green { get; set; } -> float"""
    @property
    def Red(self) -> float:"""Red { get; set; } -> float"""
    def __init__(self) -> ColorRGBA:...
    def __init__(self, red: float, green: float, blue: float) -> ColorRGBA:...
    def __init__(self, red: float, green: float, blue: float, alpha: float) -> ColorRGBA:...
class CommonDraw(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Context(self) -> Context:"""Context { get; } -> Context"""
    @property
    def IsDragging(self) -> bool:"""IsDragging { get; } -> bool"""
    @property
    def NumberOfIsolines(self) -> int:"""NumberOfIsolines { get; } -> int"""
    @property
    def RawGeometry(self) -> Geometry:"""RawGeometry { get; } -> Geometry"""
    @property
    def RegenAbort(self) -> bool:"""RegenAbort { get; } -> bool"""
    @property
    def RegenType(self) -> RegenType:"""RegenType { get; } -> RegenType"""
    @property
    def SubEntityTraits(self) -> SubEntityTraits:"""SubEntityTraits { get; } -> SubEntityTraits"""
    def Deviation(self, deviationType: DeviationType, pointOnCurve: _n_2_t_1) -> float:...
class Context(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def ByBlockLineWeight(self) -> _n_1_t_0:"""ByBlockLineWeight { get; } -> LineWeight"""
    @property
    def ByBlockPlotStyleNameId(self) -> _n_1_t_1:"""ByBlockPlotStyleNameId { get; } -> ObjectId"""
    @property
    def Database(self) -> _n_1_t_2:"""Database { get; } -> Database"""
    @property
    def EffectiveColor(self) -> _n_0_t_0:"""EffectiveColor { get; } -> EntityColor"""
    @property
    def IsBoundaryClipping(self) -> bool:"""IsBoundaryClipping { get; } -> bool"""
    @property
    def IsNesting(self) -> bool:"""IsNesting { get; } -> bool"""
    @property
    def IsPlotGeneration(self) -> bool:"""IsPlotGeneration { get; } -> bool"""
    @property
    def IsPostScriptOut(self) -> bool:"""IsPostScriptOut { get; } -> bool"""
    @property
    def SupportsTrueTypeText(self) -> bool:"""SupportsTrueTypeText { get; } -> bool"""
    def DisableFastMoveDrag(self):...
class ContextualColors(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def CameraClipping(self) -> int:"""CameraClipping { get; } -> int"""
    @property
    def CameraFrustrum(self) -> int:"""CameraFrustrum { get; } -> int"""
    @property
    def CameraGlyphs(self) -> int:"""CameraGlyphs { get; } -> int"""
    @property
    def GridAxisLines(self) -> int:"""GridAxisLines { get; } -> int"""
    @property
    def GridAxisLineTintXYZ(self) -> int:"""GridAxisLineTintXYZ { get; } -> int"""
    @property
    def GridMajorLines(self) -> int:"""GridMajorLines { get; } -> int"""
    @property
    def GridMajorLineTintXYZ(self) -> int:"""GridMajorLineTintXYZ { get; } -> int"""
    @property
    def GridMinorLines(self) -> int:"""GridMinorLines { get; } -> int"""
    @property
    def GridMinorLineTintXYZ(self) -> int:"""GridMinorLineTintXYZ { get; } -> int"""
    @property
    def LightDistanceColor(self) -> _n_0_t_1:"""LightDistanceColor { get; } -> Color"""
    @property
    def LightEndLimit(self) -> int:"""LightEndLimit { get; } -> int"""
    @property
    def LightFalloff(self) -> int:"""LightFalloff { get; } -> int"""
    @property
    def LightGlyphs(self) -> int:"""LightGlyphs { get; } -> int"""
    @property
    def LightHotspot(self) -> int:"""LightHotspot { get; } -> int"""
    @property
    def LightShapeColor(self) -> _n_0_t_1:"""LightShapeColor { get; } -> Color"""
    @property
    def LightStartLimit(self) -> int:"""LightStartLimit { get; } -> int"""
    @property
    def WebMeshColor(self) -> _n_0_t_1:"""WebMeshColor { get; } -> Color"""
    @property
    def WebMeshMissingColor(self) -> _n_0_t_1:"""WebMeshMissingColor { get; } -> Color"""
    def FlagsSet(self, flag: int) -> bool:...
    def SetContextFlags(self, flag: int, set: bool):...
class DefaultLightingType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    OneDistantLight: int
    TwoDistantLights: int
    value__: int
class DeviationType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    MaxDevForBoundary: int
    MaxDevForCircle: int
    MaxDevForCurve: int
    MaxDevForFacet: int
    MaxDevForIsoline: int
    value__: int
class DiagnosticBSPMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Depth: int
    Size: int
    value__: int
class DiagnosticGridMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Camera: int
    Object: int
    value__: int
    World: int
class DiagnosticMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BSP: int
    Grid: int
    Off: int
    Photon: int
    Samples: int
    value__: int
class DiagnosticPhotonMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Density: int
    Irradiance: int
    value__: int
class DistantLightTraits(StandardLightTraits, _n_4_t_4, _n_4_t_6):
    @property
    def IsSunlight(self) -> bool:"""IsSunlight { get; set; } -> bool"""
    @property
    def LampColor(self) -> ColorRGB:"""LampColor { get; set; } -> ColorRGB"""
    @property
    def LightDirection(self) -> _n_2_t_0:"""LightDirection { get; set; } -> Vector3d"""
    @property
    def PhysicalIntensity(self) -> float:"""PhysicalIntensity { get; set; } -> float"""
    @property
    def SkyParameters(self) -> SkyParameters:"""SkyParameters { get; set; } -> SkyParameters"""
    def __init__(self) -> DistantLightTraits:...
class Drawable(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Bounds(self) -> _n_4_t_7[_n_1_t_3]:"""Bounds { get; } -> Nullable"""
    @property
    def DrawableType(self) -> DrawableType:"""DrawableType { get; } -> DrawableType"""
    @property
    def DrawStream(self) -> DrawStream:"""DrawStream { get; set; } -> DrawStream"""
    @property
    def Id(self) -> _n_1_t_1:"""Id { get; } -> ObjectId"""
    @property
    def IsPersistent(self) -> bool:"""IsPersistent { get; } -> bool"""
    def SetAttributes(self, traits: DrawableTraits) -> int:...
    def ViewportDraw(self, vd: ViewportDraw):...
    def ViewportDrawLogicalFlags(self, vd: ViewportDraw) -> int:...
    def WorldDraw(self, wd: WorldDraw) -> bool:...
class DrawableAttributes(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BlockDependentViewportDraw: int
    HasAttributes: int
    IsAnEntity: int
    IsCompoundObject: int
    IsDimension: int
    IsExternalReference: int
    IsInvisible: int
    _None: int
    NotPlottable: int
    RegenDraw: int
    RegenTypeDependentGeometry: int
    ShadedDisplaySingleLOD: int
    StandardDisplaySingleLOD: int
    UsesNesting: int
    value__: int
    ViewDependentViewportDraw: int
    ViewIndependentViewportDraw: int
class DrawableOverrule(_n_3_t_2, _n_4_t_4, _n_4_t_6):
    def SetAttributes(self, drawable: Drawable, traits: DrawableTraits) -> int:...
    def ViewportDraw(self, drawable: Drawable, vd: ViewportDraw):...
    def ViewportDrawLogicalFlags(self, drawable: Drawable, vd: ViewportDraw) -> int:...
    def WorldDraw(self, drawable: Drawable, wd: WorldDraw) -> bool:...
class DrawableTraits(SubEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def LinePattern(self) -> Linetype:"""LinePattern { get; set; } -> Linetype"""
    @property
    def SelectionFlags(self) -> SelectionFlags:"""SelectionFlags { get; set; } -> SelectionFlags"""
    def AddLight(self, lightId: _n_1_t_1):...
    def GetHighlightProperty(self, propertyType: DrawableTraits.HighlightProperty) -> object:...
    def SetHighlightProperty(self, propertyType: DrawableTraits.HighlightProperty, value: object):...
    def SetupForEntity(self, entity: _n_1_t_4):...
    class HighlightProperty(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
        value__: int
        VertexRolloverHighlightSize: int
class DrawableType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    AmbientLight: int
    DistantLight: int
    Geometry: int
    GradientBackground: int
    GroundPlaneBackground: int
    ImageBackground: int
    ImageBasedLightingBackground: int
    PointLight: int
    SkyBackground: int
    SolidBackground: int
    SpotLight: int
    value__: int
    Viewport: int
    WebLight: int
class DrawFlags(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    DrawBackfaces: int
    DrawFillTextBoundaryEnd: int
    DrawFillTextBoundaryStart: int
    DrawNoLineWeight: int
    _None: int
    value__: int
class DrawStream(Drawable, _n_4_t_4, _n_4_t_6):
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def Owner(self) -> Drawable:"""Owner { get; set; } -> Drawable"""
    def __init__(self) -> DrawStream:...
    def __init__(self, owner: Drawable) -> DrawStream:...
class EdgeData(object):
    def __init__(self) -> EdgeData:...
    def GetColors(self) -> _n_4_t_8[int]:...
    def GetLayers(self) -> _n_4_t_8[_n_1_t_1]:...
    def GetLineTypes(self) -> _n_4_t_8[_n_1_t_1]:...
    def GetSelectionMarkers(self) -> _n_4_t_8[_n_4_t_9]:...
    def GetTrueColors(self) -> _n_4_t_8[_n_0_t_0]:...
    def GetVisibility(self) -> _n_4_t_8[_n_4_t_10]:...
    def SetColors(self, colors: _n_4_t_8[int]):...
    def SetLayers(self, layers: _n_4_t_8[_n_1_t_1]):...
    def SetLineTypes(self, lineTypes: _n_4_t_8[_n_1_t_1]):...
    def SetSelectionMarkers(self, selectionMarkers: _n_4_t_8[_n_4_t_9]):...
    def SetTrueColors(self, colors: _n_4_t_8[_n_0_t_0]):...
    def SetVisibility(self, visibility: _n_4_t_8[_n_4_t_10]):...
class ExposureType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Automatic: int
    Logarithmic: int
    value__: int
class ExtendedLightShape(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Cylinder: int
    Disk: int
    Linear: int
    Rectangle: int
    Sphere: int
    value__: int
class ExteriorDaylightMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    DaylightAuto: int
    DaylightOff: int
    DaylightOn: int
    value__: int
class FaceData(object):
    def __init__(self) -> FaceData:...
    def GetColors(self) -> _n_4_t_8[int]:...
    def GetLayers(self) -> _n_4_t_8[_n_1_t_1]:...
    def GetMappers(self) -> _n_4_t_8[Mapper]:...
    def GetMaterials(self) -> _n_4_t_8[_n_1_t_1]:...
    def GetNormalVectors(self) -> _n_4_t_8[_n_2_t_0]:...
    def GetSelectionMarkers(self) -> _n_4_t_8[_n_4_t_9]:...
    def GetTransparency(self) -> _n_4_t_8[_n_0_t_2]:...
    def GetTrueColors(self) -> _n_4_t_8[_n_0_t_0]:...
    def GetVisibility(self) -> _n_4_t_8[_n_4_t_10]:...
    def SetColors(self, colors: _n_4_t_8[int]):...
    def SetLayers(self, layers: _n_4_t_8[_n_1_t_1]):...
    def SetMappers(self, mappers: _n_4_t_8[Mapper]):...
    def SetMaterials(self, materials: _n_4_t_8[_n_1_t_1]):...
    def SetNormalVectors(self, normal: _n_4_t_8[_n_2_t_0]):...
    def SetSelectionMarkers(self, selectionMarker: _n_4_t_8[_n_4_t_9]):...
    def SetTransparency(self, transparency: _n_4_t_8[_n_0_t_2]):...
    def SetTrueColors(self, colors: _n_4_t_8[_n_0_t_0]):...
    def SetVisibility(self, visibility: _n_4_t_8[_n_4_t_10]):...
class Fill(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    def __init__(self) -> Fill:...
class FillType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    FillAlways: int
    FillNever: int
    value__: int
class Filter(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Box: int
    Gauss: int
    Lanczos: int
    Mitchell: int
    Triangle: int
    value__: int
class FinalGatheringMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    FinalGatherAuto: int
    FinalGatherOff: int
    FinalGatherOn: int
    value__: int
class FinalGatherMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    FinalGatherCast: int
    FinalGatherCastAndReceive: int
    FinalGatherNone: int
    FinalGatherReceive: int
    value__: int
class FontDescriptor(_n_4_t_5):
    @property
    def Bold(self) -> bool:"""Bold { get; } -> bool"""
    @property
    def CharacterSet(self) -> int:"""CharacterSet { get; } -> int"""
    @property
    def Italic(self) -> bool:"""Italic { get; } -> bool"""
    @property
    def PitchAndFamily(self) -> int:"""PitchAndFamily { get; } -> int"""
    @property
    def TypeFace(self) -> str:"""TypeFace { get; } -> str"""
    def __init__(self, typeFace: str, bold: bool, italic: bool, characters: int, pitchAndFamily: int) -> FontDescriptor:...
class FrontAndBackClipping(_n_4_t_5):
    @property
    def Back(self) -> float:"""Back { get; } -> float"""
    @property
    def ClipBack(self) -> bool:"""ClipBack { get; } -> bool"""
    @property
    def ClipFront(self) -> bool:"""ClipFront { get; } -> bool"""
    @property
    def Front(self) -> float:"""Front { get; } -> float"""
    def __init__(self, clipFront: bool, clipBack: bool, front: float, back: float) -> FrontAndBackClipping:...
    def IsEqualTo(self, a: FrontAndBackClipping, tolerance: _n_2_t_4) -> bool:...
    def IsEqualTo(self, a: FrontAndBackClipping) -> bool:...
class GdiDrawObject(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Height(self) -> int:"""Height { get; } -> int"""
    @property
    def Width(self) -> int:"""Width { get; } -> int"""
    def Draw(self, hDC: _n_4_t_9, bounds: _n_6_t_0) -> bool:...
class GenericTexture(ProceduralTexture, _n_4_t_4, _n_4_t_6):
    @property
    def Definition(self) -> object:"""Definition { get; set; } -> object"""
    def __init__(self) -> GenericTexture:...
    def Set(self, value: GenericTexture):...
class Geometry(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def ModelToWorldTransform(self) -> _n_2_t_2:"""ModelToWorldTransform { get; } -> Matrix3d"""
    @property
    def WorldToModelTransform(self) -> _n_2_t_2:"""WorldToModelTransform { get; } -> Matrix3d"""
    def Circle(self, center: _n_2_t_1, radius: float, normal: _n_2_t_0) -> bool:...
    def Circle(self, firstPoint: _n_2_t_1, secondPoint: _n_2_t_1, thirdPoint: _n_2_t_1) -> bool:...
    def CircularArc(self, center: _n_2_t_1, radius: float, normal: _n_2_t_0, startVector: _n_2_t_0, sweepAngle: float, arcType: ArcType) -> bool:...
    def CircularArc(self, start: _n_2_t_1, point: _n_2_t_1, endingPoint: _n_2_t_1, arcType: ArcType) -> bool:...
    def Draw(self, value: Drawable) -> bool:...
    def Edge(self, e: _n_2_t_5) -> bool:...
    def EllipticalArc(self, center: _n_2_t_1, normal: _n_2_t_0, majorAxisLength: float, minorAxisLength: float, startDegreeInRads: float, endDegreeInRads: float, tiltDegreeInRads: float, arcType: ArcType) -> bool:...
    def Image(self, imageSource: ImageBGRA32, position: _n_2_t_1, u: _n_2_t_0, v: _n_2_t_0) -> bool:...
    def Image(self, imageSource: ImageBGRA32, position: _n_2_t_1, u: _n_2_t_0, v: _n_2_t_0, transparencyMode: TransparencyMode) -> bool:...
    def Mesh(self, rows: int, columns: int, points: _n_2_t_6, edgeData: EdgeData, faceData: FaceData, vertexData: VertexData, bAutoGenerateNormals: bool) -> bool:...
    def OwnerDraw(self, gdiDrawObject: GdiDrawObject, position: _n_2_t_1, u: _n_2_t_0, v: _n_2_t_0) -> bool:...
    def Polygon(self, points: _n_2_t_6) -> bool:...
    def Polyline(self, points: _n_2_t_6, normal: _n_2_t_0, subEntityMarker: _n_4_t_9) -> bool:...
    def Polyline(self, polylineObj: Polyline) -> bool:...
    def Polyline(self, value: _n_1_t_5, fromIndex: int, segments: int) -> bool:...
    def Polypoint(self, points: _n_2_t_6, normals: _n_2_t_7, subentityMarkers: _n_2_t_8) -> bool:...
    def PolyPolygon(self, numPolygonPositions: _n_2_t_9, polygonPositions: _n_2_t_6, numPolygonPoints: _n_2_t_9, polygonPoints: _n_2_t_6, outlineColors: _n_0_t_3, outlineTypes: LinetypeCollection, fillColors: _n_0_t_3, fillOpacities: _n_0_t_4) -> bool:...
    def PolyPolyline(self, polylineCollection: PolylineCollection) -> bool:...
    def PopClipBoundary(self):...
    def PopModelTransform(self) -> bool:...
    def PushClipBoundary(self, boundary: ClipBoundary) -> bool:...
    def PushModelTransform(self, normal: _n_2_t_0) -> bool:...
    def PushModelTransform(self, matrix: _n_2_t_2) -> bool:...
    def PushOrientationTransform(self, behavior: OrientationBehavior) -> _n_2_t_2:...
    def PushPositionTransform(self, behavior: PositionBehavior, offset: _n_2_t_1) -> _n_2_t_2:...
    def PushPositionTransform(self, behavior: PositionBehavior, offset: _n_2_t_10) -> _n_2_t_2:...
    def PushScaleTransform(self, behavior: ScaleBehavior, extents: _n_2_t_1) -> _n_2_t_2:...
    def PushScaleTransform(self, behavior: ScaleBehavior, extents: _n_2_t_10) -> _n_2_t_2:...
    def Ray(self, point1: _n_2_t_1, point2: _n_2_t_1) -> bool:...
    def RowOfDots(self, count: int, start: _n_2_t_1, step: _n_2_t_0) -> bool:...
    def Shell(self, points: _n_2_t_6, faces: _n_2_t_11, edgeData: EdgeData, faceData: FaceData, vertexData: VertexData, bAutoGenerateNormals: bool) -> bool:...
    def Text(self, position: _n_2_t_1, normal: _n_2_t_0, direction: _n_2_t_0, height: float, width: float, oblique: float, message: str) -> bool:...
    def Text(self, position: _n_2_t_1, normal: _n_2_t_0, direction: _n_2_t_0, message: str, raw: bool, textStyle: TextStyle) -> bool:...
    def WorldLine(self, startPoint: _n_2_t_1, endPoint: _n_2_t_1) -> bool:...
    def Xline(self, point1: _n_2_t_1, point2: _n_2_t_1) -> bool:...
class GlobalIlluminationMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    GlobalIlluminationCast: int
    GlobalIlluminationCastAndReceive: int
    GlobalIlluminationNone: int
    GlobalIlluminationReceive: int
    value__: int
class Glyph(Drawable, _n_4_t_4, _n_4_t_6):
    def SetLocation(self, point: _n_2_t_1):...
class GradientBackgroundTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def ColorBottom(self) -> _n_0_t_0:"""ColorBottom { get; set; } -> EntityColor"""
    @property
    def ColorMiddle(self) -> _n_0_t_0:"""ColorMiddle { get; set; } -> EntityColor"""
    @property
    def ColorTop(self) -> _n_0_t_0:"""ColorTop { get; set; } -> EntityColor"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def Horizon(self) -> float:"""Horizon { get; set; } -> float"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
class GradientFill(Fill, _n_4_t_4, _n_4_t_6):
    @property
    def GradientAngle(self) -> float:"""GradientAngle { get; set; } -> float"""
    @property
    def GradientColors(self) -> _n_4_t_8[_n_0_t_1]:"""GradientColors { get; set; } -> Array"""
    @property
    def GradientShift(self) -> float:"""GradientShift { get; set; } -> float"""
    @property
    def IsAdjustAspect(self) -> bool:"""IsAdjustAspect { get; set; } -> bool"""
    @property
    def Type(self) -> GradientType:"""Type { get; set; } -> GradientType"""
    def __init__(self, gradientAngle: float, gradientShift: float, bAdjustAspect: bool, colors: _n_4_t_8[_n_0_t_1], gradientType: GradientType) -> GradientFill:...
class GradientType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Curved: int
    Cylinder: int
    Hemispherical: int
    InvCurved: int
    InvCylinder: int
    InvHemispherical: int
    InvSpherical: int
    Linear: int
    Spherical: int
    value__: int
class GroundPlaneBackgroundTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def ColorGroundPlaneFar(self) -> _n_0_t_0:"""ColorGroundPlaneFar { get; set; } -> EntityColor"""
    @property
    def ColorGroundPlaneNear(self) -> _n_0_t_0:"""ColorGroundPlaneNear { get; set; } -> EntityColor"""
    @property
    def ColorSkyHorizon(self) -> _n_0_t_0:"""ColorSkyHorizon { get; set; } -> EntityColor"""
    @property
    def ColorSkyZenith(self) -> _n_0_t_0:"""ColorSkyZenith { get; set; } -> EntityColor"""
    @property
    def ColorUndergroundAzimuth(self) -> _n_0_t_0:"""ColorUndergroundAzimuth { get; set; } -> EntityColor"""
    @property
    def ColorUndergroundHorizon(self) -> _n_0_t_0:"""ColorUndergroundHorizon { get; set; } -> EntityColor"""
class HatchPattern(Fill, _n_4_t_4, _n_4_t_6):
    @property
    def PatternLines(self) -> _n_4_t_8[HatchPatternDefinition]:"""PatternLines { get; } -> Array"""
    def __init__(self, patLines: _n_4_t_8[HatchPatternDefinition]) -> HatchPattern:...
class HatchPatternDefinition(_n_3_t_0, _n_4_t_4):
    @property
    def Angle(self) -> float:"""Angle { get; } -> float"""
    @property
    def BaseX(self) -> float:"""BaseX { get; } -> float"""
    @property
    def BaseY(self) -> float:"""BaseY { get; } -> float"""
    @property
    def DashList(self) -> _n_2_t_12:"""DashList { get; } -> DoubleCollection"""
    @property
    def OffsetX(self) -> float:"""OffsetX { get; } -> float"""
    @property
    def OffsetY(self) -> float:"""OffsetY { get; } -> float"""
    def __init__(self, angle: float, baseX: float, baseY: float, offsetX: float, offsetY: float, dashList: _n_2_t_12) -> HatchPatternDefinition:...
class HighlightStyle(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Custom: int
    DashedAndThicken: int
    Dim: int
    Glow: int
    _None: int
    ThickDim: int
    value__: int
class IBLBackgroundTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def DisplayImage(self) -> bool:"""DisplayImage { get; set; } -> bool"""
    @property
    def Enable(self) -> bool:"""Enable { get; set; } -> bool"""
    @property
    def IBLImageName(self) -> str:"""IBLImageName { get; set; } -> str"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def SecondaryBackground(self) -> _n_1_t_1:"""SecondaryBackground { get; set; } -> ObjectId"""
class IlluminationModel(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BlinnShader: int
    MetalShader: int
    value__: int
class ImageBackgroundTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def FitToScreen(self) -> bool:"""FitToScreen { get; set; } -> bool"""
    @property
    def ImageFilename(self) -> str:"""ImageFilename { get; set; } -> str"""
    @property
    def MaintainAspectRatio(self) -> bool:"""MaintainAspectRatio { get; set; } -> bool"""
    @property
    def UseTiling(self) -> bool:"""UseTiling { get; set; } -> bool"""
    @property
    def XOffset(self) -> float:"""XOffset { get; set; } -> float"""
    @property
    def XScale(self) -> float:"""XScale { get; set; } -> float"""
    @property
    def YOffset(self) -> float:"""YOffset { get; set; } -> float"""
    @property
    def YScale(self) -> float:"""YScale { get; set; } -> float"""
class ImageBGRA32(_n_3_t_0, _n_4_t_4):
    @property
    def Height(self) -> _n_4_t_11:"""Height { get; set; } -> UInt32"""
    @property
    def Image(self) -> _n_4_t_9:"""Image { get; set; } -> IntPtr"""
    @property
    def Width(self) -> _n_4_t_11:"""Width { get; set; } -> UInt32"""
    def __init__(self) -> ImageBGRA32:...
    def __init__(self, width: _n_4_t_11, height: _n_4_t_11, imageData: _n_4_t_9) -> ImageBGRA32:...
class ImageFileTexture(ImageTexture, _n_4_t_4, _n_4_t_6):
    @property
    def SourceFileName(self) -> str:"""SourceFileName { get; set; } -> str"""
    def __init__(self) -> ImageFileTexture:...
class ImageOrg(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ABGR: int
    ARGB: int
    BGR: int
    BGRA: int
    Bitonal: int
    Gray: int
    Palette: int
    RGB: int
    RGBA: int
    value__: int
class ImageSource(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    FromDwg: int
    FromOleObject: int
    FromRender: int
    value__: int
class ImageTexture(MaterialTexture, _n_4_t_4, _n_4_t_6):
    def __init__(self) -> ImageTexture:...
class LightAttenuation(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def AttenuationType(self) -> AttenuationType:"""AttenuationType { get; set; } -> AttenuationType"""
    @property
    def EndLimit(self) -> float:"""EndLimit { get; } -> float"""
    @property
    def StartLimit(self) -> float:"""StartLimit { get; } -> float"""
    @property
    def UseLimits(self) -> bool:"""UseLimits { get; set; } -> bool"""
    def __init__(self) -> LightAttenuation:...
    def SetLimits(self, startLimit: float, endLimit: float):...
class LightTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def On(self) -> bool:"""On { get; set; } -> bool"""
    def __init__(self) -> LightTraits:...
class Linetype(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    DashDot: int
    Dashed: int
    Dotted: int
    ISODash: int
    ISODashDot: int
    ISODashDoubleDot: int
    ISODashSpace: int
    ISODashTripleDot: int
    ISODot: int
    ISODoubleDashDot: int
    ISODoubleDashDoubleDot: int
    ISODoubleDashTripleDot: int
    ISOLongDashDot: int
    ISOLongDashDoubleDot: int
    ISOLongDashDoubleShortDash: int
    ISOLongDashShortDash: int
    ISOLongDashTripleDot: int
    LineTypeNone: int
    LongDash: int
    LongDashDot: int
    LongDashDotDot: int
    LongDashShortDash: int
    LongDashX2: int
    MediumDash: int
    MediumDashDotShortDashDot: int
    MediumDashShortDashShortDash: int
    MediumDashX2: int
    MediumLongDash: int
    ShortDash: int
    ShortDashX2: int
    Solid: int
    Solid6PixelsBlank6Pixels: int
    SparseDot: int
    value__: int
class LinetypeCollection(_n_3_t_0, _n_4_t_4, _n_5_t_0, typing.Iterable[Linetype]):
    def __init__(self) -> LinetypeCollection:...
    def __init__(self, values: _n_4_t_8[Linetype]) -> LinetypeCollection:...
class LuminanceMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Luminance: int
    SelfIllumination: int
    value__: int
class MapChannel(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    AllChannels: int
    MapChannels: int
    value__: int
class MapFilter(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Default: int
    _None: int
    value__: int
class Mapper(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def AutoTransform(self) -> AutoTransform:"""AutoTransform { get; } -> AutoTransform"""
    @property
    def Projection(self) -> Projection:"""Projection { get; } -> Projection"""
    @property
    def Transform(self) -> _n_2_t_2:"""Transform { get; } -> Matrix3d"""
    @property
    def UTiling(self) -> Tiling:"""UTiling { get; set; } -> Tiling"""
    @property
    def VTiling(self) -> Tiling:"""VTiling { get; set; } -> Tiling"""
    def __init__(self) -> Mapper:...
    def __init__(self, projection: Projection, uTiling: Tiling, vTiling: Tiling, autoTransform: AutoTransform, transform: _n_2_t_2) -> Mapper:...
class MarbleTexture(ProceduralTexture, _n_4_t_4, _n_4_t_6):
    @property
    def StoneColor(self) -> MaterialColor:"""StoneColor { get; set; } -> MaterialColor"""
    @property
    def VeinColor(self) -> MaterialColor:"""VeinColor { get; set; } -> MaterialColor"""
    @property
    def VeinSpacing(self) -> float:"""VeinSpacing { get; set; } -> float"""
    @property
    def VeinWidth(self) -> float:"""VeinWidth { get; set; } -> float"""
    def __init__(self) -> MarbleTexture:...
    def Set(self, value: MarbleTexture):...
class MaterialColor(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Color(self) -> _n_0_t_0:"""Color { get; } -> EntityColor"""
    @property
    def Factor(self) -> float:"""Factor { get; } -> float"""
    @property
    def Method(self) -> Method:"""Method { get; } -> Method"""
    def __init__(self) -> MaterialColor:...
    def __init__(self, method: Method, factor: float, color: _n_0_t_0) -> MaterialColor:...
class MaterialDiffuseComponent(_n_4_t_5):
    @property
    def Color(self) -> MaterialColor:"""Color { get; } -> MaterialColor"""
    @property
    def Map(self) -> MaterialMap:"""Map { get; } -> MaterialMap"""
    def __init__(self, color: MaterialColor, map: MaterialMap) -> MaterialDiffuseComponent:...
class MaterialMap(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def BlendFactor(self) -> float:"""BlendFactor { get; } -> float"""
    @property
    def Filter(self) -> MapFilter:"""Filter { get; } -> MapFilter"""
    @property
    def Mapper(self) -> Mapper:"""Mapper { get; } -> Mapper"""
    @property
    def Source(self) -> Source:"""Source { get; } -> Source"""
    @property
    def SourceFileName(self) -> str:"""SourceFileName { get; } -> str"""
    @property
    def Texture(self) -> MaterialTexture:"""Texture { get; } -> MaterialTexture"""
    def __init__(self) -> MaterialMap:...
    def __init__(self, source: Source, pTexture: MaterialTexture, blendFactor: float, mapper: Mapper) -> MaterialMap:...
    def __init__(self, source: Source, pTexture: MaterialTexture, blendFactor: float, mapper: Mapper, filter: MapFilter) -> MaterialMap:...
    def __init__(self, source: Source, fileName: str, pTexture: MaterialTexture, blendFactor: float, mapper: Mapper) -> MaterialMap:...
class MaterialNormalMapComponent(_n_4_t_5):
    @property
    def Map(self) -> MaterialMap:"""Map { get; } -> MaterialMap"""
    @property
    def Method(self) -> NormalMapMethod:"""Method { get; } -> NormalMapMethod"""
    @property
    def Strength(self) -> float:"""Strength { get; } -> float"""
    def __init__(self, map: MaterialMap, method: NormalMapMethod, strength: float) -> MaterialNormalMapComponent:...
class MaterialOpacityComponent(_n_4_t_5):
    @property
    def Map(self) -> MaterialMap:"""Map { get; } -> MaterialMap"""
    @property
    def Percentage(self) -> float:"""Percentage { get; } -> float"""
    def __init__(self, percentage: float, map: MaterialMap) -> MaterialOpacityComponent:...
class MaterialRefractionComponent(_n_4_t_5):
    @property
    def Index(self) -> float:"""Index { get; } -> float"""
    @property
    def Map(self) -> MaterialMap:"""Map { get; } -> MaterialMap"""
    def __init__(self, index: float, map: MaterialMap) -> MaterialRefractionComponent:...
class MaterialSpecularComponent(_n_4_t_5):
    @property
    def Color(self) -> MaterialColor:"""Color { get; } -> MaterialColor"""
    @property
    def Gloss(self) -> float:"""Gloss { get; } -> float"""
    @property
    def Map(self) -> MaterialMap:"""Map { get; } -> MaterialMap"""
    def __init__(self, color: MaterialColor, map: MaterialMap, gloss: float) -> MaterialSpecularComponent:...
class MaterialTexture(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    def __init__(self) -> MaterialTexture:...
class MaterialTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def Ambient(self) -> MaterialColor:"""Ambient { get; set; } -> MaterialColor"""
    @property
    def Bump(self) -> MaterialMap:"""Bump { get; set; } -> MaterialMap"""
    @property
    def ChannelFlags(self) -> ChannelFlags:"""ChannelFlags { get; set; } -> ChannelFlags"""
    @property
    def ColorBleedScale(self) -> float:"""ColorBleedScale { get; set; } -> float"""
    @property
    def Diffuse(self) -> MaterialDiffuseComponent:"""Diffuse { get; set; } -> MaterialDiffuseComponent"""
    @property
    def FinalGather(self) -> FinalGatherMode:"""FinalGather { get; set; } -> FinalGatherMode"""
    @property
    def GlobalIllumination(self) -> GlobalIlluminationMode:"""GlobalIllumination { get; set; } -> GlobalIlluminationMode"""
    @property
    def IlluminationModel(self) -> IlluminationModel:"""IlluminationModel { get; set; } -> IlluminationModel"""
    @property
    def IndirectBumpScale(self) -> float:"""IndirectBumpScale { get; set; } -> float"""
    @property
    def Luminance(self) -> float:"""Luminance { get; set; } -> float"""
    @property
    def LuminanceMode(self) -> LuminanceMode:"""LuminanceMode { get; set; } -> LuminanceMode"""
    @property
    def Mode(self) -> Mode:"""Mode { get; set; } -> Mode"""
    @property
    def NormalMap(self) -> MaterialNormalMapComponent:"""NormalMap { get; set; } -> MaterialNormalMapComponent"""
    @property
    def Opacity(self) -> MaterialOpacityComponent:"""Opacity { get; set; } -> MaterialOpacityComponent"""
    @property
    def ReflectanceScale(self) -> float:"""ReflectanceScale { get; set; } -> float"""
    @property
    def Reflection(self) -> MaterialMap:"""Reflection { get; set; } -> MaterialMap"""
    @property
    def Reflectivity(self) -> float:"""Reflectivity { get; set; } -> float"""
    @property
    def Refraction(self) -> MaterialRefractionComponent:"""Refraction { get; set; } -> MaterialRefractionComponent"""
    @property
    def SelfIllumination(self) -> float:"""SelfIllumination { get; set; } -> float"""
    @property
    def Specular(self) -> MaterialSpecularComponent:"""Specular { get; set; } -> MaterialSpecularComponent"""
    @property
    def Translucence(self) -> float:"""Translucence { get; set; } -> float"""
    @property
    def TransmittanceScale(self) -> float:"""TransmittanceScale { get; set; } -> float"""
    @property
    def TwoSided(self) -> bool:"""TwoSided { get; set; } -> bool"""
class MentalRayRenderSettingsTraits(RenderSettingsTraits, _n_4_t_4, _n_4_t_6):
    @property
    def DiagnosticBSPMode(self) -> DiagnosticBSPMode:"""DiagnosticBSPMode { get; set; } -> DiagnosticBSPMode"""
    @property
    def DiagnosticGridMode(self) -> MentalRayRenderSettingsTraitsDiagnosticGridModeParameter:"""DiagnosticGridMode { get; set; } -> MentalRayRenderSettingsTraitsDiagnosticGridModeParameter"""
    @property
    def DiagnosticMode(self) -> DiagnosticMode:"""DiagnosticMode { get; set; } -> DiagnosticMode"""
    @property
    def DiagnosticPhotonMode(self) -> DiagnosticPhotonMode:"""DiagnosticPhotonMode { get; set; } -> DiagnosticPhotonMode"""
    @property
    def EnergyMultiplier(self) -> float:"""EnergyMultiplier { get; set; } -> float"""
    @property
    def ExportMIEnabled(self) -> bool:"""ExportMIEnabled { get; set; } -> bool"""
    @property
    def ExportMIFileName(self) -> str:"""ExportMIFileName { get; set; } -> str"""
    @property
    def ExposureType(self) -> ExposureType:"""ExposureType { get; set; } -> ExposureType"""
    @property
    def FGRayCount(self) -> int:"""FGRayCount { get; set; } -> int"""
    @property
    def FGSampleRadius(self) -> MentalRayRenderSettingsTraitsDoubleRangeParameter:"""FGSampleRadius { get; set; } -> MentalRayRenderSettingsTraitsDoubleRangeParameter"""
    @property
    def FGSampleRadiusState(self) -> MentalRayRenderSettingsTraitsBoolParameter:"""FGSampleRadiusState { get; set; } -> MentalRayRenderSettingsTraitsBoolParameter"""
    @property
    def FinalGatheringEnabled(self) -> bool:"""FinalGatheringEnabled { get; set; } -> bool"""
    @property
    def FinalGatheringMode(self) -> FinalGatheringMode:"""FinalGatheringMode { get; set; } -> FinalGatheringMode"""
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
    def MrExportMIMode(self) -> MrExportMIMode:"""MrExportMIMode { get; set; } -> MrExportMIMode"""
    @property
    def PhotonTraceDepth(self) -> MentalRayRenderSettingsTraitsTraceParameter:"""PhotonTraceDepth { get; set; } -> MentalRayRenderSettingsTraitsTraceParameter"""
    @property
    def ProgressMonitor(self) -> _n_4_t_9:"""ProgressMonitor { get; set; } -> IntPtr"""
    @property
    def RayTraceDepth(self) -> MentalRayRenderSettingsTraitsTraceParameter:"""RayTraceDepth { get; set; } -> MentalRayRenderSettingsTraitsTraceParameter"""
    @property
    def RayTraceEnabled(self) -> bool:"""RayTraceEnabled { get; set; } -> bool"""
    @property
    def Sampling(self) -> MentalRayRenderSettingsTraitsIntegerRangeParameter:"""Sampling { get; set; } -> MentalRayRenderSettingsTraitsIntegerRangeParameter"""
    @property
    def SamplingContrastColor(self) -> MentalRayRenderSettingsTraitsFloatParameter:"""SamplingContrastColor { get; set; } -> MentalRayRenderSettingsTraitsFloatParameter"""
    @property
    def SamplingFilter(self) -> MentalRayRenderSettingsTraitsSamplingParameter:"""SamplingFilter { get; set; } -> MentalRayRenderSettingsTraitsSamplingParameter"""
    @property
    def ShadowMapEnabled(self) -> bool:"""ShadowMapEnabled { get; set; } -> bool"""
    @property
    def ShadowMode(self) -> ShadowMode:"""ShadowMode { get; set; } -> ShadowMode"""
    @property
    def ShadowSamplingMultiplier(self) -> float:"""ShadowSamplingMultiplier { get; set; } -> float"""
    @property
    def TileOrder(self) -> TileOrder:"""TileOrder { get; set; } -> TileOrder"""
    @property
    def TileSize(self) -> int:"""TileSize { get; set; } -> int"""
class MentalRayRenderSettingsTraitsBoolParameter(_n_4_t_5):
    @property
    def Max(self) -> bool:"""Max { get; } -> bool"""
    @property
    def Min(self) -> bool:"""Min { get; } -> bool"""
    @property
    def Pixels(self) -> bool:"""Pixels { get; } -> bool"""
    def __init__(self, a: bool, b: bool, pix: bool) -> MentalRayRenderSettingsTraitsBoolParameter:...
class MentalRayRenderSettingsTraitsDiagnosticGridModeParameter(_n_4_t_5):
    @property
    def Mode(self) -> DiagnosticGridMode:"""Mode { get; } -> DiagnosticGridMode"""
    @property
    def Size(self) -> float:"""Size { get; } -> float"""
    def __init__(self, m: DiagnosticGridMode, s: float) -> MentalRayRenderSettingsTraitsDiagnosticGridModeParameter:...
class MentalRayRenderSettingsTraitsDoubleRangeParameter(_n_4_t_5):
    @property
    def Max(self) -> float:"""Max { get; } -> float"""
    @property
    def Min(self) -> float:"""Min { get; } -> float"""
    def __init__(self, a: float, b: float) -> MentalRayRenderSettingsTraitsDoubleRangeParameter:...
class MentalRayRenderSettingsTraitsFloatParameter(_n_4_t_5):
    @property
    def A(self) -> float:"""A { get; } -> float"""
    @property
    def B(self) -> float:"""B { get; } -> float"""
    @property
    def G(self) -> float:"""G { get; } -> float"""
    @property
    def R(self) -> float:"""R { get; } -> float"""
    def __init__(self, red: float, green: float, blue: float, alpha: float) -> MentalRayRenderSettingsTraitsFloatParameter:...
class MentalRayRenderSettingsTraitsIntegerRangeParameter(_n_4_t_5):
    @property
    def Max(self) -> int:"""Max { get; } -> int"""
    @property
    def Min(self) -> int:"""Min { get; } -> int"""
    def __init__(self, a: int, b: int) -> MentalRayRenderSettingsTraitsIntegerRangeParameter:...
class MentalRayRenderSettingsTraitsSamplingParameter(_n_4_t_5):
    @property
    def Filter(self) -> Filter:"""Filter { get; } -> Filter"""
    @property
    def Height(self) -> float:"""Height { get; } -> float"""
    @property
    def Width(self) -> float:"""Width { get; } -> float"""
    def __init__(self, f: Filter, w: float, h: float) -> MentalRayRenderSettingsTraitsSamplingParameter:...
class MentalRayRenderSettingsTraitsTraceParameter(_n_4_t_5):
    @property
    def Reflection(self) -> int:"""Reflection { get; } -> int"""
    @property
    def Refraction(self) -> int:"""Refraction { get; } -> int"""
    @property
    def Sum(self) -> int:"""Sum { get; } -> int"""
    def __init__(self, reflect: int, refract: int, s: int) -> MentalRayRenderSettingsTraitsTraceParameter:...
class Method(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Inherit: int
    Override: int
    value__: int
class Mode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Advanced: int
    Realistic: int
    value__: int
class MrExportMIMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ExportMIOff: int
    ExportMIOnly: int
    ExportMIWithRender: int
    value__: int
class NonEntityTraits(DrawableTraits, _n_4_t_4, _n_4_t_6):
    pass
class NormalMapMethod(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    TangentSpaceNormalMap: int
    value__: int
class OrientationBehavior(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Screen: int
    value__: int
    World: int
    ZAxis: int
class OrientationType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Clockwise: int
    CounterClockwise: int
    NoOrientation: int
    value__: int
class PhotographicExposureParameters(ToneOperatorParameters, _n_4_t_4, _n_4_t_6):
    @property
    def Exposure(self) -> float:"""Exposure { get; set; } -> float"""
    @property
    def WhitePoint(self) -> float:"""WhitePoint { get; set; } -> float"""
    def __init__(self) -> PhotographicExposureParameters:...
class PixelBGRA32(_n_4_t_5):
    @property
    def Alpha(self) -> _n_4_t_10:"""Alpha { get; set; } -> Byte"""
    @property
    def Blue(self) -> _n_4_t_10:"""Blue { get; set; } -> Byte"""
    @property
    def Green(self) -> _n_4_t_10:"""Green { get; set; } -> Byte"""
    @property
    def Red(self) -> _n_4_t_10:"""Red { get; set; } -> Byte"""
    def __init__(self) -> PixelBGRA32:...
    def __init__(self, bgra: _n_4_t_11) -> PixelBGRA32:...
    def __init__(self, blue: _n_4_t_10, green: _n_4_t_10, red: _n_4_t_10, alpha: _n_4_t_10) -> PixelBGRA32:...
    def init(self):...
class PointLightTraits(StandardLightTraits, _n_4_t_4, _n_4_t_6):
    @property
    def Attenuation(self) -> LightAttenuation:"""Attenuation { get; set; } -> LightAttenuation"""
    @property
    def HasTarget(self) -> bool:"""HasTarget { get; set; } -> bool"""
    @property
    def LampColor(self) -> ColorRGB:"""LampColor { get; set; } -> ColorRGB"""
    @property
    def PhysicalIntensity(self) -> float:"""PhysicalIntensity { get; set; } -> float"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def TargetLocation(self) -> _n_2_t_1:"""TargetLocation { get; set; } -> Point3d"""
    def __init__(self) -> PointLightTraits:...
class Polyline(_n_3_t_0, _n_4_t_4):
    @property
    def BaseSubEntMarker(self) -> _n_4_t_9:"""BaseSubEntMarker { get; set; } -> IntPtr"""
    @property
    def Normal(self) -> _n_2_t_0:"""Normal { get; set; } -> Vector3d"""
    @property
    def Points(self) -> _n_2_t_6:"""Points { get; set; } -> Point3dCollection"""
    def __init__(self) -> Polyline:...
    def __init__(self, pPoints: _n_2_t_6, normal: _n_2_t_0, pBaseSubEntMarker: _n_4_t_9) -> Polyline:...
class PolylineCollection(_n_3_t_0, _n_4_t_4, typing.Iterable[Polyline]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def Item(self) -> Polyline:"""Item { get; set; } -> Polyline"""
    def __init__(self) -> PolylineCollection:...
    def Add(self, value: Polyline) -> int:...
    def Clear(self):...
    def RemoveAt(self, index: int):...
class PositionBehavior(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Screen: int
    ScreenLocalOrigin: int
    value__: int
    Viewport: int
    World: int
    WorldWithScreenOffset: int
class ProceduralTexture(MaterialTexture, _n_4_t_4, _n_4_t_6):
    def __init__(self) -> ProceduralTexture:...
class ProceduralTextureType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Generic: int
    Marble: int
    value__: int
    Wood: int
class Projection(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Box: int
    Cylinder: int
    InheritProjection: int
    Planar: int
    Sphere: int
    value__: int
class RapidRTFilterType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Box: int
    Gaussian: int
    Lanczos: int
    Mitchell: int
    Triangle: int
    value__: int
class RapidRTLightingMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Advanced: int
    Basic: int
    Simplified: int
    value__: int
class RapidRTQuitCondition(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ERenderLevel: int
    ERenderTime: int
    value__: int
class RapidRTRenderSettingsTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def FilterHeight(self) -> float:"""FilterHeight { get; set; } -> float"""
    @property
    def FilterType(self) -> RapidRTFilterType:"""FilterType { get; set; } -> RapidRTFilterType"""
    @property
    def FilterWidth(self) -> float:"""FilterWidth { get; set; } -> float"""
    @property
    def LightingMode(self) -> RapidRTLightingMode:"""LightingMode { get; set; } -> RapidRTLightingMode"""
    @property
    def QuitCondition(self) -> RapidRTQuitCondition:"""QuitCondition { get; set; } -> RapidRTQuitCondition"""
    @property
    def RenderLevel(self) -> int:"""RenderLevel { get; set; } -> int"""
    @property
    def RenderTime(self) -> int:"""RenderTime { get; set; } -> int"""
class RegenType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ForExplode: int
    HideOrShadeCommand: int
    Invalid: int
    RenderCommand: int
    SaveWorldDrawForProxy: int
    ShadedDisplay: int
    StandardDisplay: int
    value__: int
class RenderEnvironmentTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def Enable(self) -> bool:"""Enable { get; set; } -> bool"""
    @property
    def EnvironmentMap(self) -> MaterialTexture:"""EnvironmentMap { get; set; } -> MaterialTexture"""
    @property
    def FarDistance(self) -> float:"""FarDistance { get; set; } -> float"""
    @property
    def FarPercentage(self) -> float:"""FarPercentage { get; set; } -> float"""
    @property
    def FogColor(self) -> _n_0_t_0:"""FogColor { get; set; } -> EntityColor"""
    @property
    def IsBackground(self) -> bool:"""IsBackground { get; set; } -> bool"""
    @property
    def NearDistance(self) -> float:"""NearDistance { get; set; } -> float"""
    @property
    def NearPercentage(self) -> float:"""NearPercentage { get; set; } -> float"""
class RenderSettingsTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def BackFacesEnabled(self) -> bool:"""BackFacesEnabled { get; set; } -> bool"""
    @property
    def DiagnosticBackgroundEnabled(self) -> bool:"""DiagnosticBackgroundEnabled { get; set; } -> bool"""
    @property
    def MaterialEnabled(self) -> bool:"""MaterialEnabled { get; set; } -> bool"""
    @property
    def ModelScaleFactor(self) -> float:"""ModelScaleFactor { get; set; } -> float"""
    @property
    def ShadowsEnabled(self) -> bool:"""ShadowsEnabled { get; set; } -> bool"""
    @property
    def TextureSampling(self) -> bool:"""TextureSampling { get; set; } -> bool"""
class ScaleBehavior(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Screen: int
    ScreenLocalOrigin: int
    value__: int
    Viewport: int
    ViewportLocalOrigin: int
    World: int
class SelectionFlags(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    _None: int
    SelectionIgnore: int
    value__: int
class ShadowFlags(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ShadowsCastAndReceive: int
    ShadowsDoesNotCast: int
    ShadowsDoesNotReceive: int
    ShadowsIgnore: int
    value__: int
class ShadowMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Segments: int
    Simple: int
    Sorted: int
    value__: int
class ShadowParameters(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def ExtendedLightLength(self) -> float:"""ExtendedLightLength { get; set; } -> float"""
    @property
    def ExtendedLightRadius(self) -> float:"""ExtendedLightRadius { get; set; } -> float"""
    @property
    def ExtendedLightShape(self) -> ExtendedLightShape:"""ExtendedLightShape { get; set; } -> ExtendedLightShape"""
    @property
    def ExtendedLightWidth(self) -> float:"""ExtendedLightWidth { get; set; } -> float"""
    @property
    def ShadowMapSize(self) -> int:"""ShadowMapSize { get; set; } -> int"""
    @property
    def ShadowMapSoftness(self) -> _n_4_t_10:"""ShadowMapSoftness { get; set; } -> Byte"""
    @property
    def ShadowSamples(self) -> int:"""ShadowSamples { get; set; } -> int"""
    @property
    def ShadowsOn(self) -> bool:"""ShadowsOn { get; set; } -> bool"""
    @property
    def ShadowType(self) -> ShadowType:"""ShadowType { get; set; } -> ShadowType"""
    @property
    def ShapeVisibility(self) -> bool:"""ShapeVisibility { get; set; } -> bool"""
    def __init__(self) -> ShadowParameters:...
class ShadowType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Maps: int
    RayTraced: int
    Sampled: int
    value__: int
class SkyBackgroundTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def SkyParameters(self) -> SkyParameters:"""SkyParameters { get; set; } -> SkyParameters"""
class SkyParameters(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def AerialPerspective(self) -> bool:"""AerialPerspective { get; set; } -> bool"""
    @property
    def DiskIntensity(self) -> float:"""DiskIntensity { get; set; } -> float"""
    @property
    def DiskScale(self) -> float:"""DiskScale { get; set; } -> float"""
    @property
    def GlowIntensity(self) -> float:"""GlowIntensity { get; set; } -> float"""
    @property
    def GroundColor(self) -> _n_0_t_1:"""GroundColor { get; set; } -> Color"""
    @property
    def Haze(self) -> float:"""Haze { get; set; } -> float"""
    @property
    def HorizonBlur(self) -> float:"""HorizonBlur { get; set; } -> float"""
    @property
    def HorizonHeight(self) -> float:"""HorizonHeight { get; set; } -> float"""
    @property
    def Illumination(self) -> bool:"""Illumination { get; set; } -> bool"""
    @property
    def IntensityFactor(self) -> float:"""IntensityFactor { get; set; } -> float"""
    @property
    def NightColor(self) -> _n_0_t_1:"""NightColor { get; set; } -> Color"""
    @property
    def RedBlueShift(self) -> float:"""RedBlueShift { get; set; } -> float"""
    @property
    def Saturation(self) -> float:"""Saturation { get; set; } -> float"""
    @property
    def SolarDiskSamples(self) -> int:"""SolarDiskSamples { get; set; } -> int"""
    @property
    def SunDirection(self) -> _n_2_t_0:"""SunDirection { get; set; } -> Vector3d"""
    @property
    def VisibilityDistance(self) -> float:"""VisibilityDistance { get; set; } -> float"""
    def __init__(self) -> SkyParameters:...
class SolidBackgroundTraits(NonEntityTraits, _n_4_t_4, _n_4_t_6):
    @property
    def ColorSolid(self) -> _n_0_t_0:"""ColorSolid { get; set; } -> EntityColor"""
class Source(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    File: int
    Procedural: int
    Scene: int
    value__: int
class SpotLightTraits(StandardLightTraits, _n_4_t_4, _n_4_t_6):
    @property
    def Attenuation(self) -> LightAttenuation:"""Attenuation { get; set; } -> LightAttenuation"""
    @property
    def Falloff(self) -> float:"""Falloff { get; } -> float"""
    @property
    def Hotspot(self) -> float:"""Hotspot { get; } -> float"""
    @property
    def LampColor(self) -> ColorRGB:"""LampColor { get; set; } -> ColorRGB"""
    @property
    def PhysicalIntensity(self) -> float:"""PhysicalIntensity { get; set; } -> float"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; set; } -> Point3d"""
    @property
    def TargetLocation(self) -> _n_2_t_1:"""TargetLocation { get; set; } -> Point3d"""
    def __init__(self) -> SpotLightTraits:...
    def SetHotspotAndFalloff(self, hotspot: float, falloff: float) -> bool:...
class StandardLightTraits(LightTraits, _n_4_t_4, _n_4_t_6):
    @property
    def Intensity(self) -> float:"""Intensity { get; set; } -> float"""
    @property
    def LightColor(self) -> _n_0_t_1:"""LightColor { get; set; } -> Color"""
    @property
    def Shadow(self) -> ShadowParameters:"""Shadow { get; set; } -> ShadowParameters"""
    def __init__(self) -> StandardLightTraits:...
class SubEntityTraits(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Color(self) -> int:"""Color { get; set; } -> int"""
    @property
    def DrawFlags(self) -> int:"""DrawFlags { get; set; } -> int"""
    @property
    def Fill(self) -> Fill:"""Fill { get; set; } -> Fill"""
    @property
    def FillType(self) -> FillType:"""FillType { get; set; } -> FillType"""
    @property
    def Layer(self) -> _n_1_t_1:"""Layer { get; set; } -> ObjectId"""
    @property
    def LineType(self) -> _n_1_t_1:"""LineType { get; set; } -> ObjectId"""
    @property
    def LineTypeScale(self) -> float:"""LineTypeScale { get; set; } -> float"""
    @property
    def LineWeight(self) -> _n_1_t_0:"""LineWeight { get; set; } -> LineWeight"""
    @property
    def Mapper(self) -> Mapper:"""Mapper { get; set; } -> Mapper"""
    @property
    def Material(self) -> _n_1_t_1:"""Material { get; set; } -> ObjectId"""
    @property
    def PlotStyleDescriptor(self) -> _n_1_t_6:"""PlotStyleDescriptor { get; set; } -> PlotStyleDescriptor"""
    @property
    def Sectionable(self) -> bool:"""Sectionable { get; set; } -> bool"""
    @property
    def SelectionOnlyGeometry(self) -> bool:"""SelectionOnlyGeometry { get; set; } -> bool"""
    @property
    def ShadowFlags(self) -> ShadowFlags:"""ShadowFlags { get; set; } -> ShadowFlags"""
    @property
    def Thickness(self) -> float:"""Thickness { get; set; } -> float"""
    @property
    def Transparency(self) -> _n_0_t_2:"""Transparency { get; set; } -> Transparency"""
    @property
    def TrueColor(self) -> _n_0_t_0:"""TrueColor { get; set; } -> EntityColor"""
    @property
    def VisualStyle(self) -> _n_1_t_1:"""VisualStyle { get; set; } -> ObjectId"""
    def SetSelectionMarker(self, markerId: _n_4_t_9):...
class TextStyle(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Backward(self) -> bool:"""Backward { get; set; } -> bool"""
    @property
    def BigFontFileName(self) -> str:"""BigFontFileName { get; set; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; set; } -> str"""
    @property
    def Font(self) -> FontDescriptor:"""Font { get; set; } -> FontDescriptor"""
    @property
    def LoadStyleRec(self) -> _n_4_t_10:"""LoadStyleRec { get; } -> Byte"""
    @property
    def ObliquingAngle(self) -> float:"""ObliquingAngle { get; set; } -> float"""
    @property
    def Overlined(self) -> bool:"""Overlined { get; set; } -> bool"""
    @property
    def PreLoaded(self) -> bool:"""PreLoaded { get; set; } -> bool"""
    @property
    def Strikethrough(self) -> bool:"""Strikethrough { get; set; } -> bool"""
    @property
    def StyleName(self) -> str:"""StyleName { get; set; } -> str"""
    @property
    def TextSize(self) -> float:"""TextSize { get; set; } -> float"""
    @property
    def TrackingPercent(self) -> float:"""TrackingPercent { get; set; } -> float"""
    @property
    def Underlined(self) -> bool:"""Underlined { get; set; } -> bool"""
    @property
    def UpsideDown(self) -> bool:"""UpsideDown { get; set; } -> bool"""
    @property
    def Vertical(self) -> bool:"""Vertical { get; set; } -> bool"""
    @property
    def XScale(self) -> float:"""XScale { get; set; } -> float"""
    def __init__(self) -> TextStyle:...
    def __init__(self, fontName: str, bigFontName: str, textSize: float, x: float, obliqueAngle: float, trackingPercent: float, isBackward: bool, isUpsideDown: bool, isVertical: bool, isOverLined: bool, isUnderlined: bool, isStrikethrough: bool, styleName: str) -> TextStyle:...
    def ExtentsBox(self, value1: str, includeSpaces: bool, raw: bool, context: WorldDraw) -> _n_1_t_7:...
    def FromTextStyleTableRecord(self, AcDbStyleId: _n_1_t_1):...
    def FromTextStyleTableRecord(self, AcDbStyleName: str):...
    def SetTrackKerning(self, trackPercent: float):...
    def ToTextStyleTableRecord(self) -> _n_1_t_1:...
    def ToTextStyleTableRecord(self, AcDbStyleId: _n_1_t_1):...
    def ToTextStyleTableRecord(self, AcDbStyleName: str) -> _n_1_t_1:...
class TileOrder(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BottomToTop: int
    Hilbert: int
    LeftToRight: int
    RightToLeft: int
    Spiral: int
    TopToBottom: int
    value__: int
class Tiling(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Clamp: int
    Crop: int
    InheritTiling: int
    Mirror: int
    Tile: int
    value__: int
class ToneOperatorParameters(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Brightness(self) -> float:"""Brightness { get; set; } -> float"""
    @property
    def ChromaticAdaptation(self) -> bool:"""ChromaticAdaptation { get; set; } -> bool"""
    @property
    def ColorDifferentiation(self) -> bool:"""ColorDifferentiation { get; set; } -> bool"""
    @property
    def Contrast(self) -> float:"""Contrast { get; set; } -> float"""
    @property
    def ExteriorDaylight(self) -> ExteriorDaylightMode:"""ExteriorDaylight { get; set; } -> ExteriorDaylightMode"""
    @property
    def IsActive(self) -> bool:"""IsActive { get; set; } -> bool"""
    @property
    def MidTones(self) -> float:"""MidTones { get; set; } -> float"""
    @property
    def ProcessBackground(self) -> bool:"""ProcessBackground { get; set; } -> bool"""
    @property
    def WhiteColor(self) -> _n_0_t_1:"""WhiteColor { get; set; } -> Color"""
    def __init__(self) -> ToneOperatorParameters:...
class TransientDrawingMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Contrast: int
    Count: int
    DirectShortTerm: int
    DirectTopmost: int
    Highlight: int
    Main: int
    Sprite: int
    value__: int
class TransientManager(_n_3_t_0, _n_4_t_4):
    @property
    def CurrentTransientManager(self) -> TransientManager:"""CurrentTransientManager { get; set; } -> TransientManager"""
    def AddChildTransient(self, added: Drawable, parent: Drawable) -> bool:...
    def AddTransient(self, added: Drawable, mode: TransientDrawingMode, subDrawingMode: int, viewportNumbers: _n_2_t_11) -> bool:...
    def EraseChildTransient(self, erased: Drawable, parent: Drawable) -> bool:...
    def EraseTransient(self, erased: Drawable, viewportNumbers: _n_2_t_11) -> bool:...
    def EraseTransients(self, mode: TransientDrawingMode, subDrawingMode: int, viewportNumbers: _n_2_t_11) -> bool:...
    def GetFreeSubDrawingMode(self, mode: TransientDrawingMode, viewportNumbers: _n_2_t_11, subDrawingMode: int) -> int:...
    def UpdateChildTransient(self, updated: Drawable, parent: Drawable):...
    def UpdateTransient(self, updated: Drawable, viewportNumbers: _n_2_t_11):...
class TransparencyMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Transparency1Bit: int
    Transparency8Bit: int
    TransparencyOff: int
    value__: int
class VariantType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Boolean: int
    Color: int
    Double: int
    Int: int
    String: int
    Table: int
    Undefined: int
    value__: int
class VertexData(object):
    @property
    def OrientationFlag(self) -> OrientationType:"""OrientationFlag { get; set; } -> OrientationType"""
    def __init__(self) -> VertexData:...
    def get_MappingCoords(self, mapChannel: MapChannel) -> _n_4_t_8[_n_2_t_1]:...
    def GetNormalVectors(self) -> _n_4_t_8[_n_2_t_0]:...
    def GetTrueColors(self) -> _n_4_t_8[_n_0_t_0]:...
    def set_MappingCoords(self, mapChannel: MapChannel, coords: _n_4_t_8[_n_2_t_1]):...
    def SetNormalVectors(self, normal: _n_4_t_8[_n_2_t_0]):...
    def SetTrueColors(self, colors: _n_4_t_8[_n_0_t_0]):...
class Viewport(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def AcadWindowId(self) -> int:"""AcadWindowId { get; } -> int"""
    @property
    def CameraLocation(self) -> _n_2_t_1:"""CameraLocation { get; } -> Point3d"""
    @property
    def CameraTarget(self) -> _n_2_t_1:"""CameraTarget { get; } -> Point3d"""
    @property
    def CameraUpVector(self) -> _n_2_t_0:"""CameraUpVector { get; } -> Vector3d"""
    @property
    def DeviceContextViewportCorners(self) -> _n_1_t_7:"""DeviceContextViewportCorners { get; } -> Extents2d"""
    @property
    def EyeToModelTransform(self) -> _n_2_t_2:"""EyeToModelTransform { get; } -> Matrix3d"""
    @property
    def EyeToWorldTransform(self) -> _n_2_t_2:"""EyeToWorldTransform { get; } -> Matrix3d"""
    @property
    def FrontAndBackClipping(self) -> FrontAndBackClipping:"""FrontAndBackClipping { get; } -> FrontAndBackClipping"""
    @property
    def IsPerspective(self) -> bool:"""IsPerspective { get; } -> bool"""
    @property
    def LinetypeGenerationCriteria(self) -> float:"""LinetypeGenerationCriteria { get; } -> float"""
    @property
    def LinetypeScaleMultiplier(self) -> float:"""LinetypeScaleMultiplier { get; } -> float"""
    @property
    def ModelToEyeTransform(self) -> _n_2_t_2:"""ModelToEyeTransform { get; } -> Matrix3d"""
    @property
    def ViewDirection(self) -> _n_2_t_0:"""ViewDirection { get; } -> Vector3d"""
    @property
    def ViewportId(self) -> _n_4_t_9:"""ViewportId { get; } -> IntPtr"""
    @property
    def WorldToEyeTransform(self) -> _n_2_t_2:"""WorldToEyeTransform { get; } -> Matrix3d"""
    def DoInversePerspective(self, value: _n_2_t_1) -> _n_2_t_1:...
    def DoPerspective(self, value: _n_2_t_1) -> _n_2_t_1:...
    def GetNumPixelsInUnitSquare(self, givenWorldPoint: _n_2_t_1) -> _n_2_t_10:...
    def LayerVisible(self, idLayer: _n_1_t_1) -> bool:...
class ViewportDraw(CommonDraw, _n_4_t_4, _n_4_t_6):
    @property
    def Geometry(self) -> ViewportGeometry:"""Geometry { get; } -> ViewportGeometry"""
    @property
    def SequenceNumber(self) -> int:"""SequenceNumber { get; } -> int"""
    @property
    def Viewport(self) -> Viewport:"""Viewport { get; } -> Viewport"""
    @property
    def ViewportObjectId(self) -> _n_1_t_1:"""ViewportObjectId { get; } -> ObjectId"""
    def IsValidId(self, id: _n_4_t_9) -> bool:...
class ViewportGeometry(Geometry, _n_4_t_4, _n_4_t_6):
    def DeviceContextPolygon(self, points: _n_2_t_6) -> bool:...
    def DeviceContextPolyline(self, points: _n_2_t_6) -> bool:...
    def DeviceContextRasterImage(self, origin: _n_2_t_1, u: _n_2_t_0, v: _n_2_t_0, pixel: _n_2_t_13, entityId: _n_1_t_1, imageOrg: ImageOrg, imageWidth: int, imageHeight: int, imageColorDepth: int, transparency: bool, source: ImageSource, unRotated: _n_2_t_0, originalImage: ImageOrg, unRotatedPixel: _n_2_t_13, unRotatedImageWidth: int, unRotatedImageHeight: int) -> bool:...
    def PolygonEye(self, points: _n_2_t_6) -> bool:...
    def PolylineEye(self, points: _n_2_t_6) -> bool:...
class ViewportTraits(DrawableTraits, _n_4_t_4, _n_4_t_6):
    @property
    def AmbientLightColor(self) -> _n_0_t_1:"""AmbientLightColor { get; set; } -> Color"""
    @property
    def Background(self) -> _n_1_t_1:"""Background { get; set; } -> ObjectId"""
    @property
    def Brightness(self) -> float:"""Brightness { get; set; } -> float"""
    @property
    def Contrast(self) -> float:"""Contrast { get; set; } -> float"""
    @property
    def DefaultLightingOn(self) -> bool:"""DefaultLightingOn { get; set; } -> bool"""
    @property
    def DefaultLightingType(self) -> DefaultLightingType:"""DefaultLightingType { get; set; } -> DefaultLightingType"""
    @property
    def RenderEnvironment(self) -> _n_1_t_1:"""RenderEnvironment { get; set; } -> ObjectId"""
    @property
    def RenderSettings(self) -> _n_1_t_1:"""RenderSettings { get; set; } -> ObjectId"""
    @property
    def ToneOperatorParameters(self) -> ToneOperatorParameters:"""ToneOperatorParameters { get; set; } -> ToneOperatorParameters"""
    def __init__(self) -> ViewportTraits:...
class VisualStyle(_n_3_t_1, _n_4_t_4, _n_4_t_6):
    @property
    def Type(self) -> VisualStyleType:"""Type { get; set; } -> VisualStyleType"""
    def __init__(self) -> VisualStyle:...
    def __init__(self, type: VisualStyleType) -> VisualStyle:...
    def GetPropertyType(self, prop: VisualStyleProperty) -> VariantType:...
    def GetTrait(self, prop: VisualStyleProperty) -> object:...
    def GetTraitFlag(self, prop: VisualStyleProperty, flagVal: _n_4_t_11) -> bool:...
    def Operation(self, prop: VisualStyleProperty) -> VisualStyleOperation:...
    def SetTrait(self, prop: VisualStyleProperty, val: object, op: VisualStyleOperation):...
    def SetTrait(self, prop: VisualStyleProperty, nVal: int, op: VisualStyleOperation):...
    def SetTrait(self, prop: VisualStyleProperty, bVal: bool, __unnamed002: VisualStyleOperation):...
    def SetTrait(self, prop: VisualStyleProperty, dVal: float, op: VisualStyleOperation):...
    def SetTrait(self, prop: VisualStyleProperty, red: float, green: float, blue: float, op: VisualStyleOperation):...
    def SetTrait(self, prop: VisualStyleProperty, color: _n_0_t_1, op: VisualStyleOperation):...
    def SetTrait(self, prop: VisualStyleProperty, op: VisualStyleOperation):...
    def SetTraitFlag(self, prop: VisualStyleProperty, flagVal: _n_4_t_11, bEnable: bool):...
class VisualStyleOperation(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Disable: int
    Enable: int
    Inherit: int
    InvalidOperation: int
    Set: int
    value__: int
class VisualStyleProperty(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BloomEffect: int
    BloomIntensity: int
    BloomRadius: int
    BloomThreshold: int
    BlurAmount: int
    BlurEffect: int
    Color: int
    DepthOfField: int
    DisplayBrightness: int
    DisplayShadowType: int
    DisplayStyle: int
    EdgeColor: int
    EdgeCreaseAngle: int
    EdgeHaloGap: int
    EdgeHidePrecision: int
    EdgeIntersectionColor: int
    EdgeIntersectionLinePattern: int
    EdgeIsolines: int
    EdgeJitterAmount: int
    EdgeModel: int
    EdgeModifier: int
    EdgeObscuredColor: int
    EdgeObscuredLinePattern: int
    EdgeOpacity: int
    EdgeOverhang: int
    EdgeSilhouetteColor: int
    EdgeSilhouetteWidth: int
    EdgeStyle: int
    EdgeTexturePath: int
    EdgeWidth: int
    EdgeWiggleAmount: int
    FaceAdjustment: int
    FaceColorMode: int
    FaceLightingModel: int
    FaceLightingQuality: int
    FaceModifier: int
    FaceMonoColor: int
    FaceOpacity: int
    FaceSpecular: int
    FocusDistance: int
    FocusWidth: int
    InvalidProperty: int
    LightingEnabled: int
    MonoEffect: int
    PastelEffect: int
    PencilAngle: int
    PencilColor: int
    PencilEffect: int
    PencilPattern: int
    PencilScale: int
    PostBrightness: int
    PostContrast: int
    PosterizeEffect: int
    PostPower: int
    PropertyCount: int
    TintColor: int
    TintEffect: int
    Transparency: int
    UseDrawOrder: int
    value__: int
    ViewportTransparency: int
class VisualStyleTraits(DrawableTraits, _n_4_t_4, _n_4_t_6):
    @property
    def AcGiVisualStyle(self) -> VisualStyle:"""AcGiVisualStyle { get; set; } -> VisualStyle"""
class VisualStyleType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Basic: int
    Brighten: int
    ColorChange: int
    Conceptual: int
    Custom: int
    Dim: int
    DisplayOnly: int
    EdgeColorOff: int
    EdgeOnly: int
    EmptyStyle: int
    FaceOnly: int
    FacePattern: int
    Flat: int
    FlatWithEdges: int
    Gouraud: int
    GouraudWithEdges: int
    Hidden: int
    JitterOff: int
    LinePattern: int
    OverhangOff: int
    Realistic: int
    Shaded: int
    ShadedWithEdges: int
    ShadesOfGray: int
    Sketchy: int
    Thicken: int
    value__: int
    Wireframe2D: int
    Wireframe3D: int
    XRay: int
class VSDisplayShadowType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Full: int
    FullAndGround: int
    GroundPlane: int
    _None: int
    value__: int
class VSDisplayStyles(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BackgroundsFlag: int
    LightingFlag: int
    MaterialsFlag: int
    _None: int
    TexturesFlag: int
    value__: int
class VSEdgeJitterAmount(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    JitterHigh: int
    JitterLow: int
    JitterMedium: int
    value__: int
class VSEdgeLinePattern(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Dashed: int
    Dotted: int
    DoubleLongDash: int
    DoubleMediumDash: int
    DoubleShortDash: int
    LongDash: int
    MediumDash: int
    MediumLongDash: int
    ShortDash: int
    Solid: int
    SparseDot: int
    value__: int
class VSEdgeModel(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    FacetEdges: int
    Isolines: int
    NoEdges: int
    value__: int
class VSEdgeModifiers(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    AlwaysOnTopFlag: int
    EdgeColorFlag: int
    EdgeHaloGapFlag: int
    EdgeJitterFlag: int
    EdgeOpacityFlag: int
    EdgeOverhangFlag: int
    EdgeWidthFlag: int
    _None: int
    value__: int
class VSEdgeStyles(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    IntersectionFlag: int
    _None: int
    ObscuredFlag: int
    SilhouetteFlag: int
    value__: int
    VisibleFlag: int
class VSFaceColorMode(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    BackgroundColor: int
    Desaturate: int
    Mono: int
    _None: int
    ObjectColor: int
    Tint: int
    value__: int
class VSFaceLightingModel(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Constant: int
    Gooch: int
    Invisible: int
    Phong: int
    value__: int
class VSFaceLightingQuality(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    NoLighting: int
    PerFaceLighting: int
    PerPixelLighting: int
    PerVertexLighting: int
    value__: int
class VSFaceModifiers(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    FaceOpacityFlag: int
    _None: int
    SpecularFlag: int
    value__: int
class WebFileType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    TypeA: int
    TypeB: int
    TypeC: int
    value__: int
class WebLightTraits(PointLightTraits, _n_4_t_4, _n_4_t_6):
    @property
    def WebFile(self) -> str:"""WebFile { get; set; } -> str"""
    @property
    def WebFileType(self) -> WebFileType:"""WebFileType { get; set; } -> WebFileType"""
    @property
    def WebFlux(self) -> float:"""WebFlux { get; set; } -> float"""
    @property
    def WebHorzAng90to270(self) -> bool:"""WebHorzAng90to270 { get; set; } -> bool"""
    @property
    def WebRotation(self) -> _n_2_t_0:"""WebRotation { get; set; } -> Vector3d"""
    @property
    def WebSymmetry(self) -> WebSymmetry:"""WebSymmetry { get; set; } -> WebSymmetry"""
    def __init__(self) -> WebLightTraits:...
class WebSymmetry(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    AxialSymmetry: int
    DoubleSymmetry: int
    NoSymmetry: int
    SingleSymmetry: int
    value__: int
class WoodTexture(ProceduralTexture, _n_4_t_4, _n_4_t_6):
    @property
    def AxialNoise(self) -> float:"""AxialNoise { get; set; } -> float"""
    @property
    def Color1(self) -> MaterialColor:"""Color1 { get; set; } -> MaterialColor"""
    @property
    def Color2(self) -> MaterialColor:"""Color2 { get; set; } -> MaterialColor"""
    @property
    def GrainThickness(self) -> float:"""GrainThickness { get; set; } -> float"""
    @property
    def RadialNoise(self) -> float:"""RadialNoise { get; set; } -> float"""
    def __init__(self) -> WoodTexture:...
    def Set(self, value: WoodTexture):...
class WorldDraw(CommonDraw, _n_4_t_4, _n_4_t_6):
    @property
    def Geometry(self) -> WorldGeometry:"""Geometry { get; } -> WorldGeometry"""
class WorldGeometry(Geometry, _n_4_t_4, _n_4_t_6):
    def SetExtents(self, extents: _n_1_t_3):...
    def StartAttributesSegment(self):...
