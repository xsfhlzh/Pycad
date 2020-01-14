import __clrclasses__.System.Security.Authentication.ExtendedProtection.Configuration as Configuration
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid as _n_0_t_0
from __clrclasses__.System import IDisposable as _n_1_t_0
from __clrclasses__.System import Enum as _n_1_t_1
from __clrclasses__.System import IComparable as _n_1_t_2
from __clrclasses__.System import IFormattable as _n_1_t_3
from __clrclasses__.System import IConvertible as _n_1_t_4
from __clrclasses__.System import Byte as _n_1_t_5
from __clrclasses__.System import Array as _n_1_t_6
from __clrclasses__.System.Collections import ICollection as _n_2_t_0
from __clrclasses__.System.Collections import ReadOnlyCollectionBase as _n_2_t_1
from __clrclasses__.System.Collections import IEnumerable as _n_2_t_2
from __clrclasses__.System.ComponentModel import TypeConverter as _n_3_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_4_t_0
import typing
class ChannelBinding(_n_0_t_0, _n_1_t_0):
    @property
    def Size(self) -> int:"""Size { get; } -> int"""
class ChannelBindingKind(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    Endpoint: int
    Unique: int
    Unknown: int
    value__: int
class ExtendedProtectionPolicy(_n_4_t_0):
    @property
    def CustomChannelBinding(self) -> ChannelBinding:"""CustomChannelBinding { get; } -> ChannelBinding"""
    @property
    def CustomServiceNames(self) -> ServiceNameCollection:"""CustomServiceNames { get; } -> ServiceNameCollection"""
    @property
    def OSSupportsExtendedProtection(self) -> bool:"""OSSupportsExtendedProtection { get; } -> bool"""
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement:"""PolicyEnforcement { get; } -> PolicyEnforcement"""
    @property
    def ProtectionScenario(self) -> ProtectionScenario:"""ProtectionScenario { get; } -> ProtectionScenario"""
    def __init__(self, policyEnforcement: PolicyEnforcement) -> ExtendedProtectionPolicy:...
    def __init__(self, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding) -> ExtendedProtectionPolicy:...
    def __init__(self, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: _n_2_t_0) -> ExtendedProtectionPolicy:...
    def __init__(self, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection) -> ExtendedProtectionPolicy:...
class ExtendedProtectionPolicyTypeConverter(_n_3_t_0):
    def __init__(self) -> ExtendedProtectionPolicyTypeConverter:...
class PolicyEnforcement(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    Always: int
    Never: int
    value__: int
    WhenSupported: int
class ProtectionScenario(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    TransportSelected: int
    TrustedProxy: int
    value__: int
class ServiceNameCollection(_n_2_t_1, _n_2_t_0):
    def __init__(self, items: _n_2_t_0) -> ServiceNameCollection:...
    def Contains(self, searchServiceName: str) -> bool:...
    def Merge(self, serviceNames: _n_2_t_2) -> ServiceNameCollection:...
    def Merge(self, serviceName: str) -> ServiceNameCollection:...
class TokenBinding(object):
    @property
    def BindingType(self) -> TokenBindingType:"""BindingType { get; set; } -> TokenBindingType"""
    def GetRawTokenBindingId(self) -> _n_1_t_6[_n_1_t_5]:...
class TokenBindingType(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    Provided: int
    Referred: int
    value__: int
