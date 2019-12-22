import __clrclasses__.System.Runtime.Serialization.Formatters.Binary as Binary
from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import Array as _n_0_t_4
from __clrclasses__.System import Type as _n_0_t_5
from __clrclasses__.System.Reflection import Assembly as _n_1_t_0
from __clrclasses__.System.Reflection import FieldInfo as _n_1_t_1
from __clrclasses__.System.Runtime.Remoting.Messaging import Header as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
import typing
class FormatterAssemblyStyle(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Full: int
    Simple: int
    value__: int
class FormatterTypeStyle(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    TypesAlways: int
    TypesWhenNeeded: int
    value__: int
    XsdString: int
class IFieldInfo():
    @property
    def FieldNames(self) -> _n_0_t_4[str]:"""FieldNames { get; set; } -> Array"""
    @property
    def FieldTypes(self) -> _n_0_t_4[_n_0_t_5]:"""FieldTypes { get; set; } -> Array"""
class InternalRM(object):
    def __init__(self) -> InternalRM:...
    @staticmethod
    def InfoSoap(messages: _n_0_t_4[object]):...
    @staticmethod
    def SoapCheckEnabled() -> bool:...
class InternalST(object):
    @staticmethod
    def InfoSoap(messages: _n_0_t_4[object]):...
    @staticmethod
    def LoadAssemblyFromString(assemblyString: str) -> _n_1_t_0:...
    @staticmethod
    def SerializationSetValue(fi: _n_1_t_1, target: object, value: object):...
    @staticmethod
    def Soap(messages: _n_0_t_4[object]):...
    @staticmethod
    def SoapAssert(condition: bool, message: str):...
    @staticmethod
    def SoapCheckEnabled() -> bool:...
class ISoapMessage():
    @property
    def Headers(self) -> _n_0_t_4[_n_2_t_0]:"""Headers { get; set; } -> Array"""
    @property
    def MethodName(self) -> str:"""MethodName { get; set; } -> str"""
    @property
    def ParamNames(self) -> _n_0_t_4[str]:"""ParamNames { get; set; } -> Array"""
    @property
    def ParamTypes(self) -> _n_0_t_4[_n_0_t_5]:"""ParamTypes { get; set; } -> Array"""
    @property
    def ParamValues(self) -> _n_0_t_4[object]:"""ParamValues { get; set; } -> Array"""
    @property
    def XmlNameSpace(self) -> str:"""XmlNameSpace { get; set; } -> str"""
class ServerFault(object):
    @property
    def ExceptionMessage(self) -> str:"""ExceptionMessage { get; set; } -> str"""
    @property
    def ExceptionType(self) -> str:"""ExceptionType { get; set; } -> str"""
    @property
    def StackTrace(self) -> str:"""StackTrace { get; set; } -> str"""
    def __init__(self, exceptionType: str, message: str, stackTrace: str) -> ServerFault:...
class SoapFault(_n_3_t_0):
    @property
    def Detail(self) -> object:"""Detail { get; set; } -> object"""
    @property
    def FaultActor(self) -> str:"""FaultActor { get; set; } -> str"""
    @property
    def FaultCode(self) -> str:"""FaultCode { get; set; } -> str"""
    @property
    def FaultString(self) -> str:"""FaultString { get; set; } -> str"""
    def __init__(self, faultCode: str, faultString: str, faultActor: str, serverFault: ServerFault) -> SoapFault:...
    def __init__(self) -> SoapFault:...
class SoapMessage(ISoapMessage):
    def __init__(self) -> SoapMessage:...
class TypeFilterLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Full: int
    Low: int
    value__: int
