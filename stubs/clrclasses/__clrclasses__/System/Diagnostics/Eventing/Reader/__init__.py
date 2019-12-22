from __clrclasses__.System import IDisposable as _n_0_t_0
from __clrclasses__.System import Nullable as _n_0_t_1
from __clrclasses__.System import Guid as _n_0_t_2
from __clrclasses__.System import Exception as _n_0_t_3
from __clrclasses__.System import DateTime as _n_0_t_4
from __clrclasses__.System import Enum as _n_0_t_5
from __clrclasses__.System import IComparable as _n_0_t_6
from __clrclasses__.System import IFormattable as _n_0_t_7
from __clrclasses__.System import IConvertible as _n_0_t_8
from __clrclasses__.System import TimeSpan as _n_0_t_9
from __clrclasses__.System import EventHandler as _n_0_t_10
from __clrclasses__.System import Byte as _n_0_t_11
from __clrclasses__.System import EventArgs as _n_0_t_12
from __clrclasses__.System import Uri as _n_0_t_13
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IList as _n_1_t_1
from __clrclasses__.System.Globalization import CultureInfo as _n_2_t_0
from __clrclasses__.System.IO import SeekOrigin as _n_3_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
from __clrclasses__.System.Security import SecureString as _n_6_t_0
from __clrclasses__.System.Security.Principal import SecurityIdentifier as _n_7_t_0
import typing
class EventBookmark(_n_5_t_0):
    pass
class EventKeyword(object):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> int:"""Value { get; } -> int"""
class EventLevel(object):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> int:"""Value { get; } -> int"""
class EventLogConfiguration(_n_0_t_0):
    @property
    def IsClassicLog(self) -> bool:"""IsClassicLog { get; } -> bool"""
    @property
    def IsEnabled(self) -> bool:"""IsEnabled { get; set; } -> bool"""
    @property
    def LogFilePath(self) -> str:"""LogFilePath { get; set; } -> str"""
    @property
    def LogIsolation(self) -> EventLogIsolation:"""LogIsolation { get; } -> EventLogIsolation"""
    @property
    def LogMode(self) -> EventLogMode:"""LogMode { get; set; } -> EventLogMode"""
    @property
    def LogName(self) -> str:"""LogName { get; } -> str"""
    @property
    def LogType(self) -> EventLogType:"""LogType { get; } -> EventLogType"""
    @property
    def MaximumSizeInBytes(self) -> int:"""MaximumSizeInBytes { get; set; } -> int"""
    @property
    def OwningProviderName(self) -> str:"""OwningProviderName { get; } -> str"""
    @property
    def ProviderBufferSize(self) -> _n_0_t_1[int]:"""ProviderBufferSize { get; } -> Nullable"""
    @property
    def ProviderControlGuid(self) -> _n_0_t_1[_n_0_t_2]:"""ProviderControlGuid { get; } -> Nullable"""
    @property
    def ProviderKeywords(self) -> _n_0_t_1[int]:"""ProviderKeywords { get; set; } -> Nullable"""
    @property
    def ProviderLatency(self) -> _n_0_t_1[int]:"""ProviderLatency { get; } -> Nullable"""
    @property
    def ProviderLevel(self) -> _n_0_t_1[int]:"""ProviderLevel { get; set; } -> Nullable"""
    @property
    def ProviderMaximumNumberOfBuffers(self) -> _n_0_t_1[int]:"""ProviderMaximumNumberOfBuffers { get; } -> Nullable"""
    @property
    def ProviderMinimumNumberOfBuffers(self) -> _n_0_t_1[int]:"""ProviderMinimumNumberOfBuffers { get; } -> Nullable"""
    @property
    def ProviderNames(self) -> _n_1_t_0[str]:"""ProviderNames { get; } -> IEnumerable"""
    @property
    def SecurityDescriptor(self) -> str:"""SecurityDescriptor { get; set; } -> str"""
    def __init__(self, logName: str, session: EventLogSession) -> EventLogConfiguration:...
    def __init__(self, logName: str) -> EventLogConfiguration:...
    def SaveChanges(self):...
class EventLogException(_n_0_t_3, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_3) -> EventLogException:...
    def __init__(self, message: str) -> EventLogException:...
    def __init__(self) -> EventLogException:...
class EventLogInformation(object):
    @property
    def Attributes(self) -> _n_0_t_1[int]:"""Attributes { get; } -> Nullable"""
    @property
    def CreationTime(self) -> _n_0_t_1[_n_0_t_4]:"""CreationTime { get; } -> Nullable"""
    @property
    def FileSize(self) -> _n_0_t_1[int]:"""FileSize { get; } -> Nullable"""
    @property
    def IsLogFull(self) -> _n_0_t_1[bool]:"""IsLogFull { get; } -> Nullable"""
    @property
    def LastAccessTime(self) -> _n_0_t_1[_n_0_t_4]:"""LastAccessTime { get; } -> Nullable"""
    @property
    def LastWriteTime(self) -> _n_0_t_1[_n_0_t_4]:"""LastWriteTime { get; } -> Nullable"""
    @property
    def OldestRecordNumber(self) -> _n_0_t_1[int]:"""OldestRecordNumber { get; } -> Nullable"""
    @property
    def RecordCount(self) -> _n_0_t_1[int]:"""RecordCount { get; } -> Nullable"""
class EventLogInvalidDataException(EventLogException, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_3) -> EventLogInvalidDataException:...
    def __init__(self, message: str) -> EventLogInvalidDataException:...
    def __init__(self) -> EventLogInvalidDataException:...
class EventLogIsolation(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    Application: int
    Custom: int
    System: int
    value__: int
class EventLogLink(object):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def IsImported(self) -> bool:"""IsImported { get; } -> bool"""
    @property
    def LogName(self) -> str:"""LogName { get; } -> str"""
class EventLogMode(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    AutoBackup: int
    Circular: int
    Retain: int
    value__: int
class EventLogNotFoundException(EventLogException, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_3) -> EventLogNotFoundException:...
    def __init__(self, message: str) -> EventLogNotFoundException:...
    def __init__(self) -> EventLogNotFoundException:...
class EventLogPropertySelector(_n_0_t_0):
    def __init__(self, propertyQueries: _n_1_t_0[str]) -> EventLogPropertySelector:...
class EventLogProviderDisabledException(EventLogException, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_3) -> EventLogProviderDisabledException:...
    def __init__(self, message: str) -> EventLogProviderDisabledException:...
    def __init__(self) -> EventLogProviderDisabledException:...
class EventLogQuery(object):
    @property
    def ReverseDirection(self) -> bool:"""ReverseDirection { get; set; } -> bool"""
    @property
    def Session(self) -> EventLogSession:"""Session { get; set; } -> EventLogSession"""
    @property
    def TolerateQueryErrors(self) -> bool:"""TolerateQueryErrors { get; set; } -> bool"""
    def __init__(self, path: str, pathType: PathType, query: str) -> EventLogQuery:...
    def __init__(self, path: str, pathType: PathType) -> EventLogQuery:...
class EventLogReader(_n_0_t_0):
    @property
    def BatchSize(self) -> int:"""BatchSize { get; set; } -> int"""
    @property
    def LogStatus(self) -> _n_1_t_1[EventLogStatus]:"""LogStatus { get; } -> IList"""
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark) -> EventLogReader:...
    def __init__(self, eventQuery: EventLogQuery) -> EventLogReader:...
    def __init__(self, path: str, pathType: PathType) -> EventLogReader:...
    def __init__(self, path: str) -> EventLogReader:...
    def CancelReading(self):...
    def ReadEvent(self, timeout: _n_0_t_9) -> EventRecord:...
    def ReadEvent(self) -> EventRecord:...
    def Seek(self, origin: _n_3_t_0, offset: int):...
    def Seek(self, bookmark: EventBookmark, offset: int):...
    def Seek(self, bookmark: EventBookmark):...
class EventLogReadingException(EventLogException, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_3) -> EventLogReadingException:...
    def __init__(self, message: str) -> EventLogReadingException:...
    def __init__(self) -> EventLogReadingException:...
class EventLogRecord(EventRecord, _n_0_t_0):
    @property
    def ContainerLog(self) -> str:"""ContainerLog { get; } -> str"""
    @property
    def MatchedQueryIds(self) -> _n_1_t_0[int]:"""MatchedQueryIds { get; } -> IEnumerable"""
    def GetPropertyValues(self, propertySelector: EventLogPropertySelector) -> _n_1_t_1[object]:...
class EventLogSession(_n_0_t_0):
    @property
    def GlobalSession(self) -> EventLogSession:"""GlobalSession { get; } -> EventLogSession"""
    def __init__(self, server: str, domain: str, user: str, password: _n_6_t_0, logOnType: SessionAuthentication) -> EventLogSession:...
    def __init__(self, server: str) -> EventLogSession:...
    def __init__(self) -> EventLogSession:...
    def CancelCurrentOperations(self):...
    def ClearLog(self, logName: str, backupPath: str):...
    def ClearLog(self, logName: str):...
    def ExportLog(self, path: str, pathType: PathType, query: str, targetFilePath: str, tolerateQueryErrors: bool):...
    def ExportLog(self, path: str, pathType: PathType, query: str, targetFilePath: str):...
    def ExportLogAndMessages(self, path: str, pathType: PathType, query: str, targetFilePath: str, tolerateQueryErrors: bool, targetCultureInfo: _n_2_t_0):...
    def ExportLogAndMessages(self, path: str, pathType: PathType, query: str, targetFilePath: str):...
    def GetLogInformation(self, logName: str, pathType: PathType) -> EventLogInformation:...
    def GetLogNames(self) -> _n_1_t_0[str]:...
    def GetProviderNames(self) -> _n_1_t_0[str]:...
class EventLogStatus(object):
    @property
    def LogName(self) -> str:"""LogName { get; } -> str"""
    @property
    def StatusCode(self) -> int:"""StatusCode { get; } -> int"""
class EventLogType(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    Administrative: int
    Analytical: int
    Debug: int
    Operational: int
    value__: int
class EventLogWatcher(_n_0_t_0):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def EventRecordWritten(self) -> _n_0_t_10[EventRecordWrittenEventArgs]:
        """EventRecordWritten Event: EventHandler"""
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark, readExistingEvents: bool) -> EventLogWatcher:...
    def __init__(self, eventQuery: EventLogQuery, bookmark: EventBookmark) -> EventLogWatcher:...
    def __init__(self, eventQuery: EventLogQuery) -> EventLogWatcher:...
    def __init__(self, path: str) -> EventLogWatcher:...
class EventMetadata(object):
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def Id(self) -> int:"""Id { get; } -> int"""
    @property
    def Keywords(self) -> _n_1_t_0[EventKeyword]:"""Keywords { get; } -> IEnumerable"""
    @property
    def Level(self) -> EventLevel:"""Level { get; } -> EventLevel"""
    @property
    def LogLink(self) -> EventLogLink:"""LogLink { get; } -> EventLogLink"""
    @property
    def Opcode(self) -> EventOpcode:"""Opcode { get; } -> EventOpcode"""
    @property
    def Task(self) -> EventTask:"""Task { get; } -> EventTask"""
    @property
    def Template(self) -> str:"""Template { get; } -> str"""
    @property
    def Version(self) -> _n_0_t_11:"""Version { get; } -> Byte"""
class EventOpcode(object):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> int:"""Value { get; } -> int"""
class EventProperty(object):
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
class EventRecord(_n_0_t_0):
    @property
    def ActivityId(self) -> _n_0_t_1[_n_0_t_2]:"""ActivityId { get; } -> Nullable"""
    @property
    def Bookmark(self) -> EventBookmark:"""Bookmark { get; } -> EventBookmark"""
    @property
    def Id(self) -> int:"""Id { get; } -> int"""
    @property
    def Keywords(self) -> _n_0_t_1[int]:"""Keywords { get; } -> Nullable"""
    @property
    def KeywordsDisplayNames(self) -> _n_1_t_0[str]:"""KeywordsDisplayNames { get; } -> IEnumerable"""
    @property
    def Level(self) -> _n_0_t_1[_n_0_t_11]:"""Level { get; } -> Nullable"""
    @property
    def LevelDisplayName(self) -> str:"""LevelDisplayName { get; } -> str"""
    @property
    def LogName(self) -> str:"""LogName { get; } -> str"""
    @property
    def MachineName(self) -> str:"""MachineName { get; } -> str"""
    @property
    def Opcode(self) -> _n_0_t_1[int]:"""Opcode { get; } -> Nullable"""
    @property
    def OpcodeDisplayName(self) -> str:"""OpcodeDisplayName { get; } -> str"""
    @property
    def ProcessId(self) -> _n_0_t_1[int]:"""ProcessId { get; } -> Nullable"""
    @property
    def Properties(self) -> _n_1_t_1[EventProperty]:"""Properties { get; } -> IList"""
    @property
    def ProviderId(self) -> _n_0_t_1[_n_0_t_2]:"""ProviderId { get; } -> Nullable"""
    @property
    def ProviderName(self) -> str:"""ProviderName { get; } -> str"""
    @property
    def Qualifiers(self) -> _n_0_t_1[int]:"""Qualifiers { get; } -> Nullable"""
    @property
    def RecordId(self) -> _n_0_t_1[int]:"""RecordId { get; } -> Nullable"""
    @property
    def RelatedActivityId(self) -> _n_0_t_1[_n_0_t_2]:"""RelatedActivityId { get; } -> Nullable"""
    @property
    def Task(self) -> _n_0_t_1[int]:"""Task { get; } -> Nullable"""
    @property
    def TaskDisplayName(self) -> str:"""TaskDisplayName { get; } -> str"""
    @property
    def ThreadId(self) -> _n_0_t_1[int]:"""ThreadId { get; } -> Nullable"""
    @property
    def TimeCreated(self) -> _n_0_t_1[_n_0_t_4]:"""TimeCreated { get; } -> Nullable"""
    @property
    def UserId(self) -> _n_7_t_0:"""UserId { get; } -> SecurityIdentifier"""
    @property
    def Version(self) -> _n_0_t_1[_n_0_t_11]:"""Version { get; } -> Nullable"""
    def FormatDescription(self, values: _n_1_t_0[object]) -> str:...
    def FormatDescription(self) -> str:...
    def ToXml(self) -> str:...
class EventRecordWrittenEventArgs(_n_0_t_12):
    @property
    def EventException(self) -> _n_0_t_3:"""EventException { get; } -> Exception"""
    @property
    def EventRecord(self) -> EventRecord:"""EventRecord { get; } -> EventRecord"""
class EventTask(object):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def EventGuid(self) -> _n_0_t_2:"""EventGuid { get; } -> Guid"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> int:"""Value { get; } -> int"""
class PathType(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    FilePath: int
    LogName: int
    value__: int
class ProviderMetadata(_n_0_t_0):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
    @property
    def Events(self) -> _n_1_t_0[EventMetadata]:"""Events { get; } -> IEnumerable"""
    @property
    def HelpLink(self) -> _n_0_t_13:"""HelpLink { get; } -> Uri"""
    @property
    def Id(self) -> _n_0_t_2:"""Id { get; } -> Guid"""
    @property
    def Keywords(self) -> _n_1_t_1[EventKeyword]:"""Keywords { get; } -> IList"""
    @property
    def Levels(self) -> _n_1_t_1[EventLevel]:"""Levels { get; } -> IList"""
    @property
    def LogLinks(self) -> _n_1_t_1[EventLogLink]:"""LogLinks { get; } -> IList"""
    @property
    def MessageFilePath(self) -> str:"""MessageFilePath { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Opcodes(self) -> _n_1_t_1[EventOpcode]:"""Opcodes { get; } -> IList"""
    @property
    def ParameterFilePath(self) -> str:"""ParameterFilePath { get; } -> str"""
    @property
    def ResourceFilePath(self) -> str:"""ResourceFilePath { get; } -> str"""
    @property
    def Tasks(self) -> _n_1_t_1[EventTask]:"""Tasks { get; } -> IList"""
    def __init__(self, providerName: str, session: EventLogSession, targetCultureInfo: _n_2_t_0) -> ProviderMetadata:...
    def __init__(self, providerName: str) -> ProviderMetadata:...
class SessionAuthentication(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    Default: int
    Kerberos: int
    Negotiate: int
    Ntlm: int
    value__: int
class StandardEventKeywords(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    AuditFailure: int
    AuditSuccess: int
    CorrelationHint: int
    CorrelationHint2: int
    EventLogClassic: int
    _None: int
    ResponseTime: int
    Sqm: int
    value__: int
    WdiContext: int
    WdiDiagnostic: int
class StandardEventLevel(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    Critical: int
    Error: int
    Informational: int
    LogAlways: int
    value__: int
    Verbose: int
    Warning: int
class StandardEventOpcode(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
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
class StandardEventTask(_n_0_t_5, _n_0_t_6, _n_0_t_7, _n_0_t_8):
    _None: int
    value__: int
