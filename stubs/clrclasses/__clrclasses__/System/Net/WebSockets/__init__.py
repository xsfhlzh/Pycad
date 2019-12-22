from __clrclasses__.System import IDisposable as _n_0_t_0
from __clrclasses__.System import Uri as _n_0_t_1
from __clrclasses__.System import TimeSpan as _n_0_t_2
from __clrclasses__.System import Byte as _n_0_t_3
from __clrclasses__.System import ArraySegment as _n_0_t_4
from __clrclasses__.System import Nullable as _n_0_t_5
from __clrclasses__.System import Enum as _n_0_t_6
from __clrclasses__.System import IComparable as _n_0_t_7
from __clrclasses__.System import IFormattable as _n_0_t_8
from __clrclasses__.System import IConvertible as _n_0_t_9
from __clrclasses__.System import Exception as _n_0_t_10
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections.Specialized import NameValueCollection as _n_2_t_0
from __clrclasses__.System.ComponentModel import Win32Exception as _n_3_t_0
from __clrclasses__.System.IO import Stream as _n_4_t_0
from __clrclasses__.System.Net import CookieContainer as _n_5_t_0
from __clrclasses__.System.Net import ICredentials as _n_5_t_1
from __clrclasses__.System.Net import IWebProxy as _n_5_t_2
from __clrclasses__.System.Net import CookieCollection as _n_5_t_3
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_6_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_7_t_0
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509CertificateCollection as _n_8_t_0
from __clrclasses__.System.Security.Principal import IPrincipal as _n_9_t_0
from __clrclasses__.System.Threading import CancellationToken as _n_10_t_0
from __clrclasses__.System.Threading.Tasks import Task as _n_11_t_0
import typing
class ClientWebSocket(WebSocket, _n_0_t_0):
    @property
    def Options(self) -> ClientWebSocketOptions:"""Options { get; } -> ClientWebSocketOptions"""
    def __init__(self) -> ClientWebSocket:...
    def ConnectAsync(self, uri: _n_0_t_1, cancellationToken: _n_10_t_0) -> _n_11_t_0:...
class ClientWebSocketOptions(object):
    @property
    def ClientCertificates(self) -> _n_8_t_0:"""ClientCertificates { get; set; } -> X509CertificateCollection"""
    @property
    def Cookies(self) -> _n_5_t_0:"""Cookies { get; set; } -> CookieContainer"""
    @property
    def Credentials(self) -> _n_5_t_1:"""Credentials { get; set; } -> ICredentials"""
    @property
    def KeepAliveInterval(self) -> _n_0_t_2:"""KeepAliveInterval { get; set; } -> TimeSpan"""
    @property
    def Proxy(self) -> _n_5_t_2:"""Proxy { get; set; } -> IWebProxy"""
    @property
    def UseDefaultCredentials(self) -> bool:"""UseDefaultCredentials { get; set; } -> bool"""
    def AddSubProtocol(self, subProtocol: str):...
    def SetBuffer(self, receiveBufferSize: int, sendBufferSize: int, buffer: _n_0_t_4[_n_0_t_3]):...
    def SetBuffer(self, receiveBufferSize: int, sendBufferSize: int):...
    def SetRequestHeader(self, headerName: str, headerValue: str):...
class HttpListenerWebSocketContext(WebSocketContext):
    pass
class WebSocket(_n_0_t_0):
    @property
    def CloseStatus(self) -> _n_0_t_5[WebSocketCloseStatus]:"""CloseStatus { get; } -> Nullable"""
    @property
    def CloseStatusDescription(self) -> str:"""CloseStatusDescription { get; } -> str"""
    @property
    def DefaultKeepAliveInterval(self) -> _n_0_t_2:"""DefaultKeepAliveInterval { get; } -> TimeSpan"""
    @property
    def State(self) -> WebSocketState:"""State { get; } -> WebSocketState"""
    @property
    def SubProtocol(self) -> str:"""SubProtocol { get; } -> str"""
    def Abort(self):...
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: _n_10_t_0) -> _n_11_t_0:...
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: _n_10_t_0) -> _n_11_t_0:...
    @staticmethod
    def CreateClientBuffer(receiveBufferSize: int, sendBufferSize: int) -> _n_0_t_4[_n_0_t_3]:...
    @staticmethod
    def CreateClientWebSocket(innerStream: _n_4_t_0, subProtocol: str, receiveBufferSize: int, sendBufferSize: int, keepAliveInterval: _n_0_t_2, useZeroMaskingKey: bool, internalBuffer: _n_0_t_4[_n_0_t_3]) -> WebSocket:...
    @staticmethod
    def CreateServerBuffer(receiveBufferSize: int) -> _n_0_t_4[_n_0_t_3]:...
    @staticmethod
    def IsApplicationTargeting45() -> bool:...
    def ReceiveAsync(self, buffer: _n_0_t_4[_n_0_t_3], cancellationToken: _n_10_t_0) -> _n_11_t_0[WebSocketReceiveResult]:...
    @staticmethod
    def RegisterPrefixes():...
    def SendAsync(self, buffer: _n_0_t_4[_n_0_t_3], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: _n_10_t_0) -> _n_11_t_0:...
class WebSocketCloseStatus(_n_0_t_6, _n_0_t_7, _n_0_t_8, _n_0_t_9):
    Empty: int
    EndpointUnavailable: int
    InternalServerError: int
    InvalidMessageType: int
    InvalidPayloadData: int
    MandatoryExtension: int
    MessageTooBig: int
    NormalClosure: int
    PolicyViolation: int
    ProtocolError: int
    value__: int
class WebSocketContext(object):
    @property
    def CookieCollection(self) -> _n_5_t_3:"""CookieCollection { get; } -> CookieCollection"""
    @property
    def Headers(self) -> _n_2_t_0:"""Headers { get; } -> NameValueCollection"""
    @property
    def IsAuthenticated(self) -> bool:"""IsAuthenticated { get; } -> bool"""
    @property
    def IsLocal(self) -> bool:"""IsLocal { get; } -> bool"""
    @property
    def IsSecureConnection(self) -> bool:"""IsSecureConnection { get; } -> bool"""
    @property
    def Origin(self) -> str:"""Origin { get; } -> str"""
    @property
    def RequestUri(self) -> _n_0_t_1:"""RequestUri { get; } -> Uri"""
    @property
    def SecWebSocketKey(self) -> str:"""SecWebSocketKey { get; } -> str"""
    @property
    def SecWebSocketProtocols(self) -> _n_1_t_0[str]:"""SecWebSocketProtocols { get; } -> IEnumerable"""
    @property
    def SecWebSocketVersion(self) -> str:"""SecWebSocketVersion { get; } -> str"""
    @property
    def User(self) -> _n_9_t_0:"""User { get; } -> IPrincipal"""
    @property
    def WebSocket(self) -> WebSocket:"""WebSocket { get; } -> WebSocket"""
class WebSocketError(_n_0_t_6, _n_0_t_7, _n_0_t_8, _n_0_t_9):
    ConnectionClosedPrematurely: int
    Faulted: int
    HeaderError: int
    InvalidMessageType: int
    InvalidState: int
    NativeError: int
    NotAWebSocket: int
    Success: int
    UnsupportedProtocol: int
    UnsupportedVersion: int
    value__: int
class WebSocketException(_n_3_t_0, _n_7_t_0, _n_6_t_0):
    @property
    def WebSocketErrorCode(self) -> WebSocketError:"""WebSocketErrorCode { get; } -> WebSocketError"""
    def __init__(self, message: str, innerException: _n_0_t_10) -> WebSocketException:...
    def __init__(self, message: str) -> WebSocketException:...
    def __init__(self, error: WebSocketError, nativeError: int, message: str, innerException: _n_0_t_10) -> WebSocketException:...
    def __init__(self, error: WebSocketError, nativeError: int, innerException: _n_0_t_10) -> WebSocketException:...
    def __init__(self, error: WebSocketError, nativeError: int, message: str) -> WebSocketException:...
    def __init__(self, error: WebSocketError, nativeError: int) -> WebSocketException:...
    def __init__(self, nativeError: int, innerException: _n_0_t_10) -> WebSocketException:...
    def __init__(self, nativeError: int, message: str) -> WebSocketException:...
    def __init__(self, nativeError: int) -> WebSocketException:...
    def __init__(self, error: WebSocketError, message: str, innerException: _n_0_t_10) -> WebSocketException:...
    def __init__(self, error: WebSocketError, innerException: _n_0_t_10) -> WebSocketException:...
    def __init__(self, error: WebSocketError, message: str) -> WebSocketException:...
    def __init__(self, error: WebSocketError) -> WebSocketException:...
    def __init__(self) -> WebSocketException:...
class WebSocketMessageType(_n_0_t_6, _n_0_t_7, _n_0_t_8, _n_0_t_9):
    Binary: int
    Close: int
    Text: int
    value__: int
class WebSocketReceiveResult(object):
    @property
    def CloseStatus(self) -> _n_0_t_5[WebSocketCloseStatus]:"""CloseStatus { get; set; } -> Nullable"""
    @property
    def CloseStatusDescription(self) -> str:"""CloseStatusDescription { get; set; } -> str"""
    @property
    def Count(self) -> int:"""Count { get; set; } -> int"""
    @property
    def EndOfMessage(self) -> bool:"""EndOfMessage { get; set; } -> bool"""
    @property
    def MessageType(self) -> WebSocketMessageType:"""MessageType { get; set; } -> WebSocketMessageType"""
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: _n_0_t_5[WebSocketCloseStatus], closeStatusDescription: str) -> WebSocketReceiveResult:...
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool) -> WebSocketReceiveResult:...
class WebSocketState(_n_0_t_6, _n_0_t_7, _n_0_t_8, _n_0_t_9):
    Aborted: int
    Closed: int
    CloseReceived: int
    CloseSent: int
    Connecting: int
    _None: int
    Open: int
    value__: int
