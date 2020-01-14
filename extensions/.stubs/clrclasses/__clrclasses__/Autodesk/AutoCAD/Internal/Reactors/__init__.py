from __clrclasses__.Autodesk.AutoCAD.Customization import CustomizationSection as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Customization import Workspace as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Database as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Matrix3d as _n_2_t_0
from __clrclasses__.System import ValueType as _n_3_t_0
from __clrclasses__.System import MulticastDelegate as _n_3_t_1
from __clrclasses__.System import ICloneable as _n_3_t_2
from __clrclasses__.System import IntPtr as _n_3_t_3
from __clrclasses__.System import IAsyncResult as _n_3_t_4
from __clrclasses__.System import EventArgs as _n_3_t_5
from __clrclasses__.System import AsyncCallback as _n_3_t_6
from __clrclasses__.System import IDisposable as _n_3_t_7
from __clrclasses__.System import EventHandler as _n_3_t_8
from __clrclasses__.System import Enum as _n_3_t_9
from __clrclasses__.System import IComparable as _n_3_t_10
from __clrclasses__.System import IFormattable as _n_3_t_11
from __clrclasses__.System import IConvertible as _n_3_t_12
from __clrclasses__.System import Guid as _n_3_t_13
from __clrclasses__.System.Runtime.InteropServices import GCHandle as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
import typing
class AcEdIPEReactorImpl(_n_3_t_0):
    pass
class AcEdOPMObjectFilterReactorImpl(_n_3_t_0):
    pass
class AcEdUcsReactorImpl(_n_3_t_0):
    pass
class AcEdViewFinalChangeReactorImpl(_n_3_t_0):
    pass
class AcSunViewportMonitorReactorImpl(_n_3_t_0):
    pass
class AcVsESWDictionaryReactor(_n_3_t_0):
    pass
class AcVsESWObjectReactor(_n_3_t_0):
    pass
class ApplicationDockLayoutChangedEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ApplicationDockLayoutChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_5, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: _n_3_t_5):...
class ApplicationDocumentFrameChangedEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ApplicationDocumentFrameChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_5, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: _n_3_t_5):...
class ApplicationEventManager(object):
    @property
    def ApplicationDockLayoutChanged(self) -> ApplicationDockLayoutChangedEventHandler:
        """ApplicationDockLayoutChanged Event: ApplicationDockLayoutChangedEventHandler"""
    @property
    def ApplicationDocumentFrameChanged(self) -> ApplicationDocumentFrameChangedEventHandler:
        """ApplicationDocumentFrameChanged Event: ApplicationDocumentFrameChangedEventHandler"""
    @property
    def ApplicationMainWindowMoved(self) -> ApplicationMainWindowMovedEventHandler:
        """ApplicationMainWindowMoved Event: ApplicationMainWindowMovedEventHandler"""
    @property
    def ApplicationMainWindowSized(self) -> ApplicationMainWindowSizedEventHandler:
        """ApplicationMainWindowSized Event: ApplicationMainWindowSizedEventHandler"""
    @property
    def ApplicationMainWindowVisibleChanged(self) -> ApplicationMainWindowVisibleChangedEventHandler:
        """ApplicationMainWindowVisibleChanged Event: ApplicationMainWindowVisibleChangedEventHandler"""
    @staticmethod
    def Instance() -> ApplicationEventManager:...
class ApplicationMainWindowMovedEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ApplicationMainWindowMovedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_5, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: _n_3_t_5):...
class ApplicationMainWindowSizedEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ApplicationMainWindowSizedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_5, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: _n_3_t_5):...
class ApplicationMainWindowVisibleChangedEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ApplicationMainWindowVisibleChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_5, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: _n_3_t_5):...
class CuiEventManager(object):
    @property
    def LoadRibbon(self) -> LoadRibbonEventHandler:
        """LoadRibbon Event: LoadRibbonEventHandler"""
    @property
    def WorkspaceRestore(self) -> WorkspaceRestoreEventHandler:
        """WorkspaceRestore Event: WorkspaceRestoreEventHandler"""
    @property
    def WorkspaceRibbonSave(self) -> WorkspaceRibbonSaveEventHandler:
        """WorkspaceRibbonSave Event: WorkspaceRibbonSaveEventHandler"""
    @property
    def WorkspaceSettingsSaved(self) -> WorkspaceSettingsSavedEventHandler:
        """WorkspaceSettingsSaved Event: WorkspaceSettingsSavedEventHandler"""
    def FreeCustomizationSectionHandle(self, handle: _n_4_t_0):...
    def GetCustomizationSectionHandle(self, menuGroupName: str) -> _n_4_t_0:...
    @staticmethod
    def Instance() -> CuiEventManager:...
class CuiLoadEventArgs(_n_3_t_5):
    @property
    def CurrentWorkspaceId(self) -> str:"""CurrentWorkspaceId { get; } -> str"""
    @property
    def CurrentWorkspaceName(self) -> str:"""CurrentWorkspaceName { get; } -> str"""
    def __init__(self) -> CuiLoadEventArgs:...
class DictionaryEventManager(_n_3_t_7):
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def DictionaryModified(self) -> _n_3_t_8:
        """DictionaryModified Event: EventHandler"""
    @property
    def ObjectModified(self) -> _n_3_t_8:
        """ObjectModified Event: EventHandler"""
    def __init__(self, dictionaryId: _n_3_t_0, bMonitorDictionaryObjects: bool) -> DictionaryEventManager:...
    def __init__(self, dictionaryId: _n_3_t_0, bMonitorDictionaryObjects: bool, bNotifyImmediately: bool) -> DictionaryEventManager:...
class IPEEventArgs(_n_3_t_5):
    @property
    def Entity(self) -> _n_1_t_0:"""Entity { get; } -> Entity"""
    @property
    def ExitStatus(self) -> IPEEventArgs.IPEExitStatus:"""ExitStatus { get; } -> IPEEventArgs.IPEExitStatus"""
    def __init__(self) -> IPEEventArgs:...
    class IPEExitStatus(_n_3_t_9, _n_3_t_10, _n_3_t_11, _n_3_t_12):
        ExtraTextCreated: int
        MTextCreated: int
        MTextEdited: int
        Quit: int
        TableCell: int
        TextCreated: int
        TextStringCreated: int
        value__: int
class IPEEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> IPEEventHandler:...
    def BeginInvoke(self, sender: object, e: IPEEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: IPEEventArgs):...
class IPEEventManager(object):
    @property
    def IPEEnded(self) -> IPEEventHandler:
        """IPEEnded Event: IPEEventHandler"""
    @property
    def IPEWillStart(self) -> IPEEventHandler:
        """IPEWillStart Event: IPEEventHandler"""
    @staticmethod
    def Instance() -> IPEEventManager:...
    def invokeSetIPEMacroMode(self, iMode: int):...
    def invokeSetIPEString(self, contents: str):...
class LoadRibbonEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> LoadRibbonEventHandler:...
    def BeginInvoke(self, sender: object, e: CuiLoadEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: CuiLoadEventArgs):...
class OPMObjectFilterEventArgs(_n_3_t_5):
    @property
    def EntityCLSID(self) -> _n_3_t_13:"""EntityCLSID { get; } -> Guid"""
    @property
    def EntityName(self) -> str:"""EntityName { get; } -> str"""
    def __init__(self) -> OPMObjectFilterEventArgs:...
class OPMObjectFilterEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> OPMObjectFilterEventHandler:...
    def BeginInvoke(self, sender: object, e: OPMObjectFilterEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: OPMObjectFilterEventArgs):...
class OPMObjectFilterEventManager(object):
    @property
    def OPMObjectFilterChanged(self) -> OPMObjectFilterEventHandler:
        """OPMObjectFilterChanged Event: OPMObjectFilterEventHandler"""
    @staticmethod
    def Instance() -> OPMObjectFilterEventManager:...
class SunViewportMonitorEventManager(object):
    @property
    def ActiveSunModified(self) -> _n_3_t_8:
        """ActiveSunModified Event: EventHandler"""
    @property
    def Goodbye(self) -> _n_3_t_8:
        """Goodbye Event: EventHandler"""
    @property
    def ViewportModified(self) -> _n_3_t_8:
        """ViewportModified Event: EventHandler"""
    @staticmethod
    def Instance() -> SunViewportMonitorEventManager:...
class TableSubSelectFilter(object):
    @property
    def CellSelected(self) -> TableSubSelectFilterEventHandler:
        """CellSelected Event: TableSubSelectFilterEventHandler"""
    @staticmethod
    def Instance() -> TableSubSelectFilter:...
class TableSubSelectFilterEventArgs(_n_3_t_5):
    @property
    def Reposition(self) -> bool:"""Reposition { get; } -> bool"""
    @property
    def Selected(self) -> bool:"""Selected { get; } -> bool"""
    @property
    def TableId(self) -> _n_1_t_1:"""TableId { get; } -> ObjectId"""
    def __init__(self) -> TableSubSelectFilterEventArgs:...
class TableSubSelectFilterEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> TableSubSelectFilterEventHandler:...
    def BeginInvoke(self, sender: object, e: TableSubSelectFilterEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: TableSubSelectFilterEventArgs):...
class UcsEventArgs(_n_3_t_5):
    @property
    def Matrix3dValue(self) -> _n_2_t_0:"""Matrix3dValue { get; } -> Matrix3d"""
    def __init__(self) -> UcsEventArgs:...
class UcsEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> UcsEventHandler:...
    def BeginInvoke(self, sender: object, e: UcsEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: UcsEventArgs):...
class UcsEventManager(object):
    @property
    def DynamicOriginUpdate(self) -> UcsEventHandler:
        """DynamicOriginUpdate Event: UcsEventHandler"""
    @property
    def UcsChanged(self) -> UcsEventHandler:
        """UcsChanged Event: UcsEventHandler"""
    @property
    def UcsWillChange(self) -> UcsEventHandler:
        """UcsWillChange Event: UcsEventHandler"""
    @staticmethod
    def instance() -> UcsEventManager:...
class ViewChangeEventArgs(_n_3_t_5):
    @property
    def UsedX(self) -> int:"""UsedX { get; } -> int"""
    @property
    def UsedY(self) -> int:"""UsedY { get; } -> int"""
    def __init__(self) -> ViewChangeEventArgs:...
class ViewFinalChangeEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ViewFinalChangeEventHandler:...
    def BeginInvoke(self, sender: object, e: ViewChangeEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: ViewChangeEventArgs):...
class ViewFinalChangeEventManager(object):
    @property
    def SendViewFinalChange(self) -> ViewFinalChangeEventHandler:
        """SendViewFinalChange Event: ViewFinalChangeEventHandler"""
    @property
    def SendViewportChanged(self) -> ViewFinalChangeEventHandler:
        """SendViewportChanged Event: ViewFinalChangeEventHandler"""
    @property
    def SendViewportCycled(self) -> ViewFinalChangeEventHandler:
        """SendViewportCycled Event: ViewFinalChangeEventHandler"""
    @property
    def SendViewportsResized(self) -> ViewResizeEventHandler:
        """SendViewportsResized Event: ViewResizeEventHandler"""
    @staticmethod
    def Instance() -> ViewFinalChangeEventManager:...
class ViewResizeEventArgs(_n_3_t_5):
    @property
    def UsedEX(self) -> float:"""UsedEX { get; } -> float"""
    @property
    def UsedEY(self) -> float:"""UsedEY { get; } -> float"""
    @property
    def UsedSplit(self) -> bool:"""UsedSplit { get; } -> bool"""
    @property
    def UsedSX(self) -> float:"""UsedSX { get; } -> float"""
    @property
    def UsedSY(self) -> float:"""UsedSY { get; } -> float"""
    def __init__(self) -> ViewResizeEventArgs:...
class ViewResizeEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> ViewResizeEventHandler:...
    def BeginInvoke(self, sender: object, e: ViewResizeEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: ViewResizeEventArgs):...
class VisualStyleEventManager(_n_3_t_7):
    @property
    def VisualStyleDictionaryEvent(self) -> VsESWDictionaryEventHandler:
        """VisualStyleDictionaryEvent Event: VsESWDictionaryEventHandler"""
    @property
    def VisualStyleObjectEvent(self) -> VsESWObjectEventHandler:
        """VisualStyleObjectEvent Event: VsESWObjectEventHandler"""
    @staticmethod
    def Instance() -> VisualStyleEventManager:...
    def SetDataBase(self, acadDatabase: _n_1_t_2, bUpdateUI: bool):...
class VsESWDictionaryEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> VsESWDictionaryEventHandler:...
    def BeginInvoke(self, sender: object, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object):...
class VsESWObjectEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> VsESWObjectEventHandler:...
    def BeginInvoke(self, sender: object, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object):...
class WorkspaceEventArgs(_n_3_t_5):
    @property
    def CustomizationSection(self) -> _n_0_t_0:"""CustomizationSection { get; } -> CustomizationSection"""
    @property
    def Id(self) -> str:"""Id { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Workspace(self) -> _n_0_t_1:"""Workspace { get; } -> Workspace"""
    def __init__(self) -> WorkspaceEventArgs:...
class WorkspaceRestoreEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> WorkspaceRestoreEventHandler:...
    def BeginInvoke(self, sender: object, e: WorkspaceEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: WorkspaceEventArgs):...
class WorkspaceRibbonSaveEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> WorkspaceRibbonSaveEventHandler:...
    def BeginInvoke(self, sender: object, e: WorkspaceEventArgs, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: WorkspaceEventArgs):...
class WorkspaceSettingsSavedEventHandler(_n_3_t_1, _n_3_t_2, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> WorkspaceSettingsSavedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_3_t_5, callback: _n_3_t_6, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: _n_3_t_5):...
