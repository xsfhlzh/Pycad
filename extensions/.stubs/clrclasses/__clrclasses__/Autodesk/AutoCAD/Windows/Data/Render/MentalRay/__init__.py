from __clrclasses__.System import IDisposable as _n_0_t_0
from __clrclasses__.System.Collections.ObjectModel import ObservableCollection as _n_1_t_0
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_1_t_1
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_2_t_0
from __clrclasses__.System.Windows.Input import ICommand as _n_3_t_0
import typing
class RenderEngine(_n_2_t_0, _n_0_t_0):
    @property
    def CurrentOutputSize(self) -> str:"""CurrentOutputSize { get; set; } -> str"""
    @property
    def CurrentRenderPresetName(self) -> str:"""CurrentRenderPresetName { get; set; } -> str"""
    @property
    def CustomOutputSizes(self) -> _n_1_t_0[str]:"""CustomOutputSizes { get; } -> ObservableCollection"""
    @property
    def IsRenderActive(self) -> bool:"""IsRenderActive { get; } -> bool"""
    @property
    def IsRenderOutputFileEnabled(self) -> bool:"""IsRenderOutputFileEnabled { get; } -> bool"""
    @property
    def IsRenderPresetDirty(self) -> bool:"""IsRenderPresetDirty { get; set; } -> bool"""
    @property
    def IsRenderToggleButtonChecked(self) -> bool:"""IsRenderToggleButtonChecked { get; set; } -> bool"""
    @property
    def IsRenderToggleButtonEnabled(self) -> bool:"""IsRenderToggleButtonEnabled { get; } -> bool"""
    @property
    def OutputFile(self) -> _n_3_t_0:"""OutputFile { get; } -> ICommand"""
    @property
    def OutputSize(self) -> _n_3_t_0:"""OutputSize { get; } -> ICommand"""
    @property
    def OverallRenderProgress(self) -> float:"""OverallRenderProgress { get; set; } -> float"""
    @property
    def PredefinedOutputSizes(self) -> _n_1_t_1[str]:"""PredefinedOutputSizes { get; } -> Collection"""
    @property
    def RenderOutputFileName(self) -> str:"""RenderOutputFileName { get; set; } -> str"""
    @property
    def RenderProgress(self) -> float:"""RenderProgress { get; set; } -> float"""
    @property
    def RenderProgressTooltip(self) -> str:"""RenderProgressTooltip { get; } -> str"""
    def __init__(self) -> RenderEngine:...
