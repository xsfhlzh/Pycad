import __clrclasses__.System.Runtime.Remoting.Metadata.W3cXsd2001 as W3cXsd2001
from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Enum as _n_0_t_1
from __clrclasses__.System import IComparable as _n_0_t_2
from __clrclasses__.System import IFormattable as _n_0_t_3
from __clrclasses__.System import IConvertible as _n_0_t_4
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
import typing
class SoapAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def Embedded(self) -> bool:"""Embedded { get; set; } -> bool"""
    @property
    def UseAttribute(self) -> bool:"""UseAttribute { get; set; } -> bool"""
    @property
    def XmlNamespace(self) -> str:"""XmlNamespace { get; set; } -> str"""
    def __init__(self) -> SoapAttribute:...
class SoapFieldAttribute(SoapAttribute, _n_1_t_0):
    @property
    def Order(self) -> int:"""Order { get; set; } -> int"""
    @property
    def XmlElementName(self) -> str:"""XmlElementName { get; set; } -> str"""
    def __init__(self) -> SoapFieldAttribute:...
    def IsInteropXmlElement(self) -> bool:...
class SoapMethodAttribute(SoapAttribute, _n_1_t_0):
    @property
    def ResponseXmlElementName(self) -> str:"""ResponseXmlElementName { get; set; } -> str"""
    @property
    def ResponseXmlNamespace(self) -> str:"""ResponseXmlNamespace { get; set; } -> str"""
    @property
    def ReturnXmlElementName(self) -> str:"""ReturnXmlElementName { get; set; } -> str"""
    @property
    def SoapAction(self) -> str:"""SoapAction { get; set; } -> str"""
    def __init__(self) -> SoapMethodAttribute:...
class SoapOption(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    AlwaysIncludeTypes: int
    EmbedAll: int
    _None: int
    Option1: int
    Option2: int
    value__: int
    XsdString: int
class SoapParameterAttribute(SoapAttribute, _n_1_t_0):
    def __init__(self) -> SoapParameterAttribute:...
class SoapTypeAttribute(SoapAttribute, _n_1_t_0):
    @property
    def SoapOptions(self) -> SoapOption:"""SoapOptions { get; set; } -> SoapOption"""
    @property
    def XmlElementName(self) -> str:"""XmlElementName { get; set; } -> str"""
    @property
    def XmlFieldOrder(self) -> XmlFieldOrderOption:"""XmlFieldOrder { get; set; } -> XmlFieldOrderOption"""
    @property
    def XmlTypeName(self) -> str:"""XmlTypeName { get; set; } -> str"""
    @property
    def XmlTypeNamespace(self) -> str:"""XmlTypeNamespace { get; set; } -> str"""
    def __init__(self) -> SoapTypeAttribute:...
class XmlFieldOrderOption(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    All: int
    Choice: int
    Sequence: int
    value__: int
