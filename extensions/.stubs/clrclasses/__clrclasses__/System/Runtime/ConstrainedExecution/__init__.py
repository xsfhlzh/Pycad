from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import Attribute as _n_0_t_4
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
import typing
class Cer(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    MayFail: int
    _None: int
    Success: int
    value__: int
class Consistency(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    MayCorruptAppDomain: int
    MayCorruptInstance: int
    MayCorruptProcess: int
    value__: int
    WillNotCorruptState: int
class CriticalFinalizerObject(object):
    pass
class PrePrepareMethodAttribute(_n_0_t_4, _n_1_t_0):
    def __init__(self) -> PrePrepareMethodAttribute:...
class ReliabilityContractAttribute(_n_0_t_4, _n_1_t_0):
    @property
    def Cer(self) -> Cer:"""Cer { get; } -> Cer"""
    @property
    def ConsistencyGuarantee(self) -> Consistency:"""ConsistencyGuarantee { get; } -> Consistency"""
    def __init__(self, consistencyGuarantee: Consistency, cer: Cer) -> ReliabilityContractAttribute:...
