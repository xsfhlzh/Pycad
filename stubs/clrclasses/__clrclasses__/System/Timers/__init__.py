from __clrclasses__.System import EventArgs as _n_0_t_0
from __clrclasses__.System import DateTime as _n_0_t_1
from __clrclasses__.System import MulticastDelegate as _n_0_t_2
from __clrclasses__.System import ICloneable as _n_0_t_3
from __clrclasses__.System import IntPtr as _n_0_t_4
from __clrclasses__.System import IAsyncResult as _n_0_t_5
from __clrclasses__.System import AsyncCallback as _n_0_t_6
from __clrclasses__.System.ComponentModel import Component as _n_1_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_1_t_1
from __clrclasses__.System.ComponentModel import ISupportInitialize as _n_1_t_2
from __clrclasses__.System.ComponentModel import ISynchronizeInvoke as _n_1_t_3
from __clrclasses__.System.ComponentModel import DescriptionAttribute as _n_1_t_4
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
import typing
class ElapsedEventArgs(_n_0_t_0):
    @property
    def SignalTime(self) -> _n_0_t_1:"""SignalTime { get; } -> DateTime"""
class ElapsedEventHandler(_n_0_t_2, _n_0_t_3, _n_3_t_0):
    def __init__(self, object: object, method: _n_0_t_4) -> ElapsedEventHandler:...
    def BeginInvoke(self, sender: object, e: ElapsedEventArgs, callback: _n_0_t_6, object: object) -> _n_0_t_5:...
    def EndInvoke(self, result: _n_0_t_5):...
    def Invoke(self, sender: object, e: ElapsedEventArgs):...
class Timer(_n_1_t_0, _n_1_t_1, _n_1_t_2):
    @property
    def AutoReset(self) -> bool:"""AutoReset { get; set; } -> bool"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def Interval(self) -> float:"""Interval { get; set; } -> float"""
    @property
    def SynchronizingObject(self) -> _n_1_t_3:"""SynchronizingObject { get; set; } -> ISynchronizeInvoke"""
    @property
    def Elapsed(self) -> ElapsedEventHandler:
        """Elapsed Event: ElapsedEventHandler"""
    def __init__(self, interval: float) -> Timer:...
    def __init__(self) -> Timer:...
    def Close(self):...
    def Start(self):...
    def Stop(self):...
class TimersDescriptionAttribute(_n_1_t_4, _n_2_t_0):
    def __init__(self, description: str) -> TimersDescriptionAttribute:...
