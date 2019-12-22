import __clrclasses__.System.Diagnostics.SymbolStore as SymbolStore
import __clrclasses__.System.Diagnostics.Contracts as Contracts
import __clrclasses__.System.Diagnostics.Tracing as Tracing
import __clrclasses__.System.Diagnostics.PerformanceData as PerformanceData
import __clrclasses__.System.Diagnostics.Eventing as Eventing
import __clrclasses__.System.Diagnostics.CodeAnalysis as CodeAnalysis
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeProcessHandle as _n_0_t_0
from __clrclasses__.System import Attribute as _n_1_t_0
from __clrclasses__.System import IDisposable as _n_1_t_1
from __clrclasses__.System import Guid as _n_1_t_2
from __clrclasses__.System import Array as _n_1_t_3
from __clrclasses__.System import ValueType as _n_1_t_4
from __clrclasses__.System import EventArgs as _n_1_t_5
from __clrclasses__.System import MulticastDelegate as _n_1_t_6
from __clrclasses__.System import ICloneable as _n_1_t_7
from __clrclasses__.System import IntPtr as _n_1_t_8
from __clrclasses__.System import IAsyncResult as _n_1_t_9
from __clrclasses__.System import AsyncCallback as _n_1_t_10
from __clrclasses__.System import Enum as _n_1_t_11
from __clrclasses__.System import IComparable as _n_1_t_12
from __clrclasses__.System import IFormattable as _n_1_t_13
from __clrclasses__.System import IConvertible as _n_1_t_14
from __clrclasses__.System import Type as _n_1_t_15
from __clrclasses__.System import Byte as _n_1_t_16
from __clrclasses__.System import DateTime as _n_1_t_17
from __clrclasses__.System import EventHandler as _n_1_t_18
from __clrclasses__.System import TimeSpan as _n_1_t_19
from __clrclasses__.System import Exception as _n_1_t_20
from __clrclasses__.System import MarshalByRefObject as _n_1_t_21
from __clrclasses__.System.Collections import Stack as _n_2_t_0
from __clrclasses__.System.Collections import CollectionBase as _n_2_t_1
from __clrclasses__.System.Collections import IList as _n_2_t_2
from __clrclasses__.System.Collections import ICollection as _n_2_t_3
from __clrclasses__.System.Collections import DictionaryBase as _n_2_t_4
from __clrclasses__.System.Collections import IDictionary as _n_2_t_5
from __clrclasses__.System.Collections import ReadOnlyCollectionBase as _n_2_t_6
from __clrclasses__.System.Collections.Generic import IDictionary as _n_3_t_0
from __clrclasses__.System.Collections.Specialized import StringDictionary as _n_4_t_0
from __clrclasses__.System.ComponentModel import Component as _n_5_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_5_t_1
from __clrclasses__.System.ComponentModel import ISupportInitialize as _n_5_t_2
from __clrclasses__.System.ComponentModel import ISynchronizeInvoke as _n_5_t_3
from __clrclasses__.System.ComponentModel import DescriptionAttribute as _n_5_t_4
from __clrclasses__.System.Configuration import IConfigurationSectionHandler as _n_6_t_0
from __clrclasses__.System.IO import TextWriter as _n_7_t_0
from __clrclasses__.System.IO import Stream as _n_7_t_1
from __clrclasses__.System.IO import StreamReader as _n_7_t_2
from __clrclasses__.System.IO import StreamWriter as _n_7_t_3
from __clrclasses__.System.Reflection import MethodBase as _n_8_t_0
from __clrclasses__.System.Reflection import Assembly as _n_8_t_1
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_9_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_10_t_0
from __clrclasses__.System.Security import IPermission as _n_11_t_0
from __clrclasses__.System.Security import IStackWalk as _n_11_t_1
from __clrclasses__.System.Security import SecureString as _n_11_t_2
from __clrclasses__.System.Security.Permissions import ResourcePermissionBase as _n_12_t_0
from __clrclasses__.System.Security.Permissions import IUnrestrictedPermission as _n_12_t_1
from __clrclasses__.System.Security.Permissions import PermissionState as _n_12_t_2
from __clrclasses__.System.Security.Permissions import CodeAccessSecurityAttribute as _n_12_t_3
from __clrclasses__.System.Security.Permissions import SecurityAction as _n_12_t_4
from __clrclasses__.System.Text import Encoding as _n_13_t_0
from __clrclasses__.System.Threading import Thread as _n_14_t_0
import typing
class BooleanSwitch(Switch):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    def __init__(self, displayName: str, description: str, defaultSwitchValue: str) -> BooleanSwitch:...
    def __init__(self, displayName: str, description: str) -> BooleanSwitch:...
class ConditionalAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def ConditionString(self) -> str:"""ConditionString { get; } -> str"""
    def __init__(self, conditionString: str) -> ConditionalAttribute:...
class ConsoleTraceListener(TextWriterTraceListener, _n_1_t_1):
    def __init__(self, useErrorStream: bool) -> ConsoleTraceListener:...
    def __init__(self) -> ConsoleTraceListener:...
class CorrelationManager(object):
    @property
    def ActivityId(self) -> _n_1_t_2:"""ActivityId { get; set; } -> Guid"""
    @property
    def LogicalOperationStack(self) -> _n_2_t_0:"""LogicalOperationStack { get; } -> Stack"""
    def StartLogicalOperation(self):...
    def StartLogicalOperation(self, operationId: object):...
    def StopLogicalOperation(self):...
class CounterCreationData(object):
    @property
    def CounterHelp(self) -> str:"""CounterHelp { get; set; } -> str"""
    @property
    def CounterName(self) -> str:"""CounterName { get; set; } -> str"""
    @property
    def CounterType(self) -> PerformanceCounterType:"""CounterType { get; set; } -> PerformanceCounterType"""
    def __init__(self) -> CounterCreationData:...
    def __init__(self, counterName: str, counterHelp: str, counterType: PerformanceCounterType) -> CounterCreationData:...
class CounterCreationDataCollection(_n_2_t_1, _n_2_t_2, typing.Iterable[CounterCreationData]):
    def __init__(self, value: _n_1_t_3[CounterCreationData]) -> CounterCreationDataCollection:...
    def __init__(self, value: CounterCreationDataCollection) -> CounterCreationDataCollection:...
    def __init__(self) -> CounterCreationDataCollection:...
    def AddRange(self, value: CounterCreationDataCollection):...
    def AddRange(self, value: _n_1_t_3[CounterCreationData]):...
class CounterSample(_n_1_t_4):
    Empty: int
    @property
    def BaseValue(self) -> int:"""BaseValue { get; } -> int"""
    @property
    def CounterFrequency(self) -> int:"""CounterFrequency { get; } -> int"""
    @property
    def CounterTimeStamp(self) -> int:"""CounterTimeStamp { get; } -> int"""
    @property
    def CounterType(self) -> PerformanceCounterType:"""CounterType { get; } -> PerformanceCounterType"""
    @property
    def RawValue(self) -> int:"""RawValue { get; } -> int"""
    @property
    def SystemFrequency(self) -> int:"""SystemFrequency { get; } -> int"""
    @property
    def TimeStamp(self) -> int:"""TimeStamp { get; } -> int"""
    @property
    def TimeStamp100nSec(self) -> int:"""TimeStamp100nSec { get; } -> int"""
    def __init__(self, rawValue: int, baseValue: int, counterFrequency: int, systemFrequency: int, timeStamp: int, timeStamp100nSec: int, counterType: PerformanceCounterType, counterTimeStamp: int) -> CounterSample:...
    def __init__(self, rawValue: int, baseValue: int, counterFrequency: int, systemFrequency: int, timeStamp: int, timeStamp100nSec: int, counterType: PerformanceCounterType) -> CounterSample:...
    @staticmethod
    def Calculate(counterSample: CounterSample, nextCounterSample: CounterSample) -> float:...
    @staticmethod
    def Calculate(counterSample: CounterSample) -> float:...
class CounterSampleCalculator(object):
    @staticmethod
    def ComputeCounterValue(oldSample: CounterSample, newSample: CounterSample) -> float:...
    @staticmethod
    def ComputeCounterValue(newSample: CounterSample) -> float:...
class DataReceivedEventArgs(_n_1_t_5):
    @property
    def Data(self) -> str:"""Data { get; } -> str"""
class DataReceivedEventHandler(_n_1_t_6, _n_1_t_7, _n_10_t_0):
    def __init__(self, object: object, method: _n_1_t_8) -> DataReceivedEventHandler:...
    def BeginInvoke(self, sender: object, e: DataReceivedEventArgs, callback: _n_1_t_10, object: object) -> _n_1_t_9:...
    def EndInvoke(self, result: _n_1_t_9):...
    def Invoke(self, sender: object, e: DataReceivedEventArgs):...
class Debug(object):
    @property
    def AutoFlush(self) -> bool:"""AutoFlush { get; set; } -> bool"""
    @property
    def IndentLevel(self) -> int:"""IndentLevel { get; set; } -> int"""
    @property
    def IndentSize(self) -> int:"""IndentSize { get; set; } -> int"""
    @property
    def Listeners(self) -> TraceListenerCollection:"""Listeners { get; } -> TraceListenerCollection"""
    @staticmethod
    def Assert(condition: bool, message: str, detailMessageFormat: str, args: _n_1_t_3[object]):...
    @staticmethod
    def Assert(condition: bool, message: str, detailMessage: str):...
    @staticmethod
    def Assert(condition: bool, message: str):...
    @staticmethod
    def Assert(condition: bool):...
    @staticmethod
    def Close():...
    @staticmethod
    def Fail(message: str, detailMessage: str):...
    @staticmethod
    def Fail(message: str):...
    @staticmethod
    def Flush():...
    @staticmethod
    def Indent():...
    @staticmethod
    def Print(format: str, args: _n_1_t_3[object]):...
    @staticmethod
    def Print(message: str):...
    @staticmethod
    def Unindent():...
    @staticmethod
    def Write(value: object, category: str):...
    @staticmethod
    def Write(message: str, category: str):...
    @staticmethod
    def Write(value: object):...
    @staticmethod
    def Write(message: str):...
    @staticmethod
    def WriteIf(condition: bool, value: object, category: str):...
    @staticmethod
    def WriteIf(condition: bool, message: str, category: str):...
    @staticmethod
    def WriteIf(condition: bool, value: object):...
    @staticmethod
    def WriteIf(condition: bool, message: str):...
    @staticmethod
    def WriteLine(format: str, args: _n_1_t_3[object]):...
    @staticmethod
    def WriteLine(value: object, category: str):...
    @staticmethod
    def WriteLine(message: str, category: str):...
    @staticmethod
    def WriteLine(value: object):...
    @staticmethod
    def WriteLine(message: str):...
    @staticmethod
    def WriteLineIf(condition: bool, value: object, category: str):...
    @staticmethod
    def WriteLineIf(condition: bool, message: str, category: str):...
    @staticmethod
    def WriteLineIf(condition: bool, value: object):...
    @staticmethod
    def WriteLineIf(condition: bool, message: str):...
class DebuggableAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def DebuggingFlags(self) -> DebuggableAttribute.DebuggingModes:"""DebuggingFlags { get; } -> DebuggableAttribute.DebuggingModes"""
    @property
    def IsJITOptimizerDisabled(self) -> bool:"""IsJITOptimizerDisabled { get; } -> bool"""
    @property
    def IsJITTrackingEnabled(self) -> bool:"""IsJITTrackingEnabled { get; } -> bool"""
    def __init__(self, modes: DebuggableAttribute.DebuggingModes) -> DebuggableAttribute:...
    def __init__(self, isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool) -> DebuggableAttribute:...
    class DebuggingModes(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
        Default: int
        DisableOptimizations: int
        EnableEditAndContinue: int
        IgnoreSymbolStoreSequencePoints: int
        _None: int
        value__: int
class Debugger(object):
    DefaultCategory: int
    @property
    def IsAttached(self) -> bool:"""IsAttached { get; } -> bool"""
    def __init__(self) -> Debugger:...
    @staticmethod
    def Break():...
    @staticmethod
    def IsLogging() -> bool:...
    @staticmethod
    def Launch() -> bool:...
    @staticmethod
    def Log(level: int, category: str, message: str):...
    @staticmethod
    def NotifyOfCrossThreadDependency():...
class DebuggerBrowsableAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def State(self) -> DebuggerBrowsableState:"""State { get; } -> DebuggerBrowsableState"""
    def __init__(self, state: DebuggerBrowsableState) -> DebuggerBrowsableAttribute:...
class DebuggerBrowsableState(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Collapsed: int
    Never: int
    RootHidden: int
    value__: int
class DebuggerDisplayAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Target(self) -> _n_1_t_15:"""Target { get; set; } -> Type"""
    @property
    def TargetTypeName(self) -> str:"""TargetTypeName { get; set; } -> str"""
    @property
    def Type(self) -> str:"""Type { get; set; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def __init__(self, value: str) -> DebuggerDisplayAttribute:...
class DebuggerHiddenAttribute(_n_1_t_0, _n_9_t_0):
    def __init__(self) -> DebuggerHiddenAttribute:...
class DebuggerNonUserCodeAttribute(_n_1_t_0, _n_9_t_0):
    def __init__(self) -> DebuggerNonUserCodeAttribute:...
class DebuggerStepperBoundaryAttribute(_n_1_t_0, _n_9_t_0):
    def __init__(self) -> DebuggerStepperBoundaryAttribute:...
class DebuggerStepThroughAttribute(_n_1_t_0, _n_9_t_0):
    def __init__(self) -> DebuggerStepThroughAttribute:...
class DebuggerTypeProxyAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def ProxyTypeName(self) -> str:"""ProxyTypeName { get; } -> str"""
    @property
    def Target(self) -> _n_1_t_15:"""Target { get; set; } -> Type"""
    @property
    def TargetTypeName(self) -> str:"""TargetTypeName { get; set; } -> str"""
    def __init__(self, typeName: str) -> DebuggerTypeProxyAttribute:...
    def __init__(self, type: _n_1_t_15) -> DebuggerTypeProxyAttribute:...
class DebuggerVisualizerAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def Target(self) -> _n_1_t_15:"""Target { get; set; } -> Type"""
    @property
    def TargetTypeName(self) -> str:"""TargetTypeName { get; set; } -> str"""
    @property
    def VisualizerObjectSourceTypeName(self) -> str:"""VisualizerObjectSourceTypeName { get; } -> str"""
    @property
    def VisualizerTypeName(self) -> str:"""VisualizerTypeName { get; } -> str"""
    def __init__(self, visualizer: _n_1_t_15, visualizerObjectSourceTypeName: str) -> DebuggerVisualizerAttribute:...
    def __init__(self, visualizer: _n_1_t_15, visualizerObjectSource: _n_1_t_15) -> DebuggerVisualizerAttribute:...
    def __init__(self, visualizer: _n_1_t_15) -> DebuggerVisualizerAttribute:...
    def __init__(self, visualizerTypeName: str, visualizerObjectSource: _n_1_t_15) -> DebuggerVisualizerAttribute:...
    def __init__(self, visualizerTypeName: str, visualizerObjectSourceTypeName: str) -> DebuggerVisualizerAttribute:...
    def __init__(self, visualizerTypeName: str) -> DebuggerVisualizerAttribute:...
class DefaultTraceListener(TraceListener, _n_1_t_1):
    @property
    def AssertUiEnabled(self) -> bool:"""AssertUiEnabled { get; set; } -> bool"""
    @property
    def LogFileName(self) -> str:"""LogFileName { get; set; } -> str"""
    def __init__(self) -> DefaultTraceListener:...
class DelimitedListTraceListener(TextWriterTraceListener, _n_1_t_1):
    @property
    def Delimiter(self) -> str:"""Delimiter { get; set; } -> str"""
    def __init__(self, fileName: str, name: str) -> DelimitedListTraceListener:...
    def __init__(self, fileName: str) -> DelimitedListTraceListener:...
    def __init__(self, writer: _n_7_t_0, name: str) -> DelimitedListTraceListener:...
    def __init__(self, writer: _n_7_t_0) -> DelimitedListTraceListener:...
    def __init__(self, stream: _n_7_t_1, name: str) -> DelimitedListTraceListener:...
    def __init__(self, stream: _n_7_t_1) -> DelimitedListTraceListener:...
class DiagnosticsConfigurationHandler(_n_6_t_0):
    def __init__(self) -> DiagnosticsConfigurationHandler:...
class EntryWrittenEventArgs(_n_1_t_5):
    @property
    def Entry(self) -> EventLogEntry:"""Entry { get; } -> EventLogEntry"""
    def __init__(self, entry: EventLogEntry) -> EntryWrittenEventArgs:...
    def __init__(self) -> EntryWrittenEventArgs:...
class EntryWrittenEventHandler(_n_1_t_6, _n_1_t_7, _n_10_t_0):
    def __init__(self, object: object, method: _n_1_t_8) -> EntryWrittenEventHandler:...
    def BeginInvoke(self, sender: object, e: EntryWrittenEventArgs, callback: _n_1_t_10, object: object) -> _n_1_t_9:...
    def EndInvoke(self, result: _n_1_t_9):...
    def Invoke(self, sender: object, e: EntryWrittenEventArgs):...
class EventInstance(object):
    @property
    def CategoryId(self) -> int:"""CategoryId { get; set; } -> int"""
    @property
    def EntryType(self) -> EventLogEntryType:"""EntryType { get; set; } -> EventLogEntryType"""
    @property
    def InstanceId(self) -> int:"""InstanceId { get; set; } -> int"""
    def __init__(self, instanceId: int, categoryId: int, entryType: EventLogEntryType) -> EventInstance:...
    def __init__(self, instanceId: int, categoryId: int) -> EventInstance:...
class EventLog(_n_5_t_0, _n_5_t_1, _n_5_t_2):
    @property
    def EnableRaisingEvents(self) -> bool:"""EnableRaisingEvents { get; set; } -> bool"""
    @property
    def Entries(self) -> EventLogEntryCollection:"""Entries { get; } -> EventLogEntryCollection"""
    @property
    def Log(self) -> str:"""Log { get; set; } -> str"""
    @property
    def LogDisplayName(self) -> str:"""LogDisplayName { get; } -> str"""
    @property
    def MachineName(self) -> str:"""MachineName { get; set; } -> str"""
    @property
    def MaximumKilobytes(self) -> int:"""MaximumKilobytes { get; set; } -> int"""
    @property
    def MinimumRetentionDays(self) -> int:"""MinimumRetentionDays { get; } -> int"""
    @property
    def OverflowAction(self) -> OverflowAction:"""OverflowAction { get; } -> OverflowAction"""
    @property
    def Source(self) -> str:"""Source { get; set; } -> str"""
    @property
    def SynchronizingObject(self) -> _n_5_t_3:"""SynchronizingObject { get; set; } -> ISynchronizeInvoke"""
    @property
    def EntryWritten(self) -> EntryWrittenEventHandler:
        """EntryWritten Event: EntryWrittenEventHandler"""
    def __init__(self, logName: str, machineName: str, source: str) -> EventLog:...
    def __init__(self, logName: str, machineName: str) -> EventLog:...
    def __init__(self, logName: str) -> EventLog:...
    def __init__(self) -> EventLog:...
    def Clear(self):...
    def Close(self):...
    @staticmethod
    def CreateEventSource(sourceData: EventSourceCreationData):...
    @staticmethod
    def CreateEventSource(source: str, logName: str, machineName: str):...
    @staticmethod
    def CreateEventSource(source: str, logName: str):...
    @staticmethod
    def Delete(logName: str, machineName: str):...
    @staticmethod
    def Delete(logName: str):...
    @staticmethod
    def DeleteEventSource(source: str, machineName: str):...
    @staticmethod
    def DeleteEventSource(source: str):...
    @staticmethod
    def Exists(logName: str, machineName: str) -> bool:...
    @staticmethod
    def Exists(logName: str) -> bool:...
    @staticmethod
    def GetEventLogs(machineName: str) -> _n_1_t_3[EventLog]:...
    @staticmethod
    def GetEventLogs() -> _n_1_t_3[EventLog]:...
    @staticmethod
    def LogNameFromSourceName(source: str, machineName: str) -> str:...
    def ModifyOverflowPolicy(self, action: OverflowAction, retentionDays: int):...
    def RegisterDisplayName(self, resourceFile: str, resourceId: int):...
    @staticmethod
    def SourceExists(source: str, machineName: str) -> bool:...
    @staticmethod
    def SourceExists(source: str) -> bool:...
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int, category: int, rawData: _n_1_t_3[_n_1_t_16]):...
    @staticmethod
    def WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: int, rawData: _n_1_t_3[_n_1_t_16]):...
    @staticmethod
    def WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: int):...
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int, category: int):...
    @staticmethod
    def WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int):...
    def WriteEntry(self, message: str, type: EventLogEntryType, eventID: int):...
    @staticmethod
    def WriteEntry(source: str, message: str, type: EventLogEntryType):...
    def WriteEntry(self, message: str, type: EventLogEntryType):...
    @staticmethod
    def WriteEntry(source: str, message: str):...
    def WriteEntry(self, message: str):...
    @staticmethod
    def WriteEvent(source: str, instance: EventInstance, data: _n_1_t_3[_n_1_t_16], values: _n_1_t_3[object]):...
    @staticmethod
    def WriteEvent(source: str, instance: EventInstance, values: _n_1_t_3[object]):...
    def WriteEvent(self, instance: EventInstance, data: _n_1_t_3[_n_1_t_16], values: _n_1_t_3[object]):...
    def WriteEvent(self, instance: EventInstance, values: _n_1_t_3[object]):...
class EventLogEntry(_n_5_t_0, _n_5_t_1, _n_10_t_0):
    @property
    def Category(self) -> str:"""Category { get; } -> str"""
    @property
    def CategoryNumber(self) -> int:"""CategoryNumber { get; } -> int"""
    @property
    def Data(self) -> _n_1_t_3[_n_1_t_16]:"""Data { get; } -> Array"""
    @property
    def EntryType(self) -> EventLogEntryType:"""EntryType { get; } -> EventLogEntryType"""
    @property
    def EventID(self) -> int:"""EventID { get; } -> int"""
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def InstanceId(self) -> int:"""InstanceId { get; } -> int"""
    @property
    def MachineName(self) -> str:"""MachineName { get; } -> str"""
    @property
    def Message(self) -> str:"""Message { get; } -> str"""
    @property
    def ReplacementStrings(self) -> _n_1_t_3[str]:"""ReplacementStrings { get; } -> Array"""
    @property
    def Source(self) -> str:"""Source { get; } -> str"""
    @property
    def TimeGenerated(self) -> _n_1_t_17:"""TimeGenerated { get; } -> DateTime"""
    @property
    def TimeWritten(self) -> _n_1_t_17:"""TimeWritten { get; } -> DateTime"""
    @property
    def UserName(self) -> str:"""UserName { get; } -> str"""
class EventLogEntryCollection(_n_2_t_3, typing.Iterable[EventLogEntry]):
    @property
    def Item(self) -> EventLogEntry:"""Item { get; } -> EventLogEntry"""
class EventLogEntryType(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Error: int
    FailureAudit: int
    Information: int
    SuccessAudit: int
    value__: int
    Warning: int
class EventLogPermission(_n_12_t_0, _n_11_t_0, _n_11_t_1, _n_12_t_1):
    @property
    def PermissionEntries(self) -> EventLogPermissionEntryCollection:"""PermissionEntries { get; } -> EventLogPermissionEntryCollection"""
    def __init__(self, permissionAccessEntries: _n_1_t_3[EventLogPermissionEntry]) -> EventLogPermission:...
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: str) -> EventLogPermission:...
    def __init__(self, state: _n_12_t_2) -> EventLogPermission:...
    def __init__(self) -> EventLogPermission:...
class EventLogPermissionAccess(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Administer: int
    Audit: int
    Browse: int
    Instrument: int
    _None: int
    value__: int
    Write: int
class EventLogPermissionAttribute(_n_12_t_3, _n_9_t_0):
    @property
    def MachineName(self) -> str:"""MachineName { get; set; } -> str"""
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:"""PermissionAccess { get; set; } -> EventLogPermissionAccess"""
    def __init__(self, action: _n_12_t_4) -> EventLogPermissionAttribute:...
class EventLogPermissionEntry(object):
    @property
    def MachineName(self) -> str:"""MachineName { get; } -> str"""
    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:"""PermissionAccess { get; } -> EventLogPermissionAccess"""
    def __init__(self, permissionAccess: EventLogPermissionAccess, machineName: str) -> EventLogPermissionEntry:...
class EventLogPermissionEntryCollection(_n_2_t_1, _n_2_t_2, typing.Iterable[EventLogPermissionEntry]):
    def AddRange(self, value: EventLogPermissionEntryCollection):...
    def AddRange(self, value: _n_1_t_3[EventLogPermissionEntry]):...
class EventLogTraceListener(TraceListener, _n_1_t_1):
    @property
    def EventLog(self) -> EventLog:"""EventLog { get; set; } -> EventLog"""
    def __init__(self, source: str) -> EventLogTraceListener:...
    def __init__(self, eventLog: EventLog) -> EventLogTraceListener:...
    def __init__(self) -> EventLogTraceListener:...
class EventSchemaTraceListener(TextWriterTraceListener, _n_1_t_1):
    @property
    def BufferSize(self) -> int:"""BufferSize { get; } -> int"""
    @property
    def MaximumFileSize(self) -> int:"""MaximumFileSize { get; } -> int"""
    @property
    def MaximumNumberOfFiles(self) -> int:"""MaximumNumberOfFiles { get; } -> int"""
    @property
    def TraceLogRetentionOption(self) -> TraceLogRetentionOption:"""TraceLogRetentionOption { get; } -> TraceLogRetentionOption"""
    def __init__(self, fileName: str) -> EventSchemaTraceListener:...
    def __init__(self, fileName: str, name: str) -> EventSchemaTraceListener:...
    def __init__(self, fileName: str, name: str, bufferSize: int) -> EventSchemaTraceListener:...
    def __init__(self, fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption) -> EventSchemaTraceListener:...
    def __init__(self, fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption, maximumFileSize: int) -> EventSchemaTraceListener:...
    def __init__(self, fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption, maximumFileSize: int, maximumNumberOfFiles: int) -> EventSchemaTraceListener:...
class EventSourceCreationData(object):
    @property
    def CategoryCount(self) -> int:"""CategoryCount { get; set; } -> int"""
    @property
    def CategoryResourceFile(self) -> str:"""CategoryResourceFile { get; set; } -> str"""
    @property
    def LogName(self) -> str:"""LogName { get; set; } -> str"""
    @property
    def MachineName(self) -> str:"""MachineName { get; set; } -> str"""
    @property
    def MessageResourceFile(self) -> str:"""MessageResourceFile { get; set; } -> str"""
    @property
    def ParameterResourceFile(self) -> str:"""ParameterResourceFile { get; set; } -> str"""
    @property
    def Source(self) -> str:"""Source { get; set; } -> str"""
    def __init__(self, source: str, logName: str) -> EventSourceCreationData:...
class EventTypeFilter(TraceFilter):
    @property
    def EventType(self) -> SourceLevels:"""EventType { get; set; } -> SourceLevels"""
    def __init__(self, level: SourceLevels) -> EventTypeFilter:...
class FileVersionInfo(object):
    @property
    def Comments(self) -> str:"""Comments { get; } -> str"""
    @property
    def CompanyName(self) -> str:"""CompanyName { get; } -> str"""
    @property
    def FileBuildPart(self) -> int:"""FileBuildPart { get; } -> int"""
    @property
    def FileDescription(self) -> str:"""FileDescription { get; } -> str"""
    @property
    def FileMajorPart(self) -> int:"""FileMajorPart { get; } -> int"""
    @property
    def FileMinorPart(self) -> int:"""FileMinorPart { get; } -> int"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def FilePrivatePart(self) -> int:"""FilePrivatePart { get; } -> int"""
    @property
    def FileVersion(self) -> str:"""FileVersion { get; } -> str"""
    @property
    def InternalName(self) -> str:"""InternalName { get; } -> str"""
    @property
    def IsDebug(self) -> bool:"""IsDebug { get; } -> bool"""
    @property
    def IsPatched(self) -> bool:"""IsPatched { get; } -> bool"""
    @property
    def IsPreRelease(self) -> bool:"""IsPreRelease { get; } -> bool"""
    @property
    def IsPrivateBuild(self) -> bool:"""IsPrivateBuild { get; } -> bool"""
    @property
    def IsSpecialBuild(self) -> bool:"""IsSpecialBuild { get; } -> bool"""
    @property
    def Language(self) -> str:"""Language { get; } -> str"""
    @property
    def LegalCopyright(self) -> str:"""LegalCopyright { get; } -> str"""
    @property
    def LegalTrademarks(self) -> str:"""LegalTrademarks { get; } -> str"""
    @property
    def OriginalFilename(self) -> str:"""OriginalFilename { get; } -> str"""
    @property
    def PrivateBuild(self) -> str:"""PrivateBuild { get; } -> str"""
    @property
    def ProductBuildPart(self) -> int:"""ProductBuildPart { get; } -> int"""
    @property
    def ProductMajorPart(self) -> int:"""ProductMajorPart { get; } -> int"""
    @property
    def ProductMinorPart(self) -> int:"""ProductMinorPart { get; } -> int"""
    @property
    def ProductName(self) -> str:"""ProductName { get; } -> str"""
    @property
    def ProductPrivatePart(self) -> int:"""ProductPrivatePart { get; } -> int"""
    @property
    def ProductVersion(self) -> str:"""ProductVersion { get; } -> str"""
    @property
    def SpecialBuild(self) -> str:"""SpecialBuild { get; } -> str"""
    @staticmethod
    def GetVersionInfo(fileName: str) -> FileVersionInfo:...
class ICollectData():
    def CloseData(self):...
    def CollectData(self, id: int, valueName: _n_1_t_8, data: _n_1_t_8, totalBytes: int, res: _n_1_t_8):...
class InstanceData(object):
    @property
    def InstanceName(self) -> str:"""InstanceName { get; } -> str"""
    @property
    def RawValue(self) -> int:"""RawValue { get; } -> int"""
    @property
    def Sample(self) -> CounterSample:"""Sample { get; } -> CounterSample"""
    def __init__(self, instanceName: str, sample: CounterSample) -> InstanceData:...
class InstanceDataCollection(_n_2_t_4, _n_2_t_5, typing.Iterable[InstanceData]):
    @property
    def CounterName(self) -> str:"""CounterName { get; } -> str"""
    def __init__(self, counterName: str) -> InstanceDataCollection:...
class InstanceDataCollectionCollection(_n_2_t_4, _n_2_t_5, typing.Iterable[InstanceDataCollection]):
    def __init__(self) -> InstanceDataCollectionCollection:...
class MonitoringDescriptionAttribute(_n_5_t_4, _n_9_t_0):
    def __init__(self, description: str) -> MonitoringDescriptionAttribute:...
class OverflowAction(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    DoNotOverwrite: int
    OverwriteAsNeeded: int
    OverwriteOlder: int
    value__: int
class PerformanceCounter(_n_5_t_0, _n_5_t_1, _n_5_t_2):
    DefaultFileMappingSize: int
    @property
    def CategoryName(self) -> str:"""CategoryName { get; set; } -> str"""
    @property
    def CounterHelp(self) -> str:"""CounterHelp { get; } -> str"""
    @property
    def CounterName(self) -> str:"""CounterName { get; set; } -> str"""
    @property
    def CounterType(self) -> PerformanceCounterType:"""CounterType { get; } -> PerformanceCounterType"""
    @property
    def InstanceLifetime(self) -> PerformanceCounterInstanceLifetime:"""InstanceLifetime { get; set; } -> PerformanceCounterInstanceLifetime"""
    @property
    def InstanceName(self) -> str:"""InstanceName { get; set; } -> str"""
    @property
    def MachineName(self) -> str:"""MachineName { get; set; } -> str"""
    @property
    def RawValue(self) -> int:"""RawValue { get; set; } -> int"""
    @property
    def ReadOnly(self) -> bool:"""ReadOnly { get; set; } -> bool"""
    def __init__(self, categoryName: str, counterName: str, readOnly: bool) -> PerformanceCounter:...
    def __init__(self, categoryName: str, counterName: str) -> PerformanceCounter:...
    def __init__(self, categoryName: str, counterName: str, instanceName: str, readOnly: bool) -> PerformanceCounter:...
    def __init__(self, categoryName: str, counterName: str, instanceName: str) -> PerformanceCounter:...
    def __init__(self, categoryName: str, counterName: str, instanceName: str, machineName: str) -> PerformanceCounter:...
    def __init__(self) -> PerformanceCounter:...
    def Close(self):...
    @staticmethod
    def CloseSharedResources():...
    def Decrement(self) -> int:...
    def Increment(self) -> int:...
    def IncrementBy(self, value: int) -> int:...
    def NextSample(self) -> CounterSample:...
    def NextValue(self) -> float:...
    def RemoveInstance(self):...
class PerformanceCounterCategory(object):
    @property
    def CategoryHelp(self) -> str:"""CategoryHelp { get; } -> str"""
    @property
    def CategoryName(self) -> str:"""CategoryName { get; set; } -> str"""
    @property
    def CategoryType(self) -> PerformanceCounterCategoryType:"""CategoryType { get; } -> PerformanceCounterCategoryType"""
    @property
    def MachineName(self) -> str:"""MachineName { get; set; } -> str"""
    def __init__(self, categoryName: str, machineName: str) -> PerformanceCounterCategory:...
    def __init__(self, categoryName: str) -> PerformanceCounterCategory:...
    def __init__(self) -> PerformanceCounterCategory:...
    @staticmethod
    def CounterExists(counterName: str, categoryName: str, machineName: str) -> bool:...
    @staticmethod
    def CounterExists(counterName: str, categoryName: str) -> bool:...
    def CounterExists(self, counterName: str) -> bool:...
    @staticmethod
    def Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory:...
    @staticmethod
    def Create(categoryName: str, categoryHelp: str, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory:...
    @staticmethod
    def Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterName: str, counterHelp: str) -> PerformanceCounterCategory:...
    @staticmethod
    def Create(categoryName: str, categoryHelp: str, counterName: str, counterHelp: str) -> PerformanceCounterCategory:...
    @staticmethod
    def Delete(categoryName: str):...
    @staticmethod
    def Exists(categoryName: str, machineName: str) -> bool:...
    @staticmethod
    def Exists(categoryName: str) -> bool:...
    @staticmethod
    def GetCategories(machineName: str) -> _n_1_t_3[PerformanceCounterCategory]:...
    @staticmethod
    def GetCategories() -> _n_1_t_3[PerformanceCounterCategory]:...
    def GetCounters(self, instanceName: str) -> _n_1_t_3[PerformanceCounter]:...
    def GetCounters(self) -> _n_1_t_3[PerformanceCounter]:...
    def GetInstanceNames(self) -> _n_1_t_3[str]:...
    @staticmethod
    def InstanceExists(instanceName: str, categoryName: str, machineName: str) -> bool:...
    @staticmethod
    def InstanceExists(instanceName: str, categoryName: str) -> bool:...
    def InstanceExists(self, instanceName: str) -> bool:...
    def ReadCategory(self) -> InstanceDataCollectionCollection:...
class PerformanceCounterCategoryType(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    MultiInstance: int
    SingleInstance: int
    Unknown: int
    value__: int
class PerformanceCounterInstanceLifetime(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Global: int
    Process: int
    value__: int
class PerformanceCounterManager(ICollectData):
    def __init__(self) -> PerformanceCounterManager:...
class PerformanceCounterPermission(_n_12_t_0, _n_11_t_0, _n_11_t_1, _n_12_t_1):
    @property
    def PermissionEntries(self) -> PerformanceCounterPermissionEntryCollection:"""PermissionEntries { get; } -> PerformanceCounterPermissionEntryCollection"""
    def __init__(self, permissionAccessEntries: _n_1_t_3[PerformanceCounterPermissionEntry]) -> PerformanceCounterPermission:...
    def __init__(self, permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str) -> PerformanceCounterPermission:...
    def __init__(self, state: _n_12_t_2) -> PerformanceCounterPermission:...
    def __init__(self) -> PerformanceCounterPermission:...
class PerformanceCounterPermissionAccess(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Administer: int
    Browse: int
    Instrument: int
    _None: int
    Read: int
    value__: int
    Write: int
class PerformanceCounterPermissionAttribute(_n_12_t_3, _n_9_t_0):
    @property
    def CategoryName(self) -> str:"""CategoryName { get; set; } -> str"""
    @property
    def MachineName(self) -> str:"""MachineName { get; set; } -> str"""
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:"""PermissionAccess { get; set; } -> PerformanceCounterPermissionAccess"""
    def __init__(self, action: _n_12_t_4) -> PerformanceCounterPermissionAttribute:...
class PerformanceCounterPermissionEntry(object):
    @property
    def CategoryName(self) -> str:"""CategoryName { get; } -> str"""
    @property
    def MachineName(self) -> str:"""MachineName { get; } -> str"""
    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:"""PermissionAccess { get; } -> PerformanceCounterPermissionAccess"""
    def __init__(self, permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str) -> PerformanceCounterPermissionEntry:...
class PerformanceCounterPermissionEntryCollection(_n_2_t_1, _n_2_t_2, typing.Iterable[PerformanceCounterPermissionEntry]):
    def AddRange(self, value: PerformanceCounterPermissionEntryCollection):...
    def AddRange(self, value: _n_1_t_3[PerformanceCounterPermissionEntry]):...
class PerformanceCounterType(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    AverageBase: int
    AverageCount64: int
    AverageTimer32: int
    CounterDelta32: int
    CounterDelta64: int
    CounterMultiBase: int
    CounterMultiTimer: int
    CounterMultiTimer100Ns: int
    CounterMultiTimer100NsInverse: int
    CounterMultiTimerInverse: int
    CounterTimer: int
    CounterTimerInverse: int
    CountPerTimeInterval32: int
    CountPerTimeInterval64: int
    ElapsedTime: int
    NumberOfItems32: int
    NumberOfItems64: int
    NumberOfItemsHEX32: int
    NumberOfItemsHEX64: int
    RateOfCountsPerSecond32: int
    RateOfCountsPerSecond64: int
    RawBase: int
    RawFraction: int
    SampleBase: int
    SampleCounter: int
    SampleFraction: int
    Timer100Ns: int
    Timer100NsInverse: int
    value__: int
class Process(_n_5_t_0, _n_5_t_1):
    @property
    def BasePriority(self) -> int:"""BasePriority { get; } -> int"""
    @property
    def EnableRaisingEvents(self) -> bool:"""EnableRaisingEvents { get; set; } -> bool"""
    @property
    def ExitCode(self) -> int:"""ExitCode { get; } -> int"""
    @property
    def ExitTime(self) -> _n_1_t_17:"""ExitTime { get; } -> DateTime"""
    @property
    def Handle(self) -> _n_1_t_8:"""Handle { get; } -> IntPtr"""
    @property
    def HandleCount(self) -> int:"""HandleCount { get; } -> int"""
    @property
    def HasExited(self) -> bool:"""HasExited { get; } -> bool"""
    @property
    def Id(self) -> int:"""Id { get; } -> int"""
    @property
    def MachineName(self) -> str:"""MachineName { get; } -> str"""
    @property
    def MainModule(self) -> ProcessModule:"""MainModule { get; } -> ProcessModule"""
    @property
    def MainWindowHandle(self) -> _n_1_t_8:"""MainWindowHandle { get; } -> IntPtr"""
    @property
    def MainWindowTitle(self) -> str:"""MainWindowTitle { get; } -> str"""
    @property
    def MaxWorkingSet(self) -> _n_1_t_8:"""MaxWorkingSet { get; set; } -> IntPtr"""
    @property
    def MinWorkingSet(self) -> _n_1_t_8:"""MinWorkingSet { get; set; } -> IntPtr"""
    @property
    def Modules(self) -> ProcessModuleCollection:"""Modules { get; } -> ProcessModuleCollection"""
    @property
    def NonpagedSystemMemorySize(self) -> int:"""NonpagedSystemMemorySize { get; } -> int"""
    @property
    def NonpagedSystemMemorySize64(self) -> int:"""NonpagedSystemMemorySize64 { get; } -> int"""
    @property
    def PagedMemorySize(self) -> int:"""PagedMemorySize { get; } -> int"""
    @property
    def PagedMemorySize64(self) -> int:"""PagedMemorySize64 { get; } -> int"""
    @property
    def PagedSystemMemorySize(self) -> int:"""PagedSystemMemorySize { get; } -> int"""
    @property
    def PagedSystemMemorySize64(self) -> int:"""PagedSystemMemorySize64 { get; } -> int"""
    @property
    def PeakPagedMemorySize(self) -> int:"""PeakPagedMemorySize { get; } -> int"""
    @property
    def PeakPagedMemorySize64(self) -> int:"""PeakPagedMemorySize64 { get; } -> int"""
    @property
    def PeakVirtualMemorySize(self) -> int:"""PeakVirtualMemorySize { get; } -> int"""
    @property
    def PeakVirtualMemorySize64(self) -> int:"""PeakVirtualMemorySize64 { get; } -> int"""
    @property
    def PeakWorkingSet(self) -> int:"""PeakWorkingSet { get; } -> int"""
    @property
    def PeakWorkingSet64(self) -> int:"""PeakWorkingSet64 { get; } -> int"""
    @property
    def PriorityBoostEnabled(self) -> bool:"""PriorityBoostEnabled { get; set; } -> bool"""
    @property
    def PriorityClass(self) -> ProcessPriorityClass:"""PriorityClass { get; set; } -> ProcessPriorityClass"""
    @property
    def PrivateMemorySize(self) -> int:"""PrivateMemorySize { get; } -> int"""
    @property
    def PrivateMemorySize64(self) -> int:"""PrivateMemorySize64 { get; } -> int"""
    @property
    def PrivilegedProcessorTime(self) -> _n_1_t_19:"""PrivilegedProcessorTime { get; } -> TimeSpan"""
    @property
    def ProcessName(self) -> str:"""ProcessName { get; } -> str"""
    @property
    def ProcessorAffinity(self) -> _n_1_t_8:"""ProcessorAffinity { get; set; } -> IntPtr"""
    @property
    def Responding(self) -> bool:"""Responding { get; } -> bool"""
    @property
    def SafeHandle(self) -> _n_0_t_0:"""SafeHandle { get; } -> SafeProcessHandle"""
    @property
    def SessionId(self) -> int:"""SessionId { get; } -> int"""
    @property
    def StandardError(self) -> _n_7_t_2:"""StandardError { get; } -> StreamReader"""
    @property
    def StandardInput(self) -> _n_7_t_3:"""StandardInput { get; } -> StreamWriter"""
    @property
    def StandardOutput(self) -> _n_7_t_2:"""StandardOutput { get; } -> StreamReader"""
    @property
    def StartInfo(self) -> ProcessStartInfo:"""StartInfo { get; set; } -> ProcessStartInfo"""
    @property
    def StartTime(self) -> _n_1_t_17:"""StartTime { get; } -> DateTime"""
    @property
    def SynchronizingObject(self) -> _n_5_t_3:"""SynchronizingObject { get; set; } -> ISynchronizeInvoke"""
    @property
    def Threads(self) -> ProcessThreadCollection:"""Threads { get; } -> ProcessThreadCollection"""
    @property
    def TotalProcessorTime(self) -> _n_1_t_19:"""TotalProcessorTime { get; } -> TimeSpan"""
    @property
    def UserProcessorTime(self) -> _n_1_t_19:"""UserProcessorTime { get; } -> TimeSpan"""
    @property
    def VirtualMemorySize(self) -> int:"""VirtualMemorySize { get; } -> int"""
    @property
    def VirtualMemorySize64(self) -> int:"""VirtualMemorySize64 { get; } -> int"""
    @property
    def WorkingSet(self) -> int:"""WorkingSet { get; } -> int"""
    @property
    def WorkingSet64(self) -> int:"""WorkingSet64 { get; } -> int"""
    @property
    def ErrorDataReceived(self) -> DataReceivedEventHandler:
        """ErrorDataReceived Event: DataReceivedEventHandler"""
    @property
    def Exited(self) -> _n_1_t_18:
        """Exited Event: EventHandler"""
    @property
    def OutputDataReceived(self) -> DataReceivedEventHandler:
        """OutputDataReceived Event: DataReceivedEventHandler"""
    def __init__(self) -> Process:...
    def BeginErrorReadLine(self):...
    def BeginOutputReadLine(self):...
    def CancelErrorRead(self):...
    def CancelOutputRead(self):...
    def Close(self):...
    def CloseMainWindow(self) -> bool:...
    @staticmethod
    def EnterDebugMode():...
    @staticmethod
    def GetCurrentProcess() -> Process:...
    @staticmethod
    def GetProcessById(processId: int) -> Process:...
    @staticmethod
    def GetProcessById(processId: int, machineName: str) -> Process:...
    @staticmethod
    def GetProcesses(machineName: str) -> _n_1_t_3[Process]:...
    @staticmethod
    def GetProcesses() -> _n_1_t_3[Process]:...
    @staticmethod
    def GetProcessesByName(processName: str, machineName: str) -> _n_1_t_3[Process]:...
    @staticmethod
    def GetProcessesByName(processName: str) -> _n_1_t_3[Process]:...
    def Kill(self):...
    @staticmethod
    def LeaveDebugMode():...
    def Refresh(self):...
    @staticmethod
    def Start(startInfo: ProcessStartInfo) -> Process:...
    @staticmethod
    def Start(fileName: str, arguments: str) -> Process:...
    @staticmethod
    def Start(fileName: str) -> Process:...
    @staticmethod
    def Start(fileName: str, arguments: str, userName: str, password: _n_11_t_2, domain: str) -> Process:...
    @staticmethod
    def Start(fileName: str, userName: str, password: _n_11_t_2, domain: str) -> Process:...
    def Start(self) -> bool:...
    def WaitForExit(self):...
    def WaitForExit(self, milliseconds: int) -> bool:...
    def WaitForInputIdle(self) -> bool:...
    def WaitForInputIdle(self, milliseconds: int) -> bool:...
class ProcessModule(_n_5_t_0, _n_5_t_1):
    @property
    def BaseAddress(self) -> _n_1_t_8:"""BaseAddress { get; } -> IntPtr"""
    @property
    def EntryPointAddress(self) -> _n_1_t_8:"""EntryPointAddress { get; } -> IntPtr"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def FileVersionInfo(self) -> FileVersionInfo:"""FileVersionInfo { get; } -> FileVersionInfo"""
    @property
    def ModuleMemorySize(self) -> int:"""ModuleMemorySize { get; } -> int"""
    @property
    def ModuleName(self) -> str:"""ModuleName { get; } -> str"""
class ProcessModuleCollection(_n_2_t_6, _n_2_t_3, typing.Iterable[ProcessModule]):
    @property
    def Item(self) -> ProcessModule:"""Item { get; } -> ProcessModule"""
    def __init__(self, processModules: _n_1_t_3[ProcessModule]) -> ProcessModuleCollection:...
    def Contains(self, module: ProcessModule) -> bool:...
    def IndexOf(self, module: ProcessModule) -> int:...
class ProcessPriorityClass(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    AboveNormal: int
    BelowNormal: int
    High: int
    Idle: int
    Normal: int
    RealTime: int
    value__: int
class ProcessStartInfo(object):
    @property
    def Arguments(self) -> str:"""Arguments { get; set; } -> str"""
    @property
    def CreateNoWindow(self) -> bool:"""CreateNoWindow { get; set; } -> bool"""
    @property
    def Domain(self) -> str:"""Domain { get; set; } -> str"""
    @property
    def Environment(self) -> _n_3_t_0[str, str]:"""Environment { get; } -> IDictionary"""
    @property
    def EnvironmentVariables(self) -> _n_4_t_0:"""EnvironmentVariables { get; } -> StringDictionary"""
    @property
    def ErrorDialog(self) -> bool:"""ErrorDialog { get; set; } -> bool"""
    @property
    def ErrorDialogParentHandle(self) -> _n_1_t_8:"""ErrorDialogParentHandle { get; set; } -> IntPtr"""
    @property
    def FileName(self) -> str:"""FileName { get; set; } -> str"""
    @property
    def LoadUserProfile(self) -> bool:"""LoadUserProfile { get; set; } -> bool"""
    @property
    def Password(self) -> _n_11_t_2:"""Password { get; set; } -> SecureString"""
    @property
    def PasswordInClearText(self) -> str:"""PasswordInClearText { get; set; } -> str"""
    @property
    def RedirectStandardError(self) -> bool:"""RedirectStandardError { get; set; } -> bool"""
    @property
    def RedirectStandardInput(self) -> bool:"""RedirectStandardInput { get; set; } -> bool"""
    @property
    def RedirectStandardOutput(self) -> bool:"""RedirectStandardOutput { get; set; } -> bool"""
    @property
    def StandardErrorEncoding(self) -> _n_13_t_0:"""StandardErrorEncoding { get; set; } -> Encoding"""
    @property
    def StandardOutputEncoding(self) -> _n_13_t_0:"""StandardOutputEncoding { get; set; } -> Encoding"""
    @property
    def UserName(self) -> str:"""UserName { get; set; } -> str"""
    @property
    def UseShellExecute(self) -> bool:"""UseShellExecute { get; set; } -> bool"""
    @property
    def Verb(self) -> str:"""Verb { get; set; } -> str"""
    @property
    def Verbs(self) -> _n_1_t_3[str]:"""Verbs { get; } -> Array"""
    @property
    def WindowStyle(self) -> ProcessWindowStyle:"""WindowStyle { get; set; } -> ProcessWindowStyle"""
    @property
    def WorkingDirectory(self) -> str:"""WorkingDirectory { get; set; } -> str"""
    def __init__(self, fileName: str, arguments: str) -> ProcessStartInfo:...
    def __init__(self, fileName: str) -> ProcessStartInfo:...
    def __init__(self) -> ProcessStartInfo:...
class ProcessThread(_n_5_t_0, _n_5_t_1):
    @property
    def BasePriority(self) -> int:"""BasePriority { get; } -> int"""
    @property
    def CurrentPriority(self) -> int:"""CurrentPriority { get; } -> int"""
    @property
    def Id(self) -> int:"""Id { get; } -> int"""
    @property
    def IdealProcessor(self) -> int:"""IdealProcessor { set; } -> int"""
    @property
    def PriorityBoostEnabled(self) -> bool:"""PriorityBoostEnabled { get; set; } -> bool"""
    @property
    def PriorityLevel(self) -> ThreadPriorityLevel:"""PriorityLevel { get; set; } -> ThreadPriorityLevel"""
    @property
    def PrivilegedProcessorTime(self) -> _n_1_t_19:"""PrivilegedProcessorTime { get; } -> TimeSpan"""
    @property
    def ProcessorAffinity(self) -> _n_1_t_8:"""ProcessorAffinity { set; } -> IntPtr"""
    @property
    def StartAddress(self) -> _n_1_t_8:"""StartAddress { get; } -> IntPtr"""
    @property
    def StartTime(self) -> _n_1_t_17:"""StartTime { get; } -> DateTime"""
    @property
    def ThreadState(self) -> ThreadState:"""ThreadState { get; } -> ThreadState"""
    @property
    def TotalProcessorTime(self) -> _n_1_t_19:"""TotalProcessorTime { get; } -> TimeSpan"""
    @property
    def UserProcessorTime(self) -> _n_1_t_19:"""UserProcessorTime { get; } -> TimeSpan"""
    @property
    def WaitReason(self) -> ThreadWaitReason:"""WaitReason { get; } -> ThreadWaitReason"""
    def ResetIdealProcessor(self):...
class ProcessThreadCollection(_n_2_t_6, _n_2_t_3, typing.Iterable[ProcessThread]):
    @property
    def Item(self) -> ProcessThread:"""Item { get; } -> ProcessThread"""
    def __init__(self, processThreads: _n_1_t_3[ProcessThread]) -> ProcessThreadCollection:...
    def Add(self, thread: ProcessThread) -> int:...
    def Contains(self, thread: ProcessThread) -> bool:...
    def IndexOf(self, thread: ProcessThread) -> int:...
    def Insert(self, index: int, thread: ProcessThread):...
    def Remove(self, thread: ProcessThread):...
class ProcessWindowStyle(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Hidden: int
    Maximized: int
    Minimized: int
    Normal: int
    value__: int
class SourceFilter(TraceFilter):
    @property
    def Source(self) -> str:"""Source { get; set; } -> str"""
    def __init__(self, source: str) -> SourceFilter:...
class SourceLevels(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    ActivityTracing: int
    All: int
    Critical: int
    Error: int
    Information: int
    Off: int
    value__: int
    Verbose: int
    Warning: int
class SourceSwitch(Switch):
    @property
    def Level(self) -> SourceLevels:"""Level { get; set; } -> SourceLevels"""
    def __init__(self, displayName: str, defaultSwitchValue: str) -> SourceSwitch:...
    def __init__(self, name: str) -> SourceSwitch:...
    def ShouldTrace(self, eventType: TraceEventType) -> bool:...
class StackFrame(object):
    OFFSET_UNKNOWN: int
    def __init__(self, fileName: str, lineNumber: int, colNumber: int) -> StackFrame:...
    def __init__(self, fileName: str, lineNumber: int) -> StackFrame:...
    def __init__(self, skipFrames: int, fNeedFileInfo: bool) -> StackFrame:...
    def __init__(self, skipFrames: int) -> StackFrame:...
    def __init__(self, fNeedFileInfo: bool) -> StackFrame:...
    def __init__(self) -> StackFrame:...
    def GetFileColumnNumber(self) -> int:...
    def GetFileLineNumber(self) -> int:...
    def GetFileName(self) -> str:...
    def GetILOffset(self) -> int:...
    def GetMethod(self) -> _n_8_t_0:...
    def GetNativeOffset(self) -> int:...
    def GetNativeImageBase(self) -> _n_1_t_8:
        """Extension from: System.Diagnostics.StackFrameExtensions"""
    def GetNativeIP(self) -> _n_1_t_8:
        """Extension from: System.Diagnostics.StackFrameExtensions"""
    def HasILOffset(self) -> bool:
        """Extension from: System.Diagnostics.StackFrameExtensions"""
    def HasMethod(self) -> bool:
        """Extension from: System.Diagnostics.StackFrameExtensions"""
    def HasNativeImage(self) -> bool:
        """Extension from: System.Diagnostics.StackFrameExtensions"""
    def HasSource(self) -> bool:
        """Extension from: System.Diagnostics.StackFrameExtensions"""
class StackFrameExtensions(object):
    @staticmethod
    def GetNativeImageBase(stackFrame: StackFrame) -> _n_1_t_8:...
    @staticmethod
    def GetNativeIP(stackFrame: StackFrame) -> _n_1_t_8:...
    @staticmethod
    def HasILOffset(stackFrame: StackFrame) -> bool:...
    @staticmethod
    def HasMethod(stackFrame: StackFrame) -> bool:...
    @staticmethod
    def HasNativeImage(stackFrame: StackFrame) -> bool:...
    @staticmethod
    def HasSource(stackFrame: StackFrame) -> bool:...
class StackTrace(object):
    METHODS_TO_SKIP: int
    @property
    def FrameCount(self) -> int:"""FrameCount { get; } -> int"""
    def __init__(self, targetThread: _n_14_t_0, needFileInfo: bool) -> StackTrace:...
    def __init__(self, frame: StackFrame) -> StackTrace:...
    def __init__(self, e: _n_1_t_20, skipFrames: int, fNeedFileInfo: bool) -> StackTrace:...
    def __init__(self, e: _n_1_t_20, skipFrames: int) -> StackTrace:...
    def __init__(self, e: _n_1_t_20, fNeedFileInfo: bool) -> StackTrace:...
    def __init__(self, e: _n_1_t_20) -> StackTrace:...
    def __init__(self, skipFrames: int, fNeedFileInfo: bool) -> StackTrace:...
    def __init__(self, skipFrames: int) -> StackTrace:...
    def __init__(self, fNeedFileInfo: bool) -> StackTrace:...
    def __init__(self) -> StackTrace:...
    def GetFrame(self, index: int) -> StackFrame:...
    def GetFrames(self) -> _n_1_t_3[StackFrame]:...
class Stopwatch(object):
    Frequency: int
    IsHighResolution: int
    @property
    def Elapsed(self) -> _n_1_t_19:"""Elapsed { get; } -> TimeSpan"""
    @property
    def ElapsedMilliseconds(self) -> int:"""ElapsedMilliseconds { get; } -> int"""
    @property
    def ElapsedTicks(self) -> int:"""ElapsedTicks { get; } -> int"""
    @property
    def IsRunning(self) -> bool:"""IsRunning { get; } -> bool"""
    def __init__(self) -> Stopwatch:...
    @staticmethod
    def GetTimestamp() -> int:...
    def Reset(self):...
    def Restart(self):...
    def Start(self):...
    @staticmethod
    def StartNew() -> Stopwatch:...
    def Stop(self):...
class Switch(object):
    @property
    def Attributes(self) -> _n_4_t_0:"""Attributes { get; } -> StringDictionary"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    @property
    def DisplayName(self) -> str:"""DisplayName { get; } -> str"""
class SwitchAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def SwitchDescription(self) -> str:"""SwitchDescription { get; set; } -> str"""
    @property
    def SwitchName(self) -> str:"""SwitchName { get; set; } -> str"""
    @property
    def SwitchType(self) -> _n_1_t_15:"""SwitchType { get; set; } -> Type"""
    def __init__(self, switchName: str, switchType: _n_1_t_15) -> SwitchAttribute:...
    @staticmethod
    def GetAll(assembly: _n_8_t_1) -> _n_1_t_3[SwitchAttribute]:...
class SwitchLevelAttribute(_n_1_t_0, _n_9_t_0):
    @property
    def SwitchLevelType(self) -> _n_1_t_15:"""SwitchLevelType { get; set; } -> Type"""
    def __init__(self, switchLevelType: _n_1_t_15) -> SwitchLevelAttribute:...
class TextWriterTraceListener(TraceListener, _n_1_t_1):
    @property
    def Writer(self) -> _n_7_t_0:"""Writer { get; set; } -> TextWriter"""
    def __init__(self, fileName: str, name: str) -> TextWriterTraceListener:...
    def __init__(self, fileName: str) -> TextWriterTraceListener:...
    def __init__(self, writer: _n_7_t_0, name: str) -> TextWriterTraceListener:...
    def __init__(self, writer: _n_7_t_0) -> TextWriterTraceListener:...
    def __init__(self, stream: _n_7_t_1, name: str) -> TextWriterTraceListener:...
    def __init__(self, stream: _n_7_t_1) -> TextWriterTraceListener:...
    def __init__(self) -> TextWriterTraceListener:...
class ThreadPriorityLevel(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    AboveNormal: int
    BelowNormal: int
    Highest: int
    Idle: int
    Lowest: int
    Normal: int
    TimeCritical: int
    value__: int
class ThreadState(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Initialized: int
    Ready: int
    Running: int
    Standby: int
    Terminated: int
    Transition: int
    Unknown: int
    value__: int
    Wait: int
class ThreadWaitReason(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    EventPairHigh: int
    EventPairLow: int
    ExecutionDelay: int
    Executive: int
    FreePage: int
    LpcReceive: int
    LpcReply: int
    PageIn: int
    PageOut: int
    Suspended: int
    SystemAllocation: int
    Unknown: int
    UserRequest: int
    value__: int
    VirtualMemory: int
class Trace(object):
    @property
    def AutoFlush(self) -> bool:"""AutoFlush { get; set; } -> bool"""
    @property
    def CorrelationManager(self) -> CorrelationManager:"""CorrelationManager { get; } -> CorrelationManager"""
    @property
    def IndentLevel(self) -> int:"""IndentLevel { get; set; } -> int"""
    @property
    def IndentSize(self) -> int:"""IndentSize { get; set; } -> int"""
    @property
    def Listeners(self) -> TraceListenerCollection:"""Listeners { get; } -> TraceListenerCollection"""
    @property
    def UseGlobalLock(self) -> bool:"""UseGlobalLock { get; set; } -> bool"""
    @staticmethod
    def Assert(condition: bool, message: str, detailMessage: str):...
    @staticmethod
    def Assert(condition: bool, message: str):...
    @staticmethod
    def Assert(condition: bool):...
    @staticmethod
    def Close():...
    @staticmethod
    def Fail(message: str, detailMessage: str):...
    @staticmethod
    def Fail(message: str):...
    @staticmethod
    def Flush():...
    @staticmethod
    def Indent():...
    @staticmethod
    def Refresh():...
    @staticmethod
    def TraceError(format: str, args: _n_1_t_3[object]):...
    @staticmethod
    def TraceError(message: str):...
    @staticmethod
    def TraceInformation(format: str, args: _n_1_t_3[object]):...
    @staticmethod
    def TraceInformation(message: str):...
    @staticmethod
    def TraceWarning(format: str, args: _n_1_t_3[object]):...
    @staticmethod
    def TraceWarning(message: str):...
    @staticmethod
    def Unindent():...
    @staticmethod
    def Write(value: object, category: str):...
    @staticmethod
    def Write(message: str, category: str):...
    @staticmethod
    def Write(value: object):...
    @staticmethod
    def Write(message: str):...
    @staticmethod
    def WriteIf(condition: bool, value: object, category: str):...
    @staticmethod
    def WriteIf(condition: bool, message: str, category: str):...
    @staticmethod
    def WriteIf(condition: bool, value: object):...
    @staticmethod
    def WriteIf(condition: bool, message: str):...
    @staticmethod
    def WriteLine(value: object, category: str):...
    @staticmethod
    def WriteLine(message: str, category: str):...
    @staticmethod
    def WriteLine(value: object):...
    @staticmethod
    def WriteLine(message: str):...
    @staticmethod
    def WriteLineIf(condition: bool, value: object, category: str):...
    @staticmethod
    def WriteLineIf(condition: bool, message: str, category: str):...
    @staticmethod
    def WriteLineIf(condition: bool, value: object):...
    @staticmethod
    def WriteLineIf(condition: bool, message: str):...
class TraceEventCache(object):
    @property
    def Callstack(self) -> str:"""Callstack { get; } -> str"""
    @property
    def DateTime(self) -> _n_1_t_17:"""DateTime { get; } -> DateTime"""
    @property
    def LogicalOperationStack(self) -> _n_2_t_0:"""LogicalOperationStack { get; } -> Stack"""
    @property
    def ProcessId(self) -> int:"""ProcessId { get; } -> int"""
    @property
    def ThreadId(self) -> str:"""ThreadId { get; } -> str"""
    @property
    def Timestamp(self) -> int:"""Timestamp { get; } -> int"""
    def __init__(self) -> TraceEventCache:...
class TraceEventType(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Critical: int
    Error: int
    Information: int
    Resume: int
    Start: int
    Stop: int
    Suspend: int
    Transfer: int
    value__: int
    Verbose: int
    Warning: int
class TraceFilter(object):
    def ShouldTrace(self, cache: TraceEventCache, source: str, eventType: TraceEventType, id: int, formatOrMessage: str, args: _n_1_t_3[object], data1: object, data: _n_1_t_3[object]) -> bool:...
class TraceLevel(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Error: int
    Info: int
    Off: int
    value__: int
    Verbose: int
    Warning: int
class TraceListener(_n_1_t_21, _n_1_t_1):
    @property
    def Attributes(self) -> _n_4_t_0:"""Attributes { get; } -> StringDictionary"""
    @property
    def Filter(self) -> TraceFilter:"""Filter { get; set; } -> TraceFilter"""
    @property
    def IndentLevel(self) -> int:"""IndentLevel { get; set; } -> int"""
    @property
    def IndentSize(self) -> int:"""IndentSize { get; set; } -> int"""
    @property
    def IsThreadSafe(self) -> bool:"""IsThreadSafe { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def TraceOutputOptions(self) -> TraceOptions:"""TraceOutputOptions { get; set; } -> TraceOptions"""
    def Close(self):...
    def Fail(self, message: str, detailMessage: str):...
    def Fail(self, message: str):...
    def Flush(self):...
    def TraceData(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: _n_1_t_3[object]):...
    def TraceData(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object):...
    def TraceEvent(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, args: _n_1_t_3[object]):...
    def TraceEvent(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str):...
    def TraceEvent(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int):...
    def TraceTransfer(self, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: _n_1_t_2):...
    def Write(self, o: object, category: str):...
    def Write(self, message: str, category: str):...
    def Write(self, o: object):...
    def Write(self, message: str):...
    def WriteLine(self, o: object, category: str):...
    def WriteLine(self, message: str, category: str):...
    def WriteLine(self, o: object):...
    def WriteLine(self, message: str):...
class TraceListenerCollection(_n_2_t_2, typing.Iterable[TraceListener]):
    def AddRange(self, value: TraceListenerCollection):...
    def AddRange(self, value: _n_1_t_3[TraceListener]):...
class TraceLogRetentionOption(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    LimitedCircularFiles: int
    LimitedSequentialFiles: int
    SingleFileBoundedSize: int
    SingleFileUnboundedSize: int
    UnlimitedSequentialFiles: int
    value__: int
class TraceOptions(_n_1_t_11, _n_1_t_12, _n_1_t_13, _n_1_t_14):
    Callstack: int
    DateTime: int
    LogicalOperationStack: int
    _None: int
    ProcessId: int
    ThreadId: int
    Timestamp: int
    value__: int
class TraceSource(object):
    @property
    def Attributes(self) -> _n_4_t_0:"""Attributes { get; } -> StringDictionary"""
    @property
    def Listeners(self) -> TraceListenerCollection:"""Listeners { get; } -> TraceListenerCollection"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Switch(self) -> SourceSwitch:"""Switch { get; set; } -> SourceSwitch"""
    def __init__(self, name: str, defaultLevel: SourceLevels) -> TraceSource:...
    def __init__(self, name: str) -> TraceSource:...
    def Close(self):...
    def Flush(self):...
    def TraceData(self, eventType: TraceEventType, id: int, data: _n_1_t_3[object]):...
    def TraceData(self, eventType: TraceEventType, id: int, data: object):...
    def TraceEvent(self, eventType: TraceEventType, id: int, format: str, args: _n_1_t_3[object]):...
    def TraceEvent(self, eventType: TraceEventType, id: int, message: str):...
    def TraceEvent(self, eventType: TraceEventType, id: int):...
    def TraceInformation(self, format: str, args: _n_1_t_3[object]):...
    def TraceInformation(self, message: str):...
    def TraceTransfer(self, id: int, message: str, relatedActivityId: _n_1_t_2):...
class TraceSwitch(Switch):
    @property
    def Level(self) -> TraceLevel:"""Level { get; set; } -> TraceLevel"""
    @property
    def TraceError(self) -> bool:"""TraceError { get; } -> bool"""
    @property
    def TraceInfo(self) -> bool:"""TraceInfo { get; } -> bool"""
    @property
    def TraceVerbose(self) -> bool:"""TraceVerbose { get; } -> bool"""
    @property
    def TraceWarning(self) -> bool:"""TraceWarning { get; } -> bool"""
    def __init__(self, displayName: str, description: str, defaultSwitchValue: str) -> TraceSwitch:...
    def __init__(self, displayName: str, description: str) -> TraceSwitch:...
class UnescapedXmlDiagnosticData(object):
    @property
    def UnescapedXml(self) -> str:"""UnescapedXml { get; set; } -> str"""
    def __init__(self, xmlPayload: str) -> UnescapedXmlDiagnosticData:...
class XmlWriterTraceListener(TextWriterTraceListener, _n_1_t_1):
    def __init__(self, filename: str, name: str) -> XmlWriterTraceListener:...
    def __init__(self, filename: str) -> XmlWriterTraceListener:...
    def __init__(self, writer: _n_7_t_0, name: str) -> XmlWriterTraceListener:...
    def __init__(self, writer: _n_7_t_0) -> XmlWriterTraceListener:...
    def __init__(self, stream: _n_7_t_1, name: str) -> XmlWriterTraceListener:...
    def __init__(self, stream: _n_7_t_1) -> XmlWriterTraceListener:...
