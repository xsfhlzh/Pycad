from __clrclasses__.System import Exception as _n_0_t_0
from __clrclasses__.System import EventArgs as _n_0_t_1
from __clrclasses__.System import Attribute as _n_0_t_2
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
import typing
class ExceptionDispatchInfo(object):
    @property
    def SourceException(self) -> _n_0_t_0:"""SourceException { get; } -> Exception"""
    @staticmethod
    def Capture(source: _n_0_t_0) -> ExceptionDispatchInfo:...
    def Throw(self):...
class FirstChanceExceptionEventArgs(_n_0_t_1):
    @property
    def Exception(self) -> _n_0_t_0:"""Exception { get; } -> Exception"""
    def __init__(self, exception: _n_0_t_0) -> FirstChanceExceptionEventArgs:...
class HandleProcessCorruptedStateExceptionsAttribute(_n_0_t_2, _n_1_t_0):
    def __init__(self) -> HandleProcessCorruptedStateExceptionsAttribute:...
