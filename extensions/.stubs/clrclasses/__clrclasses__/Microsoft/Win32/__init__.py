import __clrclasses__.Microsoft.Win32.SafeHandles as SafeHandles
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeRegistryHandle as _n_0_t_0
from __clrclasses__.System import EventArgs as _n_1_t_0
from __clrclasses__.System import MulticastDelegate as _n_1_t_1
from __clrclasses__.System import ICloneable as _n_1_t_2
from __clrclasses__.System import IntPtr as _n_1_t_3
from __clrclasses__.System import IAsyncResult as _n_1_t_4
from __clrclasses__.System import AsyncCallback as _n_1_t_5
from __clrclasses__.System import Enum as _n_1_t_6
from __clrclasses__.System import IComparable as _n_1_t_7
from __clrclasses__.System import IFormattable as _n_1_t_8
from __clrclasses__.System import IConvertible as _n_1_t_9
from __clrclasses__.System import MarshalByRefObject as _n_1_t_10
from __clrclasses__.System import IDisposable as _n_1_t_11
from __clrclasses__.System import Array as _n_1_t_12
from __clrclasses__.System import EventHandler as _n_1_t_13
from __clrclasses__.System import Delegate as _n_1_t_14
from __clrclasses__.System.Net import ICredentialPolicy as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
from __clrclasses__.System.Security.AccessControl import RegistrySecurity as _n_4_t_0
from __clrclasses__.System.Security.AccessControl import AccessControlSections as _n_4_t_1
from __clrclasses__.System.Security.AccessControl import RegistryRights as _n_4_t_2
import typing
class IntranetZoneCredentialPolicy(_n_2_t_0):
    def __init__(self) -> IntranetZoneCredentialPolicy:...
class PowerModeChangedEventArgs(_n_1_t_0):
    @property
    def Mode(self) -> PowerModes:"""Mode { get; } -> PowerModes"""
    def __init__(self, mode: PowerModes) -> PowerModeChangedEventArgs:...
class PowerModeChangedEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> PowerModeChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: PowerModeChangedEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: PowerModeChangedEventArgs):...
class PowerModes(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    Resume: int
    StatusChange: int
    Suspend: int
    value__: int
class Registry(object):
    ClassesRoot: int
    CurrentConfig: int
    CurrentUser: int
    DynData: int
    LocalMachine: int
    PerformanceData: int
    Users: int
    @staticmethod
    def GetValue(keyName: str, valueName: str, defaultValue: object) -> object:...
    @staticmethod
    def SetValue(keyName: str, valueName: str, value: object):...
    @staticmethod
    def SetValue(keyName: str, valueName: str, value: object, valueKind: RegistryValueKind):...
class RegistryHive(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    ClassesRoot: int
    CurrentConfig: int
    CurrentUser: int
    DynData: int
    LocalMachine: int
    PerformanceData: int
    Users: int
    value__: int
class RegistryKey(_n_1_t_10, _n_1_t_11):
    @property
    def Handle(self) -> _n_0_t_0:"""Handle { get; } -> SafeRegistryHandle"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def SubKeyCount(self) -> int:"""SubKeyCount { get; } -> int"""
    @property
    def ValueCount(self) -> int:"""ValueCount { get; } -> int"""
    @property
    def View(self) -> RegistryView:"""View { get; } -> RegistryView"""
    def Close(self):...
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: _n_4_t_0) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: _n_4_t_0) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, writable: bool, options: RegistryOptions) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, writable: bool) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:...
    def CreateSubKey(self, subkey: str) -> RegistryKey:...
    def DeleteSubKey(self, subkey: str, throwOnMissingSubKey: bool):...
    def DeleteSubKey(self, subkey: str):...
    def DeleteSubKeyTree(self, subkey: str, throwOnMissingSubKey: bool):...
    def DeleteSubKeyTree(self, subkey: str):...
    def DeleteValue(self, name: str, throwOnMissingValue: bool):...
    def DeleteValue(self, name: str):...
    def Flush(self):...
    @staticmethod
    def FromHandle(handle: _n_0_t_0, view: RegistryView) -> RegistryKey:...
    @staticmethod
    def FromHandle(handle: _n_0_t_0) -> RegistryKey:...
    def GetAccessControl(self, includeSections: _n_4_t_1) -> _n_4_t_0:...
    def GetAccessControl(self) -> _n_4_t_0:...
    def GetSubKeyNames(self) -> _n_1_t_12[str]:...
    def GetValue(self, name: str, defaultValue: object, options: RegistryValueOptions) -> object:...
    def GetValue(self, name: str, defaultValue: object) -> object:...
    def GetValue(self, name: str) -> object:...
    def GetValueKind(self, name: str) -> RegistryValueKind:...
    def GetValueNames(self) -> _n_1_t_12[str]:...
    @staticmethod
    def OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey:...
    @staticmethod
    def OpenRemoteBaseKey(hKey: RegistryHive, machineName: str, view: RegistryView) -> RegistryKey:...
    @staticmethod
    def OpenRemoteBaseKey(hKey: RegistryHive, machineName: str) -> RegistryKey:...
    def OpenSubKey(self, name: str) -> RegistryKey:...
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: _n_4_t_2) -> RegistryKey:...
    def OpenSubKey(self, name: str, rights: _n_4_t_2) -> RegistryKey:...
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey:...
    def OpenSubKey(self, name: str, writable: bool) -> RegistryKey:...
    def SetAccessControl(self, registrySecurity: _n_4_t_0):...
    def SetValue(self, name: str, value: object, valueKind: RegistryValueKind):...
    def SetValue(self, name: str, value: object):...
class RegistryKeyPermissionCheck(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    Default: int
    ReadSubTree: int
    ReadWriteSubTree: int
    value__: int
class RegistryOptions(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    _None: int
    value__: int
    Volatile: int
class RegistryValueKind(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    Binary: int
    DWord: int
    ExpandString: int
    MultiString: int
    _None: int
    QWord: int
    String: int
    Unknown: int
    value__: int
class RegistryValueOptions(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    DoNotExpandEnvironmentNames: int
    _None: int
    value__: int
class RegistryView(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    Default: int
    Registry32: int
    Registry64: int
    value__: int
class SessionEndedEventArgs(_n_1_t_0):
    @property
    def Reason(self) -> SessionEndReasons:"""Reason { get; } -> SessionEndReasons"""
    def __init__(self, reason: SessionEndReasons) -> SessionEndedEventArgs:...
class SessionEndedEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> SessionEndedEventHandler:...
    def BeginInvoke(self, sender: object, e: SessionEndedEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: SessionEndedEventArgs):...
class SessionEndingEventArgs(_n_1_t_0):
    @property
    def Cancel(self) -> bool:"""Cancel { get; set; } -> bool"""
    @property
    def Reason(self) -> SessionEndReasons:"""Reason { get; } -> SessionEndReasons"""
    def __init__(self, reason: SessionEndReasons) -> SessionEndingEventArgs:...
class SessionEndingEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> SessionEndingEventHandler:...
    def BeginInvoke(self, sender: object, e: SessionEndingEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: SessionEndingEventArgs):...
class SessionEndReasons(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    Logoff: int
    SystemShutdown: int
    value__: int
class SessionSwitchEventArgs(_n_1_t_0):
    @property
    def Reason(self) -> SessionSwitchReason:"""Reason { get; } -> SessionSwitchReason"""
    def __init__(self, reason: SessionSwitchReason) -> SessionSwitchEventArgs:...
class SessionSwitchEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> SessionSwitchEventHandler:...
    def BeginInvoke(self, sender: object, e: SessionSwitchEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: SessionSwitchEventArgs):...
class SessionSwitchReason(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    ConsoleConnect: int
    ConsoleDisconnect: int
    RemoteConnect: int
    RemoteDisconnect: int
    SessionLock: int
    SessionLogoff: int
    SessionLogon: int
    SessionRemoteControl: int
    SessionUnlock: int
    value__: int
class SystemEvents(object):
    @property
    def DisplaySettingsChanged(self) -> _n_1_t_13:
        """DisplaySettingsChanged Event: EventHandler"""
    @property
    def DisplaySettingsChanging(self) -> _n_1_t_13:
        """DisplaySettingsChanging Event: EventHandler"""
    @property
    def EventsThreadShutdown(self) -> _n_1_t_13:
        """EventsThreadShutdown Event: EventHandler"""
    @property
    def InstalledFontsChanged(self) -> _n_1_t_13:
        """InstalledFontsChanged Event: EventHandler"""
    @property
    def LowMemory(self) -> _n_1_t_13:
        """LowMemory Event: EventHandler"""
    @property
    def PaletteChanged(self) -> _n_1_t_13:
        """PaletteChanged Event: EventHandler"""
    @property
    def PowerModeChanged(self) -> PowerModeChangedEventHandler:
        """PowerModeChanged Event: PowerModeChangedEventHandler"""
    @property
    def SessionEnded(self) -> SessionEndedEventHandler:
        """SessionEnded Event: SessionEndedEventHandler"""
    @property
    def SessionEnding(self) -> SessionEndingEventHandler:
        """SessionEnding Event: SessionEndingEventHandler"""
    @property
    def SessionSwitch(self) -> SessionSwitchEventHandler:
        """SessionSwitch Event: SessionSwitchEventHandler"""
    @property
    def TimeChanged(self) -> _n_1_t_13:
        """TimeChanged Event: EventHandler"""
    @property
    def TimerElapsed(self) -> TimerElapsedEventHandler:
        """TimerElapsed Event: TimerElapsedEventHandler"""
    @property
    def UserPreferenceChanged(self) -> UserPreferenceChangedEventHandler:
        """UserPreferenceChanged Event: UserPreferenceChangedEventHandler"""
    @property
    def UserPreferenceChanging(self) -> UserPreferenceChangingEventHandler:
        """UserPreferenceChanging Event: UserPreferenceChangingEventHandler"""
    @staticmethod
    def CreateTimer(interval: int) -> _n_1_t_3:...
    @staticmethod
    def InvokeOnEventsThread(method: _n_1_t_14):...
    @staticmethod
    def KillTimer(timerId: _n_1_t_3):...
class TimerElapsedEventArgs(_n_1_t_0):
    @property
    def TimerId(self) -> _n_1_t_3:"""TimerId { get; } -> IntPtr"""
    def __init__(self, timerId: _n_1_t_3) -> TimerElapsedEventArgs:...
class TimerElapsedEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> TimerElapsedEventHandler:...
    def BeginInvoke(self, sender: object, e: TimerElapsedEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: TimerElapsedEventArgs):...
class UserPreferenceCategory(_n_1_t_6, _n_1_t_7, _n_1_t_8, _n_1_t_9):
    Accessibility: int
    Color: int
    Desktop: int
    General: int
    Icon: int
    Keyboard: int
    Locale: int
    Menu: int
    Mouse: int
    Policy: int
    Power: int
    Screensaver: int
    value__: int
    VisualStyle: int
    Window: int
class UserPreferenceChangedEventArgs(_n_1_t_0):
    @property
    def Category(self) -> UserPreferenceCategory:"""Category { get; } -> UserPreferenceCategory"""
    def __init__(self, category: UserPreferenceCategory) -> UserPreferenceChangedEventArgs:...
class UserPreferenceChangedEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> UserPreferenceChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: UserPreferenceChangedEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: UserPreferenceChangedEventArgs):...
class UserPreferenceChangingEventArgs(_n_1_t_0):
    @property
    def Category(self) -> UserPreferenceCategory:"""Category { get; } -> UserPreferenceCategory"""
    def __init__(self, category: UserPreferenceCategory) -> UserPreferenceChangingEventArgs:...
class UserPreferenceChangingEventHandler(_n_1_t_1, _n_1_t_2, _n_3_t_0):
    def __init__(self, object: object, method: _n_1_t_3) -> UserPreferenceChangingEventHandler:...
    def BeginInvoke(self, sender: object, e: UserPreferenceChangingEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
    def EndInvoke(self, result: _n_1_t_4):...
    def Invoke(self, sender: object, e: UserPreferenceChangingEventArgs):...
