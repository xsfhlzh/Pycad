from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import Document as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.EditorInput import PromptStatus as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.EditorInput import SelectionMode as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3dCollection as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import CommandFlags as _n_3_t_0
from __clrclasses__.System import ValueType as _n_4_t_0
from __clrclasses__.System import Enum as _n_4_t_1
from __clrclasses__.System import IComparable as _n_4_t_2
from __clrclasses__.System import IFormattable as _n_4_t_3
from __clrclasses__.System import IConvertible as _n_4_t_4
from __clrclasses__.System import MulticastDelegate as _n_4_t_5
from __clrclasses__.System import ICloneable as _n_4_t_6
from __clrclasses__.System import IntPtr as _n_4_t_7
from __clrclasses__.System import IAsyncResult as _n_4_t_8
from __clrclasses__.System import AsyncCallback as _n_4_t_9
from __clrclasses__.System import EventArgs as _n_4_t_10
from __clrclasses__.System.Collections import ArrayList as _n_5_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_6_t_0
import typing
class AcPiMonitorReactorImpl(_n_4_t_0):
    pass
class CommandLineMonitor(object):
    @property
    def CurrentCommandName(self) -> str:"""CurrentCommandName { get; } -> str"""
    @property
    def CurrentDoubleOut(self) -> float:"""CurrentDoubleOut { get; } -> float"""
    @property
    def CurrentInitgetFlags(self) -> int:"""CurrentInitgetFlags { get; } -> int"""
    @property
    def CurrentInitgetKeywords(self) -> str:"""CurrentInitgetKeywords { get; } -> str"""
    @property
    def CurrentInputControlFlags(self) -> InputControlFlags:"""CurrentInputControlFlags { get; } -> InputControlFlags"""
    @property
    def CurrentIntOut(self) -> int:"""CurrentIntOut { get; } -> int"""
    @property
    def CurrentKeywordsIn(self) -> str:"""CurrentKeywordsIn { get; } -> str"""
    @property
    def CurrentMode(self) -> InputModes:"""CurrentMode { get; } -> InputModes"""
    @property
    def CurrentModes(self) -> InputModes:"""CurrentModes { get; } -> InputModes"""
    @property
    def CurrentNestingCount(self) -> int:"""CurrentNestingCount { get; } -> int"""
    @property
    def CurrentPointIn(self) -> _n_4_t_0:"""CurrentPointIn { get; } -> ValueType"""
    @property
    def CurrentPointInFlag(self) -> bool:"""CurrentPointInFlag { get; } -> bool"""
    @property
    def CurrentPointOut(self) -> _n_4_t_0:"""CurrentPointOut { get; } -> ValueType"""
    @property
    def CurrentPointOut2d(self) -> _n_4_t_0:"""CurrentPointOut2d { get; } -> ValueType"""
    @property
    def CurrentPointOut2dFlag(self) -> bool:"""CurrentPointOut2dFlag { get; } -> bool"""
    @property
    def CurrentPointOutFlag(self) -> bool:"""CurrentPointOutFlag { get; } -> bool"""
    @property
    def CurrentPrompt(self) -> str:"""CurrentPrompt { get; } -> str"""
    @property
    def CurrentReturnStatus(self) -> _n_1_t_0:"""CurrentReturnStatus { get; } -> PromptStatus"""
    @property
    def CurrentSSControlsIn(self) -> str:"""CurrentSSControlsIn { get; } -> str"""
    @property
    def CurrentSSGetConsumedPickfirst(self) -> bool:"""CurrentSSGetConsumedPickfirst { get; } -> bool"""
    @property
    def CurrentSSGetCount(self) -> int:"""CurrentSSGetCount { get; } -> int"""
    @property
    def CurrentSSGetIsManual(self) -> bool:"""CurrentSSGetIsManual { get; } -> bool"""
    @property
    def CurrentSSGetKeywordsUsed(self) -> _n_5_t_0:"""CurrentSSGetKeywordsUsed { get; } -> ArrayList"""
    @property
    def CurrentStringOut(self) -> str:"""CurrentStringOut { get; } -> str"""
    @property
    def LastCommandName(self) -> str:"""LastCommandName { get; } -> str"""
    @property
    def LastNotifiedSSGetCount(self) -> int:"""LastNotifiedSSGetCount { get; } -> int"""
    @property
    def BeginSSGetCustomKeywordCallback(self) -> InputStringEventHandler:
        """BeginSSGetCustomKeywordCallback Event: InputStringEventHandler"""
    @property
    def CommandEnded(self) -> InputStringEventHandler:
        """CommandEnded Event: InputStringEventHandler"""
    @property
    def CommandWillStart(self) -> InputStringEventHandler:
        """CommandWillStart Event: InputStringEventHandler"""
    @property
    def EndSSGetCustomKeywordCallback(self) -> InputStringEventHandler:
        """EndSSGetCustomKeywordCallback Event: InputStringEventHandler"""
    @property
    def GetAngleEnded(self) -> GetAngleEventHandler:
        """GetAngleEnded Event: GetAngleEventHandler"""
    @property
    def GetAngleWillStart(self) -> GetAngleEventHandler:
        """GetAngleWillStart Event: GetAngleEventHandler"""
    @property
    def GetDistanceEnded(self) -> GetDistanceEventHandler:
        """GetDistanceEnded Event: GetDistanceEventHandler"""
    @property
    def GetDistanceWillStart(self) -> GetDistanceEventHandler:
        """GetDistanceWillStart Event: GetDistanceEventHandler"""
    @property
    def GetInput(self) -> GetInputEventHandler:
        """GetInput Event: GetInputEventHandler"""
    @property
    def PickfirstEnded(self) -> SelectEventHandler:
        """PickfirstEnded Event: SelectEventHandler"""
    @property
    def PickfirstWillStart(self) -> SelectEventHandler:
        """PickfirstWillStart Event: SelectEventHandler"""
    @property
    def SelectEnded(self) -> GetInputEventHandler:
        """SelectEnded Event: GetInputEventHandler"""
    @property
    def SelectOperation(self) -> SelectOperationEventHandler:
        """SelectOperation Event: SelectOperationEventHandler"""
    @property
    def SelectWillStart(self) -> SelectEventHandler:
        """SelectWillStart Event: SelectEventHandler"""
    @property
    def UnknownCmd(self) -> InputStringEventHandler:
        """UnknownCmd Event: InputStringEventHandler"""
    def EnableSsGetFilter(self, on: bool):...
class CommandLineMonitorServices(object):
    def ActiveCommandFlags(self) -> _n_3_t_0:...
    def CommandActiveBits(self) -> int:...
    def CommandNestedDepth(self) -> int:...
    def GetCommandLineMonitor(self, doc: _n_0_t_0) -> CommandLineMonitor:...
    def GetLocalCommandName(self, globalCmdName: str) -> str:...
    @staticmethod
    def Instance() -> CommandLineMonitorServices:...
    def IsCurrentCommandTransparent(self) -> bool:...
class GetAngleEventHandler(_n_4_t_5, _n_4_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_7) -> GetAngleEventHandler:...
    def BeginInvoke(self, sender: object, e: GetInputEventArgs, callback: _n_4_t_9, obj: object) -> _n_4_t_8:...
    def EndInvoke(self, result: _n_4_t_8):...
    def Invoke(self, sender: object, e: GetInputEventArgs):...
class GetDistanceEventHandler(_n_4_t_5, _n_4_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_7) -> GetDistanceEventHandler:...
    def BeginInvoke(self, sender: object, e: GetInputEventArgs, callback: _n_4_t_9, obj: object) -> _n_4_t_8:...
    def EndInvoke(self, result: _n_4_t_8):...
    def Invoke(self, sender: object, e: GetInputEventArgs):...
class GetInputEventArgs(_n_4_t_10):
    @property
    def Mode(self) -> InputModes:"""Mode { get; } -> InputModes"""
    @property
    def ReturnStatus(self) -> _n_1_t_0:"""ReturnStatus { get; } -> PromptStatus"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
class GetInputEventHandler(_n_4_t_5, _n_4_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_7) -> GetInputEventHandler:...
    def BeginInvoke(self, sender: object, e: GetInputEventArgs, callback: _n_4_t_9, obj: object) -> _n_4_t_8:...
    def EndInvoke(self, result: _n_4_t_8):...
    def Invoke(self, sender: object, e: GetInputEventArgs):...
class InputControlFlags(_n_4_t_1, _n_4_t_2, _n_4_t_3, _n_4_t_4):
    ud2DDIST: int
    udANYBLANK: int
    udBASE: int
    udBKSL: int
    udCURSOR: int
    udDISPLPT: int
    udDRAG: int
    udENTITY: int
    udFIRSTBLANK: int
    udFLATCUR: int
    udGETZ: int
    udIGNOREETX: int
    udKWORD: int
    udLABELOK: int
    udMSG: int
    udMSGNUM: int
    udNOLAST: int
    udNOLIM: int
    udNONE: int
    udNONEG: int
    udNOOSNAP: int
    udNOPFILT: int
    udNORANGEMSG: int
    udNOSMODE: int
    udNOZERO: int
    udNULLOK: int
    udORTHO: int
    udOTHER: int
    udPOINTOK: int
    udPOINTUP: int
    udRESCAN: int
    udSILENTETX: int
    udWNOSORT: int
    udXCTL: int
    value__: int
class InputModes(_n_4_t_1, _n_4_t_2, _n_4_t_3, _n_4_t_4):
    AllGetInput: int
    Angle: int
    Cmd: int
    Color: int
    Corner: int
    Distance: int
    Drag: int
    DynDimGetPoint: int
    EntSel: int
    Integer: int
    kword: int
    Nentsel: int
    _None: int
    Orientation: int
    Point: int
    RawAngle: int
    Real: int
    ScaleFactor: int
    ScaleFactor2: int
    SSGet: int
    String: int
    UnknownCmd: int
    value__: int
    Vector: int
class InputStringEventArgs(_n_4_t_10):
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
class InputStringEventHandler(_n_4_t_5, _n_4_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_7) -> InputStringEventHandler:...
    def BeginInvoke(self, sender: object, e: InputStringEventArgs, callback: _n_4_t_9, obj: object) -> _n_4_t_8:...
    def EndInvoke(self, result: _n_4_t_8):...
    def Invoke(self, sender: object, e: InputStringEventArgs):...
class SelectEventHandler(_n_4_t_5, _n_4_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_7) -> SelectEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_4_t_10, callback: _n_4_t_9, obj: object) -> _n_4_t_8:...
    def EndInvoke(self, result: _n_4_t_8):...
    def Invoke(self, sender: object, e: _n_4_t_10):...
class SelectOperationEventArgs(_n_4_t_10):
    @property
    def GroupName(self) -> str:"""GroupName { get; } -> str"""
    @property
    def IsAdding(self) -> bool:"""IsAdding { get; } -> bool"""
    @property
    def IsCancel(self) -> bool:"""IsCancel { get; } -> bool"""
    @property
    def IsCrossingBox(self) -> bool:"""IsCrossingBox { get; } -> bool"""
    @property
    def IsSubSelection(self) -> bool:"""IsSubSelection { get; } -> bool"""
    @property
    def Points(self) -> _n_2_t_0:"""Points { get; } -> Point3dCollection"""
    @property
    def SelectionFlags(self) -> int:"""SelectionFlags { get; } -> int"""
    @property
    def SelectionMode(self) -> _n_1_t_1:"""SelectionMode { get; } -> SelectionMode"""
class SelectOperationEventHandler(_n_4_t_5, _n_4_t_6, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_7) -> SelectOperationEventHandler:...
    def BeginInvoke(self, sender: object, e: SelectOperationEventArgs, callback: _n_4_t_9, obj: object) -> _n_4_t_8:...
    def EndInvoke(self, result: _n_4_t_8):...
    def Invoke(self, sender: object, e: SelectOperationEventArgs):...
