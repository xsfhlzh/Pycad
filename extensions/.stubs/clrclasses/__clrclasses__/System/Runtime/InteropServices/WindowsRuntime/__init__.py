from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Type as _n_0_t_1
from __clrclasses__.System import EventArgs as _n_0_t_2
from __clrclasses__.System import ValueType as _n_0_t_3
from __clrclasses__.System import Byte as _n_0_t_4
from __clrclasses__.System import Func as _n_0_t_5
from __clrclasses__.System import Action as _n_0_t_6
from __clrclasses__.System import IntPtr as _n_0_t_7
from __clrclasses__.System import EventHandler as _n_0_t_8
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_2_t_0
from __clrclasses__.System.Reflection import Assembly as _n_3_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_4_t_0
import typing
T = typing.TypeVar('T')
class DefaultInterfaceAttribute(_n_0_t_0, _n_4_t_0):
    @property
    def DefaultInterface(self) -> _n_0_t_1:"""DefaultInterface { get; } -> Type"""
    def __init__(self, defaultInterface: _n_0_t_1) -> DefaultInterfaceAttribute:...
class DesignerNamespaceResolveEventArgs(_n_0_t_2):
    @property
    def NamespaceName(self) -> str:"""NamespaceName { get; } -> str"""
    @property
    def ResolvedAssemblyFiles(self) -> _n_2_t_0[str]:"""ResolvedAssemblyFiles { get; } -> Collection"""
    def __init__(self, namespaceName: str) -> DesignerNamespaceResolveEventArgs:...
class EventRegistrationToken(_n_0_t_3):
    pass
class EventRegistrationTokenTable(typing.Generic[T]):
    @property
    def InvocationList(self) -> T:"""InvocationList { get; set; } -> T"""
    def __init__(self) -> EventRegistrationTokenTable:...
    def AddEventHandler(self, handler: T) -> EventRegistrationToken:...
    @staticmethod
    def GetOrCreateEventRegistrationTokenTable(refEventTable: EventRegistrationTokenTable[T]) -> EventRegistrationTokenTable[T]:...
    def RemoveEventHandler(self, handler: T):...
    def RemoveEventHandler(self, token: EventRegistrationToken):...
class IActivationFactory():
    def ActivateInstance(self) -> object:...
class InterfaceImplementedInVersionAttribute(_n_0_t_0, _n_4_t_0):
    @property
    def BuildVersion(self) -> _n_0_t_4:"""BuildVersion { get; } -> Byte"""
    @property
    def InterfaceType(self) -> _n_0_t_1:"""InterfaceType { get; } -> Type"""
    @property
    def MajorVersion(self) -> _n_0_t_4:"""MajorVersion { get; } -> Byte"""
    @property
    def MinorVersion(self) -> _n_0_t_4:"""MinorVersion { get; } -> Byte"""
    @property
    def RevisionVersion(self) -> _n_0_t_4:"""RevisionVersion { get; } -> Byte"""
    def __init__(self, interfaceType: _n_0_t_1, majorVersion: _n_0_t_4, minorVersion: _n_0_t_4, buildVersion: _n_0_t_4, revisionVersion: _n_0_t_4) -> InterfaceImplementedInVersionAttribute:...
class NamespaceResolveEventArgs(_n_0_t_2):
    @property
    def NamespaceName(self) -> str:"""NamespaceName { get; } -> str"""
    @property
    def RequestingAssembly(self) -> _n_3_t_0:"""RequestingAssembly { get; } -> Assembly"""
    @property
    def ResolvedAssemblies(self) -> _n_2_t_0[_n_3_t_0]:"""ResolvedAssemblies { get; } -> Collection"""
    def __init__(self, namespaceName: str, requestingAssembly: _n_3_t_0) -> NamespaceResolveEventArgs:...
class ReadOnlyArrayAttribute(_n_0_t_0, _n_4_t_0):
    def __init__(self) -> ReadOnlyArrayAttribute:...
class ReturnValueNameAttribute(_n_0_t_0, _n_4_t_0):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, name: str) -> ReturnValueNameAttribute:...
class WindowsRuntimeMarshal(object):
    @staticmethod
    def AddEventHandler(addMethod: _n_0_t_5[typing.Any, EventRegistrationToken], removeMethod: _n_0_t_6[EventRegistrationToken], handler: typing.Any):...
    @staticmethod
    def FreeHString(ptr: _n_0_t_7):...
    @staticmethod
    def GetActivationFactory(type: _n_0_t_1) -> IActivationFactory:...
    @staticmethod
    def PtrToStringHString(ptr: _n_0_t_7) -> str:...
    @staticmethod
    def RemoveAllEventHandlers(removeMethod: _n_0_t_6[EventRegistrationToken]):...
    @staticmethod
    def RemoveEventHandler(removeMethod: _n_0_t_6[EventRegistrationToken], handler: typing.Any):...
    @staticmethod
    def StringToHString(s: str) -> _n_0_t_7:...
class WindowsRuntimeMetadata(object):
    @property
    def DesignerNamespaceResolve(self) -> _n_0_t_8[DesignerNamespaceResolveEventArgs]:
        """DesignerNamespaceResolve Event: EventHandler"""
    @property
    def ReflectionOnlyNamespaceResolve(self) -> _n_0_t_8[NamespaceResolveEventArgs]:
        """ReflectionOnlyNamespaceResolve Event: EventHandler"""
    @staticmethod
    def ResolveNamespace(namespaceName: str, windowsSdkFilePath: str, packageGraphFilePaths: _n_1_t_0[str]) -> _n_1_t_0[str]:...
    @staticmethod
    def ResolveNamespace(namespaceName: str, packageGraphFilePaths: _n_1_t_0[str]) -> _n_1_t_0[str]:...
class WriteOnlyArrayAttribute(_n_0_t_0, _n_4_t_0):
    def __init__(self) -> WriteOnlyArrayAttribute:...
