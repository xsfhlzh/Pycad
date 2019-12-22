from __clrclasses__.Autodesk.AutoCAD import UniqueString as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ViewportTableRecord as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Extents2d as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3dCollection as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3d as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2d as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import Drawable as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import TransientDrawingMode as _n_3_t_1
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import VisualStyle as _n_3_t_2
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_4_t_0
from __clrclasses__.System import ValueType as _n_5_t_0
from __clrclasses__.System import IDisposable as _n_5_t_1
from __clrclasses__.System import Array as _n_5_t_2
from __clrclasses__.System import MulticastDelegate as _n_5_t_3
from __clrclasses__.System import ICloneable as _n_5_t_4
from __clrclasses__.System import IntPtr as _n_5_t_5
from __clrclasses__.System import IAsyncResult as _n_5_t_6
from __clrclasses__.System import EventArgs as _n_5_t_7
from __clrclasses__.System import AsyncCallback as _n_5_t_8
from __clrclasses__.System import Enum as _n_5_t_9
from __clrclasses__.System import IComparable as _n_5_t_10
from __clrclasses__.System import IFormattable as _n_5_t_11
from __clrclasses__.System import IConvertible as _n_5_t_12
from __clrclasses__.System import EventHandler as _n_5_t_13
from __clrclasses__.System.Collections.Generic import List as _n_6_t_0
from __clrclasses__.System.Drawing import Color as _n_7_t_0
from __clrclasses__.System.Drawing import Bitmap as _n_7_t_1
from __clrclasses__.System.Drawing import Rectangle as _n_7_t_2
from __clrclasses__.System.Drawing import Size as _n_7_t_3
from __clrclasses__.System.Drawing import Point as _n_7_t_4
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_8_t_0
from __clrclasses__.System.Windows import Size as _n_9_t_0
import typing
class CertificationData(object):
    @property
    def CardName(self) -> str:"""CardName { get; set; } -> str"""
    @property
    def CertificationStatus(self) -> int:"""CertificationStatus { get; set; } -> int"""
    @property
    def DriverVersion(self) -> str:"""DriverVersion { get; set; } -> str"""
    @property
    def FailedDevices(self) -> str:"""FailedDevices { get; set; } -> str"""
    @property
    def HardwareFeatureLevel(self) -> int:"""HardwareFeatureLevel { get; set; } -> int"""
    @property
    def HardwareID(self) -> int:"""HardwareID { get; set; } -> int"""
    @property
    def ProductDriverURL(self) -> str:"""ProductDriverURL { get; set; } -> str"""
    @property
    def SoftwareFeatureLevel(self) -> int:"""SoftwareFeatureLevel { get; set; } -> int"""
    @property
    def TuningDate(self) -> str:"""TuningDate { get; set; } -> str"""
    def __init__(self) -> CertificationData:...
class ClientViewInfo(_n_5_t_0):
    @property
    def AcadWindowId(self) -> int:"""AcadWindowId { get; set; } -> int"""
    @property
    def ViewportId(self) -> int:"""ViewportId { get; set; } -> int"""
    @property
    def ViewportObjectId(self) -> int:"""ViewportObjectId { get; set; } -> int"""
    def __init__(self) -> ClientViewInfo:...
class Configuration(_n_4_t_0, _n_5_t_1):
    @property
    def AdaptiveDegradation(self) -> bool:"""AdaptiveDegradation { get; set; } -> bool"""
    @property
    def CurrentDisplayDriver(self) -> DriverInfo:"""CurrentDisplayDriver { get; } -> DriverInfo"""
    @property
    def CurveTessellationTolerance(self) -> int:"""CurveTessellationTolerance { get; set; } -> int"""
    @property
    def DefaultHardwareAcceleratedDriver(self) -> DriverInfo:"""DefaultHardwareAcceleratedDriver { get; } -> DriverInfo"""
    @property
    def DiscardBackFaces(self) -> bool:"""DiscardBackFaces { get; set; } -> bool"""
    @property
    def DriverName(self) -> str:"""DriverName { get; } -> str"""
    @property
    def DriverRevision(self) -> int:"""DriverRevision { get; } -> int"""
    @property
    def DriverSearchPath(self) -> str:"""DriverSearchPath { get; set; } -> str"""
    @property
    def DriverVersion(self) -> int:"""DriverVersion { get; } -> int"""
    @property
    def DynamicTessellation(self) -> bool:"""DynamicTessellation { get; set; } -> bool"""
    @property
    def FrameRate(self) -> int:"""FrameRate { get; set; } -> int"""
    @property
    def GenerateVertexNormals(self) -> bool:"""GenerateVertexNormals { get; set; } -> bool"""
    @property
    def Handedness(self) -> Handedness:"""Handedness { get; set; } -> Handedness"""
    @property
    def HardwareAcceleratedDriver(self) -> DriverInfo:"""HardwareAcceleratedDriver { get; set; } -> DriverInfo"""
    @property
    def MaxLODs(self) -> int:"""MaxLODs { get; set; } -> int"""
    @property
    def RedrawOnWindowExpose(self) -> bool:"""RedrawOnWindowExpose { get; set; } -> bool"""
    @property
    def SurfaceTessellationTolerance(self) -> int:"""SurfaceTessellationTolerance { get; set; } -> int"""
    @property
    def Transparency(self) -> Quality:"""Transparency { get; set; } -> Quality"""
    def __init__(self) -> Configuration:...
    def Configure(self) -> bool:...
    def DegradationChainPosition(self, channel: DegradationChannel) -> int:...
    def DegradationChannelAt(self, order: int) -> DegradationChannel:...
    def GetCanDegradeChannel(self, channel: DegradationChannel) -> bool:...
    def GetCertificationData(self) -> CertificationData:...
    def GetEffectList(self, type: EffectListType) -> _n_6_t_0[EffectStatus]:...
    def GetHardwareAcceleratedDrivers(self) -> _n_5_t_2[DriverInfo]:...
    def GetVirtualDeviceName(self) -> str:...
    def IsFeatureAvailable(self, feature: _n_0_t_0) -> bool:...
    def IsFeatureEnabled(self, feature: _n_0_t_0) -> bool:...
    def IsFeatureRecommended(self, feature: _n_0_t_0) -> bool:...
    def IsHardwareAccelerationAvailable(self) -> bool:...
    def IsHardwareAccelerationEnabled(self) -> bool:...
    def IsHardwareAccelerationRecommended(self) -> bool:...
    def IsNoHardwareOverrideEnabled(self) -> bool:...
    def SetCanDegradeChannel(self, channel: DegradationChannel, degrade: bool):...
    def SetFeatureEnabled(self, feature: _n_0_t_0, enable: bool):...
    def setHardwareAcceleration(self, bEnable: bool):...
    def ShiftDegradationChainPosition(self, channel: DegradationChannel, shiftDown: bool):...
    def ShowConfigDialog(self, dlgType: str) -> bool:...
class ConfigWasModifiedEventHandler(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> ConfigWasModifiedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_5_t_7, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, sender: object, e: _n_5_t_7):...
class DefaultLightingType(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    OneLight: int
    TwoLights: int
    value__: int
class DegradationChannel(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    Backgrounds: int
    DegradationChannels: int
    DiscardBackfaces: int
    EdgeStyles: int
    Faceted: int
    FacetEdges: int
    FastSilhouette: int
    IntersectEdges: int
    Lighting: int
    LightingQuality: int
    LineAntialias: int
    Materials: int
    ShadowsFull: int
    ShadowsGround: int
    Textures: int
    Transparency: int
    TransparencyQuality: int
    value__: int
    ViewportDraw: int
    Wireframe: int
class Device(_n_4_t_0, _n_5_t_1):
    @property
    def BackgroundColor(self) -> _n_7_t_0:"""BackgroundColor { get; set; } -> Color"""
    @property
    def DeviceRenderType(self) -> RendererType:"""DeviceRenderType { get; set; } -> RendererType"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    def __init__(self, hwnd: _n_5_t_5, deviceType: DeviceType) -> Device:...
    def __init__(self, hwnd: _n_5_t_5) -> Device:...
    def __init__(self) -> Device:...
    def Add(self, view: View) -> bool:...
    def Erase(self, view: View) -> bool:...
    def EraseAll(self):...
    def GetSnapshot(self, rectangle: _n_7_t_2) -> _n_7_t_1:...
    def Invalidate(self, rect: _n_7_t_2):...
    def Invalidate(self):...
    def OnDisplayChange(self, bitsPerPixel: int, xRes: int, yRes: int):...
    def OnRealizeBackgroundPalette(self):...
    def OnRealizeForegroundPalette(self):...
    def OnSize(self, size: _n_7_t_3):...
    def SetLogicalPalette(self, palette: _n_5_t_2[_n_7_t_0]):...
    def SetPhysicalPalette(self, palette: _n_5_t_2[_n_7_t_0]):...
    def Update(self, updatedRect: _n_7_t_2):...
    def Update(self):...
class DeviceType(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    OffScreenDevice: int
    ScreenDevice: int
    SelectionDevice: int
    value__: int
class DriverInfo(_n_5_t_0):
    @property
    def Driver(self) -> str:"""Driver { get; } -> str"""
    @property
    def HardwareAccelerated(self) -> bool:"""HardwareAccelerated { get; } -> bool"""
    @property
    def Path(self) -> str:"""Path { get; } -> str"""
    def __init__(self, hardwareAccelerated: bool, path: str, driver: str) -> DriverInfo:...
    def __init__(self, path: str, driver: str) -> DriverInfo:...
class EffectListType(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    kEL_Current: int
    kEL_File: int
    kEL_RegistryHardware: int
    kEL_RegistrySoftware: int
    value__: int
class EffectStatus(object):
    @property
    def Available(self) -> bool:"""Available { get; set; } -> bool"""
    @property
    def EffectName(self) -> str:"""EffectName { get; set; } -> str"""
    @property
    def EffectUniqueString(self) -> _n_0_t_0:"""EffectUniqueString { get; set; } -> UniqueString"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def FeatureLevel(self) -> int:"""FeatureLevel { get; set; } -> int"""
    @property
    def Recommended(self) -> bool:"""Recommended { get; set; } -> bool"""
    @property
    def EffectOnChanged(self) -> _n_5_t_13:
        """EffectOnChanged Event: EventHandler"""
    def __init__(self) -> EffectStatus:...
class ErrorStatus(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    InvalidInput: int
    OutOfRange: int
    Success: int
    value__: int
class GetInterfaceFunction(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> GetInterfaceFunction:...
    def BeginInvoke(self, objectId: int, bNeedsValidation: bool, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6) -> _n_3_t_0:...
    def Invoke(self, objectId: int, bNeedsValidation: bool) -> _n_3_t_0:...
class GraphicsKernel(_n_4_t_0, _n_5_t_1):
    def __init__(self, unmanagedPointer: _n_5_t_5) -> GraphicsKernel:...
    def __init__(self) -> GraphicsKernel:...
class GsToBeUnloadedEventHandler(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> GsToBeUnloadedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_5_t_7, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, sender: object, e: _n_5_t_7):...
class Handedness(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    Left: int
    Right: int
    value__: int
class HighlightStyle(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    HighlightDashed: int
    value__: int
class InvalidationHint(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    InvalidateAll: int
    InvalidateAllStatic: int
    InvalidateFacets: int
    InvalidateFills: int
    InvalidateIsolines: int
    InvalidateLinetypes: int
    InvalidateMaterials: int
    InvalidateNone: int
    InvalidateViewportCache: int
    value__: int
class KernelDescriptor(_n_4_t_0, _n_5_t_1):
    Drawing2D: int
    Drawing3D: int
    RapidRTRendering3D: int
    Selection3D: int
    def __init__(self) -> KernelDescriptor:...
    def addRequirement(self, capability: _n_0_t_0):...
    def supports(self, capability: _n_0_t_0) -> bool:...
class LinePattern(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    DashDot: int
    Dashed: int
    DefaultLinePattern: int
    Dotted: int
    DoubleLongDash: int
    DoubleMediumDash: int
    DoubleShortDash: int
    LongDash: int
    LongDashDot: int
    LongDashDotDot: int
    LongDashShortDash: int
    MediumDash: int
    MediumDashDotShortDashDot: int
    MediumDashShortDashShortDash: int
    MediumLongDash: int
    ShortDash: int
    Solid: int
    SparseDot: int
    value__: int
class LineWeight(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    kLnWt000: int
    kLnWt005: int
    kLnWt009: int
    kLnWt013: int
    kLnWt015: int
    kLnWt018: int
    kLnWt020: int
    kLnWt025: int
    kLnWt030: int
    kLnWt035: int
    kLnWt040: int
    kLnWt050: int
    kLnWt053: int
    kLnWt060: int
    kLnWt070: int
    kLnWt080: int
    kLnWt090: int
    kLnWt100: int
    kLnWt106: int
    kLnWt120: int
    kLnWt140: int
    kLnWt158: int
    kLnWt200: int
    kLnWt211: int
    kLnWtByBlock: int
    kLnWtByLayer: int
    kLnWtByLwDefault: int
    value__: int
class Manager(_n_4_t_0, _n_5_t_1):
    @property
    def DeviceIndependentDisplaySize(self) -> _n_9_t_0:"""DeviceIndependentDisplaySize { get; } -> Size"""
    @property
    def ConfigWasModified(self) -> ConfigWasModifiedEventHandler:
        """ConfigWasModified Event: ConfigWasModifiedEventHandler"""
    @property
    def GsToBeUnloaded(self) -> GsToBeUnloadedEventHandler:
        """GsToBeUnloaded Event: GsToBeUnloadedEventHandler"""
    @property
    def ViewToBeDestroyed(self) -> ViewToBeDestroyedEventHandler:
        """ViewToBeDestroyed Event: ViewToBeDestroyedEventHandler"""
    @property
    def ViewToBeUpdated(self) -> ViewToBeUpdatedEventHandler:
        """ViewToBeUpdated Event: ViewToBeUpdatedEventHandler"""
    @property
    def ViewWasCreated(self) -> ViewWasCreatedEventHandler:
        """ViewWasCreated Event: ViewWasCreatedEventHandler"""
    @property
    def ViewWasUpdated(self) -> ViewWasUpdatedEventHandler:
        """ViewWasUpdated Event: ViewWasUpdatedEventHandler"""
    @staticmethod
    def AcquireGraphicsKernel(desc: KernelDescriptor) -> GraphicsKernel:...
    def CreateAutoCADDevice(self, __unnamed000: GraphicsKernel, hwnd: _n_5_t_5) -> Device:...
    def CreateAutoCADModel(self, A_0: GraphicsKernel) -> Model:...
    def CreateAutoCADOffScreenDevice(self, A_0: GraphicsKernel) -> Device:...
    def CreateAutoCADView(self, __unnamed000: GraphicsKernel, drawable: _n_3_t_0) -> View:...
    def CreateAutoCADViewport(self, __unnamed000: GraphicsKernel, vp: _n_1_t_0) -> View:...
    def GetCurrent3dAcGsView(self, viewportNumber: int) -> View:...
    def GetCurrentAcGsView(self, viewportNumber: int) -> View:...
    def GetDBModel(self, A_0: GraphicsKernel) -> Model:...
    def GetGsModel(self, mode: _n_3_t_1, subDrawingMode: int, viewportNumber: int) -> Model:...
    def GetGUIDevice(self, A_0: GraphicsKernel) -> Device:...
    def ObtainAcGsView(self, viewportNumber: int, createIfNone: KernelDescriptor) -> View:...
    @staticmethod
    def ReleaseGraphicsKernel(kernel: GraphicsKernel):...
    def SetViewFromViewport(self, view: View, viewportNumber: int):...
    def SetViewportFromView(self, viewportNumber: int, view: View):...
    def SetViewportFromView(self, viewportNumber: int, view: View, regenRequired: bool, rescaleRequired: bool, syncRequired: bool):...
class Manager2(Manager, _n_5_t_1):
    def __init__(self, manager: Manager) -> Manager2:...
    def GetOffScreenDevice(self, A_0: GraphicsKernel) -> Device:...
    def GetOffScreenView(self, A_0: GraphicsKernel, A_1: ClientViewInfo) -> View:...
class Model(_n_4_t_0, _n_5_t_1):
    @property
    def BackgroundId(self) -> _n_1_t_1:"""BackgroundId { get; set; } -> ObjectId"""
    @property
    def EnableSectioning(self) -> bool:"""EnableSectioning { get; set; } -> bool"""
    @property
    def LinetypesEnabled(self) -> bool:"""LinetypesEnabled { get; set; } -> bool"""
    @property
    def RenderType(self) -> RenderType:"""RenderType { get; } -> RenderType"""
    @property
    def SectioningVisualStyle(self) -> _n_1_t_1:"""SectioningVisualStyle { set; } -> ObjectId"""
    @property
    def Selectable(self) -> bool:"""Selectable { get; set; } -> bool"""
    @property
    def ShadowPlaneLocation(self) -> float:"""ShadowPlaneLocation { get; set; } -> float"""
    @property
    def Transform(self) -> _n_2_t_0:"""Transform { get; set; } -> Matrix3d"""
    @property
    def ViewClippingOverride(self) -> bool:"""ViewClippingOverride { set; } -> bool"""
    @property
    def VisualStyle(self) -> _n_3_t_2:"""VisualStyle { get; set; } -> VisualStyle"""
    @property
    def VisualStyleId(self) -> _n_1_t_1:"""VisualStyleId { get; set; } -> ObjectId"""
    def __init__(self, renderType: RenderType) -> Model:...
    def AddSceneGraphRoot(self, pRoot: _n_3_t_0) -> bool:...
    def EraseSceneGraphRoot(self, pRoot: _n_3_t_0) -> bool:...
    def Invalidate(self, hint: InvalidationHint):...
    def OnAdded(self, added: _n_3_t_0, parentId: int):...
    def OnAdded(self, added: _n_3_t_0, parent: _n_3_t_0):...
    def OnErased(self, erased: _n_3_t_0, parentId: int):...
    def OnErased(self, erased: _n_3_t_0, parent: _n_3_t_0):...
    def OnModified(self, modified: _n_3_t_0, parentId: int):...
    def OnModified(self, modified: _n_3_t_0, parent: _n_3_t_0):...
    def OnPaletteModified(self):...
    def SetExtents(self, point3dx: _n_2_t_1, point3dy: _n_2_t_1):...
    def SetSectioning(self, pts: _n_2_t_2, upVector: _n_2_t_3, top: float, bottom: float) -> bool:...
    def SetSectioning(self, pts: _n_2_t_2, upVector: _n_2_t_3) -> bool:...
class Node(_n_4_t_0, _n_5_t_1):
    @property
    def Drawable(self) -> _n_3_t_0:"""Drawable { get; } -> Drawable"""
class Projection(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    Parallel: int
    Perspective: int
    value__: int
class Quality(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    HighQuality: int
    LowQuality: int
    MediumQuality: int
    value__: int
class ReleaseInterfaceFunction(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> ReleaseInterfaceFunction:...
    def BeginInvoke(self, __unnamed000: _n_3_t_0, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, A_0: _n_3_t_0):...
class RendererType(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    Default: int
    FullRender: int
    SelectionRender: int
    Software: int
    SoftwareNewViewsOnly: int
    value__: int
class RenderType(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    Contrast: int
    Count: int
    Direct: int
    DirectTopmost: int
    Highlight: int
    HighlightSelection: int
    Main: int
    Sprite: int
    value__: int
class StereoParameters(_n_5_t_0):
    @property
    def Magnitude(self) -> float:"""Magnitude { get; } -> float"""
    @property
    def Parallax(self) -> float:"""Parallax { get; } -> float"""
    def __init__(self, magnitude: float, parallax: float) -> StereoParameters:...
class View(_n_4_t_0, _n_5_t_1):
    @property
    def AcadWindowId(self) -> int:"""AcadWindowId { get; } -> int"""
    @property
    def BackClip(self) -> float:"""BackClip { get; set; } -> float"""
    @property
    def BackgroundId(self) -> _n_1_t_1:"""BackgroundId { get; set; } -> ObjectId"""
    @property
    def Device(self) -> Device:"""Device { get; } -> Device"""
    @property
    def EnableBackClip(self) -> bool:"""EnableBackClip { get; set; } -> bool"""
    @property
    def EnableFrontClip(self) -> bool:"""EnableFrontClip { get; set; } -> bool"""
    @property
    def EnableStereo(self) -> bool:"""EnableStereo { get; set; } -> bool"""
    @property
    def ExceededBounds(self) -> bool:"""ExceededBounds { get; } -> bool"""
    @property
    def FieldHeight(self) -> float:"""FieldHeight { get; } -> float"""
    @property
    def FieldWidth(self) -> float:"""FieldWidth { get; } -> float"""
    @property
    def FrontClip(self) -> float:"""FrontClip { get; set; } -> float"""
    @property
    def IsInteractive(self) -> bool:"""IsInteractive { get; } -> bool"""
    @property
    def IsPerspective(self) -> bool:"""IsPerspective { get; } -> bool"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def IsVisible(self) -> bool:"""IsVisible { get; } -> bool"""
    @property
    def ObjectToDeviceMatrix(self) -> _n_2_t_0:"""ObjectToDeviceMatrix { get; } -> Matrix3d"""
    @property
    def Position(self) -> _n_2_t_1:"""Position { get; } -> Point3d"""
    @property
    def ProjectionMatrix(self) -> _n_2_t_0:"""ProjectionMatrix { get; } -> Matrix3d"""
    @property
    def ScreenMatrix(self) -> _n_2_t_0:"""ScreenMatrix { get; } -> Matrix3d"""
    @property
    def StereoParameters(self) -> StereoParameters:"""StereoParameters { get; set; } -> StereoParameters"""
    @property
    def Target(self) -> _n_2_t_1:"""Target { get; } -> Point3d"""
    @property
    def UpVector(self) -> _n_2_t_3:"""UpVector { get; } -> Vector3d"""
    @property
    def ViewingMatrix(self) -> _n_2_t_0:"""ViewingMatrix { get; } -> Matrix3d"""
    @property
    def ViewportBorderProperties(self) -> ViewportBorderProperties:"""ViewportBorderProperties { get; set; } -> ViewportBorderProperties"""
    @property
    def ViewportBorderVisibility(self) -> bool:"""ViewportBorderVisibility { get; set; } -> bool"""
    @property
    def ViewportExtents(self) -> _n_1_t_2:"""ViewportExtents { get; set; } -> Extents2d"""
    @property
    def ViewportId(self) -> _n_5_t_5:"""ViewportId { get; } -> IntPtr"""
    @property
    def ViewportObjectId(self) -> _n_1_t_1:"""ViewportObjectId { get; } -> ObjectId"""
    @property
    def VisualStyle(self) -> _n_3_t_2:"""VisualStyle { get; set; } -> VisualStyle"""
    @property
    def VisualStyleId(self) -> _n_1_t_1:"""VisualStyleId { get; set; } -> ObjectId"""
    @property
    def WorldToDeviceMatrix(self) -> _n_2_t_0:"""WorldToDeviceMatrix { get; } -> Matrix3d"""
    def __init__(self, clientViewInfo: ClientViewInfo, enableLayerVisibilityPerView: bool) -> View:...
    def __init__(self) -> View:...
    def Add(self, drawable: _n_3_t_0, model: Model) -> bool:...
    def BeginInteractivity(self, frameRateInHZ: float):...
    def ClearFrozenLayers(self):...
    def Clone(self) -> View:...
    def Clone(self, cloneViewParameters: bool, cloneGeometry: bool) -> View:...
    def Dolly(self, x: float, y: float, z: float):...
    def Dolly(self, vector: _n_2_t_3):...
    def EnableDefaultLighting(self, bEnable: bool):...
    def EnableDefaultLighting(self, bEnable: bool, type: DefaultLightingType):...
    def EndInteractivity(self):...
    def Erase(self, drawable: _n_3_t_0) -> bool:...
    def EraseAll(self):...
    def ExtentsInView(self, minPoint: _n_2_t_1, maxPoint: _n_2_t_1) -> bool:...
    def Flush(self):...
    def FreezeLayer(self, layerId: _n_5_t_5):...
    def FreezeLayer(self, layerId: int):...
    def GetModel(self, drw: _n_3_t_0) -> Model:...
    def GetModelList(self) -> _n_5_t_2[Model]:...
    def GetNumPixelsInUnitSquare(self, givenWorldpt: _n_2_t_1) -> _n_2_t_4:...
    def GetNumPixelsInUnitSquare(self, givenWorldpt: _n_2_t_1, includePerspective: bool) -> _n_2_t_4:...
    def GetSnapshot(self, rectangle: _n_7_t_2) -> _n_7_t_1:...
    def Hide(self):...
    def Invalidate(self, rect: _n_7_t_2):...
    def Invalidate(self):...
    def InvalidateCachedViewportGeometry(self):...
    def Orbit(self, x: float, y: float):...
    def Pan(self, x: float, y: float):...
    def PointInView(self, point: _n_2_t_1) -> bool:...
    def RemoveViewportClipRegion(self):...
    def RenderToImage(self) -> _n_7_t_1:...
    def RenderToImage(self, settings: _n_3_t_0, rectScreen: _n_7_t_2) -> _n_7_t_1:...
    def Roll(self, angle: float):...
    def SetView(self, position: _n_2_t_1, target: _n_2_t_1, upVector: _n_2_t_3, fieldWidth: float, fieldHeight: float):...
    def SetView(self, position: _n_2_t_1, target: _n_2_t_1, upVector: _n_2_t_3, fieldWidth: float, fieldHeight: float, projection: Projection):...
    def SetViewportClipRegion(self, contours: int, counts: _n_5_t_2[int], points: _n_5_t_2[_n_7_t_4]):...
    def Show(self):...
    def ThawLayer(self, layerId: _n_5_t_5):...
    def ThawLayer(self, layerId: int):...
    def Update(self):...
    def Zoom(self, factor: float):...
    def ZoomExtents(self, minPoint: _n_2_t_1, maxPoint: _n_2_t_1):...
    def ZoomWindow(self, lowerLeft: _n_2_t_4, upperRight: _n_2_t_4):...
class ViewEventArgs(_n_5_t_7):
    @property
    def View(self) -> View:"""View { get; } -> View"""
    def __init__(self) -> ViewEventArgs:...
class ViewportBorderProperties(_n_5_t_0):
    @property
    def Color(self) -> _n_7_t_0:"""Color { get; } -> Color"""
    @property
    def Weight(self) -> int:"""Weight { get; } -> int"""
    def __init__(self, color: _n_7_t_0, weight: int) -> ViewportBorderProperties:...
class ViewToBeDestroyedEventHandler(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> ViewToBeDestroyedEventHandler:...
    def BeginInvoke(self, sender: object, e: ViewEventArgs, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, sender: object, e: ViewEventArgs):...
class ViewToBeUpdatedEventHandler(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> ViewToBeUpdatedEventHandler:...
    def BeginInvoke(self, sender: object, e: ViewUpdateEventArgs, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, sender: object, e: ViewUpdateEventArgs):...
class ViewUpdateEventArgs(_n_5_t_7):
    @property
    def View(self) -> View:"""View { get; } -> View"""
    @property
    def viewUpdateFlags(self) -> ViewUpdateFlags:"""viewUpdateFlags { get; } -> ViewUpdateFlags"""
    def __init__(self) -> ViewUpdateEventArgs:...
class ViewUpdateFlags(_n_5_t_9, _n_5_t_10, _n_5_t_11, _n_5_t_12):
    CameraChanged: int
    value__: int
class ViewWasCreatedEventHandler(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> ViewWasCreatedEventHandler:...
    def BeginInvoke(self, sender: object, e: ViewEventArgs, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, sender: object, e: ViewEventArgs):...
class ViewWasUpdatedEventHandler(_n_5_t_3, _n_5_t_4, _n_8_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_5) -> ViewWasUpdatedEventHandler:...
    def BeginInvoke(self, sender: object, e: ViewUpdateEventArgs, callback: _n_5_t_8, obj: object) -> _n_5_t_6:...
    def EndInvoke(self, result: _n_5_t_6):...
    def Invoke(self, sender: object, e: ViewUpdateEventArgs):...
