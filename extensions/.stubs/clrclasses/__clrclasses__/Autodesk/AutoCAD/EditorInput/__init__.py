from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import Document as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import FullSubentityPath as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ResultBuffer as _n_1_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ViewTableRecord as _n_1_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DBObjectCollection as _n_1_t_5
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import CustomObjectSnapMode as _n_1_t_6
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import TypedValue as _n_1_t_7
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3d as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3dCollection as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.Geometry import Curve3d as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.Geometry import Tolerance as _n_2_t_5
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ImageBGRA32 as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ViewportDraw as _n_3_t_1
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import Drawable as _n_3_t_2
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_4_t_0
from __clrclasses__.System import IDisposable as _n_5_t_0
from __clrclasses__.System import ICloneable as _n_5_t_1
from __clrclasses__.System import Array as _n_5_t_2
from __clrclasses__.System import IntPtr as _n_5_t_3
from __clrclasses__.System import Enum as _n_5_t_4
from __clrclasses__.System import IComparable as _n_5_t_5
from __clrclasses__.System import IFormattable as _n_5_t_6
from __clrclasses__.System import IConvertible as _n_5_t_7
from __clrclasses__.System import EventArgs as _n_5_t_8
from __clrclasses__.System import MulticastDelegate as _n_5_t_9
from __clrclasses__.System import IAsyncResult as _n_5_t_10
from __clrclasses__.System import AsyncCallback as _n_5_t_11
from __clrclasses__.System import MarshalByRefObject as _n_5_t_12
from __clrclasses__.System import EventHandler as _n_5_t_13
from __clrclasses__.System import Delegate as _n_5_t_14
from __clrclasses__.System import ValueType as _n_5_t_15
from __clrclasses__.System import Type as _n_5_t_16
from __clrclasses__.System.Collections import ICollection as _n_6_t_0
from __clrclasses__.System.ComponentModel import PropertyDescriptor as _n_7_t_0
from __clrclasses__.System.Drawing import Point as _n_8_t_0
from __clrclasses__.System.Runtime.CompilerServices import INotifyCompletion as _n_9_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_10_t_0
from __clrclasses__.System.Windows import Point as _n_11_t_0
from __clrclasses__.System.Windows import Window as _n_11_t_1
from __clrclasses__.System.Windows.Forms import Control as _n_12_t_0
import typing
class Camera(_n_1_t_0, _n_5_t_0, _n_5_t_1):
    @property
    def BackClipDistance(self) -> float:"""BackClipDistance { get; } -> float"""
    @property
    def BackClipEnabled(self) -> bool:"""BackClipEnabled { get; } -> bool"""
    @property
    def FieldOfView(self) -> float:"""FieldOfView { get; } -> float"""
    @property
    def FrontClipDistance(self) -> float:"""FrontClipDistance { get; } -> float"""
    @property
    def FrontClipEnabled(self) -> bool:"""FrontClipEnabled { get; } -> bool"""
    @property
    def IsCameraPlottable(self) -> bool:"""IsCameraPlottable { get; } -> bool"""
    @property
    def LensLength(self) -> float:"""LensLength { get; } -> float"""
    @property
    def Position(self) -> _n_2_t_0:"""Position { get; } -> Point3d"""
    @property
    def Target(self) -> _n_2_t_0:"""Target { get; } -> Point3d"""
    @property
    def ViewId(self) -> _n_1_t_1:"""ViewId { get; } -> ObjectId"""
    @property
    def ViewTwist(self) -> float:"""ViewTwist { get; } -> float"""
class ConstraintUtilities(object):
    def __init__(self) -> ConstraintUtilities:...
    @staticmethod
    def ShowConstraintBar(subentityPaths: _n_5_t_2[_n_1_t_2], bToShow: bool) -> bool:...
class CrossingOrWindowSelectedObject(SelectedObject):
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: int) -> CrossingOrWindowSelectedObject:...
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: _n_5_t_3) -> CrossingOrWindowSelectedObject:...
    def GetPickPoints(self) -> _n_5_t_2[PickPointDescriptor]:...
class CrossingOrWindowSelectedSubObject(SelectedSubObject):
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: int) -> CrossingOrWindowSelectedSubObject:...
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: _n_5_t_3) -> CrossingOrWindowSelectedSubObject:...
    def GetPickPoints(self) -> _n_5_t_2[PickPointDescriptor]:...
class CursorBadgeUtilities(object):
    def __init__(self) -> CursorBadgeUtilities:...
    def AddSupplementalCursorImage(self, cursorImage: _n_3_t_0, priority: int) -> bool:...
    def GetSupplementalCursorOffset(self, x: int, y: int):...
    def HasSupplementalCursorImage(self) -> bool:...
    def RemoveSupplementalCursorImage(self, cursorImage: _n_3_t_0) -> bool:...
    def SetSupplementalCursorOffset(self, x: int, y: int):...
class CursorType(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Crosshair: int
    CrosshairNoRotate: int
    EntitySelect: int
    EntitySelectNoPerspective: int
    Invisible: int
    NoSpecialCursor: int
    NotRotated: int
    Parallelogram: int
    PickfirstOrGrips: int
    RectangularCursor: int
    RotatedCrosshair: int
    RubberBand: int
    TargetBox: int
    value__: int
class DeviceInputEventArgs(_n_5_t_8):
    @property
    def GraphicsSystemMarker(self) -> _n_5_t_3:"""GraphicsSystemMarker { get; } -> IntPtr"""
    @property
    def Handled(self) -> bool:"""Handled { get; set; } -> bool"""
    @property
    def LParam(self) -> _n_5_t_3:"""LParam { get; } -> IntPtr"""
    @property
    def Message(self) -> int:"""Message { get; } -> int"""
    @property
    def WParam(self) -> _n_5_t_3:"""WParam { get; } -> IntPtr"""
class DeviceInputEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> DeviceInputEventHandler:...
    def BeginInvoke(self, sender: object, e: DeviceInputEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: DeviceInputEventArgs):...
class DisposableSelectionSet(_n_5_t_0):
    def __init__(self, selectionSet: SelectionSetDelayMarshalled) -> DisposableSelectionSet:...
class DragCallback(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> DragCallback:...
    def BeginInvoke(self, current: _n_2_t_0, xform: _n_2_t_1, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10) -> SamplerStatus:...
    def Invoke(self, current: _n_2_t_0, xform: _n_2_t_1) -> SamplerStatus:...
class DragCursor(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    _None: int
    Normal: int
    Selection: int
    value__: int
class DraggingEndedEventArgs(_n_5_t_8):
    @property
    def Offset(self) -> _n_2_t_2:"""Offset { get; } -> Vector3d"""
    @property
    def PickPoint(self) -> _n_2_t_0:"""PickPoint { get; } -> Point3d"""
    @property
    def Status(self) -> PromptStatus:"""Status { get; } -> PromptStatus"""
class DraggingEndedEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> DraggingEndedEventHandler:...
    def BeginInvoke(self, sender: object, e: DraggingEndedEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: DraggingEndedEventArgs):...
class DraggingEventArgs(_n_5_t_8):
    @property
    def Prompt(self) -> str:"""Prompt { get; } -> str"""
    def __init__(self, prompt: str) -> DraggingEventArgs:...
class DraggingEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> DraggingEventHandler:...
    def BeginInvoke(self, sender: object, e: DraggingEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: DraggingEventArgs):...
class DrawJig(Jig):
    pass
class Editor(_n_5_t_12):
    PauseToken: int
    @property
    def ActiveViewportId(self) -> _n_1_t_1:"""ActiveViewportId { get; } -> ObjectId"""
    @property
    def CurrentUserCoordinateSystem(self) -> _n_2_t_1:"""CurrentUserCoordinateSystem { get; set; } -> Matrix3d"""
    @property
    def CurrentViewportObjectId(self) -> _n_1_t_1:"""CurrentViewportObjectId { get; } -> ObjectId"""
    @property
    def Document(self) -> _n_0_t_0:"""Document { get; } -> Document"""
    @property
    def IsDragging(self) -> bool:"""IsDragging { get; } -> bool"""
    @property
    def IsQuiescent(self) -> bool:"""IsQuiescent { get; } -> bool"""
    @property
    def IsQuiescentForTransparentCommand(self) -> bool:"""IsQuiescentForTransparentCommand { get; } -> bool"""
    @property
    def MouseHasMoved(self) -> bool:"""MouseHasMoved { get; } -> bool"""
    @property
    def UseCommandLineInterface(self) -> bool:"""UseCommandLineInterface { get; } -> bool"""
    @property
    def Dragging(self) -> DraggingEventHandler:
        """Dragging Event: DraggingEventHandler"""
    @property
    def DraggingEnded(self) -> DraggingEndedEventHandler:
        """DraggingEnded Event: DraggingEndedEventHandler"""
    @property
    def EnteringQuiescentState(self) -> _n_5_t_13:
        """EnteringQuiescentState Event: EventHandler"""
    @property
    def LeavingQuiescentState(self) -> _n_5_t_13:
        """LeavingQuiescentState Event: EventHandler"""
    @property
    def PointFilter(self) -> PointFilterEventHandler:
        """PointFilter Event: PointFilterEventHandler"""
    @property
    def PointMonitor(self) -> PointMonitorEventHandler:
        """PointMonitor Event: PointMonitorEventHandler"""
    @property
    def PromptedForAngle(self) -> PromptDoubleResultEventHandler:
        """PromptedForAngle Event: PromptDoubleResultEventHandler"""
    @property
    def PromptedForCorner(self) -> PromptPointResultEventHandler:
        """PromptedForCorner Event: PromptPointResultEventHandler"""
    @property
    def PromptedForDistance(self) -> PromptDoubleResultEventHandler:
        """PromptedForDistance Event: PromptDoubleResultEventHandler"""
    @property
    def PromptedForDouble(self) -> PromptDoubleResultEventHandler:
        """PromptedForDouble Event: PromptDoubleResultEventHandler"""
    @property
    def PromptedForEntity(self) -> PromptEntityResultEventHandler:
        """PromptedForEntity Event: PromptEntityResultEventHandler"""
    @property
    def PromptedForInteger(self) -> PromptIntegerResultEventHandler:
        """PromptedForInteger Event: PromptIntegerResultEventHandler"""
    @property
    def PromptedForKeyword(self) -> PromptStringResultEventHandler:
        """PromptedForKeyword Event: PromptStringResultEventHandler"""
    @property
    def PromptedForNestedEntity(self) -> PromptNestedEntityResultEventHandler:
        """PromptedForNestedEntity Event: PromptNestedEntityResultEventHandler"""
    @property
    def PromptedForPoint(self) -> PromptPointResultEventHandler:
        """PromptedForPoint Event: PromptPointResultEventHandler"""
    @property
    def PromptedForSelection(self) -> PromptSelectionResultEventHandler:
        """PromptedForSelection Event: PromptSelectionResultEventHandler"""
    @property
    def PromptedForString(self) -> PromptStringResultEventHandler:
        """PromptedForString Event: PromptStringResultEventHandler"""
    @property
    def PromptForEntityEnding(self) -> PromptForEntityEndingEventHandler:
        """PromptForEntityEnding Event: PromptForEntityEndingEventHandler"""
    @property
    def PromptForSelectionEnding(self) -> PromptForSelectionEndingEventHandler:
        """PromptForSelectionEnding Event: PromptForSelectionEndingEventHandler"""
    @property
    def PromptingForAngle(self) -> PromptAngleOptionsEventHandler:
        """PromptingForAngle Event: PromptAngleOptionsEventHandler"""
    @property
    def PromptingForCorner(self) -> PromptPointOptionsEventHandler:
        """PromptingForCorner Event: PromptPointOptionsEventHandler"""
    @property
    def PromptingForDistance(self) -> PromptDistanceOptionsEventHandler:
        """PromptingForDistance Event: PromptDistanceOptionsEventHandler"""
    @property
    def PromptingForDouble(self) -> PromptDoubleOptionsEventHandler:
        """PromptingForDouble Event: PromptDoubleOptionsEventHandler"""
    @property
    def PromptingForEntity(self) -> PromptEntityOptionsEventHandler:
        """PromptingForEntity Event: PromptEntityOptionsEventHandler"""
    @property
    def PromptingForInteger(self) -> PromptIntegerOptionsEventHandler:
        """PromptingForInteger Event: PromptIntegerOptionsEventHandler"""
    @property
    def PromptingForKeyword(self) -> PromptKeywordOptionsEventHandler:
        """PromptingForKeyword Event: PromptKeywordOptionsEventHandler"""
    @property
    def PromptingForNestedEntity(self) -> PromptNestedEntityOptionsEventHandler:
        """PromptingForNestedEntity Event: PromptNestedEntityOptionsEventHandler"""
    @property
    def PromptingForPoint(self) -> PromptPointOptionsEventHandler:
        """PromptingForPoint Event: PromptPointOptionsEventHandler"""
    @property
    def PromptingForSelection(self) -> PromptSelectionOptionsEventHandler:
        """PromptingForSelection Event: PromptSelectionOptionsEventHandler"""
    @property
    def PromptingForString(self) -> PromptStringOptionsEventHandler:
        """PromptingForString Event: PromptStringOptionsEventHandler"""
    @property
    def Rollover(self) -> RolloverEventHandler:
        """Rollover Event: RolloverEventHandler"""
    @property
    def SelectionAdded(self) -> SelectionAddedEventHandler:
        """SelectionAdded Event: SelectionAddedEventHandler"""
    @property
    def SelectionRemoved(self) -> SelectionRemovedEventHandler:
        """SelectionRemoved Event: SelectionRemovedEventHandler"""
    def ApplyCurDwgLayerTableChanges(self):...
    def Command(self, parameter: _n_5_t_2[object]):...
    def CommandAsync(self, parameter: _n_5_t_2[object]) -> Editor.CommandResult:...
    def DoPrompt(self, opt: PromptOptions) -> PromptResult:...
    def Drag(self, jig: Jig) -> PromptResult:...
    def Drag(self, selection: SelectionSet, message: str, callback: DragCallback) -> PromptPointResult:...
    def Drag(self, options: PromptDragOptions) -> PromptPointResult:...
    def DrawVector(self, _from: _n_2_t_0, to: _n_2_t_0, color: int, drawHighlighted: bool):...
    def DrawVectors(self, rb: _n_1_t_3, transform: _n_2_t_1):...
    def GetAngle(self, message: str) -> PromptDoubleResult:...
    def GetAngle(self, options: PromptAngleOptions) -> PromptDoubleResult:...
    def GetCommandVersion(self) -> int:...
    def GetCorner(self, message: str, basePoint: _n_2_t_0) -> PromptPointResult:...
    def GetCorner(self, options: PromptCornerOptions) -> PromptPointResult:...
    def GetCurrentView(self) -> _n_1_t_4:...
    def GetDistance(self, message: str) -> PromptDoubleResult:...
    def GetDistance(self, options: PromptDistanceOptions) -> PromptDoubleResult:...
    def GetDouble(self, message: str) -> PromptDoubleResult:...
    def GetDouble(self, options: PromptDoubleOptions) -> PromptDoubleResult:...
    def GetEntity(self, message: str) -> PromptEntityResult:...
    def GetEntity(self, options: PromptEntityOptions) -> PromptEntityResult:...
    def GetFileNameForOpen(self, message: str) -> PromptFileNameResult:...
    def GetFileNameForOpen(self, options: PromptOpenFileOptions) -> PromptFileNameResult:...
    def GetFileNameForSave(self, message: str) -> PromptFileNameResult:...
    def GetFileNameForSave(self, options: PromptSaveFileOptions) -> PromptFileNameResult:...
    def GetInteger(self, message: str) -> PromptIntegerResult:...
    def GetInteger(self, options: PromptIntegerOptions) -> PromptIntegerResult:...
    def GetKeywords(self, message: str, globalKeywords: _n_5_t_2[str]) -> PromptResult:...
    def GetKeywords(self, options: PromptKeywordOptions) -> PromptResult:...
    def GetNestedEntity(self, message: str) -> PromptNestedEntityResult:...
    def GetNestedEntity(self, options: PromptNestedEntityOptions) -> PromptNestedEntityResult:...
    def GetPoint(self, message: str) -> PromptPointResult:...
    def GetPoint(self, options: PromptPointOptions) -> PromptPointResult:...
    def GetSelection(self) -> PromptSelectionResult:...
    def GetSelection(self, filter: SelectionFilter) -> PromptSelectionResult:...
    def GetSelection(self, options: PromptSelectionOptions) -> PromptSelectionResult:...
    def GetSelection(self, options: PromptSelectionOptions, filter: SelectionFilter) -> PromptSelectionResult:...
    def GetString(self, message: str) -> PromptResult:...
    def GetString(self, options: PromptStringOptions) -> PromptResult:...
    def GetViewportNumber(self, point: _n_11_t_0) -> int:...
    def GetViewportNumber(self, point: _n_8_t_0) -> int:
        """Extension from: Autodesk.AutoCAD.EditorInput.EditorExtension"""
    def InitCommandVersion(self, nVersion: int) -> int:...
    def PointToScreen(self, pt: _n_2_t_0, viewportNumber: int) -> _n_11_t_0:...
    def PointToScreen(self, pt: _n_2_t_0, viewportNumber: int) -> _n_8_t_0:
        """Extension from: Autodesk.AutoCAD.EditorInput.EditorExtension"""
    def PointToWorld(self, pt: _n_11_t_0) -> _n_2_t_0:...
    def PointToWorld(self, pt: _n_11_t_0, viewportNumber: int) -> _n_2_t_0:...
    def PointToWorld(self, pt: _n_8_t_0, viewportNumber: int) -> _n_2_t_0:
        """Extension from: Autodesk.AutoCAD.EditorInput.EditorExtension"""
    def PointToWorld(self, pt: _n_8_t_0) -> _n_2_t_0:
        """Extension from: Autodesk.AutoCAD.EditorInput.EditorExtension"""
    def PostCommandPrompt(self):...
    def Regen(self):...
    def SelectAll(self) -> PromptSelectionResult:...
    def SelectAll(self, filter: SelectionFilter) -> PromptSelectionResult:...
    def SelectCrossingPolygon(self, polygon: _n_2_t_3) -> PromptSelectionResult:...
    def SelectCrossingPolygon(self, polygon: _n_2_t_3, filter: SelectionFilter) -> PromptSelectionResult:...
    def SelectCrossingWindow(self, pt1: _n_2_t_0, pt2: _n_2_t_0) -> PromptSelectionResult:...
    def SelectCrossingWindow(self, pt1: _n_2_t_0, pt2: _n_2_t_0, filter: SelectionFilter) -> PromptSelectionResult:...
    def SelectCrossingWindow(self, pt1: _n_2_t_0, pt2: _n_2_t_0, filter: SelectionFilter, forceSubEntitySelection: bool) -> PromptSelectionResult:...
    def SelectFence(self, fence: _n_2_t_3) -> PromptSelectionResult:...
    def SelectFence(self, fence: _n_2_t_3, filter: SelectionFilter) -> PromptSelectionResult:...
    def SelectImplied(self) -> PromptSelectionResult:...
    def SelectLast(self) -> PromptSelectionResult:...
    def SelectPrevious(self) -> PromptSelectionResult:...
    def SelectWindow(self, pt1: _n_2_t_0, pt2: _n_2_t_0) -> PromptSelectionResult:...
    def SelectWindow(self, pt1: _n_2_t_0, pt2: _n_2_t_0, filter: SelectionFilter) -> PromptSelectionResult:...
    def SelectWindowPolygon(self, polygon: _n_2_t_3) -> PromptSelectionResult:...
    def SelectWindowPolygon(self, polygon: _n_2_t_3, filter: SelectionFilter) -> PromptSelectionResult:...
    def SetCurrentView(self, value: _n_1_t_4):...
    def SetImpliedSelection(self, selectedObjects: _n_5_t_2[_n_1_t_1]):...
    def SetImpliedSelection(self, selectionSet: SelectionSet):...
    def Snap(self, snapMode: str, input: _n_2_t_0) -> _n_2_t_0:...
    def StartUserInteraction(self, window: _n_11_t_1) -> EditorUserInteraction:...
    def StartUserInteraction(self, hwnd: _n_5_t_3) -> EditorUserInteraction:...
    def StartUserInteraction(self, modalForm: _n_12_t_0) -> EditorUserInteraction:
        """Extension from: Autodesk.AutoCAD.EditorInput.EditorExtension"""
    def SwitchToModelSpace(self):...
    def SwitchToPaperSpace(self):...
    def TraceBoundary(self, seedPoint: _n_2_t_0, detectIslands: bool) -> _n_1_t_5:...
    def TurnForcedPickOff(self) -> int:...
    def TurnForcedPickOn(self) -> int:...
    def TurnSubentityWindowSelectionOff(self):...
    def TurnSubentityWindowSelectionOn(self):...
    def UpdateScreen(self):...
    def UpdateTiledViewportsFromDatabase(self):...
    def UpdateTiledViewportsInDatabase(self):...
    def ViewportIdFromNumber(self, viewportNumber: int) -> _n_1_t_1:...
    def WriteMessage(self, message: str):...
    def WriteMessage(self, message: str, parameter: _n_5_t_2[object]):...
    class CommandResult(_n_9_t_0):
        @property
        def IsCompleted(self) -> bool:"""IsCompleted { get; } -> bool"""
        def GetAwaiter(self) -> Editor.CommandResult:...
        def GetResult(self):...
class EditorExtension(object):
    @staticmethod
    def GetViewportNumber(editor: Editor, point: _n_8_t_0) -> int:...
    @staticmethod
    def PointToScreen(editor: Editor, pt: _n_2_t_0, viewportNumber: int) -> _n_8_t_0:...
    @staticmethod
    def PointToWorld(editor: Editor, pt: _n_8_t_0, viewportNumber: int) -> _n_2_t_0:...
    @staticmethod
    def PointToWorld(editor: Editor, pt: _n_8_t_0) -> _n_2_t_0:...
    @staticmethod
    def StartUserInteraction(editor: Editor, modalForm: _n_12_t_0) -> EditorUserInteraction:...
class EditorUserInteraction(_n_5_t_0):
    def End(self):...
class EditorVisualStyle(object):
    @property
    def IsVS2dType(self) -> bool:"""IsVS2dType { get; } -> bool"""
    @property
    def IsVS3dType(self) -> bool:"""IsVS3dType { get; } -> bool"""
    def __init__(self) -> EditorVisualStyle:...
    @staticmethod
    def setCvpVS2d():...
class EntityJig(Jig):
    pass
class FenceSelectedObject(SelectedObject):
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: int, descriptors: _n_5_t_2[PickPointDescriptor]) -> FenceSelectedObject:...
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: _n_5_t_3, descriptors: _n_5_t_2[PickPointDescriptor]) -> FenceSelectedObject:...
    def GetIntersectionPoints(self) -> _n_5_t_2[PickPointDescriptor]:...
class FenceSelectedSubObject(SelectedSubObject):
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: int, descriptors: _n_5_t_2[PickPointDescriptor]) -> FenceSelectedSubObject:...
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: _n_5_t_3, descriptors: _n_5_t_2[PickPointDescriptor]) -> FenceSelectedSubObject:...
    def GetIntersectionPoints(self) -> _n_5_t_2[PickPointDescriptor]:...
class InputPointContext(_n_5_t_0):
    @property
    def CartesianSnappedPoint(self) -> _n_2_t_0:"""CartesianSnappedPoint { get; } -> Point3d"""
    @property
    def ComputedPoint(self) -> _n_2_t_0:"""ComputedPoint { get; } -> Point3d"""
    @property
    def Document(self) -> _n_0_t_0:"""Document { get; } -> Document"""
    @property
    def DrawContext(self) -> _n_3_t_1:"""DrawContext { get; } -> ViewportDraw"""
    @property
    def GrippedPoint(self) -> _n_2_t_0:"""GrippedPoint { get; } -> Point3d"""
    @property
    def History(self) -> PointHistoryBits:"""History { get; } -> PointHistoryBits"""
    @property
    def LastPoint(self) -> _n_2_t_0:"""LastPoint { get; } -> Point3d"""
    @property
    def ObjectSnapMask(self) -> ObjectSnapMasks:"""ObjectSnapMask { get; } -> ObjectSnapMasks"""
    @property
    def ObjectSnapOverrides(self) -> ObjectSnapMasks:"""ObjectSnapOverrides { get; } -> ObjectSnapMasks"""
    @property
    def ObjectSnappedPoint(self) -> _n_2_t_0:"""ObjectSnappedPoint { get; } -> Point3d"""
    @property
    def PointComputed(self) -> bool:"""PointComputed { get; } -> bool"""
    @property
    def RawPoint(self) -> _n_2_t_0:"""RawPoint { get; } -> Point3d"""
    @property
    def ToolTipText(self) -> str:"""ToolTipText { get; } -> str"""
    def GetAlignmentPaths(self) -> _n_5_t_2[_n_2_t_4]:...
    def GetCustomObjectSnapModes(self) -> _n_5_t_2[_n_1_t_6]:...
    def GetCustomObjectSnapOverrides(self) -> _n_5_t_2[_n_1_t_6]:...
    def GetKeyPointEntities(self) -> _n_5_t_2[_n_1_t_2]:...
    def GetPickedEntities(self) -> _n_5_t_2[_n_1_t_2]:...
class Jig(object):
    pass
class JigPromptAngleOptions(JigPromptGeometryOptions):
    @property
    def DefaultValue(self) -> float:"""DefaultValue { get; set; } -> float"""
    def __init__(self) -> JigPromptAngleOptions:...
    def __init__(self, message: str) -> JigPromptAngleOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> JigPromptAngleOptions:...
class JigPromptDistanceOptions(JigPromptGeometryOptions):
    @property
    def DefaultValue(self) -> float:"""DefaultValue { get; set; } -> float"""
    def __init__(self) -> JigPromptDistanceOptions:...
    def __init__(self, message: str) -> JigPromptDistanceOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> JigPromptDistanceOptions:...
class JigPromptGeometryOptions(JigPromptOptions):
    @property
    def BasePoint(self) -> _n_2_t_0:"""BasePoint { get; set; } -> Point3d"""
    @property
    def UseBasePoint(self) -> bool:"""UseBasePoint { get; set; } -> bool"""
    def __init__(self) -> JigPromptGeometryOptions:...
    def __init__(self, message: str) -> JigPromptGeometryOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> JigPromptGeometryOptions:...
class JigPromptOptions(PromptOptions):
    @property
    def Cursor(self) -> CursorType:"""Cursor { get; set; } -> CursorType"""
    @property
    def UserInputControls(self) -> UserInputControls:"""UserInputControls { get; set; } -> UserInputControls"""
class JigPromptPointOptions(JigPromptGeometryOptions):
    @property
    def DefaultValue(self) -> _n_2_t_0:"""DefaultValue { get; set; } -> Point3d"""
    def __init__(self) -> JigPromptPointOptions:...
    def __init__(self, message: str) -> JigPromptPointOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> JigPromptPointOptions:...
class JigPrompts(object):
    def AcquireAngle(self) -> PromptDoubleResult:...
    def AcquireAngle(self, options: JigPromptAngleOptions) -> PromptDoubleResult:...
    def AcquireAngle(self, message: str) -> PromptDoubleResult:...
    def AcquireAngle(self, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleResult:...
    def AcquireDistance(self) -> PromptDoubleResult:...
    def AcquireDistance(self, options: JigPromptDistanceOptions) -> PromptDoubleResult:...
    def AcquireDistance(self, message: str) -> PromptDoubleResult:...
    def AcquireDistance(self, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleResult:...
    def AcquirePoint(self) -> PromptPointResult:...
    def AcquirePoint(self, options: JigPromptPointOptions) -> PromptPointResult:...
    def AcquirePoint(self, message: str) -> PromptPointResult:...
    def AcquirePoint(self, messageAndKeywords: str, globalKeywords: str) -> PromptPointResult:...
    def AcquireString(self) -> PromptResult:...
    def AcquireString(self, options: JigPromptStringOptions) -> PromptResult:...
    def AcquireString(self, message: str) -> PromptResult:...
    def AcquireString(self, messageAndKeywords: str, globalKeywords: str) -> PromptResult:...
class JigPromptStringOptions(JigPromptOptions):
    @property
    def DefaultValue(self) -> str:"""DefaultValue { get; set; } -> str"""
    def __init__(self) -> JigPromptStringOptions:...
    def __init__(self, message: str) -> JigPromptStringOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> JigPromptStringOptions:...
class Keyword(object):
    @property
    def DisplayName(self) -> str:"""DisplayName { get; set; } -> str"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def GlobalName(self) -> str:"""GlobalName { get; set; } -> str"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; set; } -> bool"""
    @property
    def LocalName(self) -> str:"""LocalName { get; set; } -> str"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
class KeywordCollection(_n_6_t_0, typing.Iterable[Keyword]):
    @property
    def Default(self) -> str:"""Default { get; set; } -> str"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def Item(self) -> Keyword:"""Item { get; } -> Keyword"""
    def __init__(self) -> KeywordCollection:...
    def Add(self, globalName: str, localName: str, displayName: str, visible: bool, enabled: bool):...
    def Add(self, globalName: str, localName: str, displayName: str):...
    def Add(self, globalName: str, localName: str):...
    def Add(self, globalName: str):...
    def Clear(self):...
    def GetDisplayString(self, showNoDefault: bool) -> str:...
class LivePreview(_n_4_t_0, _n_5_t_0):
    @property
    def PreviewEnded(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """PreviewEnded Event: EventHandler"""
    @property
    def Previewing(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """Previewing Event: EventHandler"""
    @property
    def PreviewStarted(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """PreviewStarted Event: EventHandler"""
    @property
    def PreviewWillEnd(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """PreviewWillEnd Event: EventHandler"""
    @property
    def PreviewWillStart(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """PreviewWillStart Event: EventHandler"""
    @property
    def RecordingEnded(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """RecordingEnded Event: EventHandler"""
    @property
    def RecordingStarted(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """RecordingStarted Event: EventHandler"""
    @property
    def RecordingWillEnd(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """RecordingWillEnd Event: EventHandler"""
    @property
    def RecordingWillStart(self) -> _n_5_t_13[LivePreviewEventArgs]:
        """RecordingWillStart Event: EventHandler"""
    def __init__(self) -> LivePreview:...
    def __init__(self, doc: _n_0_t_0) -> LivePreview:...
    def __init__(self, doc: _n_0_t_0, startPending: bool) -> LivePreview:...
    def AbortAll(self):...
    def EndPreview(self, delayTime: int, bRegen: bool):...
    def EndPreview(self, bRegen: bool):...
    def EndPreview(self, delayTime: int):...
    def EndPreview(self):...
    def EndRecording(self):...
    @staticmethod
    def IsPreviewRecording() -> bool:...
    @staticmethod
    def IsPreviewRecording(doc: _n_0_t_0) -> bool:...
    @staticmethod
    def IsPreviewStarted() -> bool:...
    @staticmethod
    def IsPreviewStarted(doc: _n_0_t_0) -> bool:...
    def QueueAction(self, action: LivePreviewActionBase, delayTime: int):...
    def QueueAction(self, action: LivePreviewActionBase):...
    def StartRecording(self):...
class LivePreviewAction(LivePreviewActionBase):
    def __init__(self, method: _n_5_t_14, args: _n_5_t_2[object]) -> LivePreviewAction:...
class LivePreviewActionBase(object):
    def Execute(self):...
    def OnAborted(self):...
class LivePreviewCallback(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> LivePreviewCallback:...
    def BeginInvoke(self, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self):...
class LivePreviewCommand(LivePreviewActionBase):
    def __init__(self, cmd: str) -> LivePreviewCommand:...
class LivePreviewContextCallback(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> LivePreviewContextCallback:...
    def BeginInvoke(self, contextName: str, contextVal: object, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, contextName: str, contextVal: object):...
class LivePreviewContextParameter(object):
    @property
    def LivePreview(self) -> LivePreview:"""LivePreview { get; } -> LivePreview"""
    @property
    def Type(self) -> LivePreviewContextType:"""Type { get; } -> LivePreviewContextType"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
class LivePreviewContextProxy(_n_5_t_0):
    def __init__(self, contexName: str, callback: _n_5_t_14, parameters: _n_5_t_2[object]) -> LivePreviewContextProxy:...
class LivePreviewContextType(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    EndPreview: int
    UpdatePreview: int
    value__: int
class LivePreviewDelegate(LivePreviewActionBase):
    def __init__(self, actCallback: LivePreviewCallback, abortedCallback: LivePreviewCallback) -> LivePreviewDelegate:...
    def __init__(self, actCallback: LivePreviewCallback) -> LivePreviewDelegate:...
class LivePreviewEventArgs(_n_5_t_8):
    @property
    def AbortPreview(self) -> bool:"""AbortPreview { get; set; } -> bool"""
    @property
    def CommandParameter(self) -> object:"""CommandParameter { get; } -> object"""
    @property
    def Document(self) -> _n_0_t_0:"""Document { get; } -> Document"""
    @property
    def Parameters(self) -> _n_5_t_2[object]:"""Parameters { get; } -> Array"""
    def __init__(self, parameters: _n_5_t_2[object]) -> LivePreviewEventArgs:...
    def __init__(self, document: _n_0_t_0, parameters: _n_5_t_2[object]) -> LivePreviewEventArgs:...
    def __init__(self) -> LivePreviewEventArgs:...
    def LockDocument(self) -> _n_5_t_0:...
class LivePreviewPropertySetting(LivePreviewActionBase):
    def __init__(self, prop: _n_7_t_0, component: object, value: object) -> LivePreviewPropertySetting:...
class ObjectSnapMasks(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    AllowTangent: int
    ApparentIntersection: int
    Center: int
    DisablePerpendicular: int
    End: int
    Immediate: int
    Insertion: int
    Intersection: int
    Middle: int
    Near: int
    Node: int
    NoneOverride: int
    Perpendicular: int
    Quadrant: int
    Quick: int
    RelativeCartesian: int
    RelativePolar: int
    Tangent: int
    value__: int
class PickPointDescriptor(_n_5_t_15):
    @property
    def Direction(self) -> _n_2_t_2:"""Direction { get; } -> Vector3d"""
    @property
    def Kind(self) -> PickPointKind:"""Kind { get; } -> PickPointKind"""
    @property
    def PointOnLine(self) -> _n_2_t_0:"""PointOnLine { get; } -> Point3d"""
    def __init__(self, kind: PickPointKind, pointOnLine: _n_2_t_0, direction: _n_2_t_2) -> PickPointDescriptor:...
    def IsEqualTo(self, a: PickPointDescriptor, tolerance: _n_2_t_5) -> bool:...
    def IsEqualTo(self, a: PickPointDescriptor) -> bool:...
class PickPointKind(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    InfiniteLine: int
    LineSegment: int
    Ray: int
    value__: int
class PickPointSelectedObject(SelectedObject):
    @property
    def PickPoint(self) -> PickPointDescriptor:"""PickPoint { get; } -> PickPointDescriptor"""
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: int, descriptor: PickPointDescriptor) -> PickPointSelectedObject:...
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: _n_5_t_3, descriptor: PickPointDescriptor) -> PickPointSelectedObject:...
class PickPointSelectedSubObject(SelectedSubObject):
    @property
    def PickPoint(self) -> PickPointDescriptor:"""PickPoint { get; } -> PickPointDescriptor"""
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: int, descriptor: PickPointDescriptor) -> PickPointSelectedSubObject:...
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: _n_5_t_3, descriptor: PickPointDescriptor) -> PickPointSelectedSubObject:...
class PointFilterEventArgs(_n_5_t_8, _n_5_t_0):
    @property
    def CallNext(self) -> bool:"""CallNext { get; set; } -> bool"""
    @property
    def Context(self) -> InputPointContext:"""Context { get; } -> InputPointContext"""
    @property
    def Result(self) -> PointFilterResult:"""Result { get; } -> PointFilterResult"""
class PointFilterEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PointFilterEventHandler:...
    def BeginInvoke(self, sender: object, e: PointFilterEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PointFilterEventArgs):...
class PointFilterResult(_n_5_t_0):
    @property
    def DisplayObjectSnapGlyph(self) -> bool:"""DisplayObjectSnapGlyph { get; set; } -> bool"""
    @property
    def NewPoint(self) -> _n_2_t_0:"""NewPoint { get; set; } -> Point3d"""
    @property
    def Retry(self) -> bool:"""Retry { get; set; } -> bool"""
    @property
    def ToolTipText(self) -> str:"""ToolTipText { get; set; } -> str"""
class PointHistoryBits(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Aligned: int
    AppFiltered: int
    CartSnapped: int
    CoordinatePending: int
    CyclingPoint: int
    DidNotPick: int
    ForcedPick: int
    FromKeyboard: int
    Gripped: int
    LastPoint: int
    NotDigitizer: int
    NotInteractive: int
    ObjectSnapped: int
    Ortho: int
    PickAborted: int
    PickMask: int
    PolarAngle: int
    Tablet: int
    UsedObjectSnapBox: int
    UsedPickBox: int
    value__: int
    XPending: int
    YPending: int
    ZPending: int
class PointInputEventArgs(_n_5_t_8):
    @property
    def Context(self) -> InputPointContext:"""Context { get; } -> InputPointContext"""
    @property
    def GraphicsSystemMarker(self) -> _n_5_t_3:"""GraphicsSystemMarker { get; } -> IntPtr"""
    @property
    def Handled(self) -> bool:"""Handled { get; set; } -> bool"""
    @property
    def Result(self) -> PointFilterResult:"""Result { get; } -> PointFilterResult"""
class PointInputEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PointInputEventHandler:...
    def BeginInvoke(self, sender: object, e: PointInputEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PointInputEventArgs):...
class PointMonitorEventArgs(_n_5_t_8, _n_5_t_0):
    @property
    def Context(self) -> InputPointContext:"""Context { get; } -> InputPointContext"""
    def AppendToolTipText(self, value: str):...
class PointMonitorEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PointMonitorEventHandler:...
    def BeginInvoke(self, sender: object, e: PointMonitorEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PointMonitorEventArgs):...
class PromptAngleOptions(PromptEditorOptions):
    @property
    def AllowArbitraryInput(self) -> bool:"""AllowArbitraryInput { get; set; } -> bool"""
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    @property
    def AllowZero(self) -> bool:"""AllowZero { get; set; } -> bool"""
    @property
    def BasePoint(self) -> _n_2_t_0:"""BasePoint { get; set; } -> Point3d"""
    @property
    def DefaultValue(self) -> float:"""DefaultValue { get; set; } -> float"""
    @property
    def UseAngleBase(self) -> bool:"""UseAngleBase { get; set; } -> bool"""
    @property
    def UseBasePoint(self) -> bool:"""UseBasePoint { get; set; } -> bool"""
    @property
    def UseDashedLine(self) -> bool:"""UseDashedLine { get; set; } -> bool"""
    @property
    def UseDefaultValue(self) -> bool:"""UseDefaultValue { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptAngleOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptAngleOptions:...
class PromptAngleOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptAngleOptions:"""Options { get; } -> PromptAngleOptions"""
class PromptAngleOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptAngleOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptAngleOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptAngleOptionsEventArgs):...
class PromptCornerOptions(PromptEditorOptions):
    @property
    def AllowArbitraryInput(self) -> bool:"""AllowArbitraryInput { get; set; } -> bool"""
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    @property
    def BasePoint(self) -> _n_2_t_0:"""BasePoint { get; set; } -> Point3d"""
    @property
    def LimitsChecked(self) -> bool:"""LimitsChecked { get; set; } -> bool"""
    @property
    def UseDashedLine(self) -> bool:"""UseDashedLine { get; set; } -> bool"""
    def __init__(self, message: str, basePoint: _n_2_t_0) -> PromptCornerOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str, basePoint: _n_2_t_0) -> PromptCornerOptions:...
class PromptDistanceOptions(PromptNumericalOptions):
    @property
    def BasePoint(self) -> _n_2_t_0:"""BasePoint { get; set; } -> Point3d"""
    @property
    def DefaultValue(self) -> float:"""DefaultValue { get; set; } -> float"""
    @property
    def Only2d(self) -> bool:"""Only2d { get; set; } -> bool"""
    @property
    def UseBasePoint(self) -> bool:"""UseBasePoint { get; set; } -> bool"""
    @property
    def UseDashedLine(self) -> bool:"""UseDashedLine { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptDistanceOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptDistanceOptions:...
class PromptDistanceOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptDistanceOptions:"""Options { get; } -> PromptDistanceOptions"""
class PromptDistanceOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptDistanceOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptDistanceOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptDistanceOptionsEventArgs):...
class PromptDoubleOptions(PromptNumericalOptions):
    @property
    def DefaultValue(self) -> float:"""DefaultValue { get; set; } -> float"""
    def __init__(self, message: str) -> PromptDoubleOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleOptions:...
class PromptDoubleOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptDoubleOptions:"""Options { get; } -> PromptDoubleOptions"""
class PromptDoubleOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptDoubleOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptDoubleOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptDoubleOptionsEventArgs):...
class PromptDoubleResult(PromptResult):
    @property
    def Value(self) -> float:"""Value { get; } -> float"""
class PromptDoubleResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptDoubleResult:"""Result { get; } -> PromptDoubleResult"""
class PromptDoubleResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptDoubleResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptDoubleResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptDoubleResultEventArgs):...
class PromptDragOptions(PromptEditorOptions):
    @property
    def AllowArbitraryInput(self) -> bool:"""AllowArbitraryInput { get; set; } -> bool"""
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    @property
    def Callback(self) -> DragCallback:"""Callback { get; set; } -> DragCallback"""
    @property
    def Cursor(self) -> DragCursor:"""Cursor { get; set; } -> DragCursor"""
    @property
    def Selection(self) -> SelectionSet:"""Selection { get; } -> SelectionSet"""
    def __init__(self, selection: SelectionSet, message: str, callback: DragCallback) -> PromptDragOptions:...
    def __init__(self, selection: SelectionSet, messageAndKeywords: str, globalKeywords: str, callback: DragCallback) -> PromptDragOptions:...
class PromptEditorOptions(PromptOptions):
    pass
class PromptEntityOptions(PromptEditorOptions):
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    @property
    def AllowObjectOnLockedLayer(self) -> bool:"""AllowObjectOnLockedLayer { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptEntityOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptEntityOptions:...
    def AddAllowedClass(self, type: _n_5_t_16, exactMatch: bool):...
    def RemoveAllowedClass(self, type: _n_5_t_16):...
    def SetRejectMessage(self, message: str):...
class PromptEntityOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptEntityOptions:"""Options { get; } -> PromptEntityOptions"""
class PromptEntityOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptEntityOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptEntityOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptEntityOptionsEventArgs):...
class PromptEntityResult(PromptResult):
    @property
    def ObjectId(self) -> _n_1_t_1:"""ObjectId { get; } -> ObjectId"""
    @property
    def PickedPoint(self) -> _n_2_t_0:"""PickedPoint { get; } -> Point3d"""
class PromptEntityResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptEntityResult:"""Result { get; } -> PromptEntityResult"""
class PromptEntityResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptEntityResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptEntityResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptEntityResultEventArgs):...
class PromptFileNameResult(PromptResult):
    @property
    def ReadOnly(self) -> bool:"""ReadOnly { get; } -> bool"""
class PromptFileOptions(object):
    @property
    def AllowUrls(self) -> bool:"""AllowUrls { get; set; } -> bool"""
    @property
    def DialogCaption(self) -> str:"""DialogCaption { get; set; } -> str"""
    @property
    def DialogName(self) -> str:"""DialogName { get; set; } -> str"""
    @property
    def Filter(self) -> str:"""Filter { get; set; } -> str"""
    @property
    def FilterIndex(self) -> int:"""FilterIndex { get; set; } -> int"""
    @property
    def InitialDirectory(self) -> str:"""InitialDirectory { get; set; } -> str"""
    @property
    def InitialFileName(self) -> str:"""InitialFileName { get; set; } -> str"""
    @property
    def Message(self) -> str:"""Message { get; set; } -> str"""
    @property
    def PreferCommandLine(self) -> bool:"""PreferCommandLine { get; set; } -> bool"""
class PromptForEntityEndingEventArgs(_n_5_t_8, _n_5_t_0):
    @property
    def Result(self) -> PromptEntityResult:"""Result { get; } -> PromptEntityResult"""
    def RemoveSelectedObject(self):...
    def ReplaceSelectedObject(self, newValue: SelectedObject):...
class PromptForEntityEndingEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptForEntityEndingEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptForEntityEndingEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptForEntityEndingEventArgs):...
class PromptForSelectionEndingEventArgs(_n_5_t_8, _n_5_t_0):
    @property
    def Flags(self) -> SelectionFlags:"""Flags { get; } -> SelectionFlags"""
    @property
    def Selection(self) -> SelectionSet:"""Selection { get; } -> SelectionSet"""
    def Add(self, value: SelectedObject):...
    def AddSubEntity(self, value: SelectedSubObject):...
    def Remove(self, index: int):...
    def RemoveSubEntity(self, entityIndex: int, subEntityIndex: int):...
class PromptForSelectionEndingEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptForSelectionEndingEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptForSelectionEndingEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptForSelectionEndingEventArgs):...
class PromptIntegerOptions(PromptNumericalOptions):
    @property
    def DefaultValue(self) -> int:"""DefaultValue { get; set; } -> int"""
    @property
    def LowerLimit(self) -> int:"""LowerLimit { get; set; } -> int"""
    @property
    def UpperLimit(self) -> int:"""UpperLimit { get; set; } -> int"""
    def __init__(self, message: str) -> PromptIntegerOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptIntegerOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str, lowerLimit: int, upperLimit: int) -> PromptIntegerOptions:...
class PromptIntegerOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptIntegerOptions:"""Options { get; } -> PromptIntegerOptions"""
class PromptIntegerOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptIntegerOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptIntegerOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptIntegerOptionsEventArgs):...
class PromptIntegerResult(PromptResult):
    @property
    def Value(self) -> int:"""Value { get; } -> int"""
class PromptIntegerResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptIntegerResult:"""Result { get; } -> PromptIntegerResult"""
class PromptIntegerResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptIntegerResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptIntegerResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptIntegerResultEventArgs):...
class PromptKeywordOptions(PromptEditorOptions):
    @property
    def AllowArbitraryInput(self) -> bool:"""AllowArbitraryInput { get; set; } -> bool"""
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptKeywordOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptKeywordOptions:...
class PromptKeywordOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptKeywordOptions:"""Options { get; } -> PromptKeywordOptions"""
class PromptKeywordOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptKeywordOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptKeywordOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptKeywordOptionsEventArgs):...
class PromptNestedEntityOptions(PromptEditorOptions):
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    @property
    def NonInteractivePickPoint(self) -> _n_2_t_0:"""NonInteractivePickPoint { get; set; } -> Point3d"""
    @property
    def UseNonInteractivePickPoint(self) -> bool:"""UseNonInteractivePickPoint { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptNestedEntityOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptNestedEntityOptions:...
class PromptNestedEntityOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptNestedEntityOptions:"""Options { get; } -> PromptNestedEntityOptions"""
class PromptNestedEntityOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptNestedEntityOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptNestedEntityOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptNestedEntityOptionsEventArgs):...
class PromptNestedEntityResult(PromptEntityResult):
    @property
    def Transform(self) -> _n_2_t_1:"""Transform { get; } -> Matrix3d"""
    def GetContainers(self) -> _n_5_t_2[_n_1_t_1]:...
class PromptNestedEntityResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptNestedEntityResult:"""Result { get; } -> PromptNestedEntityResult"""
class PromptNestedEntityResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptNestedEntityResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptNestedEntityResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptNestedEntityResultEventArgs):...
class PromptNumericalOptions(PromptEditorOptions):
    @property
    def AllowArbitraryInput(self) -> bool:"""AllowArbitraryInput { get; set; } -> bool"""
    @property
    def AllowNegative(self) -> bool:"""AllowNegative { get; set; } -> bool"""
    @property
    def AllowNone(self) -> bool:"""AllowNone { get; set; } -> bool"""
    @property
    def AllowZero(self) -> bool:"""AllowZero { get; set; } -> bool"""
    @property
    def UseDefaultValue(self) -> bool:"""UseDefaultValue { get; set; } -> bool"""
class PromptOpenFileOptions(PromptFileOptions):
    @property
    def SearchPath(self) -> bool:"""SearchPath { get; set; } -> bool"""
    @property
    def TransferRemoteFiles(self) -> bool:"""TransferRemoteFiles { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptOpenFileOptions:...
class PromptOptions(object):
    @property
    def AppendKeywordsToMessage(self) -> bool:"""AppendKeywordsToMessage { get; set; } -> bool"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def Keywords(self) -> KeywordCollection:"""Keywords { get; } -> KeywordCollection"""
    @property
    def Message(self) -> str:"""Message { get; set; } -> str"""
    def SetMessageAndKeywords(self, messageAndKeywords: str, globalKeywords: str):...
class PromptPointOptions(PromptCornerOptions):
    @property
    def UseBasePoint(self) -> bool:"""UseBasePoint { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptPointOptions:...
    def __init__(self, messageAndKeywords: str, globalKeywords: str) -> PromptPointOptions:...
class PromptPointOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptPointOptions:"""Options { get; } -> PromptPointOptions"""
class PromptPointOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptPointOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptPointOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptPointOptionsEventArgs):...
class PromptPointResult(PromptResult):
    @property
    def Value(self) -> _n_2_t_0:"""Value { get; } -> Point3d"""
class PromptPointResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptPointResult:"""Result { get; } -> PromptPointResult"""
class PromptPointResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptPointResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptPointResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptPointResultEventArgs):...
class PromptResult(object):
    @property
    def Status(self) -> PromptStatus:"""Status { get; } -> PromptStatus"""
    @property
    def StringResult(self) -> str:"""StringResult { get; } -> str"""
class PromptSaveFileOptions(PromptFileOptions):
    @property
    def DeriveInitialFilenameFromDrawingName(self) -> bool:"""DeriveInitialFilenameFromDrawingName { get; set; } -> bool"""
    @property
    def DisplaySaveOptionsMenuItem(self) -> bool:"""DisplaySaveOptionsMenuItem { get; set; } -> bool"""
    @property
    def ForceOverwriteWarningForScriptsAndLisp(self) -> bool:"""ForceOverwriteWarningForScriptsAndLisp { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptSaveFileOptions:...
class PromptSelectionOptions(object):
    @property
    def AllowDuplicates(self) -> bool:"""AllowDuplicates { get; set; } -> bool"""
    @property
    def AllowSubSelections(self) -> bool:"""AllowSubSelections { get; set; } -> bool"""
    @property
    def ForceSubSelections(self) -> bool:"""ForceSubSelections { get; set; } -> bool"""
    @property
    def Keywords(self) -> KeywordCollection:"""Keywords { get; } -> KeywordCollection"""
    @property
    def MessageForAdding(self) -> str:"""MessageForAdding { get; set; } -> str"""
    @property
    def MessageForRemoval(self) -> str:"""MessageForRemoval { get; set; } -> str"""
    @property
    def PrepareOptionalDetails(self) -> bool:"""PrepareOptionalDetails { get; set; } -> bool"""
    @property
    def RejectObjectsFromNonCurrentSpace(self) -> bool:"""RejectObjectsFromNonCurrentSpace { get; set; } -> bool"""
    @property
    def RejectObjectsOnLockedLayers(self) -> bool:"""RejectObjectsOnLockedLayers { get; set; } -> bool"""
    @property
    def RejectPaperspaceViewport(self) -> bool:"""RejectPaperspaceViewport { get; set; } -> bool"""
    @property
    def SelectEverythingInAperture(self) -> bool:"""SelectEverythingInAperture { get; set; } -> bool"""
    @property
    def SingleOnly(self) -> bool:"""SingleOnly { get; set; } -> bool"""
    @property
    def SinglePickInSpace(self) -> bool:"""SinglePickInSpace { get; set; } -> bool"""
    @property
    def KeywordInput(self) -> SelectionTextInputEventHandler:
        """KeywordInput Event: SelectionTextInputEventHandler"""
    @property
    def UnknownInput(self) -> SelectionTextInputEventHandler:
        """UnknownInput Event: SelectionTextInputEventHandler"""
    def __init__(self) -> PromptSelectionOptions:...
    def SetKeywords(self, keywords: str, globalKeywords: str):...
class PromptSelectionOptionsEventArgs(_n_5_t_8):
    @property
    def Filter(self) -> SelectionFilter:"""Filter { get; } -> SelectionFilter"""
    @property
    def Options(self) -> PromptSelectionOptions:"""Options { get; } -> PromptSelectionOptions"""
    def GetPoints(self) -> _n_5_t_2[_n_2_t_0]:...
class PromptSelectionOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptSelectionOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptSelectionOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptSelectionOptionsEventArgs):...
class PromptSelectionResult(object):
    @property
    def Status(self) -> PromptStatus:"""Status { get; } -> PromptStatus"""
    @property
    def Value(self) -> SelectionSet:"""Value { get; } -> SelectionSet"""
class PromptSelectionResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptSelectionResult:"""Result { get; } -> PromptSelectionResult"""
class PromptSelectionResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptSelectionResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptSelectionResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptSelectionResultEventArgs):...
class PromptStatus(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Cancel: int
    Error: int
    Keyword: int
    Modeless: int
    _None: int
    OK: int
    Other: int
    value__: int
class PromptStringOptions(PromptEditorOptions):
    @property
    def AllowSpaces(self) -> bool:"""AllowSpaces { get; set; } -> bool"""
    @property
    def DefaultValue(self) -> str:"""DefaultValue { get; set; } -> str"""
    @property
    def UseDefaultValue(self) -> bool:"""UseDefaultValue { get; set; } -> bool"""
    def __init__(self, message: str) -> PromptStringOptions:...
class PromptStringOptionsEventArgs(_n_5_t_8):
    @property
    def Options(self) -> PromptStringOptions:"""Options { get; } -> PromptStringOptions"""
class PromptStringOptionsEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptStringOptionsEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptStringOptionsEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptStringOptionsEventArgs):...
class PromptStringResultEventArgs(_n_5_t_8):
    @property
    def Result(self) -> PromptResult:"""Result { get; } -> PromptResult"""
class PromptStringResultEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> PromptStringResultEventHandler:...
    def BeginInvoke(self, sender: object, e: PromptStringResultEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PromptStringResultEventArgs):...
class RolloverEventArgs(_n_5_t_8):
    @property
    def Highlighted(self) -> _n_1_t_2:"""Highlighted { get; set; } -> FullSubentityPath"""
    @property
    def Picked(self) -> _n_1_t_2:"""Picked { get; } -> FullSubentityPath"""
class RolloverEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> RolloverEventHandler:...
    def BeginInvoke(self, sender: object, e: RolloverEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: RolloverEventArgs):...
class SamplerStatus(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Cancel: int
    NoChange: int
    OK: int
    value__: int
class SelectedObject(object):
    @property
    def GraphicsSystemMarker(self) -> int:"""GraphicsSystemMarker { get; } -> int"""
    @property
    def GraphicsSystemMarkerPtr(self) -> _n_5_t_3:"""GraphicsSystemMarkerPtr { get; } -> IntPtr"""
    @property
    def ObjectId(self) -> _n_1_t_1:"""ObjectId { get; } -> ObjectId"""
    @property
    def OptionalDetails(self) -> SelectionDetails:"""OptionalDetails { get; set; } -> SelectionDetails"""
    @property
    def SelectionMethod(self) -> SelectionMethod:"""SelectionMethod { get; } -> SelectionMethod"""
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: int) -> SelectedObject:...
    def __init__(self, id: _n_1_t_1, method: SelectionMethod, gsMarker: _n_5_t_3) -> SelectedObject:...
    def __init__(self, id: _n_1_t_1, subSelections: _n_5_t_2[SelectedSubObject]) -> SelectedObject:...
    def GetSubentities(self) -> _n_5_t_2[SelectedSubObject]:...
class SelectedSubObject(object):
    @property
    def FullSubentityPath(self) -> _n_1_t_2:"""FullSubentityPath { get; } -> FullSubentityPath"""
    @property
    def GraphicsSystemMarker(self) -> int:"""GraphicsSystemMarker { get; } -> int"""
    @property
    def GraphicsSystemMarkerPtr(self) -> _n_5_t_3:"""GraphicsSystemMarkerPtr { get; } -> IntPtr"""
    @property
    def OptionalDetails(self) -> SelectionDetails:"""OptionalDetails { get; } -> SelectionDetails"""
    @property
    def SelectionMethod(self) -> SelectionMethod:"""SelectionMethod { get; } -> SelectionMethod"""
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: int) -> SelectedSubObject:...
    def __init__(self, path: _n_1_t_2, method: SelectionMethod, gsMarker: _n_5_t_3) -> SelectedSubObject:...
class SelectionAddedEventArgs(_n_5_t_8, _n_5_t_0):
    @property
    def AddedObjects(self) -> SelectionSet:"""AddedObjects { get; } -> SelectionSet"""
    @property
    def Flags(self) -> SelectionFlags:"""Flags { get; } -> SelectionFlags"""
    @property
    def Selection(self) -> SelectionSet:"""Selection { get; } -> SelectionSet"""
    def Add(self, value: SelectedObject):...
    def AddSubEntity(self, value: SelectedSubObject):...
    def Highlight(self, subSelectionIndex: int, path: _n_1_t_2):...
    def Remove(self, index: int):...
    def RemoveSubEntity(self, entityIndex: int, subEntityIndex: int):...
class SelectionAddedEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> SelectionAddedEventHandler:...
    def BeginInvoke(self, sender: object, e: SelectionAddedEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: SelectionAddedEventArgs):...
class SelectionDetails(object):
    @property
    def Transform(self) -> _n_2_t_1:"""Transform { get; } -> Matrix3d"""
    def GetContainers(self) -> _n_5_t_2[_n_1_t_1]:...
class SelectionFilter(object):
    def __init__(self, value: _n_5_t_2[_n_1_t_7]) -> SelectionFilter:...
    def GetFilter(self) -> _n_5_t_2[_n_1_t_7]:...
class SelectionFlags(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Duplicates: int
    FailedPickAuto: int
    NestedEntities: int
    Normal: int
    PickfirstSet: int
    PickPoints: int
    PreviousSet: int
    SinglePick: int
    SubEntities: int
    SubSelection: int
    Undo: int
    value__: int
class SelectionMethod(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Crossing: int
    Fence: int
    NonGraphical: int
    PickPoint: int
    SubEntity: int
    Unavailable: int
    value__: int
    Window: int
class SelectionMode(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    All: int
    Box: int
    Crossing: int
    CrossingPolygon: int
    Entity: int
    Every: int
    Extents: int
    FencePolyline: int
    Group: int
    Last: int
    Multiple: int
    Pick: int
    Previous: int
    value__: int
    Window: int
    WindowPolygon: int
class SelectionRemovedEventArgs(_n_5_t_8, _n_5_t_0):
    @property
    def Flags(self) -> SelectionFlags:"""Flags { get; } -> SelectionFlags"""
    @property
    def RemovedObjects(self) -> SelectionSet:"""RemovedObjects { get; } -> SelectionSet"""
    @property
    def Selection(self) -> SelectionSet:"""Selection { get; } -> SelectionSet"""
    def Remove(self, index: int):...
    def RemoveSubentity(self, index: int, subentityIndex: int):...
class SelectionRemovedEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> SelectionRemovedEventHandler:...
    def BeginInvoke(self, sender: object, e: SelectionRemovedEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: SelectionRemovedEventArgs):...
class SelectionSet(_n_6_t_0, _n_5_t_0, typing.Iterable[SelectedObject]):
    @property
    def Item(self) -> SelectedObject:"""Item { get; } -> SelectedObject"""
    @staticmethod
    def FromObjectIds(ids: _n_5_t_2[_n_1_t_1]) -> SelectionSet:...
    def GetObjectIds(self) -> _n_5_t_2[_n_1_t_1]:...
class SelectionSetDelayMarshalled(SelectionSet, _n_6_t_0, _n_5_t_0, typing.Iterable[SelectedObject]):
    @property
    def Name(self) -> object:"""Name { get; } -> object"""
class SelectionTextInputEventArgs(_n_5_t_8):
    @property
    def Input(self) -> str:"""Input { get; } -> str"""
    def AddObjects(self, ids: _n_5_t_2[_n_1_t_1]):...
    def SetErrorMessage(self, errorMessage: str):...
class SelectionTextInputEventHandler(_n_5_t_9, _n_5_t_1, _n_10_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_3) -> SelectionTextInputEventHandler:...
    def BeginInvoke(self, sender: object, e: SelectionTextInputEventArgs, callback: _n_5_t_11, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: SelectionTextInputEventArgs):...
class Transient(_n_3_t_2, _n_5_t_0, _n_5_t_1):
    @property
    def CapturedDrawable(self) -> _n_3_t_2:"""CapturedDrawable { get; set; } -> Drawable"""
    @property
    def Captured(self) -> _n_5_t_13:
        """Captured Event: EventHandler"""
    @property
    def CaptureReleased(self) -> _n_5_t_13:
        """CaptureReleased Event: EventHandler"""
    @property
    def DeviceInput(self) -> DeviceInputEventHandler:
        """DeviceInput Event: DeviceInputEventHandler"""
    @property
    def PointInput(self) -> PointInputEventHandler:
        """PointInput Event: PointInputEventHandler"""
class UserInputControls(_n_5_t_4, _n_5_t_5, _n_5_t_6, _n_5_t_7):
    Accept3dCoordinates: int
    AcceptMouseUpAsPoint: int
    AcceptOtherInputString: int
    AnyBlankTerminatesInput: int
    DoNotEchoCancelForCtrlC: int
    DoNotUpdateLastPoint: int
    GovernedByOrthoMode: int
    GovernedByUCSDetect: int
    InitialBlankTerminatesInput: int
    NoDwgLimitsChecking: int
    NoNegativeResponseAccepted: int
    NoZDirectionOrtho: int
    NoZeroResponseAccepted: int
    NullResponseAccepted: int
    UseBasePointElevation: int
    value__: int
