from __clrclasses__.System import EventHandler as _n_0_t_0
from __clrclasses__.System.ComponentModel import Component as _n_1_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_1_t_1
from __clrclasses__.System.ComponentModel import AsyncCompletedEventHandler as _n_1_t_2
from __clrclasses__.System.IO import Stream as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
import typing
class SoundPlayer(_n_1_t_0, _n_1_t_1, _n_3_t_0):
    @property
    def IsLoadCompleted(self) -> bool:"""IsLoadCompleted { get; } -> bool"""
    @property
    def LoadTimeout(self) -> int:"""LoadTimeout { get; set; } -> int"""
    @property
    def SoundLocation(self) -> str:"""SoundLocation { get; set; } -> str"""
    @property
    def Stream(self) -> _n_2_t_0:"""Stream { get; set; } -> Stream"""
    @property
    def Tag(self) -> object:"""Tag { get; set; } -> object"""
    @property
    def LoadCompleted(self) -> _n_1_t_2:
        """LoadCompleted Event: AsyncCompletedEventHandler"""
    @property
    def SoundLocationChanged(self) -> _n_0_t_0:
        """SoundLocationChanged Event: EventHandler"""
    @property
    def StreamChanged(self) -> _n_0_t_0:
        """StreamChanged Event: EventHandler"""
    def __init__(self, stream: _n_2_t_0) -> SoundPlayer:...
    def __init__(self, soundLocation: str) -> SoundPlayer:...
    def __init__(self) -> SoundPlayer:...
    def Load(self):...
    def LoadAsync(self):...
    def Play(self):...
    def PlayLooping(self):...
    def PlaySync(self):...
    def Stop(self):...
class SystemSound(object):
    def Play(self):...
class SystemSounds(object):
    @property
    def Asterisk(self) -> SystemSound:"""Asterisk { get; } -> SystemSound"""
    @property
    def Beep(self) -> SystemSound:"""Beep { get; } -> SystemSound"""
    @property
    def Exclamation(self) -> SystemSound:"""Exclamation { get; } -> SystemSound"""
    @property
    def Hand(self) -> SystemSound:"""Hand { get; } -> SystemSound"""
    @property
    def Question(self) -> SystemSound:"""Question { get; } -> SystemSound"""
