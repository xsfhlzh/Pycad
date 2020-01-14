from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import EventArgs as _n_0_t_4
from __clrclasses__.System import MulticastDelegate as _n_0_t_5
from __clrclasses__.System import ICloneable as _n_0_t_6
from __clrclasses__.System import IntPtr as _n_0_t_7
from __clrclasses__.System import IAsyncResult as _n_0_t_8
from __clrclasses__.System import AsyncCallback as _n_0_t_9
from __clrclasses__.System import Byte as _n_0_t_10
from __clrclasses__.System import Array as _n_0_t_11
from __clrclasses__.System import Char as _n_0_t_12
from __clrclasses__.System.ComponentModel import Component as _n_1_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_1_t_1
from __clrclasses__.System.ComponentModel import IContainer as _n_1_t_2
from __clrclasses__.System.IO import Stream as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
from __clrclasses__.System.Text import Encoding as _n_4_t_0
import typing
class Handshake(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    RequestToSend: int
    RequestToSendXOnXOff: int
    value__: int
    XOnXOff: int
class Parity(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Even: int
    Mark: int
    _None: int
    Odd: int
    Space: int
    value__: int
class SerialData(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Chars: int
    Eof: int
    value__: int
class SerialDataReceivedEventArgs(_n_0_t_4):
    @property
    def EventType(self) -> SerialData:"""EventType { get; } -> SerialData"""
class SerialDataReceivedEventHandler(_n_0_t_5, _n_0_t_6, _n_3_t_0):
    def __init__(self, object: object, method: _n_0_t_7) -> SerialDataReceivedEventHandler:...
    def BeginInvoke(self, sender: object, e: SerialDataReceivedEventArgs, callback: _n_0_t_9, object: object) -> _n_0_t_8:...
    def EndInvoke(self, result: _n_0_t_8):...
    def Invoke(self, sender: object, e: SerialDataReceivedEventArgs):...
class SerialError(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Frame: int
    Overrun: int
    RXOver: int
    RXParity: int
    TXFull: int
    value__: int
class SerialErrorReceivedEventArgs(_n_0_t_4):
    @property
    def EventType(self) -> SerialError:"""EventType { get; } -> SerialError"""
class SerialErrorReceivedEventHandler(_n_0_t_5, _n_0_t_6, _n_3_t_0):
    def __init__(self, object: object, method: _n_0_t_7) -> SerialErrorReceivedEventHandler:...
    def BeginInvoke(self, sender: object, e: SerialErrorReceivedEventArgs, callback: _n_0_t_9, object: object) -> _n_0_t_8:...
    def EndInvoke(self, result: _n_0_t_8):...
    def Invoke(self, sender: object, e: SerialErrorReceivedEventArgs):...
class SerialPinChange(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Break: int
    CDChanged: int
    CtsChanged: int
    DsrChanged: int
    Ring: int
    value__: int
class SerialPinChangedEventArgs(_n_0_t_4):
    @property
    def EventType(self) -> SerialPinChange:"""EventType { get; } -> SerialPinChange"""
class SerialPinChangedEventHandler(_n_0_t_5, _n_0_t_6, _n_3_t_0):
    def __init__(self, object: object, method: _n_0_t_7) -> SerialPinChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: SerialPinChangedEventArgs, callback: _n_0_t_9, object: object) -> _n_0_t_8:...
    def EndInvoke(self, result: _n_0_t_8):...
    def Invoke(self, sender: object, e: SerialPinChangedEventArgs):...
class SerialPort(_n_1_t_0, _n_1_t_1):
    InfiniteTimeout: int
    @property
    def BaseStream(self) -> _n_2_t_0:"""BaseStream { get; } -> Stream"""
    @property
    def BaudRate(self) -> int:"""BaudRate { get; set; } -> int"""
    @property
    def BreakState(self) -> bool:"""BreakState { get; set; } -> bool"""
    @property
    def BytesToRead(self) -> int:"""BytesToRead { get; } -> int"""
    @property
    def BytesToWrite(self) -> int:"""BytesToWrite { get; } -> int"""
    @property
    def CDHolding(self) -> bool:"""CDHolding { get; } -> bool"""
    @property
    def CtsHolding(self) -> bool:"""CtsHolding { get; } -> bool"""
    @property
    def DataBits(self) -> int:"""DataBits { get; set; } -> int"""
    @property
    def DiscardNull(self) -> bool:"""DiscardNull { get; set; } -> bool"""
    @property
    def DsrHolding(self) -> bool:"""DsrHolding { get; } -> bool"""
    @property
    def DtrEnable(self) -> bool:"""DtrEnable { get; set; } -> bool"""
    @property
    def Encoding(self) -> _n_4_t_0:"""Encoding { get; set; } -> Encoding"""
    @property
    def Handshake(self) -> Handshake:"""Handshake { get; set; } -> Handshake"""
    @property
    def IsOpen(self) -> bool:"""IsOpen { get; } -> bool"""
    @property
    def NewLine(self) -> str:"""NewLine { get; set; } -> str"""
    @property
    def Parity(self) -> Parity:"""Parity { get; set; } -> Parity"""
    @property
    def ParityReplace(self) -> _n_0_t_10:"""ParityReplace { get; set; } -> Byte"""
    @property
    def PortName(self) -> str:"""PortName { get; set; } -> str"""
    @property
    def ReadBufferSize(self) -> int:"""ReadBufferSize { get; set; } -> int"""
    @property
    def ReadTimeout(self) -> int:"""ReadTimeout { get; set; } -> int"""
    @property
    def ReceivedBytesThreshold(self) -> int:"""ReceivedBytesThreshold { get; set; } -> int"""
    @property
    def RtsEnable(self) -> bool:"""RtsEnable { get; set; } -> bool"""
    @property
    def StopBits(self) -> StopBits:"""StopBits { get; set; } -> StopBits"""
    @property
    def WriteBufferSize(self) -> int:"""WriteBufferSize { get; set; } -> int"""
    @property
    def WriteTimeout(self) -> int:"""WriteTimeout { get; set; } -> int"""
    @property
    def DataReceived(self) -> SerialDataReceivedEventHandler:
        """DataReceived Event: SerialDataReceivedEventHandler"""
    @property
    def ErrorReceived(self) -> SerialErrorReceivedEventHandler:
        """ErrorReceived Event: SerialErrorReceivedEventHandler"""
    @property
    def PinChanged(self) -> SerialPinChangedEventHandler:
        """PinChanged Event: SerialPinChangedEventHandler"""
    def __init__(self, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits) -> SerialPort:...
    def __init__(self, portName: str, baudRate: int, parity: Parity, dataBits: int) -> SerialPort:...
    def __init__(self, portName: str, baudRate: int, parity: Parity) -> SerialPort:...
    def __init__(self, portName: str, baudRate: int) -> SerialPort:...
    def __init__(self, portName: str) -> SerialPort:...
    def __init__(self) -> SerialPort:...
    def __init__(self, container: _n_1_t_2) -> SerialPort:...
    def Close(self):...
    def DiscardInBuffer(self):...
    def DiscardOutBuffer(self):...
    @staticmethod
    def GetPortNames() -> _n_0_t_11[str]:...
    def Open(self):...
    def Read(self, buffer: _n_0_t_11[_n_0_t_10], offset: int, count: int) -> int:...
    def ReadByte(self) -> int:...
    def ReadChar(self) -> int:...
    def ReadExisting(self) -> str:...
    def ReadLine(self) -> str:...
    def ReadTo(self, value: str) -> str:...
    def Write(self, buffer: _n_0_t_11[_n_0_t_12], offset: int, count: int):...
    def Write(self, text: str):...
    def WriteLine(self, text: str):...
class StopBits(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    _None: int
    One: int
    OnePointFive: int
    Two: int
    value__: int
