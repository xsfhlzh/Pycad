from __clrclasses__.System import Predicate as _n_0_t_0
from __clrclasses__.System import Func as _n_0_t_1
from __clrclasses__.System.Collections.Generic import IDictionary as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_1
from __clrclasses__.System.IO import BinaryReader as _n_2_t_0
from __clrclasses__.System.IO import BinaryWriter as _n_2_t_1
from __clrclasses__.System.Security.Principal import IIdentity as _n_3_t_0
from __clrclasses__.System.Security.Principal import IPrincipal as _n_3_t_1
import typing
class Claim(object):
    @property
    def Issuer(self) -> str:"""Issuer { get; } -> str"""
    @property
    def OriginalIssuer(self) -> str:"""OriginalIssuer { get; } -> str"""
    @property
    def Properties(self) -> _n_1_t_0[str, str]:"""Properties { get; } -> IDictionary"""
    @property
    def Subject(self) -> ClaimsIdentity:"""Subject { get; set; } -> ClaimsIdentity"""
    @property
    def Type(self) -> str:"""Type { get; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    @property
    def ValueType(self) -> str:"""ValueType { get; } -> str"""
    def __init__(self, reader: _n_2_t_0) -> Claim:...
    def __init__(self, reader: _n_2_t_0, subject: ClaimsIdentity) -> Claim:...
    def __init__(self, type: str, value: str) -> Claim:...
    def __init__(self, type: str, value: str, valueType: str) -> Claim:...
    def __init__(self, type: str, value: str, valueType: str, issuer: str) -> Claim:...
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str) -> Claim:...
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity) -> Claim:...
    def Clone(self) -> Claim:...
    def Clone(self, identity: ClaimsIdentity) -> Claim:...
    def WriteTo(self, writer: _n_2_t_1):...
class ClaimsIdentity(_n_3_t_0):
    DefaultIssuer: int
    DefaultNameClaimType: int
    DefaultRoleClaimType: int
    @property
    def Actor(self) -> ClaimsIdentity:"""Actor { get; set; } -> ClaimsIdentity"""
    @property
    def BootstrapContext(self) -> object:"""BootstrapContext { get; set; } -> object"""
    @property
    def Claims(self) -> _n_1_t_1[Claim]:"""Claims { get; } -> IEnumerable"""
    @property
    def Label(self) -> str:"""Label { get; set; } -> str"""
    @property
    def NameClaimType(self) -> str:"""NameClaimType { get; } -> str"""
    @property
    def RoleClaimType(self) -> str:"""RoleClaimType { get; } -> str"""
    def __init__(self) -> ClaimsIdentity:...
    def __init__(self, identity: _n_3_t_0) -> ClaimsIdentity:...
    def __init__(self, claims: _n_1_t_1[Claim]) -> ClaimsIdentity:...
    def __init__(self, authenticationType: str) -> ClaimsIdentity:...
    def __init__(self, claims: _n_1_t_1[Claim], authenticationType: str) -> ClaimsIdentity:...
    def __init__(self, identity: _n_3_t_0, claims: _n_1_t_1[Claim]) -> ClaimsIdentity:...
    def __init__(self, authenticationType: str, nameType: str, roleType: str) -> ClaimsIdentity:...
    def __init__(self, claims: _n_1_t_1[Claim], authenticationType: str, nameType: str, roleType: str) -> ClaimsIdentity:...
    def __init__(self, identity: _n_3_t_0, claims: _n_1_t_1[Claim], authenticationType: str, nameType: str, roleType: str) -> ClaimsIdentity:...
    def __init__(self, reader: _n_2_t_0) -> ClaimsIdentity:...
    def AddClaim(self, claim: Claim):...
    def AddClaims(self, claims: _n_1_t_1[Claim]):...
    def Clone(self) -> ClaimsIdentity:...
    def FindAll(self, match: _n_0_t_0[Claim]) -> _n_1_t_1[Claim]:...
    def FindAll(self, type: str) -> _n_1_t_1[Claim]:...
    def FindFirst(self, match: _n_0_t_0[Claim]) -> Claim:...
    def FindFirst(self, type: str) -> Claim:...
    def HasClaim(self, match: _n_0_t_0[Claim]) -> bool:...
    def HasClaim(self, type: str, value: str) -> bool:...
    def RemoveClaim(self, claim: Claim):...
    def TryRemoveClaim(self, claim: Claim) -> bool:...
    def WriteTo(self, writer: _n_2_t_1):...
class ClaimsPrincipal(_n_3_t_1):
    @property
    def Claims(self) -> _n_1_t_1[Claim]:"""Claims { get; } -> IEnumerable"""
    @property
    def ClaimsPrincipalSelector(self) -> _n_0_t_1[ClaimsPrincipal]:"""ClaimsPrincipalSelector { get; set; } -> Func"""
    @property
    def Current(self) -> ClaimsPrincipal:"""Current { get; } -> ClaimsPrincipal"""
    @property
    def Identities(self) -> _n_1_t_1[ClaimsIdentity]:"""Identities { get; } -> IEnumerable"""
    @property
    def PrimaryIdentitySelector(self) -> _n_0_t_1[_n_1_t_1[ClaimsIdentity], ClaimsIdentity]:"""PrimaryIdentitySelector { get; set; } -> Func"""
    def __init__(self) -> ClaimsPrincipal:...
    def __init__(self, identity: _n_3_t_0) -> ClaimsPrincipal:...
    def __init__(self, identities: _n_1_t_1[ClaimsIdentity]) -> ClaimsPrincipal:...
    def __init__(self, principal: _n_3_t_1) -> ClaimsPrincipal:...
    def __init__(self, reader: _n_2_t_0) -> ClaimsPrincipal:...
    def AddIdentities(self, identities: _n_1_t_1[ClaimsIdentity]):...
    def AddIdentity(self, identity: ClaimsIdentity):...
    def Clone(self) -> ClaimsPrincipal:...
    def FindAll(self, match: _n_0_t_0[Claim]) -> _n_1_t_1[Claim]:...
    def FindAll(self, type: str) -> _n_1_t_1[Claim]:...
    def FindFirst(self, match: _n_0_t_0[Claim]) -> Claim:...
    def FindFirst(self, type: str) -> Claim:...
    def HasClaim(self, match: _n_0_t_0[Claim]) -> bool:...
    def HasClaim(self, type: str, value: str) -> bool:...
    def WriteTo(self, writer: _n_2_t_1):...
class ClaimTypes(object):
    Actor: int
    Anonymous: int
    Authentication: int
    AuthenticationInstant: int
    AuthenticationMethod: int
    AuthorizationDecision: int
    CookiePath: int
    Country: int
    DateOfBirth: int
    DenyOnlyPrimaryGroupSid: int
    DenyOnlyPrimarySid: int
    DenyOnlySid: int
    DenyOnlyWindowsDeviceGroup: int
    Dns: int
    Dsa: int
    Email: int
    Expiration: int
    Expired: int
    Gender: int
    GivenName: int
    GroupSid: int
    Hash: int
    HomePhone: int
    IsPersistent: int
    Locality: int
    MobilePhone: int
    Name: int
    NameIdentifier: int
    OtherPhone: int
    PostalCode: int
    PrimaryGroupSid: int
    PrimarySid: int
    Role: int
    Rsa: int
    SerialNumber: int
    Sid: int
    Spn: int
    StateOrProvince: int
    StreetAddress: int
    Surname: int
    System: int
    Thumbprint: int
    Upn: int
    Uri: int
    UserData: int
    Version: int
    Webpage: int
    WindowsAccountName: int
    WindowsDeviceClaim: int
    WindowsDeviceGroup: int
    WindowsFqbnVersion: int
    WindowsSubAuthority: int
    WindowsUserClaim: int
    X500DistinguishedName: int
class ClaimValueTypes(object):
    Base64Binary: int
    Base64Octet: int
    Boolean: int
    Date: int
    DateTime: int
    DaytimeDuration: int
    DnsName: int
    Double: int
    DsaKeyValue: int
    Email: int
    Fqbn: int
    HexBinary: int
    Integer: int
    Integer32: int
    Integer64: int
    KeyInfo: int
    Rfc822Name: int
    Rsa: int
    RsaKeyValue: int
    Sid: int
    String: int
    Time: int
    UInteger32: int
    UInteger64: int
    UpnName: int
    X500Name: int
    YearMonthDuration: int
class DynamicRoleClaimProvider(object):
    @staticmethod
    def AddDynamicRoleClaims(claimsIdentity: ClaimsIdentity, claims: _n_1_t_1[Claim]):...
