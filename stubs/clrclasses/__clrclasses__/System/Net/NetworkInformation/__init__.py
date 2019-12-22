from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import IAsyncResult as _n_0_t_4
from __clrclasses__.System import AsyncCallback as _n_0_t_5
from __clrclasses__.System import Array as _n_0_t_6
from __clrclasses__.System import MulticastDelegate as _n_0_t_7
from __clrclasses__.System import ICloneable as _n_0_t_8
from __clrclasses__.System import IntPtr as _n_0_t_9
from __clrclasses__.System import EventArgs as _n_0_t_10
from __clrclasses__.System import Byte as _n_0_t_11
from __clrclasses__.System import InvalidOperationException as _n_0_t_12
from __clrclasses__.System import Exception as _n_0_t_13
from __clrclasses__.System.Collections.Generic import ICollection as _n_1_t_0
from __clrclasses__.System.ComponentModel import Win32Exception as _n_2_t_0
from __clrclasses__.System.ComponentModel import Component as _n_2_t_1
from __clrclasses__.System.ComponentModel import IComponent as _n_2_t_2
from __clrclasses__.System.ComponentModel import AsyncCompletedEventArgs as _n_2_t_3
from __clrclasses__.System.Net import IPAddress as _n_3_t_0
from __clrclasses__.System.Net import IPEndPoint as _n_3_t_1
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_4_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_4_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
from __clrclasses__.System.Security import CodeAccessPermission as _n_6_t_0
from __clrclasses__.System.Security import IPermission as _n_6_t_1
from __clrclasses__.System.Security import IStackWalk as _n_6_t_2
from __clrclasses__.System.Security.Permissions import IUnrestrictedPermission as _n_7_t_0
from __clrclasses__.System.Security.Permissions import PermissionState as _n_7_t_1
from __clrclasses__.System.Security.Permissions import CodeAccessSecurityAttribute as _n_7_t_2
from __clrclasses__.System.Security.Permissions import SecurityAction as _n_7_t_3
from __clrclasses__.System.Threading.Tasks import Task as _n_8_t_0
import typing
class DuplicateAddressDetectionState(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Deprecated: int
    Duplicate: int
    Invalid: int
    Preferred: int
    Tentative: int
    value__: int
class GatewayIPAddressInformation(object):
    @property
    def Address(self) -> _n_3_t_0:"""Address { get; } -> IPAddress"""
class GatewayIPAddressInformationCollection(_n_1_t_0[GatewayIPAddressInformation], typing.Iterable[GatewayIPAddressInformation]):
    @property
    def Item(self) -> GatewayIPAddressInformation:"""Item { get; } -> GatewayIPAddressInformation"""
class IcmpV4Statistics(object):
    @property
    def AddressMaskRepliesReceived(self) -> int:"""AddressMaskRepliesReceived { get; } -> int"""
    @property
    def AddressMaskRepliesSent(self) -> int:"""AddressMaskRepliesSent { get; } -> int"""
    @property
    def AddressMaskRequestsReceived(self) -> int:"""AddressMaskRequestsReceived { get; } -> int"""
    @property
    def AddressMaskRequestsSent(self) -> int:"""AddressMaskRequestsSent { get; } -> int"""
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:"""DestinationUnreachableMessagesReceived { get; } -> int"""
    @property
    def DestinationUnreachableMessagesSent(self) -> int:"""DestinationUnreachableMessagesSent { get; } -> int"""
    @property
    def EchoRepliesReceived(self) -> int:"""EchoRepliesReceived { get; } -> int"""
    @property
    def EchoRepliesSent(self) -> int:"""EchoRepliesSent { get; } -> int"""
    @property
    def EchoRequestsReceived(self) -> int:"""EchoRequestsReceived { get; } -> int"""
    @property
    def EchoRequestsSent(self) -> int:"""EchoRequestsSent { get; } -> int"""
    @property
    def ErrorsReceived(self) -> int:"""ErrorsReceived { get; } -> int"""
    @property
    def ErrorsSent(self) -> int:"""ErrorsSent { get; } -> int"""
    @property
    def MessagesReceived(self) -> int:"""MessagesReceived { get; } -> int"""
    @property
    def MessagesSent(self) -> int:"""MessagesSent { get; } -> int"""
    @property
    def ParameterProblemsReceived(self) -> int:"""ParameterProblemsReceived { get; } -> int"""
    @property
    def ParameterProblemsSent(self) -> int:"""ParameterProblemsSent { get; } -> int"""
    @property
    def RedirectsReceived(self) -> int:"""RedirectsReceived { get; } -> int"""
    @property
    def RedirectsSent(self) -> int:"""RedirectsSent { get; } -> int"""
    @property
    def SourceQuenchesReceived(self) -> int:"""SourceQuenchesReceived { get; } -> int"""
    @property
    def SourceQuenchesSent(self) -> int:"""SourceQuenchesSent { get; } -> int"""
    @property
    def TimeExceededMessagesReceived(self) -> int:"""TimeExceededMessagesReceived { get; } -> int"""
    @property
    def TimeExceededMessagesSent(self) -> int:"""TimeExceededMessagesSent { get; } -> int"""
    @property
    def TimestampRepliesReceived(self) -> int:"""TimestampRepliesReceived { get; } -> int"""
    @property
    def TimestampRepliesSent(self) -> int:"""TimestampRepliesSent { get; } -> int"""
    @property
    def TimestampRequestsReceived(self) -> int:"""TimestampRequestsReceived { get; } -> int"""
    @property
    def TimestampRequestsSent(self) -> int:"""TimestampRequestsSent { get; } -> int"""
class IcmpV6Statistics(object):
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:"""DestinationUnreachableMessagesReceived { get; } -> int"""
    @property
    def DestinationUnreachableMessagesSent(self) -> int:"""DestinationUnreachableMessagesSent { get; } -> int"""
    @property
    def EchoRepliesReceived(self) -> int:"""EchoRepliesReceived { get; } -> int"""
    @property
    def EchoRepliesSent(self) -> int:"""EchoRepliesSent { get; } -> int"""
    @property
    def EchoRequestsReceived(self) -> int:"""EchoRequestsReceived { get; } -> int"""
    @property
    def EchoRequestsSent(self) -> int:"""EchoRequestsSent { get; } -> int"""
    @property
    def ErrorsReceived(self) -> int:"""ErrorsReceived { get; } -> int"""
    @property
    def ErrorsSent(self) -> int:"""ErrorsSent { get; } -> int"""
    @property
    def MembershipQueriesReceived(self) -> int:"""MembershipQueriesReceived { get; } -> int"""
    @property
    def MembershipQueriesSent(self) -> int:"""MembershipQueriesSent { get; } -> int"""
    @property
    def MembershipReductionsReceived(self) -> int:"""MembershipReductionsReceived { get; } -> int"""
    @property
    def MembershipReductionsSent(self) -> int:"""MembershipReductionsSent { get; } -> int"""
    @property
    def MembershipReportsReceived(self) -> int:"""MembershipReportsReceived { get; } -> int"""
    @property
    def MembershipReportsSent(self) -> int:"""MembershipReportsSent { get; } -> int"""
    @property
    def MessagesReceived(self) -> int:"""MessagesReceived { get; } -> int"""
    @property
    def MessagesSent(self) -> int:"""MessagesSent { get; } -> int"""
    @property
    def NeighborAdvertisementsReceived(self) -> int:"""NeighborAdvertisementsReceived { get; } -> int"""
    @property
    def NeighborAdvertisementsSent(self) -> int:"""NeighborAdvertisementsSent { get; } -> int"""
    @property
    def NeighborSolicitsReceived(self) -> int:"""NeighborSolicitsReceived { get; } -> int"""
    @property
    def NeighborSolicitsSent(self) -> int:"""NeighborSolicitsSent { get; } -> int"""
    @property
    def PacketTooBigMessagesReceived(self) -> int:"""PacketTooBigMessagesReceived { get; } -> int"""
    @property
    def PacketTooBigMessagesSent(self) -> int:"""PacketTooBigMessagesSent { get; } -> int"""
    @property
    def ParameterProblemsReceived(self) -> int:"""ParameterProblemsReceived { get; } -> int"""
    @property
    def ParameterProblemsSent(self) -> int:"""ParameterProblemsSent { get; } -> int"""
    @property
    def RedirectsReceived(self) -> int:"""RedirectsReceived { get; } -> int"""
    @property
    def RedirectsSent(self) -> int:"""RedirectsSent { get; } -> int"""
    @property
    def RouterAdvertisementsReceived(self) -> int:"""RouterAdvertisementsReceived { get; } -> int"""
    @property
    def RouterAdvertisementsSent(self) -> int:"""RouterAdvertisementsSent { get; } -> int"""
    @property
    def RouterSolicitsReceived(self) -> int:"""RouterSolicitsReceived { get; } -> int"""
    @property
    def RouterSolicitsSent(self) -> int:"""RouterSolicitsSent { get; } -> int"""
    @property
    def TimeExceededMessagesReceived(self) -> int:"""TimeExceededMessagesReceived { get; } -> int"""
    @property
    def TimeExceededMessagesSent(self) -> int:"""TimeExceededMessagesSent { get; } -> int"""
class IPAddressCollection(_n_1_t_0[_n_3_t_0], typing.Iterable[_n_3_t_0]):
    @property
    def Item(self) -> _n_3_t_0:"""Item { get; } -> IPAddress"""
class IPAddressInformation(object):
    @property
    def Address(self) -> _n_3_t_0:"""Address { get; } -> IPAddress"""
    @property
    def IsDnsEligible(self) -> bool:"""IsDnsEligible { get; } -> bool"""
    @property
    def IsTransient(self) -> bool:"""IsTransient { get; } -> bool"""
class IPAddressInformationCollection(_n_1_t_0[IPAddressInformation], typing.Iterable[IPAddressInformation]):
    @property
    def Item(self) -> IPAddressInformation:"""Item { get; } -> IPAddressInformation"""
class IPGlobalProperties(object):
    @property
    def DhcpScopeName(self) -> str:"""DhcpScopeName { get; } -> str"""
    @property
    def DomainName(self) -> str:"""DomainName { get; } -> str"""
    @property
    def HostName(self) -> str:"""HostName { get; } -> str"""
    @property
    def IsWinsProxy(self) -> bool:"""IsWinsProxy { get; } -> bool"""
    @property
    def NodeType(self) -> NetBiosNodeType:"""NodeType { get; } -> NetBiosNodeType"""
    def BeginGetUnicastAddresses(self, callback: _n_0_t_5, state: object) -> _n_0_t_4:...
    def EndGetUnicastAddresses(self, asyncResult: _n_0_t_4) -> UnicastIPAddressInformationCollection:...
    def GetActiveTcpConnections(self) -> _n_0_t_6[TcpConnectionInformation]:...
    def GetActiveTcpListeners(self) -> _n_0_t_6[_n_3_t_1]:...
    def GetActiveUdpListeners(self) -> _n_0_t_6[_n_3_t_1]:...
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics:...
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics:...
    @staticmethod
    def GetIPGlobalProperties() -> IPGlobalProperties:...
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics:...
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics:...
    def GetTcpIPv4Statistics(self) -> TcpStatistics:...
    def GetTcpIPv6Statistics(self) -> TcpStatistics:...
    def GetUdpIPv4Statistics(self) -> UdpStatistics:...
    def GetUdpIPv6Statistics(self) -> UdpStatistics:...
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection:...
    def GetUnicastAddressesAsync(self) -> _n_8_t_0[UnicastIPAddressInformationCollection]:...
class IPGlobalStatistics(object):
    @property
    def DefaultTtl(self) -> int:"""DefaultTtl { get; } -> int"""
    @property
    def ForwardingEnabled(self) -> bool:"""ForwardingEnabled { get; } -> bool"""
    @property
    def NumberOfInterfaces(self) -> int:"""NumberOfInterfaces { get; } -> int"""
    @property
    def NumberOfIPAddresses(self) -> int:"""NumberOfIPAddresses { get; } -> int"""
    @property
    def NumberOfRoutes(self) -> int:"""NumberOfRoutes { get; } -> int"""
    @property
    def OutputPacketRequests(self) -> int:"""OutputPacketRequests { get; } -> int"""
    @property
    def OutputPacketRoutingDiscards(self) -> int:"""OutputPacketRoutingDiscards { get; } -> int"""
    @property
    def OutputPacketsDiscarded(self) -> int:"""OutputPacketsDiscarded { get; } -> int"""
    @property
    def OutputPacketsWithNoRoute(self) -> int:"""OutputPacketsWithNoRoute { get; } -> int"""
    @property
    def PacketFragmentFailures(self) -> int:"""PacketFragmentFailures { get; } -> int"""
    @property
    def PacketReassembliesRequired(self) -> int:"""PacketReassembliesRequired { get; } -> int"""
    @property
    def PacketReassemblyFailures(self) -> int:"""PacketReassemblyFailures { get; } -> int"""
    @property
    def PacketReassemblyTimeout(self) -> int:"""PacketReassemblyTimeout { get; } -> int"""
    @property
    def PacketsFragmented(self) -> int:"""PacketsFragmented { get; } -> int"""
    @property
    def PacketsReassembled(self) -> int:"""PacketsReassembled { get; } -> int"""
    @property
    def ReceivedPackets(self) -> int:"""ReceivedPackets { get; } -> int"""
    @property
    def ReceivedPacketsDelivered(self) -> int:"""ReceivedPacketsDelivered { get; } -> int"""
    @property
    def ReceivedPacketsDiscarded(self) -> int:"""ReceivedPacketsDiscarded { get; } -> int"""
    @property
    def ReceivedPacketsForwarded(self) -> int:"""ReceivedPacketsForwarded { get; } -> int"""
    @property
    def ReceivedPacketsWithAddressErrors(self) -> int:"""ReceivedPacketsWithAddressErrors { get; } -> int"""
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> int:"""ReceivedPacketsWithHeadersErrors { get; } -> int"""
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> int:"""ReceivedPacketsWithUnknownProtocol { get; } -> int"""
class IPInterfaceProperties(object):
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection:"""AnycastAddresses { get; } -> IPAddressInformationCollection"""
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection:"""DhcpServerAddresses { get; } -> IPAddressCollection"""
    @property
    def DnsAddresses(self) -> IPAddressCollection:"""DnsAddresses { get; } -> IPAddressCollection"""
    @property
    def DnsSuffix(self) -> str:"""DnsSuffix { get; } -> str"""
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection:"""GatewayAddresses { get; } -> GatewayIPAddressInformationCollection"""
    @property
    def IsDnsEnabled(self) -> bool:"""IsDnsEnabled { get; } -> bool"""
    @property
    def IsDynamicDnsEnabled(self) -> bool:"""IsDynamicDnsEnabled { get; } -> bool"""
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection:"""MulticastAddresses { get; } -> MulticastIPAddressInformationCollection"""
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection:"""UnicastAddresses { get; } -> UnicastIPAddressInformationCollection"""
    @property
    def WinsServersAddresses(self) -> IPAddressCollection:"""WinsServersAddresses { get; } -> IPAddressCollection"""
    def GetIPv4Properties(self) -> IPv4InterfaceProperties:...
    def GetIPv6Properties(self) -> IPv6InterfaceProperties:...
class IPInterfaceStatistics(object):
    @property
    def BytesReceived(self) -> int:"""BytesReceived { get; } -> int"""
    @property
    def BytesSent(self) -> int:"""BytesSent { get; } -> int"""
    @property
    def IncomingPacketsDiscarded(self) -> int:"""IncomingPacketsDiscarded { get; } -> int"""
    @property
    def IncomingPacketsWithErrors(self) -> int:"""IncomingPacketsWithErrors { get; } -> int"""
    @property
    def IncomingUnknownProtocolPackets(self) -> int:"""IncomingUnknownProtocolPackets { get; } -> int"""
    @property
    def NonUnicastPacketsReceived(self) -> int:"""NonUnicastPacketsReceived { get; } -> int"""
    @property
    def NonUnicastPacketsSent(self) -> int:"""NonUnicastPacketsSent { get; } -> int"""
    @property
    def OutgoingPacketsDiscarded(self) -> int:"""OutgoingPacketsDiscarded { get; } -> int"""
    @property
    def OutgoingPacketsWithErrors(self) -> int:"""OutgoingPacketsWithErrors { get; } -> int"""
    @property
    def OutputQueueLength(self) -> int:"""OutputQueueLength { get; } -> int"""
    @property
    def UnicastPacketsReceived(self) -> int:"""UnicastPacketsReceived { get; } -> int"""
    @property
    def UnicastPacketsSent(self) -> int:"""UnicastPacketsSent { get; } -> int"""
class IPStatus(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    BadDestination: int
    BadHeader: int
    BadOption: int
    BadRoute: int
    DestinationHostUnreachable: int
    DestinationNetworkUnreachable: int
    DestinationPortUnreachable: int
    DestinationProhibited: int
    DestinationProtocolUnreachable: int
    DestinationScopeMismatch: int
    DestinationUnreachable: int
    HardwareError: int
    IcmpError: int
    NoResources: int
    PacketTooBig: int
    ParameterProblem: int
    SourceQuench: int
    Success: int
    TimedOut: int
    TimeExceeded: int
    TtlExpired: int
    TtlReassemblyTimeExceeded: int
    Unknown: int
    UnrecognizedNextHeader: int
    value__: int
class IPv4InterfaceProperties(object):
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool:"""IsAutomaticPrivateAddressingActive { get; } -> bool"""
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool:"""IsAutomaticPrivateAddressingEnabled { get; } -> bool"""
    @property
    def IsDhcpEnabled(self) -> bool:"""IsDhcpEnabled { get; } -> bool"""
    @property
    def IsForwardingEnabled(self) -> bool:"""IsForwardingEnabled { get; } -> bool"""
    @property
    def Mtu(self) -> int:"""Mtu { get; } -> int"""
    @property
    def UsesWins(self) -> bool:"""UsesWins { get; } -> bool"""
class IPv4InterfaceStatistics(object):
    @property
    def BytesReceived(self) -> int:"""BytesReceived { get; } -> int"""
    @property
    def BytesSent(self) -> int:"""BytesSent { get; } -> int"""
    @property
    def IncomingPacketsDiscarded(self) -> int:"""IncomingPacketsDiscarded { get; } -> int"""
    @property
    def IncomingPacketsWithErrors(self) -> int:"""IncomingPacketsWithErrors { get; } -> int"""
    @property
    def IncomingUnknownProtocolPackets(self) -> int:"""IncomingUnknownProtocolPackets { get; } -> int"""
    @property
    def NonUnicastPacketsReceived(self) -> int:"""NonUnicastPacketsReceived { get; } -> int"""
    @property
    def NonUnicastPacketsSent(self) -> int:"""NonUnicastPacketsSent { get; } -> int"""
    @property
    def OutgoingPacketsDiscarded(self) -> int:"""OutgoingPacketsDiscarded { get; } -> int"""
    @property
    def OutgoingPacketsWithErrors(self) -> int:"""OutgoingPacketsWithErrors { get; } -> int"""
    @property
    def OutputQueueLength(self) -> int:"""OutputQueueLength { get; } -> int"""
    @property
    def UnicastPacketsReceived(self) -> int:"""UnicastPacketsReceived { get; } -> int"""
    @property
    def UnicastPacketsSent(self) -> int:"""UnicastPacketsSent { get; } -> int"""
class IPv6InterfaceProperties(object):
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def Mtu(self) -> int:"""Mtu { get; } -> int"""
    def GetScopeId(self, scopeLevel: ScopeLevel) -> int:...
class MulticastIPAddressInformation(IPAddressInformation):
    @property
    def AddressPreferredLifetime(self) -> int:"""AddressPreferredLifetime { get; } -> int"""
    @property
    def AddressValidLifetime(self) -> int:"""AddressValidLifetime { get; } -> int"""
    @property
    def DhcpLeaseLifetime(self) -> int:"""DhcpLeaseLifetime { get; } -> int"""
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:"""DuplicateAddressDetectionState { get; } -> DuplicateAddressDetectionState"""
    @property
    def PrefixOrigin(self) -> PrefixOrigin:"""PrefixOrigin { get; } -> PrefixOrigin"""
    @property
    def SuffixOrigin(self) -> SuffixOrigin:"""SuffixOrigin { get; } -> SuffixOrigin"""
class MulticastIPAddressInformationCollection(_n_1_t_0[MulticastIPAddressInformation], typing.Iterable[MulticastIPAddressInformation]):
    @property
    def Item(self) -> MulticastIPAddressInformation:"""Item { get; } -> MulticastIPAddressInformation"""
class NetBiosNodeType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Broadcast: int
    Hybrid: int
    Mixed: int
    Peer2Peer: int
    Unknown: int
    value__: int
class NetworkAddressChangedEventHandler(_n_0_t_7, _n_0_t_8, _n_5_t_0):
    def __init__(self, object: object, method: _n_0_t_9) -> NetworkAddressChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_0_t_10, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: _n_0_t_10):...
class NetworkAvailabilityChangedEventHandler(_n_0_t_7, _n_0_t_8, _n_5_t_0):
    def __init__(self, object: object, method: _n_0_t_9) -> NetworkAvailabilityChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: NetworkAvailabilityEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: NetworkAvailabilityEventArgs):...
class NetworkAvailabilityEventArgs(_n_0_t_10):
    @property
    def IsAvailable(self) -> bool:"""IsAvailable { get; } -> bool"""
class NetworkChange(object):
    @property
    def NetworkAddressChanged(self) -> NetworkAddressChangedEventHandler:
        """NetworkAddressChanged Event: NetworkAddressChangedEventHandler"""
    @property
    def NetworkAvailabilityChanged(self) -> NetworkAvailabilityChangedEventHandler:
        """NetworkAvailabilityChanged Event: NetworkAvailabilityChangedEventHandler"""
    def __init__(self) -> NetworkChange:...
    @staticmethod
    def RegisterNetworkChange(nc: NetworkChange):...
class NetworkInformationAccess(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    Ping: int
    Read: int
    value__: int
class NetworkInformationException(_n_2_t_0, _n_5_t_0, _n_4_t_0):
    def __init__(self, errorCode: int) -> NetworkInformationException:...
    def __init__(self) -> NetworkInformationException:...
class NetworkInformationPermission(_n_6_t_0, _n_6_t_1, _n_6_t_2, _n_7_t_0):
    @property
    def Access(self) -> NetworkInformationAccess:"""Access { get; } -> NetworkInformationAccess"""
    def __init__(self, access: NetworkInformationAccess) -> NetworkInformationPermission:...
    def __init__(self, state: _n_7_t_1) -> NetworkInformationPermission:...
    def AddPermission(self, access: NetworkInformationAccess):...
class NetworkInformationPermissionAttribute(_n_7_t_2, _n_4_t_1):
    @property
    def Access(self) -> str:"""Access { get; set; } -> str"""
    def __init__(self, action: _n_7_t_3) -> NetworkInformationPermissionAttribute:...
class NetworkInterface(object):
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def Id(self) -> str:"""Id { get; } -> str"""
    @property
    def IPv6LoopbackInterfaceIndex(self) -> int:"""IPv6LoopbackInterfaceIndex { get; } -> int"""
    @property
    def IsReceiveOnly(self) -> bool:"""IsReceiveOnly { get; } -> bool"""
    @property
    def LoopbackInterfaceIndex(self) -> int:"""LoopbackInterfaceIndex { get; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType:"""NetworkInterfaceType { get; } -> NetworkInterfaceType"""
    @property
    def OperationalStatus(self) -> OperationalStatus:"""OperationalStatus { get; } -> OperationalStatus"""
    @property
    def Speed(self) -> int:"""Speed { get; } -> int"""
    @property
    def SupportsMulticast(self) -> bool:"""SupportsMulticast { get; } -> bool"""
    @staticmethod
    def GetAllNetworkInterfaces() -> _n_0_t_6[NetworkInterface]:...
    def GetIPProperties(self) -> IPInterfaceProperties:...
    def GetIPStatistics(self) -> IPInterfaceStatistics:...
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics:...
    @staticmethod
    def GetIsNetworkAvailable() -> bool:...
    def GetPhysicalAddress(self) -> PhysicalAddress:...
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> bool:...
class NetworkInterfaceComponent(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    IPv4: int
    IPv6: int
    value__: int
class NetworkInterfaceType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AsymmetricDsl: int
    Atm: int
    BasicIsdn: int
    Ethernet: int
    Ethernet3Megabit: int
    FastEthernetFx: int
    FastEthernetT: int
    Fddi: int
    GenericModem: int
    GigabitEthernet: int
    HighPerformanceSerialBus: int
    IPOverAtm: int
    Isdn: int
    Loopback: int
    MultiRateSymmetricDsl: int
    Ppp: int
    PrimaryIsdn: int
    RateAdaptDsl: int
    Slip: int
    SymmetricDsl: int
    TokenRing: int
    Tunnel: int
    Unknown: int
    value__: int
    VeryHighSpeedDsl: int
    Wireless80211: int
    Wman: int
    Wwanpp: int
    Wwanpp2: int
class OperationalStatus(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Dormant: int
    Down: int
    LowerLayerDown: int
    NotPresent: int
    Testing: int
    Unknown: int
    Up: int
    value__: int
class PhysicalAddress(object):
    _None: int
    def __init__(self, address: _n_0_t_6[_n_0_t_11]) -> PhysicalAddress:...
    def GetAddressBytes(self) -> _n_0_t_6[_n_0_t_11]:...
    @staticmethod
    def Parse(address: str) -> PhysicalAddress:...
class Ping(_n_2_t_1, _n_2_t_2):
    @property
    def PingCompleted(self) -> PingCompletedEventHandler:
        """PingCompleted Event: PingCompletedEventHandler"""
    def __init__(self) -> Ping:...
    def Send(self, address: _n_3_t_0, timeout: int, buffer: _n_0_t_6[_n_0_t_11], options: PingOptions) -> PingReply:...
    def Send(self, hostNameOrAddress: str, timeout: int, buffer: _n_0_t_6[_n_0_t_11], options: PingOptions) -> PingReply:...
    def Send(self, address: _n_3_t_0, timeout: int, buffer: _n_0_t_6[_n_0_t_11]) -> PingReply:...
    def Send(self, hostNameOrAddress: str, timeout: int, buffer: _n_0_t_6[_n_0_t_11]) -> PingReply:...
    def Send(self, address: _n_3_t_0, timeout: int) -> PingReply:...
    def Send(self, address: _n_3_t_0) -> PingReply:...
    def Send(self, hostNameOrAddress: str, timeout: int) -> PingReply:...
    def Send(self, hostNameOrAddress: str) -> PingReply:...
    def SendAsync(self, address: _n_3_t_0, timeout: int, buffer: _n_0_t_6[_n_0_t_11], options: PingOptions, userToken: object):...
    def SendAsync(self, hostNameOrAddress: str, timeout: int, buffer: _n_0_t_6[_n_0_t_11], options: PingOptions, userToken: object):...
    def SendAsync(self, address: _n_3_t_0, timeout: int, buffer: _n_0_t_6[_n_0_t_11], userToken: object):...
    def SendAsync(self, hostNameOrAddress: str, timeout: int, buffer: _n_0_t_6[_n_0_t_11], userToken: object):...
    def SendAsync(self, address: _n_3_t_0, timeout: int, userToken: object):...
    def SendAsync(self, address: _n_3_t_0, userToken: object):...
    def SendAsync(self, hostNameOrAddress: str, timeout: int, userToken: object):...
    def SendAsync(self, hostNameOrAddress: str, userToken: object):...
    def SendAsyncCancel(self):...
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int, buffer: _n_0_t_6[_n_0_t_11], options: PingOptions) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, address: _n_3_t_0, timeout: int, buffer: _n_0_t_6[_n_0_t_11], options: PingOptions) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int, buffer: _n_0_t_6[_n_0_t_11]) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, address: _n_3_t_0, timeout: int, buffer: _n_0_t_6[_n_0_t_11]) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, address: _n_3_t_0, timeout: int) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, hostNameOrAddress: str) -> _n_8_t_0[PingReply]:...
    def SendPingAsync(self, address: _n_3_t_0) -> _n_8_t_0[PingReply]:...
class PingCompletedEventArgs(_n_2_t_3):
    @property
    def Reply(self) -> PingReply:"""Reply { get; } -> PingReply"""
class PingCompletedEventHandler(_n_0_t_7, _n_0_t_8, _n_5_t_0):
    def __init__(self, object: object, method: _n_0_t_9) -> PingCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: PingCompletedEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: PingCompletedEventArgs):...
class PingException(_n_0_t_12, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_13) -> PingException:...
    def __init__(self, message: str) -> PingException:...
class PingOptions(object):
    @property
    def DontFragment(self) -> bool:"""DontFragment { get; set; } -> bool"""
    @property
    def Ttl(self) -> int:"""Ttl { get; set; } -> int"""
    def __init__(self) -> PingOptions:...
    def __init__(self, ttl: int, dontFragment: bool) -> PingOptions:...
class PingReply(object):
    @property
    def Address(self) -> _n_3_t_0:"""Address { get; } -> IPAddress"""
    @property
    def Buffer(self) -> _n_0_t_6[_n_0_t_11]:"""Buffer { get; } -> Array"""
    @property
    def Options(self) -> PingOptions:"""Options { get; } -> PingOptions"""
    @property
    def RoundtripTime(self) -> int:"""RoundtripTime { get; } -> int"""
    @property
    def Status(self) -> IPStatus:"""Status { get; } -> IPStatus"""
class PrefixOrigin(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Dhcp: int
    Manual: int
    Other: int
    RouterAdvertisement: int
    value__: int
    WellKnown: int
class ScopeLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Admin: int
    Global: int
    Interface: int
    Link: int
    _None: int
    Organization: int
    Site: int
    Subnet: int
    value__: int
class SuffixOrigin(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    LinkLayerAddress: int
    Manual: int
    OriginDhcp: int
    Other: int
    Random: int
    value__: int
    WellKnown: int
class TcpConnectionInformation(object):
    @property
    def LocalEndPoint(self) -> _n_3_t_1:"""LocalEndPoint { get; } -> IPEndPoint"""
    @property
    def RemoteEndPoint(self) -> _n_3_t_1:"""RemoteEndPoint { get; } -> IPEndPoint"""
    @property
    def State(self) -> TcpState:"""State { get; } -> TcpState"""
class TcpState(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Closed: int
    CloseWait: int
    Closing: int
    DeleteTcb: int
    Established: int
    FinWait1: int
    FinWait2: int
    LastAck: int
    Listen: int
    SynReceived: int
    SynSent: int
    TimeWait: int
    Unknown: int
    value__: int
class TcpStatistics(object):
    @property
    def ConnectionsAccepted(self) -> int:"""ConnectionsAccepted { get; } -> int"""
    @property
    def ConnectionsInitiated(self) -> int:"""ConnectionsInitiated { get; } -> int"""
    @property
    def CumulativeConnections(self) -> int:"""CumulativeConnections { get; } -> int"""
    @property
    def CurrentConnections(self) -> int:"""CurrentConnections { get; } -> int"""
    @property
    def ErrorsReceived(self) -> int:"""ErrorsReceived { get; } -> int"""
    @property
    def FailedConnectionAttempts(self) -> int:"""FailedConnectionAttempts { get; } -> int"""
    @property
    def MaximumConnections(self) -> int:"""MaximumConnections { get; } -> int"""
    @property
    def MaximumTransmissionTimeout(self) -> int:"""MaximumTransmissionTimeout { get; } -> int"""
    @property
    def MinimumTransmissionTimeout(self) -> int:"""MinimumTransmissionTimeout { get; } -> int"""
    @property
    def ResetConnections(self) -> int:"""ResetConnections { get; } -> int"""
    @property
    def ResetsSent(self) -> int:"""ResetsSent { get; } -> int"""
    @property
    def SegmentsReceived(self) -> int:"""SegmentsReceived { get; } -> int"""
    @property
    def SegmentsResent(self) -> int:"""SegmentsResent { get; } -> int"""
    @property
    def SegmentsSent(self) -> int:"""SegmentsSent { get; } -> int"""
class UdpStatistics(object):
    @property
    def DatagramsReceived(self) -> int:"""DatagramsReceived { get; } -> int"""
    @property
    def DatagramsSent(self) -> int:"""DatagramsSent { get; } -> int"""
    @property
    def IncomingDatagramsDiscarded(self) -> int:"""IncomingDatagramsDiscarded { get; } -> int"""
    @property
    def IncomingDatagramsWithErrors(self) -> int:"""IncomingDatagramsWithErrors { get; } -> int"""
    @property
    def UdpListeners(self) -> int:"""UdpListeners { get; } -> int"""
class UnicastIPAddressInformation(IPAddressInformation):
    @property
    def AddressPreferredLifetime(self) -> int:"""AddressPreferredLifetime { get; } -> int"""
    @property
    def AddressValidLifetime(self) -> int:"""AddressValidLifetime { get; } -> int"""
    @property
    def DhcpLeaseLifetime(self) -> int:"""DhcpLeaseLifetime { get; } -> int"""
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:"""DuplicateAddressDetectionState { get; } -> DuplicateAddressDetectionState"""
    @property
    def IPv4Mask(self) -> _n_3_t_0:"""IPv4Mask { get; } -> IPAddress"""
    @property
    def PrefixLength(self) -> int:"""PrefixLength { get; } -> int"""
    @property
    def PrefixOrigin(self) -> PrefixOrigin:"""PrefixOrigin { get; } -> PrefixOrigin"""
    @property
    def SuffixOrigin(self) -> SuffixOrigin:"""SuffixOrigin { get; } -> SuffixOrigin"""
class UnicastIPAddressInformationCollection(_n_1_t_0[UnicastIPAddressInformation], typing.Iterable[UnicastIPAddressInformation]):
    @property
    def Item(self) -> UnicastIPAddressInformation:"""Item { get; } -> UnicastIPAddressInformation"""
