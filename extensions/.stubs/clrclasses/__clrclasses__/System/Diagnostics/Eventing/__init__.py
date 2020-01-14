import __clrclasses__.System.Diagnostics.Eventing.Reader as Reader
from __clrclasses__.System import ValueType as _n_0_t_0
from __clrclasses__.System import Byte as _n_0_t_1
from __clrclasses__.System import IDisposable as _n_0_t_2
from __clrclasses__.System import Guid as _n_0_t_3
from __clrclasses__.System import Array as _n_0_t_4
from __clrclasses__.System import Enum as _n_0_t_5
from __clrclasses__.System import IComparable as _n_0_t_6
from __clrclasses__.System import IFormattable as _n_0_t_7
from __clrclasses__.System import IConvertible as _n_0_t_8
from __clrclasses__.System.Diagnostics import TraceListener as _n_1_t_0
import typing
class EventDescriptor(_n_0_t_0):
    @property
    def Channel(self) -> _n_0_t_1:"""Channel { get; } -> Byte"""
    @property
    def EventId(self) -> int:"""EventId { get; } -> int"""
    @property
    def Keywords(self) -> int:"""Keywords { get; } -> int"""
    @property
    def Level(self) -> _n_0_t_1:"""Level { get; } -> Byte"""
    @property
    def Opcode(self) -> _n_0_t_1:"""Opcode { get; } -> Byte"""
    @property
    def Task(self) -> int:"""Task { get; } -> int"""
    @property
    def Version(self) -> _n_0_t_1:"""Version { get; } -> Byte"""
    def __init__(self, id: int, version: _n_0_t_1, channel: _n_0_t_1, level: _n_0_t_1, opcode: _n_0_t_1, task: int, keywords: int) -> EventDescriptor:...
class EventProvider(_n_0_t_2):
    def __init__(self, providerGuid: _n_0_t_3) -> EventProvider:...
    def Close(self):...
    @staticmethod
    def CreateActivityId() -> _n_0_t_3:...
    @staticmethod
    def GetLastWriteEventError() -> EventProvider.WriteEventErrorCode:...
    def IsEnabled(self, level: _n_0_t_1, keywords: int) -> bool:...
    def IsEnabled(self) -> bool:...
    @staticmethod
    def SetActivityId(id: _n_0_t_3):...
    def WriteEvent(self, eventDescriptor: EventDescriptor, data: str) -> bool:...
    def WriteEvent(self, eventDescriptor: EventDescriptor, eventPayload: _n_0_t_4[object]) -> bool:...
    def WriteMessageEvent(self, eventMessage: str) -> bool:...
    def WriteMessageEvent(self, eventMessage: str, eventLevel: _n_0_t_1, eventKeywords: int) -> bool:...
    def WriteTransferEvent(self, eventDescriptor: EventDescriptor, relatedActivityId: _n_0_t_3, eventPayload: _n_0_t_4[object]) -> bool:...
    class WriteEventErrorCode(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
        EventTooBig: int
        NoError: int
        NoFreeBuffers: int
        value__: int
class EventProviderTraceListener(_n_1_t_0, _n_0_t_2):
    @property
    def Delimiter(self) -> str:"""Delimiter { get; set; } -> str"""
    def __init__(self, providerId: str, name: str, delimiter: str) -> EventProviderTraceListener:...
    def __init__(self, providerId: str, name: str) -> EventProviderTraceListener:...
    def __init__(self, providerId: str) -> EventProviderTraceListener:...
