from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import Attribute as _n_0_t_4
from __clrclasses__.System import Byte as _n_0_t_5
from __clrclasses__.System import EventArgs as _n_0_t_6
from __clrclasses__.System import IDisposable as _n_0_t_7
from __clrclasses__.System import EventHandler as _n_0_t_8
from __clrclasses__.System import Exception as _n_0_t_9
from __clrclasses__.System import Guid as _n_0_t_10
from __clrclasses__.System import Array as _n_0_t_11
from __clrclasses__.System import Type as _n_0_t_12
from __clrclasses__.System import ValueType as _n_0_t_13
from __clrclasses__.System.Collections.Generic import IDictionary as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_1
from __clrclasses__.System.Collections.ObjectModel import ReadOnlyCollection as _n_2_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_3_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_3_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_4_t_0
import typing
class EventActivityOptions(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Detachable: int
    Disable: int
    _None: int
    Recursive: int
    value__: int
class EventAttribute(_n_0_t_4, _n_3_t_0):
    @property
    def ActivityOptions(self) -> EventActivityOptions:"""ActivityOptions { get; set; } -> EventActivityOptions"""
    @property
    def Channel(self) -> EventChannel:"""Channel { get; set; } -> EventChannel"""
    @property
    def EventId(self) -> int:"""EventId { get; set; } -> int"""
    @property
    def Keywords(self) -> EventKeywords:"""Keywords { get; set; } -> EventKeywords"""
    @property
    def Level(self) -> EventLevel:"""Level { get; set; } -> EventLevel"""
    @property
    def Message(self) -> str:"""Message { get; set; } -> str"""
    @property
    def Opcode(self) -> EventOpcode:"""Opcode { get; set; } -> EventOpcode"""
    @property
    def Tags(self) -> EventTags:"""Tags { get; set; } -> EventTags"""
    @property
    def Task(self) -> EventTask:"""Task { get; set; } -> EventTask"""
    @property
    def Version(self) -> _n_0_t_5:"""Version { get; set; } -> Byte"""
    def __init__(self, eventId: int) -> EventAttribute:...
class EventChannel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Admin: int
    Analytic: int
    Debug: int
    _None: int
    Operational: int
    value__: int
class EventCommand(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Disable: int
    Enable: int
    SendManifest: int
    Update: int
    value__: int
class EventCommandEventArgs(_n_0_t_6):
    @property
    def Arguments(self) -> _n_1_t_0[str, str]:"""Arguments { get; set; } -> IDictionary"""
    @property
    def Command(self) -> EventCommand:"""Command { get; set; } -> EventCommand"""
    def DisableEvent(self, eventId: int) -> bool:...
    def EnableEvent(self, eventId: int) -> bool:...
class EventDataAttribute(_n_0_t_4, _n_3_t_0):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    def __init__(self) -> EventDataAttribute:...
class EventFieldAttribute(_n_0_t_4, _n_3_t_0):
    @property
    def Format(self) -> EventFieldFormat:"""Format { get; set; } -> EventFieldFormat"""
    @property
    def Tags(self) -> EventFieldTags:"""Tags { get; set; } -> EventFieldTags"""
    def __init__(self) -> EventFieldAttribute:...
class EventFieldFormat(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Boolean: int
    Default: int
    Hexadecimal: int
    HResult: int
    Json: int
    String: int
    value__: int
    Xml: int
class EventFieldTags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    value__: int
class EventIgnoreAttribute(_n_0_t_4, _n_3_t_0):
    def __init__(self) -> EventIgnoreAttribute:...
class EventKeywords(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    All: int
    AuditFailure: int
    AuditSuccess: int
    CorrelationHint: int
    EventLogClassic: int
    MicrosoftTelemetry: int
    _None: int
    Sqm: int
    value__: int
    WdiContext: int
    WdiDiagnostic: int
class EventLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Critical: int
    Error: int
    Informational: int
    LogAlways: int
    value__: int
    Verbose: int
    Warning: int
class EventListener(_n_0_t_7):
    @property
    def EventSourceCreated(self) -> _n_0_t_8[EventSourceCreatedEventArgs]:
        """EventSourceCreated Event: EventHandler"""
    @property
    def EventWritten(self) -> _n_0_t_8[EventWrittenEventArgs]:
        """EventWritten Event: EventHandler"""
    def __init__(self) -> EventListener:...
    def DisableEvents(self, eventSource: EventSource):...
    def EnableEvents(self, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords, arguments: _n_1_t_0[str, str]):...
    def EnableEvents(self, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords):...
    def EnableEvents(self, eventSource: EventSource, level: EventLevel):...
    @staticmethod
    def EventSourceIndex(eventSource: EventSource) -> int:...
class EventManifestOptions(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AllCultures: int
    AllowEventSourceOverride: int
    _None: int
    OnlyIfNeededForRegistration: int
    Strict: int
    value__: int
class EventOpcode(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DataCollectionStart: int
    DataCollectionStop: int
    Extension: int
    Info: int
    Receive: int
    Reply: int
    Resume: int
    Send: int
    Start: int
    Stop: int
    Suspend: int
    value__: int
class EventSource(_n_0_t_7):
    @property
    def ConstructionException(self) -> _n_0_t_9:"""ConstructionException { get; } -> Exception"""
    @property
    def CurrentThreadActivityId(self) -> _n_0_t_10:"""CurrentThreadActivityId { get; } -> Guid"""
    @property
    def Guid(self) -> _n_0_t_10:"""Guid { get; } -> Guid"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Settings(self) -> EventSourceSettings:"""Settings { get; } -> EventSourceSettings"""
    @property
    def EventCommandExecuted(self) -> _n_0_t_8[EventCommandEventArgs]:
        """EventCommandExecuted Event: EventHandler"""
    def __init__(self, eventSourceName: str, config: EventSourceSettings, traits: _n_0_t_11[str]) -> EventSource:...
    def __init__(self, eventSourceName: str, config: EventSourceSettings) -> EventSource:...
    def __init__(self, eventSourceName: str) -> EventSource:...
    @staticmethod
    def GenerateManifest(eventSourceType: _n_0_t_12, assemblyPathToIncludeInManifest: str, flags: EventManifestOptions) -> str:...
    @staticmethod
    def GenerateManifest(eventSourceType: _n_0_t_12, assemblyPathToIncludeInManifest: str) -> str:...
    @staticmethod
    def GetGuid(eventSourceType: _n_0_t_12) -> _n_0_t_10:...
    @staticmethod
    def GetName(eventSourceType: _n_0_t_12) -> str:...
    @staticmethod
    def GetSources() -> _n_1_t_1[EventSource]:...
    def GetTrait(self, key: str) -> str:...
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:...
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:...
    def IsEnabled(self) -> bool:...
    @staticmethod
    def SendCommand(eventSource: EventSource, command: EventCommand, commandArguments: _n_1_t_0[str, str]):...
    @staticmethod
    def SetCurrentThreadActivityId(activityId: _n_0_t_10, oldActivityThatWillContinue: _n_0_t_10):...
    @staticmethod
    def SetCurrentThreadActivityId(activityId: _n_0_t_10):...
    def Write(self, eventName: str, options: EventSourceOptions, activityId: _n_0_t_10, relatedActivityId: _n_0_t_10, data: object):...
    def Write(self, eventName: str, options: EventSourceOptions, data: object):...
    def Write(self, eventName: str, options: EventSourceOptions, data: typing.Any):...
    def Write(self, eventName: str, data: typing.Any):...
    def Write(self, eventName: str, options: EventSourceOptions):...
    def Write(self, eventName: str):...
class EventSourceAttribute(_n_0_t_4, _n_3_t_0):
    @property
    def Guid(self) -> str:"""Guid { get; set; } -> str"""
    @property
    def LocalizationResources(self) -> str:"""LocalizationResources { get; set; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    def __init__(self) -> EventSourceAttribute:...
class EventSourceCreatedEventArgs(_n_0_t_6):
    @property
    def EventSource(self) -> EventSource:"""EventSource { get; set; } -> EventSource"""
    def __init__(self) -> EventSourceCreatedEventArgs:...
class EventSourceException(_n_0_t_9, _n_4_t_0, _n_3_t_1):
    def __init__(self, message: str, innerException: _n_0_t_9) -> EventSourceException:...
    def __init__(self, message: str) -> EventSourceException:...
    def __init__(self) -> EventSourceException:...
class EventSourceOptions(_n_0_t_13):
    @property
    def ActivityOptions(self) -> EventActivityOptions:"""ActivityOptions { get; set; } -> EventActivityOptions"""
    @property
    def Keywords(self) -> EventKeywords:"""Keywords { get; set; } -> EventKeywords"""
    @property
    def Level(self) -> EventLevel:"""Level { get; set; } -> EventLevel"""
    @property
    def Opcode(self) -> EventOpcode:"""Opcode { get; set; } -> EventOpcode"""
    @property
    def Tags(self) -> EventTags:"""Tags { get; set; } -> EventTags"""
class EventSourceSettings(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Default: int
    EtwManifestEventFormat: int
    EtwSelfDescribingEventFormat: int
    ThrowOnEventWriteErrors: int
    value__: int
class EventTags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    value__: int
class EventTask(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    value__: int
class EventWrittenEventArgs(_n_0_t_6):
    @property
    def ActivityId(self) -> _n_0_t_10:"""ActivityId { get; } -> Guid"""
    @property
    def Channel(self) -> EventChannel:"""Channel { get; } -> EventChannel"""
    @property
    def EventId(self) -> int:"""EventId { get; set; } -> int"""
    @property
    def EventName(self) -> str:"""EventName { get; set; } -> str"""
    @property
    def EventSource(self) -> EventSource:"""EventSource { get; } -> EventSource"""
    @property
    def Keywords(self) -> EventKeywords:"""Keywords { get; } -> EventKeywords"""
    @property
    def Level(self) -> EventLevel:"""Level { get; } -> EventLevel"""
    @property
    def Message(self) -> str:"""Message { get; set; } -> str"""
    @property
    def Opcode(self) -> EventOpcode:"""Opcode { get; } -> EventOpcode"""
    @property
    def Payload(self) -> _n_2_t_0[object]:"""Payload { get; set; } -> ReadOnlyCollection"""
    @property
    def PayloadNames(self) -> _n_2_t_0[str]:"""PayloadNames { get; set; } -> ReadOnlyCollection"""
    @property
    def RelatedActivityId(self) -> _n_0_t_10:"""RelatedActivityId { get; set; } -> Guid"""
    @property
    def Tags(self) -> EventTags:"""Tags { get; } -> EventTags"""
    @property
    def Task(self) -> EventTask:"""Task { get; } -> EventTask"""
    @property
    def Version(self) -> _n_0_t_5:"""Version { get; } -> Byte"""
class NonEventAttribute(_n_0_t_4, _n_3_t_0):
    def __init__(self) -> NonEventAttribute:...
