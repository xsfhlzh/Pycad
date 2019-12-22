from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_1_t_0
from __clrclasses__.System import ValueType as _n_2_t_0
from __clrclasses__.System import Enum as _n_2_t_1
from __clrclasses__.System import IComparable as _n_2_t_2
from __clrclasses__.System import IFormattable as _n_2_t_3
from __clrclasses__.System import IConvertible as _n_2_t_4
from __clrclasses__.System import IDisposable as _n_2_t_5
from __clrclasses__.System import Guid as _n_2_t_6
from __clrclasses__.System import MulticastDelegate as _n_2_t_7
from __clrclasses__.System import ICloneable as _n_2_t_8
from __clrclasses__.System import IntPtr as _n_2_t_9
from __clrclasses__.System import IAsyncResult as _n_2_t_10
from __clrclasses__.System import UInt32 as _n_2_t_11
from __clrclasses__.System import AsyncCallback as _n_2_t_12
from __clrclasses__.System import Attribute as _n_2_t_13
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_3_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_4_t_0
import typing
class AcTcToolReactorImpl(_n_2_t_0):
    pass
class ContextMenuMode(_n_2_t_1, _n_2_t_2, _n_2_t_3, _n_2_t_4):
    ContextMenuEditorImage: int
    ContextMenuPaletteBackground: int
    ContextMenuPaletteSetCaption: int
    ContextMenuPaletteSetOptionButton: int
    ContextMenuPaletteSetTab: int
    ContextMenuPaletteTool: int
    ContextNone: int
    value__: int
class CustomToolBase(_n_2_t_5, IAcadTool, IAcadStockTool, IDropTarget, IAcPiPropertyUnspecified, IAcPiPropertyDisplay, IOPMPropertyExtension, IAcadToolContextMenu, IPerPropertyBrowsing, IOPMPropertyDialog, IAcadToolFlyoutShape):
    @property
    def CurrentShapeId(self) -> _n_2_t_6:"""CurrentShapeId { get; set; } -> Guid"""
    @property
    def FlayoutPackageID(self) -> _n_2_t_6:"""FlayoutPackageID { get; set; } -> Guid"""
    @property
    def ToolGuid(self) -> _n_2_t_6:"""ToolGuid { get; } -> Guid"""
    @property
    def ToolImage(self) -> str:"""ToolImage { get; } -> str"""
    @property
    def ToolName(self) -> str:"""ToolName { get; } -> str"""
    def CreateCommandTool(self, palette: Package, toolName: str, bitmapName: ImageInfo, macro: str) -> Tool:...
    def CreateFlyoutTool(self, palette: Package, shapePackage: Package, toolNameOverride: str) -> Tool:...
    def CreatePalette(self, catalogName: Catalog, paletteName: str) -> Palette:...
    def CreateShapeCatalog(self, shapeName: str) -> Package:...
    def CreateStockTool(self, catalogName: str) -> Catalog:...
    def DropCallback(self, entity: _n_0_t_0) -> bool:...
    def ExecuteCallback(self) -> bool:...
class DragHandler(_n_2_t_7, _n_2_t_8, _n_4_t_0):
    def __init__(self, A_0: object, A_1: _n_2_t_9) -> DragHandler:...
    def BeginInvoke(self, pTool: _n_2_t_0, dwKeyState: _n_2_t_11, tpOperationFlag: TPOperationFlag, callback: _n_2_t_12, obj: object) -> _n_2_t_10:...
    def EndInvoke(self, result: _n_2_t_10):...
    def Invoke(self, pTool: _n_2_t_0, dwKeyState: _n_2_t_11, tpOperationFlag: TPOperationFlag):...
class DropPointHandler(_n_2_t_7, _n_2_t_8, _n_4_t_0):
    def __init__(self, A_0: object, A_1: _n_2_t_9) -> DropPointHandler:...
    def BeginInvoke(self, point: _n_1_t_0, callback: _n_2_t_12, obj: object) -> _n_2_t_10:...
    def EndInvoke(self, result: _n_2_t_10):...
    def Invoke(self, point: _n_1_t_0):...
class ExecutionContext(_n_2_t_1, _n_2_t_2, _n_2_t_3, _n_2_t_4):
    DroppedInDrawing: int
    LeftButtonClicked: int
    value__: int
class FlyoutEntryAttribute(_n_2_t_13, _n_3_t_0):
    @property
    def DispId(self) -> int:"""DispId { get; } -> int"""
    def __init__(self, dispatchId: int) -> FlyoutEntryAttribute:...
class PerPropertyBrowsingEntryAttribute(_n_2_t_13, _n_3_t_0):
    @property
    def DispId(self) -> int:"""DispId { get; } -> int"""
    @property
    def EllipsisBmpResource(self) -> str:"""EllipsisBmpResource { get; } -> str"""
    @property
    def EllipsisBmpType(self) -> int:"""EllipsisBmpType { get; } -> int"""
    @property
    def IntegralHeight(self) -> int:"""IntegralHeight { get; } -> int"""
    @property
    def IsFullView(self) -> bool:"""IsFullView { get; } -> bool"""
    @property
    def LefIconResource(self) -> str:"""LefIconResource { get; } -> str"""
    @property
    def LeftIconType(self) -> int:"""LeftIconType { get; } -> int"""
    @property
    def ProgId(self) -> str:"""ProgId { get; } -> str"""
    @property
    def TextColor(self) -> int:"""TextColor { get; } -> int"""
    @property
    def Weight(self) -> int:"""Weight { get; } -> int"""
    def __init__(self, dispatchId: int, programId: str, leftIconResource: str, leftIconType: int, ellipsisBmpResource: str, ellipsisBmpType: int, textColor: int, fullView: bool, integralHeight: int, weight: int) -> PerPropertyBrowsingEntryAttribute:...
class PickHandler(_n_2_t_7, _n_2_t_8, _n_4_t_0):
    def __init__(self, A_0: object, A_1: _n_2_t_9) -> PickHandler:...
    def BeginInvoke(self, pTool: _n_2_t_0, dwKeyState: _n_2_t_11, tpOperationFlag: TPOperationFlag, nIndex: int, callback: _n_2_t_12, obj: object) -> _n_2_t_10:...
    def EndInvoke(self, result: _n_2_t_10):...
    def Invoke(self, pTool: _n_2_t_0, dwKeyState: _n_2_t_11, tpOperationFlag: TPOperationFlag, nIndex: int):...
class ReturnStatus(_n_2_t_1, _n_2_t_2, _n_2_t_3, _n_2_t_4):
    ContextMenuHide: int
    ContextMenuShow: int
    ContextMenuUpdatePalette: int
    ExecutionCanceled: int
    ExecutionCancelRejected: int
    value__: int
class ToolAttribute(_n_2_t_13, _n_3_t_0):
    @property
    def ToolImage(self) -> str:"""ToolImage { get; } -> str"""
    @property
    def ToolName(self) -> str:"""ToolName { get; } -> str"""
    def __init__(self, toolName: str, toolImage: str) -> ToolAttribute:...
class ToolEditFlags(_n_2_t_1, _n_2_t_2, _n_2_t_3, _n_2_t_4):
    EditCustom: int
    EditDefault: int
    EditMultiple: int
    EditNone: int
    value__: int
class ToolItemInfo(_n_2_t_0):
    Description: int
    ItemId: int
    Name: int
class ToolReactorManager(object):
    @property
    def Drag(self) -> DragHandler:
        """Drag Event: DragHandler"""
    @property
    def DropPoint(self) -> DropPointHandler:
        """DropPoint Event: DropPointHandler"""
    @property
    def Pick(self) -> PickHandler:
        """Pick Event: PickHandler"""
    @staticmethod
    def Instance() -> ToolReactorManager:...
    def invokeToolContextMenu(self, itemId: _n_2_t_6, nIndex: int):...
    def invokeToolDrag(self, itemId: _n_2_t_6, dwKeyState: _n_2_t_11, point: _n_1_t_0):...
    def invokeToolPick(self, itemId: _n_2_t_6, dwKeyState: _n_2_t_11):...
class TPOperationFlag(_n_2_t_1, _n_2_t_2, _n_2_t_3, _n_2_t_4):
    ContextMenu: int
    Drag: int
    Pick: int
    value__: int
