from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import Array as _n_0_t_4
from __clrclasses__.System import Attribute as _n_0_t_5
from __clrclasses__.System import Version as _n_0_t_6
from __clrclasses__.System import Byte as _n_0_t_7
from __clrclasses__.System.Collections import ICollection as _n_1_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_1_t_1
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_2_t_0
from __clrclasses__.System.Security import CodeAccessPermission as _n_3_t_0
from __clrclasses__.System.Security import IPermission as _n_3_t_1
from __clrclasses__.System.Security import IStackWalk as _n_3_t_2
from __clrclasses__.System.Security import PermissionSet as _n_3_t_3
from __clrclasses__.System.Security import SecurityZone as _n_3_t_4
from __clrclasses__.System.Security.AccessControl import AccessControlActions as _n_4_t_0
from __clrclasses__.System.Security.Cryptography import CspParameters as _n_5_t_0
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509Certificate as _n_6_t_0
import typing
class CodeAccessSecurityAttribute(SecurityAttribute, _n_2_t_0):
    pass
class EnvironmentPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    def __init__(self, state: PermissionState) -> EnvironmentPermission:...
    def __init__(self, flag: EnvironmentPermissionAccess, pathList: str) -> EnvironmentPermission:...
    def AddPathList(self, flag: EnvironmentPermissionAccess, pathList: str):...
    def GetPathList(self, flag: EnvironmentPermissionAccess) -> str:...
    def SetPathList(self, flag: EnvironmentPermissionAccess, pathList: str):...
class EnvironmentPermissionAccess(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllAccess: int
    NoAccess: int
    Read: int
    value__: int
    Write: int
class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def All(self) -> str:"""All { get; set; } -> str"""
    @property
    def Read(self) -> str:"""Read { get; set; } -> str"""
    @property
    def Write(self) -> str:"""Write { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> EnvironmentPermissionAttribute:...
class FileDialogPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    @property
    def Access(self) -> FileDialogPermissionAccess:"""Access { get; set; } -> FileDialogPermissionAccess"""
    def __init__(self, state: PermissionState) -> FileDialogPermission:...
    def __init__(self, access: FileDialogPermissionAccess) -> FileDialogPermission:...
class FileDialogPermissionAccess(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    Open: int
    OpenSave: int
    Save: int
    value__: int
class FileDialogPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Open(self) -> bool:"""Open { get; set; } -> bool"""
    @property
    def Save(self) -> bool:"""Save { get; set; } -> bool"""
    def __init__(self, action: SecurityAction) -> FileDialogPermissionAttribute:...
class FileIOPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    @property
    def AllFiles(self) -> FileIOPermissionAccess:"""AllFiles { get; set; } -> FileIOPermissionAccess"""
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:"""AllLocalFiles { get; set; } -> FileIOPermissionAccess"""
    def __init__(self, state: PermissionState) -> FileIOPermission:...
    def __init__(self, access: FileIOPermissionAccess, path: str) -> FileIOPermission:...
    def __init__(self, access: FileIOPermissionAccess, pathList: _n_0_t_4[str]) -> FileIOPermission:...
    def __init__(self, access: FileIOPermissionAccess, control: _n_4_t_0, path: str) -> FileIOPermission:...
    def __init__(self, access: FileIOPermissionAccess, control: _n_4_t_0, pathList: _n_0_t_4[str]) -> FileIOPermission:...
    def AddPathList(self, access: FileIOPermissionAccess, path: str):...
    def AddPathList(self, access: FileIOPermissionAccess, pathList: _n_0_t_4[str]):...
    def GetPathList(self, access: FileIOPermissionAccess) -> _n_0_t_4[str]:...
    def SetPathList(self, access: FileIOPermissionAccess, path: str):...
    def SetPathList(self, access: FileIOPermissionAccess, pathList: _n_0_t_4[str]):...
class FileIOPermissionAccess(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllAccess: int
    Append: int
    NoAccess: int
    PathDiscovery: int
    Read: int
    value__: int
    Write: int
class FileIOPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def All(self) -> str:"""All { get; set; } -> str"""
    @property
    def AllFiles(self) -> FileIOPermissionAccess:"""AllFiles { get; set; } -> FileIOPermissionAccess"""
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:"""AllLocalFiles { get; set; } -> FileIOPermissionAccess"""
    @property
    def Append(self) -> str:"""Append { get; set; } -> str"""
    @property
    def ChangeAccessControl(self) -> str:"""ChangeAccessControl { get; set; } -> str"""
    @property
    def PathDiscovery(self) -> str:"""PathDiscovery { get; set; } -> str"""
    @property
    def Read(self) -> str:"""Read { get; set; } -> str"""
    @property
    def ViewAccessControl(self) -> str:"""ViewAccessControl { get; set; } -> str"""
    @property
    def ViewAndModify(self) -> str:"""ViewAndModify { get; set; } -> str"""
    @property
    def Write(self) -> str:"""Write { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> FileIOPermissionAttribute:...
class GacIdentityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IBuiltInPermission):
    def __init__(self, state: PermissionState) -> GacIdentityPermission:...
    def __init__(self) -> GacIdentityPermission:...
class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    def __init__(self, action: SecurityAction) -> GacIdentityPermissionAttribute:...
class HostProtectionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def ExternalProcessMgmt(self) -> bool:"""ExternalProcessMgmt { get; set; } -> bool"""
    @property
    def ExternalThreading(self) -> bool:"""ExternalThreading { get; set; } -> bool"""
    @property
    def MayLeakOnAbort(self) -> bool:"""MayLeakOnAbort { get; set; } -> bool"""
    @property
    def Resources(self) -> HostProtectionResource:"""Resources { get; set; } -> HostProtectionResource"""
    @property
    def SecurityInfrastructure(self) -> bool:"""SecurityInfrastructure { get; set; } -> bool"""
    @property
    def SelfAffectingProcessMgmt(self) -> bool:"""SelfAffectingProcessMgmt { get; set; } -> bool"""
    @property
    def SelfAffectingThreading(self) -> bool:"""SelfAffectingThreading { get; set; } -> bool"""
    @property
    def SharedState(self) -> bool:"""SharedState { get; set; } -> bool"""
    @property
    def Synchronization(self) -> bool:"""Synchronization { get; set; } -> bool"""
    @property
    def UI(self) -> bool:"""UI { get; set; } -> bool"""
    def __init__(self) -> HostProtectionAttribute:...
    def __init__(self, action: SecurityAction) -> HostProtectionAttribute:...
class HostProtectionResource(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    All: int
    ExternalProcessMgmt: int
    ExternalThreading: int
    MayLeakOnAbort: int
    _None: int
    SecurityInfrastructure: int
    SelfAffectingProcessMgmt: int
    SelfAffectingThreading: int
    SharedState: int
    Synchronization: int
    UI: int
    value__: int
class IsolatedStorageContainment(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AdministerIsolatedStorageByUser: int
    ApplicationIsolationByMachine: int
    ApplicationIsolationByRoamingUser: int
    ApplicationIsolationByUser: int
    AssemblyIsolationByMachine: int
    AssemblyIsolationByRoamingUser: int
    AssemblyIsolationByUser: int
    DomainIsolationByMachine: int
    DomainIsolationByRoamingUser: int
    DomainIsolationByUser: int
    _None: int
    UnrestrictedIsolatedStorage: int
    value__: int
class IsolatedStorageFilePermission(IsolatedStoragePermission, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    def __init__(self, state: PermissionState) -> IsolatedStorageFilePermission:...
class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute, _n_2_t_0):
    def __init__(self, action: SecurityAction) -> IsolatedStorageFilePermissionAttribute:...
class IsolatedStoragePermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission):
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:"""UsageAllowed { get; set; } -> IsolatedStorageContainment"""
    @property
    def UserQuota(self) -> int:"""UserQuota { get; set; } -> int"""
class IsolatedStoragePermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:"""UsageAllowed { get; set; } -> IsolatedStorageContainment"""
    @property
    def UserQuota(self) -> int:"""UserQuota { get; set; } -> int"""
class IUnrestrictedPermission():
    def IsUnrestricted(self) -> bool:...
class KeyContainerPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    @property
    def AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection:"""AccessEntries { get; } -> KeyContainerPermissionAccessEntryCollection"""
    @property
    def Flags(self) -> KeyContainerPermissionFlags:"""Flags { get; } -> KeyContainerPermissionFlags"""
    def __init__(self, flags: KeyContainerPermissionFlags) -> KeyContainerPermission:...
    def __init__(self, state: PermissionState) -> KeyContainerPermission:...
    def __init__(self, flags: KeyContainerPermissionFlags, accessList: _n_0_t_4[KeyContainerPermissionAccessEntry]) -> KeyContainerPermission:...
class KeyContainerPermissionAccessEntry(object):
    @property
    def Flags(self) -> KeyContainerPermissionFlags:"""Flags { get; set; } -> KeyContainerPermissionFlags"""
    @property
    def KeyContainerName(self) -> str:"""KeyContainerName { get; set; } -> str"""
    @property
    def KeySpec(self) -> int:"""KeySpec { get; set; } -> int"""
    @property
    def KeyStore(self) -> str:"""KeyStore { get; set; } -> str"""
    @property
    def ProviderName(self) -> str:"""ProviderName { get; set; } -> str"""
    @property
    def ProviderType(self) -> int:"""ProviderType { get; set; } -> int"""
    def __init__(self, keyContainerName: str, flags: KeyContainerPermissionFlags) -> KeyContainerPermissionAccessEntry:...
    def __init__(self, parameters: _n_5_t_0, flags: KeyContainerPermissionFlags) -> KeyContainerPermissionAccessEntry:...
    def __init__(self, keyStore: str, providerName: str, providerType: int, keyContainerName: str, keySpec: int, flags: KeyContainerPermissionFlags) -> KeyContainerPermissionAccessEntry:...
class KeyContainerPermissionAccessEntryCollection(_n_1_t_0, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> KeyContainerPermissionAccessEntry:"""Item { get; } -> KeyContainerPermissionAccessEntry"""
    def Add(self, accessEntry: KeyContainerPermissionAccessEntry) -> int:...
    def Clear(self):...
    def IndexOf(self, accessEntry: KeyContainerPermissionAccessEntry) -> int:...
    def Remove(self, accessEntry: KeyContainerPermissionAccessEntry):...
class KeyContainerPermissionAccessEntryEnumerator(_n_1_t_1):
    pass
class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Flags(self) -> KeyContainerPermissionFlags:"""Flags { get; set; } -> KeyContainerPermissionFlags"""
    @property
    def KeyContainerName(self) -> str:"""KeyContainerName { get; set; } -> str"""
    @property
    def KeySpec(self) -> int:"""KeySpec { get; set; } -> int"""
    @property
    def KeyStore(self) -> str:"""KeyStore { get; set; } -> str"""
    @property
    def ProviderName(self) -> str:"""ProviderName { get; set; } -> str"""
    @property
    def ProviderType(self) -> int:"""ProviderType { get; set; } -> int"""
    def __init__(self, action: SecurityAction) -> KeyContainerPermissionAttribute:...
class KeyContainerPermissionFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllFlags: int
    ChangeAcl: int
    Create: int
    Decrypt: int
    Delete: int
    Export: int
    Import: int
    NoFlags: int
    Open: int
    Sign: int
    value__: int
    ViewAcl: int
class PermissionSetAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def File(self) -> str:"""File { get; set; } -> str"""
    @property
    def Hex(self) -> str:"""Hex { get; set; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def UnicodeEncoded(self) -> bool:"""UnicodeEncoded { get; set; } -> bool"""
    @property
    def XML(self) -> str:"""XML { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> PermissionSetAttribute:...
    def CreatePermissionSet(self) -> _n_3_t_3:...
class PermissionState(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    Unrestricted: int
    value__: int
class PrincipalPermission(_n_3_t_1, IUnrestrictedPermission, IBuiltInPermission):
    def __init__(self, state: PermissionState) -> PrincipalPermission:...
    def __init__(self, name: str, role: str) -> PrincipalPermission:...
    def __init__(self, name: str, role: str, isAuthenticated: bool) -> PrincipalPermission:...
class PrincipalPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Authenticated(self) -> bool:"""Authenticated { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Role(self) -> str:"""Role { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> PrincipalPermissionAttribute:...
class PublisherIdentityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IBuiltInPermission):
    @property
    def Certificate(self) -> _n_6_t_0:"""Certificate { get; set; } -> X509Certificate"""
    def __init__(self, state: PermissionState) -> PublisherIdentityPermission:...
    def __init__(self, certificate: _n_6_t_0) -> PublisherIdentityPermission:...
class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def CertFile(self) -> str:"""CertFile { get; set; } -> str"""
    @property
    def SignedFile(self) -> str:"""SignedFile { get; set; } -> str"""
    @property
    def X509Certificate(self) -> str:"""X509Certificate { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> PublisherIdentityPermissionAttribute:...
class ReflectionPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    @property
    def Flags(self) -> ReflectionPermissionFlag:"""Flags { get; set; } -> ReflectionPermissionFlag"""
    def __init__(self, state: PermissionState) -> ReflectionPermission:...
    def __init__(self, flag: ReflectionPermissionFlag) -> ReflectionPermission:...
class ReflectionPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Flags(self) -> ReflectionPermissionFlag:"""Flags { get; set; } -> ReflectionPermissionFlag"""
    @property
    def MemberAccess(self) -> bool:"""MemberAccess { get; set; } -> bool"""
    @property
    def ReflectionEmit(self) -> bool:"""ReflectionEmit { get; set; } -> bool"""
    @property
    def RestrictedMemberAccess(self) -> bool:"""RestrictedMemberAccess { get; set; } -> bool"""
    @property
    def TypeInformation(self) -> bool:"""TypeInformation { get; set; } -> bool"""
    def __init__(self, action: SecurityAction) -> ReflectionPermissionAttribute:...
class ReflectionPermissionFlag(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllFlags: int
    MemberAccess: int
    NoFlags: int
    ReflectionEmit: int
    RestrictedMemberAccess: int
    TypeInformation: int
    value__: int
class RegistryPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    def __init__(self, state: PermissionState) -> RegistryPermission:...
    def __init__(self, access: RegistryPermissionAccess, pathList: str) -> RegistryPermission:...
    def __init__(self, access: RegistryPermissionAccess, control: _n_4_t_0, pathList: str) -> RegistryPermission:...
    def AddPathList(self, access: RegistryPermissionAccess, pathList: str):...
    def AddPathList(self, access: RegistryPermissionAccess, control: _n_4_t_0, pathList: str):...
    def GetPathList(self, access: RegistryPermissionAccess) -> str:...
    def SetPathList(self, access: RegistryPermissionAccess, pathList: str):...
class RegistryPermissionAccess(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllAccess: int
    Create: int
    NoAccess: int
    Read: int
    value__: int
    Write: int
class RegistryPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def All(self) -> str:"""All { get; set; } -> str"""
    @property
    def ChangeAccessControl(self) -> str:"""ChangeAccessControl { get; set; } -> str"""
    @property
    def Create(self) -> str:"""Create { get; set; } -> str"""
    @property
    def Read(self) -> str:"""Read { get; set; } -> str"""
    @property
    def ViewAccessControl(self) -> str:"""ViewAccessControl { get; set; } -> str"""
    @property
    def ViewAndModify(self) -> str:"""ViewAndModify { get; set; } -> str"""
    @property
    def Write(self) -> str:"""Write { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> RegistryPermissionAttribute:...
class ResourcePermissionBase(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission):
    Any: int
    Local: int
class ResourcePermissionBaseEntry(object):
    @property
    def PermissionAccess(self) -> int:"""PermissionAccess { get; } -> int"""
    @property
    def PermissionAccessPath(self) -> _n_0_t_4[str]:"""PermissionAccessPath { get; } -> Array"""
    def __init__(self) -> ResourcePermissionBaseEntry:...
    def __init__(self, permissionAccess: int, permissionAccessPath: _n_0_t_4[str]) -> ResourcePermissionBaseEntry:...
class SecurityAction(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Assert: int
    Demand: int
    Deny: int
    InheritanceDemand: int
    LinkDemand: int
    PermitOnly: int
    RequestMinimum: int
    RequestOptional: int
    RequestRefuse: int
    value__: int
class SecurityAttribute(_n_0_t_5, _n_2_t_0):
    @property
    def Action(self) -> SecurityAction:"""Action { get; set; } -> SecurityAction"""
    @property
    def Unrestricted(self) -> bool:"""Unrestricted { get; set; } -> bool"""
    def CreatePermission(self) -> _n_3_t_1:...
class SecurityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    @property
    def Flags(self) -> SecurityPermissionFlag:"""Flags { get; set; } -> SecurityPermissionFlag"""
    def __init__(self, state: PermissionState) -> SecurityPermission:...
    def __init__(self, flag: SecurityPermissionFlag) -> SecurityPermission:...
class SecurityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Assertion(self) -> bool:"""Assertion { get; set; } -> bool"""
    @property
    def BindingRedirects(self) -> bool:"""BindingRedirects { get; set; } -> bool"""
    @property
    def ControlAppDomain(self) -> bool:"""ControlAppDomain { get; set; } -> bool"""
    @property
    def ControlDomainPolicy(self) -> bool:"""ControlDomainPolicy { get; set; } -> bool"""
    @property
    def ControlEvidence(self) -> bool:"""ControlEvidence { get; set; } -> bool"""
    @property
    def ControlPolicy(self) -> bool:"""ControlPolicy { get; set; } -> bool"""
    @property
    def ControlPrincipal(self) -> bool:"""ControlPrincipal { get; set; } -> bool"""
    @property
    def ControlThread(self) -> bool:"""ControlThread { get; set; } -> bool"""
    @property
    def Execution(self) -> bool:"""Execution { get; set; } -> bool"""
    @property
    def Flags(self) -> SecurityPermissionFlag:"""Flags { get; set; } -> SecurityPermissionFlag"""
    @property
    def Infrastructure(self) -> bool:"""Infrastructure { get; set; } -> bool"""
    @property
    def RemotingConfiguration(self) -> bool:"""RemotingConfiguration { get; set; } -> bool"""
    @property
    def SerializationFormatter(self) -> bool:"""SerializationFormatter { get; set; } -> bool"""
    @property
    def SkipVerification(self) -> bool:"""SkipVerification { get; set; } -> bool"""
    @property
    def UnmanagedCode(self) -> bool:"""UnmanagedCode { get; set; } -> bool"""
    def __init__(self, action: SecurityAction) -> SecurityPermissionAttribute:...
class SecurityPermissionFlag(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllFlags: int
    Assertion: int
    BindingRedirects: int
    ControlAppDomain: int
    ControlDomainPolicy: int
    ControlEvidence: int
    ControlPolicy: int
    ControlPrincipal: int
    ControlThread: int
    Execution: int
    Infrastructure: int
    NoFlags: int
    RemotingConfiguration: int
    SerializationFormatter: int
    SkipVerification: int
    UnmanagedCode: int
    value__: int
class SiteIdentityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IBuiltInPermission):
    @property
    def Site(self) -> str:"""Site { get; set; } -> str"""
    def __init__(self, state: PermissionState) -> SiteIdentityPermission:...
    def __init__(self, site: str) -> SiteIdentityPermission:...
class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Site(self) -> str:"""Site { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> SiteIdentityPermissionAttribute:...
class StorePermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission):
    @property
    def Flags(self) -> StorePermissionFlags:"""Flags { get; set; } -> StorePermissionFlags"""
    def __init__(self, flag: StorePermissionFlags) -> StorePermission:...
    def __init__(self, state: PermissionState) -> StorePermission:...
class StorePermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def AddToStore(self) -> bool:"""AddToStore { get; set; } -> bool"""
    @property
    def CreateStore(self) -> bool:"""CreateStore { get; set; } -> bool"""
    @property
    def DeleteStore(self) -> bool:"""DeleteStore { get; set; } -> bool"""
    @property
    def EnumerateCertificates(self) -> bool:"""EnumerateCertificates { get; set; } -> bool"""
    @property
    def EnumerateStores(self) -> bool:"""EnumerateStores { get; set; } -> bool"""
    @property
    def Flags(self) -> StorePermissionFlags:"""Flags { get; set; } -> StorePermissionFlags"""
    @property
    def OpenStore(self) -> bool:"""OpenStore { get; set; } -> bool"""
    @property
    def RemoveFromStore(self) -> bool:"""RemoveFromStore { get; set; } -> bool"""
    def __init__(self, action: SecurityAction) -> StorePermissionAttribute:...
class StorePermissionFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AddToStore: int
    AllFlags: int
    CreateStore: int
    DeleteStore: int
    EnumerateCertificates: int
    EnumerateStores: int
    NoFlags: int
    OpenStore: int
    RemoveFromStore: int
    value__: int
class StrongNameIdentityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IBuiltInPermission):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:"""PublicKey { get; set; } -> StrongNamePublicKeyBlob"""
    @property
    def Version(self) -> _n_0_t_6:"""Version { get; set; } -> Version"""
    def __init__(self, state: PermissionState) -> StrongNameIdentityPermission:...
    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: _n_0_t_6) -> StrongNameIdentityPermission:...
class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PublicKey(self) -> str:"""PublicKey { get; set; } -> str"""
    @property
    def Version(self) -> str:"""Version { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> StrongNameIdentityPermissionAttribute:...
class StrongNamePublicKeyBlob(object):
    def __init__(self, publicKey: _n_0_t_4[_n_0_t_7]) -> StrongNamePublicKeyBlob:...
class TypeDescriptorPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission):
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:"""Flags { get; set; } -> TypeDescriptorPermissionFlags"""
    def __init__(self, flag: TypeDescriptorPermissionFlags) -> TypeDescriptorPermission:...
    def __init__(self, state: PermissionState) -> TypeDescriptorPermission:...
class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:"""Flags { get; set; } -> TypeDescriptorPermissionFlags"""
    @property
    def RestrictedRegistrationAccess(self) -> bool:"""RestrictedRegistrationAccess { get; set; } -> bool"""
    def __init__(self, action: SecurityAction) -> TypeDescriptorPermissionAttribute:...
class TypeDescriptorPermissionFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    NoFlags: int
    RestrictedRegistrationAccess: int
    value__: int
class UIPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IUnrestrictedPermission, IBuiltInPermission):
    @property
    def Clipboard(self) -> UIPermissionClipboard:"""Clipboard { get; set; } -> UIPermissionClipboard"""
    @property
    def Window(self) -> UIPermissionWindow:"""Window { get; set; } -> UIPermissionWindow"""
    def __init__(self, state: PermissionState) -> UIPermission:...
    def __init__(self, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard) -> UIPermission:...
    def __init__(self, windowFlag: UIPermissionWindow) -> UIPermission:...
    def __init__(self, clipboardFlag: UIPermissionClipboard) -> UIPermission:...
class UIPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Clipboard(self) -> UIPermissionClipboard:"""Clipboard { get; set; } -> UIPermissionClipboard"""
    @property
    def Window(self) -> UIPermissionWindow:"""Window { get; set; } -> UIPermissionWindow"""
    def __init__(self, action: SecurityAction) -> UIPermissionAttribute:...
class UIPermissionClipboard(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllClipboard: int
    NoClipboard: int
    OwnClipboard: int
    value__: int
class UIPermissionWindow(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllWindows: int
    NoWindows: int
    SafeSubWindows: int
    SafeTopLevelWindows: int
    value__: int
class UrlIdentityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IBuiltInPermission):
    @property
    def Url(self) -> str:"""Url { get; set; } -> str"""
    def __init__(self, state: PermissionState) -> UrlIdentityPermission:...
    def __init__(self, site: str) -> UrlIdentityPermission:...
class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Url(self) -> str:"""Url { get; set; } -> str"""
    def __init__(self, action: SecurityAction) -> UrlIdentityPermissionAttribute:...
class ZoneIdentityPermission(_n_3_t_0, _n_3_t_1, _n_3_t_2, IBuiltInPermission):
    @property
    def SecurityZone(self) -> _n_3_t_4:"""SecurityZone { get; set; } -> SecurityZone"""
    def __init__(self, state: PermissionState) -> ZoneIdentityPermission:...
    def __init__(self, zone: _n_3_t_4) -> ZoneIdentityPermission:...
class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute, _n_2_t_0):
    @property
    def Zone(self) -> _n_3_t_4:"""Zone { get; set; } -> SecurityZone"""
    def __init__(self, action: SecurityAction) -> ZoneIdentityPermissionAttribute:...
