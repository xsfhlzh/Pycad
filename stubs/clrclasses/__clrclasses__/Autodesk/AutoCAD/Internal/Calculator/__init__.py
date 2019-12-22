from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_0_t_0
from __clrclasses__.System import Enum as _n_1_t_0
from __clrclasses__.System import IComparable as _n_1_t_1
from __clrclasses__.System import IFormattable as _n_1_t_2
from __clrclasses__.System import IConvertible as _n_1_t_3
from __clrclasses__.System import IDisposable as _n_1_t_4
from __clrclasses__.System import ValueType as _n_1_t_5
from __clrclasses__.System import EventArgs as _n_1_t_6
from __clrclasses__.System import MulticastDelegate as _n_1_t_7
from __clrclasses__.System import ICloneable as _n_1_t_8
from __clrclasses__.System import IntPtr as _n_1_t_9
from __clrclasses__.System import IAsyncResult as _n_1_t_10
from __clrclasses__.System import AsyncCallback as _n_1_t_11
from __clrclasses__.System.Collections import IEnumerable as _n_2_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_2_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
import typing
class AngleUnitsEnum(_n_1_t_0, _n_1_t_1, _n_1_t_2, _n_1_t_3):
    Degree: int
    DegreeMinSec: int
    Grad: int
    _None: int
    Radian: int
    Surveyor: int
    value__: int
class CalcContext(_n_0_t_0, _n_1_t_4):
    @property
    def AngleUnits(self) -> AngleUnitsEnum:"""AngleUnits { get; set; } -> AngleUnitsEnum"""
    @property
    def HostServices(self) -> CalcHostServices:"""HostServices { get; } -> CalcHostServices"""
    def __init__(self) -> CalcContext:...
class CalcEngine(_n_0_t_0, _n_1_t_4):
    @property
    def GlobalVariableCollection(self) -> CalcGlobalVariableBag:"""GlobalVariableCollection { get; } -> CalcGlobalVariableBag"""
    @property
    def GlobalVariableServices(self) -> CalcGlobalVariableServices:"""GlobalVariableServices { get; set; } -> CalcGlobalVariableServices"""
    def AddGlobalVariable(self, variableName: str, variableValue: CalcValueType) -> bool:...
    def EvaluateExpression(self, expression: str, context: CalcContext, result: CalcResult) -> bool:...
    def EvaluateExpressionDisableSnap(self, expression: str, context: CalcContext, result: CalcResult) -> bool:...
    @staticmethod
    def GetEngine() -> CalcEngine:...
    def RemoveGlobalVariable(self, variableName: str) -> bool:...
class CalcGlobalVariableBag(_n_0_t_0, _n_1_t_4, _n_2_t_0, _n_2_t_1):
    def __init__(self, pvars: object) -> CalcGlobalVariableBag:...
class CalcGlobalVariableServices(_n_0_t_0, _n_1_t_4):
    @property
    def GlobalVariableModifiedEvent(self) -> OnGlobalVariableModifiedHandler:"""GlobalVariableModifiedEvent { get; set; } -> OnGlobalVariableModifiedHandler"""
    def __init__(self) -> CalcGlobalVariableServices:...
class CalcHostServices(_n_0_t_0, _n_1_t_4):
    @property
    def FuncEpilogEvent(self) -> OnInteractiveFunctionEpilogEventHandler:"""FuncEpilogEvent { get; set; } -> OnInteractiveFunctionEpilogEventHandler"""
    @property
    def FuncPrologEvent(self) -> OnInteractiveFunctionPrologEventHandler:"""FuncPrologEvent { get; set; } -> OnInteractiveFunctionPrologEventHandler"""
    @property
    def WriteStringEvent(self) -> OnWriteStringEventHandler:"""WriteStringEvent { get; set; } -> OnWriteStringEventHandler"""
    def __init__(self) -> CalcHostServices:...
    def SetQCState(self, value: bool):...
class CalcResult(_n_0_t_0, _n_1_t_4):
    @property
    def DWGResultString(self) -> str:"""DWGResultString { get; } -> str"""
    @property
    def Result(self) -> CalcValueType:"""Result { get; set; } -> CalcValueType"""
    @property
    def ResultString(self) -> str:"""ResultString { get; } -> str"""
    @property
    def Type(self) -> ValueTypeEnum:"""Type { get; set; } -> ValueTypeEnum"""
    def __init__(self, Value: CalcValueType) -> CalcResult:...
class CalcValueType(_n_1_t_5):
    @property
    def DistanceUnit(self) -> float:"""DistanceUnit { get; set; } -> float"""
    @property
    def DistanceUnitType(self) -> object:"""DistanceUnitType { get; } -> object"""
    @property
    def R(self) -> float:"""R { get; set; } -> float"""
    @property
    def Type(self) -> ValueTypeEnum:"""Type { get; set; } -> ValueTypeEnum"""
    @property
    def V(self) -> XYZPoint:"""V { get; set; } -> XYZPoint"""
    @staticmethod
    def Parse(string: str) -> CalcValueType:...
class FuncPrologEpilogEventArgs(_n_1_t_6):
    FuncName: int
    Result: int
    def __init__(self, FuncName: str, Result: CalcResult) -> FuncPrologEpilogEventArgs:...
class GlobalVariable(_n_0_t_0, _n_1_t_4):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> CalcValueType:"""Value { get; } -> CalcValueType"""
    def __init__(self, umgd: object) -> GlobalVariable:...
class GlobalVariableEventArgs(_n_1_t_6):
    IsNewVariable: int
    VariableName: int
    VariableValue: int
    def __init__(self, VariableName: str, VariableValue: CalcValueType, IsNewVariable: bool) -> GlobalVariableEventArgs:...
class IOStringEventArgs(_n_1_t_6):
    @property
    def IOString(self) -> str:"""IOString { get; set; } -> str"""
    def __init__(self, IOString: str) -> IOStringEventArgs:...
class OnGlobalVariableModifiedHandler(_n_1_t_7, _n_1_t_8, _n_3_t_0):
    def __init__(self, A_0: object, A_1: _n_1_t_9) -> OnGlobalVariableModifiedHandler:...
    def BeginInvoke(self, e: GlobalVariableEventArgs, callback: _n_1_t_11, obj: object) -> _n_1_t_10:...
    def EndInvoke(self, result: _n_1_t_10):...
    def Invoke(self, e: GlobalVariableEventArgs):...
class OnInteractiveFunctionEpilogEventHandler(_n_1_t_7, _n_1_t_8, _n_3_t_0):
    def __init__(self, A_0: object, A_1: _n_1_t_9) -> OnInteractiveFunctionEpilogEventHandler:...
    def BeginInvoke(self, e: FuncPrologEpilogEventArgs, callback: _n_1_t_11, obj: object) -> _n_1_t_10:...
    def EndInvoke(self, result: _n_1_t_10):...
    def Invoke(self, e: FuncPrologEpilogEventArgs):...
class OnInteractiveFunctionPrologEventHandler(_n_1_t_7, _n_1_t_8, _n_3_t_0):
    def __init__(self, A_0: object, A_1: _n_1_t_9) -> OnInteractiveFunctionPrologEventHandler:...
    def BeginInvoke(self, e: FuncPrologEpilogEventArgs, callback: _n_1_t_11, obj: object) -> _n_1_t_10:...
    def EndInvoke(self, result: _n_1_t_10):...
    def Invoke(self, e: FuncPrologEpilogEventArgs):...
class OnWriteStringEventHandler(_n_1_t_7, _n_1_t_8, _n_3_t_0):
    def __init__(self, A_0: object, A_1: _n_1_t_9) -> OnWriteStringEventHandler:...
    def BeginInvoke(self, e: IOStringEventArgs, callback: _n_1_t_11, obj: object) -> _n_1_t_10:...
    def EndInvoke(self, result: _n_1_t_10):...
    def Invoke(self, e: IOStringEventArgs):...
class Unit(_n_1_t_5):
    m_Distance: int
    m_DistanceUnitType: int
    def __init__(self) -> Unit:...
class ValueTypeEnum(_n_1_t_0, _n_1_t_1, _n_1_t_2, _n_1_t_3):
    IntType: int
    NoType: int
    RealType: int
    value__: int
    VectorType: int
class XYZPoint(_n_1_t_5):
    @property
    def X(self) -> float:"""X { get; set; } -> float"""
    @property
    def Y(self) -> float:"""Y { get; set; } -> float"""
    @property
    def Z(self) -> float:"""Z { get; set; } -> float"""
    def __init__(self, X: float, Y: float, Z: float) -> XYZPoint:...
