from __clrclasses__.System import IDisposable as _n_0_t_0
from __clrclasses__.System import Uri as _n_0_t_1
from __clrclasses__.System import Enum as _n_0_t_2
from __clrclasses__.System import IComparable as _n_0_t_3
from __clrclasses__.System import IFormattable as _n_0_t_4
from __clrclasses__.System import IConvertible as _n_0_t_5
from __clrclasses__.System import MulticastDelegate as _n_0_t_6
from __clrclasses__.System import ICloneable as _n_0_t_7
from __clrclasses__.System import IntPtr as _n_0_t_8
from __clrclasses__.System import IAsyncResult as _n_0_t_9
from __clrclasses__.System import AsyncCallback as _n_0_t_10
from __clrclasses__.System import Exception as _n_0_t_11
from __clrclasses__.System import Array as _n_0_t_12
from __clrclasses__.System.Collections import IList as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IList as _n_2_t_0
from __clrclasses__.System.Collections.Generic import IReadOnlyList as _n_2_t_1
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_3_t_0
from __clrclasses__.System.Collections.Specialized import NameValueCollection as _n_4_t_0
from __clrclasses__.System.ComponentModel import AsyncCompletedEventArgs as _n_5_t_0
from __clrclasses__.System.IO import Stream as _n_6_t_0
from __clrclasses__.System.Net import ICredentialsByHost as _n_7_t_0
from __clrclasses__.System.Net import ServicePoint as _n_7_t_1
from __clrclasses__.System.Net.Mime import ContentType as _n_8_t_0
from __clrclasses__.System.Net.Mime import ContentDisposition as _n_8_t_1
from __clrclasses__.System.Net.Mime import TransferEncoding as _n_8_t_2
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_9_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_9_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_10_t_0
from __clrclasses__.System.Security import CodeAccessPermission as _n_11_t_0
from __clrclasses__.System.Security import IPermission as _n_11_t_1
from __clrclasses__.System.Security import IStackWalk as _n_11_t_2
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509CertificateCollection as _n_12_t_0
from __clrclasses__.System.Security.Permissions import IUnrestrictedPermission as _n_13_t_0
from __clrclasses__.System.Security.Permissions import PermissionState as _n_13_t_1
from __clrclasses__.System.Security.Permissions import CodeAccessSecurityAttribute as _n_13_t_2
from __clrclasses__.System.Security.Permissions import SecurityAction as _n_13_t_3
from __clrclasses__.System.Text import Encoding as _n_14_t_0
from __clrclasses__.System.Threading.Tasks import Task as _n_15_t_0
import typing
class AlternateView(AttachmentBase, _n_0_t_0):
    @property
    def BaseUri(self) -> _n_0_t_1:"""BaseUri { get; set; } -> Uri"""
    @property
    def LinkedResources(self) -> LinkedResourceCollection:"""LinkedResources { get; } -> LinkedResourceCollection"""
    def __init__(self, contentStream: _n_6_t_0, contentType: _n_8_t_0) -> AlternateView:...
    def __init__(self, contentStream: _n_6_t_0, mediaType: str) -> AlternateView:...
    def __init__(self, contentStream: _n_6_t_0) -> AlternateView:...
    def __init__(self, fileName: str, contentType: _n_8_t_0) -> AlternateView:...
    def __init__(self, fileName: str, mediaType: str) -> AlternateView:...
    def __init__(self, fileName: str) -> AlternateView:...
    @staticmethod
    def CreateAlternateViewFromString(content: str, contentType: _n_8_t_0) -> AlternateView:...
    @staticmethod
    def CreateAlternateViewFromString(content: str, contentEncoding: _n_14_t_0, mediaType: str) -> AlternateView:...
    @staticmethod
    def CreateAlternateViewFromString(content: str) -> AlternateView:...
class AlternateViewCollection(_n_3_t_0[AlternateView], _n_2_t_0[AlternateView], _n_1_t_0, _n_2_t_1[AlternateView], _n_0_t_0, typing.Iterable[AlternateView]):
    pass
class Attachment(AttachmentBase, _n_0_t_0):
    @property
    def ContentDisposition(self) -> _n_8_t_1:"""ContentDisposition { get; } -> ContentDisposition"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def NameEncoding(self) -> _n_14_t_0:"""NameEncoding { get; set; } -> Encoding"""
    def __init__(self, contentStream: _n_6_t_0, contentType: _n_8_t_0) -> Attachment:...
    def __init__(self, contentStream: _n_6_t_0, name: str, mediaType: str) -> Attachment:...
    def __init__(self, contentStream: _n_6_t_0, name: str) -> Attachment:...
    def __init__(self, fileName: str, contentType: _n_8_t_0) -> Attachment:...
    def __init__(self, fileName: str, mediaType: str) -> Attachment:...
    def __init__(self, fileName: str) -> Attachment:...
    @staticmethod
    def CreateAttachmentFromString(content: str, contentType: _n_8_t_0) -> Attachment:...
    @staticmethod
    def CreateAttachmentFromString(content: str, name: str, contentEncoding: _n_14_t_0, mediaType: str) -> Attachment:...
    @staticmethod
    def CreateAttachmentFromString(content: str, name: str) -> Attachment:...
class AttachmentBase(_n_0_t_0):
    @property
    def ContentId(self) -> str:"""ContentId { get; set; } -> str"""
    @property
    def ContentStream(self) -> _n_6_t_0:"""ContentStream { get; } -> Stream"""
    @property
    def ContentType(self) -> _n_8_t_0:"""ContentType { get; set; } -> ContentType"""
    @property
    def TransferEncoding(self) -> _n_8_t_2:"""TransferEncoding { get; set; } -> TransferEncoding"""
class AttachmentCollection(_n_3_t_0[Attachment], _n_2_t_0[Attachment], _n_1_t_0, _n_2_t_1[Attachment], _n_0_t_0, typing.Iterable[Attachment]):
    pass
class DeliveryNotificationOptions(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Delay: int
    Never: int
    _None: int
    OnFailure: int
    OnSuccess: int
    value__: int
class LinkedResource(AttachmentBase, _n_0_t_0):
    @property
    def ContentLink(self) -> _n_0_t_1:"""ContentLink { get; set; } -> Uri"""
    def __init__(self, contentStream: _n_6_t_0, contentType: _n_8_t_0) -> LinkedResource:...
    def __init__(self, contentStream: _n_6_t_0, mediaType: str) -> LinkedResource:...
    def __init__(self, contentStream: _n_6_t_0) -> LinkedResource:...
    def __init__(self, fileName: str, contentType: _n_8_t_0) -> LinkedResource:...
    def __init__(self, fileName: str, mediaType: str) -> LinkedResource:...
    def __init__(self, fileName: str) -> LinkedResource:...
    @staticmethod
    def CreateLinkedResourceFromString(content: str, contentType: _n_8_t_0) -> LinkedResource:...
    @staticmethod
    def CreateLinkedResourceFromString(content: str, contentEncoding: _n_14_t_0, mediaType: str) -> LinkedResource:...
    @staticmethod
    def CreateLinkedResourceFromString(content: str) -> LinkedResource:...
class LinkedResourceCollection(_n_3_t_0[LinkedResource], _n_2_t_0[LinkedResource], _n_1_t_0, _n_2_t_1[LinkedResource], _n_0_t_0, typing.Iterable[LinkedResource]):
    pass
class MailAddress(object):
    @property
    def Address(self) -> str:"""Address { get; } -> str"""
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def Host(self) -> str:"""Host { get; } -> str"""
    @property
    def User(self) -> str:"""User { get; } -> str"""
    def __init__(self, address: str, displayName: str, displayNameEncoding: _n_14_t_0) -> MailAddress:...
    def __init__(self, address: str, displayName: str) -> MailAddress:...
    def __init__(self, address: str) -> MailAddress:...
class MailAddressCollection(_n_3_t_0[MailAddress], _n_2_t_0[MailAddress], _n_1_t_0, _n_2_t_1[MailAddress], typing.Iterable[MailAddress]):
    def __init__(self) -> MailAddressCollection:...
class MailMessage(_n_0_t_0):
    @property
    def AlternateViews(self) -> AlternateViewCollection:"""AlternateViews { get; } -> AlternateViewCollection"""
    @property
    def Attachments(self) -> AttachmentCollection:"""Attachments { get; } -> AttachmentCollection"""
    @property
    def Bcc(self) -> MailAddressCollection:"""Bcc { get; } -> MailAddressCollection"""
    @property
    def Body(self) -> str:"""Body { get; set; } -> str"""
    @property
    def BodyEncoding(self) -> _n_14_t_0:"""BodyEncoding { get; set; } -> Encoding"""
    @property
    def BodyTransferEncoding(self) -> _n_8_t_2:"""BodyTransferEncoding { get; set; } -> TransferEncoding"""
    @property
    def CC(self) -> MailAddressCollection:"""CC { get; } -> MailAddressCollection"""
    @property
    def DeliveryNotificationOptions(self) -> DeliveryNotificationOptions:"""DeliveryNotificationOptions { get; set; } -> DeliveryNotificationOptions"""
    @property
    def From(self) -> MailAddress:"""From { get; set; } -> MailAddress"""
    @property
    def Headers(self) -> _n_4_t_0:"""Headers { get; } -> NameValueCollection"""
    @property
    def HeadersEncoding(self) -> _n_14_t_0:"""HeadersEncoding { get; set; } -> Encoding"""
    @property
    def IsBodyHtml(self) -> bool:"""IsBodyHtml { get; set; } -> bool"""
    @property
    def Priority(self) -> MailPriority:"""Priority { get; set; } -> MailPriority"""
    @property
    def ReplyTo(self) -> MailAddress:"""ReplyTo { get; set; } -> MailAddress"""
    @property
    def ReplyToList(self) -> MailAddressCollection:"""ReplyToList { get; } -> MailAddressCollection"""
    @property
    def Sender(self) -> MailAddress:"""Sender { get; set; } -> MailAddress"""
    @property
    def Subject(self) -> str:"""Subject { get; set; } -> str"""
    @property
    def SubjectEncoding(self) -> _n_14_t_0:"""SubjectEncoding { get; set; } -> Encoding"""
    @property
    def To(self) -> MailAddressCollection:"""To { get; } -> MailAddressCollection"""
    def __init__(self, _from: MailAddress, to: MailAddress) -> MailMessage:...
    def __init__(self, _from: str, to: str, subject: str, body: str) -> MailMessage:...
    def __init__(self, _from: str, to: str) -> MailMessage:...
    def __init__(self) -> MailMessage:...
class MailPriority(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    High: int
    Low: int
    Normal: int
    value__: int
class SendCompletedEventHandler(_n_0_t_6, _n_0_t_7, _n_10_t_0):
    def __init__(self, object: object, method: _n_0_t_8) -> SendCompletedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_5_t_0, callback: _n_0_t_10, object: object) -> _n_0_t_9:...
    def EndInvoke(self, result: _n_0_t_9):...
    def Invoke(self, sender: object, e: _n_5_t_0):...
class SmtpAccess(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Connect: int
    ConnectToUnrestrictedPort: int
    _None: int
    value__: int
class SmtpClient(_n_0_t_0):
    @property
    def ClientCertificates(self) -> _n_12_t_0:"""ClientCertificates { get; } -> X509CertificateCollection"""
    @property
    def Credentials(self) -> _n_7_t_0:"""Credentials { get; set; } -> ICredentialsByHost"""
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:"""DeliveryFormat { get; set; } -> SmtpDeliveryFormat"""
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:"""DeliveryMethod { get; set; } -> SmtpDeliveryMethod"""
    @property
    def EnableSsl(self) -> bool:"""EnableSsl { get; set; } -> bool"""
    @property
    def Host(self) -> str:"""Host { get; set; } -> str"""
    @property
    def PickupDirectoryLocation(self) -> str:"""PickupDirectoryLocation { get; set; } -> str"""
    @property
    def Port(self) -> int:"""Port { get; set; } -> int"""
    @property
    def ServicePoint(self) -> _n_7_t_1:"""ServicePoint { get; } -> ServicePoint"""
    @property
    def TargetName(self) -> str:"""TargetName { get; set; } -> str"""
    @property
    def Timeout(self) -> int:"""Timeout { get; set; } -> int"""
    @property
    def UseDefaultCredentials(self) -> bool:"""UseDefaultCredentials { get; set; } -> bool"""
    @property
    def SendCompleted(self) -> SendCompletedEventHandler:
        """SendCompleted Event: SendCompletedEventHandler"""
    def __init__(self, host: str, port: int) -> SmtpClient:...
    def __init__(self, host: str) -> SmtpClient:...
    def __init__(self) -> SmtpClient:...
    def Send(self, message: MailMessage):...
    def Send(self, _from: str, recipients: str, subject: str, body: str):...
    def SendAsync(self, message: MailMessage, userToken: object):...
    def SendAsync(self, _from: str, recipients: str, subject: str, body: str, userToken: object):...
    def SendAsyncCancel(self):...
    def SendMailAsync(self, message: MailMessage) -> _n_15_t_0:...
    def SendMailAsync(self, _from: str, recipients: str, subject: str, body: str) -> _n_15_t_0:...
class SmtpDeliveryFormat(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    International: int
    SevenBit: int
    value__: int
class SmtpDeliveryMethod(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Network: int
    PickupDirectoryFromIis: int
    SpecifiedPickupDirectory: int
    value__: int
class SmtpException(_n_0_t_11, _n_10_t_0, _n_9_t_0):
    @property
    def StatusCode(self) -> SmtpStatusCode:"""StatusCode { get; set; } -> SmtpStatusCode"""
    def __init__(self, message: str, innerException: _n_0_t_11) -> SmtpException:...
    def __init__(self, message: str) -> SmtpException:...
    def __init__(self) -> SmtpException:...
    def __init__(self, statusCode: SmtpStatusCode, message: str) -> SmtpException:...
    def __init__(self, statusCode: SmtpStatusCode) -> SmtpException:...
class SmtpFailedRecipientException(SmtpException, _n_10_t_0, _n_9_t_0):
    @property
    def FailedRecipient(self) -> str:"""FailedRecipient { get; } -> str"""
    def __init__(self, message: str, failedRecipient: str, innerException: _n_0_t_11) -> SmtpFailedRecipientException:...
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: str, serverResponse: str) -> SmtpFailedRecipientException:...
    def __init__(self, statusCode: SmtpStatusCode, failedRecipient: str) -> SmtpFailedRecipientException:...
    def __init__(self, message: str, innerException: _n_0_t_11) -> SmtpFailedRecipientException:...
    def __init__(self, message: str) -> SmtpFailedRecipientException:...
    def __init__(self) -> SmtpFailedRecipientException:...
class SmtpFailedRecipientsException(SmtpFailedRecipientException, _n_10_t_0, _n_9_t_0):
    @property
    def InnerExceptions(self) -> _n_0_t_12[SmtpFailedRecipientException]:"""InnerExceptions { get; } -> Array"""
    def __init__(self, message: str, innerExceptions: _n_0_t_12[SmtpFailedRecipientException]) -> SmtpFailedRecipientsException:...
    def __init__(self, message: str, innerException: _n_0_t_11) -> SmtpFailedRecipientsException:...
    def __init__(self, message: str) -> SmtpFailedRecipientsException:...
    def __init__(self) -> SmtpFailedRecipientsException:...
class SmtpPermission(_n_11_t_0, _n_11_t_1, _n_11_t_2, _n_13_t_0):
    @property
    def Access(self) -> SmtpAccess:"""Access { get; } -> SmtpAccess"""
    def __init__(self, access: SmtpAccess) -> SmtpPermission:...
    def __init__(self, unrestricted: bool) -> SmtpPermission:...
    def __init__(self, state: _n_13_t_1) -> SmtpPermission:...
    def AddPermission(self, access: SmtpAccess):...
class SmtpPermissionAttribute(_n_13_t_2, _n_9_t_1):
    @property
    def Access(self) -> str:"""Access { get; set; } -> str"""
    def __init__(self, action: _n_13_t_3) -> SmtpPermissionAttribute:...
class SmtpStatusCode(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    BadCommandSequence: int
    CannotVerifyUserWillAttemptDelivery: int
    ClientNotPermitted: int
    CommandNotImplemented: int
    CommandParameterNotImplemented: int
    CommandUnrecognized: int
    ExceededStorageAllocation: int
    GeneralFailure: int
    HelpMessage: int
    InsufficientStorage: int
    LocalErrorInProcessing: int
    MailboxBusy: int
    MailboxNameNotAllowed: int
    MailboxUnavailable: int
    MustIssueStartTlsFirst: int
    Ok: int
    ServiceClosingTransmissionChannel: int
    ServiceNotAvailable: int
    ServiceReady: int
    StartMailInput: int
    SyntaxError: int
    SystemStatus: int
    TransactionFailed: int
    UserNotLocalTryAlternatePath: int
    UserNotLocalWillForward: int
    value__: int
