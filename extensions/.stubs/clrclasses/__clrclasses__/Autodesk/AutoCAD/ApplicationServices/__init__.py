import __clrclasses__.Autodesk.AutoCAD.ApplicationServices.Core as Core
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices.Core import Application as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectIdCollection as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LongTransaction as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Database as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import TextEditor as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ITextEditorSelectable as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import TextEditorParagraph as _n_2_t_5
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Field as _n_2_t_6
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DBText as _n_2_t_7
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_2_t_8
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import MText as _n_2_t_9
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import IdMapping as _n_2_t_10
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import TransactionManager as _n_2_t_11
from __clrclasses__.Autodesk.AutoCAD.EditorInput import Editor as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.EditorInput import SelectionSet as _n_3_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_4_t_0
from __clrclasses__.Autodesk.AutoCAD.GraphicsSystem import Manager as _n_5_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXClass as _n_6_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_6_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_6_t_2
from __clrclasses__.Autodesk.AutoCAD.Windows import InfoCenter as _n_7_t_0
from __clrclasses__.Autodesk.AutoCAD.Windows import Window as _n_7_t_1
from __clrclasses__.Autodesk.AutoCAD.Windows import StatusBar as _n_7_t_2
from __clrclasses__.Autodesk.AutoCAD.Windows import ContextMenuExtension as _n_7_t_3
from __clrclasses__.Autodesk.AutoCAD.Windows import DropTarget as _n_7_t_4
from __clrclasses__.Autodesk.AutoCAD.Windows import DocumentWindow as _n_7_t_5
from __clrclasses__.Autodesk.AutoCAD.Windows.Data import DataBindings as _n_8_t_0
from __clrclasses__.System import EventHandler as _n_9_t_0
from __clrclasses__.System import IntPtr as _n_9_t_1
from __clrclasses__.System import EventArgs as _n_9_t_2
from __clrclasses__.System import MulticastDelegate as _n_9_t_3
from __clrclasses__.System import ICloneable as _n_9_t_4
from __clrclasses__.System import IAsyncResult as _n_9_t_5
from __clrclasses__.System import AsyncCallback as _n_9_t_6
from __clrclasses__.System import Attribute as _n_9_t_7
from __clrclasses__.System import IDisposable as _n_9_t_8
from __clrclasses__.System import MarshalByRefObject as _n_9_t_9
from __clrclasses__.System import Func as _n_9_t_10
from __clrclasses__.System import Tuple as _n_9_t_11
from __clrclasses__.System import UInt32 as _n_9_t_12
from __clrclasses__.System import Enum as _n_9_t_13
from __clrclasses__.System import IComparable as _n_9_t_14
from __clrclasses__.System import IFormattable as _n_9_t_15
from __clrclasses__.System import IConvertible as _n_9_t_16
from __clrclasses__.System import Uri as _n_9_t_17
from __clrclasses__.System import Array as _n_9_t_18
from __clrclasses__.System import ValueType as _n_9_t_19
from __clrclasses__.System.Collections import Hashtable as _n_10_t_0
from __clrclasses__.System.Collections import ICollection as _n_10_t_1
from __clrclasses__.System.Collections import IList as _n_10_t_2
from __clrclasses__.System.Collections.Generic import IList as _n_11_t_0
from __clrclasses__.System.Collections.Generic import IReadOnlyList as _n_11_t_1
from __clrclasses__.System.Collections.ObjectModel import ReadOnlyObservableCollection as _n_12_t_0
from __clrclasses__.System.Collections.Specialized import INotifyCollectionChanged as _n_13_t_0
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_14_t_0
from __clrclasses__.System.Drawing import Point as _n_15_t_0
from __clrclasses__.System.Drawing import Size as _n_15_t_1
from __clrclasses__.System.Drawing import Bitmap as _n_15_t_2
from __clrclasses__.System.Runtime.CompilerServices import INotifyCompletion as _n_16_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_17_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_18_t_0
from __clrclasses__.System.Threading.Tasks import Task as _n_19_t_0
from __clrclasses__.System.Windows import DependencyObject as _n_20_t_0
from __clrclasses__.System.Windows import DragDropEffects as _n_20_t_1
from __clrclasses__.System.Windows import Point as _n_20_t_2
from __clrclasses__.System.Windows import Size as _n_20_t_3
from __clrclasses__.System.Windows.Forms import Control as _n_21_t_0
from __clrclasses__.System.Windows.Forms import DragDropEffects as _n_21_t_1
from __clrclasses__.System.Windows.Forms import HelpEventArgs as _n_21_t_2
from __clrclasses__.System.Windows.Forms import DialogResult as _n_21_t_3
from __clrclasses__.System.Windows.Forms import Form as _n_21_t_4
from __clrclasses__.System.Windows.Forms import IWin32Window as _n_21_t_5
from __clrclasses__.System.Windows.Interop import MSG as _n_22_t_0
from __clrclasses__.System.Windows.Media.Imaging import BitmapSource as _n_23_t_0
import typing
class Application(_n_0_t_0):
    @property
    def AcadApplication(self) -> object:"""AcadApplication { get; } -> object"""
    @property
    def DisplayTextScreen(self) -> bool:"""DisplayTextScreen { get; set; } -> bool"""
    @property
    def DocumentWindowCollection(self) -> DocumentWindowCollection:"""DocumentWindowCollection { get; } -> DocumentWindowCollection"""
    @property
    def InfoCenter(self) -> _n_7_t_0:"""InfoCenter { get; } -> InfoCenter"""
    @property
    def IsInCustomizationMode(self) -> bool:"""IsInCustomizationMode { get; set; } -> bool"""
    @property
    def IsSteelInstalled(self) -> bool:"""IsSteelInstalled { get; } -> bool"""
    @property
    def MenuBar(self) -> object:"""MenuBar { get; } -> object"""
    @property
    def MenuGroups(self) -> object:"""MenuGroups { get; } -> object"""
    @property
    def NonInPlaceMainWindow(self) -> _n_7_t_1:"""NonInPlaceMainWindow { get; } -> Window"""
    @property
    def Preferences(self) -> object:"""Preferences { get; } -> object"""
    @property
    def StatusBar(self) -> _n_7_t_2:"""StatusBar { get; } -> StatusBar"""
    @property
    def UIBindings(self) -> _n_8_t_0:"""UIBindings { get; } -> DataBindings"""
    @property
    def BeginCustomizationMode(self) -> _n_9_t_0:
        """BeginCustomizationMode Event: EventHandler"""
    @property
    def DisplayingCustomizeDialog(self) -> TabbedDialogEventHandler:
        """DisplayingCustomizeDialog Event: TabbedDialogEventHandler"""
    @property
    def DisplayingDraftingSettingsDialog(self) -> TabbedDialogEventHandler:
        """DisplayingDraftingSettingsDialog Event: TabbedDialogEventHandler"""
    @property
    def DisplayingOptionDialog(self) -> TabbedDialogEventHandler:
        """DisplayingOptionDialog Event: TabbedDialogEventHandler"""
    @property
    def EndCustomizationMode(self) -> _n_9_t_0:
        """EndCustomizationMode Event: EventHandler"""
    @staticmethod
    def AddDefaultContextMenuExtension(menuExtension: _n_7_t_3):...
    @staticmethod
    def AddObjectContextMenuExtension(runtimeClass: _n_6_t_0, menuExtension: _n_7_t_3):...
    @staticmethod
    def DoDragDrop(dragSource: _n_20_t_0, data: object, allowedEffects: _n_20_t_1, target: _n_7_t_4):...
    @staticmethod
    def DoDragDrop(control: _n_21_t_0, data: object, allowedEffects: _n_21_t_1, target: _n_7_t_4):...
    @staticmethod
    def InvokeContextHelp(window: _n_9_t_1, contextId: int, helpPrefix: str, hlpevent: _n_21_t_2):...
    @staticmethod
    def InvokeContextHelp(window: _n_9_t_1, contextId: int, helpPrefix: str):...
    @staticmethod
    def InvokeContextHelp(window: _n_9_t_1, contextId: int):...
    @staticmethod
    def InvokeHelp(fileName: str, topic: str):...
    @staticmethod
    def InvokeHelpForExternal(functionName: str) -> bool:...
    @staticmethod
    def IsConnectEnabled() -> bool:...
    @staticmethod
    def LoadMainMenu(filename: str) -> bool:...
    @staticmethod
    def LoadPartialMenu(filename: str) -> bool:...
    @staticmethod
    def PostSearchQuery(searchString: str):...
    @staticmethod
    def ReloadAllMenus():...
    @staticmethod
    def RemoveDefaultContextMenuExtension(menuExtension: _n_7_t_3):...
    @staticmethod
    def RemoveObjectContextMenuExtension(runtimeClass: _n_6_t_0, menuExtension: _n_7_t_3):...
    @staticmethod
    def SetCurrentWorkspace(workspacename: str) -> bool:...
    @staticmethod
    def ShowModalDialog(owner: _n_9_t_1, formToShow: _n_21_t_4) -> _n_21_t_3:...
    @staticmethod
    def ShowModalDialog(owner: _n_9_t_1, formToShow: _n_21_t_4, persistSizeAndPosition: bool) -> _n_21_t_3:...
    @staticmethod
    def ShowModalDialog(formToShow: _n_21_t_4) -> _n_21_t_3:...
    @staticmethod
    def ShowModalDialog(owner: _n_21_t_5, formToShow: _n_21_t_4) -> _n_21_t_3:...
    @staticmethod
    def ShowModalDialog(owner: _n_21_t_5, formToShow: _n_21_t_4, persistSizeAndPosition: bool) -> _n_21_t_3:...
    @staticmethod
    def ShowModelessDialog(owner: _n_9_t_1, formToShow: _n_21_t_4):...
    @staticmethod
    def ShowModelessDialog(owner: _n_9_t_1, formToShow: _n_21_t_4, persistSizeAndPosition: bool):...
    @staticmethod
    def ShowModelessDialog(formToShow: _n_21_t_4):...
    @staticmethod
    def ShowModelessDialog(owner: _n_21_t_5, formToShow: _n_21_t_4):...
    @staticmethod
    def ShowModelessDialog(owner: _n_21_t_5, formToShow: _n_21_t_4, persistSizeAndPosition: bool):...
    @staticmethod
    def ToSystemDrawingPoint(point: _n_20_t_2) -> _n_15_t_0:...
    @staticmethod
    def ToSystemDrawingSize(point: _n_20_t_3) -> _n_15_t_1:...
    @staticmethod
    def ToSystemWindowsPoint(point: _n_15_t_0) -> _n_20_t_2:...
    @staticmethod
    def ToSystemWindowsSize(point: _n_15_t_1) -> _n_20_t_3:...
    @staticmethod
    def UnloadPartialMenu(filename: str) -> bool:...
class BeginDoubleClickEventArgs(_n_9_t_2):
    @property
    def Location(self) -> _n_4_t_0:"""Location { get; } -> Point3d"""
class BeginDoubleClickEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> BeginDoubleClickEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginDoubleClickEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: BeginDoubleClickEventArgs):...
class CheckingOutEventArgs(_n_9_t_2):
    @property
    def CheckOutSet(self) -> _n_2_t_0:"""CheckOutSet { get; } -> ObjectIdCollection"""
    @property
    def Transaction(self) -> _n_2_t_1:"""Transaction { get; } -> LongTransaction"""
    def __init__(self, longTrans: _n_2_t_1, objCollection: _n_2_t_0) -> CheckingOutEventArgs:...
    def Veto(self):...
class CheckingOutEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> CheckingOutEventHandler:...
    def BeginInvoke(self, sender: object, e: CheckingOutEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: CheckingOutEventArgs):...
class CommandEventArgs(_n_9_t_2):
    @property
    def GlobalCommandName(self) -> str:"""GlobalCommandName { get; } -> str"""
    def __init__(self) -> CommandEventArgs:...
class CommandEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> CommandEventHandler:...
    def BeginInvoke(self, sender: object, e: CommandEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: CommandEventArgs):...
class ConfigurationSectionNameAttribute(_n_9_t_7, _n_17_t_0):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, name: str) -> ConfigurationSectionNameAttribute:...
class DatabaseExtension(object):
    @staticmethod
    def Audit(db: _n_2_t_2, bFixErrors: bool, bCmdLnEcho: bool):...
class Document(_n_6_t_1, _n_9_t_8):
    @property
    def CommandInProgress(self) -> str:"""CommandInProgress { get; } -> str"""
    @property
    def Database(self) -> _n_2_t_2:"""Database { get; } -> Database"""
    @property
    def Editor(self) -> _n_3_t_0:"""Editor { get; } -> Editor"""
    @property
    def FormatForSave(self) -> DocumentSaveFormat:"""FormatForSave { get; } -> DocumentSaveFormat"""
    @property
    def GraphicsManager(self) -> _n_5_t_0:"""GraphicsManager { get; } -> Manager"""
    @property
    def IsActive(self) -> bool:"""IsActive { get; } -> bool"""
    @property
    def IsNamedDrawing(self) -> bool:"""IsNamedDrawing { get; } -> bool"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def TransactionManager(self) -> TransactionManager:"""TransactionManager { get; } -> TransactionManager"""
    @property
    def UserData(self) -> _n_10_t_0:"""UserData { get; } -> Hashtable"""
    @property
    def Window(self) -> _n_7_t_1:"""Window { get; } -> Window"""
    @property
    def BeginDocumentClose(self) -> DocumentBeginCloseEventHandler:
        """BeginDocumentClose Event: DocumentBeginCloseEventHandler"""
    @property
    def BeginDwgOpen(self) -> DrawingOpenEventHandler:
        """BeginDwgOpen Event: DrawingOpenEventHandler"""
    @property
    def CloseAborted(self) -> _n_9_t_0:
        """CloseAborted Event: EventHandler"""
    @property
    def CloseWillStart(self) -> _n_9_t_0:
        """CloseWillStart Event: EventHandler"""
    @property
    def CommandCancelled(self) -> CommandEventHandler:
        """CommandCancelled Event: CommandEventHandler"""
    @property
    def CommandEnded(self) -> CommandEventHandler:
        """CommandEnded Event: CommandEventHandler"""
    @property
    def CommandFailed(self) -> CommandEventHandler:
        """CommandFailed Event: CommandEventHandler"""
    @property
    def CommandWillStart(self) -> CommandEventHandler:
        """CommandWillStart Event: CommandEventHandler"""
    @property
    def EndDwgOpen(self) -> DrawingOpenEventHandler:
        """EndDwgOpen Event: DrawingOpenEventHandler"""
    @property
    def ImpliedSelectionChanged(self) -> _n_9_t_0:
        """ImpliedSelectionChanged Event: EventHandler"""
    @property
    def LayoutSwitched(self) -> LayoutSwitchedEventHandler:
        """LayoutSwitched Event: LayoutSwitchedEventHandler"""
    @property
    def LayoutSwitching(self) -> LayoutSwitchingEventHandler:
        """LayoutSwitching Event: LayoutSwitchingEventHandler"""
    @property
    def LispCancelled(self) -> _n_9_t_0:
        """LispCancelled Event: EventHandler"""
    @property
    def LispEnded(self) -> _n_9_t_0:
        """LispEnded Event: EventHandler"""
    @property
    def LispWillStart(self) -> LispWillStartEventHandler:
        """LispWillStart Event: LispWillStartEventHandler"""
    @property
    def UnknownCommand(self) -> UnknownCommandEventHandler:
        """UnknownCommand Event: UnknownCommandEventHandler"""
    @property
    def ViewChanged(self) -> _n_9_t_0:
        """ViewChanged Event: EventHandler"""
    def DowngradeDocOpen(self, bPromptForSave: bool):...
    def GetLispSymbol(self, name: str) -> object:...
    def LockDocument(self, lockMode: DocumentLockMode, globalCommandName: str, localCommandName: str, promptIfFails: bool) -> DocumentLock:...
    def LockDocument(self) -> DocumentLock:...
    def LockMode(self) -> DocumentLockMode:...
    def LockMode(self, bIncludeMyLocks: bool) -> DocumentLockMode:...
    def PopDbmod(self):...
    def PushDbmod(self):...
    def SendStringToExecute(self, command: str, activate: bool, wrapUpInactiveDoc: bool, echoCommand: bool):...
    def SetLispSymbol(self, name: str, value: object):...
    def TryGetDatabase(self) -> _n_2_t_2:...
    def UpgradeDocOpen(self):...
    def CapturePreviewImage(self, width: _n_9_t_12, height: _n_9_t_12) -> _n_15_t_2:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentExtension"""
    def CloseAndDiscard(self):
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentExtension"""
    def CloseAndSave(self, fileName: str):
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentExtension"""
    def GetAcadDocument(self) -> object:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentExtension"""
    def GetStatusBar(self) -> _n_7_t_2:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentExtension"""
class DocumentActivationChangedEventArgs(_n_9_t_2):
    @property
    def NewValue(self) -> bool:"""NewValue { get; } -> bool"""
class DocumentActivationChangedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentActivationChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentActivationChangedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentActivationChangedEventArgs):...
class DocumentBeginCloseEventArgs(_n_9_t_2):
    def __init__(self) -> DocumentBeginCloseEventArgs:...
    def Veto(self):...
class DocumentBeginCloseEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentBeginCloseEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentBeginCloseEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentBeginCloseEventArgs):...
class DocumentClosedEventArgs(_n_9_t_2):
    @property
    def RecentDocument(self) -> RecentDocument:"""RecentDocument { get; } -> RecentDocument"""
class DocumentClosedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentClosedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentClosedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentClosedEventArgs):...
class DocumentCollection(_n_9_t_9, _n_10_t_1):
    @property
    def CurrentDocument(self) -> Document:"""CurrentDocument { get; set; } -> Document"""
    @property
    def DefaultFormatForSave(self) -> DocumentSaveFormat:"""DefaultFormatForSave { get; set; } -> DocumentSaveFormat"""
    @property
    def DocumentActivationEnabled(self) -> bool:"""DocumentActivationEnabled { get; set; } -> bool"""
    @property
    def IsApplicationContext(self) -> bool:"""IsApplicationContext { get; } -> bool"""
    @property
    def MdiActiveDocument(self) -> Document:"""MdiActiveDocument { get; set; } -> Document"""
    @property
    def DocumentActivated(self) -> DocumentCollectionEventHandler:
        """DocumentActivated Event: DocumentCollectionEventHandler"""
    @property
    def DocumentActivationChanged(self) -> DocumentActivationChangedEventHandler:
        """DocumentActivationChanged Event: DocumentActivationChangedEventHandler"""
    @property
    def DocumentBecameCurrent(self) -> DocumentCollectionEventHandler:
        """DocumentBecameCurrent Event: DocumentCollectionEventHandler"""
    @property
    def DocumentCreated(self) -> DocumentCollectionEventHandler:
        """DocumentCreated Event: DocumentCollectionEventHandler"""
    @property
    def DocumentCreateStarted(self) -> DocumentCollectionEventHandler:
        """DocumentCreateStarted Event: DocumentCollectionEventHandler"""
    @property
    def DocumentCreationCanceled(self) -> DocumentCollectionEventHandler:
        """DocumentCreationCanceled Event: DocumentCollectionEventHandler"""
    @property
    def DocumentDestroyed(self) -> DocumentDestroyedEventHandler:
        """DocumentDestroyed Event: DocumentDestroyedEventHandler"""
    @property
    def DocumentLockModeChanged(self) -> DocumentLockModeChangedEventHandler:
        """DocumentLockModeChanged Event: DocumentLockModeChangedEventHandler"""
    @property
    def DocumentLockModeChangeVetoed(self) -> DocumentLockModeChangeVetoedEventHandler:
        """DocumentLockModeChangeVetoed Event: DocumentLockModeChangeVetoedEventHandler"""
    @property
    def DocumentLockModeWillChange(self) -> DocumentLockModeWillChangeEventHandler:
        """DocumentLockModeWillChange Event: DocumentLockModeWillChangeEventHandler"""
    @property
    def DocumentToBeActivated(self) -> DocumentCollectionEventHandler:
        """DocumentToBeActivated Event: DocumentCollectionEventHandler"""
    @property
    def DocumentToBeDeactivated(self) -> DocumentCollectionEventHandler:
        """DocumentToBeDeactivated Event: DocumentCollectionEventHandler"""
    @property
    def DocumentToBeDestroyed(self) -> DocumentCollectionEventHandler:
        """DocumentToBeDestroyed Event: DocumentCollectionEventHandler"""
    def AppContextNewDocument(self, templateFileName: str):...
    def AppContextOpenDocument(self, fileName: str):...
    def AppContextRecoverDocument(self, fileName: str):...
    def ExecuteInApplicationContext(self, callback: ExecuteInApplicationContextCallback, data: object):...
    def ExecuteInCommandContextAsync(self, callback: _n_9_t_10[object, _n_19_t_0], data: object) -> DocumentCollection.ExecutionResult:...
    def GetDocument(self, db: _n_2_t_2) -> Document:...
    def GetPendingDocumentForSwitch(self) -> _n_9_t_11[bool, Document]:...
    def Add(self, templateFileName: str) -> Document:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentCollectionExtension"""
    def CloseAll(self):
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentCollectionExtension"""
    def Open(self, fileName: str, forReadOnly: bool, password: str) -> Document:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentCollectionExtension"""
    def Open(self, fileName: str, forReadOnly: bool) -> Document:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentCollectionExtension"""
    def Open(self, fileName: str) -> Document:
        """Extension from: Autodesk.AutoCAD.ApplicationServices.DocumentCollectionExtension"""
    class ExecutionResult(_n_16_t_0):
        @property
        def IsCompleted(self) -> bool:"""IsCompleted { get; } -> bool"""
        def GetAwaiter(self) -> DocumentCollection.ExecutionResult:...
        def GetResult(self):...
class DocumentCollectionEventArgs(_n_9_t_2):
    @property
    def Document(self) -> Document:"""Document { get; } -> Document"""
class DocumentCollectionEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentCollectionEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentCollectionEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentCollectionEventArgs):...
class DocumentCollectionExtension(object):
    @staticmethod
    def Add(docCol: DocumentCollection, templateFileName: str) -> Document:...
    @staticmethod
    def CloseAll(docCol: DocumentCollection):...
    @staticmethod
    def Open(docCol: DocumentCollection, fileName: str, forReadOnly: bool, password: str) -> Document:...
    @staticmethod
    def Open(docCol: DocumentCollection, fileName: str, forReadOnly: bool) -> Document:...
    @staticmethod
    def Open(docCol: DocumentCollection, fileName: str) -> Document:...
class DocumentDestroyedEventArgs(_n_9_t_2):
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
class DocumentDestroyedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentDestroyedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentDestroyedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentDestroyedEventArgs):...
class DocumentExtension(object):
    @staticmethod
    def CapturePreviewImage(doc: Document, width: _n_9_t_12, height: _n_9_t_12) -> _n_15_t_2:...
    @staticmethod
    def CloseAndDiscard(doc: Document):...
    @staticmethod
    def CloseAndSave(doc: Document, fileName: str):...
    @staticmethod
    def FromAcadDocument(acadDocument: object) -> Document:...
    @staticmethod
    def GetAcadDocument(doc: Document) -> object:...
    @staticmethod
    def GetStatusBar(doc: Document) -> _n_7_t_2:...
class DocumentLock(_n_9_t_8):
    pass
class DocumentLockMode(_n_9_t_13, _n_9_t_14, _n_9_t_15, _n_9_t_16):
    AutoWrite: int
    ExclusiveWrite: int
    _None: int
    NotLocked: int
    ProtectedAutoWrite: int
    Read: int
    value__: int
    Write: int
class DocumentLockModeChangedEventArgs(_n_9_t_2):
    @property
    def CurrentMode(self) -> DocumentLockMode:"""CurrentMode { get; } -> DocumentLockMode"""
    @property
    def Document(self) -> Document:"""Document { get; } -> Document"""
    @property
    def GlobalCommandName(self) -> str:"""GlobalCommandName { get; } -> str"""
    @property
    def MyCurrentMode(self) -> DocumentLockMode:"""MyCurrentMode { get; } -> DocumentLockMode"""
    @property
    def MyPreviousMode(self) -> DocumentLockMode:"""MyPreviousMode { get; } -> DocumentLockMode"""
    def Veto(self):...
class DocumentLockModeChangedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentLockModeChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentLockModeChangedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentLockModeChangedEventArgs):...
class DocumentLockModeChangeVetoedEventArgs(_n_9_t_2):
    @property
    def Document(self) -> Document:"""Document { get; } -> Document"""
    @property
    def GlobalCommandName(self) -> str:"""GlobalCommandName { get; } -> str"""
class DocumentLockModeChangeVetoedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentLockModeChangeVetoedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentLockModeChangeVetoedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentLockModeChangeVetoedEventArgs):...
class DocumentLockModeWillChangeEventArgs(_n_9_t_2):
    @property
    def CurrentMode(self) -> DocumentLockMode:"""CurrentMode { get; } -> DocumentLockMode"""
    @property
    def Document(self) -> Document:"""Document { get; } -> Document"""
    @property
    def GlobalCommandName(self) -> str:"""GlobalCommandName { get; } -> str"""
    @property
    def MyCurrentMode(self) -> DocumentLockMode:"""MyCurrentMode { get; } -> DocumentLockMode"""
    @property
    def MyNewMode(self) -> DocumentLockMode:"""MyNewMode { get; } -> DocumentLockMode"""
class DocumentLockModeWillChangeEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentLockModeWillChangeEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentLockModeWillChangeEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentLockModeWillChangeEventArgs):...
class DocumentPinStateChangedEventArgs(_n_9_t_2):
    @property
    def RecentDocument(self) -> RecentDocument:"""RecentDocument { get; } -> RecentDocument"""
class DocumentPinStateChangedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentPinStateChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentPinStateChangedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentPinStateChangedEventArgs):...
class DocumentSaveFormat(_n_9_t_13, _n_9_t_14, _n_9_t_15, _n_9_t_16):
    Native: int
    R12Dxf: int
    R13Dwg: int
    R13Dxf: int
    R14Dwg: int
    R14Dxf: int
    R2000Dwg: int
    R2000Dxf: int
    R2000Standard: int
    R2000Template: int
    R2000Xml: int
    R2004Dwg: int
    R2004Dxf: int
    R2004Standard: int
    R2004Template: int
    R2007Dwg: int
    R2007Dxf: int
    R2007Standard: int
    R2007Template: int
    R2010Dwg: int
    R2010Dxf: int
    R2010Standard: int
    R2010Template: int
    R2013Dwg: int
    R2013Dxf: int
    R2013Standard: int
    R2013Template: int
    Unknown: int
    value__: int
class DocumentWindowActivatedEventArgs(_n_9_t_2):
    @property
    def DocumentWindow(self) -> _n_7_t_5:"""DocumentWindow { get; } -> DocumentWindow"""
class DocumentWindowActivatedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DocumentWindowActivatedEventHandler:...
    def BeginInvoke(self, sender: object, e: DocumentWindowActivatedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DocumentWindowActivatedEventArgs):...
class DocumentWindowCollection(_n_10_t_1, _n_13_t_0, _n_9_t_8):
    @property
    def ActiveDocumentWindow(self) -> _n_7_t_5:"""ActiveDocumentWindow { get; } -> DocumentWindow"""
    @property
    def DocumentWindowActivated(self) -> DocumentWindowActivatedEventHandler:
        """DocumentWindowActivated Event: DocumentWindowActivatedEventHandler"""
    def __init__(self) -> DocumentWindowCollection:...
    def AddDocumentWindow(self, title: str, htmlPage: _n_9_t_17) -> _n_7_t_5:...
    def AddDocumentWindow(self, documentWindow: _n_7_t_5) -> bool:...
    def ArrangeIcons(self):...
    def Cascade(self):...
    def LookupDocumentWindow(self, docWindow: object) -> _n_7_t_5:...
    def MoveDocumentWindow(self, documentWindow: _n_7_t_5, newIndex: int) -> bool:...
    def TileHorizontally(self):...
    def TileVertically(self):...
class DrawingOpenEventArgs(_n_9_t_2):
    @property
    def Database(self) -> _n_2_t_2:"""Database { get; } -> Database"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
class DrawingOpenEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> DrawingOpenEventHandler:...
    def BeginInvoke(self, sender: object, e: DrawingOpenEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: DrawingOpenEventArgs):...
class ExecuteInApplicationContextCallback(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> ExecuteInApplicationContextCallback:...
    def BeginInvoke(self, userData: object, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, userData: object):...
class IConfigurationSection(_n_9_t_8):
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    def Close(self):...
    def Contains(self, name: str) -> bool:...
    def ContainsSubsection(self, name: str) -> bool:...
    def CreateSubsection(self, name: str) -> IConfigurationSection:...
    def Delete(self, name: str):...
    def DeleteSubsection(self, name: str):...
    def OpenSubsection(self, name: str) -> IConfigurationSection:...
    def ReadProperty(self, name: str, defaultValue: object) -> object:...
    def WriteProperty(self, name: str, value: object):...
class InplaceTextEditor(_n_2_t_3, _n_9_t_8, _n_2_t_4):
    @property
    def alginment(self) -> _n_2_t_5AlignmentType:"""alginment { get; } -> TextEditorParagraph.AlignmentType"""
    @property
    def Annotative(self) -> bool:"""Annotative { get; set; } -> bool"""
    @property
    def CanCopy(self) -> bool:"""CanCopy { get; } -> bool"""
    @property
    def CanCut(self) -> bool:"""CanCut { get; } -> bool"""
    @property
    def CanExitEditor(self) -> bool:"""CanExitEditor { get; set; } -> bool"""
    @property
    def CanPaste(self) -> bool:"""CanPaste { get; } -> bool"""
    @property
    def CanRedo(self) -> bool:"""CanRedo { get; } -> bool"""
    @property
    def CanUndo(self) -> bool:"""CanUndo { get; } -> bool"""
    @property
    def Current(self) -> InplaceTextEditor:"""Current { get; } -> InplaceTextEditor"""
    @property
    def ForcedOpaqueBackground(self) -> bool:"""ForcedOpaqueBackground { get; } -> bool"""
    @property
    def LayerColor(self) -> _n_1_t_0:"""LayerColor { get; } -> Color"""
    @property
    def MultiAttribute(self) -> bool:"""MultiAttribute { get; } -> bool"""
    @property
    def OpaqueBackground(self) -> bool:"""OpaqueBackground { get; set; } -> bool"""
    @property
    def ParagraphSupported(self) -> bool:"""ParagraphSupported { get; } -> bool"""
    @property
    def RulerHidden(self) -> bool:"""RulerHidden { get; set; } -> bool"""
    @property
    def RulerSupported(self) -> bool:"""RulerSupported { get; } -> bool"""
    @property
    def SimpleMText(self) -> bool:"""SimpleMText { get; } -> bool"""
    @property
    def SpellerEnabled(self) -> bool:"""SpellerEnabled { get; set; } -> bool"""
    @property
    def TableCell(self) -> bool:"""TableCell { get; } -> bool"""
    @property
    def Text(self) -> bool:"""Text { get; } -> bool"""
    @property
    def ToolbarHidden(self) -> bool:"""ToolbarHidden { get; set; } -> bool"""
    @property
    def ToolbarOptionHidden(self) -> bool:"""ToolbarOptionHidden { get; set; } -> bool"""
    @property
    def UndoRecordingDisabled(self) -> bool:"""UndoRecordingDisabled { get; set; } -> bool"""
    @property
    def Wysiwyg(self) -> bool:"""Wysiwyg { get; set; } -> bool"""
    def AddUndoMarker(self, undoType: InplaceTextEditor.TextUndoType):...
    def AttachmentMenus(self, pos: _n_15_t_0, parent: _n_7_t_1):...
    def ColumnMenus(self, pos: _n_15_t_0, parent: _n_7_t_1):...
    def ColumnsDialog(self, staticColumnCount: int):...
    def ContextMenus(self, pos: _n_15_t_0, parent: _n_7_t_1):...
    def Copy(self):...
    def Cut(self):...
    def DrawHightlight(self):...
    def FieldDialog(self, field: _n_2_t_6):...
    def FindAndReplaceDialog(self):...
    def FindMatchItem(self, flags: int, findStr: str):...
    def HelpDialog(self):...
    def HightlightColorDialog(self):...
    def ImportTextDialog(self):...
    def InsertFile(self, filename: str):...
    @staticmethod
    def Invoke(text: _n_2_t_7, appendedEntities: _n_9_t_18[_n_2_t_8]):...
    @staticmethod
    def Invoke(mtext: _n_2_t_9, settings: InplaceTextEditorSettings):...
    def LineSpaceMenus(self, pos: _n_15_t_0, parent: _n_7_t_1):...
    def NewFeatureWorkShop(self):...
    def NumberingMenus(self, pos: _n_15_t_0, parent: _n_7_t_1):...
    def OtherSymbol(self):...
    def ParagraphDialog(self):...
    def Paste(self):...
    def PasteWithoutFormats(self):...
    def Redo(self):...
    def RemoveHightlight(self):...
    def ReplaceAllMatches(self, flags: int, findStr: str, replaceStr: str):...
    def ReplaceCurrentMatch(self, flags: int, findStr: str, replaceStr: str):...
    def SetStaticColumnsWithCount(self, columnCount: int):...
    def SpellDictinaryDialog(self):...
    def SpellSettingDialog(self):...
    def StackPropertyDialog(self):...
    def SymbolMenus(self, pos: _n_15_t_0, parent: _n_7_t_1):...
    def Undo(self):...
    def WipeoutDialog(self):...
    class TextUndoType(_n_9_t_13, _n_9_t_14, _n_9_t_15, _n_9_t_16):
        UndoAnnoState: int
        UndoAttachment: int
        UndoAutoDimBreak: int
        UndoAutoDimension: int
        UndoAutoDTextEscape: int
        UndoAutoField: int
        UndoAutoMifOrCif: int
        UndoAutoSpell: int
        UndoAutoStack: int
        UndoAutoSymbol: int
        UndoBackspace: int
        UndoBoldOff: int
        UndoBoldOn: int
        UndoChangeCase: int
        UndoCharAttributes: int
        UndoColor: int
        UndoColumns: int
        UndoCombineParagraphs: int
        UndoCursorAttributes: int
        UndoCustomConvert: int
        UndoCut: int
        UndoDelete: int
        UndoDeleteAndMoveSelection: int
        UndoDimBreakInsert: int
        UndoDimensionInsert: int
        UndoDimensionSymbol: int
        UndoDimensionTemplate: int
        UndoDimensionTweak: int
        UndoFieldConvert: int
        UndoFieldInsert: int
        UndoFieldUpdate: int
        UndoFont: int
        UndoHeight: int
        UndoImportText: int
        UndoItalicOff: int
        UndoItalicOn: int
        UndoLanguage: int
        UndoObliqueAngle: int
        UndoOverlineOff: int
        UndoOverlineOn: int
        UndoParagraphAttributes: int
        UndoParagraphNumbering: int
        UndoPaste: int
        UndoRemoveAllFormatting: int
        UndoRemoveCharFormatting: int
        UndoRemoveParaFormatting: int
        UndoReplace: int
        UndoReplaceAll: int
        UndoSetDefinedHeight: int
        UndoSetDefinedWidth: int
        UndoStack: int
        UndoStackProperties: int
        UndoStyle: int
        UndoSymbolInsert: int
        UndoTrackingFactor: int
        UndoTyping: int
        UndoUnderlineOff: int
        UndoUnderlineOn: int
        UndoUnstack: int
        UndoWidthScale: int
        UndoWipeout: int
        value__: int
class InplaceTextEditorSettings(_n_6_t_1, _n_9_t_8):
    @property
    def DefinedHeight(self) -> float:"""DefinedHeight { get; set; } -> float"""
    @property
    def Flags(self) -> InplaceTextEditorSettings.EditFlags:"""Flags { get; set; } -> InplaceTextEditorSettings.EditFlags"""
    @property
    def SimpleMText(self) -> bool:"""SimpleMText { get; set; } -> bool"""
    @property
    def TabSupported(self) -> bool:"""TabSupported { get; set; } -> bool"""
    @property
    def Type(self) -> InplaceTextEditorSettings.EntityType:"""Type { get; set; } -> InplaceTextEditorSettings.EntityType"""
    def __init__(self) -> InplaceTextEditorSettings:...
    class EditFlags(_n_9_t_13, _n_9_t_14, _n_9_t_15, _n_9_t_16):
        CursorAtEnd: int
        ForceOpaqueBackground: int
        SelectAll: int
        value__: int
    class EntityType(_n_9_t_13, _n_9_t_14, _n_9_t_15, _n_9_t_16):
        Default: int
        MultiAttribute: int
        TableCell: int
        value__: int
class LayoutSwitchedEventArgs(_n_9_t_2):
    @property
    def NewLayout(self) -> str:"""NewLayout { get; } -> str"""
class LayoutSwitchedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> LayoutSwitchedEventHandler:...
    def BeginInvoke(self, sender: object, e: LayoutSwitchedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: LayoutSwitchedEventArgs):...
class LayoutSwitchingEventArgs(_n_9_t_2):
    @property
    def NewLayout(self) -> str:"""NewLayout { get; } -> str"""
    @property
    def OldLayout(self) -> str:"""OldLayout { get; } -> str"""
class LayoutSwitchingEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> LayoutSwitchingEventHandler:...
    def BeginInvoke(self, sender: object, e: LayoutSwitchingEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: LayoutSwitchingEventArgs):...
class LispWillStartEventArgs(_n_9_t_2):
    @property
    def FirstLine(self) -> str:"""FirstLine { get; } -> str"""
class LispWillStartEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> LispWillStartEventHandler:...
    def BeginInvoke(self, sender: object, e: LispWillStartEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: LispWillStartEventArgs):...
class LongTransactionEventArgs(_n_9_t_2):
    @property
    def Transaction(self) -> _n_2_t_1:"""Transaction { get; } -> LongTransaction"""
    def __init__(self, longTrans: _n_2_t_1) -> LongTransactionEventArgs:...
class LongTransactionEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> LongTransactionEventHandler:...
    def BeginInvoke(self, sender: object, e: LongTransactionEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: LongTransactionEventArgs):...
class LongTransactionManager(_n_6_t_2, _n_9_t_8, _n_9_t_4):
    @property
    def Aborted(self) -> LongTransactionEventHandler:
        """Aborted Event: LongTransactionEventHandler"""
    @property
    def CheckedIn(self) -> LongTransactionEventHandler:
        """CheckedIn Event: LongTransactionEventHandler"""
    @property
    def CheckedOut(self) -> LongTransactionEventHandler:
        """CheckedOut Event: LongTransactionEventHandler"""
    @property
    def CheckingIn(self) -> LongTransactionEventHandler:
        """CheckingIn Event: LongTransactionEventHandler"""
    @property
    def CheckingOut(self) -> CheckingOutEventHandler:
        """CheckingOut Event: CheckingOutEventHandler"""
    def AbortLongTransaction(self, transId: _n_2_t_8, keepObjs: bool):...
    def AddClassFilter(self, filter: _n_6_t_0):...
    def CheckIn(self, transId: _n_2_t_8, errorMap: _n_2_t_10, keepObjs: bool):...
    def CheckOut(self, checkoutSet: _n_2_t_0, toBlock: _n_2_t_8, errorMap: _n_2_t_10, blkRef: _n_2_t_8) -> _n_2_t_8:...
    def CurrentLongTransactionFor(self, doc: Document) -> _n_2_t_8:...
    def IsFiltered(self, A_0: _n_6_t_0) -> bool:...
class Marshaler(object):
    @staticmethod
    def AdsNameToSelectionSet(pointerToAdsName: _n_9_t_1) -> _n_3_t_1:...
    @staticmethod
    def SelectionSetToAdsName(selectionSet: _n_3_t_1, pointerToAdsName: _n_9_t_1):...
class PreTranslateMessageEventArgs(_n_9_t_2):
    @property
    def Handled(self) -> bool:"""Handled { get; set; } -> bool"""
    @property
    def Message(self) -> _n_22_t_0:"""Message { get; set; } -> MSG"""
class PreTranslateMessageEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> PreTranslateMessageEventHandler:...
    def BeginInvoke(self, sender: object, e: PreTranslateMessageEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: PreTranslateMessageEventArgs):...
class ProfileEventArgs(_n_9_t_2):
    @property
    def ProfileName(self) -> str:"""ProfileName { get; } -> str"""
class ProfileEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> ProfileEventHandler:...
    def BeginInvoke(self, sender: object, e: ProfileEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: ProfileEventArgs):...
class RecentDocument(object):
    @property
    def CurrentlyOpenBy(self) -> str:"""CurrentlyOpenBy { get; } -> str"""
    @property
    def IsClosed(self) -> bool:"""IsClosed { get; } -> bool"""
    @property
    def IsPinned(self) -> bool:"""IsPinned { get; set; } -> bool"""
    @property
    def LastOpenedTime(self) -> _n_9_t_19:"""LastOpenedTime { get; } -> ValueType"""
    @property
    def LastSavedBy(self) -> str:"""LastSavedBy { get; } -> str"""
    @property
    def Path(self) -> str:"""Path { get; } -> str"""
    @property
    def Preview(self) -> _n_23_t_0:"""Preview { get; } -> BitmapSource"""
    @property
    def Version(self) -> str:"""Version { get; } -> str"""
class RecentDocumentCollection(_n_12_t_0[RecentDocument], _n_11_t_0[RecentDocument], _n_10_t_2, _n_11_t_1[RecentDocument], _n_13_t_0, _n_14_t_0, _n_9_t_8, typing.Iterable[RecentDocument]):
    @property
    def Instance(self) -> RecentDocumentCollection:"""Instance { get; } -> RecentDocumentCollection"""
    @property
    def UsePinnedItems(self) -> bool:"""UsePinnedItems { get; set; } -> bool"""
    @property
    def DocumentClosed(self) -> DocumentClosedEventHandler:
        """DocumentClosed Event: DocumentClosedEventHandler"""
    @property
    def DocumentPinStateChanged(self) -> DocumentPinStateChangedEventHandler:
        """DocumentPinStateChanged Event: DocumentPinStateChangedEventHandler"""
class SystemVariableChangedEventArgs(_n_9_t_2):
    @property
    def Changed(self) -> bool:"""Changed { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class SystemVariableChangedEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> SystemVariableChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: SystemVariableChangedEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: SystemVariableChangedEventArgs):...
class SystemVariableChangingEventArgs(_n_9_t_2):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class SystemVariableChangingEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> SystemVariableChangingEventHandler:...
    def BeginInvoke(self, sender: object, e: SystemVariableChangingEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: SystemVariableChangingEventArgs):...
class TabbedDialogAction(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> TabbedDialogAction:...
    def BeginInvoke(self, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self):...
class TabbedDialogEventArgs(_n_9_t_2):
    def AddTab(self, name: str, extension: TabbedDialogExtension):...
class TabbedDialogEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> TabbedDialogEventHandler:...
    def BeginInvoke(self, sender: object, e: TabbedDialogEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: TabbedDialogEventArgs):...
class TabbedDialogExtension(object):
    @property
    def Control(self) -> object:"""Control { get; } -> object"""
    @property
    def OnApply(self) -> TabbedDialogAction:"""OnApply { get; } -> TabbedDialogAction"""
    @property
    def OnCancel(self) -> TabbedDialogAction:"""OnCancel { get; } -> TabbedDialogAction"""
    @property
    def OnHelp(self) -> TabbedDialogAction:"""OnHelp { get; } -> TabbedDialogAction"""
    @property
    def OnOk(self) -> TabbedDialogAction:"""OnOk { get; } -> TabbedDialogAction"""
    def __init__(self, control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction, onApply: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: object, onOK: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: _n_21_t_0, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction, onApply: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: _n_21_t_0, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: _n_21_t_0, onOK: TabbedDialogAction, onCancel: TabbedDialogAction) -> TabbedDialogExtension:...
    def __init__(self, control: _n_21_t_0, onOK: TabbedDialogAction) -> TabbedDialogExtension:...
    @staticmethod
    def SetDirty(control: object, dirty: bool):...
    @staticmethod
    def SetDirty(control: _n_21_t_0, dirty: bool):...
class TransactionManager(_n_2_t_11, _n_9_t_8, _n_9_t_4):
    def EnableGraphicsFlush(self, doEnable: bool):...
    def FlushGraphics(self):...
class UnknownCommandEventArgs(_n_9_t_2):
    @property
    def GlobalCommandName(self) -> str:"""GlobalCommandName { get; } -> str"""
class UnknownCommandEventHandler(_n_9_t_3, _n_9_t_4, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_9_t_1) -> UnknownCommandEventHandler:...
    def BeginInvoke(self, sender: object, e: UnknownCommandEventArgs, callback: _n_9_t_6, obj: object) -> _n_9_t_5:...
    def EndInvoke(self, result: _n_9_t_5):...
    def Invoke(self, sender: object, e: UnknownCommandEventArgs):...
class UserConfigurationManager(_n_9_t_9):
    @property
    def CurrentProfileChanged(self) -> ProfileEventHandler:
        """CurrentProfileChanged Event: ProfileEventHandler"""
    @property
    def CurrentProfileChanging(self) -> ProfileEventHandler:
        """CurrentProfileChanging Event: ProfileEventHandler"""
    @property
    def CurrentProfileReset(self) -> ProfileEventHandler:
        """CurrentProfileReset Event: ProfileEventHandler"""
    @property
    def CurrentProfileResetting(self) -> ProfileEventHandler:
        """CurrentProfileResetting Event: ProfileEventHandler"""
    @property
    def CurrentProfileSaved(self) -> ProfileEventHandler:
        """CurrentProfileSaved Event: ProfileEventHandler"""
    @property
    def CurrentProfileSaving(self) -> ProfileEventHandler:
        """CurrentProfileSaving Event: ProfileEventHandler"""
    @property
    def ProfileReset(self) -> ProfileEventHandler:
        """ProfileReset Event: ProfileEventHandler"""
    @property
    def ProfileResetting(self) -> ProfileEventHandler:
        """ProfileResetting Event: ProfileEventHandler"""
    @property
    def ProfileSaved(self) -> ProfileEventHandler:
        """ProfileSaved Event: ProfileEventHandler"""
    @property
    def ProfileSaving(self) -> ProfileEventHandler:
        """ProfileSaving Event: ProfileEventHandler"""
    def OpenCurrentProfile(self) -> IConfigurationSection:...
    def OpenDialogSection(self, dialog: object) -> IConfigurationSection:...
    def OpenGlobalSection(self) -> IConfigurationSection:...
    def SetCurrentProfile(self, profileName: str):...
class WhoHasInfo(_n_9_t_19):
    @property
    def ComputerName(self) -> str:"""ComputerName { get; } -> str"""
    @property
    def IsFileLocked(self) -> bool:"""IsFileLocked { get; } -> bool"""
    @property
    def OpenTime(self) -> str:"""OpenTime { get; } -> str"""
    @property
    def UserName(self) -> str:"""UserName { get; } -> str"""
class XrefFileLock(_n_6_t_1, _n_9_t_8):
    @property
    def OutOfSyncBlockIds(self) -> _n_2_t_0:"""OutOfSyncBlockIds { get; } -> ObjectIdCollection"""
    @property
    def XloadCtlType(self) -> int:"""XloadCtlType { get; } -> int"""
    def ConsistencyCheck(self):...
    @staticmethod
    def ConsistencyCheck(selectedBlockId: _n_2_t_8) -> _n_2_t_0:...
    @staticmethod
    def ConsistencyCheckLocal(selectedBlockId: _n_2_t_8) -> _n_2_t_0:...
    @staticmethod
    def GetXloadCtlType(selectedBlockId: _n_2_t_8) -> int:...
    @staticmethod
    def LockFile(selectedBlockId: _n_2_t_8) -> XrefFileLock:...
    def ReleaseFile(self, skipSaveback: bool, reload: bool):...
    def ReleaseFile(self):...
    def ReloadFile(self, xldCtlType: int):...
    def ReloadFile(self):...
    @staticmethod
    def ReloadFile(blocks: _n_2_t_0, xldCtlType: int):...
    @staticmethod
    def ReloadFile(blocks: _n_2_t_0):...
