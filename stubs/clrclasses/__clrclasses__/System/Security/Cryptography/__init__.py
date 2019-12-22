import __clrclasses__.System.Security.Cryptography.X509Certificates as X509Certificates
from __clrclasses__.Internal.Cryptography import ICngSymmetricAlgorithm as _n_0_t_0
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeNCryptKeyHandle as _n_1_t_0
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeNCryptProviderHandle as _n_1_t_1
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeNCryptSecretHandle as _n_1_t_2
from __clrclasses__.System import IDisposable as _n_2_t_0
from __clrclasses__.System import Byte as _n_2_t_1
from __clrclasses__.System import Array as _n_2_t_2
from __clrclasses__.System import Type as _n_2_t_3
from __clrclasses__.System import Enum as _n_2_t_4
from __clrclasses__.System import IComparable as _n_2_t_5
from __clrclasses__.System import IFormattable as _n_2_t_6
from __clrclasses__.System import IConvertible as _n_2_t_7
from __clrclasses__.System import IEquatable as _n_2_t_8
from __clrclasses__.System import IntPtr as _n_2_t_9
from __clrclasses__.System import Nullable as _n_2_t_10
from __clrclasses__.System import ValueType as _n_2_t_11
from __clrclasses__.System import SystemException as _n_2_t_12
from __clrclasses__.System import Exception as _n_2_t_13
from __clrclasses__.System import ActivationContext as _n_2_t_14
from __clrclasses__.System.Collections import ICollection as _n_3_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_3_t_1
from __clrclasses__.System.Collections import IList as _n_3_t_2
from __clrclasses__.System.Collections.Generic import IList as _n_4_t_0
from __clrclasses__.System.Collections.Generic import IReadOnlyList as _n_4_t_1
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_5_t_0
from __clrclasses__.System.Collections.ObjectModel import ReadOnlyCollection as _n_5_t_1
from __clrclasses__.System.IO import Stream as _n_6_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_7_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_8_t_0
from __clrclasses__.System.Security import SecureString as _n_9_t_0
from __clrclasses__.System.Security import ManifestKinds as _n_9_t_1
from __clrclasses__.System.Security import SecurityElement as _n_9_t_2
from __clrclasses__.System.Security.AccessControl import CryptoKeySecurity as _n_10_t_0
from __clrclasses__.System.Security.Cryptography.X509Certificates import AuthenticodeSignatureInformation as _n_11_t_0
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509RevocationFlag as _n_11_t_1
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509RevocationMode as _n_11_t_2
import typing
class Aes(SymmetricAlgorithm, _n_2_t_0):
    pass
class AesCng(Aes, _n_2_t_0, _n_0_t_0):
    def __init__(self) -> AesCng:...
    def __init__(self, keyName: str) -> AesCng:...
    def __init__(self, keyName: str, provider: CngProvider) -> AesCng:...
    def __init__(self, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> AesCng:...
class AesCryptoServiceProvider(Aes, _n_2_t_0):
    def __init__(self) -> AesCryptoServiceProvider:...
class AesManaged(Aes, _n_2_t_0):
    def __init__(self) -> AesManaged:...
class AsnEncodedData(object):
    @property
    def Oid(self) -> Oid:"""Oid { get; set; } -> Oid"""
    @property
    def RawData(self) -> _n_2_t_2[_n_2_t_1]:"""RawData { get; set; } -> Array"""
    def __init__(self, asnEncodedData: AsnEncodedData) -> AsnEncodedData:...
    def __init__(self, oid: Oid, rawData: _n_2_t_2[_n_2_t_1]) -> AsnEncodedData:...
    def __init__(self, oid: str, rawData: _n_2_t_2[_n_2_t_1]) -> AsnEncodedData:...
    def __init__(self, rawData: _n_2_t_2[_n_2_t_1]) -> AsnEncodedData:...
    def CopyFrom(self, asnEncodedData: AsnEncodedData):...
    def Format(self, multiLine: bool) -> str:...
class AsnEncodedDataCollection(_n_3_t_0, typing.Iterable[AsnEncodedData]):
    @property
    def Item(self) -> AsnEncodedData:"""Item { get; } -> AsnEncodedData"""
    def __init__(self, asnEncodedData: AsnEncodedData) -> AsnEncodedDataCollection:...
    def __init__(self) -> AsnEncodedDataCollection:...
    def Add(self, asnEncodedData: AsnEncodedData) -> int:...
    def Remove(self, asnEncodedData: AsnEncodedData):...
class AsnEncodedDataEnumerator(_n_3_t_1):
    pass
class AsymmetricAlgorithm(_n_2_t_0):
    @property
    def KeyExchangeAlgorithm(self) -> str:"""KeyExchangeAlgorithm { get; } -> str"""
    @property
    def KeySize(self) -> int:"""KeySize { get; set; } -> int"""
    @property
    def LegalKeySizes(self) -> _n_2_t_2[KeySizes]:"""LegalKeySizes { get; } -> Array"""
    @property
    def SignatureAlgorithm(self) -> str:"""SignatureAlgorithm { get; } -> str"""
    def Clear(self):...
    @staticmethod
    def Create(algName: str) -> AsymmetricAlgorithm:...
    @staticmethod
    def Create() -> AsymmetricAlgorithm:...
    def FromXmlString(self, xmlString: str):...
    def ToXmlString(self, includePrivateParameters: bool) -> str:...
class AsymmetricKeyExchangeDeformatter(object):
    @property
    def Parameters(self) -> str:"""Parameters { get; set; } -> str"""
    def DecryptKeyExchange(self, rgb: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def SetKey(self, key: AsymmetricAlgorithm):...
class AsymmetricKeyExchangeFormatter(object):
    @property
    def Parameters(self) -> str:"""Parameters { get; } -> str"""
    def CreateKeyExchange(self, data: _n_2_t_2[_n_2_t_1], symAlgType: _n_2_t_3) -> _n_2_t_2[_n_2_t_1]:...
    def CreateKeyExchange(self, data: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def SetKey(self, key: AsymmetricAlgorithm):...
class AsymmetricSignatureDeformatter(object):
    def SetHashAlgorithm(self, strName: str):...
    def SetKey(self, key: AsymmetricAlgorithm):...
    def VerifySignature(self, rgbHash: _n_2_t_2[_n_2_t_1], rgbSignature: _n_2_t_2[_n_2_t_1]) -> bool:...
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: _n_2_t_2[_n_2_t_1]) -> bool:...
class AsymmetricSignatureFormatter(object):
    def CreateSignature(self, rgbHash: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def CreateSignature(self, hash: HashAlgorithm) -> _n_2_t_2[_n_2_t_1]:...
    def SetHashAlgorithm(self, strName: str):...
    def SetKey(self, key: AsymmetricAlgorithm):...
class CipherMode(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    CBC: int
    CFB: int
    CTS: int
    ECB: int
    OFB: int
    value__: int
class CngAlgorithm(_n_2_t_8[CngAlgorithm]):
    @property
    def Algorithm(self) -> str:"""Algorithm { get; } -> str"""
    @property
    def ECDiffieHellman(self) -> CngAlgorithm:"""ECDiffieHellman { get; } -> CngAlgorithm"""
    @property
    def ECDiffieHellmanP256(self) -> CngAlgorithm:"""ECDiffieHellmanP256 { get; } -> CngAlgorithm"""
    @property
    def ECDiffieHellmanP384(self) -> CngAlgorithm:"""ECDiffieHellmanP384 { get; } -> CngAlgorithm"""
    @property
    def ECDiffieHellmanP521(self) -> CngAlgorithm:"""ECDiffieHellmanP521 { get; } -> CngAlgorithm"""
    @property
    def ECDsa(self) -> CngAlgorithm:"""ECDsa { get; } -> CngAlgorithm"""
    @property
    def ECDsaP256(self) -> CngAlgorithm:"""ECDsaP256 { get; } -> CngAlgorithm"""
    @property
    def ECDsaP384(self) -> CngAlgorithm:"""ECDsaP384 { get; } -> CngAlgorithm"""
    @property
    def ECDsaP521(self) -> CngAlgorithm:"""ECDsaP521 { get; } -> CngAlgorithm"""
    @property
    def MD5(self) -> CngAlgorithm:"""MD5 { get; } -> CngAlgorithm"""
    @property
    def Rsa(self) -> CngAlgorithm:"""Rsa { get; } -> CngAlgorithm"""
    @property
    def Sha1(self) -> CngAlgorithm:"""Sha1 { get; } -> CngAlgorithm"""
    @property
    def Sha256(self) -> CngAlgorithm:"""Sha256 { get; } -> CngAlgorithm"""
    @property
    def Sha384(self) -> CngAlgorithm:"""Sha384 { get; } -> CngAlgorithm"""
    @property
    def Sha512(self) -> CngAlgorithm:"""Sha512 { get; } -> CngAlgorithm"""
    def __init__(self, algorithm: str) -> CngAlgorithm:...
class CngAlgorithmGroup(_n_2_t_8[CngAlgorithmGroup]):
    @property
    def AlgorithmGroup(self) -> str:"""AlgorithmGroup { get; } -> str"""
    @property
    def DiffieHellman(self) -> CngAlgorithmGroup:"""DiffieHellman { get; } -> CngAlgorithmGroup"""
    @property
    def Dsa(self) -> CngAlgorithmGroup:"""Dsa { get; } -> CngAlgorithmGroup"""
    @property
    def ECDiffieHellman(self) -> CngAlgorithmGroup:"""ECDiffieHellman { get; } -> CngAlgorithmGroup"""
    @property
    def ECDsa(self) -> CngAlgorithmGroup:"""ECDsa { get; } -> CngAlgorithmGroup"""
    @property
    def Rsa(self) -> CngAlgorithmGroup:"""Rsa { get; } -> CngAlgorithmGroup"""
    def __init__(self, algorithmGroup: str) -> CngAlgorithmGroup:...
class CngExportPolicies(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    AllowArchiving: int
    AllowExport: int
    AllowPlaintextArchiving: int
    AllowPlaintextExport: int
    _None: int
    value__: int
class CngKey(_n_2_t_0):
    @property
    def Algorithm(self) -> CngAlgorithm:"""Algorithm { get; } -> CngAlgorithm"""
    @property
    def AlgorithmGroup(self) -> CngAlgorithmGroup:"""AlgorithmGroup { get; } -> CngAlgorithmGroup"""
    @property
    def ExportPolicy(self) -> CngExportPolicies:"""ExportPolicy { get; set; } -> CngExportPolicies"""
    @property
    def Handle(self) -> _n_1_t_0:"""Handle { get; } -> SafeNCryptKeyHandle"""
    @property
    def IsEphemeral(self) -> bool:"""IsEphemeral { get; set; } -> bool"""
    @property
    def IsMachineKey(self) -> bool:"""IsMachineKey { get; } -> bool"""
    @property
    def KeyName(self) -> str:"""KeyName { get; } -> str"""
    @property
    def KeySize(self) -> int:"""KeySize { get; } -> int"""
    @property
    def KeyUsage(self) -> CngKeyUsages:"""KeyUsage { get; } -> CngKeyUsages"""
    @property
    def ParentWindowHandle(self) -> _n_2_t_9:"""ParentWindowHandle { get; set; } -> IntPtr"""
    @property
    def Provider(self) -> CngProvider:"""Provider { get; } -> CngProvider"""
    @property
    def ProviderHandle(self) -> _n_1_t_1:"""ProviderHandle { get; } -> SafeNCryptProviderHandle"""
    @property
    def UIPolicy(self) -> CngUIPolicy:"""UIPolicy { get; } -> CngUIPolicy"""
    @property
    def UniqueName(self) -> str:"""UniqueName { get; } -> str"""
    @staticmethod
    def Create(algorithm: CngAlgorithm) -> CngKey:...
    @staticmethod
    def Create(algorithm: CngAlgorithm, keyName: str) -> CngKey:...
    @staticmethod
    def Create(algorithm: CngAlgorithm, keyName: str, creationParameters: CngKeyCreationParameters) -> CngKey:...
    def Delete(self):...
    @staticmethod
    def Exists(keyName: str) -> bool:...
    @staticmethod
    def Exists(keyName: str, provider: CngProvider) -> bool:...
    @staticmethod
    def Exists(keyName: str, provider: CngProvider, options: CngKeyOpenOptions) -> bool:...
    def Export(self, format: CngKeyBlobFormat) -> _n_2_t_2[_n_2_t_1]:...
    def GetProperty(self, name: str, options: CngPropertyOptions) -> CngProperty:...
    def HasProperty(self, name: str, options: CngPropertyOptions) -> bool:...
    @staticmethod
    def Import(keyBlob: _n_2_t_2[_n_2_t_1], format: CngKeyBlobFormat) -> CngKey:...
    @staticmethod
    def Import(keyBlob: _n_2_t_2[_n_2_t_1], format: CngKeyBlobFormat, provider: CngProvider) -> CngKey:...
    @staticmethod
    def Open(keyName: str) -> CngKey:...
    @staticmethod
    def Open(keyName: str, provider: CngProvider) -> CngKey:...
    @staticmethod
    def Open(keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> CngKey:...
    @staticmethod
    def Open(keyHandle: _n_1_t_0, keyHandleOpenOptions: CngKeyHandleOpenOptions) -> CngKey:...
    def SetProperty(self, property: CngProperty):...
class CngKeyBlobFormat(_n_2_t_8[CngKeyBlobFormat]):
    @property
    def EccFullPrivateBlob(self) -> CngKeyBlobFormat:"""EccFullPrivateBlob { get; } -> CngKeyBlobFormat"""
    @property
    def EccFullPublicBlob(self) -> CngKeyBlobFormat:"""EccFullPublicBlob { get; } -> CngKeyBlobFormat"""
    @property
    def EccPrivateBlob(self) -> CngKeyBlobFormat:"""EccPrivateBlob { get; } -> CngKeyBlobFormat"""
    @property
    def EccPublicBlob(self) -> CngKeyBlobFormat:"""EccPublicBlob { get; } -> CngKeyBlobFormat"""
    @property
    def Format(self) -> str:"""Format { get; } -> str"""
    @property
    def GenericPrivateBlob(self) -> CngKeyBlobFormat:"""GenericPrivateBlob { get; } -> CngKeyBlobFormat"""
    @property
    def GenericPublicBlob(self) -> CngKeyBlobFormat:"""GenericPublicBlob { get; } -> CngKeyBlobFormat"""
    @property
    def OpaqueTransportBlob(self) -> CngKeyBlobFormat:"""OpaqueTransportBlob { get; } -> CngKeyBlobFormat"""
    @property
    def Pkcs8PrivateBlob(self) -> CngKeyBlobFormat:"""Pkcs8PrivateBlob { get; } -> CngKeyBlobFormat"""
    def __init__(self, format: str) -> CngKeyBlobFormat:...
class CngKeyCreationOptions(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    MachineKey: int
    _None: int
    OverwriteExistingKey: int
    value__: int
class CngKeyCreationParameters(object):
    @property
    def ExportPolicy(self) -> _n_2_t_10[CngExportPolicies]:"""ExportPolicy { get; set; } -> Nullable"""
    @property
    def KeyCreationOptions(self) -> CngKeyCreationOptions:"""KeyCreationOptions { get; set; } -> CngKeyCreationOptions"""
    @property
    def KeyUsage(self) -> _n_2_t_10[CngKeyUsages]:"""KeyUsage { get; set; } -> Nullable"""
    @property
    def Parameters(self) -> CngPropertyCollection:"""Parameters { get; } -> CngPropertyCollection"""
    @property
    def ParentWindowHandle(self) -> _n_2_t_9:"""ParentWindowHandle { get; set; } -> IntPtr"""
    @property
    def Provider(self) -> CngProvider:"""Provider { get; set; } -> CngProvider"""
    @property
    def UIPolicy(self) -> CngUIPolicy:"""UIPolicy { get; set; } -> CngUIPolicy"""
    def __init__(self) -> CngKeyCreationParameters:...
class CngKeyHandleOpenOptions(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    EphemeralKey: int
    _None: int
    value__: int
class CngKeyOpenOptions(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    MachineKey: int
    _None: int
    Silent: int
    UserKey: int
    value__: int
class CngKeyUsages(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    AllUsages: int
    Decryption: int
    KeyAgreement: int
    _None: int
    Signing: int
    value__: int
class CngProperty(_n_2_t_11, _n_2_t_8[CngProperty]):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Options(self) -> CngPropertyOptions:"""Options { get; } -> CngPropertyOptions"""
    def __init__(self, name: str, value: _n_2_t_2[_n_2_t_1], options: CngPropertyOptions) -> CngProperty:...
    def GetValue(self) -> _n_2_t_2[_n_2_t_1]:...
class CngPropertyCollection(_n_5_t_0[CngProperty], _n_4_t_0[CngProperty], _n_3_t_2, _n_4_t_1[CngProperty], typing.Iterable[typing.Any]):
    def __init__(self) -> CngPropertyCollection:...
class CngPropertyOptions(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    CustomProperty: int
    _None: int
    Persist: int
    value__: int
class CngProvider(_n_2_t_8[CngProvider]):
    @property
    def MicrosoftSmartCardKeyStorageProvider(self) -> CngProvider:"""MicrosoftSmartCardKeyStorageProvider { get; } -> CngProvider"""
    @property
    def MicrosoftSoftwareKeyStorageProvider(self) -> CngProvider:"""MicrosoftSoftwareKeyStorageProvider { get; } -> CngProvider"""
    @property
    def Provider(self) -> str:"""Provider { get; } -> str"""
    def __init__(self, provider: str) -> CngProvider:...
class CngUIPolicy(object):
    @property
    def CreationTitle(self) -> str:"""CreationTitle { get; } -> str"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def FriendlyName(self) -> str:"""FriendlyName { get; } -> str"""
    @property
    def ProtectionLevel(self) -> CngUIProtectionLevels:"""ProtectionLevel { get; } -> CngUIProtectionLevels"""
    @property
    def UseContext(self) -> str:"""UseContext { get; } -> str"""
    def __init__(self, protectionLevel: CngUIProtectionLevels) -> CngUIPolicy:...
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str) -> CngUIPolicy:...
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str) -> CngUIPolicy:...
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str, useContext: str) -> CngUIPolicy:...
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str, useContext: str, creationTitle: str) -> CngUIPolicy:...
class CngUIProtectionLevels(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    ForceHighProtection: int
    _None: int
    ProtectKey: int
    value__: int
class CryptoAPITransform(ICryptoTransform):
    @property
    def KeyHandle(self) -> _n_2_t_9:"""KeyHandle { get; } -> IntPtr"""
    def Clear(self):...
    def Reset(self):...
class CryptoConfig(object):
    @property
    def AllowOnlyFipsAlgorithms(self) -> bool:"""AllowOnlyFipsAlgorithms { get; } -> bool"""
    def __init__(self) -> CryptoConfig:...
    @staticmethod
    def AddAlgorithm(algorithm: _n_2_t_3, names: _n_2_t_2[str]):...
    @staticmethod
    def AddOID(oid: str, names: _n_2_t_2[str]):...
    @staticmethod
    def CreateFromName(name: str) -> object:...
    @staticmethod
    def CreateFromName(name: str, args: _n_2_t_2[object]) -> object:...
    @staticmethod
    def EncodeOID(str: str) -> _n_2_t_2[_n_2_t_1]:...
    @staticmethod
    def MapNameToOID(name: str) -> str:...
class CryptographicException(_n_2_t_12, _n_8_t_0, _n_7_t_0):
    def __init__(self, hr: int) -> CryptographicException:...
    def __init__(self, message: str, inner: _n_2_t_13) -> CryptographicException:...
    def __init__(self, format: str, insert: str) -> CryptographicException:...
    def __init__(self, message: str) -> CryptographicException:...
    def __init__(self) -> CryptographicException:...
class CryptographicUnexpectedOperationException(CryptographicException, _n_8_t_0, _n_7_t_0):
    def __init__(self, message: str, inner: _n_2_t_13) -> CryptographicUnexpectedOperationException:...
    def __init__(self, format: str, insert: str) -> CryptographicUnexpectedOperationException:...
    def __init__(self, message: str) -> CryptographicUnexpectedOperationException:...
    def __init__(self) -> CryptographicUnexpectedOperationException:...
class CryptoStream(_n_6_t_0, _n_2_t_0):
    @property
    def HasFlushedFinalBlock(self) -> bool:"""HasFlushedFinalBlock { get; } -> bool"""
    def __init__(self, stream: _n_6_t_0, transform: ICryptoTransform, mode: CryptoStreamMode, leaveOpen: bool) -> CryptoStream:...
    def __init__(self, stream: _n_6_t_0, transform: ICryptoTransform, mode: CryptoStreamMode) -> CryptoStream:...
    def Clear(self):...
    def FlushFinalBlock(self):...
class CryptoStreamMode(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    Read: int
    value__: int
    Write: int
class CspKeyContainerInfo(object):
    @property
    def Accessible(self) -> bool:"""Accessible { get; } -> bool"""
    @property
    def CryptoKeySecurity(self) -> _n_10_t_0:"""CryptoKeySecurity { get; } -> CryptoKeySecurity"""
    @property
    def Exportable(self) -> bool:"""Exportable { get; } -> bool"""
    @property
    def HardwareDevice(self) -> bool:"""HardwareDevice { get; } -> bool"""
    @property
    def KeyContainerName(self) -> str:"""KeyContainerName { get; } -> str"""
    @property
    def KeyNumber(self) -> KeyNumber:"""KeyNumber { get; } -> KeyNumber"""
    @property
    def MachineKeyStore(self) -> bool:"""MachineKeyStore { get; } -> bool"""
    @property
    def Protected(self) -> bool:"""Protected { get; } -> bool"""
    @property
    def ProviderName(self) -> str:"""ProviderName { get; } -> str"""
    @property
    def ProviderType(self) -> int:"""ProviderType { get; } -> int"""
    @property
    def RandomlyGenerated(self) -> bool:"""RandomlyGenerated { get; } -> bool"""
    @property
    def Removable(self) -> bool:"""Removable { get; } -> bool"""
    @property
    def UniqueKeyContainerName(self) -> str:"""UniqueKeyContainerName { get; } -> str"""
    def __init__(self, parameters: CspParameters) -> CspKeyContainerInfo:...
class CspParameters(object):
    KeyContainerName: int
    KeyNumber: int
    ProviderName: int
    ProviderType: int
    @property
    def CryptoKeySecurity(self) -> _n_10_t_0:"""CryptoKeySecurity { get; set; } -> CryptoKeySecurity"""
    @property
    def Flags(self) -> CspProviderFlags:"""Flags { get; set; } -> CspProviderFlags"""
    @property
    def KeyPassword(self) -> _n_9_t_0:"""KeyPassword { get; set; } -> SecureString"""
    @property
    def ParentWindowHandle(self) -> _n_2_t_9:"""ParentWindowHandle { get; set; } -> IntPtr"""
    def __init__(self, providerType: int, providerName: str, keyContainerName: str, cryptoKeySecurity: _n_10_t_0, parentWindowHandle: _n_2_t_9) -> CspParameters:...
    def __init__(self, providerType: int, providerName: str, keyContainerName: str, cryptoKeySecurity: _n_10_t_0, keyPassword: _n_9_t_0) -> CspParameters:...
    def __init__(self, dwTypeIn: int, strProviderNameIn: str, strContainerNameIn: str) -> CspParameters:...
    def __init__(self, dwTypeIn: int, strProviderNameIn: str) -> CspParameters:...
    def __init__(self, dwTypeIn: int) -> CspParameters:...
    def __init__(self) -> CspParameters:...
class CspProviderFlags(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    CreateEphemeralKey: int
    NoFlags: int
    NoPrompt: int
    UseArchivableKey: int
    UseDefaultKeyContainer: int
    UseExistingKey: int
    UseMachineKeyStore: int
    UseNonExportableKey: int
    UseUserProtectedKey: int
    value__: int
class DeriveBytes(_n_2_t_0):
    def GetBytes(self, cb: int) -> _n_2_t_2[_n_2_t_1]:...
    def Reset(self):...
class DES(SymmetricAlgorithm, _n_2_t_0):
    @staticmethod
    def IsSemiWeakKey(rgbKey: _n_2_t_2[_n_2_t_1]) -> bool:...
    @staticmethod
    def IsWeakKey(rgbKey: _n_2_t_2[_n_2_t_1]) -> bool:...
class DESCryptoServiceProvider(DES, _n_2_t_0):
    def __init__(self) -> DESCryptoServiceProvider:...
class DSA(AsymmetricAlgorithm, _n_2_t_0):
    def CreateSignature(self, rgbHash: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:...
    def ImportParameters(self, parameters: DSAParameters):...
    def SignData(self, data: _n_6_t_0, hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def SignData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def SignData(self, data: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def VerifyData(self, data: _n_6_t_0, signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> bool:...
    def VerifyData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int, signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> bool:...
    def VerifyData(self, data: _n_2_t_2[_n_2_t_1], signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> bool:...
    def VerifySignature(self, rgbHash: _n_2_t_2[_n_2_t_1], rgbSignature: _n_2_t_2[_n_2_t_1]) -> bool:...
class DSACng(DSA, _n_2_t_0):
    @property
    def Key(self) -> CngKey:"""Key { get; set; } -> CngKey"""
    def __init__(self) -> DSACng:...
    def __init__(self, keySize: int) -> DSACng:...
    def __init__(self, key: CngKey) -> DSACng:...
class DSACryptoServiceProvider(DSA, _n_2_t_0, ICspAsymmetricAlgorithm):
    @property
    def PersistKeyInCsp(self) -> bool:"""PersistKeyInCsp { get; set; } -> bool"""
    @property
    def PublicOnly(self) -> bool:"""PublicOnly { get; } -> bool"""
    @property
    def UseMachineKeyStore(self) -> bool:"""UseMachineKeyStore { get; set; } -> bool"""
    def __init__(self, dwKeySize: int, parameters: CspParameters) -> DSACryptoServiceProvider:...
    def __init__(self, parameters: CspParameters) -> DSACryptoServiceProvider:...
    def __init__(self, dwKeySize: int) -> DSACryptoServiceProvider:...
    def __init__(self) -> DSACryptoServiceProvider:...
    def SignHash(self, rgbHash: _n_2_t_2[_n_2_t_1], str: str) -> _n_2_t_2[_n_2_t_1]:...
    def VerifyHash(self, rgbHash: _n_2_t_2[_n_2_t_1], str: str, rgbSignature: _n_2_t_2[_n_2_t_1]) -> bool:...
class DSAParameters(_n_2_t_11):
    Counter: int
    G: int
    J: int
    P: int
    Q: int
    Seed: int
    X: int
    Y: int
class DSASignatureDeformatter(AsymmetricSignatureDeformatter):
    def __init__(self, key: AsymmetricAlgorithm) -> DSASignatureDeformatter:...
    def __init__(self) -> DSASignatureDeformatter:...
class DSASignatureFormatter(AsymmetricSignatureFormatter):
    def __init__(self, key: AsymmetricAlgorithm) -> DSASignatureFormatter:...
    def __init__(self) -> DSASignatureFormatter:...
class ECCurve(_n_2_t_11):
    A: int
    B: int
    Cofactor: int
    CurveType: int
    G: int
    Hash: int
    Order: int
    Polynomial: int
    Prime: int
    Seed: int
    @property
    def IsCharacteristic2(self) -> bool:"""IsCharacteristic2 { get; } -> bool"""
    @property
    def IsExplicit(self) -> bool:"""IsExplicit { get; } -> bool"""
    @property
    def IsNamed(self) -> bool:"""IsNamed { get; } -> bool"""
    @property
    def IsPrime(self) -> bool:"""IsPrime { get; } -> bool"""
    @property
    def Oid(self) -> Oid:"""Oid { get; set; } -> Oid"""
    @staticmethod
    def CreateFromFriendlyName(oidFriendlyName: str) -> ECCurve:...
    @staticmethod
    def CreateFromOid(curveOid: Oid) -> ECCurve:...
    @staticmethod
    def CreateFromValue(oidValue: str) -> ECCurve:...
    def Validate(self):...
    class ECCurveType(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
        Characteristic2: int
        Implicit: int
        Named: int
        PrimeMontgomery: int
        PrimeShortWeierstrass: int
        PrimeTwistedEdwards: int
        value__: int
    class NamedCurves(object):
        @property
        def brainpoolP160r1(self) -> ECCurve:"""brainpoolP160r1 { get; } -> ECCurve"""
        @property
        def brainpoolP160t1(self) -> ECCurve:"""brainpoolP160t1 { get; } -> ECCurve"""
        @property
        def brainpoolP192r1(self) -> ECCurve:"""brainpoolP192r1 { get; } -> ECCurve"""
        @property
        def brainpoolP192t1(self) -> ECCurve:"""brainpoolP192t1 { get; } -> ECCurve"""
        @property
        def brainpoolP224r1(self) -> ECCurve:"""brainpoolP224r1 { get; } -> ECCurve"""
        @property
        def brainpoolP224t1(self) -> ECCurve:"""brainpoolP224t1 { get; } -> ECCurve"""
        @property
        def brainpoolP256r1(self) -> ECCurve:"""brainpoolP256r1 { get; } -> ECCurve"""
        @property
        def brainpoolP256t1(self) -> ECCurve:"""brainpoolP256t1 { get; } -> ECCurve"""
        @property
        def brainpoolP320r1(self) -> ECCurve:"""brainpoolP320r1 { get; } -> ECCurve"""
        @property
        def brainpoolP320t1(self) -> ECCurve:"""brainpoolP320t1 { get; } -> ECCurve"""
        @property
        def brainpoolP384r1(self) -> ECCurve:"""brainpoolP384r1 { get; } -> ECCurve"""
        @property
        def brainpoolP384t1(self) -> ECCurve:"""brainpoolP384t1 { get; } -> ECCurve"""
        @property
        def brainpoolP512r1(self) -> ECCurve:"""brainpoolP512r1 { get; } -> ECCurve"""
        @property
        def brainpoolP512t1(self) -> ECCurve:"""brainpoolP512t1 { get; } -> ECCurve"""
        @property
        def nistP256(self) -> ECCurve:"""nistP256 { get; } -> ECCurve"""
        @property
        def nistP384(self) -> ECCurve:"""nistP384 { get; } -> ECCurve"""
        @property
        def nistP521(self) -> ECCurve:"""nistP521 { get; } -> ECCurve"""
class ECDiffieHellman(AsymmetricAlgorithm, _n_2_t_0):
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey:"""PublicKey { get; } -> ECDiffieHellmanPublicKey"""
    def DeriveKeyFromHash(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def DeriveKeyFromHash(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, secretPrepend: _n_2_t_2[_n_2_t_1], secretAppend: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def DeriveKeyFromHmac(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def DeriveKeyFromHmac(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName, hmacKey: _n_2_t_2[_n_2_t_1], secretPrepend: _n_2_t_2[_n_2_t_1], secretAppend: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> _n_2_t_2[_n_2_t_1]:...
    def DeriveKeyTls(self, otherPartyPublicKey: ECDiffieHellmanPublicKey, prfLabel: _n_2_t_2[_n_2_t_1], prfSeed: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:...
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:...
    def GenerateKey(self, curve: ECCurve):...
    def ImportParameters(self, parameters: ECParameters):...
class ECDiffieHellmanCng(ECDiffieHellman, _n_2_t_0):
    @property
    def HashAlgorithm(self) -> CngAlgorithm:"""HashAlgorithm { get; set; } -> CngAlgorithm"""
    @property
    def HmacKey(self) -> _n_2_t_2[_n_2_t_1]:"""HmacKey { get; set; } -> Array"""
    @property
    def Key(self) -> CngKey:"""Key { get; set; } -> CngKey"""
    @property
    def KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction:"""KeyDerivationFunction { get; set; } -> ECDiffieHellmanKeyDerivationFunction"""
    @property
    def Label(self) -> _n_2_t_2[_n_2_t_1]:"""Label { get; set; } -> Array"""
    @property
    def SecretAppend(self) -> _n_2_t_2[_n_2_t_1]:"""SecretAppend { get; set; } -> Array"""
    @property
    def SecretPrepend(self) -> _n_2_t_2[_n_2_t_1]:"""SecretPrepend { get; set; } -> Array"""
    @property
    def Seed(self) -> _n_2_t_2[_n_2_t_1]:"""Seed { get; set; } -> Array"""
    @property
    def UseSecretAgreementAsHmacKey(self) -> bool:"""UseSecretAgreementAsHmacKey { get; } -> bool"""
    def __init__(self) -> ECDiffieHellmanCng:...
    def __init__(self, keySize: int) -> ECDiffieHellmanCng:...
    def __init__(self, curve: ECCurve) -> ECDiffieHellmanCng:...
    def __init__(self, key: CngKey) -> ECDiffieHellmanCng:...
    def DeriveSecretAgreementHandle(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> _n_1_t_2:...
    def DeriveSecretAgreementHandle(self, otherPartyPublicKey: CngKey) -> _n_1_t_2:...
class ECDiffieHellmanCngPublicKey(ECDiffieHellmanPublicKey, _n_2_t_0):
    @property
    def BlobFormat(self) -> CngKeyBlobFormat:"""BlobFormat { get; } -> CngKeyBlobFormat"""
    @staticmethod
    def FromByteArray(publicKeyBlob: _n_2_t_2[_n_2_t_1], format: CngKeyBlobFormat) -> ECDiffieHellmanPublicKey:...
    @staticmethod
    def FromXmlString(xml: str) -> ECDiffieHellmanCngPublicKey:...
    def Import(self) -> CngKey:...
class ECDiffieHellmanKeyDerivationFunction(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    Hash: int
    Hmac: int
    Tls: int
    value__: int
class ECDiffieHellmanPublicKey(_n_2_t_0):
    def ExportExplicitParameters(self) -> ECParameters:...
    def ExportParameters(self) -> ECParameters:...
    def ToByteArray(self) -> _n_2_t_2[_n_2_t_1]:...
    def ToXmlString(self) -> str:...
class ECDsa(AsymmetricAlgorithm, _n_2_t_0):
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:...
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:...
    def GenerateKey(self, curve: ECCurve):...
    def ImportParameters(self, parameters: ECParameters):...
    def SignData(self, data: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def SignData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int, hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def SignData(self, data: _n_6_t_0, hashAlgorithm: HashAlgorithmName) -> _n_2_t_2[_n_2_t_1]:...
    def SignHash(self, hash: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def VerifyData(self, data: _n_2_t_2[_n_2_t_1], signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> bool:...
    def VerifyData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int, signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> bool:...
    def VerifyData(self, data: _n_6_t_0, signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName) -> bool:...
    def VerifyHash(self, hash: _n_2_t_2[_n_2_t_1], signature: _n_2_t_2[_n_2_t_1]) -> bool:...
class ECDsaCng(ECDsa, _n_2_t_0):
    @property
    def HashAlgorithm(self) -> CngAlgorithm:"""HashAlgorithm { get; set; } -> CngAlgorithm"""
    @property
    def Key(self) -> CngKey:"""Key { get; set; } -> CngKey"""
    def __init__(self) -> ECDsaCng:...
    def __init__(self, keySize: int) -> ECDsaCng:...
    def __init__(self, curve: ECCurve) -> ECDsaCng:...
    def __init__(self, key: CngKey) -> ECDsaCng:...
class ECKeyXmlFormat(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    Rfc4050: int
    value__: int
class ECParameters(_n_2_t_11):
    Curve: int
    D: int
    Q: int
    def Validate(self):...
class ECPoint(_n_2_t_11):
    X: int
    Y: int
class FromBase64Transform(ICryptoTransform):
    def __init__(self, whitespaces: FromBase64TransformMode) -> FromBase64Transform:...
    def __init__(self) -> FromBase64Transform:...
    def Clear(self):...
class FromBase64TransformMode(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    DoNotIgnoreWhiteSpaces: int
    IgnoreWhiteSpaces: int
    value__: int
class HashAlgorithm(_n_2_t_0, ICryptoTransform):
    @property
    def Hash(self) -> _n_2_t_2[_n_2_t_1]:"""Hash { get; } -> Array"""
    @property
    def HashSize(self) -> int:"""HashSize { get; } -> int"""
    def Clear(self):...
    def ComputeHash(self, buffer: _n_2_t_2[_n_2_t_1], offset: int, count: int) -> _n_2_t_2[_n_2_t_1]:...
    def ComputeHash(self, buffer: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def ComputeHash(self, inputStream: _n_6_t_0) -> _n_2_t_2[_n_2_t_1]:...
    @staticmethod
    def Create(hashName: str) -> HashAlgorithm:...
    @staticmethod
    def Create() -> HashAlgorithm:...
    def Initialize(self):...
class HashAlgorithmName(_n_2_t_11, _n_2_t_8[HashAlgorithmName]):
    @property
    def MD5(self) -> HashAlgorithmName:"""MD5 { get; } -> HashAlgorithmName"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def SHA1(self) -> HashAlgorithmName:"""SHA1 { get; } -> HashAlgorithmName"""
    @property
    def SHA256(self) -> HashAlgorithmName:"""SHA256 { get; } -> HashAlgorithmName"""
    @property
    def SHA384(self) -> HashAlgorithmName:"""SHA384 { get; } -> HashAlgorithmName"""
    @property
    def SHA512(self) -> HashAlgorithmName:"""SHA512 { get; } -> HashAlgorithmName"""
    def __init__(self, name: str) -> HashAlgorithmName:...
class HMAC(KeyedHashAlgorithm, _n_2_t_0, ICryptoTransform):
    @property
    def HashName(self) -> str:"""HashName { get; set; } -> str"""
class HMACMD5(HMAC, _n_2_t_0, ICryptoTransform):
    def __init__(self, key: _n_2_t_2[_n_2_t_1]) -> HMACMD5:...
    def __init__(self) -> HMACMD5:...
class HMACRIPEMD160(HMAC, _n_2_t_0, ICryptoTransform):
    def __init__(self, key: _n_2_t_2[_n_2_t_1]) -> HMACRIPEMD160:...
    def __init__(self) -> HMACRIPEMD160:...
class HMACSHA1(HMAC, _n_2_t_0, ICryptoTransform):
    def __init__(self, key: _n_2_t_2[_n_2_t_1], useManagedSha1: bool) -> HMACSHA1:...
    def __init__(self, key: _n_2_t_2[_n_2_t_1]) -> HMACSHA1:...
    def __init__(self) -> HMACSHA1:...
class HMACSHA256(HMAC, _n_2_t_0, ICryptoTransform):
    def __init__(self, key: _n_2_t_2[_n_2_t_1]) -> HMACSHA256:...
    def __init__(self) -> HMACSHA256:...
class HMACSHA384(HMAC, _n_2_t_0, ICryptoTransform):
    @property
    def ProduceLegacyHmacValues(self) -> bool:"""ProduceLegacyHmacValues { get; set; } -> bool"""
    def __init__(self, key: _n_2_t_2[_n_2_t_1]) -> HMACSHA384:...
    def __init__(self) -> HMACSHA384:...
class HMACSHA512(HMAC, _n_2_t_0, ICryptoTransform):
    @property
    def ProduceLegacyHmacValues(self) -> bool:"""ProduceLegacyHmacValues { get; set; } -> bool"""
    def __init__(self, key: _n_2_t_2[_n_2_t_1]) -> HMACSHA512:...
    def __init__(self) -> HMACSHA512:...
class ICryptoTransform(_n_2_t_0):
    @property
    def CanReuseTransform(self) -> bool:"""CanReuseTransform { get; } -> bool"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:"""CanTransformMultipleBlocks { get; } -> bool"""
    @property
    def InputBlockSize(self) -> int:"""InputBlockSize { get; } -> int"""
    @property
    def OutputBlockSize(self) -> int:"""OutputBlockSize { get; } -> int"""
    def TransformBlock(self, inputBuffer: _n_2_t_2[_n_2_t_1], inputOffset: int, inputCount: int, outputBuffer: _n_2_t_2[_n_2_t_1], outputOffset: int) -> int:...
    def TransformFinalBlock(self, inputBuffer: _n_2_t_2[_n_2_t_1], inputOffset: int, inputCount: int) -> _n_2_t_2[_n_2_t_1]:...
class ICspAsymmetricAlgorithm():
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:"""CspKeyContainerInfo { get; } -> CspKeyContainerInfo"""
    def ExportCspBlob(self, includePrivateParameters: bool) -> _n_2_t_2[_n_2_t_1]:...
    def ImportCspBlob(self, rawData: _n_2_t_2[_n_2_t_1]):...
class IncrementalHash(_n_2_t_0):
    @property
    def AlgorithmName(self) -> HashAlgorithmName:"""AlgorithmName { get; } -> HashAlgorithmName"""
    def AppendData(self, data: _n_2_t_2[_n_2_t_1]):...
    def AppendData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int):...
    @staticmethod
    def CreateHash(hashAlgorithm: HashAlgorithmName) -> IncrementalHash:...
    @staticmethod
    def CreateHMAC(hashAlgorithm: HashAlgorithmName, key: _n_2_t_2[_n_2_t_1]) -> IncrementalHash:...
    def GetHashAndReset(self) -> _n_2_t_2[_n_2_t_1]:...
class KeyedHashAlgorithm(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    @property
    def Key(self) -> _n_2_t_2[_n_2_t_1]:"""Key { get; set; } -> Array"""
class KeyNumber(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    Exchange: int
    Signature: int
    value__: int
class KeySizes(object):
    @property
    def MaxSize(self) -> int:"""MaxSize { get; } -> int"""
    @property
    def MinSize(self) -> int:"""MinSize { get; } -> int"""
    @property
    def SkipSize(self) -> int:"""SkipSize { get; } -> int"""
    def __init__(self, minSize: int, maxSize: int, skipSize: int) -> KeySizes:...
class MACTripleDES(KeyedHashAlgorithm, _n_2_t_0, ICryptoTransform):
    @property
    def Padding(self) -> PaddingMode:"""Padding { get; set; } -> PaddingMode"""
    def __init__(self, strTripleDES: str, rgbKey: _n_2_t_2[_n_2_t_1]) -> MACTripleDES:...
    def __init__(self, rgbKey: _n_2_t_2[_n_2_t_1]) -> MACTripleDES:...
    def __init__(self) -> MACTripleDES:...
class ManifestSignatureInformation(object):
    @property
    def AuthenticodeSignature(self) -> _n_11_t_0:"""AuthenticodeSignature { get; } -> AuthenticodeSignatureInformation"""
    @property
    def Manifest(self) -> _n_9_t_1:"""Manifest { get; } -> ManifestKinds"""
    @property
    def StrongNameSignature(self) -> StrongNameSignatureInformation:"""StrongNameSignature { get; } -> StrongNameSignatureInformation"""
    @staticmethod
    def VerifySignature(application: _n_2_t_14) -> ManifestSignatureInformationCollection:...
    @staticmethod
    def VerifySignature(application: _n_2_t_14, manifests: _n_9_t_1) -> ManifestSignatureInformationCollection:...
    @staticmethod
    def VerifySignature(application: _n_2_t_14, manifests: _n_9_t_1, revocationFlag: _n_11_t_1, revocationMode: _n_11_t_2) -> ManifestSignatureInformationCollection:...
class ManifestSignatureInformationCollection(_n_5_t_1[ManifestSignatureInformation], _n_4_t_0[ManifestSignatureInformation], _n_3_t_2, _n_4_t_1[ManifestSignatureInformation], typing.Iterable[typing.Any]):
    pass
class MaskGenerationMethod(object):
    def GenerateMask(self, rgbSeed: _n_2_t_2[_n_2_t_1], cbReturn: int) -> _n_2_t_2[_n_2_t_1]:...
class MD5(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    pass
class MD5Cng(MD5, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> MD5Cng:...
class MD5CryptoServiceProvider(MD5, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> MD5CryptoServiceProvider:...
class Oid(object):
    @property
    def FriendlyName(self) -> str:"""FriendlyName { get; set; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; set; } -> str"""
    def __init__(self, oid: Oid) -> Oid:...
    def __init__(self, value: str, friendlyName: str) -> Oid:...
    def __init__(self, oid: str) -> Oid:...
    def __init__(self) -> Oid:...
    @staticmethod
    def FromFriendlyName(friendlyName: str, group: OidGroup) -> Oid:...
    @staticmethod
    def FromOidValue(oidValue: str, group: OidGroup) -> Oid:...
class OidCollection(_n_3_t_0, typing.Iterable[Oid]):
    @property
    def Item(self) -> Oid:"""Item { get; } -> Oid"""
    def __init__(self) -> OidCollection:...
    def Add(self, oid: Oid) -> int:...
class OidEnumerator(_n_3_t_1):
    pass
class OidGroup(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    All: int
    Attribute: int
    EncryptionAlgorithm: int
    EnhancedKeyUsage: int
    ExtensionOrAttribute: int
    HashAlgorithm: int
    KeyDerivationFunction: int
    Policy: int
    PublicKeyAlgorithm: int
    SignatureAlgorithm: int
    Template: int
    value__: int
class PaddingMode(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    ANSIX923: int
    ISO10126: int
    _None: int
    PKCS7: int
    value__: int
    Zeros: int
class PasswordDeriveBytes(DeriveBytes, _n_2_t_0):
    @property
    def HashName(self) -> str:"""HashName { get; set; } -> str"""
    @property
    def IterationCount(self) -> int:"""IterationCount { get; set; } -> int"""
    @property
    def Salt(self) -> _n_2_t_2[_n_2_t_1]:"""Salt { get; set; } -> Array"""
    def __init__(self, password: _n_2_t_2[_n_2_t_1], salt: _n_2_t_2[_n_2_t_1], hashName: str, iterations: int, cspParams: CspParameters) -> PasswordDeriveBytes:...
    def __init__(self, strPassword: str, rgbSalt: _n_2_t_2[_n_2_t_1], strHashName: str, iterations: int, cspParams: CspParameters) -> PasswordDeriveBytes:...
    def __init__(self, password: _n_2_t_2[_n_2_t_1], salt: _n_2_t_2[_n_2_t_1], cspParams: CspParameters) -> PasswordDeriveBytes:...
    def __init__(self, strPassword: str, rgbSalt: _n_2_t_2[_n_2_t_1], cspParams: CspParameters) -> PasswordDeriveBytes:...
    def __init__(self, password: _n_2_t_2[_n_2_t_1], salt: _n_2_t_2[_n_2_t_1], hashName: str, iterations: int) -> PasswordDeriveBytes:...
    def __init__(self, strPassword: str, rgbSalt: _n_2_t_2[_n_2_t_1], strHashName: str, iterations: int) -> PasswordDeriveBytes:...
    def __init__(self, password: _n_2_t_2[_n_2_t_1], salt: _n_2_t_2[_n_2_t_1]) -> PasswordDeriveBytes:...
    def __init__(self, strPassword: str, rgbSalt: _n_2_t_2[_n_2_t_1]) -> PasswordDeriveBytes:...
    def CryptDeriveKey(self, algname: str, alghashname: str, keySize: int, rgbIV: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
class PKCS1MaskGenerationMethod(MaskGenerationMethod):
    @property
    def HashName(self) -> str:"""HashName { get; set; } -> str"""
    def __init__(self) -> PKCS1MaskGenerationMethod:...
class RandomNumberGenerator(_n_2_t_0):
    @staticmethod
    def Create(rngName: str) -> RandomNumberGenerator:...
    @staticmethod
    def Create() -> RandomNumberGenerator:...
    def GetBytes(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int):...
    def GetBytes(self, data: _n_2_t_2[_n_2_t_1]):...
    def GetNonZeroBytes(self, data: _n_2_t_2[_n_2_t_1]):...
class RC2(SymmetricAlgorithm, _n_2_t_0):
    @property
    def EffectiveKeySize(self) -> int:"""EffectiveKeySize { get; set; } -> int"""
class RC2CryptoServiceProvider(RC2, _n_2_t_0):
    @property
    def UseSalt(self) -> bool:"""UseSalt { get; set; } -> bool"""
    def __init__(self) -> RC2CryptoServiceProvider:...
class Rfc2898DeriveBytes(DeriveBytes, _n_2_t_0):
    @property
    def IterationCount(self) -> int:"""IterationCount { get; set; } -> int"""
    @property
    def Salt(self) -> _n_2_t_2[_n_2_t_1]:"""Salt { get; set; } -> Array"""
    def __init__(self, password: _n_2_t_2[_n_2_t_1], salt: _n_2_t_2[_n_2_t_1], iterations: int, hashAlgorithm: HashAlgorithmName) -> Rfc2898DeriveBytes:...
    def __init__(self, password: _n_2_t_2[_n_2_t_1], salt: _n_2_t_2[_n_2_t_1], iterations: int) -> Rfc2898DeriveBytes:...
    def __init__(self, password: str, salt: _n_2_t_2[_n_2_t_1], iterations: int, hashAlgorithm: HashAlgorithmName) -> Rfc2898DeriveBytes:...
    def __init__(self, password: str, salt: _n_2_t_2[_n_2_t_1], iterations: int) -> Rfc2898DeriveBytes:...
    def __init__(self, password: str, salt: _n_2_t_2[_n_2_t_1]) -> Rfc2898DeriveBytes:...
    def __init__(self, password: str, saltSize: int, iterations: int, hashAlgorithm: HashAlgorithmName) -> Rfc2898DeriveBytes:...
    def __init__(self, password: str, saltSize: int, iterations: int) -> Rfc2898DeriveBytes:...
    def __init__(self, password: str, saltSize: int) -> Rfc2898DeriveBytes:...
    def CryptDeriveKey(self, algname: str, alghashname: str, keySize: int, rgbIV: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
class Rijndael(SymmetricAlgorithm, _n_2_t_0):
    pass
class RijndaelManaged(Rijndael, _n_2_t_0):
    def __init__(self) -> RijndaelManaged:...
class RijndaelManagedTransform(ICryptoTransform):
    @property
    def BlockSizeValue(self) -> int:"""BlockSizeValue { get; } -> int"""
    def Clear(self):...
    def Reset(self):...
class RIPEMD160(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    pass
class RIPEMD160Managed(RIPEMD160, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> RIPEMD160Managed:...
class RNGCryptoServiceProvider(RandomNumberGenerator, _n_2_t_0):
    def __init__(self, rgb: _n_2_t_2[_n_2_t_1]) -> RNGCryptoServiceProvider:...
    def __init__(self, str: str) -> RNGCryptoServiceProvider:...
    def __init__(self) -> RNGCryptoServiceProvider:...
    def __init__(self, cspParams: CspParameters) -> RNGCryptoServiceProvider:...
class RSA(AsymmetricAlgorithm, _n_2_t_0):
    def Decrypt(self, data: _n_2_t_2[_n_2_t_1], padding: RSAEncryptionPadding) -> _n_2_t_2[_n_2_t_1]:...
    def DecryptValue(self, rgb: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def Encrypt(self, data: _n_2_t_2[_n_2_t_1], padding: RSAEncryptionPadding) -> _n_2_t_2[_n_2_t_1]:...
    def EncryptValue(self, rgb: _n_2_t_2[_n_2_t_1]) -> _n_2_t_2[_n_2_t_1]:...
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:...
    def ImportParameters(self, parameters: RSAParameters):...
    def SignData(self, data: _n_6_t_0, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> _n_2_t_2[_n_2_t_1]:...
    def SignData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> _n_2_t_2[_n_2_t_1]:...
    def SignData(self, data: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> _n_2_t_2[_n_2_t_1]:...
    def SignHash(self, hash: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> _n_2_t_2[_n_2_t_1]:...
    def VerifyData(self, data: _n_6_t_0, signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool:...
    def VerifyData(self, data: _n_2_t_2[_n_2_t_1], offset: int, count: int, signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool:...
    def VerifyData(self, data: _n_2_t_2[_n_2_t_1], signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool:...
    def VerifyHash(self, hash: _n_2_t_2[_n_2_t_1], signature: _n_2_t_2[_n_2_t_1], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding) -> bool:...
class RSACng(RSA, _n_2_t_0):
    @property
    def Key(self) -> CngKey:"""Key { get; set; } -> CngKey"""
    def __init__(self) -> RSACng:...
    def __init__(self, keySize: int) -> RSACng:...
    def __init__(self, key: CngKey) -> RSACng:...
class RSACryptoServiceProvider(RSA, _n_2_t_0, ICspAsymmetricAlgorithm):
    @property
    def PersistKeyInCsp(self) -> bool:"""PersistKeyInCsp { get; set; } -> bool"""
    @property
    def PublicOnly(self) -> bool:"""PublicOnly { get; } -> bool"""
    @property
    def UseMachineKeyStore(self) -> bool:"""UseMachineKeyStore { get; set; } -> bool"""
    def __init__(self, dwKeySize: int, parameters: CspParameters) -> RSACryptoServiceProvider:...
    def __init__(self, parameters: CspParameters) -> RSACryptoServiceProvider:...
    def __init__(self, dwKeySize: int) -> RSACryptoServiceProvider:...
    def __init__(self) -> RSACryptoServiceProvider:...
class RSAEncryptionPadding(_n_2_t_8[RSAEncryptionPadding]):
    @property
    def Mode(self) -> RSAEncryptionPaddingMode:"""Mode { get; } -> RSAEncryptionPaddingMode"""
    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName:"""OaepHashAlgorithm { get; } -> HashAlgorithmName"""
    @property
    def OaepSHA1(self) -> RSAEncryptionPadding:"""OaepSHA1 { get; } -> RSAEncryptionPadding"""
    @property
    def OaepSHA256(self) -> RSAEncryptionPadding:"""OaepSHA256 { get; } -> RSAEncryptionPadding"""
    @property
    def OaepSHA384(self) -> RSAEncryptionPadding:"""OaepSHA384 { get; } -> RSAEncryptionPadding"""
    @property
    def OaepSHA512(self) -> RSAEncryptionPadding:"""OaepSHA512 { get; } -> RSAEncryptionPadding"""
    @property
    def Pkcs1(self) -> RSAEncryptionPadding:"""Pkcs1 { get; } -> RSAEncryptionPadding"""
    @staticmethod
    def CreateOaep(hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding:...
class RSAEncryptionPaddingMode(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    Oaep: int
    Pkcs1: int
    value__: int
class RSAOAEPKeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    def __init__(self, key: AsymmetricAlgorithm) -> RSAOAEPKeyExchangeDeformatter:...
    def __init__(self) -> RSAOAEPKeyExchangeDeformatter:...
class RSAOAEPKeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    @property
    def Parameter(self) -> _n_2_t_2[_n_2_t_1]:"""Parameter { get; set; } -> Array"""
    @property
    def Rng(self) -> RandomNumberGenerator:"""Rng { get; set; } -> RandomNumberGenerator"""
    def __init__(self, key: AsymmetricAlgorithm) -> RSAOAEPKeyExchangeFormatter:...
    def __init__(self) -> RSAOAEPKeyExchangeFormatter:...
class RSAParameters(_n_2_t_11):
    D: int
    DP: int
    DQ: int
    Exponent: int
    InverseQ: int
    Modulus: int
    P: int
    Q: int
class RSAPKCS1KeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    @property
    def RNG(self) -> RandomNumberGenerator:"""RNG { get; set; } -> RandomNumberGenerator"""
    def __init__(self, key: AsymmetricAlgorithm) -> RSAPKCS1KeyExchangeDeformatter:...
    def __init__(self) -> RSAPKCS1KeyExchangeDeformatter:...
class RSAPKCS1KeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    @property
    def Rng(self) -> RandomNumberGenerator:"""Rng { get; set; } -> RandomNumberGenerator"""
    def __init__(self, key: AsymmetricAlgorithm) -> RSAPKCS1KeyExchangeFormatter:...
    def __init__(self) -> RSAPKCS1KeyExchangeFormatter:...
class RSAPKCS1SignatureDeformatter(AsymmetricSignatureDeformatter):
    def __init__(self, key: AsymmetricAlgorithm) -> RSAPKCS1SignatureDeformatter:...
    def __init__(self) -> RSAPKCS1SignatureDeformatter:...
class RSAPKCS1SignatureFormatter(AsymmetricSignatureFormatter):
    def __init__(self, key: AsymmetricAlgorithm) -> RSAPKCS1SignatureFormatter:...
    def __init__(self) -> RSAPKCS1SignatureFormatter:...
class RSASignaturePadding(_n_2_t_8[RSASignaturePadding]):
    @property
    def Mode(self) -> RSASignaturePaddingMode:"""Mode { get; } -> RSASignaturePaddingMode"""
    @property
    def Pkcs1(self) -> RSASignaturePadding:"""Pkcs1 { get; } -> RSASignaturePadding"""
    @property
    def Pss(self) -> RSASignaturePadding:"""Pss { get; } -> RSASignaturePadding"""
class RSASignaturePaddingMode(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    Pkcs1: int
    Pss: int
    value__: int
class SHA1(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    pass
class SHA1Cng(SHA1, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA1Cng:...
class SHA1CryptoServiceProvider(SHA1, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA1CryptoServiceProvider:...
class SHA1Managed(SHA1, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA1Managed:...
class SHA256(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    pass
class SHA256Cng(SHA256, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA256Cng:...
class SHA256CryptoServiceProvider(SHA256, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA256CryptoServiceProvider:...
class SHA256Managed(SHA256, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA256Managed:...
class SHA384(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    pass
class SHA384Cng(SHA384, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA384Cng:...
class SHA384CryptoServiceProvider(SHA384, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA384CryptoServiceProvider:...
class SHA384Managed(SHA384, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA384Managed:...
class SHA512(HashAlgorithm, _n_2_t_0, ICryptoTransform):
    pass
class SHA512Cng(SHA512, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA512Cng:...
class SHA512CryptoServiceProvider(SHA512, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA512CryptoServiceProvider:...
class SHA512Managed(SHA512, _n_2_t_0, ICryptoTransform):
    def __init__(self) -> SHA512Managed:...
class SignatureDescription(object):
    @property
    def DeformatterAlgorithm(self) -> str:"""DeformatterAlgorithm { get; set; } -> str"""
    @property
    def DigestAlgorithm(self) -> str:"""DigestAlgorithm { get; set; } -> str"""
    @property
    def FormatterAlgorithm(self) -> str:"""FormatterAlgorithm { get; set; } -> str"""
    @property
    def KeyAlgorithm(self) -> str:"""KeyAlgorithm { get; set; } -> str"""
    def __init__(self, el: _n_9_t_2) -> SignatureDescription:...
    def __init__(self) -> SignatureDescription:...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:...
    def CreateDigest(self) -> HashAlgorithm:...
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:...
class SignatureVerificationResult(_n_2_t_4, _n_2_t_5, _n_2_t_6, _n_2_t_7):
    AssemblyIdentityMismatch: int
    BadDigest: int
    BadSignatureFormat: int
    BasicConstraintsNotObserved: int
    CertificateExpired: int
    CertificateExplicitlyDistrusted: int
    CertificateMalformed: int
    CertificateNotExplicitlyTrusted: int
    CertificateRevoked: int
    CertificateUsageNotAllowed: int
    ContainingSignatureInvalid: int
    CouldNotBuildChain: int
    GenericTrustFailure: int
    InvalidCertificateName: int
    InvalidCertificatePolicy: int
    InvalidCertificateRole: int
    InvalidCertificateSignature: int
    InvalidCertificateUsage: int
    InvalidCountersignature: int
    InvalidSignerCertificate: int
    InvalidTimePeriodNesting: int
    InvalidTimestamp: int
    IssuerChainingError: int
    MissingSignature: int
    PathLengthConstraintViolated: int
    PublicKeyTokenMismatch: int
    PublisherMismatch: int
    RevocationCheckFailure: int
    SystemError: int
    UnknownCriticalExtension: int
    UnknownTrustProvider: int
    UnknownVerificationAction: int
    UntrustedCertificationAuthority: int
    UntrustedRootCertificate: int
    UntrustedTestRootCertificate: int
    Valid: int
    value__: int
class StrongNameSignatureInformation(object):
    @property
    def HashAlgorithm(self) -> str:"""HashAlgorithm { get; } -> str"""
    @property
    def HResult(self) -> int:"""HResult { get; } -> int"""
    @property
    def IsValid(self) -> bool:"""IsValid { get; } -> bool"""
    @property
    def PublicKey(self) -> AsymmetricAlgorithm:"""PublicKey { get; } -> AsymmetricAlgorithm"""
    @property
    def VerificationResult(self) -> SignatureVerificationResult:"""VerificationResult { get; } -> SignatureVerificationResult"""
class SymmetricAlgorithm(_n_2_t_0):
    @property
    def BlockSize(self) -> int:"""BlockSize { get; set; } -> int"""
    @property
    def FeedbackSize(self) -> int:"""FeedbackSize { get; set; } -> int"""
    @property
    def IV(self) -> _n_2_t_2[_n_2_t_1]:"""IV { get; set; } -> Array"""
    @property
    def Key(self) -> _n_2_t_2[_n_2_t_1]:"""Key { get; set; } -> Array"""
    @property
    def KeySize(self) -> int:"""KeySize { get; set; } -> int"""
    @property
    def LegalBlockSizes(self) -> _n_2_t_2[KeySizes]:"""LegalBlockSizes { get; } -> Array"""
    @property
    def LegalKeySizes(self) -> _n_2_t_2[KeySizes]:"""LegalKeySizes { get; } -> Array"""
    @property
    def Mode(self) -> CipherMode:"""Mode { get; set; } -> CipherMode"""
    @property
    def Padding(self) -> PaddingMode:"""Padding { get; set; } -> PaddingMode"""
    def Clear(self):...
    @staticmethod
    def Create(algName: str) -> SymmetricAlgorithm:...
    @staticmethod
    def Create() -> SymmetricAlgorithm:...
    def CreateDecryptor(self, rgbKey: _n_2_t_2[_n_2_t_1], rgbIV: _n_2_t_2[_n_2_t_1]) -> ICryptoTransform:...
    def CreateDecryptor(self) -> ICryptoTransform:...
    def CreateEncryptor(self, rgbKey: _n_2_t_2[_n_2_t_1], rgbIV: _n_2_t_2[_n_2_t_1]) -> ICryptoTransform:...
    def CreateEncryptor(self) -> ICryptoTransform:...
    def GenerateIV(self):...
    def GenerateKey(self):...
    def ValidKeySize(self, bitLength: int) -> bool:...
class ToBase64Transform(ICryptoTransform):
    def __init__(self) -> ToBase64Transform:...
    def Clear(self):...
class TripleDES(SymmetricAlgorithm, _n_2_t_0):
    @staticmethod
    def IsWeakKey(rgbKey: _n_2_t_2[_n_2_t_1]) -> bool:...
class TripleDESCng(TripleDES, _n_2_t_0, _n_0_t_0):
    def __init__(self) -> TripleDESCng:...
    def __init__(self, keyName: str) -> TripleDESCng:...
    def __init__(self, keyName: str, provider: CngProvider) -> TripleDESCng:...
    def __init__(self, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> TripleDESCng:...
class TripleDESCryptoServiceProvider(TripleDES, _n_2_t_0):
    def __init__(self) -> TripleDESCryptoServiceProvider:...
