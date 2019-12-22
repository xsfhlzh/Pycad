from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Enum as _n_0_t_1
from __clrclasses__.System import IComparable as _n_0_t_2
from __clrclasses__.System import IFormattable as _n_0_t_3
from __clrclasses__.System import IConvertible as _n_0_t_4
from __clrclasses__.System import IEquatable as _n_0_t_5
from __clrclasses__.System import Version as _n_0_t_6
from __clrclasses__.System import Type as _n_0_t_7
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
import typing
class CompatibilitySwitch(object):
    @staticmethod
    def GetValue(compatibilitySwitchName: str) -> str:...
    @staticmethod
    def IsEnabled(compatibilitySwitchName: str) -> bool:...
class ComponentGuaranteesAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def Guarantees(self) -> ComponentGuaranteesOptions:"""Guarantees { get; } -> ComponentGuaranteesOptions"""
    def __init__(self, guarantees: ComponentGuaranteesOptions) -> ComponentGuaranteesAttribute:...
class ComponentGuaranteesOptions(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    Exchange: int
    _None: int
    SideBySide: int
    Stable: int
    value__: int
class FrameworkName(_n_0_t_5[FrameworkName]):
    @property
    def FullName(self) -> str:"""FullName { get; } -> str"""
    @property
    def Identifier(self) -> str:"""Identifier { get; } -> str"""
    @property
    def Profile(self) -> str:"""Profile { get; } -> str"""
    @property
    def Version(self) -> _n_0_t_6:"""Version { get; } -> Version"""
    def __init__(self, frameworkName: str) -> FrameworkName:...
    def __init__(self, identifier: str, version: _n_0_t_6, profile: str) -> FrameworkName:...
    def __init__(self, identifier: str, version: _n_0_t_6) -> FrameworkName:...
class ResourceConsumptionAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def ConsumptionScope(self) -> ResourceScope:"""ConsumptionScope { get; } -> ResourceScope"""
    @property
    def ResourceScope(self) -> ResourceScope:"""ResourceScope { get; } -> ResourceScope"""
    def __init__(self, resourceScope: ResourceScope) -> ResourceConsumptionAttribute:...
    def __init__(self, resourceScope: ResourceScope, consumptionScope: ResourceScope) -> ResourceConsumptionAttribute:...
class ResourceExposureAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def ResourceExposureLevel(self) -> ResourceScope:"""ResourceExposureLevel { get; } -> ResourceScope"""
    def __init__(self, exposureLevel: ResourceScope) -> ResourceExposureAttribute:...
class ResourceScope(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    AppDomain: int
    Assembly: int
    Library: int
    Machine: int
    _None: int
    Private: int
    Process: int
    value__: int
class TargetFrameworkAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def FrameworkDisplayName(self) -> str:"""FrameworkDisplayName { get; set; } -> str"""
    @property
    def FrameworkName(self) -> str:"""FrameworkName { get; } -> str"""
    def __init__(self, frameworkName: str) -> TargetFrameworkAttribute:...
class VersioningHelper(object):
    @staticmethod
    def MakeVersionSafeName(name: str, _from: ResourceScope, to: ResourceScope, type: _n_0_t_7) -> str:...
    @staticmethod
    def MakeVersionSafeName(name: str, _from: ResourceScope, to: ResourceScope) -> str:...
