from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Type as _n_0_t_1
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
import typing
class ValueSerializerAttribute(_n_0_t_0, _n_1_t_0):
    @property
    def ValueSerializerType(self) -> _n_0_t_1:"""ValueSerializerType { get; } -> Type"""
    @property
    def ValueSerializerTypeName(self) -> str:"""ValueSerializerTypeName { get; } -> str"""
    def __init__(self, valueSerializerTypeName: str) -> ValueSerializerAttribute:...
    def __init__(self, valueSerializerType: _n_0_t_1) -> ValueSerializerAttribute:...
