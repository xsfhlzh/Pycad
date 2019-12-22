import __clrclasses__.System.Net.WebSockets as WebSockets
import __clrclasses__.System.Net.Mime as Mime
import __clrclasses__.System.Net.Mail as Mail
import __clrclasses__.System.Net.NetworkInformation as NetworkInformation
import __clrclasses__.System.Net.Cache as Cache
import __clrclasses__.System.Net.Configuration as Configuration
import __clrclasses__.System.Net.Security as Security
import __clrclasses__.System.Net.Sockets as Sockets
from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import MulticastDelegate as _n_0_t_4
from __clrclasses__.System import ICloneable as _n_0_t_5
from __clrclasses__.System import IntPtr as _n_0_t_6
from __clrclasses__.System import IAsyncResult as _n_0_t_7
from __clrclasses__.System import AsyncCallback as _n_0_t_8
from __clrclasses__.System import Array as _n_0_t_9
from __clrclasses__.System import Uri as _n_0_t_10
from __clrclasses__.System import DateTime as _n_0_t_11
from __clrclasses__.System import FormatException as _n_0_t_12
from __clrclasses__.System import Byte as _n_0_t_13
from __clrclasses__.System import IDisposable as _n_0_t_14
from __clrclasses__.System import TimeSpan as _n_0_t_15
from __clrclasses__.System import ArraySegment as _n_0_t_16
from __clrclasses__.System import Version as _n_0_t_17
from __clrclasses__.System import Guid as _n_0_t_18
from __clrclasses__.System import Type as _n_0_t_19
from __clrclasses__.System import InvalidOperationException as _n_0_t_20
from __clrclasses__.System import Exception as _n_0_t_21
from __clrclasses__.System import MarshalByRefObject as _n_0_t_22
from __clrclasses__.System import EventArgs as _n_0_t_23
from __clrclasses__.System.Collections import IEnumerator as _n_1_t_0
from __clrclasses__.System.Collections import ICollection as _n_1_t_1
from __clrclasses__.System.Collections import IEnumerable as _n_1_t_2
from __clrclasses__.System.Collections import ArrayList as _n_1_t_3
from __clrclasses__.System.Collections.Generic import ICollection as _n_2_t_0
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_2_t_1
from __clrclasses__.System.Collections.Specialized import StringDictionary as _n_3_t_0
from __clrclasses__.System.Collections.Specialized import NameValueCollection as _n_3_t_1
from __clrclasses__.System.ComponentModel import AsyncCompletedEventArgs as _n_4_t_0
from __clrclasses__.System.ComponentModel import ProgressChangedEventArgs as _n_4_t_1
from __clrclasses__.System.ComponentModel import Win32Exception as _n_4_t_2
from __clrclasses__.System.ComponentModel import Component as _n_4_t_3
from __clrclasses__.System.ComponentModel import IComponent as _n_4_t_4
from __clrclasses__.System.ComponentModel import AsyncCompletedEventHandler as _n_4_t_5
from __clrclasses__.System.IO import Stream as _n_5_t_0
from __clrclasses__.System.IO import TextWriter as _n_5_t_1
from __clrclasses__.System.Net.Cache import RequestCachePolicy as _n_6_t_0
from __clrclasses__.System.Net.Security import RemoteCertificateValidationCallback as _n_7_t_0
from __clrclasses__.System.Net.Security import EncryptionPolicy as _n_7_t_1
from __clrclasses__.System.Net.Security import AuthenticationLevel as _n_7_t_2
from __clrclasses__.System.Net.Sockets import AddressFamily as _n_8_t_0
from __clrclasses__.System.Net.WebSockets import HttpListenerWebSocketContext as _n_9_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_10_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_10_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_11_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_11_t_1
from __clrclasses__.System.Security import CodeAccessPermission as _n_12_t_0
from __clrclasses__.System.Security import IPermission as _n_12_t_1
from __clrclasses__.System.Security import IStackWalk as _n_12_t_2
from __clrclasses__.System.Security import SecureString as _n_12_t_3
from __clrclasses__.System.Security.Authentication.ExtendedProtection import ServiceNameCollection as _n_13_t_0
from __clrclasses__.System.Security.Authentication.ExtendedProtection import ExtendedProtectionPolicy as _n_13_t_1
from __clrclasses__.System.Security.Authentication.ExtendedProtection import ChannelBinding as _n_13_t_2
from __clrclasses__.System.Security.Authentication.ExtendedProtection import ChannelBindingKind as _n_13_t_3
from __clrclasses__.System.Security.Authentication.ExtendedProtection import TokenBinding as _n_13_t_4
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509CertificateCollection as _n_14_t_0
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509Certificate2 as _n_14_t_1
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509Certificate as _n_14_t_2
from __clrclasses__.System.Security.Permissions import IUnrestrictedPermission as _n_15_t_0
from __clrclasses__.System.Security.Permissions import PermissionState as _n_15_t_1
from __clrclasses__.System.Security.Permissions import CodeAccessSecurityAttribute as _n_15_t_2
from __clrclasses__.System.Security.Permissions import SecurityAction as _n_15_t_3
from __clrclasses__.System.Security.Principal import GenericIdentity as _n_16_t_0
from __clrclasses__.System.Security.Principal import IIdentity as _n_16_t_1
from __clrclasses__.System.Security.Principal import IPrincipal as _n_16_t_2
from __clrclasses__.System.Security.Principal import TokenImpersonationLevel as _n_16_t_3
from __clrclasses__.System.Text import Encoding as _n_17_t_0
from __clrclasses__.System.Text.RegularExpressions import Regex as _n_18_t_0
from __clrclasses__.System.Threading.Tasks import Task as _n_19_t_0
import typing
class AuthenticationManager(object):
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:"""CredentialPolicy { get; set; } -> ICredentialPolicy"""
    @property
    def CustomTargetNameDictionary(self) -> _n_3_t_0:"""CustomTargetNameDictionary { get; } -> StringDictionary"""
    @property
    def RegisteredModules(self) -> _n_1_t_0:"""RegisteredModules { get; } -> IEnumerator"""
    @staticmethod
    def Authenticate(challenge: str, request: WebRequest, credentials: ICredentials) -> Authorization:...
    @staticmethod
    def PreAuthenticate(request: WebRequest, credentials: ICredentials) -> Authorization:...
    @staticmethod
    def Register(authenticationModule: IAuthenticationModule):...
    @staticmethod
    def Unregister(authenticationScheme: str):...
    @staticmethod
    def Unregister(authenticationModule: IAuthenticationModule):...
class AuthenticationSchemes(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Anonymous: int
    Basic: int
    Digest: int
    IntegratedWindowsAuthentication: int
    Negotiate: int
    _None: int
    Ntlm: int
    value__: int
class AuthenticationSchemeSelector(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> AuthenticationSchemeSelector:...
    def BeginInvoke(self, httpRequest: HttpListenerRequest, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7) -> AuthenticationSchemes:...
    def Invoke(self, httpRequest: HttpListenerRequest) -> AuthenticationSchemes:...
class Authorization(object):
    @property
    def Complete(self) -> bool:"""Complete { get; } -> bool"""
    @property
    def ConnectionGroupId(self) -> str:"""ConnectionGroupId { get; } -> str"""
    @property
    def Message(self) -> str:"""Message { get; } -> str"""
    @property
    def MutuallyAuthenticated(self) -> bool:"""MutuallyAuthenticated { get; set; } -> bool"""
    @property
    def ProtectionRealm(self) -> _n_0_t_9[str]:"""ProtectionRealm { get; set; } -> Array"""
    def __init__(self, token: str, finished: bool, connectionGroupId: str) -> Authorization:...
    def __init__(self, token: str, finished: bool) -> Authorization:...
    def __init__(self, token: str) -> Authorization:...
class BindIPEndPoint(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> BindIPEndPoint:...
    def BeginInvoke(self, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: int, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7) -> IPEndPoint:...
    def Invoke(self, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: int) -> IPEndPoint:...
class Cookie(object):
    @property
    def Comment(self) -> str:"""Comment { get; set; } -> str"""
    @property
    def CommentUri(self) -> _n_0_t_10:"""CommentUri { get; set; } -> Uri"""
    @property
    def Discard(self) -> bool:"""Discard { get; set; } -> bool"""
    @property
    def Domain(self) -> str:"""Domain { get; set; } -> str"""
    @property
    def Expired(self) -> bool:"""Expired { get; set; } -> bool"""
    @property
    def Expires(self) -> _n_0_t_11:"""Expires { get; set; } -> DateTime"""
    @property
    def HttpOnly(self) -> bool:"""HttpOnly { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Path(self) -> str:"""Path { get; set; } -> str"""
    @property
    def Port(self) -> str:"""Port { get; set; } -> str"""
    @property
    def Secure(self) -> bool:"""Secure { get; set; } -> bool"""
    @property
    def TimeStamp(self) -> _n_0_t_11:"""TimeStamp { get; } -> DateTime"""
    @property
    def Value(self) -> str:"""Value { get; set; } -> str"""
    @property
    def Version(self) -> int:"""Version { get; set; } -> int"""
    def __init__(self, name: str, value: str, path: str, domain: str) -> Cookie:...
    def __init__(self, name: str, value: str, path: str) -> Cookie:...
    def __init__(self, name: str, value: str) -> Cookie:...
    def __init__(self) -> Cookie:...
class CookieCollection(_n_1_t_1, typing.Iterable[Cookie]):
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def Item(self) -> Cookie:"""Item { get; } -> Cookie"""
    def __init__(self) -> CookieCollection:...
    def Add(self, cookies: CookieCollection):...
    def Add(self, cookie: Cookie):...
class CookieContainer(object):
    DefaultCookieLengthLimit: int
    DefaultCookieLimit: int
    DefaultPerDomainCookieLimit: int
    @property
    def Capacity(self) -> int:"""Capacity { get; set; } -> int"""
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def MaxCookieSize(self) -> int:"""MaxCookieSize { get; set; } -> int"""
    @property
    def PerDomainCapacity(self) -> int:"""PerDomainCapacity { get; set; } -> int"""
    def __init__(self, capacity: int, perDomainCapacity: int, maxCookieSize: int) -> CookieContainer:...
    def __init__(self, capacity: int) -> CookieContainer:...
    def __init__(self) -> CookieContainer:...
    def Add(self, uri: _n_0_t_10, cookies: CookieCollection):...
    def Add(self, uri: _n_0_t_10, cookie: Cookie):...
    def Add(self, cookies: CookieCollection):...
    def Add(self, cookie: Cookie):...
    def GetCookieHeader(self, uri: _n_0_t_10) -> str:...
    def GetCookies(self, uri: _n_0_t_10) -> CookieCollection:...
    def SetCookies(self, uri: _n_0_t_10, cookieHeader: str):...
class CookieException(_n_0_t_12, _n_11_t_0, _n_10_t_0):
    def __init__(self) -> CookieException:...
class CredentialCache(ICredentials, ICredentialsByHost, _n_1_t_2):
    @property
    def DefaultCredentials(self) -> ICredentials:"""DefaultCredentials { get; } -> ICredentials"""
    @property
    def DefaultNetworkCredentials(self) -> NetworkCredential:"""DefaultNetworkCredentials { get; } -> NetworkCredential"""
    def __init__(self) -> CredentialCache:...
    def Add(self, host: str, port: int, authenticationType: str, credential: NetworkCredential):...
    def Add(self, uriPrefix: _n_0_t_10, authType: str, cred: NetworkCredential):...
    def Remove(self, host: str, port: int, authenticationType: str):...
    def Remove(self, uriPrefix: _n_0_t_10, authType: str):...
class DecompressionMethods(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Deflate: int
    GZip: int
    _None: int
    value__: int
class Dns(object):
    @staticmethod
    def BeginGetHostAddresses(hostNameOrAddress: str, requestCallback: _n_0_t_8, state: object) -> _n_0_t_7:...
    @staticmethod
    def BeginGetHostByName(hostName: str, requestCallback: _n_0_t_8, stateObject: object) -> _n_0_t_7:...
    @staticmethod
    def BeginGetHostEntry(address: IPAddress, requestCallback: _n_0_t_8, stateObject: object) -> _n_0_t_7:...
    @staticmethod
    def BeginGetHostEntry(hostNameOrAddress: str, requestCallback: _n_0_t_8, stateObject: object) -> _n_0_t_7:...
    @staticmethod
    def BeginResolve(hostName: str, requestCallback: _n_0_t_8, stateObject: object) -> _n_0_t_7:...
    @staticmethod
    def EndGetHostAddresses(asyncResult: _n_0_t_7) -> _n_0_t_9[IPAddress]:...
    @staticmethod
    def EndGetHostByName(asyncResult: _n_0_t_7) -> IPHostEntry:...
    @staticmethod
    def EndGetHostEntry(asyncResult: _n_0_t_7) -> IPHostEntry:...
    @staticmethod
    def EndResolve(asyncResult: _n_0_t_7) -> IPHostEntry:...
    @staticmethod
    def GetHostAddresses(hostNameOrAddress: str) -> _n_0_t_9[IPAddress]:...
    @staticmethod
    def GetHostAddressesAsync(hostNameOrAddress: str) -> _n_19_t_0[_n_0_t_9[IPAddress]]:...
    @staticmethod
    def GetHostByAddress(address: IPAddress) -> IPHostEntry:...
    @staticmethod
    def GetHostByAddress(address: str) -> IPHostEntry:...
    @staticmethod
    def GetHostByName(hostName: str) -> IPHostEntry:...
    @staticmethod
    def GetHostEntry(address: IPAddress) -> IPHostEntry:...
    @staticmethod
    def GetHostEntry(hostNameOrAddress: str) -> IPHostEntry:...
    @staticmethod
    def GetHostEntryAsync(hostNameOrAddress: str) -> _n_19_t_0[IPHostEntry]:...
    @staticmethod
    def GetHostEntryAsync(address: IPAddress) -> _n_19_t_0[IPHostEntry]:...
    @staticmethod
    def GetHostName() -> str:...
    @staticmethod
    def Resolve(hostName: str) -> IPHostEntry:...
class DnsEndPoint(EndPoint):
    @property
    def Host(self) -> str:"""Host { get; } -> str"""
    @property
    def Port(self) -> int:"""Port { get; } -> int"""
    def __init__(self, host: str, port: int, addressFamily: _n_8_t_0) -> DnsEndPoint:...
    def __init__(self, host: str, port: int) -> DnsEndPoint:...
class DnsPermission(_n_12_t_0, _n_12_t_1, _n_12_t_2, _n_15_t_0):
    def __init__(self, state: _n_15_t_1) -> DnsPermission:...
class DnsPermissionAttribute(_n_15_t_2, _n_10_t_1):
    def __init__(self, action: _n_15_t_3) -> DnsPermissionAttribute:...
class DownloadDataCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> _n_0_t_9[_n_0_t_13]:"""Result { get; } -> Array"""
class DownloadDataCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> DownloadDataCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: DownloadDataCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: DownloadDataCompletedEventArgs):...
class DownloadProgressChangedEventArgs(_n_4_t_1):
    @property
    def BytesReceived(self) -> int:"""BytesReceived { get; } -> int"""
    @property
    def TotalBytesToReceive(self) -> int:"""TotalBytesToReceive { get; } -> int"""
class DownloadProgressChangedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> DownloadProgressChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: DownloadProgressChangedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: DownloadProgressChangedEventArgs):...
class DownloadStringCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> str:"""Result { get; } -> str"""
class DownloadStringCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> DownloadStringCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: DownloadStringCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: DownloadStringCompletedEventArgs):...
class EndPoint(object):
    @property
    def AddressFamily(self) -> _n_8_t_0:"""AddressFamily { get; } -> AddressFamily"""
    def Create(self, socketAddress: SocketAddress) -> EndPoint:...
    def Serialize(self) -> SocketAddress:...
class EndpointPermission(object):
    @property
    def Hostname(self) -> str:"""Hostname { get; } -> str"""
    @property
    def Port(self) -> int:"""Port { get; } -> int"""
    @property
    def Transport(self) -> TransportType:"""Transport { get; } -> TransportType"""
class FileWebRequest(WebRequest, _n_11_t_0):
    pass
class FileWebResponse(WebResponse, _n_11_t_0, _n_0_t_14, ICloseEx):
    pass
class FtpStatusCode(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AccountNeeded: int
    ActionAbortedLocalProcessingError: int
    ActionAbortedUnknownPageType: int
    ActionNotTakenFilenameNotAllowed: int
    ActionNotTakenFileUnavailable: int
    ActionNotTakenFileUnavailableOrBusy: int
    ActionNotTakenInsufficientSpace: int
    ArgumentSyntaxError: int
    BadCommandSequence: int
    CantOpenData: int
    ClosingControl: int
    ClosingData: int
    CommandExtraneous: int
    CommandNotImplemented: int
    CommandOK: int
    CommandSyntaxError: int
    ConnectionClosed: int
    DataAlreadyOpen: int
    DirectoryStatus: int
    EnteringPassive: int
    FileActionAborted: int
    FileActionOK: int
    FileCommandPending: int
    FileStatus: int
    LoggedInProceed: int
    NeedLoginAccount: int
    NotLoggedIn: int
    OpeningData: int
    PathnameCreated: int
    RestartMarker: int
    SendPasswordCommand: int
    SendUserCommand: int
    ServerWantsSecureSession: int
    ServiceNotAvailable: int
    ServiceTemporarilyNotAvailable: int
    SystemType: int
    Undefined: int
    value__: int
class FtpWebRequest(WebRequest, _n_11_t_0):
    @property
    def ClientCertificates(self) -> _n_14_t_0:"""ClientCertificates { get; set; } -> X509CertificateCollection"""
    @property
    def ContentOffset(self) -> int:"""ContentOffset { get; set; } -> int"""
    @property
    def EnableSsl(self) -> bool:"""EnableSsl { get; set; } -> bool"""
    @property
    def KeepAlive(self) -> bool:"""KeepAlive { get; set; } -> bool"""
    @property
    def ReadWriteTimeout(self) -> int:"""ReadWriteTimeout { get; set; } -> int"""
    @property
    def RenameTo(self) -> str:"""RenameTo { get; set; } -> str"""
    @property
    def ServicePoint(self) -> ServicePoint:"""ServicePoint { get; } -> ServicePoint"""
    @property
    def UseBinary(self) -> bool:"""UseBinary { get; set; } -> bool"""
    @property
    def UsePassive(self) -> bool:"""UsePassive { get; set; } -> bool"""
class FtpWebResponse(WebResponse, _n_11_t_0, _n_0_t_14):
    @property
    def BannerMessage(self) -> str:"""BannerMessage { get; } -> str"""
    @property
    def ExitMessage(self) -> str:"""ExitMessage { get; } -> str"""
    @property
    def LastModified(self) -> _n_0_t_11:"""LastModified { get; } -> DateTime"""
    @property
    def StatusCode(self) -> FtpStatusCode:"""StatusCode { get; } -> FtpStatusCode"""
    @property
    def StatusDescription(self) -> str:"""StatusDescription { get; } -> str"""
    @property
    def WelcomeMessage(self) -> str:"""WelcomeMessage { get; } -> str"""
class GlobalProxySelection(object):
    @property
    def Select(self) -> IWebProxy:"""Select { get; set; } -> IWebProxy"""
    def __init__(self) -> GlobalProxySelection:...
    @staticmethod
    def GetEmptyWebProxy() -> IWebProxy:...
class HttpContinueDelegate(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> HttpContinueDelegate:...
    def BeginInvoke(self, StatusCode: int, httpHeaders: WebHeaderCollection, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, StatusCode: int, httpHeaders: WebHeaderCollection):...
class HttpListener(_n_0_t_14):
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes:"""AuthenticationSchemes { get; set; } -> AuthenticationSchemes"""
    @property
    def AuthenticationSchemeSelectorDelegate(self) -> AuthenticationSchemeSelector:"""AuthenticationSchemeSelectorDelegate { get; set; } -> AuthenticationSchemeSelector"""
    @property
    def DefaultServiceNames(self) -> _n_13_t_0:"""DefaultServiceNames { get; } -> ServiceNameCollection"""
    @property
    def ExtendedProtectionPolicy(self) -> _n_13_t_1:"""ExtendedProtectionPolicy { get; set; } -> ExtendedProtectionPolicy"""
    @property
    def ExtendedProtectionSelectorDelegate(self) -> HttpListener.ExtendedProtectionSelector:"""ExtendedProtectionSelectorDelegate { get; set; } -> HttpListener.ExtendedProtectionSelector"""
    @property
    def IgnoreWriteExceptions(self) -> bool:"""IgnoreWriteExceptions { get; set; } -> bool"""
    @property
    def IsListening(self) -> bool:"""IsListening { get; } -> bool"""
    @property
    def IsSupported(self) -> bool:"""IsSupported { get; } -> bool"""
    @property
    def Prefixes(self) -> HttpListenerPrefixCollection:"""Prefixes { get; } -> HttpListenerPrefixCollection"""
    @property
    def Realm(self) -> str:"""Realm { get; set; } -> str"""
    @property
    def TimeoutManager(self) -> HttpListenerTimeoutManager:"""TimeoutManager { get; } -> HttpListenerTimeoutManager"""
    @property
    def UnsafeConnectionNtlmAuthentication(self) -> bool:"""UnsafeConnectionNtlmAuthentication { get; set; } -> bool"""
    def __init__(self) -> HttpListener:...
    def Abort(self):...
    def BeginGetContext(self, callback: _n_0_t_8, state: object) -> _n_0_t_7:...
    def Close(self):...
    def EndGetContext(self, asyncResult: _n_0_t_7) -> HttpListenerContext:...
    def GetContext(self) -> HttpListenerContext:...
    def GetContextAsync(self) -> _n_19_t_0[HttpListenerContext]:...
    def Start(self):...
    def Stop(self):...
    class ExtendedProtectionSelector(_n_0_t_4, _n_0_t_5, _n_11_t_0):
        def __init__(self, object: object, method: _n_0_t_6) -> HttpListener.ExtendedProtectionSelector:...
        def BeginInvoke(self, request: HttpListenerRequest, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
        def EndInvoke(self, result: _n_0_t_7) -> _n_13_t_1:...
        def Invoke(self, request: HttpListenerRequest) -> _n_13_t_1:...
class HttpListenerBasicIdentity(_n_16_t_0, _n_16_t_1):
    @property
    def Password(self) -> str:"""Password { get; } -> str"""
    def __init__(self, username: str, password: str) -> HttpListenerBasicIdentity:...
class HttpListenerContext(object):
    @property
    def Request(self) -> HttpListenerRequest:"""Request { get; } -> HttpListenerRequest"""
    @property
    def Response(self) -> HttpListenerResponse:"""Response { get; } -> HttpListenerResponse"""
    @property
    def User(self) -> _n_16_t_2:"""User { get; } -> IPrincipal"""
    def AcceptWebSocketAsync(self, subProtocol: str, receiveBufferSize: int, keepAliveInterval: _n_0_t_15, internalBuffer: _n_0_t_16[_n_0_t_13]) -> _n_19_t_0[_n_9_t_0]:...
    def AcceptWebSocketAsync(self, subProtocol: str, receiveBufferSize: int, keepAliveInterval: _n_0_t_15) -> _n_19_t_0[_n_9_t_0]:...
    def AcceptWebSocketAsync(self, subProtocol: str, keepAliveInterval: _n_0_t_15) -> _n_19_t_0[_n_9_t_0]:...
    def AcceptWebSocketAsync(self, subProtocol: str) -> _n_19_t_0[_n_9_t_0]:...
class HttpListenerException(_n_4_t_2, _n_11_t_0, _n_10_t_0):
    def __init__(self, errorCode: int, message: str) -> HttpListenerException:...
    def __init__(self, errorCode: int) -> HttpListenerException:...
    def __init__(self) -> HttpListenerException:...
class HttpListenerPrefixCollection(_n_2_t_0[str]):
    @property
    def IsSynchronized(self) -> bool:"""IsSynchronized { get; } -> bool"""
class HttpListenerRequest(object):
    @property
    def AcceptTypes(self) -> _n_0_t_9[str]:"""AcceptTypes { get; } -> Array"""
    @property
    def ClientCertificateError(self) -> int:"""ClientCertificateError { get; } -> int"""
    @property
    def ContentEncoding(self) -> _n_17_t_0:"""ContentEncoding { get; } -> Encoding"""
    @property
    def ContentLength64(self) -> int:"""ContentLength64 { get; } -> int"""
    @property
    def ContentType(self) -> str:"""ContentType { get; } -> str"""
    @property
    def Cookies(self) -> CookieCollection:"""Cookies { get; } -> CookieCollection"""
    @property
    def HasEntityBody(self) -> bool:"""HasEntityBody { get; } -> bool"""
    @property
    def Headers(self) -> _n_3_t_1:"""Headers { get; } -> NameValueCollection"""
    @property
    def HttpMethod(self) -> str:"""HttpMethod { get; } -> str"""
    @property
    def InputStream(self) -> _n_5_t_0:"""InputStream { get; } -> Stream"""
    @property
    def IsAuthenticated(self) -> bool:"""IsAuthenticated { get; } -> bool"""
    @property
    def IsLocal(self) -> bool:"""IsLocal { get; } -> bool"""
    @property
    def IsSecureConnection(self) -> bool:"""IsSecureConnection { get; } -> bool"""
    @property
    def IsWebSocketRequest(self) -> bool:"""IsWebSocketRequest { get; } -> bool"""
    @property
    def KeepAlive(self) -> bool:"""KeepAlive { get; } -> bool"""
    @property
    def LocalEndPoint(self) -> IPEndPoint:"""LocalEndPoint { get; } -> IPEndPoint"""
    @property
    def ProtocolVersion(self) -> _n_0_t_17:"""ProtocolVersion { get; } -> Version"""
    @property
    def QueryString(self) -> _n_3_t_1:"""QueryString { get; } -> NameValueCollection"""
    @property
    def RawUrl(self) -> str:"""RawUrl { get; } -> str"""
    @property
    def RemoteEndPoint(self) -> IPEndPoint:"""RemoteEndPoint { get; } -> IPEndPoint"""
    @property
    def RequestTraceIdentifier(self) -> _n_0_t_18:"""RequestTraceIdentifier { get; } -> Guid"""
    @property
    def ServiceName(self) -> str:"""ServiceName { get; set; } -> str"""
    @property
    def TransportContext(self) -> TransportContext:"""TransportContext { get; } -> TransportContext"""
    @property
    def Url(self) -> _n_0_t_10:"""Url { get; } -> Uri"""
    @property
    def UrlReferrer(self) -> _n_0_t_10:"""UrlReferrer { get; } -> Uri"""
    @property
    def UserAgent(self) -> str:"""UserAgent { get; } -> str"""
    @property
    def UserHostAddress(self) -> str:"""UserHostAddress { get; } -> str"""
    @property
    def UserHostName(self) -> str:"""UserHostName { get; } -> str"""
    @property
    def UserLanguages(self) -> _n_0_t_9[str]:"""UserLanguages { get; } -> Array"""
    def BeginGetClientCertificate(self, requestCallback: _n_0_t_8, state: object) -> _n_0_t_7:...
    def EndGetClientCertificate(self, asyncResult: _n_0_t_7) -> _n_14_t_1:...
    def GetClientCertificate(self) -> _n_14_t_1:...
    def GetClientCertificateAsync(self) -> _n_19_t_0[_n_14_t_1]:...
class HttpListenerResponse(_n_0_t_14):
    @property
    def ContentEncoding(self) -> _n_17_t_0:"""ContentEncoding { get; set; } -> Encoding"""
    @property
    def ContentLength64(self) -> int:"""ContentLength64 { get; set; } -> int"""
    @property
    def ContentType(self) -> str:"""ContentType { get; set; } -> str"""
    @property
    def Cookies(self) -> CookieCollection:"""Cookies { get; set; } -> CookieCollection"""
    @property
    def Headers(self) -> WebHeaderCollection:"""Headers { get; set; } -> WebHeaderCollection"""
    @property
    def KeepAlive(self) -> bool:"""KeepAlive { get; set; } -> bool"""
    @property
    def OutputStream(self) -> _n_5_t_0:"""OutputStream { get; } -> Stream"""
    @property
    def ProtocolVersion(self) -> _n_0_t_17:"""ProtocolVersion { get; set; } -> Version"""
    @property
    def RedirectLocation(self) -> str:"""RedirectLocation { get; set; } -> str"""
    @property
    def SendChunked(self) -> bool:"""SendChunked { get; set; } -> bool"""
    @property
    def StatusCode(self) -> int:"""StatusCode { get; set; } -> int"""
    @property
    def StatusDescription(self) -> str:"""StatusDescription { get; set; } -> str"""
    def Abort(self):...
    def AddHeader(self, name: str, value: str):...
    def AppendCookie(self, cookie: Cookie):...
    def AppendHeader(self, name: str, value: str):...
    def Close(self):...
    def Close(self, responseEntity: _n_0_t_9[_n_0_t_13], willBlock: bool):...
    def CopyFrom(self, templateResponse: HttpListenerResponse):...
    def Redirect(self, url: str):...
    def SetCookie(self, cookie: Cookie):...
class HttpListenerTimeoutManager(object):
    @property
    def DrainEntityBody(self) -> _n_0_t_15:"""DrainEntityBody { get; set; } -> TimeSpan"""
    @property
    def EntityBody(self) -> _n_0_t_15:"""EntityBody { get; set; } -> TimeSpan"""
    @property
    def HeaderWait(self) -> _n_0_t_15:"""HeaderWait { get; set; } -> TimeSpan"""
    @property
    def IdleConnection(self) -> _n_0_t_15:"""IdleConnection { get; set; } -> TimeSpan"""
    @property
    def MinSendBytesPerSecond(self) -> int:"""MinSendBytesPerSecond { get; set; } -> int"""
    @property
    def RequestQueue(self) -> _n_0_t_15:"""RequestQueue { get; set; } -> TimeSpan"""
class HttpRequestHeader(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Accept: int
    AcceptCharset: int
    AcceptEncoding: int
    AcceptLanguage: int
    Allow: int
    Authorization: int
    CacheControl: int
    Connection: int
    ContentEncoding: int
    ContentLanguage: int
    ContentLength: int
    ContentLocation: int
    ContentMd5: int
    ContentRange: int
    ContentType: int
    Cookie: int
    Date: int
    Expect: int
    Expires: int
    From: int
    Host: int
    IfMatch: int
    IfModifiedSince: int
    IfNoneMatch: int
    IfRange: int
    IfUnmodifiedSince: int
    KeepAlive: int
    LastModified: int
    MaxForwards: int
    Pragma: int
    ProxyAuthorization: int
    Range: int
    Referer: int
    Te: int
    Trailer: int
    TransferEncoding: int
    Translate: int
    Upgrade: int
    UserAgent: int
    value__: int
    Via: int
    Warning: int
class HttpResponseHeader(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AcceptRanges: int
    Age: int
    Allow: int
    CacheControl: int
    Connection: int
    ContentEncoding: int
    ContentLanguage: int
    ContentLength: int
    ContentLocation: int
    ContentMd5: int
    ContentRange: int
    ContentType: int
    Date: int
    ETag: int
    Expires: int
    KeepAlive: int
    LastModified: int
    Location: int
    Pragma: int
    ProxyAuthenticate: int
    RetryAfter: int
    Server: int
    SetCookie: int
    Trailer: int
    TransferEncoding: int
    Upgrade: int
    value__: int
    Vary: int
    Via: int
    Warning: int
    WwwAuthenticate: int
class HttpStatusCode(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Accepted: int
    Ambiguous: int
    BadGateway: int
    BadRequest: int
    Conflict: int
    Continue: int
    Created: int
    ExpectationFailed: int
    Forbidden: int
    Found: int
    GatewayTimeout: int
    Gone: int
    HttpVersionNotSupported: int
    InternalServerError: int
    LengthRequired: int
    MethodNotAllowed: int
    Moved: int
    MovedPermanently: int
    MultipleChoices: int
    NoContent: int
    NonAuthoritativeInformation: int
    NotAcceptable: int
    NotFound: int
    NotImplemented: int
    NotModified: int
    OK: int
    PartialContent: int
    PaymentRequired: int
    PreconditionFailed: int
    ProxyAuthenticationRequired: int
    Redirect: int
    RedirectKeepVerb: int
    RedirectMethod: int
    RequestedRangeNotSatisfiable: int
    RequestEntityTooLarge: int
    RequestTimeout: int
    RequestUriTooLong: int
    ResetContent: int
    SeeOther: int
    ServiceUnavailable: int
    SwitchingProtocols: int
    TemporaryRedirect: int
    Unauthorized: int
    UnsupportedMediaType: int
    Unused: int
    UpgradeRequired: int
    UseProxy: int
    value__: int
class HttpVersion(object):
    Version10: int
    Version11: int
    def __init__(self) -> HttpVersion:...
class HttpWebRequest(WebRequest, _n_11_t_0):
    @property
    def Accept(self) -> str:"""Accept { get; set; } -> str"""
    @property
    def Address(self) -> _n_0_t_10:"""Address { get; } -> Uri"""
    @property
    def AllowAutoRedirect(self) -> bool:"""AllowAutoRedirect { get; set; } -> bool"""
    @property
    def AllowReadStreamBuffering(self) -> bool:"""AllowReadStreamBuffering { get; set; } -> bool"""
    @property
    def AllowWriteStreamBuffering(self) -> bool:"""AllowWriteStreamBuffering { get; set; } -> bool"""
    @property
    def AutomaticDecompression(self) -> DecompressionMethods:"""AutomaticDecompression { get; set; } -> DecompressionMethods"""
    @property
    def ClientCertificates(self) -> _n_14_t_0:"""ClientCertificates { get; set; } -> X509CertificateCollection"""
    @property
    def Connection(self) -> str:"""Connection { get; set; } -> str"""
    @property
    def ContinueDelegate(self) -> HttpContinueDelegate:"""ContinueDelegate { get; set; } -> HttpContinueDelegate"""
    @property
    def ContinueTimeout(self) -> int:"""ContinueTimeout { get; set; } -> int"""
    @property
    def CookieContainer(self) -> CookieContainer:"""CookieContainer { get; set; } -> CookieContainer"""
    @property
    def Date(self) -> _n_0_t_11:"""Date { get; set; } -> DateTime"""
    @property
    def DefaultMaximumErrorResponseLength(self) -> int:"""DefaultMaximumErrorResponseLength { get; set; } -> int"""
    @property
    def DefaultMaximumResponseHeadersLength(self) -> int:"""DefaultMaximumResponseHeadersLength { get; set; } -> int"""
    @property
    def Expect(self) -> str:"""Expect { get; set; } -> str"""
    @property
    def HaveResponse(self) -> bool:"""HaveResponse { get; } -> bool"""
    @property
    def Host(self) -> str:"""Host { get; set; } -> str"""
    @property
    def IfModifiedSince(self) -> _n_0_t_11:"""IfModifiedSince { get; set; } -> DateTime"""
    @property
    def KeepAlive(self) -> bool:"""KeepAlive { get; set; } -> bool"""
    @property
    def MaximumAutomaticRedirections(self) -> int:"""MaximumAutomaticRedirections { get; set; } -> int"""
    @property
    def MaximumResponseHeadersLength(self) -> int:"""MaximumResponseHeadersLength { get; set; } -> int"""
    @property
    def MediaType(self) -> str:"""MediaType { get; set; } -> str"""
    @property
    def Pipelined(self) -> bool:"""Pipelined { get; set; } -> bool"""
    @property
    def ProtocolVersion(self) -> _n_0_t_17:"""ProtocolVersion { get; set; } -> Version"""
    @property
    def ReadWriteTimeout(self) -> int:"""ReadWriteTimeout { get; set; } -> int"""
    @property
    def Referer(self) -> str:"""Referer { get; set; } -> str"""
    @property
    def SendChunked(self) -> bool:"""SendChunked { get; set; } -> bool"""
    @property
    def ServerCertificateValidationCallback(self) -> _n_7_t_0:"""ServerCertificateValidationCallback { get; set; } -> RemoteCertificateValidationCallback"""
    @property
    def ServicePoint(self) -> ServicePoint:"""ServicePoint { get; } -> ServicePoint"""
    @property
    def SupportsCookieContainer(self) -> bool:"""SupportsCookieContainer { get; } -> bool"""
    @property
    def TransferEncoding(self) -> str:"""TransferEncoding { get; set; } -> str"""
    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> bool:"""UnsafeAuthenticatedConnectionSharing { get; set; } -> bool"""
    @property
    def UserAgent(self) -> str:"""UserAgent { get; set; } -> str"""
    def __init__(self) -> HttpWebRequest:...
    def AddRange(self, rangeSpecifier: str, range: int):...
    def AddRange(self, rangeSpecifier: str, _from: int, to: int):...
    def AddRange(self, range: int):...
    def AddRange(self, _from: int, to: int):...
class HttpWebResponse(WebResponse, _n_11_t_0, _n_0_t_14):
    @property
    def CharacterSet(self) -> str:"""CharacterSet { get; } -> str"""
    @property
    def ContentEncoding(self) -> str:"""ContentEncoding { get; } -> str"""
    @property
    def Cookies(self) -> CookieCollection:"""Cookies { get; set; } -> CookieCollection"""
    @property
    def LastModified(self) -> _n_0_t_11:"""LastModified { get; } -> DateTime"""
    @property
    def Method(self) -> str:"""Method { get; } -> str"""
    @property
    def ProtocolVersion(self) -> _n_0_t_17:"""ProtocolVersion { get; } -> Version"""
    @property
    def Server(self) -> str:"""Server { get; } -> str"""
    @property
    def StatusCode(self) -> HttpStatusCode:"""StatusCode { get; } -> HttpStatusCode"""
    @property
    def StatusDescription(self) -> str:"""StatusDescription { get; } -> str"""
    def __init__(self) -> HttpWebResponse:...
    def GetResponseHeader(self, headerName: str) -> str:...
class IAuthenticationModule():
    @property
    def AuthenticationType(self) -> str:"""AuthenticationType { get; } -> str"""
    @property
    def CanPreAuthenticate(self) -> bool:"""CanPreAuthenticate { get; } -> bool"""
    def Authenticate(self, challenge: str, request: WebRequest, credentials: ICredentials) -> Authorization:...
    def PreAuthenticate(self, request: WebRequest, credentials: ICredentials) -> Authorization:...
class ICertificatePolicy():
    def CheckValidationResult(self, srvPoint: ServicePoint, certificate: _n_14_t_2, request: WebRequest, certificateProblem: int) -> bool:...
class ICredentialPolicy():
    def ShouldSendCredential(self, challengeUri: _n_0_t_10, request: WebRequest, credential: NetworkCredential, authenticationModule: IAuthenticationModule) -> bool:...
class ICredentials():
    def GetCredential(self, uri: _n_0_t_10, authType: str) -> NetworkCredential:...
class ICredentialsByHost():
    def GetCredential(self, host: str, port: int, authenticationType: str) -> NetworkCredential:...
class IPAddress(object):
    Any: int
    Broadcast: int
    IPv6Any: int
    IPv6Loopback: int
    IPv6None: int
    Loopback: int
    _None: int
    @property
    def Address(self) -> int:"""Address { get; set; } -> int"""
    @property
    def AddressFamily(self) -> _n_8_t_0:"""AddressFamily { get; } -> AddressFamily"""
    @property
    def IsIPv4MappedToIPv6(self) -> bool:"""IsIPv4MappedToIPv6 { get; } -> bool"""
    @property
    def IsIPv6LinkLocal(self) -> bool:"""IsIPv6LinkLocal { get; } -> bool"""
    @property
    def IsIPv6Multicast(self) -> bool:"""IsIPv6Multicast { get; } -> bool"""
    @property
    def IsIPv6SiteLocal(self) -> bool:"""IsIPv6SiteLocal { get; } -> bool"""
    @property
    def IsIPv6Teredo(self) -> bool:"""IsIPv6Teredo { get; } -> bool"""
    @property
    def ScopeId(self) -> int:"""ScopeId { get; set; } -> int"""
    def __init__(self, address: _n_0_t_9[_n_0_t_13]) -> IPAddress:...
    def __init__(self, address: _n_0_t_9[_n_0_t_13], scopeid: int) -> IPAddress:...
    def __init__(self, newAddress: int) -> IPAddress:...
    def GetAddressBytes(self) -> _n_0_t_9[_n_0_t_13]:...
    @staticmethod
    def HostToNetworkOrder(host: int) -> int:...
    @staticmethod
    def IsLoopback(address: IPAddress) -> bool:...
    def MapToIPv4(self) -> IPAddress:...
    def MapToIPv6(self) -> IPAddress:...
    @staticmethod
    def NetworkToHostOrder(network: int) -> int:...
    @staticmethod
    def Parse(ipString: str) -> IPAddress:...
    @staticmethod
    def TryParse(ipString: str, address: IPAddress) -> bool:...
class IPEndPoint(EndPoint):
    MaxPort: int
    MinPort: int
    @property
    def Address(self) -> IPAddress:"""Address { get; set; } -> IPAddress"""
    @property
    def Port(self) -> int:"""Port { get; set; } -> int"""
    def __init__(self, address: IPAddress, port: int) -> IPEndPoint:...
    def __init__(self, address: int, port: int) -> IPEndPoint:...
class IPHostEntry(object):
    @property
    def AddressList(self) -> _n_0_t_9[IPAddress]:"""AddressList { get; set; } -> Array"""
    @property
    def Aliases(self) -> _n_0_t_9[str]:"""Aliases { get; set; } -> Array"""
    @property
    def HostName(self) -> str:"""HostName { get; set; } -> str"""
    def __init__(self) -> IPHostEntry:...
class IWebProxy():
    @property
    def Credentials(self) -> ICredentials:"""Credentials { get; set; } -> ICredentials"""
    def GetProxy(self, destination: _n_0_t_10) -> _n_0_t_10:...
    def IsBypassed(self, host: _n_0_t_10) -> bool:...
class IWebProxyScript():
    def Close(self):...
    def Load(self, scriptLocation: _n_0_t_10, script: str, helperType: _n_0_t_19) -> bool:...
    def Run(self, url: str, host: str) -> str:...
class IWebRequestCreate():
    def Create(self, uri: _n_0_t_10) -> WebRequest:...
class NetworkAccess(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Accept: int
    Connect: int
    value__: int
class NetworkCredential(ICredentials, ICredentialsByHost):
    @property
    def Domain(self) -> str:"""Domain { get; set; } -> str"""
    @property
    def Password(self) -> str:"""Password { get; set; } -> str"""
    @property
    def SecurePassword(self) -> _n_12_t_3:"""SecurePassword { get; set; } -> SecureString"""
    @property
    def UserName(self) -> str:"""UserName { get; set; } -> str"""
    def __init__(self, userName: str, password: _n_12_t_3, domain: str) -> NetworkCredential:...
    def __init__(self, userName: str, password: str, domain: str) -> NetworkCredential:...
    def __init__(self, userName: str, password: _n_12_t_3) -> NetworkCredential:...
    def __init__(self) -> NetworkCredential:...
    def __init__(self, userName: str, password: str) -> NetworkCredential:...
class OpenReadCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> _n_5_t_0:"""Result { get; } -> Stream"""
class OpenReadCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> OpenReadCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: OpenReadCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: OpenReadCompletedEventArgs):...
class OpenWriteCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> _n_5_t_0:"""Result { get; } -> Stream"""
class OpenWriteCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> OpenWriteCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: OpenWriteCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: OpenWriteCompletedEventArgs):...
class ProtocolViolationException(_n_0_t_20, _n_11_t_0, _n_10_t_0):
    def __init__(self, message: str) -> ProtocolViolationException:...
    def __init__(self) -> ProtocolViolationException:...
class SecurityProtocolType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Ssl3: int
    SystemDefault: int
    Tls: int
    Tls11: int
    Tls12: int
    value__: int
class ServicePoint(object):
    @property
    def Address(self) -> _n_0_t_10:"""Address { get; } -> Uri"""
    @property
    def BindIPEndPointDelegate(self) -> BindIPEndPoint:"""BindIPEndPointDelegate { get; set; } -> BindIPEndPoint"""
    @property
    def Certificate(self) -> _n_14_t_2:"""Certificate { get; } -> X509Certificate"""
    @property
    def ClientCertificate(self) -> _n_14_t_2:"""ClientCertificate { get; } -> X509Certificate"""
    @property
    def ConnectionLeaseTimeout(self) -> int:"""ConnectionLeaseTimeout { get; set; } -> int"""
    @property
    def ConnectionLimit(self) -> int:"""ConnectionLimit { get; set; } -> int"""
    @property
    def ConnectionName(self) -> str:"""ConnectionName { get; } -> str"""
    @property
    def CurrentConnections(self) -> int:"""CurrentConnections { get; } -> int"""
    @property
    def Expect100Continue(self) -> bool:"""Expect100Continue { get; set; } -> bool"""
    @property
    def IdleSince(self) -> _n_0_t_11:"""IdleSince { get; } -> DateTime"""
    @property
    def MaxIdleTime(self) -> int:"""MaxIdleTime { get; set; } -> int"""
    @property
    def ProtocolVersion(self) -> _n_0_t_17:"""ProtocolVersion { get; } -> Version"""
    @property
    def ReceiveBufferSize(self) -> int:"""ReceiveBufferSize { get; set; } -> int"""
    @property
    def SupportsPipelining(self) -> bool:"""SupportsPipelining { get; } -> bool"""
    @property
    def UseNagleAlgorithm(self) -> bool:"""UseNagleAlgorithm { get; set; } -> bool"""
    def CloseConnectionGroup(self, connectionGroupName: str) -> bool:...
    def SetTcpKeepAlive(self, enabled: bool, keepAliveTime: int, keepAliveInterval: int):...
class ServicePointManager(object):
    DefaultNonPersistentConnectionLimit: int
    DefaultPersistentConnectionLimit: int
    @property
    def CertificatePolicy(self) -> ICertificatePolicy:"""CertificatePolicy { get; set; } -> ICertificatePolicy"""
    @property
    def CheckCertificateRevocationList(self) -> bool:"""CheckCertificateRevocationList { get; set; } -> bool"""
    @property
    def DefaultConnectionLimit(self) -> int:"""DefaultConnectionLimit { get; set; } -> int"""
    @property
    def DnsRefreshTimeout(self) -> int:"""DnsRefreshTimeout { get; set; } -> int"""
    @property
    def EnableDnsRoundRobin(self) -> bool:"""EnableDnsRoundRobin { get; set; } -> bool"""
    @property
    def EncryptionPolicy(self) -> _n_7_t_1:"""EncryptionPolicy { get; } -> EncryptionPolicy"""
    @property
    def Expect100Continue(self) -> bool:"""Expect100Continue { get; set; } -> bool"""
    @property
    def MaxServicePointIdleTime(self) -> int:"""MaxServicePointIdleTime { get; set; } -> int"""
    @property
    def MaxServicePoints(self) -> int:"""MaxServicePoints { get; set; } -> int"""
    @property
    def ReusePort(self) -> bool:"""ReusePort { get; set; } -> bool"""
    @property
    def SecurityProtocol(self) -> SecurityProtocolType:"""SecurityProtocol { get; set; } -> SecurityProtocolType"""
    @property
    def ServerCertificateValidationCallback(self) -> _n_7_t_0:"""ServerCertificateValidationCallback { get; set; } -> RemoteCertificateValidationCallback"""
    @property
    def UseNagleAlgorithm(self) -> bool:"""UseNagleAlgorithm { get; set; } -> bool"""
    @staticmethod
    def FindServicePoint(address: _n_0_t_10, proxy: IWebProxy) -> ServicePoint:...
    @staticmethod
    def FindServicePoint(uriString: str, proxy: IWebProxy) -> ServicePoint:...
    @staticmethod
    def FindServicePoint(address: _n_0_t_10) -> ServicePoint:...
    @staticmethod
    def SetTcpKeepAlive(enabled: bool, keepAliveTime: int, keepAliveInterval: int):...
class SocketAddress(typing.Iterable[_n_0_t_13]):
    @property
    def Family(self) -> _n_8_t_0:"""Family { get; } -> AddressFamily"""
    @property
    def Item(self) -> _n_0_t_13:"""Item { get; set; } -> Byte"""
    @property
    def Size(self) -> int:"""Size { get; } -> int"""
    def __init__(self, family: _n_8_t_0) -> SocketAddress:...
    def __init__(self, family: _n_8_t_0, size: int) -> SocketAddress:...
class SocketPermission(_n_12_t_0, _n_12_t_1, _n_12_t_2, _n_15_t_0):
    AllPorts: int
    @property
    def AcceptList(self) -> _n_1_t_0:"""AcceptList { get; } -> IEnumerator"""
    @property
    def ConnectList(self) -> _n_1_t_0:"""ConnectList { get; } -> IEnumerator"""
    def __init__(self, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int) -> SocketPermission:...
    def __init__(self, state: _n_15_t_1) -> SocketPermission:...
    def AddPermission(self, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int):...
class SocketPermissionAttribute(_n_15_t_2, _n_10_t_1):
    @property
    def Access(self) -> str:"""Access { get; set; } -> str"""
    @property
    def Host(self) -> str:"""Host { get; set; } -> str"""
    @property
    def Port(self) -> str:"""Port { get; set; } -> str"""
    @property
    def Transport(self) -> str:"""Transport { get; set; } -> str"""
    def __init__(self, action: _n_15_t_3) -> SocketPermissionAttribute:...
class TransportContext(object):
    def GetChannelBinding(self, kind: _n_13_t_3) -> _n_13_t_2:...
    def GetTlsTokenBindings(self) -> _n_2_t_1[_n_13_t_4]:...
class TransportType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    All: int
    Connectionless: int
    ConnectionOriented: int
    Tcp: int
    Udp: int
    value__: int
class UploadDataCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> _n_0_t_9[_n_0_t_13]:"""Result { get; } -> Array"""
class UploadDataCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> UploadDataCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: UploadDataCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: UploadDataCompletedEventArgs):...
class UploadFileCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> _n_0_t_9[_n_0_t_13]:"""Result { get; } -> Array"""
class UploadFileCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> UploadFileCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: UploadFileCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: UploadFileCompletedEventArgs):...
class UploadProgressChangedEventArgs(_n_4_t_1):
    @property
    def BytesReceived(self) -> int:"""BytesReceived { get; } -> int"""
    @property
    def BytesSent(self) -> int:"""BytesSent { get; } -> int"""
    @property
    def TotalBytesToReceive(self) -> int:"""TotalBytesToReceive { get; } -> int"""
    @property
    def TotalBytesToSend(self) -> int:"""TotalBytesToSend { get; } -> int"""
class UploadProgressChangedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> UploadProgressChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: UploadProgressChangedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: UploadProgressChangedEventArgs):...
class UploadStringCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> str:"""Result { get; } -> str"""
class UploadStringCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> UploadStringCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: UploadStringCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: UploadStringCompletedEventArgs):...
class UploadValuesCompletedEventArgs(_n_4_t_0):
    @property
    def Result(self) -> _n_0_t_9[_n_0_t_13]:"""Result { get; } -> Array"""
class UploadValuesCompletedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> UploadValuesCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: UploadValuesCompletedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: UploadValuesCompletedEventArgs):...
class WebClient(_n_4_t_3, _n_4_t_4):
    @property
    def AllowReadStreamBuffering(self) -> bool:"""AllowReadStreamBuffering { get; set; } -> bool"""
    @property
    def AllowWriteStreamBuffering(self) -> bool:"""AllowWriteStreamBuffering { get; set; } -> bool"""
    @property
    def BaseAddress(self) -> str:"""BaseAddress { get; set; } -> str"""
    @property
    def CachePolicy(self) -> _n_6_t_0:"""CachePolicy { get; set; } -> RequestCachePolicy"""
    @property
    def Credentials(self) -> ICredentials:"""Credentials { get; set; } -> ICredentials"""
    @property
    def Encoding(self) -> _n_17_t_0:"""Encoding { get; set; } -> Encoding"""
    @property
    def Headers(self) -> WebHeaderCollection:"""Headers { get; set; } -> WebHeaderCollection"""
    @property
    def IsBusy(self) -> bool:"""IsBusy { get; } -> bool"""
    @property
    def Proxy(self) -> IWebProxy:"""Proxy { get; set; } -> IWebProxy"""
    @property
    def QueryString(self) -> _n_3_t_1:"""QueryString { get; set; } -> NameValueCollection"""
    @property
    def ResponseHeaders(self) -> WebHeaderCollection:"""ResponseHeaders { get; } -> WebHeaderCollection"""
    @property
    def UseDefaultCredentials(self) -> bool:"""UseDefaultCredentials { get; set; } -> bool"""
    @property
    def DownloadDataCompleted(self) -> DownloadDataCompletedEventHandler:
        """DownloadDataCompleted Event: DownloadDataCompletedEventHandler"""
    @property
    def DownloadFileCompleted(self) -> _n_4_t_5:
        """DownloadFileCompleted Event: AsyncCompletedEventHandler"""
    @property
    def DownloadProgressChanged(self) -> DownloadProgressChangedEventHandler:
        """DownloadProgressChanged Event: DownloadProgressChangedEventHandler"""
    @property
    def DownloadStringCompleted(self) -> DownloadStringCompletedEventHandler:
        """DownloadStringCompleted Event: DownloadStringCompletedEventHandler"""
    @property
    def OpenReadCompleted(self) -> OpenReadCompletedEventHandler:
        """OpenReadCompleted Event: OpenReadCompletedEventHandler"""
    @property
    def OpenWriteCompleted(self) -> OpenWriteCompletedEventHandler:
        """OpenWriteCompleted Event: OpenWriteCompletedEventHandler"""
    @property
    def UploadDataCompleted(self) -> UploadDataCompletedEventHandler:
        """UploadDataCompleted Event: UploadDataCompletedEventHandler"""
    @property
    def UploadFileCompleted(self) -> UploadFileCompletedEventHandler:
        """UploadFileCompleted Event: UploadFileCompletedEventHandler"""
    @property
    def UploadProgressChanged(self) -> UploadProgressChangedEventHandler:
        """UploadProgressChanged Event: UploadProgressChangedEventHandler"""
    @property
    def UploadStringCompleted(self) -> UploadStringCompletedEventHandler:
        """UploadStringCompleted Event: UploadStringCompletedEventHandler"""
    @property
    def UploadValuesCompleted(self) -> UploadValuesCompletedEventHandler:
        """UploadValuesCompleted Event: UploadValuesCompletedEventHandler"""
    @property
    def WriteStreamClosed(self) -> WriteStreamClosedEventHandler:
        """WriteStreamClosed Event: WriteStreamClosedEventHandler"""
    def __init__(self) -> WebClient:...
    def CancelAsync(self):...
    def DownloadData(self, address: _n_0_t_10) -> _n_0_t_9[_n_0_t_13]:...
    def DownloadData(self, address: str) -> _n_0_t_9[_n_0_t_13]:...
    def DownloadDataAsync(self, address: _n_0_t_10, userToken: object):...
    def DownloadDataAsync(self, address: _n_0_t_10):...
    def DownloadDataTaskAsync(self, address: _n_0_t_10) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def DownloadDataTaskAsync(self, address: str) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def DownloadFile(self, address: _n_0_t_10, fileName: str):...
    def DownloadFile(self, address: str, fileName: str):...
    def DownloadFileAsync(self, address: _n_0_t_10, fileName: str, userToken: object):...
    def DownloadFileAsync(self, address: _n_0_t_10, fileName: str):...
    def DownloadFileTaskAsync(self, address: _n_0_t_10, fileName: str) -> _n_19_t_0:...
    def DownloadFileTaskAsync(self, address: str, fileName: str) -> _n_19_t_0:...
    def DownloadString(self, address: _n_0_t_10) -> str:...
    def DownloadString(self, address: str) -> str:...
    def DownloadStringAsync(self, address: _n_0_t_10, userToken: object):...
    def DownloadStringAsync(self, address: _n_0_t_10):...
    def DownloadStringTaskAsync(self, address: _n_0_t_10) -> _n_19_t_0[str]:...
    def DownloadStringTaskAsync(self, address: str) -> _n_19_t_0[str]:...
    def OpenRead(self, address: _n_0_t_10) -> _n_5_t_0:...
    def OpenRead(self, address: str) -> _n_5_t_0:...
    def OpenReadAsync(self, address: _n_0_t_10, userToken: object):...
    def OpenReadAsync(self, address: _n_0_t_10):...
    def OpenReadTaskAsync(self, address: _n_0_t_10) -> _n_19_t_0[_n_5_t_0]:...
    def OpenReadTaskAsync(self, address: str) -> _n_19_t_0[_n_5_t_0]:...
    def OpenWrite(self, address: _n_0_t_10, method: str) -> _n_5_t_0:...
    def OpenWrite(self, address: str, method: str) -> _n_5_t_0:...
    def OpenWrite(self, address: _n_0_t_10) -> _n_5_t_0:...
    def OpenWrite(self, address: str) -> _n_5_t_0:...
    def OpenWriteAsync(self, address: _n_0_t_10, method: str, userToken: object):...
    def OpenWriteAsync(self, address: _n_0_t_10, method: str):...
    def OpenWriteAsync(self, address: _n_0_t_10):...
    def OpenWriteTaskAsync(self, address: _n_0_t_10, method: str) -> _n_19_t_0[_n_5_t_0]:...
    def OpenWriteTaskAsync(self, address: str, method: str) -> _n_19_t_0[_n_5_t_0]:...
    def OpenWriteTaskAsync(self, address: _n_0_t_10) -> _n_19_t_0[_n_5_t_0]:...
    def OpenWriteTaskAsync(self, address: str) -> _n_19_t_0[_n_5_t_0]:...
    def UploadData(self, address: _n_0_t_10, method: str, data: _n_0_t_9[_n_0_t_13]) -> _n_0_t_9[_n_0_t_13]:...
    def UploadData(self, address: str, method: str, data: _n_0_t_9[_n_0_t_13]) -> _n_0_t_9[_n_0_t_13]:...
    def UploadData(self, address: _n_0_t_10, data: _n_0_t_9[_n_0_t_13]) -> _n_0_t_9[_n_0_t_13]:...
    def UploadData(self, address: str, data: _n_0_t_9[_n_0_t_13]) -> _n_0_t_9[_n_0_t_13]:...
    def UploadDataAsync(self, address: _n_0_t_10, method: str, data: _n_0_t_9[_n_0_t_13], userToken: object):...
    def UploadDataAsync(self, address: _n_0_t_10, method: str, data: _n_0_t_9[_n_0_t_13]):...
    def UploadDataAsync(self, address: _n_0_t_10, data: _n_0_t_9[_n_0_t_13]):...
    def UploadDataTaskAsync(self, address: _n_0_t_10, method: str, data: _n_0_t_9[_n_0_t_13]) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadDataTaskAsync(self, address: str, method: str, data: _n_0_t_9[_n_0_t_13]) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadDataTaskAsync(self, address: _n_0_t_10, data: _n_0_t_9[_n_0_t_13]) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadDataTaskAsync(self, address: str, data: _n_0_t_9[_n_0_t_13]) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadFile(self, address: _n_0_t_10, method: str, fileName: str) -> _n_0_t_9[_n_0_t_13]:...
    def UploadFile(self, address: str, method: str, fileName: str) -> _n_0_t_9[_n_0_t_13]:...
    def UploadFile(self, address: _n_0_t_10, fileName: str) -> _n_0_t_9[_n_0_t_13]:...
    def UploadFile(self, address: str, fileName: str) -> _n_0_t_9[_n_0_t_13]:...
    def UploadFileAsync(self, address: _n_0_t_10, method: str, fileName: str, userToken: object):...
    def UploadFileAsync(self, address: _n_0_t_10, method: str, fileName: str):...
    def UploadFileAsync(self, address: _n_0_t_10, fileName: str):...
    def UploadFileTaskAsync(self, address: _n_0_t_10, method: str, fileName: str) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadFileTaskAsync(self, address: str, method: str, fileName: str) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadFileTaskAsync(self, address: _n_0_t_10, fileName: str) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadFileTaskAsync(self, address: str, fileName: str) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadString(self, address: _n_0_t_10, method: str, data: str) -> str:...
    def UploadString(self, address: str, method: str, data: str) -> str:...
    def UploadString(self, address: _n_0_t_10, data: str) -> str:...
    def UploadString(self, address: str, data: str) -> str:...
    def UploadStringAsync(self, address: _n_0_t_10, method: str, data: str, userToken: object):...
    def UploadStringAsync(self, address: _n_0_t_10, method: str, data: str):...
    def UploadStringAsync(self, address: _n_0_t_10, data: str):...
    def UploadStringTaskAsync(self, address: _n_0_t_10, method: str, data: str) -> _n_19_t_0[str]:...
    def UploadStringTaskAsync(self, address: str, method: str, data: str) -> _n_19_t_0[str]:...
    def UploadStringTaskAsync(self, address: _n_0_t_10, data: str) -> _n_19_t_0[str]:...
    def UploadStringTaskAsync(self, address: str, data: str) -> _n_19_t_0[str]:...
    def UploadValues(self, address: _n_0_t_10, method: str, data: _n_3_t_1) -> _n_0_t_9[_n_0_t_13]:...
    def UploadValues(self, address: str, method: str, data: _n_3_t_1) -> _n_0_t_9[_n_0_t_13]:...
    def UploadValues(self, address: _n_0_t_10, data: _n_3_t_1) -> _n_0_t_9[_n_0_t_13]:...
    def UploadValues(self, address: str, data: _n_3_t_1) -> _n_0_t_9[_n_0_t_13]:...
    def UploadValuesAsync(self, address: _n_0_t_10, method: str, data: _n_3_t_1, userToken: object):...
    def UploadValuesAsync(self, address: _n_0_t_10, method: str, data: _n_3_t_1):...
    def UploadValuesAsync(self, address: _n_0_t_10, data: _n_3_t_1):...
    def UploadValuesTaskAsync(self, address: _n_0_t_10, method: str, data: _n_3_t_1) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadValuesTaskAsync(self, address: _n_0_t_10, data: _n_3_t_1) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadValuesTaskAsync(self, address: str, method: str, data: _n_3_t_1) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
    def UploadValuesTaskAsync(self, address: str, data: _n_3_t_1) -> _n_19_t_0[_n_0_t_9[_n_0_t_13]]:...
class WebException(_n_0_t_20, _n_11_t_0, _n_10_t_0):
    @property
    def Response(self) -> WebResponse:"""Response { get; } -> WebResponse"""
    @property
    def Status(self) -> WebExceptionStatus:"""Status { get; } -> WebExceptionStatus"""
    def __init__(self, message: str, innerException: _n_0_t_21, status: WebExceptionStatus, response: WebResponse) -> WebException:...
    def __init__(self, message: str, status: WebExceptionStatus) -> WebException:...
    def __init__(self, message: str, innerException: _n_0_t_21) -> WebException:...
    def __init__(self, message: str) -> WebException:...
    def __init__(self) -> WebException:...
class WebExceptionStatus(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    CacheEntryNotFound: int
    ConnectFailure: int
    ConnectionClosed: int
    KeepAliveFailure: int
    MessageLengthLimitExceeded: int
    NameResolutionFailure: int
    Pending: int
    PipelineFailure: int
    ProtocolError: int
    ProxyNameResolutionFailure: int
    ReceiveFailure: int
    RequestCanceled: int
    RequestProhibitedByCachePolicy: int
    RequestProhibitedByProxy: int
    SecureChannelFailure: int
    SendFailure: int
    ServerProtocolViolation: int
    Success: int
    Timeout: int
    TrustFailure: int
    UnknownError: int
    value__: int
class WebHeaderCollection(_n_3_t_1, _n_1_t_1, _n_11_t_0, _n_11_t_1, typing.Iterable[str]):
    def __init__(self) -> WebHeaderCollection:...
    @staticmethod
    def IsRestricted(headerName: str, response: bool) -> bool:...
    @staticmethod
    def IsRestricted(headerName: str) -> bool:...
    def ToByteArray(self) -> _n_0_t_9[_n_0_t_13]:...
class WebPermission(_n_12_t_0, _n_12_t_1, _n_12_t_2, _n_15_t_0):
    @property
    def AcceptList(self) -> _n_1_t_0:"""AcceptList { get; } -> IEnumerator"""
    @property
    def ConnectList(self) -> _n_1_t_0:"""ConnectList { get; } -> IEnumerator"""
    def __init__(self, access: NetworkAccess, uriString: str) -> WebPermission:...
    def __init__(self, access: NetworkAccess, uriRegex: _n_18_t_0) -> WebPermission:...
    def __init__(self) -> WebPermission:...
    def __init__(self, state: _n_15_t_1) -> WebPermission:...
    def AddPermission(self, access: NetworkAccess, uriRegex: _n_18_t_0):...
    def AddPermission(self, access: NetworkAccess, uriString: str):...
class WebPermissionAttribute(_n_15_t_2, _n_10_t_1):
    @property
    def Accept(self) -> str:"""Accept { get; set; } -> str"""
    @property
    def AcceptPattern(self) -> str:"""AcceptPattern { get; set; } -> str"""
    @property
    def Connect(self) -> str:"""Connect { get; set; } -> str"""
    @property
    def ConnectPattern(self) -> str:"""ConnectPattern { get; set; } -> str"""
    def __init__(self, action: _n_15_t_3) -> WebPermissionAttribute:...
class WebProxy(IAutoWebProxy, _n_11_t_0):
    @property
    def Address(self) -> _n_0_t_10:"""Address { get; set; } -> Uri"""
    @property
    def BypassArrayList(self) -> _n_1_t_3:"""BypassArrayList { get; } -> ArrayList"""
    @property
    def BypassList(self) -> _n_0_t_9[str]:"""BypassList { get; set; } -> Array"""
    @property
    def BypassProxyOnLocal(self) -> bool:"""BypassProxyOnLocal { get; set; } -> bool"""
    @property
    def UseDefaultCredentials(self) -> bool:"""UseDefaultCredentials { get; set; } -> bool"""
    def __init__(self, Address: str, BypassOnLocal: bool, BypassList: _n_0_t_9[str], Credentials: ICredentials) -> WebProxy:...
    def __init__(self, Address: str, BypassOnLocal: bool, BypassList: _n_0_t_9[str]) -> WebProxy:...
    def __init__(self, Address: str, BypassOnLocal: bool) -> WebProxy:...
    def __init__(self, Address: str) -> WebProxy:...
    def __init__(self, Host: str, Port: int) -> WebProxy:...
    def __init__(self, Address: _n_0_t_10, BypassOnLocal: bool, BypassList: _n_0_t_9[str], Credentials: ICredentials) -> WebProxy:...
    def __init__(self, Address: _n_0_t_10, BypassOnLocal: bool, BypassList: _n_0_t_9[str]) -> WebProxy:...
    def __init__(self, Address: _n_0_t_10, BypassOnLocal: bool) -> WebProxy:...
    def __init__(self, Address: _n_0_t_10) -> WebProxy:...
    def __init__(self) -> WebProxy:...
    @staticmethod
    def GetDefaultProxy() -> WebProxy:...
class WebRequest(_n_0_t_22, _n_11_t_0):
    @property
    def AuthenticationLevel(self) -> _n_7_t_2:"""AuthenticationLevel { get; set; } -> AuthenticationLevel"""
    @property
    def CachePolicy(self) -> _n_6_t_0:"""CachePolicy { get; set; } -> RequestCachePolicy"""
    @property
    def ConnectionGroupName(self) -> str:"""ConnectionGroupName { get; set; } -> str"""
    @property
    def ContentLength(self) -> int:"""ContentLength { get; set; } -> int"""
    @property
    def ContentType(self) -> str:"""ContentType { get; set; } -> str"""
    @property
    def CreatorInstance(self) -> IWebRequestCreate:"""CreatorInstance { get; } -> IWebRequestCreate"""
    @property
    def Credentials(self) -> ICredentials:"""Credentials { get; set; } -> ICredentials"""
    @property
    def DefaultCachePolicy(self) -> _n_6_t_0:"""DefaultCachePolicy { get; set; } -> RequestCachePolicy"""
    @property
    def DefaultWebProxy(self) -> IWebProxy:"""DefaultWebProxy { get; set; } -> IWebProxy"""
    @property
    def Headers(self) -> WebHeaderCollection:"""Headers { get; set; } -> WebHeaderCollection"""
    @property
    def ImpersonationLevel(self) -> _n_16_t_3:"""ImpersonationLevel { get; set; } -> TokenImpersonationLevel"""
    @property
    def Method(self) -> str:"""Method { get; set; } -> str"""
    @property
    def PreAuthenticate(self) -> bool:"""PreAuthenticate { get; set; } -> bool"""
    @property
    def Proxy(self) -> IWebProxy:"""Proxy { get; set; } -> IWebProxy"""
    @property
    def RequestUri(self) -> _n_0_t_10:"""RequestUri { get; } -> Uri"""
    @property
    def Timeout(self) -> int:"""Timeout { get; set; } -> int"""
    @property
    def UseDefaultCredentials(self) -> bool:"""UseDefaultCredentials { get; set; } -> bool"""
    def Abort(self):...
    def BeginGetRequestStream(self, callback: _n_0_t_8, state: object) -> _n_0_t_7:...
    def BeginGetResponse(self, callback: _n_0_t_8, state: object) -> _n_0_t_7:...
    @staticmethod
    def Create(requestUri: _n_0_t_10) -> WebRequest:...
    @staticmethod
    def Create(requestUriString: str) -> WebRequest:...
    @staticmethod
    def CreateDefault(requestUri: _n_0_t_10) -> WebRequest:...
    @staticmethod
    def CreateHttp(requestUri: _n_0_t_10) -> HttpWebRequest:...
    @staticmethod
    def CreateHttp(requestUriString: str) -> HttpWebRequest:...
    def EndGetRequestStream(self, asyncResult: _n_0_t_7) -> _n_5_t_0:...
    def EndGetResponse(self, asyncResult: _n_0_t_7) -> WebResponse:...
    def GetRequestStream(self) -> _n_5_t_0:...
    def GetRequestStreamAsync(self) -> _n_19_t_0[_n_5_t_0]:...
    def GetResponse(self) -> WebResponse:...
    def GetResponseAsync(self) -> _n_19_t_0[WebResponse]:...
    @staticmethod
    def GetSystemWebProxy() -> IWebProxy:...
    @staticmethod
    def RegisterPortableWebRequestCreator(creator: IWebRequestCreate):...
    @staticmethod
    def RegisterPrefix(prefix: str, creator: IWebRequestCreate) -> bool:...
class WebRequestMethods(object):
    pass
class WebResponse(_n_0_t_22, _n_11_t_0, _n_0_t_14):
    @property
    def ContentLength(self) -> int:"""ContentLength { get; set; } -> int"""
    @property
    def ContentType(self) -> str:"""ContentType { get; set; } -> str"""
    @property
    def Headers(self) -> WebHeaderCollection:"""Headers { get; } -> WebHeaderCollection"""
    @property
    def IsFromCache(self) -> bool:"""IsFromCache { get; } -> bool"""
    @property
    def IsMutuallyAuthenticated(self) -> bool:"""IsMutuallyAuthenticated { get; } -> bool"""
    @property
    def ResponseUri(self) -> _n_0_t_10:"""ResponseUri { get; } -> Uri"""
    @property
    def SupportsHeaders(self) -> bool:"""SupportsHeaders { get; } -> bool"""
    def Close(self):...
    def GetResponseStream(self) -> _n_5_t_0:...
class WebUtility(object):
    @staticmethod
    def HtmlDecode(value: str, output: _n_5_t_1):...
    @staticmethod
    def HtmlDecode(value: str) -> str:...
    @staticmethod
    def HtmlEncode(value: str, output: _n_5_t_1):...
    @staticmethod
    def HtmlEncode(value: str) -> str:...
    @staticmethod
    def UrlDecode(encodedValue: str) -> str:...
    @staticmethod
    def UrlDecodeToBytes(encodedValue: _n_0_t_9[_n_0_t_13], offset: int, count: int) -> _n_0_t_9[_n_0_t_13]:...
    @staticmethod
    def UrlEncode(value: str) -> str:...
    @staticmethod
    def UrlEncodeToBytes(value: _n_0_t_9[_n_0_t_13], offset: int, count: int) -> _n_0_t_9[_n_0_t_13]:...
class WriteStreamClosedEventArgs(_n_0_t_23):
    @property
    def Error(self) -> _n_0_t_21:"""Error { get; } -> Exception"""
    def __init__(self) -> WriteStreamClosedEventArgs:...
class WriteStreamClosedEventHandler(_n_0_t_4, _n_0_t_5, _n_11_t_0):
    def __init__(self, object: object, method: _n_0_t_6) -> WriteStreamClosedEventHandler:...
    def BeginInvoke(self, sender: object, e: WriteStreamClosedEventArgs, callback: _n_0_t_8, object: object) -> _n_0_t_7:...
    def EndInvoke(self, result: _n_0_t_7):...
    def Invoke(self, sender: object, e: WriteStreamClosedEventArgs):...
