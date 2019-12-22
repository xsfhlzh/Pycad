import __clrclasses__.System.Runtime.DesignerServices as DesignerServices
import __clrclasses__.System.Runtime.ConstrainedExecution as ConstrainedExecution
import __clrclasses__.System.Runtime.Serialization as Serialization
import __clrclasses__.System.Runtime.ExceptionServices as ExceptionServices
import __clrclasses__.System.Runtime.Remoting as Remoting
import __clrclasses__.System.Runtime.InteropServices as InteropServices
import __clrclasses__.System.Runtime.Hosting as Hosting
import __clrclasses__.System.Runtime.CompilerServices as CompilerServices
import __clrclasses__.System.Runtime.Versioning as Versioning
from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Enum as _n_0_t_1
from __clrclasses__.System import IComparable as _n_0_t_2
from __clrclasses__.System import IFormattable as _n_0_t_3
from __clrclasses__.System import IConvertible as _n_0_t_4
from __clrclasses__.System import IDisposable as _n_0_t_5
from __clrclasses__.System.Runtime.ConstrainedExecution import CriticalFinalizerObject as _n_1_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_2_t_0
import typing
class AssemblyTargetedPatchBandAttribute(_n_0_t_0, _n_2_t_0):
    @property
    def TargetedPatchBand(self) -> str:"""TargetedPatchBand { get; } -> str"""
    def __init__(self, targetedPatchBand: str) -> AssemblyTargetedPatchBandAttribute:...
class GCLargeObjectHeapCompactionMode(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    CompactOnce: int
    Default: int
    value__: int
class GCLatencyMode(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    Batch: int
    Interactive: int
    LowLatency: int
    NoGCRegion: int
    SustainedLowLatency: int
    value__: int
class GCSettings(object):
    @property
    def IsServerGC(self) -> bool:"""IsServerGC { get; } -> bool"""
    @property
    def LargeObjectHeapCompactionMode(self) -> GCLargeObjectHeapCompactionMode:"""LargeObjectHeapCompactionMode { get; set; } -> GCLargeObjectHeapCompactionMode"""
    @property
    def LatencyMode(self) -> GCLatencyMode:"""LatencyMode { get; set; } -> GCLatencyMode"""
class MemoryFailPoint(_n_1_t_0, _n_0_t_5):
    def __init__(self, sizeInMegabytes: int) -> MemoryFailPoint:...
class ProfileOptimization(object):
    @staticmethod
    def SetProfileRoot(directoryPath: str):...
    @staticmethod
    def StartProfile(profile: str):...
class TargetedPatchingOptOutAttribute(_n_0_t_0, _n_2_t_0):
    @property
    def Reason(self) -> str:"""Reason { get; } -> str"""
    def __init__(self, reason: str) -> TargetedPatchingOptOutAttribute:...
