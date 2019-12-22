import __clrclasses__.System.Reflection.Emit as Emit
from __clrclasses__.System import SystemException as _n_0_t_0
from __clrclasses__.System import Exception as _n_0_t_1
from __clrclasses__.System import Type as _n_0_t_2
from __clrclasses__.System import Byte as _n_0_t_3
from __clrclasses__.System import Array as _n_0_t_4
from __clrclasses__.System import Attribute as _n_0_t_5
from __clrclasses__.System import UInt32 as _n_0_t_6
from __clrclasses__.System import Enum as _n_0_t_7
from __clrclasses__.System import IComparable as _n_0_t_8
from __clrclasses__.System import IFormattable as _n_0_t_9
from __clrclasses__.System import IConvertible as _n_0_t_10
from __clrclasses__.System import ICloneable as _n_0_t_11
from __clrclasses__.System import Version as _n_0_t_12
from __clrclasses__.System import MarshalByRefObject as _n_0_t_13
from __clrclasses__.System import FormatException as _n_0_t_14
from __clrclasses__.System import ValueType as _n_0_t_15
from __clrclasses__.System import RuntimeFieldHandle as _n_0_t_16
from __clrclasses__.System import RuntimeTypeHandle as _n_0_t_17
from __clrclasses__.System import ApplicationException as _n_0_t_18
from __clrclasses__.System import MulticastDelegate as _n_0_t_19
from __clrclasses__.System import IntPtr as _n_0_t_20
from __clrclasses__.System import IAsyncResult as _n_0_t_21
from __clrclasses__.System import AsyncCallback as _n_0_t_22
from __clrclasses__.System import RuntimeMethodHandle as _n_0_t_23
from __clrclasses__.System import Delegate as _n_0_t_24
from __clrclasses__.System import ModuleHandle as _n_0_t_25
from __clrclasses__.System import Guid as _n_0_t_26
from __clrclasses__.System import ResolveEventArgs as _n_0_t_27
from __clrclasses__.System import Void as _n_0_t_28
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IList as _n_1_t_1
from __clrclasses__.System.Configuration.Assemblies import AssemblyHashAlgorithm as _n_2_t_0
from __clrclasses__.System.Configuration.Assemblies import AssemblyVersionCompatibility as _n_2_t_1
from __clrclasses__.System.Globalization import CultureInfo as _n_3_t_0
from __clrclasses__.System.IO import FileStream as _n_4_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_5_t_0
from __clrclasses__.System.Runtime.InteropServices import _Assembly as _n_5_t_1
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_5_t_2
from __clrclasses__.System.Runtime.InteropServices import _AssemblyName as _n_5_t_3
from __clrclasses__.System.Runtime.InteropServices import _MemberInfo as _n_5_t_4
from __clrclasses__.System.Runtime.InteropServices import _MethodBase as _n_5_t_5
from __clrclasses__.System.Runtime.InteropServices import _ConstructorInfo as _n_5_t_6
from __clrclasses__.System.Runtime.InteropServices import _EventInfo as _n_5_t_7
from __clrclasses__.System.Runtime.InteropServices import _FieldInfo as _n_5_t_8
from __clrclasses__.System.Runtime.InteropServices import _MethodInfo as _n_5_t_9
from __clrclasses__.System.Runtime.InteropServices import _Module as _n_5_t_10
from __clrclasses__.System.Runtime.InteropServices import _ParameterInfo as _n_5_t_11
from __clrclasses__.System.Runtime.InteropServices import _PropertyInfo as _n_5_t_12
from __clrclasses__.System.Runtime.InteropServices import _Type as _n_5_t_13
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_6_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_6_t_1
from __clrclasses__.System.Runtime.Serialization import IObjectReference as _n_6_t_2
from __clrclasses__.System.Security import IEvidenceFactory as _n_7_t_0
from __clrclasses__.System.Security import PermissionSet as _n_7_t_1
from __clrclasses__.System.Security import SecurityRuleSet as _n_7_t_2
from __clrclasses__.System.Security import SecurityContextSource as _n_7_t_3
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509Certificate as _n_8_t_0
from __clrclasses__.System.Security.Policy import Evidence as _n_9_t_0
import typing
class AmbiguousMatchException(_n_0_t_0, _n_6_t_0, _n_5_t_0):
    def __init__(self) -> AmbiguousMatchException:...
    def __init__(self, message: str) -> AmbiguousMatchException:...
    def __init__(self, message: str, inner: _n_0_t_1) -> AmbiguousMatchException:...
class Assembly(_n_5_t_1, _n_7_t_0, ICustomAttributeProvider, _n_6_t_0):
    @property
    def CustomAttributes(self) -> _n_1_t_0[CustomAttributeData]:"""CustomAttributes { get; } -> IEnumerable"""
    @property
    def DefinedTypes(self) -> _n_1_t_0[TypeInfo]:"""DefinedTypes { get; } -> IEnumerable"""
    @property
    def ExportedTypes(self) -> _n_1_t_0[_n_0_t_2]:"""ExportedTypes { get; } -> IEnumerable"""
    @property
    def HostContext(self) -> int:"""HostContext { get; } -> int"""
    @property
    def ImageRuntimeVersion(self) -> str:"""ImageRuntimeVersion { get; } -> str"""
    @property
    def IsDynamic(self) -> bool:"""IsDynamic { get; } -> bool"""
    @property
    def IsFullyTrusted(self) -> bool:"""IsFullyTrusted { get; } -> bool"""
    @property
    def ManifestModule(self) -> Module:"""ManifestModule { get; } -> Module"""
    @property
    def Modules(self) -> _n_1_t_0[Module]:"""Modules { get; } -> IEnumerable"""
    @property
    def PermissionSet(self) -> _n_7_t_1:"""PermissionSet { get; } -> PermissionSet"""
    @property
    def ReflectionOnly(self) -> bool:"""ReflectionOnly { get; } -> bool"""
    @property
    def SecurityRuleSet(self) -> _n_7_t_2:"""SecurityRuleSet { get; } -> SecurityRuleSet"""
    @staticmethod
    def CreateQualifiedName(assemblyName: str, typeName: str) -> str:...
    @staticmethod
    def GetAssembly(type: _n_0_t_2) -> Assembly:...
    @staticmethod
    def GetCallingAssembly() -> Assembly:...
    def GetCustomAttributesData(self) -> _n_1_t_1[CustomAttributeData]:...
    @staticmethod
    def GetEntryAssembly() -> Assembly:...
    @staticmethod
    def GetExecutingAssembly() -> Assembly:...
    @staticmethod
    def Load(assemblyString: str) -> Assembly:...
    @staticmethod
    def Load(assemblyString: str, assemblySecurity: _n_9_t_0) -> Assembly:...
    @staticmethod
    def Load(assemblyRef: AssemblyName) -> Assembly:...
    @staticmethod
    def Load(assemblyRef: AssemblyName, assemblySecurity: _n_9_t_0) -> Assembly:...
    @staticmethod
    def Load(rawAssembly: _n_0_t_4[_n_0_t_3]) -> Assembly:...
    @staticmethod
    def Load(rawAssembly: _n_0_t_4[_n_0_t_3], rawSymbolStore: _n_0_t_4[_n_0_t_3]) -> Assembly:...
    @staticmethod
    def Load(rawAssembly: _n_0_t_4[_n_0_t_3], rawSymbolStore: _n_0_t_4[_n_0_t_3], securityContextSource: _n_7_t_3) -> Assembly:...
    @staticmethod
    def Load(rawAssembly: _n_0_t_4[_n_0_t_3], rawSymbolStore: _n_0_t_4[_n_0_t_3], securityEvidence: _n_9_t_0) -> Assembly:...
    @staticmethod
    def LoadFile(path: str) -> Assembly:...
    @staticmethod
    def LoadFile(path: str, securityEvidence: _n_9_t_0) -> Assembly:...
    @staticmethod
    def LoadFrom(assemblyFile: str) -> Assembly:...
    @staticmethod
    def LoadFrom(assemblyFile: str, securityEvidence: _n_9_t_0) -> Assembly:...
    @staticmethod
    def LoadFrom(assemblyFile: str, securityEvidence: _n_9_t_0, hashValue: _n_0_t_4[_n_0_t_3], hashAlgorithm: _n_2_t_0) -> Assembly:...
    @staticmethod
    def LoadFrom(assemblyFile: str, hashValue: _n_0_t_4[_n_0_t_3], hashAlgorithm: _n_2_t_0) -> Assembly:...
    @staticmethod
    def LoadWithPartialName(partialName: str) -> Assembly:...
    @staticmethod
    def LoadWithPartialName(partialName: str, securityEvidence: _n_9_t_0) -> Assembly:...
    @staticmethod
    def ReflectionOnlyLoad(assemblyString: str) -> Assembly:...
    @staticmethod
    def ReflectionOnlyLoad(rawAssembly: _n_0_t_4[_n_0_t_3]) -> Assembly:...
    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile: str) -> Assembly:...
    @staticmethod
    def UnsafeLoadFrom(assemblyFile: str) -> Assembly:...
    def GetCustomAttribute(self, attributeType: _n_0_t_2) -> _n_0_t_5:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self) -> typing.Any:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def IsDefined(self, attributeType: _n_0_t_2) -> bool:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
class AssemblyAlgorithmIdAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def AlgorithmId(self) -> _n_0_t_6:"""AlgorithmId { get; } -> UInt32"""
    def __init__(self, algorithmId: _n_2_t_0) -> AssemblyAlgorithmIdAttribute:...
    def __init__(self, algorithmId: _n_0_t_6) -> AssemblyAlgorithmIdAttribute:...
class AssemblyCompanyAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Company(self) -> str:"""Company { get; } -> str"""
    def __init__(self, company: str) -> AssemblyCompanyAttribute:...
class AssemblyConfigurationAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Configuration(self) -> str:"""Configuration { get; } -> str"""
    def __init__(self, configuration: str) -> AssemblyConfigurationAttribute:...
class AssemblyContentType(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Default: int
    value__: int
    WindowsRuntime: int
class AssemblyCopyrightAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Copyright(self) -> str:"""Copyright { get; } -> str"""
    def __init__(self, copyright: str) -> AssemblyCopyrightAttribute:...
class AssemblyCultureAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Culture(self) -> str:"""Culture { get; } -> str"""
    def __init__(self, culture: str) -> AssemblyCultureAttribute:...
class AssemblyDefaultAliasAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def DefaultAlias(self) -> str:"""DefaultAlias { get; } -> str"""
    def __init__(self, defaultAlias: str) -> AssemblyDefaultAliasAttribute:...
class AssemblyDelaySignAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def DelaySign(self) -> bool:"""DelaySign { get; } -> bool"""
    def __init__(self, delaySign: bool) -> AssemblyDelaySignAttribute:...
class AssemblyDescriptionAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    def __init__(self, description: str) -> AssemblyDescriptionAttribute:...
class AssemblyFileVersionAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Version(self) -> str:"""Version { get; } -> str"""
    def __init__(self, version: str) -> AssemblyFileVersionAttribute:...
class AssemblyFlagsAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def AssemblyFlags(self) -> int:"""AssemblyFlags { get; } -> int"""
    @property
    def Flags(self) -> _n_0_t_6:"""Flags { get; } -> UInt32"""
    def __init__(self, flags: _n_0_t_6) -> AssemblyFlagsAttribute:...
    def __init__(self, assemblyFlags: int) -> AssemblyFlagsAttribute:...
    def __init__(self, assemblyFlags: AssemblyNameFlags) -> AssemblyFlagsAttribute:...
class AssemblyInformationalVersionAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def InformationalVersion(self) -> str:"""InformationalVersion { get; } -> str"""
    def __init__(self, informationalVersion: str) -> AssemblyInformationalVersionAttribute:...
class AssemblyKeyFileAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def KeyFile(self) -> str:"""KeyFile { get; } -> str"""
    def __init__(self, keyFile: str) -> AssemblyKeyFileAttribute:...
class AssemblyKeyNameAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def KeyName(self) -> str:"""KeyName { get; } -> str"""
    def __init__(self, keyName: str) -> AssemblyKeyNameAttribute:...
class AssemblyMetadataAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Key(self) -> str:"""Key { get; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def __init__(self, key: str, value: str) -> AssemblyMetadataAttribute:...
class AssemblyName(_n_5_t_3, _n_0_t_11, _n_6_t_0, _n_6_t_1):
    @property
    def CodeBase(self) -> str:"""CodeBase { get; set; } -> str"""
    @property
    def ContentType(self) -> AssemblyContentType:"""ContentType { get; set; } -> AssemblyContentType"""
    @property
    def CultureInfo(self) -> _n_3_t_0:"""CultureInfo { get; set; } -> CultureInfo"""
    @property
    def CultureName(self) -> str:"""CultureName { get; set; } -> str"""
    @property
    def EscapedCodeBase(self) -> str:"""EscapedCodeBase { get; } -> str"""
    @property
    def Flags(self) -> AssemblyNameFlags:"""Flags { get; set; } -> AssemblyNameFlags"""
    @property
    def FullName(self) -> str:"""FullName { get; } -> str"""
    @property
    def HashAlgorithm(self) -> _n_2_t_0:"""HashAlgorithm { get; set; } -> AssemblyHashAlgorithm"""
    @property
    def KeyPair(self) -> StrongNameKeyPair:"""KeyPair { get; set; } -> StrongNameKeyPair"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:"""ProcessorArchitecture { get; set; } -> ProcessorArchitecture"""
    @property
    def Version(self) -> _n_0_t_12:"""Version { get; set; } -> Version"""
    @property
    def VersionCompatibility(self) -> _n_2_t_1:"""VersionCompatibility { get; set; } -> AssemblyVersionCompatibility"""
    def __init__(self) -> AssemblyName:...
    def __init__(self, assemblyName: str) -> AssemblyName:...
    @staticmethod
    def GetAssemblyName(assemblyFile: str) -> AssemblyName:...
    def GetPublicKey(self) -> _n_0_t_4[_n_0_t_3]:...
    def GetPublicKeyToken(self) -> _n_0_t_4[_n_0_t_3]:...
    @staticmethod
    def ReferenceMatchesDefinition(reference: AssemblyName, definition: AssemblyName) -> bool:...
    def SetPublicKey(self, publicKey: _n_0_t_4[_n_0_t_3]):...
    def SetPublicKeyToken(self, publicKeyToken: _n_0_t_4[_n_0_t_3]):...
class AssemblyNameFlags(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    EnableJITcompileOptimizer: int
    EnableJITcompileTracking: int
    _None: int
    PublicKey: int
    Retargetable: int
    value__: int
class AssemblyNameProxy(_n_0_t_13):
    def __init__(self) -> AssemblyNameProxy:...
    def GetAssemblyName(self, assemblyFile: str) -> AssemblyName:...
class AssemblyProductAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Product(self) -> str:"""Product { get; } -> str"""
    def __init__(self, product: str) -> AssemblyProductAttribute:...
class AssemblySignatureKeyAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Countersignature(self) -> str:"""Countersignature { get; } -> str"""
    @property
    def PublicKey(self) -> str:"""PublicKey { get; } -> str"""
    def __init__(self, publicKey: str, countersignature: str) -> AssemblySignatureKeyAttribute:...
class AssemblyTitleAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Title(self) -> str:"""Title { get; } -> str"""
    def __init__(self, title: str) -> AssemblyTitleAttribute:...
class AssemblyTrademarkAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Trademark(self) -> str:"""Trademark { get; } -> str"""
    def __init__(self, trademark: str) -> AssemblyTrademarkAttribute:...
class AssemblyVersionAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def Version(self) -> str:"""Version { get; } -> str"""
    def __init__(self, version: str) -> AssemblyVersionAttribute:...
class Binder(object):
    def BindToField(self, bindingAttr: BindingFlags, match: _n_0_t_4[FieldInfo], value: object, culture: _n_3_t_0) -> FieldInfo:...
    def BindToMethod(self, bindingAttr: BindingFlags, match: _n_0_t_4[MethodBase], args: _n_0_t_4[object], modifiers: _n_0_t_4[ParameterModifier], culture: _n_3_t_0, names: _n_0_t_4[str], state: object) -> MethodBase:...
    def ChangeType(self, value: object, type: _n_0_t_2, culture: _n_3_t_0) -> object:...
    def ReorderArgumentArray(self, args: _n_0_t_4[object], state: object):...
    def SelectMethod(self, bindingAttr: BindingFlags, match: _n_0_t_4[MethodBase], types: _n_0_t_4[_n_0_t_2], modifiers: _n_0_t_4[ParameterModifier]) -> MethodBase:...
    def SelectProperty(self, bindingAttr: BindingFlags, match: _n_0_t_4[PropertyInfo], returnType: _n_0_t_2, indexes: _n_0_t_4[_n_0_t_2], modifiers: _n_0_t_4[ParameterModifier]) -> PropertyInfo:...
class BindingFlags(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    CreateInstance: int
    DeclaredOnly: int
    Default: int
    ExactBinding: int
    FlattenHierarchy: int
    GetField: int
    GetProperty: int
    IgnoreCase: int
    IgnoreReturn: int
    Instance: int
    InvokeMethod: int
    NonPublic: int
    OptionalParamBinding: int
    Public: int
    PutDispProperty: int
    PutRefDispProperty: int
    SetField: int
    SetProperty: int
    Static: int
    SuppressChangeType: int
    value__: int
class CallingConventions(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Any: int
    ExplicitThis: int
    HasThis: int
    Standard: int
    value__: int
    VarArgs: int
class ConstructorInfo(MethodBase, ICustomAttributeProvider, _n_5_t_4, _n_5_t_5, _n_5_t_6):
    ConstructorName: int
    TypeConstructorName: int
class CustomAttributeData(object):
    @property
    def AttributeType(self) -> _n_0_t_2:"""AttributeType { get; } -> Type"""
    @property
    def Constructor(self) -> ConstructorInfo:"""Constructor { get; } -> ConstructorInfo"""
    @property
    def ConstructorArguments(self) -> _n_1_t_1[CustomAttributeTypedArgument]:"""ConstructorArguments { get; } -> IList"""
    @property
    def NamedArguments(self) -> _n_1_t_1[CustomAttributeNamedArgument]:"""NamedArguments { get; } -> IList"""
    @staticmethod
    def GetCustomAttributes(target: MemberInfo) -> _n_1_t_1[CustomAttributeData]:...
    @staticmethod
    def GetCustomAttributes(target: Module) -> _n_1_t_1[CustomAttributeData]:...
    @staticmethod
    def GetCustomAttributes(target: Assembly) -> _n_1_t_1[CustomAttributeData]:...
    @staticmethod
    def GetCustomAttributes(target: ParameterInfo) -> _n_1_t_1[CustomAttributeData]:...
class CustomAttributeExtensions(object):
    @staticmethod
    def GetCustomAttribute(element: Assembly, attributeType: _n_0_t_2) -> _n_0_t_5:...
    @staticmethod
    def GetCustomAttribute(element: Module, attributeType: _n_0_t_2) -> _n_0_t_5:...
    @staticmethod
    def GetCustomAttribute(element: MemberInfo, attributeType: _n_0_t_2) -> _n_0_t_5:...
    @staticmethod
    def GetCustomAttribute(element: ParameterInfo, attributeType: _n_0_t_2) -> _n_0_t_5:...
    @staticmethod
    def GetCustomAttribute(element: Assembly) -> typing.Any:...
    @staticmethod
    def GetCustomAttribute(element: Module) -> typing.Any:...
    @staticmethod
    def GetCustomAttribute(element: MemberInfo) -> typing.Any:...
    @staticmethod
    def GetCustomAttribute(element: ParameterInfo) -> typing.Any:...
    @staticmethod
    def GetCustomAttribute(element: MemberInfo, attributeType: _n_0_t_2, inherit: bool) -> _n_0_t_5:...
    @staticmethod
    def GetCustomAttribute(element: ParameterInfo, attributeType: _n_0_t_2, inherit: bool) -> _n_0_t_5:...
    @staticmethod
    def GetCustomAttribute(element: MemberInfo, inherit: bool) -> typing.Any:...
    @staticmethod
    def GetCustomAttribute(element: ParameterInfo, inherit: bool) -> typing.Any:...
    @staticmethod
    def GetCustomAttributes(element: Assembly) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: Module) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: MemberInfo) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: MemberInfo, inherit: bool) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo, inherit: bool) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: Assembly, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: Module, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: MemberInfo, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: MemberInfo, attributeType: _n_0_t_2, inherit: bool) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def GetCustomAttributes(element: ParameterInfo, attributeType: _n_0_t_2, inherit: bool) -> _n_1_t_0[_n_0_t_5]:...
    @staticmethod
    def IsDefined(element: Assembly, attributeType: _n_0_t_2) -> bool:...
    @staticmethod
    def IsDefined(element: Module, attributeType: _n_0_t_2) -> bool:...
    @staticmethod
    def IsDefined(element: MemberInfo, attributeType: _n_0_t_2) -> bool:...
    @staticmethod
    def IsDefined(element: ParameterInfo, attributeType: _n_0_t_2) -> bool:...
    @staticmethod
    def IsDefined(element: MemberInfo, attributeType: _n_0_t_2, inherit: bool) -> bool:...
    @staticmethod
    def IsDefined(element: ParameterInfo, attributeType: _n_0_t_2, inherit: bool) -> bool:...
class CustomAttributeFormatException(_n_0_t_14, _n_6_t_0, _n_5_t_0):
    def __init__(self) -> CustomAttributeFormatException:...
    def __init__(self, message: str) -> CustomAttributeFormatException:...
    def __init__(self, message: str, inner: _n_0_t_1) -> CustomAttributeFormatException:...
class CustomAttributeNamedArgument(_n_0_t_15):
    @property
    def IsField(self) -> bool:"""IsField { get; } -> bool"""
    @property
    def MemberInfo(self) -> MemberInfo:"""MemberInfo { get; } -> MemberInfo"""
    @property
    def MemberName(self) -> str:"""MemberName { get; } -> str"""
    @property
    def TypedValue(self) -> CustomAttributeTypedArgument:"""TypedValue { get; } -> CustomAttributeTypedArgument"""
    def __init__(self, memberInfo: MemberInfo, value: object) -> CustomAttributeNamedArgument:...
    def __init__(self, memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument) -> CustomAttributeNamedArgument:...
class CustomAttributeTypedArgument(_n_0_t_15):
    @property
    def ArgumentType(self) -> _n_0_t_2:"""ArgumentType { get; } -> Type"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
    def __init__(self, argumentType: _n_0_t_2, value: object) -> CustomAttributeTypedArgument:...
    def __init__(self, value: object) -> CustomAttributeTypedArgument:...
class DefaultMemberAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def MemberName(self) -> str:"""MemberName { get; } -> str"""
    def __init__(self, memberName: str) -> DefaultMemberAttribute:...
class EventAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    _None: int
    ReservedMask: int
    RTSpecialName: int
    SpecialName: int
    value__: int
class EventInfo(MemberInfo, ICustomAttributeProvider, _n_5_t_4, _n_5_t_7):
    @property
    def AddMethod(self) -> MethodInfo:"""AddMethod { get; } -> MethodInfo"""
    @property
    def RaiseMethod(self) -> MethodInfo:"""RaiseMethod { get; } -> MethodInfo"""
    @property
    def RemoveMethod(self) -> MethodInfo:"""RemoveMethod { get; } -> MethodInfo"""
    def GetOtherMethods(self, nonPublic: bool) -> _n_0_t_4[MethodInfo]:...
    def GetOtherMethods(self) -> _n_0_t_4[MethodInfo]:...
class ExceptionHandlingClause(object):
    @property
    def CatchType(self) -> _n_0_t_2:"""CatchType { get; } -> Type"""
    @property
    def FilterOffset(self) -> int:"""FilterOffset { get; } -> int"""
    @property
    def Flags(self) -> ExceptionHandlingClauseOptions:"""Flags { get; } -> ExceptionHandlingClauseOptions"""
    @property
    def HandlerLength(self) -> int:"""HandlerLength { get; } -> int"""
    @property
    def HandlerOffset(self) -> int:"""HandlerOffset { get; } -> int"""
    @property
    def TryLength(self) -> int:"""TryLength { get; } -> int"""
    @property
    def TryOffset(self) -> int:"""TryOffset { get; } -> int"""
class ExceptionHandlingClauseOptions(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Clause: int
    Fault: int
    Filter: int
    Finally: int
    value__: int
class FieldAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Assembly: int
    FamANDAssem: int
    Family: int
    FamORAssem: int
    FieldAccessMask: int
    HasDefault: int
    HasFieldMarshal: int
    HasFieldRVA: int
    InitOnly: int
    Literal: int
    NotSerialized: int
    PinvokeImpl: int
    Private: int
    PrivateScope: int
    Public: int
    ReservedMask: int
    RTSpecialName: int
    SpecialName: int
    Static: int
    value__: int
class FieldInfo(MemberInfo, ICustomAttributeProvider, _n_5_t_4, _n_5_t_8):
    @property
    def IsSecurityCritical(self) -> bool:"""IsSecurityCritical { get; } -> bool"""
    @property
    def IsSecuritySafeCritical(self) -> bool:"""IsSecuritySafeCritical { get; } -> bool"""
    @property
    def IsSecurityTransparent(self) -> bool:"""IsSecurityTransparent { get; } -> bool"""
    @staticmethod
    def GetFieldFromHandle(handle: _n_0_t_16) -> FieldInfo:...
    @staticmethod
    def GetFieldFromHandle(handle: _n_0_t_16, declaringType: _n_0_t_17) -> FieldInfo:...
    def GetOptionalCustomModifiers(self) -> _n_0_t_4[_n_0_t_2]:...
    def GetRawConstantValue(self) -> object:...
    def GetRequiredCustomModifiers(self) -> _n_0_t_4[_n_0_t_2]:...
class GenericParameterAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Contravariant: int
    Covariant: int
    DefaultConstructorConstraint: int
    _None: int
    NotNullableValueTypeConstraint: int
    ReferenceTypeConstraint: int
    SpecialConstraintMask: int
    value__: int
    VarianceMask: int
class ICustomAttributeProvider():
    def GetCustomAttributes(self, attributeType: _n_0_t_2, inherit: bool) -> _n_0_t_4[object]:...
    def GetCustomAttributes(self, inherit: bool) -> _n_0_t_4[object]:...
    def IsDefined(self, attributeType: _n_0_t_2, inherit: bool) -> bool:...
class ICustomTypeProvider():
    def GetCustomType(self) -> _n_0_t_2:...
class ImageFileMachine(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    AMD64: int
    ARM: int
    I386: int
    IA64: int
    value__: int
class InterfaceMapping(_n_0_t_15):
    InterfaceMethods: int
    InterfaceType: int
    TargetMethods: int
    TargetType: int
class IntrospectionExtensions(object):
    @staticmethod
    def GetTypeInfo(type: _n_0_t_2) -> TypeInfo:...
class InvalidFilterCriteriaException(_n_0_t_18, _n_6_t_0, _n_5_t_0):
    def __init__(self) -> InvalidFilterCriteriaException:...
    def __init__(self, message: str) -> InvalidFilterCriteriaException:...
    def __init__(self, message: str, inner: _n_0_t_1) -> InvalidFilterCriteriaException:...
class IReflect():
    @property
    def UnderlyingSystemType(self) -> _n_0_t_2:"""UnderlyingSystemType { get; } -> Type"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:...
    def GetFields(self, bindingAttr: BindingFlags) -> _n_0_t_4[FieldInfo]:...
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> _n_0_t_4[MemberInfo]:...
    def GetMembers(self, bindingAttr: BindingFlags) -> _n_0_t_4[MemberInfo]:...
    def GetMethod(self, name: str, bindingAttr: BindingFlags, binder: Binder, types: _n_0_t_4[_n_0_t_2], modifiers: _n_0_t_4[ParameterModifier]) -> MethodInfo:...
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:...
    def GetMethods(self, bindingAttr: BindingFlags) -> _n_0_t_4[MethodInfo]:...
    def GetProperties(self, bindingAttr: BindingFlags) -> _n_0_t_4[PropertyInfo]:...
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:...
    def GetProperty(self, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: _n_0_t_2, types: _n_0_t_4[_n_0_t_2], modifiers: _n_0_t_4[ParameterModifier]) -> PropertyInfo:...
    def InvokeMember(self, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: _n_0_t_4[object], modifiers: _n_0_t_4[ParameterModifier], culture: _n_3_t_0, namedParameters: _n_0_t_4[str]) -> object:...
class IReflectableType():
    def GetTypeInfo(self) -> TypeInfo:...
class LocalVariableInfo(object):
    @property
    def IsPinned(self) -> bool:"""IsPinned { get; } -> bool"""
    @property
    def LocalIndex(self) -> int:"""LocalIndex { get; } -> int"""
    @property
    def LocalType(self) -> _n_0_t_2:"""LocalType { get; } -> Type"""
class ManifestResourceInfo(object):
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def ReferencedAssembly(self) -> Assembly:"""ReferencedAssembly { get; } -> Assembly"""
    @property
    def ResourceLocation(self) -> ResourceLocation:"""ResourceLocation { get; } -> ResourceLocation"""
    def __init__(self, containingAssembly: Assembly, containingFileName: str, resourceLocation: ResourceLocation) -> ManifestResourceInfo:...
class MemberFilter(_n_0_t_19, _n_0_t_11, _n_6_t_0):
    def __init__(self, object: object, method: _n_0_t_20) -> MemberFilter:...
    def BeginInvoke(self, m: MemberInfo, filterCriteria: object, callback: _n_0_t_22, object: object) -> _n_0_t_21:...
    def EndInvoke(self, result: _n_0_t_21) -> bool:...
    def Invoke(self, m: MemberInfo, filterCriteria: object) -> bool:...
class MemberInfo(ICustomAttributeProvider, _n_5_t_4):
    @property
    def CustomAttributes(self) -> _n_1_t_0[CustomAttributeData]:"""CustomAttributes { get; } -> IEnumerable"""
    @property
    def MetadataToken(self) -> int:"""MetadataToken { get; } -> int"""
    @property
    def Module(self) -> Module:"""Module { get; } -> Module"""
    def GetCustomAttributesData(self) -> _n_1_t_1[CustomAttributeData]:...
    def GetCustomAttribute(self, attributeType: _n_0_t_2) -> _n_0_t_5:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self) -> typing.Any:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self, attributeType: _n_0_t_2, inherit: bool) -> _n_0_t_5:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self, inherit: bool) -> typing.Any:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, inherit: bool) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, attributeType: _n_0_t_2, inherit: bool) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def IsDefined(self, attributeType: _n_0_t_2) -> bool:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def IsDefined(self, attributeType: _n_0_t_2, inherit: bool) -> bool:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
class MemberTypes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    All: int
    Constructor: int
    Custom: int
    Event: int
    Field: int
    Method: int
    NestedType: int
    Property: int
    TypeInfo: int
    value__: int
class MethodAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Abstract: int
    Assembly: int
    CheckAccessOnOverride: int
    FamANDAssem: int
    Family: int
    FamORAssem: int
    Final: int
    HasSecurity: int
    HideBySig: int
    MemberAccessMask: int
    NewSlot: int
    PinvokeImpl: int
    Private: int
    PrivateScope: int
    Public: int
    RequireSecObject: int
    ReservedMask: int
    ReuseSlot: int
    RTSpecialName: int
    SpecialName: int
    Static: int
    UnmanagedExport: int
    value__: int
    Virtual: int
    VtableLayoutMask: int
class MethodBase(MemberInfo, ICustomAttributeProvider, _n_5_t_4, _n_5_t_5):
    @property
    def ContainsGenericParameters(self) -> bool:"""ContainsGenericParameters { get; } -> bool"""
    @property
    def IsGenericMethod(self) -> bool:"""IsGenericMethod { get; } -> bool"""
    @property
    def IsGenericMethodDefinition(self) -> bool:"""IsGenericMethodDefinition { get; } -> bool"""
    @property
    def IsSecurityCritical(self) -> bool:"""IsSecurityCritical { get; } -> bool"""
    @property
    def IsSecuritySafeCritical(self) -> bool:"""IsSecuritySafeCritical { get; } -> bool"""
    @property
    def IsSecurityTransparent(self) -> bool:"""IsSecurityTransparent { get; } -> bool"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:"""MethodImplementationFlags { get; } -> MethodImplAttributes"""
    @staticmethod
    def GetCurrentMethod() -> MethodBase:...
    def GetGenericArguments(self) -> _n_0_t_4[_n_0_t_2]:...
    def GetMethodBody(self) -> MethodBody:...
    @staticmethod
    def GetMethodFromHandle(handle: _n_0_t_23) -> MethodBase:...
    @staticmethod
    def GetMethodFromHandle(handle: _n_0_t_23, declaringType: _n_0_t_17) -> MethodBase:...
class MethodBody(object):
    @property
    def ExceptionHandlingClauses(self) -> _n_1_t_1[ExceptionHandlingClause]:"""ExceptionHandlingClauses { get; } -> IList"""
    @property
    def InitLocals(self) -> bool:"""InitLocals { get; } -> bool"""
    @property
    def LocalSignatureMetadataToken(self) -> int:"""LocalSignatureMetadataToken { get; } -> int"""
    @property
    def LocalVariables(self) -> _n_1_t_1[LocalVariableInfo]:"""LocalVariables { get; } -> IList"""
    @property
    def MaxStackSize(self) -> int:"""MaxStackSize { get; } -> int"""
    def GetILAsByteArray(self) -> _n_0_t_4[_n_0_t_3]:...
class MethodImplAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    AggressiveInlining: int
    CodeTypeMask: int
    ForwardRef: int
    IL: int
    InternalCall: int
    Managed: int
    ManagedMask: int
    MaxMethodImplVal: int
    Native: int
    NoInlining: int
    NoOptimization: int
    OPTIL: int
    PreserveSig: int
    Runtime: int
    Synchronized: int
    Unmanaged: int
    value__: int
class MethodInfo(MethodBase, ICustomAttributeProvider, _n_5_t_4, _n_5_t_5, _n_5_t_9):
    @property
    def ReturnParameter(self) -> ParameterInfo:"""ReturnParameter { get; } -> ParameterInfo"""
    def CreateDelegate(self, delegateType: _n_0_t_2) -> _n_0_t_24:...
    def CreateDelegate(self, delegateType: _n_0_t_2, target: object) -> _n_0_t_24:...
    def GetGenericMethodDefinition(self) -> MethodInfo:...
    def MakeGenericMethod(self, typeArguments: _n_0_t_4[_n_0_t_2]) -> MethodInfo:...
    def GetRuntimeBaseDefinition(self) -> MethodInfo:
        """Extension from: System.Reflection.RuntimeReflectionExtensions"""
class Missing(_n_6_t_0):
    Value: int
class Module(_n_5_t_10, _n_6_t_0, ICustomAttributeProvider):
    FilterTypeName: int
    FilterTypeNameIgnoreCase: int
    @property
    def Assembly(self) -> Assembly:"""Assembly { get; } -> Assembly"""
    @property
    def CustomAttributes(self) -> _n_1_t_0[CustomAttributeData]:"""CustomAttributes { get; } -> IEnumerable"""
    @property
    def FullyQualifiedName(self) -> str:"""FullyQualifiedName { get; } -> str"""
    @property
    def MDStreamVersion(self) -> int:"""MDStreamVersion { get; } -> int"""
    @property
    def MetadataToken(self) -> int:"""MetadataToken { get; } -> int"""
    @property
    def ModuleHandle(self) -> _n_0_t_25:"""ModuleHandle { get; } -> ModuleHandle"""
    @property
    def ModuleVersionId(self) -> _n_0_t_26:"""ModuleVersionId { get; } -> Guid"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def ScopeName(self) -> str:"""ScopeName { get; } -> str"""
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> _n_0_t_4[_n_0_t_2]:...
    def GetCustomAttributesData(self) -> _n_1_t_1[CustomAttributeData]:...
    def GetField(self, name: str) -> FieldInfo:...
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:...
    def GetFields(self) -> _n_0_t_4[FieldInfo]:...
    def GetFields(self, bindingFlags: BindingFlags) -> _n_0_t_4[FieldInfo]:...
    def GetMethod(self, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: _n_0_t_4[_n_0_t_2], modifiers: _n_0_t_4[ParameterModifier]) -> MethodInfo:...
    def GetMethod(self, name: str, types: _n_0_t_4[_n_0_t_2]) -> MethodInfo:...
    def GetMethod(self, name: str) -> MethodInfo:...
    def GetMethods(self) -> _n_0_t_4[MethodInfo]:...
    def GetMethods(self, bindingFlags: BindingFlags) -> _n_0_t_4[MethodInfo]:...
    def GetPEKind(self, peKind: PortableExecutableKinds, machine: ImageFileMachine):...
    def GetSignerCertificate(self) -> _n_8_t_0:...
    def GetTypes(self) -> _n_0_t_4[_n_0_t_2]:...
    def IsResource(self) -> bool:...
    def ResolveField(self, metadataToken: int) -> FieldInfo:...
    def ResolveField(self, metadataToken: int, genericTypeArguments: _n_0_t_4[_n_0_t_2], genericMethodArguments: _n_0_t_4[_n_0_t_2]) -> FieldInfo:...
    def ResolveMember(self, metadataToken: int) -> MemberInfo:...
    def ResolveMember(self, metadataToken: int, genericTypeArguments: _n_0_t_4[_n_0_t_2], genericMethodArguments: _n_0_t_4[_n_0_t_2]) -> MemberInfo:...
    def ResolveMethod(self, metadataToken: int) -> MethodBase:...
    def ResolveMethod(self, metadataToken: int, genericTypeArguments: _n_0_t_4[_n_0_t_2], genericMethodArguments: _n_0_t_4[_n_0_t_2]) -> MethodBase:...
    def ResolveSignature(self, metadataToken: int) -> _n_0_t_4[_n_0_t_3]:...
    def ResolveString(self, metadataToken: int) -> str:...
    def ResolveType(self, metadataToken: int) -> _n_0_t_2:...
    def ResolveType(self, metadataToken: int, genericTypeArguments: _n_0_t_4[_n_0_t_2], genericMethodArguments: _n_0_t_4[_n_0_t_2]) -> _n_0_t_2:...
    def GetCustomAttribute(self, attributeType: _n_0_t_2) -> _n_0_t_5:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self) -> typing.Any:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def IsDefined(self, attributeType: _n_0_t_2) -> bool:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
class ModuleResolveEventHandler(_n_0_t_19, _n_0_t_11, _n_6_t_0):
    def __init__(self, object: object, method: _n_0_t_20) -> ModuleResolveEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_0_t_27, callback: _n_0_t_22, object: object) -> _n_0_t_21:...
    def EndInvoke(self, result: _n_0_t_21) -> Module:...
    def Invoke(self, sender: object, e: _n_0_t_27) -> Module:...
class ObfuscateAssemblyAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def AssemblyIsPrivate(self) -> bool:"""AssemblyIsPrivate { get; } -> bool"""
    @property
    def StripAfterObfuscation(self) -> bool:"""StripAfterObfuscation { get; set; } -> bool"""
    def __init__(self, assemblyIsPrivate: bool) -> ObfuscateAssemblyAttribute:...
class ObfuscationAttribute(_n_0_t_5, _n_5_t_2):
    @property
    def ApplyToMembers(self) -> bool:"""ApplyToMembers { get; set; } -> bool"""
    @property
    def Exclude(self) -> bool:"""Exclude { get; set; } -> bool"""
    @property
    def Feature(self) -> str:"""Feature { get; set; } -> str"""
    @property
    def StripAfterObfuscation(self) -> bool:"""StripAfterObfuscation { get; set; } -> bool"""
    def __init__(self) -> ObfuscationAttribute:...
class ParameterAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    HasDefault: int
    HasFieldMarshal: int
    In: int
    Lcid: int
    _None: int
    Optional: int
    Out: int
    Reserved3: int
    Reserved4: int
    ReservedMask: int
    Retval: int
    value__: int
class ParameterInfo(_n_5_t_11, ICustomAttributeProvider, _n_6_t_2):
    @property
    def Attributes(self) -> ParameterAttributes:"""Attributes { get; } -> ParameterAttributes"""
    @property
    def CustomAttributes(self) -> _n_1_t_0[CustomAttributeData]:"""CustomAttributes { get; } -> IEnumerable"""
    @property
    def DefaultValue(self) -> object:"""DefaultValue { get; } -> object"""
    @property
    def HasDefaultValue(self) -> bool:"""HasDefaultValue { get; } -> bool"""
    @property
    def IsIn(self) -> bool:"""IsIn { get; } -> bool"""
    @property
    def IsLcid(self) -> bool:"""IsLcid { get; } -> bool"""
    @property
    def IsOptional(self) -> bool:"""IsOptional { get; } -> bool"""
    @property
    def IsOut(self) -> bool:"""IsOut { get; } -> bool"""
    @property
    def IsRetval(self) -> bool:"""IsRetval { get; } -> bool"""
    @property
    def Member(self) -> MemberInfo:"""Member { get; } -> MemberInfo"""
    @property
    def MetadataToken(self) -> int:"""MetadataToken { get; } -> int"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def ParameterType(self) -> _n_0_t_2:"""ParameterType { get; } -> Type"""
    @property
    def Position(self) -> int:"""Position { get; } -> int"""
    @property
    def RawDefaultValue(self) -> object:"""RawDefaultValue { get; } -> object"""
    def GetCustomAttributesData(self) -> _n_1_t_1[CustomAttributeData]:...
    def GetOptionalCustomModifiers(self) -> _n_0_t_4[_n_0_t_2]:...
    def GetRequiredCustomModifiers(self) -> _n_0_t_4[_n_0_t_2]:...
    def GetCustomAttribute(self, attributeType: _n_0_t_2) -> _n_0_t_5:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self) -> typing.Any:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self, attributeType: _n_0_t_2, inherit: bool) -> _n_0_t_5:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttribute(self, inherit: bool) -> typing.Any:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, inherit: bool) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, attributeType: _n_0_t_2) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def GetCustomAttributes(self, attributeType: _n_0_t_2, inherit: bool) -> _n_1_t_0[_n_0_t_5]:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def IsDefined(self, attributeType: _n_0_t_2) -> bool:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
    def IsDefined(self, attributeType: _n_0_t_2, inherit: bool) -> bool:
        """Extension from: System.Reflection.CustomAttributeExtensions"""
class ParameterModifier(_n_0_t_15, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> bool:"""Item { get; set; } -> bool"""
    def __init__(self, parameterCount: int) -> ParameterModifier:...
class Pointer(_n_6_t_0):
    @staticmethod
    def Box(ptr: _n_0_t_28, type: _n_0_t_2) -> object:...
    @staticmethod
    def Unbox(ptr: object) -> _n_0_t_28:...
class PortableExecutableKinds(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    ILOnly: int
    NotAPortableExecutableImage: int
    PE32Plus: int
    Preferred32Bit: int
    Required32Bit: int
    Unmanaged32Bit: int
    value__: int
class ProcessorArchitecture(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Amd64: int
    Arm: int
    IA64: int
    MSIL: int
    _None: int
    value__: int
    X86: int
class PropertyAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    HasDefault: int
    _None: int
    Reserved2: int
    Reserved3: int
    Reserved4: int
    ReservedMask: int
    RTSpecialName: int
    SpecialName: int
    value__: int
class PropertyInfo(MemberInfo, ICustomAttributeProvider, _n_5_t_4, _n_5_t_12):
    @property
    def GetMethod(self) -> MethodInfo:"""GetMethod { get; } -> MethodInfo"""
    @property
    def SetMethod(self) -> MethodInfo:"""SetMethod { get; } -> MethodInfo"""
    def GetConstantValue(self) -> object:...
    def GetOptionalCustomModifiers(self) -> _n_0_t_4[_n_0_t_2]:...
    def GetRawConstantValue(self) -> object:...
    def GetRequiredCustomModifiers(self) -> _n_0_t_4[_n_0_t_2]:...
class ReflectionContext(object):
    def GetTypeForObject(self, value: object) -> TypeInfo:...
    def MapAssembly(self, assembly: Assembly) -> Assembly:...
    def MapType(self, type: TypeInfo) -> TypeInfo:...
class ReflectionTypeLoadException(_n_0_t_0, _n_6_t_0, _n_5_t_0):
    @property
    def LoaderExceptions(self) -> _n_0_t_4[_n_0_t_1]:"""LoaderExceptions { get; } -> Array"""
    @property
    def Types(self) -> _n_0_t_4[_n_0_t_2]:"""Types { get; } -> Array"""
    def __init__(self, classes: _n_0_t_4[_n_0_t_2], exceptions: _n_0_t_4[_n_0_t_1]) -> ReflectionTypeLoadException:...
    def __init__(self, classes: _n_0_t_4[_n_0_t_2], exceptions: _n_0_t_4[_n_0_t_1], message: str) -> ReflectionTypeLoadException:...
class ResourceAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Private: int
    Public: int
    value__: int
class ResourceLocation(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    ContainedInAnotherAssembly: int
    ContainedInManifestFile: int
    Embedded: int
    value__: int
class RuntimeReflectionExtensions(object):
    @staticmethod
    def GetMethodInfo(_del: _n_0_t_24) -> MethodInfo:...
    @staticmethod
    def GetRuntimeBaseDefinition(method: MethodInfo) -> MethodInfo:...
    @staticmethod
    def GetRuntimeEvent(type: _n_0_t_2, name: str) -> EventInfo:...
    @staticmethod
    def GetRuntimeEvents(type: _n_0_t_2) -> _n_1_t_0[EventInfo]:...
    @staticmethod
    def GetRuntimeField(type: _n_0_t_2, name: str) -> FieldInfo:...
    @staticmethod
    def GetRuntimeFields(type: _n_0_t_2) -> _n_1_t_0[FieldInfo]:...
    @staticmethod
    def GetRuntimeInterfaceMap(typeInfo: TypeInfo, interfaceType: _n_0_t_2) -> InterfaceMapping:...
    @staticmethod
    def GetRuntimeMethod(type: _n_0_t_2, name: str, parameters: _n_0_t_4[_n_0_t_2]) -> MethodInfo:...
    @staticmethod
    def GetRuntimeMethods(type: _n_0_t_2) -> _n_1_t_0[MethodInfo]:...
    @staticmethod
    def GetRuntimeProperties(type: _n_0_t_2) -> _n_1_t_0[PropertyInfo]:...
    @staticmethod
    def GetRuntimeProperty(type: _n_0_t_2, name: str) -> PropertyInfo:...
class StrongNameKeyPair(_n_6_t_1, _n_6_t_0):
    @property
    def PublicKey(self) -> _n_0_t_4[_n_0_t_3]:"""PublicKey { get; } -> Array"""
    def __init__(self, keyPairFile: _n_4_t_0) -> StrongNameKeyPair:...
    def __init__(self, keyPairArray: _n_0_t_4[_n_0_t_3]) -> StrongNameKeyPair:...
    def __init__(self, keyPairContainer: str) -> StrongNameKeyPair:...
class TargetException(_n_0_t_18, _n_6_t_0, _n_5_t_0):
    def __init__(self) -> TargetException:...
    def __init__(self, message: str) -> TargetException:...
    def __init__(self, message: str, inner: _n_0_t_1) -> TargetException:...
class TargetInvocationException(_n_0_t_18, _n_6_t_0, _n_5_t_0):
    def __init__(self, inner: _n_0_t_1) -> TargetInvocationException:...
    def __init__(self, message: str, inner: _n_0_t_1) -> TargetInvocationException:...
class TargetParameterCountException(_n_0_t_18, _n_6_t_0, _n_5_t_0):
    def __init__(self) -> TargetParameterCountException:...
    def __init__(self, message: str) -> TargetParameterCountException:...
    def __init__(self, message: str, inner: _n_0_t_1) -> TargetParameterCountException:...
class TypeAttributes(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Abstract: int
    AnsiClass: int
    AutoClass: int
    AutoLayout: int
    BeforeFieldInit: int
    Class: int
    ClassSemanticsMask: int
    CustomFormatClass: int
    CustomFormatMask: int
    ExplicitLayout: int
    HasSecurity: int
    Import: int
    Interface: int
    LayoutMask: int
    NestedAssembly: int
    NestedFamANDAssem: int
    NestedFamily: int
    NestedFamORAssem: int
    NestedPrivate: int
    NestedPublic: int
    NotPublic: int
    Public: int
    ReservedMask: int
    RTSpecialName: int
    Sealed: int
    SequentialLayout: int
    Serializable: int
    SpecialName: int
    StringFormatMask: int
    UnicodeClass: int
    value__: int
    VisibilityMask: int
    WindowsRuntime: int
class TypeDelegator(TypeInfo, ICustomAttributeProvider, _n_5_t_4, _n_5_t_13, IReflect, IReflectableType):
    def __init__(self, delegatingType: _n_0_t_2) -> TypeDelegator:...
class TypeFilter(_n_0_t_19, _n_0_t_11, _n_6_t_0):
    def __init__(self, object: object, method: _n_0_t_20) -> TypeFilter:...
    def BeginInvoke(self, m: _n_0_t_2, filterCriteria: object, callback: _n_0_t_22, object: object) -> _n_0_t_21:...
    def EndInvoke(self, result: _n_0_t_21) -> bool:...
    def Invoke(self, m: _n_0_t_2, filterCriteria: object) -> bool:...
class TypeInfo(_n_0_t_2, ICustomAttributeProvider, _n_5_t_4, _n_5_t_13, IReflect, IReflectableType):
    @property
    def DeclaredConstructors(self) -> _n_1_t_0[ConstructorInfo]:"""DeclaredConstructors { get; } -> IEnumerable"""
    @property
    def DeclaredEvents(self) -> _n_1_t_0[EventInfo]:"""DeclaredEvents { get; } -> IEnumerable"""
    @property
    def DeclaredFields(self) -> _n_1_t_0[FieldInfo]:"""DeclaredFields { get; } -> IEnumerable"""
    @property
    def DeclaredMembers(self) -> _n_1_t_0[MemberInfo]:"""DeclaredMembers { get; } -> IEnumerable"""
    @property
    def DeclaredMethods(self) -> _n_1_t_0[MethodInfo]:"""DeclaredMethods { get; } -> IEnumerable"""
    @property
    def DeclaredNestedTypes(self) -> _n_1_t_0[TypeInfo]:"""DeclaredNestedTypes { get; } -> IEnumerable"""
    @property
    def DeclaredProperties(self) -> _n_1_t_0[PropertyInfo]:"""DeclaredProperties { get; } -> IEnumerable"""
    @property
    def GenericTypeParameters(self) -> _n_0_t_4[_n_0_t_2]:"""GenericTypeParameters { get; } -> Array"""
    @property
    def ImplementedInterfaces(self) -> _n_1_t_0[_n_0_t_2]:"""ImplementedInterfaces { get; } -> IEnumerable"""
    def AsType(self) -> _n_0_t_2:...
    def GetDeclaredEvent(self, name: str) -> EventInfo:...
    def GetDeclaredField(self, name: str) -> FieldInfo:...
    def GetDeclaredMethod(self, name: str) -> MethodInfo:...
    def GetDeclaredMethods(self, name: str) -> _n_1_t_0[MethodInfo]:...
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:...
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:...
    def GetRuntimeInterfaceMap(self, interfaceType: _n_0_t_2) -> InterfaceMapping:
        """Extension from: System.Reflection.RuntimeReflectionExtensions"""
