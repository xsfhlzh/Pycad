from __clrclasses__.System import TimeSpan as _n_0_t_0
from __clrclasses__.System import Uri as _n_0_t_1
from __clrclasses__.System import Enum as _n_0_t_2
from __clrclasses__.System import IComparable as _n_0_t_3
from __clrclasses__.System import IFormattable as _n_0_t_4
from __clrclasses__.System import IConvertible as _n_0_t_5
from __clrclasses__.System import Type as _n_0_t_6
from __clrclasses__.System.Collections import ICollection as _n_1_t_0
from __clrclasses__.System.Configuration import ConfigurationElement as _n_2_t_0
from __clrclasses__.System.Configuration import ConfigurationElementCollection as _n_2_t_1
from __clrclasses__.System.Configuration import ConfigurationSection as _n_2_t_2
from __clrclasses__.System.Configuration import ConfigurationSectionGroup as _n_2_t_3
from __clrclasses__.System.Configuration import Configuration as _n_2_t_4
from __clrclasses__.System.Net.Cache import RequestCacheLevel as _n_3_t_0
from __clrclasses__.System.Net.Cache import HttpRequestCacheLevel as _n_3_t_1
from __clrclasses__.System.Net.Mail import SmtpDeliveryFormat as _n_4_t_0
from __clrclasses__.System.Net.Mail import SmtpDeliveryMethod as _n_4_t_1
from __clrclasses__.System.Net.Security import EncryptionPolicy as _n_5_t_0
from __clrclasses__.System.Net.Sockets import IPProtectionLevel as _n_6_t_0
import typing
class AuthenticationModuleElement(_n_2_t_0):
    @property
    def Type(self) -> str:"""Type { get; set; } -> str"""
    def __init__(self, typeName: str) -> AuthenticationModuleElement:...
    def __init__(self) -> AuthenticationModuleElement:...
class AuthenticationModuleElementCollection(_n_2_t_1, _n_1_t_0, typing.Iterable[AuthenticationModuleElement]):
    @property
    def Item(self) -> AuthenticationModuleElement:"""Item { get; set; } -> AuthenticationModuleElement"""
    def __init__(self) -> AuthenticationModuleElementCollection:...
    def Add(self, element: AuthenticationModuleElement):...
    def Clear(self):...
    def IndexOf(self, element: AuthenticationModuleElement) -> int:...
    def Remove(self, name: str):...
    def Remove(self, element: AuthenticationModuleElement):...
    def RemoveAt(self, index: int):...
class AuthenticationModulesSection(_n_2_t_2):
    @property
    def AuthenticationModules(self) -> AuthenticationModuleElementCollection:"""AuthenticationModules { get; } -> AuthenticationModuleElementCollection"""
    def __init__(self) -> AuthenticationModulesSection:...
class BypassElement(_n_2_t_0):
    @property
    def Address(self) -> str:"""Address { get; set; } -> str"""
    def __init__(self, address: str) -> BypassElement:...
    def __init__(self) -> BypassElement:...
class BypassElementCollection(_n_2_t_1, _n_1_t_0, typing.Iterable[BypassElement]):
    @property
    def Item(self) -> BypassElement:"""Item { get; set; } -> BypassElement"""
    def __init__(self) -> BypassElementCollection:...
    def Add(self, element: BypassElement):...
    def Clear(self):...
    def IndexOf(self, element: BypassElement) -> int:...
    def Remove(self, name: str):...
    def Remove(self, element: BypassElement):...
    def RemoveAt(self, index: int):...
class ConnectionManagementElement(_n_2_t_0):
    @property
    def Address(self) -> str:"""Address { get; set; } -> str"""
    @property
    def MaxConnection(self) -> int:"""MaxConnection { get; set; } -> int"""
    def __init__(self, address: str, maxConnection: int) -> ConnectionManagementElement:...
    def __init__(self) -> ConnectionManagementElement:...
class ConnectionManagementElementCollection(_n_2_t_1, _n_1_t_0, typing.Iterable[ConnectionManagementElement]):
    @property
    def Item(self) -> ConnectionManagementElement:"""Item { get; set; } -> ConnectionManagementElement"""
    def __init__(self) -> ConnectionManagementElementCollection:...
    def Add(self, element: ConnectionManagementElement):...
    def Clear(self):...
    def IndexOf(self, element: ConnectionManagementElement) -> int:...
    def Remove(self, name: str):...
    def Remove(self, element: ConnectionManagementElement):...
    def RemoveAt(self, index: int):...
class ConnectionManagementSection(_n_2_t_2):
    @property
    def ConnectionManagement(self) -> ConnectionManagementElementCollection:"""ConnectionManagement { get; } -> ConnectionManagementElementCollection"""
    def __init__(self) -> ConnectionManagementSection:...
class DefaultProxySection(_n_2_t_2):
    @property
    def BypassList(self) -> BypassElementCollection:"""BypassList { get; } -> BypassElementCollection"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def Module(self) -> ModuleElement:"""Module { get; } -> ModuleElement"""
    @property
    def Proxy(self) -> ProxyElement:"""Proxy { get; } -> ProxyElement"""
    @property
    def UseDefaultCredentials(self) -> bool:"""UseDefaultCredentials { get; set; } -> bool"""
    def __init__(self) -> DefaultProxySection:...
class FtpCachePolicyElement(_n_2_t_0):
    @property
    def PolicyLevel(self) -> _n_3_t_0:"""PolicyLevel { get; set; } -> RequestCacheLevel"""
    def __init__(self) -> FtpCachePolicyElement:...
class HttpCachePolicyElement(_n_2_t_0):
    @property
    def MaximumAge(self) -> _n_0_t_0:"""MaximumAge { get; set; } -> TimeSpan"""
    @property
    def MaximumStale(self) -> _n_0_t_0:"""MaximumStale { get; set; } -> TimeSpan"""
    @property
    def MinimumFresh(self) -> _n_0_t_0:"""MinimumFresh { get; set; } -> TimeSpan"""
    @property
    def PolicyLevel(self) -> _n_3_t_1:"""PolicyLevel { get; set; } -> HttpRequestCacheLevel"""
    def __init__(self) -> HttpCachePolicyElement:...
class HttpListenerElement(_n_2_t_0):
    @property
    def Timeouts(self) -> HttpListenerTimeoutsElement:"""Timeouts { get; } -> HttpListenerTimeoutsElement"""
    @property
    def UnescapeRequestUrl(self) -> bool:"""UnescapeRequestUrl { get; } -> bool"""
    def __init__(self) -> HttpListenerElement:...
class HttpListenerTimeoutsElement(_n_2_t_0):
    @property
    def DrainEntityBody(self) -> _n_0_t_0:"""DrainEntityBody { get; } -> TimeSpan"""
    @property
    def EntityBody(self) -> _n_0_t_0:"""EntityBody { get; } -> TimeSpan"""
    @property
    def HeaderWait(self) -> _n_0_t_0:"""HeaderWait { get; } -> TimeSpan"""
    @property
    def IdleConnection(self) -> _n_0_t_0:"""IdleConnection { get; } -> TimeSpan"""
    @property
    def MinSendBytesPerSecond(self) -> int:"""MinSendBytesPerSecond { get; } -> int"""
    @property
    def RequestQueue(self) -> _n_0_t_0:"""RequestQueue { get; } -> TimeSpan"""
    def __init__(self) -> HttpListenerTimeoutsElement:...
class HttpWebRequestElement(_n_2_t_0):
    @property
    def MaximumErrorResponseLength(self) -> int:"""MaximumErrorResponseLength { get; set; } -> int"""
    @property
    def MaximumResponseHeadersLength(self) -> int:"""MaximumResponseHeadersLength { get; set; } -> int"""
    @property
    def MaximumUnauthorizedUploadLength(self) -> int:"""MaximumUnauthorizedUploadLength { get; set; } -> int"""
    @property
    def UseUnsafeHeaderParsing(self) -> bool:"""UseUnsafeHeaderParsing { get; set; } -> bool"""
    def __init__(self) -> HttpWebRequestElement:...
class Ipv6Element(_n_2_t_0):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    def __init__(self) -> Ipv6Element:...
class MailSettingsSectionGroup(_n_2_t_3):
    @property
    def Smtp(self) -> SmtpSection:"""Smtp { get; } -> SmtpSection"""
    def __init__(self) -> MailSettingsSectionGroup:...
class ModuleElement(_n_2_t_0):
    @property
    def Type(self) -> str:"""Type { get; set; } -> str"""
    def __init__(self) -> ModuleElement:...
class NetSectionGroup(_n_2_t_3):
    @property
    def AuthenticationModules(self) -> AuthenticationModulesSection:"""AuthenticationModules { get; } -> AuthenticationModulesSection"""
    @property
    def ConnectionManagement(self) -> ConnectionManagementSection:"""ConnectionManagement { get; } -> ConnectionManagementSection"""
    @property
    def DefaultProxy(self) -> DefaultProxySection:"""DefaultProxy { get; } -> DefaultProxySection"""
    @property
    def MailSettings(self) -> MailSettingsSectionGroup:"""MailSettings { get; } -> MailSettingsSectionGroup"""
    @property
    def RequestCaching(self) -> RequestCachingSection:"""RequestCaching { get; } -> RequestCachingSection"""
    @property
    def Settings(self) -> SettingsSection:"""Settings { get; } -> SettingsSection"""
    @property
    def WebRequestModules(self) -> WebRequestModulesSection:"""WebRequestModules { get; } -> WebRequestModulesSection"""
    def __init__(self) -> NetSectionGroup:...
    @staticmethod
    def GetSectionGroup(config: _n_2_t_4) -> NetSectionGroup:...
class PerformanceCountersElement(_n_2_t_0):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    def __init__(self) -> PerformanceCountersElement:...
class ProxyElement(_n_2_t_0):
    @property
    def AutoDetect(self) -> ProxyElement.AutoDetectValues:"""AutoDetect { get; set; } -> ProxyElement.AutoDetectValues"""
    @property
    def BypassOnLocal(self) -> ProxyElement.BypassOnLocalValues:"""BypassOnLocal { get; set; } -> ProxyElement.BypassOnLocalValues"""
    @property
    def ProxyAddress(self) -> _n_0_t_1:"""ProxyAddress { get; set; } -> Uri"""
    @property
    def ScriptLocation(self) -> _n_0_t_1:"""ScriptLocation { get; set; } -> Uri"""
    @property
    def UseSystemDefault(self) -> ProxyElement.UseSystemDefaultValues:"""UseSystemDefault { get; set; } -> ProxyElement.UseSystemDefaultValues"""
    def __init__(self) -> ProxyElement:...
    class AutoDetectValues(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
        _False: int
        _True: int
        Unspecified: int
        value__: int
    class BypassOnLocalValues(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
        _False: int
        _True: int
        Unspecified: int
        value__: int
    class UseSystemDefaultValues(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
        _False: int
        _True: int
        Unspecified: int
        value__: int
class RequestCachingSection(_n_2_t_2):
    @property
    def DefaultFtpCachePolicy(self) -> FtpCachePolicyElement:"""DefaultFtpCachePolicy { get; } -> FtpCachePolicyElement"""
    @property
    def DefaultHttpCachePolicy(self) -> HttpCachePolicyElement:"""DefaultHttpCachePolicy { get; } -> HttpCachePolicyElement"""
    @property
    def DefaultPolicyLevel(self) -> _n_3_t_0:"""DefaultPolicyLevel { get; set; } -> RequestCacheLevel"""
    @property
    def DisableAllCaching(self) -> bool:"""DisableAllCaching { get; set; } -> bool"""
    @property
    def IsPrivateCache(self) -> bool:"""IsPrivateCache { get; set; } -> bool"""
    @property
    def UnspecifiedMaximumAge(self) -> _n_0_t_0:"""UnspecifiedMaximumAge { get; set; } -> TimeSpan"""
    def __init__(self) -> RequestCachingSection:...
class ServicePointManagerElement(_n_2_t_0):
    @property
    def CheckCertificateName(self) -> bool:"""CheckCertificateName { get; set; } -> bool"""
    @property
    def CheckCertificateRevocationList(self) -> bool:"""CheckCertificateRevocationList { get; set; } -> bool"""
    @property
    def DnsRefreshTimeout(self) -> int:"""DnsRefreshTimeout { get; set; } -> int"""
    @property
    def EnableDnsRoundRobin(self) -> bool:"""EnableDnsRoundRobin { get; set; } -> bool"""
    @property
    def EncryptionPolicy(self) -> _n_5_t_0:"""EncryptionPolicy { get; set; } -> EncryptionPolicy"""
    @property
    def Expect100Continue(self) -> bool:"""Expect100Continue { get; set; } -> bool"""
    @property
    def UseNagleAlgorithm(self) -> bool:"""UseNagleAlgorithm { get; set; } -> bool"""
    def __init__(self) -> ServicePointManagerElement:...
class SettingsSection(_n_2_t_2):
    @property
    def HttpListener(self) -> HttpListenerElement:"""HttpListener { get; } -> HttpListenerElement"""
    @property
    def HttpWebRequest(self) -> HttpWebRequestElement:"""HttpWebRequest { get; } -> HttpWebRequestElement"""
    @property
    def Ipv6(self) -> Ipv6Element:"""Ipv6 { get; } -> Ipv6Element"""
    @property
    def PerformanceCounters(self) -> PerformanceCountersElement:"""PerformanceCounters { get; } -> PerformanceCountersElement"""
    @property
    def ServicePointManager(self) -> ServicePointManagerElement:"""ServicePointManager { get; } -> ServicePointManagerElement"""
    @property
    def Socket(self) -> SocketElement:"""Socket { get; } -> SocketElement"""
    @property
    def WebProxyScript(self) -> WebProxyScriptElement:"""WebProxyScript { get; } -> WebProxyScriptElement"""
    @property
    def WebUtility(self) -> WebUtilityElement:"""WebUtility { get; } -> WebUtilityElement"""
    def __init__(self) -> SettingsSection:...
class SmtpNetworkElement(_n_2_t_0):
    @property
    def ClientDomain(self) -> str:"""ClientDomain { get; set; } -> str"""
    @property
    def DefaultCredentials(self) -> bool:"""DefaultCredentials { get; set; } -> bool"""
    @property
    def EnableSsl(self) -> bool:"""EnableSsl { get; set; } -> bool"""
    @property
    def Host(self) -> str:"""Host { get; set; } -> str"""
    @property
    def Password(self) -> str:"""Password { get; set; } -> str"""
    @property
    def Port(self) -> int:"""Port { get; set; } -> int"""
    @property
    def TargetName(self) -> str:"""TargetName { get; set; } -> str"""
    @property
    def UserName(self) -> str:"""UserName { get; set; } -> str"""
    def __init__(self) -> SmtpNetworkElement:...
class SmtpSection(_n_2_t_2):
    @property
    def DeliveryFormat(self) -> _n_4_t_0:"""DeliveryFormat { get; set; } -> SmtpDeliveryFormat"""
    @property
    def DeliveryMethod(self) -> _n_4_t_1:"""DeliveryMethod { get; set; } -> SmtpDeliveryMethod"""
    @property
    def From(self) -> str:"""From { get; set; } -> str"""
    @property
    def Network(self) -> SmtpNetworkElement:"""Network { get; } -> SmtpNetworkElement"""
    @property
    def SpecifiedPickupDirectory(self) -> SmtpSpecifiedPickupDirectoryElement:"""SpecifiedPickupDirectory { get; } -> SmtpSpecifiedPickupDirectoryElement"""
    def __init__(self) -> SmtpSection:...
class SmtpSpecifiedPickupDirectoryElement(_n_2_t_0):
    @property
    def PickupDirectoryLocation(self) -> str:"""PickupDirectoryLocation { get; set; } -> str"""
    def __init__(self) -> SmtpSpecifiedPickupDirectoryElement:...
class SocketElement(_n_2_t_0):
    @property
    def AlwaysUseCompletionPortsForAccept(self) -> bool:"""AlwaysUseCompletionPortsForAccept { get; set; } -> bool"""
    @property
    def AlwaysUseCompletionPortsForConnect(self) -> bool:"""AlwaysUseCompletionPortsForConnect { get; set; } -> bool"""
    @property
    def IPProtectionLevel(self) -> _n_6_t_0:"""IPProtectionLevel { get; set; } -> IPProtectionLevel"""
    def __init__(self) -> SocketElement:...
class UnicodeDecodingConformance(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Auto: int
    Compat: int
    Loose: int
    Strict: int
    value__: int
class UnicodeEncodingConformance(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Auto: int
    Compat: int
    Strict: int
    value__: int
class WebProxyScriptElement(_n_2_t_0):
    @property
    def DownloadTimeout(self) -> _n_0_t_0:"""DownloadTimeout { get; set; } -> TimeSpan"""
    def __init__(self) -> WebProxyScriptElement:...
class WebRequestModuleElement(_n_2_t_0):
    @property
    def Prefix(self) -> str:"""Prefix { get; set; } -> str"""
    @property
    def Type(self) -> _n_0_t_6:"""Type { get; set; } -> Type"""
    def __init__(self, prefix: str, type: _n_0_t_6) -> WebRequestModuleElement:...
    def __init__(self, prefix: str, type: str) -> WebRequestModuleElement:...
    def __init__(self) -> WebRequestModuleElement:...
class WebRequestModuleElementCollection(_n_2_t_1, _n_1_t_0, typing.Iterable[WebRequestModuleElement]):
    @property
    def Item(self) -> WebRequestModuleElement:"""Item { get; set; } -> WebRequestModuleElement"""
    def __init__(self) -> WebRequestModuleElementCollection:...
    def Add(self, element: WebRequestModuleElement):...
    def Clear(self):...
    def IndexOf(self, element: WebRequestModuleElement) -> int:...
    def Remove(self, name: str):...
    def Remove(self, element: WebRequestModuleElement):...
    def RemoveAt(self, index: int):...
class WebRequestModulesSection(_n_2_t_2):
    @property
    def WebRequestModules(self) -> WebRequestModuleElementCollection:"""WebRequestModules { get; } -> WebRequestModuleElementCollection"""
    def __init__(self) -> WebRequestModulesSection:...
class WebUtilityElement(_n_2_t_0):
    @property
    def UnicodeDecodingConformance(self) -> UnicodeDecodingConformance:"""UnicodeDecodingConformance { get; set; } -> UnicodeDecodingConformance"""
    @property
    def UnicodeEncodingConformance(self) -> UnicodeEncodingConformance:"""UnicodeEncodingConformance { get; set; } -> UnicodeEncodingConformance"""
    def __init__(self) -> WebUtilityElement:...
