from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
import typing
class ExcludeFromCodeCoverageAttribute(_n_0_t_0, _n_1_t_0):
    def __init__(self) -> ExcludeFromCodeCoverageAttribute:...
class SuppressMessageAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def Category(self) -> str:"""Category { get; } -> str"""
    @property
    def CheckId(self) -> str:"""CheckId { get; } -> str"""
    @property
    def Justification(self) -> str:"""Justification { get; set; } -> str"""
    @property
    def MessageId(self) -> str:"""MessageId { get; set; } -> str"""
    @property
    def Scope(self) -> str:"""Scope { get; set; } -> str"""
    @property
    def Target(self) -> str:"""Target { get; set; } -> str"""
    def __init__(self, category: str, checkId: str) -> SuppressMessageAttribute:...
