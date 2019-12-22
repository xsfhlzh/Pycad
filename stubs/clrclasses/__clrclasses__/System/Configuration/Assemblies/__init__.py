from __clrclasses__.System import ValueType as _n_0_t_0
from __clrclasses__.System import ICloneable as _n_0_t_1
from __clrclasses__.System import Byte as _n_0_t_2
from __clrclasses__.System import Array as _n_0_t_3
from __clrclasses__.System import Enum as _n_0_t_4
from __clrclasses__.System import IComparable as _n_0_t_5
from __clrclasses__.System import IFormattable as _n_0_t_6
from __clrclasses__.System import IConvertible as _n_0_t_7
import typing
class AssemblyHash(_n_0_t_0, _n_0_t_1):
    Empty: int
    @property
    def Algorithm(self) -> AssemblyHashAlgorithm:"""Algorithm { get; set; } -> AssemblyHashAlgorithm"""
    def __init__(self, algorithm: AssemblyHashAlgorithm, value: _n_0_t_3[_n_0_t_2]) -> AssemblyHash:...
    def __init__(self, value: _n_0_t_3[_n_0_t_2]) -> AssemblyHash:...
    def GetValue(self) -> _n_0_t_3[_n_0_t_2]:...
    def SetValue(self, value: _n_0_t_3[_n_0_t_2]):...
class AssemblyHashAlgorithm(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    MD5: int
    _None: int
    SHA1: int
    SHA256: int
    SHA384: int
    SHA512: int
    value__: int
class AssemblyVersionCompatibility(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    SameDomain: int
    SameMachine: int
    SameProcess: int
    value__: int
