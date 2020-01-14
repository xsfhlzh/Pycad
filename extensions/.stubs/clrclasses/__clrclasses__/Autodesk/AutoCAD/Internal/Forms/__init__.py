from __clrclasses__.Autodesk.Internal.Windows import ControlToolTip as _n_0_t_0
from __clrclasses__.System import ICloneable as _n_1_t_0
from __clrclasses__.System import Array as _n_1_t_1
from __clrclasses__.System import MulticastDelegate as _n_1_t_2
from __clrclasses__.System import IntPtr as _n_1_t_3
from __clrclasses__.System import IAsyncResult as _n_1_t_4
from __clrclasses__.System import AsyncCallback as _n_1_t_5
from __clrclasses__.System import ValueType as _n_1_t_6
from __clrclasses__.System.Collections import IList as _n_2_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_3_t_0
from __clrclasses__.System.ComponentModel import ISynchronizeInvoke as _n_3_t_1
from __clrclasses__.System.Drawing import Point as _n_4_t_0
from __clrclasses__.System.Drawing import Rectangle as _n_4_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
from __clrclasses__.System.Windows.Forms import ColumnHeader as _n_6_t_0
from __clrclasses__.System.Windows.Forms import ListView as _n_6_t_1
from __clrclasses__.System.Windows.Forms import UnsafeNativeMethods as _n_6_t_2
from __clrclasses__.System.Windows.Forms import ISupportOleDropSource as _n_6_t_3
from __clrclasses__.System.Windows.Forms import IDropTarget as _n_6_t_4
from __clrclasses__.System.Windows.Forms import IWin32Window as _n_6_t_5
from __clrclasses__.System.Windows.Forms import IBindableComponent as _n_6_t_6
from __clrclasses__.System.Windows.Forms import LabelEditEventHandler as _n_6_t_7
from __clrclasses__.System.Windows.Forms import ItemCheckEventHandler as _n_6_t_8
from __clrclasses__.System.Windows.Forms import ColumnClickEventHandler as _n_6_t_9
from __clrclasses__.System.Windows.Forms import ContextMenu as _n_6_t_10
from __clrclasses__.System.Windows.Forms import HelpEventArgs as _n_6_t_11
from __clrclasses__.System.Windows.Forms import TextBox as _n_6_t_12
from __clrclasses__.System.Windows.Forms import IMessageFilter as _n_6_t_13
from __clrclasses__.System.Windows.Forms import Label as _n_6_t_14
from __clrclasses__.System.Windows.Forms import LabelEditEventArgs as _n_6_t_15
from __clrclasses__.System.Windows.Forms.Layout import IArrangedElement as _n_7_t_0
import typing
class ExColumnHeader(_n_6_t_0, _n_3_t_0, _n_1_t_0):
    @property
    def AllowCellEdit(self) -> bool:"""AllowCellEdit { get; set; } -> bool"""
    def __init__(self) -> ExColumnHeader:...
class ExListView(_n_6_t_1, _n_3_t_0, _n_6_t_2IOleControl, _n_6_t_2IOleObject, _n_6_t_2IOleInPlaceObject, _n_6_t_2IOleInPlaceActiveObject, _n_6_t_2IOleWindow, _n_6_t_2IViewObject, _n_6_t_2IViewObject2, _n_6_t_2IPersist, _n_6_t_2IPersistStreamInit, _n_6_t_2IPersistPropertyBag, _n_6_t_2IPersistStorage, _n_6_t_2IQuickActivate, _n_6_t_3, _n_6_t_4, _n_3_t_1, _n_6_t_5, _n_7_t_0, _n_6_t_6):
    @property
    def DoubleClickActivation(self) -> bool:"""DoubleClickActivation { get; set; } -> bool"""
    @property
    def HeaderContextMenu(self) -> _n_6_t_10:"""HeaderContextMenu { get; set; } -> ContextMenu"""
    @property
    def IsHorizontalScrollBarVisible(self) -> bool:"""IsHorizontalScrollBarVisible { get; } -> bool"""
    @property
    def IsVerticalScrollBarVisible(self) -> bool:"""IsVerticalScrollBarVisible { get; } -> bool"""
    @property
    def LastRightClickedColumn(self) -> int:"""LastRightClickedColumn { get; set; } -> int"""
    @property
    def SortColumn(self) -> int:"""SortColumn { get; set; } -> int"""
    @property
    def SortOnColumnClick(self) -> bool:"""SortOnColumnClick { get; set; } -> bool"""
    @property
    def AfterCellEdit(self) -> ExListView.CellEditEventHandler:
        """AfterCellEdit Event: ExListView.CellEditEventHandler"""
    @property
    def AfterColumnLabelEdit(self) -> _n_6_t_7:
        """AfterColumnLabelEdit Event: LabelEditEventHandler"""
    @property
    def AfterItemCheck(self) -> _n_6_t_8:
        """AfterItemCheck Event: ItemCheckEventHandler"""
    @property
    def BeforeCellEdit(self) -> ExListView.CellEditEventHandler:
        """BeforeCellEdit Event: ExListView.CellEditEventHandler"""
    @property
    def BeforeColumnLabelEdit(self) -> _n_6_t_7:
        """BeforeColumnLabelEdit Event: LabelEditEventHandler"""
    @property
    def ColumnRightClick(self) -> _n_6_t_9:
        """ColumnRightClick Event: ColumnClickEventHandler"""
    @property
    def HideCellEdit(self) -> ExListView.CellEditEventHandler:
        """HideCellEdit Event: ExListView.CellEditEventHandler"""
    @property
    def HideColumnLabelEdit(self) -> _n_6_t_7:
        """HideColumnLabelEdit Event: LabelEditEventHandler"""
    def __init__(self) -> ExListView:...
    def EditCell(self, rowIndex: int, colIndex: int):...
    def EditColumnLabel(self, index: int):...
    def EndEditBox(self):...
    def GetColumnHeadersInDisplayOrder(self) -> _n_1_t_1[ExColumnHeader]:...
    def GetColumnIndicesInDisplayOrder(self) -> _n_1_t_1[int]:...
    def GetItemFromPoint(self, pnt: _n_4_t_0) -> int:...
    def GetMaxCellWidth(self, columnIndex: int, bIncludeHeader: bool) -> int:...
    def SetColumnIndicesInDisplayOrder(self, indices: _n_1_t_1[int]):...
    class CellEditEventHandler(_n_1_t_2, _n_1_t_0, _n_5_t_0):
        def __init__(self, object: object, method: _n_1_t_3) -> ExListView.CellEditEventHandler:...
        def BeginInvoke(self, sender: object, ea: ListViewCellEditEventArgs, callback: _n_1_t_5, object: object) -> _n_1_t_4:...
        def EndInvoke(self, result: _n_1_t_4):...
        def Invoke(self, sender: object, ea: ListViewCellEditEventArgs):...
    class ExColumnHeaderCollection(_n_6_t_1ColumnHeaderCollection, _n_2_t_0, typing.Iterable[ExColumnHeader]):
        def __init__(self, owner: ExListView) -> ExListView.ExColumnHeaderCollection:...
        def __init__(self, owner: ExListView, columns: _n_6_t_1ColumnHeaderCollection) -> ExListView.ExColumnHeaderCollection:...
    class RECT(_n_1_t_6):
        bottom: int
        left: int
        right: int
        top: int
class HelpProvider(object):
    HIDCANCEL: int
    HIDHELP: int
    HIDOK: int
    @property
    def ContextHelpFileName(self) -> str:"""ContextHelpFileName { get; set; } -> str"""
    @property
    def HelpFileName(self) -> str:"""HelpFileName { get; set; } -> str"""
    @property
    def HelpPrefix(self) -> str:"""HelpPrefix { get; set; } -> str"""
    @property
    def HelpTopic(self) -> str:"""HelpTopic { get; set; } -> str"""
    @property
    def ToolTip(self) -> _n_0_t_0:"""ToolTip { get; } -> ControlToolTip"""
    def __init__(self) -> HelpProvider:...
    def Add(self, comp: object, id: str):...
    def ctrl_HelpRequested(self, sender: object, hlpevent: _n_6_t_11):...
    def InvokeHelp(self):...
    def InvokeHelp(self, topicToDisplay: str):...
    def Remove(self, comp: object):...
    def SetToolTip(self, comp: object):...
    def SetToolTip(self, comp: object, content: object):...
    def SetToolTip(self, comp: object, content: object, includeChildItems: bool):...
class IInPlaceEditUpdater():
    def IpeIsValidText(self, edit: InPlaceEditControl, text: str) -> bool:...
    def IpeUpdateText(self, edit: InPlaceEditControl, text: str):...
class InPlaceEditControl(_n_6_t_12, _n_3_t_0, _n_6_t_2IOleControl, _n_6_t_2IOleObject, _n_6_t_2IOleInPlaceObject, _n_6_t_2IOleInPlaceActiveObject, _n_6_t_2IOleWindow, _n_6_t_2IViewObject, _n_6_t_2IViewObject2, _n_6_t_2IPersist, _n_6_t_2IPersistStreamInit, _n_6_t_2IPersistPropertyBag, _n_6_t_2IPersistStorage, _n_6_t_2IQuickActivate, _n_6_t_3, _n_6_t_4, _n_3_t_1, _n_6_t_5, _n_7_t_0, _n_6_t_6, _n_6_t_13):
    @property
    def OriginalText(self) -> str:"""OriginalText { get; set; } -> str"""
    def __init__(self, updater: IInPlaceEditUpdater) -> InPlaceEditControl:...
    def BeginEdit(self, rect: _n_4_t_1, text: str):...
    def StopEdit(self, bUpdate: bool) -> bool:...
class LabelEllipsis(_n_6_t_14, _n_3_t_0, _n_6_t_2IOleControl, _n_6_t_2IOleObject, _n_6_t_2IOleInPlaceObject, _n_6_t_2IOleInPlaceActiveObject, _n_6_t_2IOleWindow, _n_6_t_2IViewObject, _n_6_t_2IViewObject2, _n_6_t_2IPersist, _n_6_t_2IPersistStreamInit, _n_6_t_2IPersistPropertyBag, _n_6_t_2IPersistStorage, _n_6_t_2IQuickActivate, _n_6_t_3, _n_6_t_4, _n_3_t_1, _n_6_t_5, _n_7_t_0, _n_6_t_6):
    def __init__(self) -> LabelEllipsis:...
class ListViewCellEditEventArgs(_n_6_t_15):
    @property
    def ColumnIndex(self) -> int:"""ColumnIndex { get; } -> int"""
    @property
    def RowIndex(self) -> int:"""RowIndex { get; } -> int"""
    def __init__(self, rowIndex: int, colIndex: int, sLabel: str) -> ListViewCellEditEventArgs:...
