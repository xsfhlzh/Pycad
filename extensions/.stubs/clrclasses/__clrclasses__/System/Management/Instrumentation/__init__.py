from __clrclasses__.System import Exception as _n_0_t_0
from __clrclasses__.System import Type as _n_0_t_1
from __clrclasses__.System import Enum as _n_0_t_2
from __clrclasses__.System import IComparable as _n_0_t_3
from __clrclasses__.System import IFormattable as _n_0_t_4
from __clrclasses__.System import IConvertible as _n_0_t_5
from __clrclasses__.System import Attribute as _n_0_t_6
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_1_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_2_t_0
import typing
class InstanceNotFoundException(InstrumentationException, _n_2_t_0, _n_1_t_0):
    def __init__(self, message: str, innerException: _n_0_t_0) -> InstanceNotFoundException:...
    def __init__(self, message: str) -> InstanceNotFoundException:...
    def __init__(self) -> InstanceNotFoundException:...
class InstrumentationBaseException(_n_0_t_0, _n_2_t_0, _n_1_t_0):
    def __init__(self, message: str, innerException: _n_0_t_0) -> InstrumentationBaseException:...
    def __init__(self, message: str) -> InstrumentationBaseException:...
    def __init__(self) -> InstrumentationBaseException:...
class InstrumentationException(InstrumentationBaseException, _n_2_t_0, _n_1_t_0):
    def __init__(self, message: str, innerException: _n_0_t_0) -> InstrumentationException:...
    def __init__(self, innerException: _n_0_t_0) -> InstrumentationException:...
    def __init__(self, message: str) -> InstrumentationException:...
    def __init__(self) -> InstrumentationException:...
class ManagementBindAttribute(ManagementNewInstanceAttribute, _n_1_t_1):
    @property
    def Schema(self) -> _n_0_t_1:"""Schema { get; set; } -> Type"""
    def __init__(self) -> ManagementBindAttribute:...
class ManagementCommitAttribute(ManagementMemberAttribute, _n_1_t_1):
    def __init__(self) -> ManagementCommitAttribute:...
class ManagementConfigurationAttribute(ManagementMemberAttribute, _n_1_t_1):
    @property
    def Mode(self) -> ManagementConfigurationType:"""Mode { get; set; } -> ManagementConfigurationType"""
    @property
    def Schema(self) -> _n_0_t_1:"""Schema { get; set; } -> Type"""
    def __init__(self) -> ManagementConfigurationAttribute:...
class ManagementConfigurationType(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Apply: int
    OnCommit: int
    value__: int
class ManagementCreateAttribute(ManagementNewInstanceAttribute, _n_1_t_1):
    def __init__(self) -> ManagementCreateAttribute:...
class ManagementEntityAttribute(_n_0_t_6, _n_1_t_1):
    @property
    def External(self) -> bool:"""External { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Singleton(self) -> bool:"""Singleton { get; set; } -> bool"""
    def __init__(self) -> ManagementEntityAttribute:...
class ManagementEnumeratorAttribute(ManagementNewInstanceAttribute, _n_1_t_1):
    @property
    def Schema(self) -> _n_0_t_1:"""Schema { get; set; } -> Type"""
    def __init__(self) -> ManagementEnumeratorAttribute:...
class ManagementHostingModel(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Decoupled: int
    LocalService: int
    LocalSystem: int
    NetworkService: int
    value__: int
class ManagementKeyAttribute(ManagementMemberAttribute, _n_1_t_1):
    def __init__(self) -> ManagementKeyAttribute:...
class ManagementMemberAttribute(_n_0_t_6, _n_1_t_1):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
class ManagementNameAttribute(_n_0_t_6, _n_1_t_1):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, name: str) -> ManagementNameAttribute:...
class ManagementNewInstanceAttribute(ManagementMemberAttribute, _n_1_t_1):
    pass
class ManagementProbeAttribute(ManagementMemberAttribute, _n_1_t_1):
    @property
    def Schema(self) -> _n_0_t_1:"""Schema { get; set; } -> Type"""
    def __init__(self) -> ManagementProbeAttribute:...
class ManagementReferenceAttribute(_n_0_t_6, _n_1_t_1):
    @property
    def Type(self) -> str:"""Type { get; set; } -> str"""
    def __init__(self) -> ManagementReferenceAttribute:...
class ManagementRemoveAttribute(ManagementMemberAttribute, _n_1_t_1):
    @property
    def Schema(self) -> _n_0_t_1:"""Schema { get; set; } -> Type"""
    def __init__(self) -> ManagementRemoveAttribute:...
class ManagementTaskAttribute(ManagementMemberAttribute, _n_1_t_1):
    @property
    def Schema(self) -> _n_0_t_1:"""Schema { get; set; } -> Type"""
    def __init__(self) -> ManagementTaskAttribute:...
class WmiConfigurationAttribute(_n_0_t_6, _n_1_t_1):
    @property
    def HostingGroup(self) -> str:"""HostingGroup { get; set; } -> str"""
    @property
    def HostingModel(self) -> ManagementHostingModel:"""HostingModel { get; set; } -> ManagementHostingModel"""
    @property
    def IdentifyLevel(self) -> bool:"""IdentifyLevel { get; set; } -> bool"""
    @property
    def NamespaceSecurity(self) -> str:"""NamespaceSecurity { get; set; } -> str"""
    @property
    def Scope(self) -> str:"""Scope { get; } -> str"""
    @property
    def SecurityRestriction(self) -> str:"""SecurityRestriction { get; set; } -> str"""
    def __init__(self, scope: str) -> WmiConfigurationAttribute:...
