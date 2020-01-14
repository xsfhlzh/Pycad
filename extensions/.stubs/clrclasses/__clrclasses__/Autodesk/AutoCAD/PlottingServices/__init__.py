from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import PlotSettings as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2d as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Tolerance as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_2_t_1
from __clrclasses__.System import Enum as _n_3_t_0
from __clrclasses__.System import IComparable as _n_3_t_1
from __clrclasses__.System import IFormattable as _n_3_t_2
from __clrclasses__.System import IConvertible as _n_3_t_3
from __clrclasses__.System import EventArgs as _n_3_t_4
from __clrclasses__.System import MulticastDelegate as _n_3_t_5
from __clrclasses__.System import ICloneable as _n_3_t_6
from __clrclasses__.System import IntPtr as _n_3_t_7
from __clrclasses__.System import IAsyncResult as _n_3_t_8
from __clrclasses__.System import AsyncCallback as _n_3_t_9
from __clrclasses__.System import IDisposable as _n_3_t_10
from __clrclasses__.System import ValueType as _n_3_t_11
from __clrclasses__.System.Collections import ICollection as _n_4_t_0
from __clrclasses__.System.Collections.Specialized import StringCollection as _n_5_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_6_t_0
import typing
class AppPlotStatus(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    DwfFilePlotted: int
    NoPlotYet: int
    PlotHadErrors: int
    PlotHadSystemError: int
    PlotStart: int
    PlotSuccessful: int
    PlottingMessage: int
    value__: int
    ViewPlotLog: int
class BeginDocumentEventArgs(_n_3_t_4):
    @property
    def Copies(self) -> int:"""Copies { get; } -> int"""
    @property
    def DocumentName(self) -> str:"""DocumentName { get; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def PlotInfo(self) -> PlotInfo:"""PlotInfo { get; } -> PlotInfo"""
    @property
    def PlotToFile(self) -> bool:"""PlotToFile { get; } -> bool"""
    def __init__(self, plotInfo: PlotInfo, documentName: str, copies: int, plotToFile: bool, fileName: str) -> BeginDocumentEventArgs:...
class BeginDocumentEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> BeginDocumentEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginDocumentEventArgs, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: BeginDocumentEventArgs):...
class BeginPageEventArgs(_n_3_t_4):
    @property
    def LastPage(self) -> bool:"""LastPage { get; } -> bool"""
    @property
    def PlotInfo(self) -> PlotInfo:"""PlotInfo { get; } -> PlotInfo"""
    @property
    def PlotPageInfo(self) -> PlotPageInfo:"""PlotPageInfo { get; } -> PlotPageInfo"""
    def __init__(self, plotPageInfo: PlotPageInfo, plotInfo: PlotInfo, lastPage: bool) -> BeginPageEventArgs:...
class BeginPageEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> BeginPageEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginPageEventArgs, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: BeginPageEventArgs):...
class BeginPlotEventArgs(_n_3_t_4):
    @property
    def PlotProgress(self) -> PlotProgress:"""PlotProgress { get; } -> PlotProgress"""
    @property
    def PlotType(self) -> PlotType:"""PlotType { get; } -> PlotType"""
    def __init__(self, progress: PlotProgress, plotType: PlotType) -> BeginPlotEventArgs:...
class BeginPlotEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> BeginPlotEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginPlotEventArgs, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: BeginPlotEventArgs):...
class CustomSizeResults(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    DeviceLoadFailed: int
    Exception: int
    MustCreatePC3: int
    PC3DirReadOnly: int
    PC3FileReadOnly: int
    PmpDirMissing: int
    PmpDirReadOnly: int
    PmpFileReadOnly: int
    Possible: int
    RotationRequired: int
    SizeTooBig: int
    UnknownErrPC3File: int
    UnknownErrPmpDir: int
    UnknownErrPmpFile: int
    value__: int
    WidthAndHeightMustBePositive: int
class DeviceType(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    OneOffConfig: int
    PC3File: int
    SystemPrinter: int
    Uninitialized: int
    value__: int
class DsdData(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def CategoryName(self) -> str:"""CategoryName { get; set; } -> str"""
    @property
    def DestinationName(self) -> str:"""DestinationName { get; set; } -> str"""
    @property
    def Dwf3dOptions(self) -> Dwf3dOptions:"""Dwf3dOptions { get; } -> Dwf3dOptions"""
    @property
    def IsHomogeneous(self) -> bool:"""IsHomogeneous { get; set; } -> bool"""
    @property
    def IsSheetSet(self) -> bool:"""IsSheetSet { get; set; } -> bool"""
    @property
    def LogFilePath(self) -> str:"""LogFilePath { get; set; } -> str"""
    @property
    def MajorVersion(self) -> int:"""MajorVersion { get; set; } -> int"""
    @property
    def MinorVersion(self) -> int:"""MinorVersion { get; set; } -> int"""
    @property
    def NoOfCopies(self) -> int:"""NoOfCopies { get; set; } -> int"""
    @property
    def Password(self) -> str:"""Password { get; set; } -> str"""
    @property
    def PlotStampOn(self) -> bool:"""PlotStampOn { get; set; } -> bool"""
    @property
    def ProjectPath(self) -> str:"""ProjectPath { get; set; } -> str"""
    @property
    def PromptForDwfName(self) -> bool:"""PromptForDwfName { get; set; } -> bool"""
    @property
    def SelectionSetName(self) -> str:"""SelectionSetName { get; set; } -> str"""
    @property
    def SheetSetName(self) -> str:"""SheetSetName { get; set; } -> str"""
    @property
    def SheetType(self) -> SheetType:"""SheetType { get; set; } -> SheetType"""
    @property
    def UnrecognizedDataSectionNames(self) -> _n_5_t_0:"""UnrecognizedDataSectionNames { get; } -> StringCollection"""
    @property
    def UnrecognizedDataSections(self) -> _n_5_t_0:"""UnrecognizedDataSections { get; } -> StringCollection"""
    def __init__(self) -> DsdData:...
    def Copy(self) -> DsdData:...
    def GetDsdEntryCollection(self) -> DsdEntryCollection:...
    def ReadDsd(self, fileName: str):...
    def SetDsdEntryCollection(self, entries: DsdEntryCollection):...
    def SetUnrecognizedData(self, sectionName: str, sectionData: str):...
    def SetUnrecognizedData(self, sectionNames: _n_5_t_0, sectionData: _n_5_t_0):...
    def WriteDsd(self, fileName: str):...
class DsdEntry(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def DwgName(self) -> str:"""DwgName { get; set; } -> str"""
    @property
    def Layout(self) -> str:"""Layout { get; set; } -> str"""
    @property
    def Nps(self) -> str:"""Nps { get; set; } -> str"""
    @property
    def NpsSourceDwg(self) -> str:"""NpsSourceDwg { get; set; } -> str"""
    @property
    def OriginalSheetPath(self) -> str:"""OriginalSheetPath { get; } -> str"""
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    def __init__(self) -> DsdEntry:...
    def Copy(self) -> DsdEntry:...
class DsdEntryCollection(_n_2_t_1, _n_3_t_10, _n_4_t_0, typing.Iterable[DsdEntry]):
    @property
    def Item(self) -> DsdEntry:"""Item { get; set; } -> DsdEntry"""
    def __init__(self) -> DsdEntryCollection:...
    def Add(self, value: DsdEntry) -> int:...
    def Clear(self):...
    def Insert(self, index: int, value: DsdEntry):...
    def RemoveAt(self, index: int):...
class Dwf3dOptions(object):
    @property
    def GroupByXrefHierarchy(self) -> bool:"""GroupByXrefHierarchy { get; set; } -> bool"""
    @property
    def PublishWithMaterials(self) -> bool:"""PublishWithMaterials { get; set; } -> bool"""
class EndDocumentEventArgs(_n_3_t_4):
    @property
    def Status(self) -> PlotCancelStatus:"""Status { get; } -> PlotCancelStatus"""
    def __init__(self, status: PlotCancelStatus) -> EndDocumentEventArgs:...
class EndDocumentEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> EndDocumentEventHandler:...
    def BeginInvoke(self, sender: object, e: EndDocumentEventArgs, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: EndDocumentEventArgs):...
class EndPageEventArgs(_n_3_t_4):
    @property
    def Status(self) -> SheetCancelStatus:"""Status { get; } -> SheetCancelStatus"""
    def __init__(self, status: SheetCancelStatus) -> EndPageEventArgs:...
class EndPageEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> EndPageEventHandler:...
    def BeginInvoke(self, sender: object, e: EndPageEventArgs, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: EndPageEventArgs):...
class EndPlotEventArgs(_n_3_t_4):
    @property
    def Status(self) -> PlotCancelStatus:"""Status { get; } -> PlotCancelStatus"""
    def __init__(self, status: PlotCancelStatus) -> EndPlotEventArgs:...
class EndPlotEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> EndPlotEventHandler:...
    def BeginInvoke(self, sender: object, e: EndPlotEventArgs, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: EndPlotEventArgs):...
class HostAppServices(object):
    @property
    def PlotLogger(self) -> PlotLogger:"""PlotLogger { get; } -> PlotLogger"""
    @staticmethod
    def UpdatePlotJobStatus(status: AppPlotStatus, message: str):...
class MatchingPolicy(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    MatchDisabled: int
    MatchEnabled: int
    MatchEnabledCustom: int
    MatchEnabledTemporaryCustom: int
    value__: int
class MediaBounds(_n_3_t_11):
    @property
    def LowerLeftPrintableArea(self) -> _n_1_t_0:"""LowerLeftPrintableArea { get; set; } -> Point2d"""
    @property
    def PageSize(self) -> _n_1_t_0:"""PageSize { get; set; } -> Point2d"""
    @property
    def UpperRightPrintableArea(self) -> _n_1_t_0:"""UpperRightPrintableArea { get; set; } -> Point2d"""
    def __init__(self, pageSize: _n_1_t_0, lowerLeftPrintableArea: _n_1_t_0, upperRightPrintableArea: _n_1_t_0) -> MediaBounds:...
    def IsEqualTo(self, a: MediaBounds, tolerance: _n_1_t_1) -> bool:...
    def IsEqualTo(self, a: MediaBounds) -> bool:...
class MergeStatus(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    CanonicalMediaName: int
    CurrentStyleSheet: int
    DrawViewportsFirst: int
    NoChanges: int
    PlotCentered: int
    PlotConfigurationName: int
    PlotHidden: int
    PlotOrigin: int
    PlotPaperMargins: int
    PlotPaperSize: int
    PlotPaperUnits: int
    PlotPlotStyles: int
    PlotRotation: int
    PlotTransparency: int
    PlotType: int
    PlotViewName: int
    PlotViewportBorders: int
    PlotWindowArea: int
    PrintLineWeights: int
    Scale: int
    ScaleLineWeights: int
    ShadePlot: int
    ShadePlotCustomDpi: int
    ShadePlotResLevel: int
    ShowPlotStyles: int
    value__: int
class PageCancelledEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> PageCancelledEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_4, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: _n_3_t_4):...
class PlotCancelledEventHandler(_n_3_t_5, _n_3_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_7) -> PlotCancelledEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_4, callback: _n_3_t_9, obj: object) -> _n_3_t_8:...
    def EndInvoke(self, result: _n_3_t_8):...
    def Invoke(self, sender: object, e: _n_3_t_4):...
class PlotCancelStatus(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    CanceledByCaller: int
    CanceledByCancelAllButton: int
    Continue: int
    value__: int
class PlotConfig(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def CanonicalMediaNames(self) -> _n_5_t_0:"""CanonicalMediaNames { get; } -> StringCollection"""
    @property
    def Comment(self) -> str:"""Comment { get; } -> str"""
    @property
    def DefaultFileExtension(self) -> str:"""DefaultFileExtension { get; } -> str"""
    @property
    def DeviceName(self) -> str:"""DeviceName { get; } -> str"""
    @property
    def DeviceType(self) -> int:"""DeviceType { get; } -> int"""
    @property
    def DriverName(self) -> str:"""DriverName { get; } -> str"""
    @property
    def FullPath(self) -> str:"""FullPath { get; } -> str"""
    @property
    def IsPlotToFile(self) -> bool:"""IsPlotToFile { get; set; } -> bool"""
    @property
    def LocationName(self) -> str:"""LocationName { get; } -> str"""
    @property
    def MaximumDeviceDotsPerInch(self) -> int:"""MaximumDeviceDotsPerInch { get; } -> int"""
    @property
    def PlotToFileCapability(self) -> PlotToFileCapability:"""PlotToFileCapability { get; } -> PlotToFileCapability"""
    @property
    def PortName(self) -> str:"""PortName { get; } -> str"""
    @property
    def ServerName(self) -> str:"""ServerName { get; } -> str"""
    @property
    def TagLine(self) -> str:"""TagLine { get; } -> str"""
    def GetLocalMediaName(self, canonicalMediaName: str) -> str:...
    def GetMediaBounds(self, canonicalMediaName: str) -> MediaBounds:...
    def RefreshMediaNameList(self):...
    def SaveToPC3(self, name: str):...
class PlotConfigInfo(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def DeviceName(self) -> str:"""DeviceName { get; set; } -> str"""
    @property
    def DeviceType(self) -> DeviceType:"""DeviceType { get; set; } -> DeviceType"""
    @property
    def FullPath(self) -> str:"""FullPath { get; set; } -> str"""
    def __init__(self) -> PlotConfigInfo:...
class PlotConfigInfoCollection(_n_2_t_1, _n_3_t_10, _n_4_t_0, typing.Iterable[PlotConfigInfo]):
    @property
    def Item(self) -> PlotConfigInfo:"""Item { get; } -> PlotConfigInfo"""
class PlotConfigManager(object):
    @property
    def ColorDependentPlotStyles(self) -> _n_5_t_0:"""ColorDependentPlotStyles { get; } -> StringCollection"""
    @property
    def CurrentConfig(self) -> PlotConfig:"""CurrentConfig { get; } -> PlotConfig"""
    @property
    def Devices(self) -> PlotConfigInfoCollection:"""Devices { get; } -> PlotConfigInfoCollection"""
    @property
    def NamedPlotStyles(self) -> _n_5_t_0:"""NamedPlotStyles { get; } -> StringCollection"""
    @property
    def StdConfigNames(self) -> str:"""StdConfigNames { get; } -> str"""
    @staticmethod
    def RefreshList(refreshCode: RefreshCode):...
    @staticmethod
    def SetCurrentConfig(deviceName: str) -> PlotConfig:...
class PlotEngine(_n_2_t_1, _n_3_t_10):
    @property
    def IsBackgroundPackaging(self) -> bool:"""IsBackgroundPackaging { get; } -> bool"""
    def BeginDocument(self, plotInfo: PlotInfo, documentName: str, parameters: object, copies: int, plotToFile: bool, fileName: str):...
    def BeginGenerateGraphics(self, parameters: object):...
    def BeginPage(self, pageInfo: PlotPageInfo, plotInfo: PlotInfo, lastPage: bool, parameters: object):...
    def BeginPlot(self, plotProgress: PlotProgress, parameters: object):...
    def Destroy(self):...
    def EndDocument(self, parameters: object):...
    def EndGenerateGraphics(self, parameters: object):...
    def EndPage(self, parameters: object):...
    def EndPlot(self, parameters: object):...
class PlotFactory(object):
    @property
    def ProcessPlotState(self) -> ProcessPlotState:"""ProcessPlotState { get; } -> ProcessPlotState"""
    @staticmethod
    def CreatePreviewEngine(previewFlags: int) -> PlotEngine:...
    @staticmethod
    def CreatePublishEngine() -> PlotEngine:...
class PlotInfo(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def DeviceOverride(self) -> PlotConfig:"""DeviceOverride { get; set; } -> PlotConfig"""
    @property
    def IsValidated(self) -> bool:"""IsValidated { get; } -> bool"""
    @property
    def Layout(self) -> _n_0_t_0:"""Layout { get; set; } -> ObjectId"""
    @property
    def MergeStatus(self) -> int:"""MergeStatus { get; } -> int"""
    @property
    def OverrideSettings(self) -> _n_0_t_1:"""OverrideSettings { get; set; } -> PlotSettings"""
    @property
    def ValidatedConfig(self) -> PlotConfig:"""ValidatedConfig { get; set; } -> PlotConfig"""
    @property
    def ValidatedSettings(self) -> _n_0_t_1:"""ValidatedSettings { get; set; } -> PlotSettings"""
    def __init__(self) -> PlotInfo:...
    def IsCompatibleDocument(self, info: PlotInfo) -> bool:...
class PlotInfoValidator(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def DimensionalWeight(self) -> int:"""DimensionalWeight { get; set; } -> int"""
    @property
    def MediaBoundsWeight(self) -> int:"""MediaBoundsWeight { get; set; } -> int"""
    @property
    def MediaGroupWeight(self) -> int:"""MediaGroupWeight { get; set; } -> int"""
    @property
    def MediaMatchingPolicy(self) -> MatchingPolicy:"""MediaMatchingPolicy { get; set; } -> MatchingPolicy"""
    @property
    def MediaMatchingThreshold(self) -> int:"""MediaMatchingThreshold { get; set; } -> int"""
    @property
    def PrintableBoundsWeight(self) -> int:"""PrintableBoundsWeight { get; set; } -> int"""
    @property
    def SheetDimensionalWeight(self) -> int:"""SheetDimensionalWeight { get; set; } -> int"""
    @property
    def SheetMediaGroupWeight(self) -> int:"""SheetMediaGroupWeight { get; set; } -> int"""
    def __init__(self) -> PlotInfoValidator:...
    def IsCustomPossible(self, info: PlotInfo) -> int:...
    def Validate(self, info: PlotInfo):...
class PlotLogger(_n_2_t_1, _n_3_t_10):
    @property
    def ErrorHasHappenedInJob(self) -> bool:"""ErrorHasHappenedInJob { get; } -> bool"""
    @property
    def ErrorHasHappenedInSheet(self) -> bool:"""ErrorHasHappenedInSheet { get; } -> bool"""
    @property
    def WarningHasHappenedInJob(self) -> bool:"""WarningHasHappenedInJob { get; } -> bool"""
    @property
    def WarningHasHappenedInSheet(self) -> bool:"""WarningHasHappenedInSheet { get; } -> bool"""
    def EndJob(self):...
    def EndSheet(self):...
    def LogAbortRetryIgnoreError(self, message: str):...
    def LogError(self, message: str):...
    def LogInformation(self, message: str):...
    def LogMessage(self, message: str):...
    def LogSevereError(self, message: str):...
    def LogTerminalError(self, message: str):...
    def LogWarning(self, message: str):...
    def StartJob(self):...
    def StartSheet(self):...
class PlotMessageIndex(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    CancelJobButtonMessage: int
    CancelSheetButtonMessage: int
    DialogTitle: int
    MessageCanceling: int
    MessageCancelingCurrent: int
    MessageCount: int
    SheetName: int
    SheetNameToolTip: int
    SheetProgressCaption: int
    SheetSetProgressCaption: int
    Status: int
    value__: int
class PlotPageInfo(_n_2_t_0, _n_3_t_10, _n_3_t_6):
    @property
    def EntityCount(self) -> int:"""EntityCount { get; } -> int"""
    @property
    def GradientCount(self) -> int:"""GradientCount { get; } -> int"""
    @property
    def OleObjectCount(self) -> int:"""OleObjectCount { get; } -> int"""
    @property
    def RasterCount(self) -> int:"""RasterCount { get; } -> int"""
    @property
    def ShadedViewportType(self) -> int:"""ShadedViewportType { get; } -> int"""
    def __init__(self) -> PlotPageInfo:...
class PlotProgress(_n_2_t_1, _n_3_t_10):
    @property
    def IsPlotCancelled(self) -> bool:"""IsPlotCancelled { get; } -> bool"""
    @property
    def IsSheetCancelled(self) -> bool:"""IsSheetCancelled { get; } -> bool"""
    @property
    def IsVisible(self) -> bool:"""IsVisible { get; set; } -> bool"""
    @property
    def LowerPlotProgressRange(self) -> int:"""LowerPlotProgressRange { get; set; } -> int"""
    @property
    def LowerSheetProgressRange(self) -> int:"""LowerSheetProgressRange { get; set; } -> int"""
    @property
    def PlotCancelStatus(self) -> PlotCancelStatus:"""PlotCancelStatus { get; set; } -> PlotCancelStatus"""
    @property
    def PlotProgressPos(self) -> int:"""PlotProgressPos { get; set; } -> int"""
    @property
    def SheetCancelStatus(self) -> SheetCancelStatus:"""SheetCancelStatus { get; set; } -> SheetCancelStatus"""
    @property
    def SheetProgressPos(self) -> int:"""SheetProgressPos { get; set; } -> int"""
    @property
    def StatusMsgString(self) -> str:"""StatusMsgString { get; set; } -> str"""
    @property
    def UpperPlotProgressRange(self) -> int:"""UpperPlotProgressRange { get; set; } -> int"""
    @property
    def UpperSheetProgressRange(self) -> int:"""UpperSheetProgressRange { get; set; } -> int"""
    def Heartbeat(self):...
class PlotProgressDialog(PlotProgress, _n_3_t_10):
    @property
    def IsSingleSheetPlot(self) -> bool:"""IsSingleSheetPlot { get; } -> bool"""
    @property
    def PlotMsgString(self) -> str:"""PlotMsgString { get; set; } -> str"""
    def __init__(self, isPreview: bool, sheetCount: int, showCancelSheetButton: bool) -> PlotProgressDialog:...
    def Destroy(self):...
    def OnBeginPlot(self):...
    def OnBeginSheet(self):...
    def OnEndPlot(self):...
    def OnEndSheet(self):...
class PlotReactorManager(object):
    @property
    def BeginDocument(self) -> BeginDocumentEventHandler:
        """BeginDocument Event: BeginDocumentEventHandler"""
    @property
    def BeginPage(self) -> BeginPageEventHandler:
        """BeginPage Event: BeginPageEventHandler"""
    @property
    def BeginPlot(self) -> BeginPlotEventHandler:
        """BeginPlot Event: BeginPlotEventHandler"""
    @property
    def EndDocument(self) -> EndDocumentEventHandler:
        """EndDocument Event: EndDocumentEventHandler"""
    @property
    def EndPage(self) -> EndPageEventHandler:
        """EndPage Event: EndPageEventHandler"""
    @property
    def EndPlot(self) -> EndPlotEventHandler:
        """EndPlot Event: EndPlotEventHandler"""
    @property
    def PageCancelled(self) -> PageCancelledEventHandler:
        """PageCancelled Event: PageCancelledEventHandler"""
    @property
    def PlotCancelled(self) -> PlotCancelledEventHandler:
        """PlotCancelled Event: PlotCancelledEventHandler"""
    def __init__(self) -> PlotReactorManager:...
class PlotToFileCapability(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    MustPlotToFile: int
    NoPlotToFile: int
    PlotToFileAllowed: int
    value__: int
class PlotType(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    BackgroundPackaging: int
    BackgroundPlot: int
    Plot: int
    Preview: int
    value__: int
class PreviewEndPlotInfo(_n_2_t_1, _n_3_t_10):
    @property
    def Status(self) -> PreviewEndPlotStatus:"""Status { get; } -> PreviewEndPlotStatus"""
    def __init__(self) -> PreviewEndPlotInfo:...
class PreviewEndPlotStatus(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    Cancel: int
    Next: int
    Normal: int
    Plot: int
    Previous: int
    value__: int
class PreviewEngineFlags(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    NextSheet: int
    Plot: int
    PreviousSheet: int
    value__: int
class ProcessPlotState(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    BackgroundPlotting: int
    ForegroundPlotting: int
    NotPlotting: int
    value__: int
class RefreshCode(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    All: int
    RefreshDevicesList: int
    RefreshPC3DevicesList: int
    RefreshStyleList: int
    RefreshSystemDevicesList: int
    value__: int
class SheetCancelStatus(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    CanceledByCaller: int
    CanceledByCancelAllButton: int
    CanceledByCancelButton: int
    Continue: int
    value__: int
class SheetType(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    MultiDwf: int
    MultiDwfx: int
    MultiPdf: int
    OriginalDevice: int
    SingleDwf: int
    SingleDwfx: int
    SinglePdf: int
    value__: int
class StdConfiguration(_n_3_t_0, _n_3_t_1, _n_3_t_2, _n_3_t_3):
    DefaultWindowsSysPrinter: int
    Dwf6ePlot: int
    DwfEplotOptForPlotting: int
    DwfEplotOptForViewing: int
    DWFxePlot: int
    NoneDevice: int
    PublishToWebDwf: int
    PublishToWebDWFx: int
    PublishToWebJpg: int
    PublishToWebPng: int
    value__: int
