from __clrclasses__.Microsoft.Win32.SafeHandles import SafeX509ChainHandle as _n_0_t_0
from __clrclasses__.System import Uri as _n_1_t_0
from __clrclasses__.System import DateTimeOffset as _n_1_t_1
from __clrclasses__.System import Byte as _n_1_t_2
from __clrclasses__.System import Array as _n_1_t_3
from __clrclasses__.System import Enum as _n_1_t_4
from __clrclasses__.System import IComparable as _n_1_t_5
from __clrclasses__.System import IFormattable as _n_1_t_6
from __clrclasses__.System import IConvertible as _n_1_t_7
from __clrclasses__.System import DateTime as _n_1_t_8
from __clrclasses__.System import IDisposable as _n_1_t_9
from __clrclasses__.System import IntPtr as _n_1_t_10
from __clrclasses__.System import TimeSpan as _n_1_t_11
from __clrclasses__.System import ValueType as _n_1_t_12
from __clrclasses__.System.Collections import IList as _n_2_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_2_t_1
from __clrclasses__.System.Collections import CollectionBase as _n_2_t_2
from __clrclasses__.System.Collections import ICollection as _n_2_t_3
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_3_t_0
from __clrclasses__.System.Net import IPAddress as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_5_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_1
from __clrclasses__.System.Runtime.Serialization import SerializationInfo as _n_5_t_2
from __clrclasses__.System.Runtime.Serialization import StreamingContext as _n_5_t_3
from __clrclasses__.System.Security import SecureString as _n_6_t_0
from __clrclasses__.System.Security.Cryptography import SignatureVerificationResult as _n_7_t_0
from __clrclasses__.System.Security.Cryptography import HashAlgorithmName as _n_7_t_1
from __clrclasses__.System.Security.Cryptography import ECDsa as _n_7_t_2
from __clrclasses__.System.Security.Cryptography import RSA as _n_7_t_3
from __clrclasses__.System.Security.Cryptography import RSASignaturePadding as _n_7_t_4
from __clrclasses__.System.Security.Cryptography import DSA as _n_7_t_5
from __clrclasses__.System.Security.Cryptography import AsnEncodedData as _n_7_t_6
from __clrclasses__.System.Security.Cryptography import AsymmetricAlgorithm as _n_7_t_7
from __clrclasses__.System.Security.Cryptography import Oid as _n_7_t_8
from __clrclasses__.System.Security.Cryptography import OidCollection as _n_7_t_9
import typing
class AuthenticodeSignatureInformation(object):
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def DescriptionUrl(self) -> _n_1_t_0:"""DescriptionUrl { get; } -> Uri"""
    @property
    def HashAlgorithm(self) -> str:"""HashAlgorithm { get; } -> str"""
    @property
    def HResult(self) -> int:"""HResult { get; } -> int"""
    @property
    def SignatureChain(self) -> X509Chain:"""SignatureChain { get; } -> X509Chain"""
    @property
    def SigningCertificate(self) -> X509Certificate2:"""SigningCertificate { get; } -> X509Certificate2"""
    @property
    def Timestamp(self) -> TimestampInformation:"""Timestamp { get; } -> TimestampInformation"""
    @property
    def TrustStatus(self) -> TrustStatus:"""TrustStatus { get; } -> TrustStatus"""
    @property
    def VerificationResult(self) -> _n_7_t_0:"""VerificationResult { get; } -> SignatureVerificationResult"""
class CertificateRequest(object):
    @property
    def CertificateExtensions(self) -> _n_3_t_0[X509Extension]:"""CertificateExtensions { get; } -> Collection"""
    @property
    def HashAlgorithm(self) -> _n_7_t_1:"""HashAlgorithm { get; } -> HashAlgorithmName"""
    @property
    def PublicKey(self) -> PublicKey:"""PublicKey { get; } -> PublicKey"""
    @property
    def SubjectName(self) -> X500DistinguishedName:"""SubjectName { get; } -> X500DistinguishedName"""
    def __init__(self, subjectName: str, key: _n_7_t_2, hashAlgorithm: _n_7_t_1) -> CertificateRequest:...
    def __init__(self, subjectName: X500DistinguishedName, key: _n_7_t_2, hashAlgorithm: _n_7_t_1) -> CertificateRequest:...
    def __init__(self, subjectName: str, key: _n_7_t_3, hashAlgorithm: _n_7_t_1, padding: _n_7_t_4) -> CertificateRequest:...
    def __init__(self, subjectName: X500DistinguishedName, key: _n_7_t_3, hashAlgorithm: _n_7_t_1, padding: _n_7_t_4) -> CertificateRequest:...
    def __init__(self, subjectName: X500DistinguishedName, publicKey: PublicKey, hashAlgorithm: _n_7_t_1) -> CertificateRequest:...
    def Create(self, issuerCertificate: X509Certificate2, notBefore: _n_1_t_1, notAfter: _n_1_t_1, serialNumber: _n_1_t_3[_n_1_t_2]) -> X509Certificate2:...
    def Create(self, issuerName: X500DistinguishedName, generator: X509SignatureGenerator, notBefore: _n_1_t_1, notAfter: _n_1_t_1, serialNumber: _n_1_t_3[_n_1_t_2]) -> X509Certificate2:...
    def CreateSelfSigned(self, notBefore: _n_1_t_1, notAfter: _n_1_t_1) -> X509Certificate2:...
    def CreateSigningRequest(self) -> _n_1_t_3[_n_1_t_2]:...
    def CreateSigningRequest(self, signatureGenerator: X509SignatureGenerator) -> _n_1_t_3[_n_1_t_2]:...
class DSACertificateExtensions(object):
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: _n_7_t_5) -> X509Certificate2:...
    @staticmethod
    def GetDSAPrivateKey(certificate: X509Certificate2) -> _n_7_t_5:...
    @staticmethod
    def GetDSAPublicKey(certificate: X509Certificate2) -> _n_7_t_5:...
class ECDsaCertificateExtensions(object):
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: _n_7_t_2) -> X509Certificate2:...
    @staticmethod
    def GetECDsaPrivateKey(certificate: X509Certificate2) -> _n_7_t_2:...
    @staticmethod
    def GetECDsaPublicKey(certificate: X509Certificate2) -> _n_7_t_2:...
class OpenFlags(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    IncludeArchived: int
    MaxAllowed: int
    OpenExistingOnly: int
    ReadOnly: int
    ReadWrite: int
    value__: int
class PublicKey(object):
    @property
    def EncodedKeyValue(self) -> _n_7_t_6:"""EncodedKeyValue { get; } -> AsnEncodedData"""
    @property
    def EncodedParameters(self) -> _n_7_t_6:"""EncodedParameters { get; } -> AsnEncodedData"""
    @property
    def Key(self) -> _n_7_t_7:"""Key { get; } -> AsymmetricAlgorithm"""
    @property
    def Oid(self) -> _n_7_t_8:"""Oid { get; } -> Oid"""
    def __init__(self, oid: _n_7_t_8, parameters: _n_7_t_6, keyValue: _n_7_t_6) -> PublicKey:...
class RSACertificateExtensions(object):
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: _n_7_t_3) -> X509Certificate2:...
    @staticmethod
    def GetRSAPrivateKey(certificate: X509Certificate2) -> _n_7_t_3:...
    @staticmethod
    def GetRSAPublicKey(certificate: X509Certificate2) -> _n_7_t_3:...
class StoreLocation(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    CurrentUser: int
    LocalMachine: int
    value__: int
class StoreName(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    AddressBook: int
    AuthRoot: int
    CertificateAuthority: int
    Disallowed: int
    My: int
    Root: int
    TrustedPeople: int
    TrustedPublisher: int
    value__: int
class SubjectAlternativeNameBuilder(object):
    def __init__(self) -> SubjectAlternativeNameBuilder:...
    def AddDnsName(self, dnsName: str):...
    def AddEmailAddress(self, emailAddress: str):...
    def AddIpAddress(self, ipAddress: _n_4_t_0):...
    def AddUri(self, uri: _n_1_t_0):...
    def AddUserPrincipalName(self, upn: str):...
    def Build(self, critical: bool) -> X509Extension:...
class TimestampInformation(object):
    @property
    def HashAlgorithm(self) -> str:"""HashAlgorithm { get; } -> str"""
    @property
    def HResult(self) -> int:"""HResult { get; } -> int"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def SignatureChain(self) -> X509Chain:"""SignatureChain { get; } -> X509Chain"""
    @property
    def SigningCertificate(self) -> X509Certificate2:"""SigningCertificate { get; } -> X509Certificate2"""
    @property
    def Timestamp(self) -> _n_1_t_8:"""Timestamp { get; } -> DateTime"""
    @property
    def VerificationResult(self) -> _n_7_t_0:"""VerificationResult { get; } -> SignatureVerificationResult"""
class TrustStatus(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    KnownIdentity: int
    Trusted: int
    UnknownIdentity: int
    Untrusted: int
    value__: int
class X500DistinguishedName(_n_7_t_6):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, distinguishedName: str, flag: X500DistinguishedNameFlags) -> X500DistinguishedName:...
    def __init__(self, distinguishedName: str) -> X500DistinguishedName:...
    def __init__(self, distinguishedName: X500DistinguishedName) -> X500DistinguishedName:...
    def __init__(self, encodedDistinguishedName: _n_7_t_6) -> X500DistinguishedName:...
    def __init__(self, encodedDistinguishedName: _n_1_t_3[_n_1_t_2]) -> X500DistinguishedName:...
    def Decode(self, flag: X500DistinguishedNameFlags) -> str:...
class X500DistinguishedNameFlags(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    DoNotUsePlusSign: int
    DoNotUseQuotes: int
    ForceUTF8Encoding: int
    _None: int
    Reversed: int
    UseCommas: int
    UseNewLines: int
    UseSemicolons: int
    UseT61Encoding: int
    UseUTF8Encoding: int
    value__: int
class X509BasicConstraintsExtension(X509Extension):
    @property
    def CertificateAuthority(self) -> bool:"""CertificateAuthority { get; } -> bool"""
    @property
    def HasPathLengthConstraint(self) -> bool:"""HasPathLengthConstraint { get; } -> bool"""
    @property
    def PathLengthConstraint(self) -> int:"""PathLengthConstraint { get; } -> int"""
    def __init__(self, encodedBasicConstraints: _n_7_t_6, critical: bool) -> X509BasicConstraintsExtension:...
    def __init__(self, certificateAuthority: bool, hasPathLengthConstraint: bool, pathLengthConstraint: int, critical: bool) -> X509BasicConstraintsExtension:...
    def __init__(self) -> X509BasicConstraintsExtension:...
class X509Certificate(_n_1_t_9, _n_5_t_0, _n_5_t_1):
    @property
    def Handle(self) -> _n_1_t_10:"""Handle { get; } -> IntPtr"""
    @property
    def Issuer(self) -> str:"""Issuer { get; } -> str"""
    @property
    def Subject(self) -> str:"""Subject { get; } -> str"""
    def __init__(self, info: _n_5_t_2, context: _n_5_t_3) -> X509Certificate:...
    def __init__(self, cert: X509Certificate) -> X509Certificate:...
    def __init__(self, fileName: str, password: _n_6_t_0, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate:...
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate:...
    def __init__(self, fileName: str, password: _n_6_t_0) -> X509Certificate:...
    def __init__(self, fileName: str, password: str) -> X509Certificate:...
    def __init__(self, fileName: str) -> X509Certificate:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: _n_6_t_0, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: str, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: _n_6_t_0) -> X509Certificate:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: str) -> X509Certificate:...
    def __init__(self, data: _n_1_t_3[_n_1_t_2]) -> X509Certificate:...
    def __init__(self) -> X509Certificate:...
    def __init__(self, handle: _n_1_t_10) -> X509Certificate:...
    @staticmethod
    def CreateFromCertFile(filename: str) -> X509Certificate:...
    @staticmethod
    def CreateFromSignedFile(filename: str) -> X509Certificate:...
    def Export(self, contentType: X509ContentType, password: _n_6_t_0) -> _n_1_t_3[_n_1_t_2]:...
    def Export(self, contentType: X509ContentType, password: str) -> _n_1_t_3[_n_1_t_2]:...
    def Export(self, contentType: X509ContentType) -> _n_1_t_3[_n_1_t_2]:...
    def GetCertHash(self) -> _n_1_t_3[_n_1_t_2]:...
    def GetCertHashString(self) -> str:...
    def GetEffectiveDateString(self) -> str:...
    def GetExpirationDateString(self) -> str:...
    def GetFormat(self) -> str:...
    def GetIssuerName(self) -> str:...
    def GetKeyAlgorithm(self) -> str:...
    def GetKeyAlgorithmParameters(self) -> _n_1_t_3[_n_1_t_2]:...
    def GetKeyAlgorithmParametersString(self) -> str:...
    def GetName(self) -> str:...
    def GetPublicKey(self) -> _n_1_t_3[_n_1_t_2]:...
    def GetPublicKeyString(self) -> str:...
    def GetRawCertData(self) -> _n_1_t_3[_n_1_t_2]:...
    def GetRawCertDataString(self) -> str:...
    def GetSerialNumber(self) -> _n_1_t_3[_n_1_t_2]:...
    def GetSerialNumberString(self) -> str:...
    def Import(self, fileName: str, password: _n_6_t_0, keyStorageFlags: X509KeyStorageFlags):...
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags):...
    def Import(self, fileName: str):...
    def Import(self, rawData: _n_1_t_3[_n_1_t_2], password: _n_6_t_0, keyStorageFlags: X509KeyStorageFlags):...
    def Import(self, rawData: _n_1_t_3[_n_1_t_2], password: str, keyStorageFlags: X509KeyStorageFlags):...
    def Import(self, rawData: _n_1_t_3[_n_1_t_2]):...
    def Reset(self):...
class X509Certificate2(X509Certificate, _n_1_t_9, _n_5_t_0, _n_5_t_1):
    @property
    def Archived(self) -> bool:"""Archived { get; set; } -> bool"""
    @property
    def Extensions(self) -> X509ExtensionCollection:"""Extensions { get; } -> X509ExtensionCollection"""
    @property
    def FriendlyName(self) -> str:"""FriendlyName { get; set; } -> str"""
    @property
    def HasPrivateKey(self) -> bool:"""HasPrivateKey { get; } -> bool"""
    @property
    def IssuerName(self) -> X500DistinguishedName:"""IssuerName { get; } -> X500DistinguishedName"""
    @property
    def NotAfter(self) -> _n_1_t_8:"""NotAfter { get; } -> DateTime"""
    @property
    def NotBefore(self) -> _n_1_t_8:"""NotBefore { get; } -> DateTime"""
    @property
    def PrivateKey(self) -> _n_7_t_7:"""PrivateKey { get; set; } -> AsymmetricAlgorithm"""
    @property
    def PublicKey(self) -> PublicKey:"""PublicKey { get; } -> PublicKey"""
    @property
    def RawData(self) -> _n_1_t_3[_n_1_t_2]:"""RawData { get; } -> Array"""
    @property
    def SerialNumber(self) -> str:"""SerialNumber { get; } -> str"""
    @property
    def SignatureAlgorithm(self) -> _n_7_t_8:"""SignatureAlgorithm { get; } -> Oid"""
    @property
    def SubjectName(self) -> X500DistinguishedName:"""SubjectName { get; } -> X500DistinguishedName"""
    @property
    def Thumbprint(self) -> str:"""Thumbprint { get; } -> str"""
    @property
    def Version(self) -> int:"""Version { get; } -> int"""
    def __init__(self, certificate: X509Certificate) -> X509Certificate2:...
    def __init__(self, handle: _n_1_t_10) -> X509Certificate2:...
    def __init__(self, fileName: str, password: _n_6_t_0, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate2:...
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate2:...
    def __init__(self, fileName: str, password: _n_6_t_0) -> X509Certificate2:...
    def __init__(self, fileName: str, password: str) -> X509Certificate2:...
    def __init__(self, fileName: str) -> X509Certificate2:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: _n_6_t_0, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate2:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: str, keyStorageFlags: X509KeyStorageFlags) -> X509Certificate2:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: _n_6_t_0) -> X509Certificate2:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2], password: str) -> X509Certificate2:...
    def __init__(self, rawData: _n_1_t_3[_n_1_t_2]) -> X509Certificate2:...
    def __init__(self) -> X509Certificate2:...
    @staticmethod
    def GetCertContentType(fileName: str) -> X509ContentType:...
    @staticmethod
    def GetCertContentType(rawData: _n_1_t_3[_n_1_t_2]) -> X509ContentType:...
    def GetNameInfo(self, nameType: X509NameType, forIssuer: bool) -> str:...
    def Verify(self) -> bool:...
    def CopyWithPrivateKey(self, privateKey: _n_7_t_5) -> X509Certificate2:
        """Extension from: System.Security.Cryptography.X509Certificates.DSACertificateExtensions"""
    def CopyWithPrivateKey(self, privateKey: _n_7_t_2) -> X509Certificate2:
        """Extension from: System.Security.Cryptography.X509Certificates.ECDsaCertificateExtensions"""
    def CopyWithPrivateKey(self, privateKey: _n_7_t_3) -> X509Certificate2:
        """Extension from: System.Security.Cryptography.X509Certificates.RSACertificateExtensions"""
    def GetDSAPrivateKey(self) -> _n_7_t_5:
        """Extension from: System.Security.Cryptography.X509Certificates.DSACertificateExtensions"""
    def GetDSAPublicKey(self) -> _n_7_t_5:
        """Extension from: System.Security.Cryptography.X509Certificates.DSACertificateExtensions"""
    def GetECDsaPrivateKey(self) -> _n_7_t_2:
        """Extension from: System.Security.Cryptography.X509Certificates.ECDsaCertificateExtensions"""
    def GetECDsaPublicKey(self) -> _n_7_t_2:
        """Extension from: System.Security.Cryptography.X509Certificates.ECDsaCertificateExtensions"""
    def GetRSAPrivateKey(self) -> _n_7_t_3:
        """Extension from: System.Security.Cryptography.X509Certificates.RSACertificateExtensions"""
    def GetRSAPublicKey(self) -> _n_7_t_3:
        """Extension from: System.Security.Cryptography.X509Certificates.RSACertificateExtensions"""
class X509Certificate2Collection(X509CertificateCollection, _n_2_t_0, typing.Iterable[X509Certificate2]):
    def __init__(self, certificates: _n_1_t_3[X509Certificate2]) -> X509Certificate2Collection:...
    def __init__(self, certificates: X509Certificate2Collection) -> X509Certificate2Collection:...
    def __init__(self, certificate: X509Certificate2) -> X509Certificate2Collection:...
    def __init__(self) -> X509Certificate2Collection:...
    def Export(self, contentType: X509ContentType, password: str) -> _n_1_t_3[_n_1_t_2]:...
    def Export(self, contentType: X509ContentType) -> _n_1_t_3[_n_1_t_2]:...
    def Find(self, findType: X509FindType, findValue: object, validOnly: bool) -> X509Certificate2Collection:...
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags):...
    def Import(self, fileName: str):...
    def Import(self, rawData: _n_1_t_3[_n_1_t_2], password: str, keyStorageFlags: X509KeyStorageFlags):...
    def Import(self, rawData: _n_1_t_3[_n_1_t_2]):...
    def RemoveRange(self, certificates: X509Certificate2Collection):...
    def RemoveRange(self, certificates: _n_1_t_3[X509Certificate2]):...
class X509Certificate2Enumerator(_n_2_t_1):
    pass
class X509CertificateCollection(_n_2_t_2, _n_2_t_0, typing.Iterable[X509Certificate]):
    def __init__(self, value: _n_1_t_3[X509Certificate]) -> X509CertificateCollection:...
    def __init__(self, value: X509CertificateCollection) -> X509CertificateCollection:...
    def __init__(self) -> X509CertificateCollection:...
    def AddRange(self, value: X509CertificateCollection):...
    def AddRange(self, value: _n_1_t_3[X509Certificate]):...
    class X509CertificateEnumerator(_n_2_t_1):
        def __init__(self, mappings: X509CertificateCollection) -> X509CertificateCollection.X509CertificateEnumerator:...
class X509Chain(_n_1_t_9):
    @property
    def ChainContext(self) -> _n_1_t_10:"""ChainContext { get; } -> IntPtr"""
    @property
    def ChainElements(self) -> X509ChainElementCollection:"""ChainElements { get; } -> X509ChainElementCollection"""
    @property
    def ChainPolicy(self) -> X509ChainPolicy:"""ChainPolicy { get; set; } -> X509ChainPolicy"""
    @property
    def ChainStatus(self) -> _n_1_t_3[X509ChainStatus]:"""ChainStatus { get; } -> Array"""
    @property
    def SafeHandle(self) -> _n_0_t_0:"""SafeHandle { get; } -> SafeX509ChainHandle"""
    def __init__(self, chainContext: _n_1_t_10) -> X509Chain:...
    def __init__(self) -> X509Chain:...
    def __init__(self, useMachineContext: bool) -> X509Chain:...
    def Build(self, certificate: X509Certificate2) -> bool:...
    @staticmethod
    def Create() -> X509Chain:...
    def Reset(self):...
class X509ChainElement(object):
    @property
    def Certificate(self) -> X509Certificate2:"""Certificate { get; } -> X509Certificate2"""
    @property
    def ChainElementStatus(self) -> _n_1_t_3[X509ChainStatus]:"""ChainElementStatus { get; } -> Array"""
    @property
    def Information(self) -> str:"""Information { get; } -> str"""
class X509ChainElementCollection(_n_2_t_3, typing.Iterable[X509ChainElement]):
    @property
    def Item(self) -> X509ChainElement:"""Item { get; } -> X509ChainElement"""
class X509ChainElementEnumerator(_n_2_t_1):
    pass
class X509ChainPolicy(object):
    @property
    def ApplicationPolicy(self) -> _n_7_t_9:"""ApplicationPolicy { get; } -> OidCollection"""
    @property
    def CertificatePolicy(self) -> _n_7_t_9:"""CertificatePolicy { get; } -> OidCollection"""
    @property
    def ExtraStore(self) -> X509Certificate2Collection:"""ExtraStore { get; } -> X509Certificate2Collection"""
    @property
    def RevocationFlag(self) -> X509RevocationFlag:"""RevocationFlag { get; set; } -> X509RevocationFlag"""
    @property
    def RevocationMode(self) -> X509RevocationMode:"""RevocationMode { get; set; } -> X509RevocationMode"""
    @property
    def UrlRetrievalTimeout(self) -> _n_1_t_11:"""UrlRetrievalTimeout { get; set; } -> TimeSpan"""
    @property
    def VerificationFlags(self) -> X509VerificationFlags:"""VerificationFlags { get; set; } -> X509VerificationFlags"""
    @property
    def VerificationTime(self) -> _n_1_t_8:"""VerificationTime { get; set; } -> DateTime"""
    def __init__(self) -> X509ChainPolicy:...
    def Reset(self):...
class X509ChainStatus(_n_1_t_12):
    @property
    def Status(self) -> X509ChainStatusFlags:"""Status { get; set; } -> X509ChainStatusFlags"""
    @property
    def StatusInformation(self) -> str:"""StatusInformation { get; set; } -> str"""
class X509ChainStatusFlags(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    CtlNotSignatureValid: int
    CtlNotTimeValid: int
    CtlNotValidForUsage: int
    Cyclic: int
    ExplicitDistrust: int
    HasExcludedNameConstraint: int
    HasNotDefinedNameConstraint: int
    HasNotPermittedNameConstraint: int
    HasNotSupportedCriticalExtension: int
    HasNotSupportedNameConstraint: int
    HasWeakSignature: int
    InvalidBasicConstraints: int
    InvalidExtension: int
    InvalidNameConstraints: int
    InvalidPolicyConstraints: int
    NoError: int
    NoIssuanceChainPolicy: int
    NotSignatureValid: int
    NotTimeNested: int
    NotTimeValid: int
    NotValidForUsage: int
    OfflineRevocation: int
    PartialChain: int
    RevocationStatusUnknown: int
    Revoked: int
    UntrustedRoot: int
    value__: int
class X509ContentType(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    Authenticode: int
    Cert: int
    Pfx: int
    Pkcs12: int
    Pkcs7: int
    SerializedCert: int
    SerializedStore: int
    Unknown: int
    value__: int
class X509EnhancedKeyUsageExtension(X509Extension):
    @property
    def EnhancedKeyUsages(self) -> _n_7_t_9:"""EnhancedKeyUsages { get; } -> OidCollection"""
    def __init__(self, encodedEnhancedKeyUsages: _n_7_t_6, critical: bool) -> X509EnhancedKeyUsageExtension:...
    def __init__(self, enhancedKeyUsages: _n_7_t_9, critical: bool) -> X509EnhancedKeyUsageExtension:...
    def __init__(self) -> X509EnhancedKeyUsageExtension:...
class X509Extension(_n_7_t_6):
    @property
    def Critical(self) -> bool:"""Critical { get; set; } -> bool"""
    def __init__(self, oid: _n_7_t_8, rawData: _n_1_t_3[_n_1_t_2], critical: bool) -> X509Extension:...
    def __init__(self, encodedExtension: _n_7_t_6, critical: bool) -> X509Extension:...
    def __init__(self, oid: str, rawData: _n_1_t_3[_n_1_t_2], critical: bool) -> X509Extension:...
class X509ExtensionCollection(_n_2_t_3, typing.Iterable[X509Extension]):
    @property
    def Item(self) -> X509Extension:"""Item { get; } -> X509Extension"""
    def __init__(self) -> X509ExtensionCollection:...
    def Add(self, extension: X509Extension) -> int:...
class X509ExtensionEnumerator(_n_2_t_1):
    pass
class X509FindType(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    FindByApplicationPolicy: int
    FindByCertificatePolicy: int
    FindByExtension: int
    FindByIssuerDistinguishedName: int
    FindByIssuerName: int
    FindByKeyUsage: int
    FindBySerialNumber: int
    FindBySubjectDistinguishedName: int
    FindBySubjectKeyIdentifier: int
    FindBySubjectName: int
    FindByTemplateName: int
    FindByThumbprint: int
    FindByTimeExpired: int
    FindByTimeNotYetValid: int
    FindByTimeValid: int
    value__: int
class X509IncludeOption(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    EndCertOnly: int
    ExcludeRoot: int
    _None: int
    value__: int
    WholeChain: int
class X509KeyStorageFlags(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    DefaultKeySet: int
    EphemeralKeySet: int
    Exportable: int
    MachineKeySet: int
    PersistKeySet: int
    UserKeySet: int
    UserProtected: int
    value__: int
class X509KeyUsageExtension(X509Extension):
    @property
    def KeyUsages(self) -> X509KeyUsageFlags:"""KeyUsages { get; } -> X509KeyUsageFlags"""
    def __init__(self, encodedKeyUsage: _n_7_t_6, critical: bool) -> X509KeyUsageExtension:...
    def __init__(self, keyUsages: X509KeyUsageFlags, critical: bool) -> X509KeyUsageExtension:...
    def __init__(self) -> X509KeyUsageExtension:...
class X509KeyUsageFlags(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    CrlSign: int
    DataEncipherment: int
    DecipherOnly: int
    DigitalSignature: int
    EncipherOnly: int
    KeyAgreement: int
    KeyCertSign: int
    KeyEncipherment: int
    _None: int
    NonRepudiation: int
    value__: int
class X509NameType(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    DnsFromAlternativeName: int
    DnsName: int
    EmailName: int
    SimpleName: int
    UpnName: int
    UrlName: int
    value__: int
class X509RevocationFlag(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    EndCertificateOnly: int
    EntireChain: int
    ExcludeRoot: int
    value__: int
class X509RevocationMode(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    NoCheck: int
    Offline: int
    Online: int
    value__: int
class X509SignatureGenerator(object):
    @property
    def PublicKey(self) -> PublicKey:"""PublicKey { get; } -> PublicKey"""
    @staticmethod
    def CreateForECDsa(key: _n_7_t_2) -> X509SignatureGenerator:...
    @staticmethod
    def CreateForRSA(key: _n_7_t_3, signaturePadding: _n_7_t_4) -> X509SignatureGenerator:...
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: _n_7_t_1) -> _n_1_t_3[_n_1_t_2]:...
    def SignData(self, data: _n_1_t_3[_n_1_t_2], hashAlgorithm: _n_7_t_1) -> _n_1_t_3[_n_1_t_2]:...
class X509Store(_n_1_t_9):
    @property
    def Certificates(self) -> X509Certificate2Collection:"""Certificates { get; } -> X509Certificate2Collection"""
    @property
    def Location(self) -> StoreLocation:"""Location { get; } -> StoreLocation"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def StoreHandle(self) -> _n_1_t_10:"""StoreHandle { get; } -> IntPtr"""
    def __init__(self, storeHandle: _n_1_t_10) -> X509Store:...
    def __init__(self, storeName: str, storeLocation: StoreLocation) -> X509Store:...
    def __init__(self, storeName: StoreName, storeLocation: StoreLocation) -> X509Store:...
    def __init__(self, storeLocation: StoreLocation) -> X509Store:...
    def __init__(self, storeName: StoreName) -> X509Store:...
    def __init__(self, storeName: str) -> X509Store:...
    def __init__(self) -> X509Store:...
    def Add(self, certificate: X509Certificate2):...
    def AddRange(self, certificates: X509Certificate2Collection):...
    def Close(self):...
    def Open(self, flags: OpenFlags):...
    def Remove(self, certificate: X509Certificate2):...
    def RemoveRange(self, certificates: X509Certificate2Collection):...
class X509SubjectKeyIdentifierExtension(X509Extension):
    @property
    def SubjectKeyIdentifier(self) -> str:"""SubjectKeyIdentifier { get; } -> str"""
    def __init__(self, key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool) -> X509SubjectKeyIdentifierExtension:...
    def __init__(self, key: PublicKey, critical: bool) -> X509SubjectKeyIdentifierExtension:...
    def __init__(self, encodedSubjectKeyIdentifier: _n_7_t_6, critical: bool) -> X509SubjectKeyIdentifierExtension:...
    def __init__(self, subjectKeyIdentifier: _n_1_t_3[_n_1_t_2], critical: bool) -> X509SubjectKeyIdentifierExtension:...
    def __init__(self, subjectKeyIdentifier: str, critical: bool) -> X509SubjectKeyIdentifierExtension:...
    def __init__(self) -> X509SubjectKeyIdentifierExtension:...
class X509SubjectKeyIdentifierHashAlgorithm(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    CapiSha1: int
    Sha1: int
    ShortSha1: int
    value__: int
class X509VerificationFlags(_n_1_t_4, _n_1_t_5, _n_1_t_6, _n_1_t_7):
    AllFlags: int
    AllowUnknownCertificateAuthority: int
    IgnoreCertificateAuthorityRevocationUnknown: int
    IgnoreCtlNotTimeValid: int
    IgnoreCtlSignerRevocationUnknown: int
    IgnoreEndRevocationUnknown: int
    IgnoreInvalidBasicConstraints: int
    IgnoreInvalidName: int
    IgnoreInvalidPolicy: int
    IgnoreNotTimeNested: int
    IgnoreNotTimeValid: int
    IgnoreRootRevocationUnknown: int
    IgnoreWrongUsage: int
    NoFlag: int
    value__: int
