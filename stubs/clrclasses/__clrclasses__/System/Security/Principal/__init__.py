from __clrclasses__.Microsoft.Win32.SafeHandles import SafeAccessTokenHandle as _n_0_t_0
from __clrclasses__.System import Array as _n_1_t_0
from __clrclasses__.System import SystemException as _n_1_t_1
from __clrclasses__.System import Exception as _n_1_t_2
from __clrclasses__.System import Type as _n_1_t_3
from __clrclasses__.System import Enum as _n_1_t_4
from __clrclasses__.System import IComparable as _n_1_t_5
from __clrclasses__.System import IFormattable as _n_1_t_6
from __clrclasses__.System import IConvertible as _n_1_t_7
from __clrclasses__.System import IntPtr as _n_1_t_8
from __clrclasses__.System import Byte as _n_1_t_9
from __clrclasses__.System import IDisposable as _n_1_t_10
from __clrclasses__.System import Func as _n_1_t_11
from __clrclasses__.System import Action as _n_1_t_12
from __clrclasses__.System.Collections.Generic import ICollection as _n_2_t_0
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_2_t_1
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_3_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_4_t_1
from __clrclasses__.System.Runtime.Serialization import SerializationInfo as _n_4_t_2
from __clrclasses__.System.Runtime.Serialization import StreamingContext as _n_4_t_3
from __clrclasses__.System.Security.Claims import ClaimsIdentity as _n_5_t_0
from __clrclasses__.System.Security.Claims import ClaimsPrincipal as _n_5_t_1
from __clrclasses__.System.Security.Claims import Claim as _n_5_t_2
import typing
class GenericIdentity(_n_5_t_0, IIdentity):
    def __init__(self, name: str) -> GenericIdentity:...
    def __init__(self, name: str, type: str) -> GenericIdentity:...
class GenericPrincipal(_n_5_t_1, IPrincipal):
    def __init__(self, identity: IIdentity, roles: _n_1_t_0[str]) -> GenericPrincipal:...
class IdentityNotMappedException(_n_1_t_1, _n_4_t_0, _n_3_t_0):
    @property
    def UnmappedIdentities(self) -> IdentityReferenceCollection:"""UnmappedIdentities { get; } -> IdentityReferenceCollection"""
    def __init__(self, message: str, inner: _n_1_t_2) -> IdentityNotMappedException:...
    def __init__(self, message: str) -> IdentityNotMappedException:...
    def __init__(self) -> IdentityNotMappedException:...
class IdentityReference(object):
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def IsValidTargetType(self, targetType: _n_1_t_3) -> bool:...
    def Translate(self, targetType: _n_1_t_3) -> IdentityReference:...
class IdentityReferenceCollection(_n_2_t_0[IdentityReference], typing.Iterable[IdentityReference]):
    @property
    def Item(self) -> IdentityReference:"""Item { get; set; } -> IdentityReference"""
    def __init__(self, capacity: int) -> IdentityReferenceCollection:...
    def __init__(self) -> IdentityReferenceCollection:...
    def Translate(self, targetType: _n_1_t_3, forceSuccess: bool) -> IdentityReferenceCollection:...
    def Translate(self, targetType: _n_1_t_3) -> IdentityReferenceCollection:...
class IIdentity():
    @property
    def AuthenticationType(self) -> str:"""AuthenticationType { get; } -> str"""
    @property
    def IsAuthenticated(self) -> bool:"""IsAuthenticated { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class IPrincipal():
    @property
    def Identity(self) -> IIdentity:"""Identity { get; } -> IIdentity"""
    def IsInRole(self, role: str) -> bool:...
class NTAccount(IdentityReference):
    def __init__(self, name: str) -> NTAccount:...
    def __init__(self, domainName: str, accountName: str) -> NTAccount:...
class PrincipalPolicy(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    NoPrincipal: int
    UnauthenticatedPrincipal: int
    value__: int
    WindowsPrincipal: int
class SecurityIdentifier(IdentityReference, _n_1_t_5[SecurityIdentifier]):
    MaxBinaryLength: int
    MinBinaryLength: int
    @property
    def AccountDomainSid(self) -> SecurityIdentifier:"""AccountDomainSid { get; } -> SecurityIdentifier"""
    @property
    def BinaryLength(self) -> int:"""BinaryLength { get; } -> int"""
    def __init__(self, binaryForm: _n_1_t_8) -> SecurityIdentifier:...
    def __init__(self, binaryForm: _n_1_t_0[_n_1_t_9], offset: int) -> SecurityIdentifier:...
    def __init__(self, sidType: WellKnownSidType, domainSid: SecurityIdentifier) -> SecurityIdentifier:...
    def __init__(self, sddlForm: str) -> SecurityIdentifier:...
    def GetBinaryForm(self, binaryForm: _n_1_t_0[_n_1_t_9], offset: int):...
    def IsAccountSid(self) -> bool:...
    def IsEqualDomainSid(self, sid: SecurityIdentifier) -> bool:...
    def IsWellKnown(self, type: WellKnownSidType) -> bool:...
class TokenAccessLevels(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    AdjustDefault: int
    AdjustGroups: int
    AdjustPrivileges: int
    AdjustSessionId: int
    AllAccess: int
    AssignPrimary: int
    Duplicate: int
    Impersonate: int
    MaximumAllowed: int
    Query: int
    QuerySource: int
    Read: int
    value__: int
    Write: int
class TokenImpersonationLevel(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    Anonymous: int
    Delegation: int
    Identification: int
    Impersonation: int
    _None: int
    value__: int
class WellKnownSidType(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    AccountAdministratorSid: int
    AccountCertAdminsSid: int
    AccountComputersSid: int
    AccountControllersSid: int
    AccountDomainAdminsSid: int
    AccountDomainGuestsSid: int
    AccountDomainUsersSid: int
    AccountEnterpriseAdminsSid: int
    AccountGuestSid: int
    AccountKrbtgtSid: int
    AccountPolicyAdminsSid: int
    AccountRasAndIasServersSid: int
    AccountSchemaAdminsSid: int
    AnonymousSid: int
    AuthenticatedUserSid: int
    BatchSid: int
    BuiltinAccountOperatorsSid: int
    BuiltinAdministratorsSid: int
    BuiltinAuthorizationAccessSid: int
    BuiltinBackupOperatorsSid: int
    BuiltinDomainSid: int
    BuiltinGuestsSid: int
    BuiltinIncomingForestTrustBuildersSid: int
    BuiltinNetworkConfigurationOperatorsSid: int
    BuiltinPerformanceLoggingUsersSid: int
    BuiltinPerformanceMonitoringUsersSid: int
    BuiltinPowerUsersSid: int
    BuiltinPreWindows2000CompatibleAccessSid: int
    BuiltinPrintOperatorsSid: int
    BuiltinRemoteDesktopUsersSid: int
    BuiltinReplicatorSid: int
    BuiltinSystemOperatorsSid: int
    BuiltinUsersSid: int
    CreatorGroupServerSid: int
    CreatorGroupSid: int
    CreatorOwnerServerSid: int
    CreatorOwnerSid: int
    DialupSid: int
    DigestAuthenticationSid: int
    EnterpriseControllersSid: int
    InteractiveSid: int
    LocalServiceSid: int
    LocalSid: int
    LocalSystemSid: int
    LogonIdsSid: int
    MaxDefined: int
    NetworkServiceSid: int
    NetworkSid: int
    NTAuthoritySid: int
    NtlmAuthenticationSid: int
    NullSid: int
    OtherOrganizationSid: int
    ProxySid: int
    RemoteLogonIdSid: int
    RestrictedCodeSid: int
    SChannelAuthenticationSid: int
    SelfSid: int
    ServiceSid: int
    TerminalServerSid: int
    ThisOrganizationSid: int
    value__: int
    WinBuiltinTerminalServerLicenseServersSid: int
    WorldSid: int
class WindowsAccountType(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    Anonymous: int
    Guest: int
    Normal: int
    System: int
    value__: int
class WindowsBuiltInRole(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    AccountOperator: int
    Administrator: int
    BackupOperator: int
    Guest: int
    PowerUser: int
    PrintOperator: int
    Replicator: int
    SystemOperator: int
    User: int
    value__: int
class WindowsIdentity(_n_5_t_0, IIdentity, _n_4_t_0, _n_4_t_1, _n_1_t_10):
    DefaultIssuer: int
    @property
    def AccessToken(self) -> _n_0_t_0:"""AccessToken { get; } -> SafeAccessTokenHandle"""
    @property
    def DeviceClaims(self) -> _n_2_t_1[_n_5_t_2]:"""DeviceClaims { get; } -> IEnumerable"""
    @property
    def Groups(self) -> IdentityReferenceCollection:"""Groups { get; } -> IdentityReferenceCollection"""
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:"""ImpersonationLevel { get; } -> TokenImpersonationLevel"""
    @property
    def IsAnonymous(self) -> bool:"""IsAnonymous { get; } -> bool"""
    @property
    def IsGuest(self) -> bool:"""IsGuest { get; } -> bool"""
    @property
    def IsSystem(self) -> bool:"""IsSystem { get; } -> bool"""
    @property
    def Owner(self) -> SecurityIdentifier:"""Owner { get; } -> SecurityIdentifier"""
    @property
    def Token(self) -> _n_1_t_8:"""Token { get; } -> IntPtr"""
    @property
    def User(self) -> SecurityIdentifier:"""User { get; } -> SecurityIdentifier"""
    @property
    def UserClaims(self) -> _n_2_t_1[_n_5_t_2]:"""UserClaims { get; } -> IEnumerable"""
    def __init__(self, info: _n_4_t_2, context: _n_4_t_3) -> WindowsIdentity:...
    def __init__(self, sUserPrincipalName: str, type: str) -> WindowsIdentity:...
    def __init__(self, sUserPrincipalName: str) -> WindowsIdentity:...
    def __init__(self, userToken: _n_1_t_8, type: str, acctType: WindowsAccountType, isAuthenticated: bool) -> WindowsIdentity:...
    def __init__(self, userToken: _n_1_t_8, type: str, acctType: WindowsAccountType) -> WindowsIdentity:...
    def __init__(self, userToken: _n_1_t_8, type: str) -> WindowsIdentity:...
    def __init__(self, userToken: _n_1_t_8) -> WindowsIdentity:...
    @staticmethod
    def GetAnonymous() -> WindowsIdentity:...
    @staticmethod
    def GetCurrent(desiredAccess: TokenAccessLevels) -> WindowsIdentity:...
    @staticmethod
    def GetCurrent(ifImpersonating: bool) -> WindowsIdentity:...
    @staticmethod
    def GetCurrent() -> WindowsIdentity:...
    @staticmethod
    def Impersonate(userToken: _n_1_t_8) -> WindowsImpersonationContext:...
    def Impersonate(self) -> WindowsImpersonationContext:...
    @staticmethod
    def RunImpersonated(safeAccessTokenHandle: _n_0_t_0, func: _n_1_t_11[typing.Any]) -> typing.Any:...
    @staticmethod
    def RunImpersonated(safeAccessTokenHandle: _n_0_t_0, action: _n_1_t_12):...
class WindowsImpersonationContext(_n_1_t_10):
    def Undo(self):...
class WindowsPrincipal(_n_5_t_1, IPrincipal):
    @property
    def DeviceClaims(self) -> _n_2_t_1[_n_5_t_2]:"""DeviceClaims { get; } -> IEnumerable"""
    @property
    def UserClaims(self) -> _n_2_t_1[_n_5_t_2]:"""UserClaims { get; } -> IEnumerable"""
    def __init__(self, ntIdentity: WindowsIdentity) -> WindowsPrincipal:...
