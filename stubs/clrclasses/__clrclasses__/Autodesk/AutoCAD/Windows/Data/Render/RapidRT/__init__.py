from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import Document as _n_0_t_0
from __clrclasses__.System import IDisposable as _n_1_t_0
from __clrclasses__.System import Nullable as _n_1_t_1
from __clrclasses__.System import Enum as _n_1_t_2
from __clrclasses__.System import IComparable as _n_1_t_3
from __clrclasses__.System import IFormattable as _n_1_t_4
from __clrclasses__.System import IConvertible as _n_1_t_5
from __clrclasses__.System.Collections.Generic import Dictionary as _n_2_t_0
from __clrclasses__.System.Collections.ObjectModel import ObservableCollection as _n_3_t_0
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_4_t_0
from __clrclasses__.System.Drawing import Bitmap as _n_5_t_0
import typing
class RenderData(_n_4_t_0, _n_1_t_0):
    @property
    def AbortFlag(self) -> bool:"""AbortFlag { get; set; } -> bool"""
    @property
    def CurrentTileIndex(self) -> int:"""CurrentTileIndex { get; set; } -> int"""
    @property
    def IsIndeterminate(self) -> bool:"""IsIndeterminate { get; } -> bool"""
    @property
    def IsRendering(self) -> bool:"""IsRendering { get; } -> bool"""
    @property
    def IsRenderOK(self) -> bool:"""IsRenderOK { get; set; } -> bool"""
    @property
    def IsViewportRender(self) -> bool:"""IsViewportRender { get; } -> bool"""
    @property
    def JobIndex(self) -> _n_1_t_1[int]:"""JobIndex { get; set; } -> Nullable"""
    @property
    def LevelProgress(self) -> float:"""LevelProgress { get; set; } -> float"""
    @property
    def OutputFileName(self) -> str:"""OutputFileName { get; set; } -> str"""
    @property
    def OutputImageFormat(self) -> str:"""OutputImageFormat { get; set; } -> str"""
    @property
    def OutputResolution(self) -> str:"""OutputResolution { get; set; } -> str"""
    @property
    def OutputSize(self) -> str:"""OutputSize { get; } -> str"""
    @property
    def OutputView(self) -> str:"""OutputView { get; } -> str"""
    @property
    def OverallProgress(self) -> float:"""OverallProgress { get; set; } -> float"""
    @property
    def OwningDocument(self) -> _n_0_t_0:"""OwningDocument { get; } -> Document"""
    @property
    def RenderLevel(self) -> int:"""RenderLevel { get; set; } -> int"""
    @property
    def RenderPreset(self) -> str:"""RenderPreset { get; } -> str"""
    @property
    def RenderStatistics(self) -> str:"""RenderStatistics { get; set; } -> str"""
    @property
    def RenderTileImage(self) -> RenderImage:"""RenderTileImage { get; set; } -> RenderImage"""
    @property
    def RenderTime(self) -> int:"""RenderTime { get; set; } -> int"""
    def __init__(self, A_0: _n_0_t_0) -> RenderData:...
    def ReRender(self):...
class RenderDataSet(_n_4_t_0, _n_1_t_0):
    @property
    def CurrentRenderData(self) -> RenderData:"""CurrentRenderData { get; set; } -> RenderData"""
    @property
    def Reactor(self) -> RenderDataReactorImp:"""Reactor { get; set; } -> RenderDataReactorImp"""
    @property
    def RenderJobs(self) -> _n_3_t_0[RenderData]:"""RenderJobs { get; set; } -> ObservableCollection"""
    def __init__(self) -> RenderDataSet:...
class RenderEngine(_n_4_t_0, _n_1_t_0):
    @property
    def CurrentOutputFile(self) -> str:"""CurrentOutputFile { get; set; } -> str"""
    @property
    def CurrentOutputSize(self) -> str:"""CurrentOutputSize { get; set; } -> str"""
    @property
    def CurrentRenderData(self) -> RenderData:"""CurrentRenderData { get; } -> RenderData"""
    @property
    def CurrentRenderEnvironment(self) -> RenderEnvironment:"""CurrentRenderEnvironment { get; } -> RenderEnvironment"""
    @property
    def CurrentRenderExposure(self) -> RenderExposure:"""CurrentRenderExposure { get; } -> RenderExposure"""
    @property
    def IsRendering(self) -> bool:"""IsRendering { get; } -> bool"""
    @property
    def IsViewportChanging(self) -> bool:"""IsViewportChanging { get; set; } -> bool"""
    @property
    def OutputSaveEnabled(self) -> bool:"""OutputSaveEnabled { get; set; } -> bool"""
    @property
    def RenderDataMap(self) -> _n_2_t_0[_n_0_t_0, RenderDataSet]:"""RenderDataMap { get; } -> Dictionary"""
    @property
    def RenderDestination(self) -> int:"""RenderDestination { get; set; } -> int"""
    @property
    def SkipGlobalUpdate(self) -> bool:"""SkipGlobalUpdate { get; set; } -> bool"""
    def __init__(self) -> RenderEngine:...
    def MakeRenderJobSettingsCurrent(self, doc: _n_0_t_0, jobIndex: int):...
    def NotifyRenderEnd(self, doc: _n_0_t_0):...
    def NotifyRenderStart(self, doc: _n_0_t_0, jobIndex: int):...
    def RegisterDocument(self, doc: _n_0_t_0):...
    def UnregisterDocument(self, doc: _n_0_t_0):...
class RenderEnvironment(_n_4_t_0, _n_1_t_0):
    @property
    def Brightness(self) -> _n_1_t_1[float]:"""Brightness { get; set; } -> Nullable"""
    @property
    def DisplayImage(self) -> bool:"""DisplayImage { get; set; } -> bool"""
    @property
    def Enable(self) -> bool:"""Enable { get; set; } -> bool"""
    @property
    def Exposure(self) -> _n_1_t_1[float]:"""Exposure { get; set; } -> Nullable"""
    @property
    def IBLImageName(self) -> str:"""IBLImageName { get; set; } -> str"""
    @property
    def Rotation(self) -> float:"""Rotation { get; set; } -> float"""
    @property
    def WhitePoint(self) -> _n_1_t_1[float]:"""WhitePoint { get; set; } -> Nullable"""
    def __init__(self) -> RenderEnvironment:...
    def SuppressDatabaseUpdate(self, newValue: bool):...
class RenderExposure(_n_4_t_0, _n_1_t_0):
    @property
    def Active(self) -> bool:"""Active { get; set; } -> bool"""
    @property
    def Exposure(self) -> float:"""Exposure { get; set; } -> float"""
    @property
    def IBLActive(self) -> bool:"""IBLActive { get; set; } -> bool"""
    @property
    def Type(self) -> RenderExposure.ExposureType:"""Type { get; } -> RenderExposure.ExposureType"""
    @property
    def WhitePoint(self) -> float:"""WhitePoint { get; set; } -> float"""
    def __init__(self) -> RenderExposure:...
    def InvalidateUI(self):...
    def ResetDefault(self):...
    class ExposureType(_n_1_t_2, _n_1_t_3, _n_1_t_4, _n_1_t_5):
        Photographic: int
        value__: int
class RenderImage(_n_1_t_0):
    @property
    def Height(self) -> int:"""Height { get; set; } -> int"""
    @property
    def Image(self) -> _n_5_t_0:"""Image { get; set; } -> Bitmap"""
    @property
    def Left(self) -> int:"""Left { get; set; } -> int"""
    @property
    def Top(self) -> int:"""Top { get; set; } -> int"""
    @property
    def Width(self) -> int:"""Width { get; set; } -> int"""
    def __init__(self) -> RenderImage:...
