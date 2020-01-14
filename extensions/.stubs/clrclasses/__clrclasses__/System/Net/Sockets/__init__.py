from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import ValueType as _n_0_t_4
from __clrclasses__.System import IDisposable as _n_0_t_5
from __clrclasses__.System import Byte as _n_0_t_6
from __clrclasses__.System import Array as _n_0_t_7
from __clrclasses__.System import IntPtr as _n_0_t_8
from __clrclasses__.System import IAsyncResult as _n_0_t_9
from __clrclasses__.System import AsyncCallback as _n_0_t_10
from __clrclasses__.System import ArraySegment as _n_0_t_11
from __clrclasses__.System import EventArgs as _n_0_t_12
from __clrclasses__.System import EventHandler as _n_0_t_13
from __clrclasses__.System import Exception as _n_0_t_14
from __clrclasses__.System import IEquatable as _n_0_t_15
from __clrclasses__.System.Collections import IList as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IList as _n_2_t_0
from __clrclasses__.System.ComponentModel import Win32Exception as _n_3_t_0
from __clrclasses__.System.IO import Stream as _n_4_t_0
from __clrclasses__.System.IO import FileAccess as _n_4_t_1
from __clrclasses__.System.Net import IPAddress as _n_5_t_0
from __clrclasses__.System.Net import EndPoint as _n_5_t_1
from __clrclasses__.System.Net import IPEndPoint as _n_5_t_2
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_6_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_7_t_0
from __clrclasses__.System.Threading.Tasks import Task as _n_8_t_0
import typing
class AddressFamily(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AppleTalk: int
    Atm: int
    Banyan: int
    Ccitt: int
    Chaos: int
    Cluster: int
    DataKit: int
    DataLink: int
    DecNet: int
    Ecma: int
    FireFox: int
    HyperChannel: int
    Ieee12844: int
    ImpLink: int
    InterNetwork: int
    InterNetworkV6: int
    Ipx: int
    Irda: int
    Iso: int
    Lat: int
    Max: int
    NetBios: int
    NetworkDesigners: int
    NS: int
    Osi: int
    Pup: int
    Sna: int
    Unix: int
    Unknown: int
    Unspecified: int
    value__: int
    VoiceView: int
class IOControlCode(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AbsorbRouterAlert: int
    AddMulticastGroupOnInterface: int
    AddressListChange: int
    AddressListQuery: int
    AddressListSort: int
    AssociateHandle: int
    AsyncIO: int
    BindToInterface: int
    DataToRead: int
    DeleteMulticastGroupFromInterface: int
    EnableCircularQueuing: int
    Flush: int
    GetBroadcastAddress: int
    GetExtensionFunctionPointer: int
    GetGroupQos: int
    GetQos: int
    KeepAliveValues: int
    LimitBroadcasts: int
    MulticastInterface: int
    MulticastScope: int
    MultipointLoopback: int
    NamespaceChange: int
    NonBlockingIO: int
    OobDataRead: int
    QueryTargetPnpHandle: int
    ReceiveAll: int
    ReceiveAllIgmpMulticast: int
    ReceiveAllMulticast: int
    RoutingInterfaceChange: int
    RoutingInterfaceQuery: int
    SetGroupQos: int
    SetQos: int
    TranslateHandle: int
    UnicastInterface: int
    value__: int
class IPPacketInformation(_n_0_t_4):
    @property
    def Address(self) -> _n_5_t_0:"""Address { get; } -> IPAddress"""
    @property
    def Interface(self) -> int:"""Interface { get; } -> int"""
class IPProtectionLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    EdgeRestricted: int
    Restricted: int
    Unrestricted: int
    Unspecified: int
    value__: int
class IPv6MulticastOption(object):
    @property
    def Group(self) -> _n_5_t_0:"""Group { get; set; } -> IPAddress"""
    @property
    def InterfaceIndex(self) -> int:"""InterfaceIndex { get; set; } -> int"""
    def __init__(self, group: _n_5_t_0) -> IPv6MulticastOption:...
    def __init__(self, group: _n_5_t_0, ifindex: int) -> IPv6MulticastOption:...
class LingerOption(object):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def LingerTime(self) -> int:"""LingerTime { get; set; } -> int"""
    def __init__(self, enable: bool, seconds: int) -> LingerOption:...
class MulticastOption(object):
    @property
    def Group(self) -> _n_5_t_0:"""Group { get; set; } -> IPAddress"""
    @property
    def InterfaceIndex(self) -> int:"""InterfaceIndex { get; set; } -> int"""
    @property
    def LocalAddress(self) -> _n_5_t_0:"""LocalAddress { get; set; } -> IPAddress"""
    def __init__(self, group: _n_5_t_0) -> MulticastOption:...
    def __init__(self, group: _n_5_t_0, interfaceIndex: int) -> MulticastOption:...
    def __init__(self, group: _n_5_t_0, mcint: _n_5_t_0) -> MulticastOption:...
class NetworkStream(_n_4_t_0, _n_0_t_5):
    @property
    def DataAvailable(self) -> bool:"""DataAvailable { get; } -> bool"""
    def __init__(self, socket: Socket, access: _n_4_t_1, ownsSocket: bool) -> NetworkStream:...
    def __init__(self, socket: Socket, access: _n_4_t_1) -> NetworkStream:...
    def __init__(self, socket: Socket, ownsSocket: bool) -> NetworkStream:...
    def __init__(self, socket: Socket) -> NetworkStream:...
class ProtocolFamily(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AppleTalk: int
    Atm: int
    Banyan: int
    Ccitt: int
    Chaos: int
    Cluster: int
    DataKit: int
    DataLink: int
    DecNet: int
    Ecma: int
    FireFox: int
    HyperChannel: int
    Ieee12844: int
    ImpLink: int
    InterNetwork: int
    InterNetworkV6: int
    Ipx: int
    Irda: int
    Iso: int
    Lat: int
    Max: int
    NetBios: int
    NetworkDesigners: int
    NS: int
    Osi: int
    Pup: int
    Sna: int
    Unix: int
    Unknown: int
    Unspecified: int
    value__: int
    VoiceView: int
class ProtocolType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Ggp: int
    Icmp: int
    IcmpV6: int
    Idp: int
    Igmp: int
    IP: int
    IPSecAuthenticationHeader: int
    IPSecEncapsulatingSecurityPayload: int
    IPv4: int
    IPv6: int
    IPv6DestinationOptions: int
    IPv6FragmentHeader: int
    IPv6HopByHopOptions: int
    IPv6NoNextHeader: int
    IPv6RoutingHeader: int
    Ipx: int
    ND: int
    Pup: int
    Raw: int
    Spx: int
    SpxII: int
    Tcp: int
    Udp: int
    Unknown: int
    Unspecified: int
    value__: int
class SelectMode(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    SelectError: int
    SelectRead: int
    SelectWrite: int
    value__: int
class SendPacketsElement(object):
    @property
    def Buffer(self) -> _n_0_t_7[_n_0_t_6]:"""Buffer { get; } -> Array"""
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def EndOfPacket(self) -> bool:"""EndOfPacket { get; } -> bool"""
    @property
    def FilePath(self) -> str:"""FilePath { get; } -> str"""
    @property
    def Offset(self) -> int:"""Offset { get; } -> int"""
    def __init__(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, count: int, endOfPacket: bool) -> SendPacketsElement:...
    def __init__(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, count: int) -> SendPacketsElement:...
    def __init__(self, buffer: _n_0_t_7[_n_0_t_6]) -> SendPacketsElement:...
    def __init__(self, filepath: str, offset: int, count: int, endOfPacket: bool) -> SendPacketsElement:...
    def __init__(self, filepath: str, offset: int, count: int) -> SendPacketsElement:...
    def __init__(self, filepath: str) -> SendPacketsElement:...
class Socket(_n_0_t_5):
    @property
    def AddressFamily(self) -> AddressFamily:"""AddressFamily { get; } -> AddressFamily"""
    @property
    def Available(self) -> int:"""Available { get; } -> int"""
    @property
    def Blocking(self) -> bool:"""Blocking { get; set; } -> bool"""
    @property
    def Connected(self) -> bool:"""Connected { get; } -> bool"""
    @property
    def DontFragment(self) -> bool:"""DontFragment { get; set; } -> bool"""
    @property
    def DualMode(self) -> bool:"""DualMode { get; set; } -> bool"""
    @property
    def EnableBroadcast(self) -> bool:"""EnableBroadcast { get; set; } -> bool"""
    @property
    def ExclusiveAddressUse(self) -> bool:"""ExclusiveAddressUse { get; set; } -> bool"""
    @property
    def Handle(self) -> _n_0_t_8:"""Handle { get; } -> IntPtr"""
    @property
    def IsBound(self) -> bool:"""IsBound { get; } -> bool"""
    @property
    def LingerState(self) -> LingerOption:"""LingerState { get; set; } -> LingerOption"""
    @property
    def LocalEndPoint(self) -> _n_5_t_1:"""LocalEndPoint { get; } -> EndPoint"""
    @property
    def MulticastLoopback(self) -> bool:"""MulticastLoopback { get; set; } -> bool"""
    @property
    def NoDelay(self) -> bool:"""NoDelay { get; set; } -> bool"""
    @property
    def OSSupportsIPv4(self) -> bool:"""OSSupportsIPv4 { get; } -> bool"""
    @property
    def OSSupportsIPv6(self) -> bool:"""OSSupportsIPv6 { get; } -> bool"""
    @property
    def ProtocolType(self) -> ProtocolType:"""ProtocolType { get; } -> ProtocolType"""
    @property
    def ReceiveBufferSize(self) -> int:"""ReceiveBufferSize { get; set; } -> int"""
    @property
    def ReceiveTimeout(self) -> int:"""ReceiveTimeout { get; set; } -> int"""
    @property
    def RemoteEndPoint(self) -> _n_5_t_1:"""RemoteEndPoint { get; } -> EndPoint"""
    @property
    def SendBufferSize(self) -> int:"""SendBufferSize { get; set; } -> int"""
    @property
    def SendTimeout(self) -> int:"""SendTimeout { get; set; } -> int"""
    @property
    def SocketType(self) -> SocketType:"""SocketType { get; } -> SocketType"""
    @property
    def SupportsIPv4(self) -> bool:"""SupportsIPv4 { get; } -> bool"""
    @property
    def SupportsIPv6(self) -> bool:"""SupportsIPv6 { get; } -> bool"""
    @property
    def Ttl(self) -> int:"""Ttl { get; set; } -> int"""
    @property
    def UseOnlyOverlappedIO(self) -> bool:"""UseOnlyOverlappedIO { get; set; } -> bool"""
    def __init__(self, socketInformation: SocketInformation) -> Socket:...
    def __init__(self, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType) -> Socket:...
    def __init__(self, socketType: SocketType, protocolType: ProtocolType) -> Socket:...
    def Accept(self) -> Socket:...
    def AcceptAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def AcceptAsync(self, acceptSocket: Socket) -> _n_8_t_0[Socket]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def AcceptAsync(self) -> _n_8_t_0[Socket]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def BeginAccept(self, acceptSocket: Socket, receiveSize: int, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginAccept(self, receiveSize: int, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginAccept(self, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginConnect(self, addresses: _n_0_t_7[_n_5_t_0], port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginConnect(self, address: _n_5_t_0, port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginConnect(self, host: str, port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginConnect(self, remoteEP: _n_5_t_1, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginDisconnect(self, reuseSocket: bool, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginReceive(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags, errorCode: SocketError, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginReceive(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginReceive(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, errorCode: SocketError, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginReceive(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginReceiveFrom(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginReceiveMessageFrom(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags, errorCode: SocketError, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, errorCode: SocketError, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSendFile(self, fileName: str, preBuffer: _n_0_t_7[_n_0_t_6], postBuffer: _n_0_t_7[_n_0_t_6], flags: TransmitFileOptions, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSendFile(self, fileName: str, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSendTo(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def Bind(self, localEP: _n_5_t_1):...
    @staticmethod
    def CancelConnectAsync(e: SocketAsyncEventArgs):...
    def Close(self, timeout: int):...
    def Close(self):...
    def Connect(self, addresses: _n_0_t_7[_n_5_t_0], port: int):...
    def Connect(self, host: str, port: int):...
    def Connect(self, address: _n_5_t_0, port: int):...
    def Connect(self, remoteEP: _n_5_t_1):...
    @staticmethod
    def ConnectAsync(socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs) -> bool:...
    def ConnectAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def ConnectAsync(self, host: str, port: int) -> _n_8_t_0:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def ConnectAsync(self, addresses: _n_0_t_7[_n_5_t_0], port: int) -> _n_8_t_0:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def ConnectAsync(self, address: _n_5_t_0, port: int) -> _n_8_t_0:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def ConnectAsync(self, remoteEP: _n_5_t_1) -> _n_8_t_0:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def Disconnect(self, reuseSocket: bool):...
    def DisconnectAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def DuplicateAndClose(self, targetProcessId: int) -> SocketInformation:...
    def EndAccept(self, buffer: _n_0_t_7[_n_0_t_6], bytesTransferred: int, asyncResult: _n_0_t_9) -> Socket:...
    def EndAccept(self, buffer: _n_0_t_7[_n_0_t_6], asyncResult: _n_0_t_9) -> Socket:...
    def EndAccept(self, asyncResult: _n_0_t_9) -> Socket:...
    def EndConnect(self, asyncResult: _n_0_t_9):...
    def EndDisconnect(self, asyncResult: _n_0_t_9):...
    def EndReceive(self, asyncResult: _n_0_t_9, errorCode: SocketError) -> int:...
    def EndReceive(self, asyncResult: _n_0_t_9) -> int:...
    def EndReceiveFrom(self, asyncResult: _n_0_t_9, endPoint: _n_5_t_1) -> int:...
    def EndReceiveMessageFrom(self, asyncResult: _n_0_t_9, socketFlags: SocketFlags, endPoint: _n_5_t_1, ipPacketInformation: IPPacketInformation) -> int:...
    def EndSend(self, asyncResult: _n_0_t_9, errorCode: SocketError) -> int:...
    def EndSend(self, asyncResult: _n_0_t_9) -> int:...
    def EndSendFile(self, asyncResult: _n_0_t_9):...
    def EndSendTo(self, asyncResult: _n_0_t_9) -> int:...
    def GetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: int) -> _n_0_t_7[_n_0_t_6]:...
    def GetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: _n_0_t_7[_n_0_t_6]):...
    def GetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName) -> object:...
    def IOControl(self, ioControlCode: IOControlCode, optionInValue: _n_0_t_7[_n_0_t_6], optionOutValue: _n_0_t_7[_n_0_t_6]) -> int:...
    def IOControl(self, ioControlCode: int, optionInValue: _n_0_t_7[_n_0_t_6], optionOutValue: _n_0_t_7[_n_0_t_6]) -> int:...
    def Listen(self, backlog: int):...
    def Poll(self, microSeconds: int, mode: SelectMode) -> bool:...
    def Receive(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags, errorCode: SocketError) -> int:...
    def Receive(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags) -> int:...
    def Receive(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]]) -> int:...
    def Receive(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, errorCode: SocketError) -> int:...
    def Receive(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags) -> int:...
    def Receive(self, buffer: _n_0_t_7[_n_0_t_6]) -> int:...
    def Receive(self, buffer: _n_0_t_7[_n_0_t_6], socketFlags: SocketFlags) -> int:...
    def Receive(self, buffer: _n_0_t_7[_n_0_t_6], size: int, socketFlags: SocketFlags) -> int:...
    def ReceiveAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def ReceiveAsync(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags) -> _n_8_t_0[int]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def ReceiveAsync(self, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags) -> _n_8_t_0[int]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def ReceiveFrom(self, buffer: _n_0_t_7[_n_0_t_6], remoteEP: _n_5_t_1) -> int:...
    def ReceiveFrom(self, buffer: _n_0_t_7[_n_0_t_6], socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> int:...
    def ReceiveFrom(self, buffer: _n_0_t_7[_n_0_t_6], size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> int:...
    def ReceiveFrom(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> int:...
    def ReceiveFromAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def ReceiveFromAsync(self, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags, remoteEndPoint: _n_5_t_1) -> _n_8_t_0[SocketReceiveFromResult]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def ReceiveMessageFrom(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1, ipPacketInformation: IPPacketInformation) -> int:...
    def ReceiveMessageFromAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def ReceiveMessageFromAsync(self, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags, remoteEndPoint: _n_5_t_1) -> _n_8_t_0[SocketReceiveMessageFromResult]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    @staticmethod
    def Select(checkRead: _n_1_t_0, checkWrite: _n_1_t_0, checkError: _n_1_t_0, microSeconds: int):...
    def Send(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, errorCode: SocketError) -> int:...
    def Send(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags) -> int:...
    def Send(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags, errorCode: SocketError) -> int:...
    def Send(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags) -> int:...
    def Send(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]]) -> int:...
    def Send(self, buffer: _n_0_t_7[_n_0_t_6]) -> int:...
    def Send(self, buffer: _n_0_t_7[_n_0_t_6], socketFlags: SocketFlags) -> int:...
    def Send(self, buffer: _n_0_t_7[_n_0_t_6], size: int, socketFlags: SocketFlags) -> int:...
    def SendAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def SendAsync(self, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags) -> _n_8_t_0[int]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def SendAsync(self, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags) -> _n_8_t_0[int]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def SendFile(self, fileName: str, preBuffer: _n_0_t_7[_n_0_t_6], postBuffer: _n_0_t_7[_n_0_t_6], flags: TransmitFileOptions):...
    def SendFile(self, fileName: str):...
    def SendPacketsAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def SendTo(self, buffer: _n_0_t_7[_n_0_t_6], remoteEP: _n_5_t_1) -> int:...
    def SendTo(self, buffer: _n_0_t_7[_n_0_t_6], socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> int:...
    def SendTo(self, buffer: _n_0_t_7[_n_0_t_6], size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> int:...
    def SendTo(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, size: int, socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> int:...
    def SendToAsync(self, e: SocketAsyncEventArgs) -> bool:...
    def SendToAsync(self, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> _n_8_t_0[int]:
        """Extension from: System.Net.Sockets.SocketTaskExtensions"""
    def SetIPProtectionLevel(self, level: IPProtectionLevel):...
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: object):...
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: bool):...
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: _n_0_t_7[_n_0_t_6]):...
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: int):...
    def Shutdown(self, how: SocketShutdown):...
class SocketAsyncEventArgs(_n_0_t_12, _n_0_t_5):
    @property
    def AcceptSocket(self) -> Socket:"""AcceptSocket { get; set; } -> Socket"""
    @property
    def Buffer(self) -> _n_0_t_7[_n_0_t_6]:"""Buffer { get; } -> Array"""
    @property
    def BufferList(self) -> _n_2_t_0[_n_0_t_11[_n_0_t_6]]:"""BufferList { get; set; } -> IList"""
    @property
    def BytesTransferred(self) -> int:"""BytesTransferred { get; } -> int"""
    @property
    def ConnectByNameError(self) -> _n_0_t_14:"""ConnectByNameError { get; } -> Exception"""
    @property
    def ConnectSocket(self) -> Socket:"""ConnectSocket { get; } -> Socket"""
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def DisconnectReuseSocket(self) -> bool:"""DisconnectReuseSocket { get; set; } -> bool"""
    @property
    def LastOperation(self) -> SocketAsyncOperation:"""LastOperation { get; } -> SocketAsyncOperation"""
    @property
    def Offset(self) -> int:"""Offset { get; } -> int"""
    @property
    def ReceiveMessageFromPacketInfo(self) -> IPPacketInformation:"""ReceiveMessageFromPacketInfo { get; } -> IPPacketInformation"""
    @property
    def RemoteEndPoint(self) -> _n_5_t_1:"""RemoteEndPoint { get; set; } -> EndPoint"""
    @property
    def SendPacketsElements(self) -> _n_0_t_7[SendPacketsElement]:"""SendPacketsElements { get; set; } -> Array"""
    @property
    def SendPacketsFlags(self) -> TransmitFileOptions:"""SendPacketsFlags { get; set; } -> TransmitFileOptions"""
    @property
    def SendPacketsSendSize(self) -> int:"""SendPacketsSendSize { get; set; } -> int"""
    @property
    def SocketClientAccessPolicyProtocol(self) -> SocketClientAccessPolicyProtocol:"""SocketClientAccessPolicyProtocol { get; set; } -> SocketClientAccessPolicyProtocol"""
    @property
    def SocketError(self) -> SocketError:"""SocketError { get; set; } -> SocketError"""
    @property
    def SocketFlags(self) -> SocketFlags:"""SocketFlags { get; set; } -> SocketFlags"""
    @property
    def UserToken(self) -> object:"""UserToken { get; set; } -> object"""
    @property
    def Completed(self) -> _n_0_t_13[SocketAsyncEventArgs]:
        """Completed Event: EventHandler"""
    def __init__(self) -> SocketAsyncEventArgs:...
    def SetBuffer(self, offset: int, count: int):...
    def SetBuffer(self, buffer: _n_0_t_7[_n_0_t_6], offset: int, count: int):...
class SocketAsyncOperation(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Accept: int
    Connect: int
    Disconnect: int
    _None: int
    Receive: int
    ReceiveFrom: int
    ReceiveMessageFrom: int
    Send: int
    SendPackets: int
    SendTo: int
    value__: int
class SocketClientAccessPolicyProtocol(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Http: int
    Tcp: int
    value__: int
class SocketError(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AccessDenied: int
    AddressAlreadyInUse: int
    AddressFamilyNotSupported: int
    AddressNotAvailable: int
    AlreadyInProgress: int
    ConnectionAborted: int
    ConnectionRefused: int
    ConnectionReset: int
    DestinationAddressRequired: int
    Disconnecting: int
    Fault: int
    HostDown: int
    HostNotFound: int
    HostUnreachable: int
    InProgress: int
    Interrupted: int
    InvalidArgument: int
    IOPending: int
    IsConnected: int
    MessageSize: int
    NetworkDown: int
    NetworkReset: int
    NetworkUnreachable: int
    NoBufferSpaceAvailable: int
    NoData: int
    NoRecovery: int
    NotConnected: int
    NotInitialized: int
    NotSocket: int
    OperationAborted: int
    OperationNotSupported: int
    ProcessLimit: int
    ProtocolFamilyNotSupported: int
    ProtocolNotSupported: int
    ProtocolOption: int
    ProtocolType: int
    Shutdown: int
    SocketError: int
    SocketNotSupported: int
    Success: int
    SystemNotReady: int
    TimedOut: int
    TooManyOpenSockets: int
    TryAgain: int
    TypeNotFound: int
    value__: int
    VersionNotSupported: int
    WouldBlock: int
class SocketException(_n_3_t_0, _n_7_t_0, _n_6_t_0):
    @property
    def SocketErrorCode(self) -> SocketError:"""SocketErrorCode { get; } -> SocketError"""
    def __init__(self, errorCode: int) -> SocketException:...
    def __init__(self) -> SocketException:...
class SocketFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Broadcast: int
    ControlDataTruncated: int
    DontRoute: int
    MaxIOVectorLength: int
    Multicast: int
    _None: int
    OutOfBand: int
    Partial: int
    Peek: int
    Truncated: int
    value__: int
class SocketInformation(_n_0_t_4):
    @property
    def Options(self) -> SocketInformationOptions:"""Options { get; set; } -> SocketInformationOptions"""
    @property
    def ProtocolInformation(self) -> _n_0_t_7[_n_0_t_6]:"""ProtocolInformation { get; set; } -> Array"""
class SocketInformationOptions(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Connected: int
    Listening: int
    NonBlocking: int
    UseOnlyOverlappedIO: int
    value__: int
class SocketOptionLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    IP: int
    IPv6: int
    Socket: int
    Tcp: int
    Udp: int
    value__: int
class SocketOptionName(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AcceptConnection: int
    AddMembership: int
    AddSourceMembership: int
    BlockSource: int
    Broadcast: int
    BsdUrgent: int
    ChecksumCoverage: int
    Debug: int
    DontFragment: int
    DontLinger: int
    DontRoute: int
    DropMembership: int
    DropSourceMembership: int
    Error: int
    ExclusiveAddressUse: int
    Expedited: int
    HeaderIncluded: int
    HopLimit: int
    IPOptions: int
    IPProtectionLevel: int
    IpTimeToLive: int
    IPv6Only: int
    KeepAlive: int
    Linger: int
    MaxConnections: int
    MulticastInterface: int
    MulticastLoopback: int
    MulticastTimeToLive: int
    NoChecksum: int
    NoDelay: int
    OutOfBandInline: int
    PacketInformation: int
    ReceiveBuffer: int
    ReceiveLowWater: int
    ReceiveTimeout: int
    ReuseAddress: int
    ReuseUnicastPort: int
    SendBuffer: int
    SendLowWater: int
    SendTimeout: int
    Type: int
    TypeOfService: int
    UnblockSource: int
    UpdateAcceptContext: int
    UpdateConnectContext: int
    UseLoopback: int
    value__: int
class SocketReceiveFromResult(_n_0_t_4):
    ReceivedBytes: int
    RemoteEndPoint: int
class SocketReceiveMessageFromResult(_n_0_t_4):
    PacketInformation: int
    ReceivedBytes: int
    RemoteEndPoint: int
    SocketFlags: int
class SocketShutdown(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Both: int
    Receive: int
    Send: int
    value__: int
class SocketTaskExtensions(object):
    @staticmethod
    def AcceptAsync(socket: Socket, acceptSocket: Socket) -> _n_8_t_0[Socket]:...
    @staticmethod
    def AcceptAsync(socket: Socket) -> _n_8_t_0[Socket]:...
    @staticmethod
    def ConnectAsync(socket: Socket, host: str, port: int) -> _n_8_t_0:...
    @staticmethod
    def ConnectAsync(socket: Socket, addresses: _n_0_t_7[_n_5_t_0], port: int) -> _n_8_t_0:...
    @staticmethod
    def ConnectAsync(socket: Socket, address: _n_5_t_0, port: int) -> _n_8_t_0:...
    @staticmethod
    def ConnectAsync(socket: Socket, remoteEP: _n_5_t_1) -> _n_8_t_0:...
    @staticmethod
    def ReceiveAsync(socket: Socket, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags) -> _n_8_t_0[int]:...
    @staticmethod
    def ReceiveAsync(socket: Socket, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags) -> _n_8_t_0[int]:...
    @staticmethod
    def ReceiveFromAsync(socket: Socket, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags, remoteEndPoint: _n_5_t_1) -> _n_8_t_0[SocketReceiveFromResult]:...
    @staticmethod
    def ReceiveMessageFromAsync(socket: Socket, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags, remoteEndPoint: _n_5_t_1) -> _n_8_t_0[SocketReceiveMessageFromResult]:...
    @staticmethod
    def SendAsync(socket: Socket, buffers: _n_2_t_0[_n_0_t_11[_n_0_t_6]], socketFlags: SocketFlags) -> _n_8_t_0[int]:...
    @staticmethod
    def SendAsync(socket: Socket, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags) -> _n_8_t_0[int]:...
    @staticmethod
    def SendToAsync(socket: Socket, buffer: _n_0_t_11[_n_0_t_6], socketFlags: SocketFlags, remoteEP: _n_5_t_1) -> _n_8_t_0[int]:...
class SocketType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Dgram: int
    Raw: int
    Rdm: int
    Seqpacket: int
    Stream: int
    Unknown: int
    value__: int
class TcpClient(_n_0_t_5):
    @property
    def Available(self) -> int:"""Available { get; } -> int"""
    @property
    def Client(self) -> Socket:"""Client { get; set; } -> Socket"""
    @property
    def Connected(self) -> bool:"""Connected { get; } -> bool"""
    @property
    def ExclusiveAddressUse(self) -> bool:"""ExclusiveAddressUse { get; set; } -> bool"""
    @property
    def LingerState(self) -> LingerOption:"""LingerState { get; set; } -> LingerOption"""
    @property
    def NoDelay(self) -> bool:"""NoDelay { get; set; } -> bool"""
    @property
    def ReceiveBufferSize(self) -> int:"""ReceiveBufferSize { get; set; } -> int"""
    @property
    def ReceiveTimeout(self) -> int:"""ReceiveTimeout { get; set; } -> int"""
    @property
    def SendBufferSize(self) -> int:"""SendBufferSize { get; set; } -> int"""
    @property
    def SendTimeout(self) -> int:"""SendTimeout { get; set; } -> int"""
    def __init__(self, hostname: str, port: int) -> TcpClient:...
    def __init__(self, family: AddressFamily) -> TcpClient:...
    def __init__(self) -> TcpClient:...
    def __init__(self, localEP: _n_5_t_2) -> TcpClient:...
    def BeginConnect(self, addresses: _n_0_t_7[_n_5_t_0], port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginConnect(self, address: _n_5_t_0, port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginConnect(self, host: str, port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def Close(self):...
    def Connect(self, ipAddresses: _n_0_t_7[_n_5_t_0], port: int):...
    def Connect(self, remoteEP: _n_5_t_2):...
    def Connect(self, address: _n_5_t_0, port: int):...
    def Connect(self, hostname: str, port: int):...
    def ConnectAsync(self, addresses: _n_0_t_7[_n_5_t_0], port: int) -> _n_8_t_0:...
    def ConnectAsync(self, host: str, port: int) -> _n_8_t_0:...
    def ConnectAsync(self, address: _n_5_t_0, port: int) -> _n_8_t_0:...
    def EndConnect(self, asyncResult: _n_0_t_9):...
    def GetStream(self) -> NetworkStream:...
class TcpListener(object):
    @property
    def ExclusiveAddressUse(self) -> bool:"""ExclusiveAddressUse { get; set; } -> bool"""
    @property
    def LocalEndpoint(self) -> _n_5_t_1:"""LocalEndpoint { get; } -> EndPoint"""
    @property
    def Server(self) -> Socket:"""Server { get; } -> Socket"""
    def __init__(self, port: int) -> TcpListener:...
    def __init__(self, localaddr: _n_5_t_0, port: int) -> TcpListener:...
    def __init__(self, localEP: _n_5_t_2) -> TcpListener:...
    def AcceptSocket(self) -> Socket:...
    def AcceptSocketAsync(self) -> _n_8_t_0[Socket]:...
    def AcceptTcpClient(self) -> TcpClient:...
    def AcceptTcpClientAsync(self) -> _n_8_t_0[TcpClient]:...
    def AllowNatTraversal(self, allowed: bool):...
    def BeginAcceptSocket(self, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginAcceptTcpClient(self, callback: _n_0_t_10, state: object) -> _n_0_t_9:...
    @staticmethod
    def Create(port: int) -> TcpListener:...
    def EndAcceptSocket(self, asyncResult: _n_0_t_9) -> Socket:...
    def EndAcceptTcpClient(self, asyncResult: _n_0_t_9) -> TcpClient:...
    def Pending(self) -> bool:...
    def Start(self, backlog: int):...
    def Start(self):...
    def Stop(self):...
class TransmitFileOptions(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Disconnect: int
    ReuseSocket: int
    UseDefaultWorkerThread: int
    UseKernelApc: int
    UseSystemThread: int
    value__: int
    WriteBehind: int
class UdpClient(_n_0_t_5):
    @property
    def Available(self) -> int:"""Available { get; } -> int"""
    @property
    def Client(self) -> Socket:"""Client { get; set; } -> Socket"""
    @property
    def DontFragment(self) -> bool:"""DontFragment { get; set; } -> bool"""
    @property
    def EnableBroadcast(self) -> bool:"""EnableBroadcast { get; set; } -> bool"""
    @property
    def ExclusiveAddressUse(self) -> bool:"""ExclusiveAddressUse { get; set; } -> bool"""
    @property
    def MulticastLoopback(self) -> bool:"""MulticastLoopback { get; set; } -> bool"""
    @property
    def Ttl(self) -> int:"""Ttl { get; set; } -> int"""
    def __init__(self, hostname: str, port: int) -> UdpClient:...
    def __init__(self, localEP: _n_5_t_2) -> UdpClient:...
    def __init__(self, port: int, family: AddressFamily) -> UdpClient:...
    def __init__(self, port: int) -> UdpClient:...
    def __init__(self, family: AddressFamily) -> UdpClient:...
    def __init__(self) -> UdpClient:...
    def AllowNatTraversal(self, allowed: bool):...
    def BeginReceive(self, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, datagram: _n_0_t_7[_n_0_t_6], bytes: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, datagram: _n_0_t_7[_n_0_t_6], bytes: int, hostname: str, port: int, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def BeginSend(self, datagram: _n_0_t_7[_n_0_t_6], bytes: int, endPoint: _n_5_t_2, requestCallback: _n_0_t_10, state: object) -> _n_0_t_9:...
    def Close(self):...
    def Connect(self, endPoint: _n_5_t_2):...
    def Connect(self, addr: _n_5_t_0, port: int):...
    def Connect(self, hostname: str, port: int):...
    def DropMulticastGroup(self, multicastAddr: _n_5_t_0, ifindex: int):...
    def DropMulticastGroup(self, multicastAddr: _n_5_t_0):...
    def EndReceive(self, asyncResult: _n_0_t_9, remoteEP: _n_5_t_2) -> _n_0_t_7[_n_0_t_6]:...
    def EndSend(self, asyncResult: _n_0_t_9) -> int:...
    def JoinMulticastGroup(self, multicastAddr: _n_5_t_0, timeToLive: int):...
    def JoinMulticastGroup(self, ifindex: int, multicastAddr: _n_5_t_0):...
    def JoinMulticastGroup(self, multicastAddr: _n_5_t_0, localAddress: _n_5_t_0):...
    def JoinMulticastGroup(self, multicastAddr: _n_5_t_0):...
    def Receive(self, remoteEP: _n_5_t_2) -> _n_0_t_7[_n_0_t_6]:...
    def ReceiveAsync(self) -> _n_8_t_0[UdpReceiveResult]:...
    def Send(self, dgram: _n_0_t_7[_n_0_t_6], bytes: int) -> int:...
    def Send(self, dgram: _n_0_t_7[_n_0_t_6], bytes: int, hostname: str, port: int) -> int:...
    def Send(self, dgram: _n_0_t_7[_n_0_t_6], bytes: int, endPoint: _n_5_t_2) -> int:...
    def SendAsync(self, datagram: _n_0_t_7[_n_0_t_6], bytes: int, hostname: str, port: int) -> _n_8_t_0[int]:...
    def SendAsync(self, datagram: _n_0_t_7[_n_0_t_6], bytes: int, endPoint: _n_5_t_2) -> _n_8_t_0[int]:...
    def SendAsync(self, datagram: _n_0_t_7[_n_0_t_6], bytes: int) -> _n_8_t_0[int]:...
class UdpReceiveResult(_n_0_t_4, _n_0_t_15[UdpReceiveResult]):
    @property
    def Buffer(self) -> _n_0_t_7[_n_0_t_6]:"""Buffer { get; } -> Array"""
    @property
    def RemoteEndPoint(self) -> _n_5_t_2:"""RemoteEndPoint { get; } -> IPEndPoint"""
    def __init__(self, buffer: _n_0_t_7[_n_0_t_6], remoteEndPoint: _n_5_t_2) -> UdpReceiveResult:...
