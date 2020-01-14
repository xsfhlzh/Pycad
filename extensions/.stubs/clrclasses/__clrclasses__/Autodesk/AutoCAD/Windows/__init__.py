import __clrclasses__.Autodesk.AutoCAD.Windows.Data as Data
import __clrclasses__.Autodesk.AutoCAD.Windows.ToolPalette as ToolPalette
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import IConfigurationSection as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LineWeight as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.Internal import ColorThemeEnum as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import IMenuItem as _n_4_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_4_t_1
from __clrclasses__.System import Nullable as _n_5_t_0
from __clrclasses__.System import Enum as _n_5_t_1
from __clrclasses__.System import IComparable as _n_5_t_2
from __clrclasses__.System import IFormattable as _n_5_t_3
from __clrclasses__.System import IConvertible as _n_5_t_4
from __clrclasses__.System import IDisposable as _n_5_t_5
from __clrclasses__.System import EventHandler as _n_5_t_6
from __clrclasses__.System import MulticastDelegate as _n_5_t_7
from __clrclasses__.System import ICloneable as _n_5_t_8
from __clrclasses__.System import IntPtr as _n_5_t_9
from __clrclasses__.System import IAsyncResult as _n_5_t_10
from __clrclasses__.System import EventArgs as _n_5_t_11
from __clrclasses__.System import AsyncCallback as _n_5_t_12
from __clrclasses__.System import UInt32 as _n_5_t_13
from __clrclasses__.System import Array as _n_5_t_14
from __clrclasses__.System import Guid as _n_5_t_15
from __clrclasses__.System import Uri as _n_5_t_16
from __clrclasses__.System.Collections import IList as _n_6_t_0
from __clrclasses__.System.Collections import ICollection as _n_6_t_1
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_7_t_0
from __clrclasses__.System.Collections.Generic import List as _n_7_t_1
from __clrclasses__.System.Drawing import Icon as _n_8_t_0
from __clrclasses__.System.Drawing import Point as _n_8_t_1
from __clrclasses__.System.Drawing import Size as _n_8_t_2
from __clrclasses__.System.Drawing import Image as _n_8_t_3
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_9_t_0
from __clrclasses__.System.Windows import Size as _n_10_t_0
from __clrclasses__.System.Windows import Rect as _n_10_t_1
from __clrclasses__.System.Windows import Point as _n_10_t_2
from __clrclasses__.System.Windows import Vector as _n_10_t_3
from __clrclasses__.System.Windows.Forms import DialogResult as _n_11_t_0
from __clrclasses__.System.Windows.Forms import DragEventArgs as _n_11_t_1
from __clrclasses__.System.Windows.Forms import Control as _n_11_t_2
from __clrclasses__.System.Windows.Forms import ContextMenu as _n_11_t_3
from __clrclasses__.System.Windows.Forms import MouseButtons as _n_11_t_4
from __clrclasses__.System.Windows.Interop import IWin32Window as _n_12_t_0
from __clrclasses__.System.Windows.Interop import HwndSource as _n_12_t_1
from __clrclasses__.System.Windows.Media import Visual as _n_13_t_0
import typing
class ColorDialog(object):
    @property
    def Color(self) -> _n_1_t_0:"""Color { get; set; } -> Color"""
    @property
    def IncludeByBlockByLayer(self) -> bool:"""IncludeByBlockByLayer { get; set; } -> bool"""
    def __init__(self) -> ColorDialog:...
    def SetDialogTabs(self, value: ColorDialog.ColorTabs):...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
    class ColorTabs(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
        ACITab: int
        ColorBookTab: int
        TrueColorTab: int
        value__: int
class ContextMenuExtension(Menu, _n_5_t_5):
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    @property
    def Popup(self) -> _n_5_t_6:
        """Popup Event: EventHandler"""
    def __init__(self) -> ContextMenuExtension:...
class DefaultPane(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    All: int
    CursorCoordinates: int
    DynamicInput: int
    DynamicUcs: int
    Float: int
    Grid: int
    LayoutIcon: int
    LayoutModelIcons: int
    LayoutMoreIcon: int
    LineWeight: int
    Model: int
    ModelIcon: int
    ModeMacro: int
    ObjectSnap: int
    ObjectTrack: int
    Ortho: int
    Paper: int
    PaperModel: int
    Polar: int
    Snap: int
    Spacer: int
    Table: int
    value__: int
    ViewportMaximize: int
    ViewportMaximizeNext: int
    ViewportMaximizePrevious: int
class DockSides(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    Bottom: int
    Left: int
    _None: int
    Right: int
    Top: int
    value__: int
class DocumentWindow(Window, _n_5_t_5, _n_12_t_0):
    @property
    def CanClose(self) -> bool:"""CanClose { get; } -> bool"""
    @property
    def Document(self) -> object:"""Document { get; } -> object"""
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    @property
    def DocumentWindowLoaded(self) -> DocumentWindowLoadedEventHandler:
        """DocumentWindowLoaded Event: DocumentWindowLoadedEventHandler"""
    def Activate(self):...
class DocumentWindowLoadedEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> DocumentWindowLoadedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_5_t_11, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: _n_5_t_11):...
class DrawingDocumentWindow(DocumentWindow, _n_5_t_5, _n_12_t_0):
    pass
class DropTarget(object):
    def OnDragEnter(self, e: _n_11_t_1):...
    def OnDragLeave(self):...
    def OnDragOver(self, e: _n_11_t_1):...
    def OnDrop(self, e: _n_11_t_1):...
class IconType(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    Critical: int
    Information: int
    _None: int
    value__: int
    Warning: int
class InfoCenter(object):
    m_pToolbarMoveDelegate: int
    m_pToolbarResizeDelegate: int
    mInitWidth: int
    @property
    def Host(self) -> _n_12_t_1:"""Host { get; set; } -> HwndSource"""
    @property
    def KeepFocus(self) -> bool:"""KeepFocus { get; set; } -> bool"""
    @property
    def SubAwareClientInfo(self) -> str:"""SubAwareClientInfo { get; } -> str"""
    @property
    def UPIXMLData(self) -> str:"""UPIXMLData { get; } -> str"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    def __init__(self) -> InfoCenter:...
    def InfoToolbarSizeChanged(self, bExpand: bool):...
    def InvokeToolbarMoveEvent(self):...
    def InvokeToolbarResizeEvent(self, width: int):...
    def LaunchSubAwareModule(self, resReqid: int, strCourseId: str, strModuleId: str):...
class InfoToolbarMoveDelegate(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> InfoToolbarMoveDelegate:...
    def BeginInvoke(self, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self):...
class InfoToolbarResizeTo(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> InfoToolbarResizeTo:...
    def BeginInvoke(self, width: int, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, width: int):...
class LayerTransparencyDialog(object):
    @property
    def Percent(self) -> _n_5_t_13:"""Percent { get; set; } -> UInt32"""
    def __init__(self) -> LayerTransparencyDialog:...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
class LinetypeDialog(object):
    @property
    def IncludeByBlockByLayer(self) -> bool:"""IncludeByBlockByLayer { get; set; } -> bool"""
    @property
    def Linetype(self) -> _n_2_t_0:"""Linetype { get; set; } -> ObjectId"""
    def __init__(self) -> LinetypeDialog:...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
class LineWeightDialog(object):
    @property
    def IncludeByBlockByLayer(self) -> bool:"""IncludeByBlockByLayer { get; set; } -> bool"""
    @property
    def LineWeight(self) -> _n_2_t_1:"""LineWeight { get; set; } -> LineWeight"""
    def __init__(self) -> LineWeightDialog:...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
class Menu(object):
    @property
    def MenuItems(self) -> MenuItemCollection:"""MenuItems { get; } -> MenuItemCollection"""
class MenuItem(Menu, _n_4_t_0):
    def __init__(self, value: str, icon: _n_8_t_0) -> MenuItem:...
    def __init__(self, value: str) -> MenuItem:...
class MenuItemCollection(_n_6_t_0, _n_7_t_0[_n_4_t_0], typing.Iterable[typing.Any]):
    def __init__(self, owner: Menu) -> MenuItemCollection:...
class OpenFileDialog(object):
    @property
    def Filename(self) -> str:"""Filename { get; } -> str"""
    def __init__(self, title: str, defaultName: str, extension: str, dialogName: str, flags: OpenFileDialog.OpenFileDialogFlags) -> OpenFileDialog:...
    def GetFilenames(self) -> _n_5_t_14[str]:...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
    class OpenFileDialogFlags(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
        AllowAnyExtension: int
        AllowFoldersOnly: int
        AllowMultiple: int
        DefaultIsFolder: int
        DoNotTransferRemoteFiles: int
        ForceDefaultFolder: int
        NoFtpSites: int
        NoShellExtensions: int
        NoUrls: int
        SearchPath: int
        value__: int
class Palette(object):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PaletteSet(self) -> PaletteSet:"""PaletteSet { get; } -> PaletteSet"""
class PaletteActivatedEventArgs(_n_5_t_11):
    @property
    def Activated(self) -> Palette:"""Activated { get; } -> Palette"""
    @property
    def Deactivated(self) -> Palette:"""Deactivated { get; } -> Palette"""
    def __init__(self, activated: Palette, deactivated: Palette) -> PaletteActivatedEventArgs:...
class PaletteActivatedEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteActivatedEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteActivatedEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteActivatedEventArgs):...
class PaletteAddContextMenuEventArgs(_n_5_t_11):
    @property
    def HitFlag(self) -> int:"""HitFlag { get; } -> int"""
    @property
    def MenuItems(self) -> _n_7_t_1[MenuItem]:"""MenuItems { get; } -> List"""
    @property
    def RemoveMenuItems(self) -> _n_7_t_1[int]:"""RemoveMenuItems { get; } -> List"""
    @property
    def RightClickTab(self) -> int:"""RightClickTab { get; } -> int"""
    def __init__(self, menuitems: _n_7_t_1[MenuItem], removeMenuItems: _n_7_t_1[int], nHitFlag: int, nRightClkTab: int) -> PaletteAddContextMenuEventArgs:...
class PaletteAddContextMenuEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteAddContextMenuEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteAddContextMenuEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteAddContextMenuEventArgs):...
class PalettePersistEventArgs(_n_5_t_11):
    @property
    def ConfigurationSection(self) -> _n_0_t_0:"""ConfigurationSection { get; } -> IConfigurationSection"""
    def __init__(self, configurationSection: _n_0_t_0) -> PalettePersistEventArgs:...
class PalettePersistEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PalettePersistEventHandler:...
    def BeginInvoke(self, sender: object, e: PalettePersistEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PalettePersistEventArgs):...
class PaletteSet(Window, _n_5_t_5, _n_12_t_0, _n_6_t_1, typing.Iterable[typing.Any]):
    @property
    def Anchored(self) -> bool:"""Anchored { get; } -> bool"""
    @property
    def AutoRollUp(self) -> bool:"""AutoRollUp { get; set; } -> bool"""
    @property
    def DarkThemedIcon(self) -> _n_8_t_0:"""DarkThemedIcon { get; set; } -> Icon"""
    @property
    def Dock(self) -> DockSides:"""Dock { get; set; } -> DockSides"""
    @property
    def DockEnabled(self) -> DockSides:"""DockEnabled { get; set; } -> DockSides"""
    @property
    def Icon(self) -> _n_8_t_0:"""Icon { get; set; } -> Icon"""
    @property
    def Item(self) -> Palette:"""Item { get; } -> Palette"""
    @property
    def KeepFocus(self) -> bool:"""KeepFocus { get; set; } -> bool"""
    @property
    def LargeDarkThemedIcon(self) -> _n_8_t_0:"""LargeDarkThemedIcon { get; set; } -> Icon"""
    @property
    def LargeLightThemedIcon(self) -> _n_8_t_0:"""LargeLightThemedIcon { get; set; } -> Icon"""
    @property
    def LightThemedIcon(self) -> _n_8_t_0:"""LightThemedIcon { get; set; } -> Icon"""
    @property
    def Location(self) -> _n_8_t_1:"""Location { get; set; } -> Point"""
    @property
    def MinimumSize(self) -> _n_8_t_2:"""MinimumSize { get; set; } -> Size"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Opacity(self) -> int:"""Opacity { get; set; } -> int"""
    @property
    def PaletteSize(self) -> _n_10_t_0:"""PaletteSize { get; } -> Size"""
    @property
    def RolledUp(self) -> bool:"""RolledUp { get; set; } -> bool"""
    @property
    def Size(self) -> _n_8_t_2:"""Size { get; set; } -> Size"""
    @property
    def Style(self) -> PaletteSetStyles:"""Style { get; set; } -> PaletteSetStyles"""
    @property
    def TitleBarLocation(self) -> PaletteSetTitleBarLocation:"""TitleBarLocation { get; set; } -> PaletteSetTitleBarLocation"""
    @property
    def Focused(self) -> PaletteSetFocusedEventHandler:
        """Focused Event: PaletteSetFocusedEventHandler"""
    @property
    def Help(self) -> PaletteSetHelpEventHandler:
        """Help Event: PaletteSetHelpEventHandler"""
    @property
    def Load(self) -> PalettePersistEventHandler:
        """Load Event: PalettePersistEventHandler"""
    @property
    def PaletteActivated(self) -> PaletteActivatedEventHandler:
        """PaletteActivated Event: PaletteActivatedEventHandler"""
    @property
    def PaletteAddContextMenu(self) -> PaletteAddContextMenuEventHandler:
        """PaletteAddContextMenu Event: PaletteAddContextMenuEventHandler"""
    @property
    def PaletteSetDestroy(self) -> PaletteSetDestroyEventHandler:
        """PaletteSetDestroy Event: PaletteSetDestroyEventHandler"""
    @property
    def PaletteSetMoved(self) -> PaletteSetMoveEventHandler:
        """PaletteSetMoved Event: PaletteSetMoveEventHandler"""
    @property
    def PaletteSetShowDockBar(self) -> PaletteSetShowDockBarEventHandler:
        """PaletteSetShowDockBar Event: PaletteSetShowDockBarEventHandler"""
    @property
    def PaletteSetTitleBarLocationChange(self) -> PaletteSetTitleBarLocationChangeEventHandler:
        """PaletteSetTitleBarLocationChange Event: PaletteSetTitleBarLocationChangeEventHandler"""
    @property
    def Save(self) -> PalettePersistEventHandler:
        """Save Event: PalettePersistEventHandler"""
    @property
    def Saving(self) -> PalettePersistEventHandler:
        """Saving Event: PalettePersistEventHandler"""
    @property
    def SizeChanged(self) -> PaletteSetSizeEventHandler:
        """SizeChanged Event: PaletteSetSizeEventHandler"""
    @property
    def StateChanged(self) -> PaletteSetStateEventHandler:
        """StateChanged Event: PaletteSetStateEventHandler"""
    def __init__(self, name: str, cmd: str, toolID: _n_5_t_15) -> PaletteSet:...
    def __init__(self, name: str, toolID: _n_5_t_15) -> PaletteSet:...
    def __init__(self, name: str) -> PaletteSet:...
    def Activate(self, index: int):...
    def Add(self, name: str, htmlPage: _n_5_t_16) -> Palette:...
    def Add(self, name: str, control: _n_11_t_2) -> Palette:...
    def AddVisual(self, name: str, control: _n_13_t_0, bResizeContentToPaletteSize: bool) -> Palette:...
    def AddVisual(self, name: str, control: _n_13_t_0) -> Palette:...
    def EnableTransparency(self, value: bool) -> bool:...
    def FloatControl(self, value: _n_10_t_1):...
    def FloatControl(self, pointOnScreen: _n_10_t_2):...
    def GetThemedIcon(self, bBigIcon: bool) -> _n_8_t_0:...
    def InitializeFloatingPosition(self, value: _n_10_t_1):...
    def RecalculateDockSiteLayout(self):...
    def Remove(self, index: int):...
    def SetThemedIcon(self, value: _n_8_t_0, theme: _n_3_t_0):...
class PaletteSetDestroyEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetDestroyEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_5_t_11, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: _n_5_t_11):...
class PaletteSetDockSite(object):
    def __init__(self) -> PaletteSetDockSite:...
    def CanDock(self, mousePosition: _n_10_t_2) -> _n_5_t_0[_n_10_t_1]:...
    def Dock(self, paletteset: PaletteSet) -> bool:...
    def Initialize(self, paletteset: PaletteSet, desiredSize: _n_10_t_0, dockSyle: int):...
    def Uninitialize(self):...
class PaletteSetFocusedEventArgs(_n_5_t_11):
    def __init__(self) -> PaletteSetFocusedEventArgs:...
class PaletteSetFocusedEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetFocusedEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteSetFocusedEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteSetFocusedEventArgs):...
class PaletteSetHelpEventArgs(_n_5_t_11):
    def __init__(self) -> PaletteSetHelpEventArgs:...
class PaletteSetHelpEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetHelpEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteSetHelpEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteSetHelpEventArgs):...
class PaletteSetMoveEventArgs(_n_5_t_11):
    @property
    def X(self) -> int:"""X { get; } -> int"""
    @property
    def y(self) -> int:"""y { get; } -> int"""
    def __init__(self, x: int, y: int) -> PaletteSetMoveEventArgs:...
class PaletteSetMoveEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetMoveEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteSetMoveEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteSetMoveEventArgs):...
class PaletteSetShowDockBarEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetShowDockBarEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteShowDockBarEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteShowDockBarEventArgs):...
class PaletteSetSizeEventArgs(_n_5_t_11):
    @property
    def DeviceIndependentHeight(self) -> float:"""DeviceIndependentHeight { get; } -> float"""
    @property
    def DeviceIndependentWidth(self) -> float:"""DeviceIndependentWidth { get; } -> float"""
    @property
    def Height(self) -> int:"""Height { get; } -> int"""
    @property
    def Width(self) -> int:"""Width { get; } -> int"""
    def __init__(self, cx: int, cy: int, dx: float, dy: float) -> PaletteSetSizeEventArgs:...
class PaletteSetSizeEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetSizeEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteSetSizeEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteSetSizeEventArgs):...
class PaletteSetStateEventArgs(_n_5_t_11):
    @property
    def NewState(self) -> StateEventIndex:"""NewState { get; } -> StateEventIndex"""
    def __init__(self, state: StateEventIndex) -> PaletteSetStateEventArgs:...
class PaletteSetStateEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetStateEventHandler:...
    def BeginInvoke(self, sender: object, e: PaletteSetStateEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: PaletteSetStateEventArgs):...
class PaletteSetStyles(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    NameEditable: int
    Notify: int
    NoTitleBar: int
    PauseAutoRollupForChildModalDialog: int
    ShowAutoHideButton: int
    ShowCloseButton: int
    ShowPropertiesMenu: int
    ShowTabForSingle: int
    SingleColDock: int
    SingleRowDock: int
    SingleRowNoVertResize: int
    Snappable: int
    UsePaletteNameAsTitleForSingle: int
    value__: int
class PaletteSetTitleBarLocation(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    Left: int
    Right: int
    value__: int
class PaletteSetTitleBarLocationChangeEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> PaletteSetTitleBarLocationChangeEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_5_t_11, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: _n_5_t_11):...
class PaletteShowDockBarEventArgs(_n_5_t_11):
    @property
    def ShowDockBar(self) -> bool:"""ShowDockBar { get; } -> bool"""
    def __init__(self, bShowDockBar: bool) -> PaletteShowDockBarEventArgs:...
class Pane(StatusBarItem, _n_5_t_5):
    @property
    def MaximumWidth(self) -> int:"""MaximumWidth { get; set; } -> int"""
    @property
    def MinimumWidth(self) -> int:"""MinimumWidth { get; set; } -> int"""
    @property
    def Style(self) -> PaneStyles:"""Style { get; set; } -> PaneStyles"""
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    def __init__(self) -> Pane:...
class PaneCollection(_n_6_t_0, typing.Iterable[typing.Any]):
    pass
class PaneStyles(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    Command: int
    NoBorders: int
    Normal: int
    PopOut: int
    PopUp: int
    Stretch: int
    value__: int
class PlotStyleDialog(object):
    @property
    def IncludeByBlockByLayer(self) -> bool:"""IncludeByBlockByLayer { get; set; } -> bool"""
    @property
    def PlotStyle(self) -> str:"""PlotStyle { get; set; } -> str"""
    def __init__(self) -> PlotStyleDialog:...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
class SaveFileDialog(object):
    @property
    def Filename(self) -> str:"""Filename { get; } -> str"""
    def __init__(self, title: str, defaultName: str, extension: str, dialogName: str, flags: SaveFileDialog.SaveFileDialogFlags) -> SaveFileDialog:...
    def ShowDialog(self) -> _n_11_t_0:...
    def ShowModal(self) -> _n_5_t_0[bool]:...
    class SaveFileDialogFlags(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
        AllowAnyExtension: int
        DefaultIsFolder: int
        DoNotTransferRemoteFiles: int
        DoNotWarnIfFileExist: int
        ForceDefaultFolder: int
        NoFtpSites: int
        NoShellExtensions: int
        NoUrls: int
        value__: int
class StateEventIndex(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    Hide: int
    Show: int
    ThemeChange: int
    value__: int
class StatusBar(object):
    @property
    def Panes(self) -> PaneCollection:"""Panes { get; } -> PaneCollection"""
    @property
    def TrayItems(self) -> TrayItemCollection:"""TrayItems { get; } -> TrayItemCollection"""
    @property
    def Window(self) -> Window:"""Window { get; } -> Window"""
    def CloseBubbleWindows(self):...
    def GetDefaultPane(self, pane: DefaultPane) -> Pane:...
    def RemoveDefaultPane(self, pane: DefaultPane):...
    def Update(self):...
class StatusBarItem(_n_4_t_1, _n_5_t_5):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def Icon(self) -> _n_8_t_0:"""Icon { get; set; } -> Icon"""
    @property
    def ToolTipText(self) -> str:"""ToolTipText { get; set; } -> str"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    @property
    def Deleted(self) -> _n_5_t_6:
        """Deleted Event: EventHandler"""
    @property
    def MouseDown(self) -> StatusBarMouseDownEventHandler:
        """MouseDown Event: StatusBarMouseDownEventHandler"""
    def DisplayContextMenu(self, menu: _n_11_t_3, p: _n_8_t_1):...
    def PointToClient(self, p: _n_8_t_1) -> _n_8_t_1:...
    def PointToScreen(self, p: _n_8_t_1) -> _n_8_t_1:...
class StatusBarMouseDownEventArgs(_n_5_t_11):
    @property
    def Button(self) -> _n_11_t_4:"""Button { get; } -> MouseButtons"""
    @property
    def DoubleClick(self) -> bool:"""DoubleClick { get; } -> bool"""
    @property
    def X(self) -> int:"""X { get; } -> int"""
    @property
    def Y(self) -> int:"""Y { get; } -> int"""
class StatusBarMouseDownEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> StatusBarMouseDownEventHandler:...
    def BeginInvoke(self, sender: object, e: StatusBarMouseDownEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: StatusBarMouseDownEventArgs):...
class TrayItem(StatusBarItem, _n_5_t_5):
    def __init__(self) -> TrayItem:...
    def CloseBubbleWindows(self):...
    def ShowBubbleWindow(self, bubble: TrayItemBubbleWindow):...
class TrayItemBubbleWindow(_n_4_t_1, _n_5_t_5):
    @property
    def HyperLink(self) -> str:"""HyperLink { get; set; } -> str"""
    @property
    def HyperText(self) -> str:"""HyperText { get; set; } -> str"""
    @property
    def IconType(self) -> IconType:"""IconType { get; set; } -> IconType"""
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    @property
    def Text2(self) -> str:"""Text2 { get; set; } -> str"""
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    @property
    def Closed(self) -> TrayItemBubbleWindowClosedEventHandler:
        """Closed Event: TrayItemBubbleWindowClosedEventHandler"""
    def __init__(self) -> TrayItemBubbleWindow:...
class TrayItemBubbleWindowClosedEventArgs(_n_5_t_11):
    @property
    def CloseReason(self) -> TrayItemBubbleWindowCloseReason:"""CloseReason { get; } -> TrayItemBubbleWindowCloseReason"""
class TrayItemBubbleWindowClosedEventHandler(_n_5_t_7, _n_5_t_8, _n_9_t_0):
    def __init__(self, A_0: object, A_1: _n_5_t_9) -> TrayItemBubbleWindowClosedEventHandler:...
    def BeginInvoke(self, sender: object, e: TrayItemBubbleWindowClosedEventArgs, callback: _n_5_t_12, obj: object) -> _n_5_t_10:...
    def EndInvoke(self, result: _n_5_t_10):...
    def Invoke(self, sender: object, e: TrayItemBubbleWindowClosedEventArgs):...
class TrayItemBubbleWindowCloseReason(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
    ClosedByUser: int
    DocumentDeactivated: int
    FailedToCreate: int
    HyperlinkClicked: int
    NoIcons: int
    NoNotifications: int
    TimedOut: int
    value__: int
class TrayItemCollection(_n_6_t_0, typing.Iterable[typing.Any]):
    pass
class Visuals(object):
    @property
    def ApplicationIcon(self) -> _n_8_t_0:"""ApplicationIcon { get; } -> Icon"""
    @property
    def PickBitmap(self) -> _n_8_t_3:"""PickBitmap { get; } -> Image"""
    @property
    def PickSetBitmap(self) -> _n_8_t_3:"""PickSetBitmap { get; } -> Image"""
class Window(_n_4_t_1, _n_5_t_5, _n_12_t_0):
    @property
    def DeviceIndependentLocation(self) -> _n_10_t_2:"""DeviceIndependentLocation { get; set; } -> Point"""
    @property
    def DeviceIndependentSize(self) -> _n_10_t_0:"""DeviceIndependentSize { get; set; } -> Size"""
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    @property
    def UnmanagedWindow(self) -> _n_5_t_9:"""UnmanagedWindow { get; } -> IntPtr"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    @property
    def WindowState(self) -> Window.State:"""WindowState { get; set; } -> Window.State"""
    def Close(self):...
    def Focus(self) -> bool:...
    @staticmethod
    def FromHandle(handle: _n_5_t_9) -> Window:...
    @staticmethod
    def GetDeviceIndependentScale(hWnd: _n_5_t_9) -> _n_10_t_3:...
    def GetIcon(self) -> _n_8_t_0:
        """Extension from: Autodesk.AutoCAD.Windows.WindowExtension"""
    def GetLocation(self) -> _n_8_t_1:
        """Extension from: Autodesk.AutoCAD.Windows.WindowExtension"""
    def GetSize(self) -> _n_8_t_2:
        """Extension from: Autodesk.AutoCAD.Windows.WindowExtension"""
    def SetIcon(self, value: _n_8_t_0):
        """Extension from: Autodesk.AutoCAD.Windows.WindowExtension"""
    def SetLocation(self, value: _n_8_t_1):
        """Extension from: Autodesk.AutoCAD.Windows.WindowExtension"""
    def SetSize(self, value: _n_8_t_2):
        """Extension from: Autodesk.AutoCAD.Windows.WindowExtension"""
    class State(_n_5_t_1, _n_5_t_2, _n_5_t_3, _n_5_t_4):
        Maximized: int
        Minimized: int
        Normal: int
        value__: int
class WindowExtension(object):
    @staticmethod
    def GetIcon(window: Window) -> _n_8_t_0:...
    @staticmethod
    def GetLocation(window: Window) -> _n_8_t_1:...
    @staticmethod
    def GetSize(window: Window) -> _n_8_t_2:...
    @staticmethod
    def SetIcon(window: Window, value: _n_8_t_0):...
    @staticmethod
    def SetLocation(window: Window, value: _n_8_t_1):...
    @staticmethod
    def SetSize(window: Window, value: _n_8_t_2):...
class WPFDocumentWindow(DocumentWindow, _n_5_t_5, _n_12_t_0):
    def __init__(self, wpfVisual: _n_13_t_0) -> WPFDocumentWindow:...
