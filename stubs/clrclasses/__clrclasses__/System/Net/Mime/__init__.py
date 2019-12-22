from __clrclasses__.System import DateTime as _n_0_t_0
from __clrclasses__.System import Enum as _n_0_t_1
from __clrclasses__.System import IComparable as _n_0_t_2
from __clrclasses__.System import IFormattable as _n_0_t_3
from __clrclasses__.System import IConvertible as _n_0_t_4
from __clrclasses__.System.Collections.Specialized import StringDictionary as _n_1_t_0
import typing
class ContentDisposition(object):
    @property
    def CreationDate(self) -> _n_0_t_0:"""CreationDate { get; set; } -> DateTime"""
    @property
    def DispositionType(self) -> str:"""DispositionType { get; set; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; set; } -> str"""
    @property
    def Inline(self) -> bool:"""Inline { get; set; } -> bool"""
    @property
    def ModificationDate(self) -> _n_0_t_0:"""ModificationDate { get; set; } -> DateTime"""
    @property
    def Parameters(self) -> _n_1_t_0:"""Parameters { get; } -> StringDictionary"""
    @property
    def ReadDate(self) -> _n_0_t_0:"""ReadDate { get; set; } -> DateTime"""
    @property
    def Size(self) -> int:"""Size { get; set; } -> int"""
    def __init__(self, disposition: str) -> ContentDisposition:...
    def __init__(self) -> ContentDisposition:...
class ContentType(object):
    @property
    def Boundary(self) -> str:"""Boundary { get; set; } -> str"""
    @property
    def CharSet(self) -> str:"""CharSet { get; set; } -> str"""
    @property
    def MediaType(self) -> str:"""MediaType { get; set; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Parameters(self) -> _n_1_t_0:"""Parameters { get; } -> StringDictionary"""
    def __init__(self, contentType: str) -> ContentType:...
    def __init__(self) -> ContentType:...
class DispositionTypeNames(object):
    Attachment: int
    Inline: int
class MediaTypeNames(object):
    pass
class TransferEncoding(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    Base64: int
    EightBit: int
    QuotedPrintable: int
    SevenBit: int
    Unknown: int
    value__: int
