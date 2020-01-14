import __clrclasses__.Autodesk.AutoCAD.Windows.Data.Render as Render
from __clrclasses__.Atil import Image as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import DocumentCollectionEventArgs as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Transparency as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import BlockTableRecord as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DimStyleTableRecord as _n_3_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import FullSubentityPath as _n_3_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_3_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import OpenMode as _n_3_t_4
from __clrclasses__.Autodesk.AutoCAD.Geometry import DoubleCollection as _n_4_t_0
from __clrclasses__.Autodesk.AutoCAD.Internal.Reactors import CuiLoadEventArgs as _n_5_t_0
from __clrclasses__.Autodesk.AutoCAD.Internal.Reactors import WorkspaceEventArgs as _n_5_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_6_t_0
from __clrclasses__.Autodesk.AutoCAD.Windows.Data.Render.MentalRay import RenderEngine as _n_7_t_0
from __clrclasses__.Autodesk.AutoCAD.Windows.Data.Render.RapidRT import RenderEngine as _n_8_t_0
from __clrclasses__.Autodesk.Windows import IGalleryCommand as _n_9_t_0
from __clrclasses__.Autodesk.Windows import RibbonListButton as _n_9_t_1
from __clrclasses__.Autodesk.Windows import RibbonItem as _n_9_t_2
from __clrclasses__.System import IDisposable as _n_10_t_0
from __clrclasses__.System import ValueType as _n_10_t_1
from __clrclasses__.System import Enum as _n_10_t_2
from __clrclasses__.System import IComparable as _n_10_t_3
from __clrclasses__.System import IFormattable as _n_10_t_4
from __clrclasses__.System import IConvertible as _n_10_t_5
from __clrclasses__.System import ICloneable as _n_10_t_6
from __clrclasses__.System import IntPtr as _n_10_t_7
from __clrclasses__.System import Array as _n_10_t_8
from __clrclasses__.System import MulticastDelegate as _n_10_t_9
from __clrclasses__.System import IAsyncResult as _n_10_t_10
from __clrclasses__.System import AsyncCallback as _n_10_t_11
from __clrclasses__.System import EventArgs as _n_10_t_12
from __clrclasses__.System import UInt32 as _n_10_t_13
from __clrclasses__.System import Type as _n_10_t_14
from __clrclasses__.System import EventHandler as _n_10_t_15
from __clrclasses__.System import Char as _n_10_t_16
from __clrclasses__.System.Collections import IList as _n_11_t_0
from __clrclasses__.System.Collections.Generic import IList as _n_12_t_0
from __clrclasses__.System.Collections.Generic import List as _n_12_t_1
from __clrclasses__.System.Collections.Generic import IReadOnlyList as _n_12_t_2
from __clrclasses__.System.Collections.ObjectModel import ObservableCollection as _n_13_t_0
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_13_t_1
from __clrclasses__.System.Collections.Specialized import INotifyCollectionChanged as _n_14_t_0
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_15_t_0
from __clrclasses__.System.ComponentModel import PropertyChangedEventArgs as _n_15_t_1
from __clrclasses__.System.ComponentModel import ICustomTypeDescriptor as _n_15_t_2
from __clrclasses__.System.ComponentModel import PropertyDescriptor as _n_15_t_3
from __clrclasses__.System.ComponentModel import EnumConverter as _n_15_t_4
from __clrclasses__.System.Globalization import CultureInfo as _n_16_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_17_t_0
from __clrclasses__.System.Windows.Data import IValueConverter as _n_18_t_0
from __clrclasses__.System.Windows.Input import ICommand as _n_19_t_0
from __clrclasses__.System.Windows.Media import ImageSource as _n_20_t_0
from __clrclasses__.System.Windows.Media import Color as _n_20_t_1
import typing
T = typing.TypeVar('T')
class AnimationEditor(_n_15_t_0):
    @property
    def IsActive(self) -> bool:"""IsActive { get; set; } -> bool"""
    @property
    def Status(self) -> NavStatus:"""Status { get; set; } -> NavStatus"""
    def __init__(self) -> AnimationEditor:...
class AttachmentPointCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> AttachmentPointCommand:...
class AutoCompleteList(_n_6_t_0, _n_10_t_0, typing.Iterable[CommandLineItem]):
    @property
    def Item(self) -> CommandLineItem:"""Item { get; } -> CommandLineItem"""
    @property
    def Length(self) -> int:"""Length { get; } -> int"""
    def __init__(self, rawSearch: str, searchType: CommandCompletionType) -> AutoCompleteList:...
    def __init__(self, prefix: str, parsedSearch: str, cmdFlags: int, searchType: CommandCompletionType, abortIfMultipleMatchesFound: bool) -> AutoCompleteList:...
    def Sort(self):...
class AutoCompleteToolTipService(object):
    def __init__(self) -> AutoCompleteToolTipService:...
    @staticmethod
    def HideToolTip():...
    @staticmethod
    def ShowToolTip(pTooltipInfo: _n_10_t_1):...
class AutoCorrectList(_n_6_t_0, _n_10_t_0, typing.Iterable[CommandLineItem]):
    @property
    def HasClearWinner(self) -> bool:"""HasClearWinner { get; } -> bool"""
    @property
    def Item(self) -> CommandLineItem:"""Item { get; } -> CommandLineItem"""
    @property
    def Length(self) -> int:"""Length { get; } -> int"""
    def __init__(self, rawSearch: str, searchType: AutoCorrectType) -> AutoCorrectList:...
    def Sort(self):...
class AutoCorrectorService(object):
    def __init__(self) -> AutoCorrectorService:...
    @staticmethod
    def IsAutoCorrectSupported() -> bool:...
    @staticmethod
    def IsInputCommand(isInput: bool):...
    @staticmethod
    def UpdateErrInputCount(errInput: str, cmdGlobalName: str, cmdLocalName: str):...
class AutoCorrectType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    CommandSysvar: int
    InternalCommand: int
    value__: int
class BackgroundMaskCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> BackgroundMaskCommand:...
class BlockEditor(_n_15_t_0, _n_10_t_0):
    @property
    def BlockName(self) -> str:"""BlockName { get; } -> str"""
    @property
    def CurrentVisibilityStateName(self) -> str:"""CurrentVisibilityStateName { get; set; } -> str"""
    @property
    def IsAuthorPaletteVisible(self) -> bool:"""IsAuthorPaletteVisible { get; } -> bool"""
    @property
    def IsInBlockEditor(self) -> bool:"""IsInBlockEditor { get; } -> bool"""
    @property
    def IsVisibilityParameterPresent(self) -> bool:"""IsVisibilityParameterPresent { get; } -> bool"""
    @property
    def Tooltip(self) -> str:"""Tooltip { get; } -> str"""
    @property
    def VisibilitySets(self) -> _n_13_t_0[str]:"""VisibilitySets { get; } -> ObservableCollection"""
    def __init__(self) -> BlockEditor:...
    def OnDocumentActivated(self, sender: object, e: _n_1_t_0):...
    def OnSystemVariableChanged(self, sender: object, e: _n_15_t_1):...
class CellStyleConverter(_n_18_t_0):
    @property
    def ByRowColumn(self) -> str:"""ByRowColumn { get; } -> str"""
    @property
    def Varies(self) -> str:"""Varies { get; } -> str"""
    def __init__(self) -> CellStyleConverter:...
class CharacterSetCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> CharacterSetCommand:...
class ClearLineSpaceCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> ClearLineSpaceCommand:...
class CloseCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> CloseCommand:...
class CMLContentSearchPreviews(object):
    def __init__(self) -> CMLContentSearchPreviews:...
    @staticmethod
    def ClearDimStySampleObjects():...
    @staticmethod
    def ConvertImageToImageSource(pImage: _n_0_t_0) -> _n_20_t_0:...
    @staticmethod
    def CreateDimStySampleObjects():...
    @staticmethod
    def GetBlockTRThumbnail(blockTR: _n_3_t_0) -> _n_20_t_0:...
    @staticmethod
    def GetColorFromSysvarSettings(sysvarName: str, outColor: _n_2_t_0) -> bool:...
    @staticmethod
    def GetDimStyleThumbnail(dimStyle: _n_3_t_1) -> _n_20_t_0:...
class ColorCollection(DataItemCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    @property
    def Commands(self) -> ILookup[_n_19_t_0]:"""Commands { get; } -> ILookup"""
    def AddIfNotContain(self, value: object) -> object:...
    def AddIfNotContain(self, value: _n_2_t_0) -> object:...
class ColorCommand(_n_9_t_0):
    def __init__(self, colorPropertyName: str) -> ColorCommand:...
    def __init__(self, colorPropertyName: str, previewPropertyName: str) -> ColorCommand:...
class ColorSetting(_n_15_t_0):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> _n_20_t_1:"""Value { get; set; } -> Color"""
    def __init__(self, name: str, value: _n_20_t_1) -> ColorSetting:...
class ColorToNamedValueConverter(_n_18_t_0):
    def __init__(self) -> ColorToNamedValueConverter:...
class ColumnsSettingsDialogCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> ColumnsSettingsDialogCommand:...
class Command(_n_19_t_0, _n_10_t_6):
    @property
    def Hidden(self) -> bool:"""Hidden { get; set; } -> bool"""
    @property
    def IsFocusAble(self) -> bool:"""IsFocusAble { get; set; } -> bool"""
    @property
    def Synchronous(self) -> bool:"""Synchronous { get; set; } -> bool"""
class CommandCompletionType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    Command: int
    File: int
    Keyword: int
    value__: int
class CommandEditor(_n_15_t_0):
    @property
    def ActualDisplayedLinesCount(self) -> int:"""ActualDisplayedLinesCount { get; set; } -> int"""
    @property
    def CurrentCommand(self) -> str:"""CurrentCommand { get; } -> str"""
    @property
    def CurrentCommandIcon(self) -> _n_10_t_7:"""CurrentCommandIcon { get; } -> IntPtr"""
    @property
    def History(self) -> _n_13_t_0[CommandHistory]:"""History { get; } -> ObservableCollection"""
    @property
    def IsBusy(self) -> bool:"""IsBusy { get; set; } -> bool"""
    @property
    def NeedShowClickableKeywords(self) -> bool:"""NeedShowClickableKeywords { get; } -> bool"""
    @property
    def PromptAndInput(self) -> PromptAndInput:"""PromptAndInput { get; } -> PromptAndInput"""
    @property
    def RecentCommands(self) -> _n_12_t_1[str]:"""RecentCommands { get; } -> List"""
    @property
    def TemporaryHistory(self) -> _n_13_t_0[CommandHistory]:"""TemporaryHistory { get; } -> ObservableCollection"""
    @property
    def VisibleHistoryItemsCount(self) -> int:"""VisibleHistoryItemsCount { get; set; } -> int"""
    def ClearTempHistory(self):...
    def CopyHistoryToClipBoard(self):...
    def SyncHistoryViewList(self):...
class CommandEditorManager(_n_15_t_0, _n_10_t_0):
    @property
    def ActiveEditor(self) -> CommandEditor:"""ActiveEditor { get; } -> CommandEditor"""
class CommandHistory(object):
    @property
    def Command(self) -> str:"""Command { get; } -> str"""
class CommandLineItem(object):
    @property
    def DisplayText(self) -> str:"""DisplayText { get; } -> str"""
    @property
    def Flags(self) -> int:"""Flags { get; } -> int"""
    @property
    def GlobalName(self) -> str:"""GlobalName { get; } -> str"""
    @property
    def Image(self) -> _n_10_t_7:"""Image { get; } -> IntPtr"""
    @property
    def LocalName(self) -> str:"""LocalName { get; } -> str"""
    @property
    def Tooltip(self) -> _n_10_t_7:"""Tooltip { get; } -> IntPtr"""
    @property
    def UnderlyingCommand(self) -> str:"""UnderlyingCommand { get; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def AddRef(self):...
    def Release(self):...
class CommandStack(_n_15_t_0, _n_10_t_0):
    @property
    def AllCommands(self) -> str:"""AllCommands { get; } -> str"""
    @property
    def MainCommand(self) -> str:"""MainCommand { get; } -> str"""
    def ContainsAny(self, commands: _n_10_t_8[str]) -> bool:...
    def ContainsOnly(self, commands: _n_10_t_8[str]) -> bool:...
class CommonProperties(_n_15_t_2, _n_15_t_0, ILookup[CommonProperty], _n_10_t_0, typing.Iterable[CommonProperty]):
    def ContainsAny(self, properties: _n_10_t_8[str]) -> bool:...
class CommonProperty(_n_15_t_3, ITrueValueAble, _n_10_t_0):
    @property
    def TrueValues(self) -> TrueValues:"""TrueValues { get; } -> TrueValues"""
class CompositeConverter(_n_18_t_0):
    @property
    def Converters(self) -> _n_12_t_1[_n_18_t_0]:"""Converters { get; } -> List"""
    def __init__(self) -> CompositeConverter:...
class ContentSearchCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> ContentSearchCommand:...
class DataBindings(_n_10_t_0):
    @property
    def ActiveCommands(self) -> CommandStack:"""ActiveCommands { get; } -> CommandStack"""
    @property
    def AnimationEditor(self) -> AnimationEditor:"""AnimationEditor { get; } -> AnimationEditor"""
    @property
    def ArrayCreation(self) -> object:"""ArrayCreation { get; } -> object"""
    @property
    def BlockEditor(self) -> BlockEditor:"""BlockEditor { get; } -> BlockEditor"""
    @property
    def Collections(self) -> DataItemCollections:"""Collections { get; } -> DataItemCollections"""
    @property
    def ColorSettings(self) -> ILookup[ColorSetting]:"""ColorSettings { get; } -> ILookup"""
    @property
    def CommandEditorManager(self) -> CommandEditorManager:"""CommandEditorManager { get; } -> CommandEditorManager"""
    @property
    def Commands(self) -> ILookup[Command]:"""Commands { get; } -> ILookup"""
    @property
    def CurrentViewport(self) -> object:"""CurrentViewport { get; } -> object"""
    @property
    def DoNothing(self) -> object:"""DoNothing { get; } -> object"""
    @property
    def EffectivePropertySource(self) -> EffectivePropertySource:"""EffectivePropertySource { get; } -> EffectivePropertySource"""
    @property
    def EplotExport(self) -> EplotExport:"""EplotExport { get; } -> EplotExport"""
    @property
    def GeoData(self) -> GeoData:"""GeoData { get; } -> GeoData"""
    @property
    def HatchCommands(self) -> HatchCommands:"""HatchCommands { get; } -> HatchCommands"""
    @property
    def InplaceTextEditor(self) -> InplaceTextEditor:"""InplaceTextEditor { get; } -> InplaceTextEditor"""
    @property
    def IsoDraft(self) -> IsoDraft:"""IsoDraft { get; } -> IsoDraft"""
    @property
    def LightEngine(self) -> LightEngine:"""LightEngine { get; } -> LightEngine"""
    @property
    def NativeFunctions(self) -> ILookup[NativeFunction]:"""NativeFunctions { get; } -> ILookup"""
    @property
    def RenderEngine(self) -> _n_8_t_0:"""RenderEngine { get; } -> RenderEngine"""
    @property
    def RenderEngineMR(self) -> _n_7_t_0:"""RenderEngineMR { get; } -> RenderEngine"""
    @property
    def SystemVariables(self) -> ILookup[SystemVariable]:"""SystemVariables { get; } -> ILookup"""
    @property
    def SysvarMonitorState(self) -> SysvarMonitorState:"""SysvarMonitorState { get; } -> SysvarMonitorState"""
    @property
    def TextSize(self) -> TextSize:"""TextSize { get; } -> TextSize"""
    @property
    def ThemeEngine(self) -> ThemeEngine:"""ThemeEngine { get; } -> ThemeEngine"""
    @property
    def ViewportsCommands(self) -> ILookup[_n_19_t_0]:"""ViewportsCommands { get; } -> ILookup"""
    @property
    def Views2DCommands(self) -> Views2DCommands:"""Views2DCommands { get; } -> Views2DCommands"""
    @property
    def Workspaces(self) -> WorkspaceCollection:"""Workspaces { get; } -> WorkspaceCollection"""
    def GetLocalColorName(self, acadColor: _n_2_t_0) -> str:...
    def Refresh(self):...
class DataItemCollection(_n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    @property
    def Active(self) -> bool:"""Active { get; } -> bool"""
    @property
    def CurrentItem(self) -> _n_15_t_2:"""CurrentItem { get; set; } -> ICustomTypeDescriptor"""
class DataItemCollections(ILookup[DataItemCollection], _n_10_t_0, typing.Iterable[DataItemCollection]):
    @property
    def Blocks(self) -> DataItemCollection:"""Blocks { get; } -> DataItemCollection"""
    @property
    def Colors(self) -> ColorCollection:"""Colors { get; } -> ColorCollection"""
    @property
    def DetailViewStyles(self) -> DataItemCollection:"""DetailViewStyles { get; } -> DataItemCollection"""
    @property
    def DimensionStyles(self) -> DataItemCollection:"""DimensionStyles { get; } -> DataItemCollection"""
    @property
    def LayerFilters(self) -> DataItemCollection:"""LayerFilters { get; } -> DataItemCollection"""
    @property
    def Layers(self) -> DataItemCollection:"""Layers { get; } -> DataItemCollection"""
    @property
    def LayerStates(self) -> DataItemCollection:"""LayerStates { get; } -> DataItemCollection"""
    @property
    def Linetypes(self) -> DataItemCollection:"""Linetypes { get; } -> DataItemCollection"""
    @property
    def Lineweights(self) -> EnumItemCollection:"""Lineweights { get; } -> EnumItemCollection"""
    @property
    def MleaderStyles(self) -> DataItemCollection:"""MleaderStyles { get; } -> DataItemCollection"""
    @property
    def NamedViews(self) -> DataItemCollection:"""NamedViews { get; } -> DataItemCollection"""
    @property
    def PlotStyles(self) -> DataItemCollection:"""PlotStyles { get; } -> DataItemCollection"""
    @property
    def PointCloudClassificationSchemes(self) -> DataItemCollection:"""PointCloudClassificationSchemes { get; } -> DataItemCollection"""
    @property
    def PointCloudColorSchemes(self) -> DataItemCollection:"""PointCloudColorSchemes { get; } -> DataItemCollection"""
    @property
    def PointClouds(self) -> DataItemCollection:"""PointClouds { get; } -> DataItemCollection"""
    @property
    def RenderPresets(self) -> DataItemCollection:"""RenderPresets { get; } -> DataItemCollection"""
    @property
    def RenderPresetsMR(self) -> DataItemCollection:"""RenderPresetsMR { get; } -> DataItemCollection"""
    @property
    def SectionViewStyles(self) -> DataItemCollection:"""SectionViewStyles { get; } -> DataItemCollection"""
    @property
    def Selection(self) -> Selection:"""Selection { get; } -> Selection"""
    @property
    def TableCellStyles(self) -> DataItemCollection:"""TableCellStyles { get; } -> DataItemCollection"""
    @property
    def TableStyles(self) -> DataItemCollection:"""TableStyles { get; } -> DataItemCollection"""
    @property
    def TextStyles(self) -> DataItemCollection:"""TextStyles { get; } -> DataItemCollection"""
    @property
    def UcsPlanes(self) -> DataItemCollection:"""UcsPlanes { get; } -> DataItemCollection"""
    @property
    def UIFontInfoCollection(self) -> _n_12_t_0[UIFontInfo]:"""UIFontInfoCollection { get; } -> IList"""
    @property
    def VisualStyles(self) -> DataItemCollection:"""VisualStyles { get; } -> DataItemCollection"""
class DataItemFactoryMethod(_n_10_t_9, _n_10_t_6, _n_17_t_0):
    def __init__(self, A_0: object, A_1: _n_10_t_7) -> DataItemFactoryMethod:...
    def BeginInvoke(self, objId: _n_3_t_2, wrapper: object, callback: _n_10_t_11, obj: object) -> _n_10_t_10:...
    def EndInvoke(self, result: _n_10_t_10) -> DataItem:...
    def Invoke(self, objId: _n_3_t_2, wrapper: object) -> DataItem:...
class DbObjectCollection(DataItemCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    pass
class DefinedSymbolsCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> DefinedSymbolsCommand:...
class DisposingEventHandler(_n_10_t_9, _n_10_t_6, _n_17_t_0):
    def __init__(self, A_0: object, A_1: _n_10_t_7) -> DisposingEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_10_t_12, callback: _n_10_t_11, obj: object) -> _n_10_t_10:...
    def EndInvoke(self, result: _n_10_t_10):...
    def Invoke(self, sender: object, e: _n_10_t_12):...
class DoubleToStringConverter(_n_18_t_0):
    def __init__(self) -> DoubleToStringConverter:...
class EffectiveProperties(_n_15_t_2, _n_15_t_0, IInvalidateProperty, typing.Iterable[EffectiveProperty]):
    @property
    def Item(self) -> EffectiveProperty:"""Item { get; } -> EffectiveProperty"""
    def Invalidate(self, propertyName: str):...
class EffectiveProperty(_n_15_t_3, ITrueValueAble):
    @property
    def TrueValues(self) -> TrueValues:"""TrueValues { get; } -> TrueValues"""
class EffectivePropertySource(_n_15_t_0, _n_10_t_0):
    @property
    def EffectiveProperties(self) -> EffectiveProperties:"""EffectiveProperties { get; } -> EffectiveProperties"""
class EnumItemCollection(_n_12_t_0[_n_15_t_2], _n_15_t_0, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    @property
    def CurrentItem(self) -> _n_15_t_2:"""CurrentItem { get; set; } -> ICustomTypeDescriptor"""
class EnumSubsetConverter(_n_18_t_0):
    def __init__(self) -> EnumSubsetConverter:...
class EplotExport(_n_15_t_0, _n_10_t_0):
    @property
    def CurrentItemExport(self) -> str:"""CurrentItemExport { get; set; } -> str"""
    @property
    def CurrentItemPageSetup(self) -> str:"""CurrentItemPageSetup { get; set; } -> str"""
    @property
    def EnablePageSetupBtn(self) -> bool:"""EnablePageSetupBtn { get; } -> bool"""
    @property
    def EnableWindowBtn(self) -> bool:"""EnableWindowBtn { get; } -> bool"""
    @property
    def ExportSet(self) -> _n_13_t_0[str]:"""ExportSet { get; } -> ObservableCollection"""
    @property
    def PageSetupSet(self) -> _n_13_t_0[str]:"""PageSetupSet { get; } -> ObservableCollection"""
    def __init__(self) -> EplotExport:...
    def UpdateCurrentItemExport(self):...
class Expression(_n_15_t_0):
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    @property
    def Value(self) -> object:"""Value { get; set; } -> object"""
    def __init__(self, value: object, text: str) -> Expression:...
class ExtendedPropertyEventArgs(_n_10_t_12):
    @property
    def DataItem(self) -> _n_15_t_2:"""DataItem { get; } -> ICustomTypeDescriptor"""
    @property
    def DataItemType(self) -> str:"""DataItemType { get; } -> str"""
    @property
    def PropertyDesc(self) -> _n_15_t_3:"""PropertyDesc { get; set; } -> PropertyDescriptor"""
    @property
    def PropertyName(self) -> str:"""PropertyName { get; } -> str"""
    def __init__(self, propertyName: str, dataItem: _n_15_t_2, dataItemType: str) -> ExtendedPropertyEventArgs:...
class ExtendedPropertyEventHandler(_n_10_t_9, _n_10_t_6, _n_17_t_0):
    def __init__(self, A_0: object, A_1: _n_10_t_7) -> ExtendedPropertyEventHandler:...
    def BeginInvoke(self, sender: object, e: ExtendedPropertyEventArgs, callback: _n_10_t_11, obj: object) -> _n_10_t_10:...
    def EndInvoke(self, result: _n_10_t_10):...
    def Invoke(self, sender: object, e: ExtendedPropertyEventArgs):...
class ExtendedPropertyManager(object):
    @property
    def RegisterExtendedProperty(self) -> ExtendedPropertyEventHandler:
        """RegisterExtendedProperty Event: ExtendedPropertyEventHandler"""
    def __init__(self) -> ExtendedPropertyManager:...
    @staticmethod
    def TryGetExtendedProperty(propertyName: str, dataItem: _n_15_t_2, dataItemType: str) -> _n_15_t_3:...
class FieldDialogCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> FieldDialogCommand:...
class FindReplaceCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> FindReplaceCommand:...
class FindTextCommand(IPECommandBase, _n_19_t_0, _n_15_t_0, _n_10_t_0):
    def __init__(self) -> FindTextCommand:...
class GeoData(_n_15_t_0, _n_10_t_0):
    @property
    def Instance(self) -> GeoData:"""Instance { get; } -> GeoData"""
    @property
    def IsGeoCsSupported(self) -> _n_10_t_1:"""IsGeoCsSupported { get; } -> ValueType"""
    @property
    def IsGeomapImageUpdateAllowed(self) -> _n_10_t_1:"""IsGeomapImageUpdateAllowed { get; } -> ValueType"""
    @property
    def IsMyGeoDataAvailable(self) -> _n_10_t_1:"""IsMyGeoDataAvailable { get; } -> ValueType"""
    @property
    def IsMyLocationAvaliable(self) -> _n_10_t_1:"""IsMyLocationAvaliable { get; } -> ValueType"""
    @property
    def IsSnapShotAllowed(self) -> _n_10_t_1:"""IsSnapShotAllowed { get; } -> ValueType"""
    def __init__(self) -> GeoData:...
class HatchCommands(_n_15_t_0, _n_10_t_0):
    @property
    def HasDefinedBoundaries(self) -> bool:"""HasDefinedBoundaries { get; set; } -> bool"""
    @property
    def IsHatchCreation(self) -> bool:"""IsHatchCreation { get; } -> bool"""
    @property
    def LaunchDialog(self) -> _n_19_t_0:"""LaunchDialog { get; } -> ICommand"""
    @property
    def MatchProperties(self) -> _n_19_t_0:"""MatchProperties { get; } -> ICommand"""
    @property
    def PickPoints(self) -> _n_19_t_0:"""PickPoints { get; } -> ICommand"""
    @property
    def RecreateBoundaries(self) -> _n_19_t_0:"""RecreateBoundaries { get; } -> ICommand"""
    @property
    def RemoveBoundaries(self) -> _n_19_t_0:"""RemoveBoundaries { get; } -> ICommand"""
    @property
    def SelectObjects(self) -> _n_19_t_0:"""SelectObjects { get; } -> ICommand"""
    @property
    def SetOrigin(self) -> _n_19_t_0:"""SetOrigin { get; } -> ICommand"""
class HatchPatterns(_n_15_t_0, _n_10_t_0):
    @property
    def AllPatterns(self) -> _n_13_t_0[str]:"""AllPatterns { get; } -> ObservableCollection"""
    @property
    def CustomPatterns(self) -> _n_13_t_0[str]:"""CustomPatterns { get; } -> ObservableCollection"""
    @property
    def GradientPatterns(self) -> _n_13_t_0[str]:"""GradientPatterns { get; } -> ObservableCollection"""
    @property
    def Instance(self) -> HatchPatterns:"""Instance { get; } -> HatchPatterns"""
    @property
    def IsUnknownPatternSelected(self) -> bool:"""IsUnknownPatternSelected { get; set; } -> bool"""
    @property
    def PredefinedANSIPatterns(self) -> _n_13_t_0[str]:"""PredefinedANSIPatterns { get; } -> ObservableCollection"""
    @property
    def PredefinedISOPatterns(self) -> _n_13_t_0[str]:"""PredefinedISOPatterns { get; } -> ObservableCollection"""
    @property
    def PredefinedOtherPatterns(self) -> _n_13_t_0[str]:"""PredefinedOtherPatterns { get; } -> ObservableCollection"""
    @property
    def PredefinedPatterns(self) -> _n_13_t_0[str]:"""PredefinedPatterns { get; } -> ObservableCollection"""
    @property
    def UnknownPatterns(self) -> _n_13_t_0[str]:"""UnknownPatterns { get; } -> ObservableCollection"""
    def AppendUnknownPattern(self, unknownPattern: str) -> bool:...
    @staticmethod
    def ValidPatternName(patternName: str) -> PatPatternCategory:...
class IDataItem():
    @property
    def ObjectId(self) -> _n_3_t_3:"""ObjectId { get; } -> ObjectId"""
    def StartTransaction(self, mode: _n_3_t_4) -> IDataItemTransaction:...
class IDataItemTransaction(_n_10_t_0):
    @property
    def Item(self) -> object:"""Item { get; } -> object"""
    def Commit(self):...
class IInvalidateProperty():
    def InvalidateProperty(self, propertyName: str):...
class ILookup(typing.Generic[T], typing.Iterable[T]):
    @property
    def Item(self) -> T:"""Item { get; } -> T"""
class ImportCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> ImportCommand:...
class INamedImageProvider():
    def GetNamedImage(self, objectName: str) -> _n_20_t_0:...
class INamedValue():
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
class INotifyCollectionItemsChanged():
    @property
    def ItemsChanged(self) -> NotifyCollectionItemsChangedEventHandler:
        """ItemsChanged Event: NotifyCollectionItemsChangedEventHandler"""
class InplaceTextEditor(_n_15_t_0, _n_10_t_0):
    @property
    def Annotative(self) -> bool:"""Annotative { get; set; } -> bool"""
    @property
    def AttachmentPoint(self) -> _n_19_t_0:"""AttachmentPoint { get; } -> ICommand"""
    @property
    def AttachmentPointType(self) -> IPEAttachmentPoint:"""AttachmentPointType { get; set; } -> IPEAttachmentPoint"""
    @property
    def AutoCAPS(self) -> bool:"""AutoCAPS { get; set; } -> bool"""
    @property
    def BackgroundMask(self) -> _n_19_t_0:"""BackgroundMask { get; } -> ICommand"""
    @property
    def Bold(self) -> bool:"""Bold { get; set; } -> bool"""
    @property
    def CharacterSet(self) -> _n_19_t_0:"""CharacterSet { get; } -> ICommand"""
    @property
    def ClearLineSpace(self) -> _n_19_t_0:"""ClearLineSpace { get; } -> ICommand"""
    @property
    def Close(self) -> _n_19_t_0:"""Close { get; } -> ICommand"""
    @property
    def Color(self) -> _n_2_t_0:"""Color { get; set; } -> Color"""
    @property
    def ColumnsSettingsDialog(self) -> _n_19_t_0:"""ColumnsSettingsDialog { get; } -> ICommand"""
    @property
    def ColumnType(self) -> IPEColumnType:"""ColumnType { get; set; } -> IPEColumnType"""
    @property
    def ContentSearch(self) -> _n_19_t_0:"""ContentSearch { get; set; } -> ICommand"""
    @property
    def CurrentFont(self) -> UIFontInfo:"""CurrentFont { get; set; } -> UIFontInfo"""
    @property
    def DefinedSymbols(self) -> _n_19_t_0:"""DefinedSymbols { get; } -> ICommand"""
    @property
    def DynamicColumnType(self) -> IPEDynamicColumnType:"""DynamicColumnType { get; set; } -> IPEDynamicColumnType"""
    @property
    def FieldDialog(self) -> _n_19_t_0:"""FieldDialog { get; } -> ICommand"""
    @property
    def FindReplace(self) -> _n_19_t_0:"""FindReplace { get; } -> ICommand"""
    @property
    def FontSizes(self) -> _n_13_t_0[str]:"""FontSizes { get; } -> ObservableCollection"""
    @property
    def HaveSelection(self) -> bool:"""HaveSelection { get; } -> bool"""
    @property
    def Import(self) -> _n_19_t_0:"""Import { get; } -> ICommand"""
    @property
    def InsertColumnBreak(self) -> bool:"""InsertColumnBreak { get; set; } -> bool"""
    @property
    def InsertField(self) -> bool:"""InsertField { get; set; } -> bool"""
    @property
    def IsActive(self) -> bool:"""IsActive { get; } -> bool"""
    @property
    def IsAnnotativeEnabled(self) -> bool:"""IsAnnotativeEnabled { get; } -> bool"""
    @property
    def IsAutoListEnabled(self) -> bool:"""IsAutoListEnabled { get; set; } -> bool"""
    @property
    def IsBoldEnabled(self) -> bool:"""IsBoldEnabled { get; } -> bool"""
    @property
    def IsChangeCaseAvailable(self) -> bool:"""IsChangeCaseAvailable { get; } -> bool"""
    @property
    def IsColumnsEnabled(self) -> bool:"""IsColumnsEnabled { get; } -> bool"""
    @property
    def IsInsertColumnBreak(self) -> bool:"""IsInsertColumnBreak { get; } -> bool"""
    @property
    def IsInsertFieldEnabled(self) -> bool:"""IsInsertFieldEnabled { get; } -> bool"""
    @property
    def IsItalicEnabled(self) -> bool:"""IsItalicEnabled { get; } -> bool"""
    @property
    def IsLineSpacingFactorAvailable(self) -> bool:"""IsLineSpacingFactorAvailable { get; } -> bool"""
    @property
    def IsMatchPropertiesState(self) -> bool:"""IsMatchPropertiesState { get; set; } -> bool"""
    @property
    def IsOpaqueBackgroundEnabled(self) -> bool:"""IsOpaqueBackgroundEnabled { get; } -> bool"""
    @property
    def IsOverlineEnabled(self) -> bool:"""IsOverlineEnabled { get; } -> bool"""
    @property
    def IsParagraphAlignmentAvailable(self) -> bool:"""IsParagraphAlignmentAvailable { get; } -> bool"""
    @property
    def IsRedoEnabled(self) -> bool:"""IsRedoEnabled { get; } -> bool"""
    @property
    def IsRulerChecked(self) -> bool:"""IsRulerChecked { get; } -> bool"""
    @property
    def IsRulerEnabled(self) -> bool:"""IsRulerEnabled { get; } -> bool"""
    @property
    def IsShowToolbarEnabled(self) -> bool:"""IsShowToolbarEnabled { get; } -> bool"""
    @property
    def IsSpellerEnabled(self) -> bool:"""IsSpellerEnabled { get; } -> bool"""
    @property
    def IsStackOrUnstackEnabled(self) -> bool:"""IsStackOrUnstackEnabled { get; } -> bool"""
    @property
    def IsStrikeThroughEnabled(self) -> bool:"""IsStrikeThroughEnabled { get; } -> bool"""
    @property
    def IsTabOnlyDelimiterEnabled(self) -> bool:"""IsTabOnlyDelimiterEnabled { get; } -> bool"""
    @property
    def IsUnderlineEnabled(self) -> bool:"""IsUnderlineEnabled { get; } -> bool"""
    @property
    def IsUndoEnabled(self) -> bool:"""IsUndoEnabled { get; } -> bool"""
    @property
    def IsWysiwyg(self) -> bool:"""IsWysiwyg { get; } -> bool"""
    @property
    def Italic(self) -> bool:"""Italic { get; set; } -> bool"""
    @property
    def LanguageIndexType(self) -> int:"""LanguageIndexType { get; } -> int"""
    @property
    def LineSpacingFactor(self) -> float:"""LineSpacingFactor { get; set; } -> float"""
    @property
    def LineSpacingFactors(self) -> _n_13_t_1[float]:"""LineSpacingFactors { get; } -> Collection"""
    @property
    def LineSpacingMultiples(self) -> _n_19_t_0:"""LineSpacingMultiples { get; } -> ICommand"""
    @property
    def LineSpacingType(self) -> LineSpacingTypes:"""LineSpacingType { get; set; } -> LineSpacingTypes"""
    @property
    def Lowercase(self) -> _n_19_t_0:"""Lowercase { get; } -> ICommand"""
    @property
    def MoreLineSpace(self) -> _n_19_t_0:"""MoreLineSpace { get; } -> ICommand"""
    @property
    def Numbering(self) -> _n_19_t_0:"""Numbering { get; } -> ICommand"""
    @property
    def NumberingAvailable(self) -> bool:"""NumberingAvailable { get; set; } -> bool"""
    @property
    def NumberingType(self) -> IPENumberingType:"""NumberingType { get; set; } -> IPENumberingType"""
    @property
    def ObliqueAngle(self) -> float:"""ObliqueAngle { get; set; } -> float"""
    @property
    def OpaqueBackground(self) -> bool:"""OpaqueBackground { get; set; } -> bool"""
    @property
    def Options(self) -> _n_19_t_0:"""Options { get; } -> ICommand"""
    @property
    def Overline(self) -> bool:"""Overline { get; set; } -> bool"""
    @property
    def ParagraphAlignment(self) -> IPEParagraphAlignmentType:"""ParagraphAlignment { get; set; } -> IPEParagraphAlignmentType"""
    @property
    def ParagraphAlignmentOpions(self) -> _n_19_t_0:"""ParagraphAlignmentOpions { get; } -> ICommand"""
    @property
    def ParagraphDialog(self) -> _n_19_t_0:"""ParagraphDialog { get; } -> ICommand"""
    @property
    def QuickFindText(self) -> _n_19_t_0:"""QuickFindText { get; } -> ICommand"""
    @property
    def Redo(self) -> _n_19_t_0:"""Redo { get; } -> ICommand"""
    @property
    def Ruler(self) -> bool:"""Ruler { get; set; } -> bool"""
    @property
    def Scriptable(self) -> bool:"""Scriptable { get; } -> bool"""
    @property
    def ShowToolbar(self) -> bool:"""ShowToolbar { get; set; } -> bool"""
    @property
    def Speller(self) -> bool:"""Speller { get; set; } -> bool"""
    @property
    def Stacked(self) -> bool:"""Stacked { get; set; } -> bool"""
    @property
    def StaticColumns(self) -> _n_19_t_0:"""StaticColumns { get; } -> ICommand"""
    @property
    def StaticColumnsList(self) -> _n_13_t_1[float]:"""StaticColumnsList { get; } -> Collection"""
    @property
    def StaticColumnType(self) -> IPEStaticColumnType:"""StaticColumnType { get; set; } -> IPEStaticColumnType"""
    @property
    def StrikeThrough(self) -> bool:"""StrikeThrough { get; set; } -> bool"""
    @property
    def Subscript(self) -> bool:"""Subscript { get; set; } -> bool"""
    @property
    def Superscript(self) -> bool:"""Superscript { get; set; } -> bool"""
    @property
    def TextHeight(self) -> object:"""TextHeight { get; set; } -> object"""
    @property
    def TextStyle(self) -> object:"""TextStyle { get; set; } -> object"""
    @property
    def TrackingFactor(self) -> float:"""TrackingFactor { get; set; } -> float"""
    @property
    def Underline(self) -> bool:"""Underline { get; set; } -> bool"""
    @property
    def Undo(self) -> _n_19_t_0:"""Undo { get; } -> ICommand"""
    @property
    def Uppercase(self) -> _n_19_t_0:"""Uppercase { get; } -> ICommand"""
    @property
    def WidthScale(self) -> float:"""WidthScale { get; set; } -> float"""
class InputBuffer(_n_15_t_0):
    @property
    def HasSelection(self) -> bool:"""HasSelection { get; } -> bool"""
    @property
    def Position(self) -> int:"""Position { get; } -> int"""
    @property
    def SelectPosition(self) -> int:"""SelectPosition { get; } -> int"""
    @property
    def Text(self) -> str:"""Text { get; } -> str"""
    def ExecuteKeyword(self, keyword: str) -> bool:...
    def IsPromptingForCommandName(self) -> bool:...
    def OnCharQueue(self, inputChar: _n_10_t_13, repCnt: _n_10_t_13, flags: _n_10_t_13) -> bool:...
    def OnKeyDownQueue(self, inputChar: _n_10_t_13, repCnt: _n_10_t_13, flags: _n_10_t_13) -> bool:...
    def OnSetSelectedTextQueue(self, start: int, end: int) -> bool:...
    def OnSysKeyDownQueue(self, inputChar: _n_10_t_13, repCnt: _n_10_t_13, flags: _n_10_t_13) -> bool:...
    def ParseKeywordForExecute(self, keyword: str) -> str:...
    def PasteString(self, originalString: str, stringToPaste: str):...
    def ReplaceInputQueue(self, newInput: str):...
class InputSearchOptions(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    AutoComplete: int
    AutoCorrect: int
    ContentSearch: int
    MidString: int
    _None: int
    SysvarSearch: int
    value__: int
class Int32ToImageConverter(_n_18_t_0):
    @property
    def Images(self) -> _n_12_t_1[_n_20_t_0]:"""Images { get; } -> List"""
    def __init__(self) -> Int32ToImageConverter:...
class IPEAttachmentPoint(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    BottomCenter: int
    BottomLeft: int
    BottomRight: int
    MiddleCenter: int
    MiddleLeft: int
    MiddleRight: int
    TopCenter: int
    TopLeft: int
    TopRight: int
    value__: int
class IPEColumnType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    DynamicColumns: int
    NoColumns: int
    StaticColumns: int
    value__: int
class IPECommandBase(_n_19_t_0):
    def SetCanExecute(self, value: bool):...
class IPEDynamicColumnType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    DynamicAutoHeight: int
    DynamicManualHeight: int
    value__: int
class IPEEditorSettings(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    AlwaysDisplayWysiwyg: int
    CheckSpelling: int
    OpaqueBackground: int
    ShowRuler: int
    ShowToolbar: int
    value__: int
class IPENumberingType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    NumberingBullet: int
    NumberingLettered: int
    NumberingLetterLower: int
    NumberingLetterUpper: int
    NumberingNumber: int
    NumberingOff: int
    value__: int
class IPENumberingTypeEnumConverter(_n_15_t_4):
    def __init__(self, type: _n_10_t_14) -> IPENumberingTypeEnumConverter:...
class IPEParagraphAlignmentType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    AlignmentCenter: int
    AlignmentDefault: int
    AlignmentDistribute: int
    AlignmentJustify: int
    AlignmentLeft: int
    AlignmentRight: int
    NumAlignmentTypes: int
    value__: int
class IPEStaticColumnType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    FiveColumns: int
    FourColumns: int
    OneColumn: int
    SixColumns: int
    ThreeColumns: int
    TwoColumns: int
    value__: int
class IsoDraft(_n_15_t_0, _n_10_t_0):
    @property
    def State(self) -> int:"""State { get; set; } -> int"""
    def __init__(self) -> IsoDraft:...
class LayerFilterCollection(NamedObjectCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    pass
class LayerRecordCollection(DbObjectCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    pass
class LightEngine(_n_15_t_0, _n_10_t_0):
    @property
    def Brightness(self) -> SystemVariable:"""Brightness { get; } -> SystemVariable"""
    @property
    def Contrast(self) -> SystemVariable:"""Contrast { get; } -> SystemVariable"""
    @property
    def Date(self) -> float:"""Date { get; set; } -> float"""
    @property
    def DateTicks(self) -> _n_4_t_0:"""DateTicks { get; } -> DoubleCollection"""
    @property
    def IsDateTimeEnabled(self) -> bool:"""IsDateTimeEnabled { get; set; } -> bool"""
    @property
    def IsUsingGenericLightingUnits(self) -> bool:"""IsUsingGenericLightingUnits { get; } -> bool"""
    @property
    def MaxDate(self) -> float:"""MaxDate { get; } -> float"""
    @property
    def MaxTime(self) -> float:"""MaxTime { get; } -> float"""
    @property
    def MinDate(self) -> float:"""MinDate { get; } -> float"""
    @property
    def MinTime(self) -> float:"""MinTime { get; } -> float"""
    @property
    def Time(self) -> float:"""Time { get; set; } -> float"""
    def __init__(self) -> LightEngine:...
class LineSpacingMultiplesCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> LineSpacingMultiplesCommand:...
class LineSpacingTypes(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    LineSpacingAtLeast: int
    LineSpacingExactly: int
    LineSpacingMultiple: int
    value__: int
class LineSpacingTypesEnumConverter(_n_15_t_4):
    def __init__(self, type: _n_10_t_14) -> LineSpacingTypesEnumConverter:...
class LineWeightCollection(EnumItemCollection, _n_12_t_0[_n_15_t_2], _n_15_t_0, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    pass
class LowercaseCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> LowercaseCommand:...
class MoreLineSpaceCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> MoreLineSpaceCommand:...
class MultiReplaceConverter(_n_18_t_0):
    @property
    def DefaultConverter(self) -> _n_18_t_0:"""DefaultConverter { get; set; } -> IValueConverter"""
    @property
    def Filters(self) -> _n_12_t_1[ReplaceConverter]:"""Filters { get; } -> List"""
    def __init__(self) -> MultiReplaceConverter:...
class NamedImageProvider(_n_18_t_0):
    @property
    def ImageProvider(self) -> INamedImageProvider:"""ImageProvider { get; set; } -> INamedImageProvider"""
    def __init__(self) -> NamedImageProvider:...
class NamedObjectCollection(DataItemCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    pass
class NativeFunction(_n_19_t_0, _n_10_t_0):
    pass
class NavStatus(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    Default: int
    _None: int
    Paused: int
    Recording: int
    value__: int
class NotifyCollectionItemsChangedEventArgs(_n_10_t_12):
    @property
    def Items(self) -> _n_11_t_0:"""Items { get; } -> IList"""
    def __init__(self, items: _n_11_t_0) -> NotifyCollectionItemsChangedEventArgs:...
class NotifyCollectionItemsChangedEventHandler(_n_10_t_9, _n_10_t_6, _n_17_t_0):
    def __init__(self, A_0: object, A_1: _n_10_t_7) -> NotifyCollectionItemsChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: NotifyCollectionItemsChangedEventArgs, callback: _n_10_t_11, obj: object) -> _n_10_t_10:...
    def EndInvoke(self, result: _n_10_t_10):...
    def Invoke(self, sender: object, e: NotifyCollectionItemsChangedEventArgs):...
class NullToVariesConverter(_n_18_t_0):
    def __init__(self) -> NullToVariesConverter:...
class NumberingCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> NumberingCommand:...
class OptionsCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> OptionsCommand:...
class ParagraphAlignmentOpionsCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> ParagraphAlignmentOpionsCommand:...
class ParagraphDialogCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> ParagraphDialogCommand:...
class PatPatternCategory(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
    kCustomdef: int
    kInvalid: int
    kISOdef: int
    kPredef: int
    kSolid_fill: int
    kUserdef: int
    value__: int
class PlotStyleCollection(DbObjectCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    pass
class PlotStyleNameToDataItemConverter(_n_18_t_0):
    def __init__(self) -> PlotStyleNameToDataItemConverter:...
class PromptAndInput(_n_15_t_0):
    @property
    def InputBuffer(self) -> InputBuffer:"""InputBuffer { get; } -> InputBuffer"""
    @property
    def KeywordsStringLength(self) -> int:"""KeywordsStringLength { get; } -> int"""
    @property
    def KeywordsStringStart(self) -> int:"""KeywordsStringStart { get; } -> int"""
    @property
    def Position(self) -> int:"""Position { get; } -> int"""
    @property
    def Prompt(self) -> str:"""Prompt { get; } -> str"""
    @property
    def PromptDefault(self) -> str:"""PromptDefault { get; } -> str"""
    @property
    def PromptKeywords(self) -> _n_13_t_0[str]:"""PromptKeywords { get; } -> ObservableCollection"""
    @property
    def SelectPosition(self) -> int:"""SelectPosition { get; } -> int"""
    @property
    def Text(self) -> str:"""Text { get; } -> str"""
    @property
    def Accepted(self) -> _n_10_t_15:
        """Accepted Event: EventHandler"""
    @property
    def Canceled(self) -> _n_10_t_15:
        """Canceled Event: EventHandler"""
class RedoCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> RedoCommand:...
class RenderPresetConverter(_n_18_t_0):
    def __init__(self) -> RenderPresetConverter:...
class ReplaceConverter(_n_18_t_0):
    @property
    def Converter(self) -> _n_18_t_0:"""Converter { get; set; } -> IValueConverter"""
    @property
    def SourceValue(self) -> object:"""SourceValue { get; set; } -> object"""
    @property
    def TargetValue(self) -> object:"""TargetValue { get; set; } -> object"""
    def __init__(self) -> ReplaceConverter:...
class Selection(DbObjectCollection, _n_12_t_0[_n_15_t_2], _n_14_t_0, _n_15_t_0, INotifyCollectionItemsChanged, _n_10_t_0, IInvalidateProperty, IDataItemCache, typing.Iterable[_n_15_t_2]):
    @property
    def CommonProperties(self) -> CommonProperties:"""CommonProperties { get; } -> CommonProperties"""
    @property
    def IsContinuing(self) -> bool:"""IsContinuing { get; set; } -> bool"""
    def ContainsAny(self, types: _n_10_t_8[str]) -> bool:...
    def ContainsAnyDrawingView(self) -> bool:...
    def ContainsOnly(self, types: _n_10_t_8[str]) -> bool:...
    def ContainsOnlyCoordinationModel(self) -> bool:...
    def ContainsOnlyDrawingView(self) -> bool:...
    def ContainsOnlyGeoMapImage(self) -> bool:...
    def isContainSectionViewHatch(self) -> bool:...
    def isOnlySectionViewHatchs(self) -> bool:...
    def RemoveNonEditableObjects(self, type: Selection.NonEditableType) -> int:...
    class NonEditableType(_n_10_t_2, _n_10_t_3, _n_10_t_4, _n_10_t_5):
        Frozen: int
        Locked: int
        Off: int
        value__: int
class SourceToTypeConverter(_n_18_t_0):
    @property
    def ConverterType(self) -> _n_10_t_14:"""ConverterType { get; set; } -> Type"""
    @property
    def SourceType(self) -> _n_10_t_14:"""SourceType { get; set; } -> Type"""
    def __init__(self) -> SourceToTypeConverter:...
class StandardConverter(_n_18_t_0):
    @property
    def SourceType(self) -> _n_10_t_14:"""SourceType { get; set; } -> Type"""
    @property
    def TargetType(self) -> _n_10_t_14:"""TargetType { get; set; } -> Type"""
    def __init__(self) -> StandardConverter:...
class StandardUcsPlane(object):
    @property
    def Back(self) -> object:"""Back { get; } -> object"""
    @property
    def Bottom(self) -> object:"""Bottom { get; } -> object"""
    @property
    def Front(self) -> object:"""Front { get; } -> object"""
    @property
    def Left(self) -> object:"""Left { get; } -> object"""
    @property
    def Right(self) -> object:"""Right { get; } -> object"""
    @property
    def Top(self) -> object:"""Top { get; } -> object"""
    @property
    def Unnamed(self) -> object:"""Unnamed { get; } -> object"""
    @property
    def World(self) -> object:"""World { get; } -> object"""
class StaticColumnsCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> StaticColumnsCommand:...
class SubEntity(_n_10_t_0):
    @property
    def ParentType(self) -> _n_10_t_14:"""ParentType { get; } -> Type"""
    @staticmethod
    def Create(path: _n_3_t_2) -> SubEntity:...
class SystemVariable(_n_15_t_0, ITrueValueAble, _n_10_t_0):
    @property
    def IsEnabled(self) -> bool:"""IsEnabled { get; } -> bool"""
    @property
    def Maximum(self) -> float:"""Maximum { get; } -> float"""
    @property
    def Minimum(self) -> float:"""Minimum { get; } -> float"""
    @property
    def MutedValue(self) -> object:"""MutedValue { get; set; } -> object"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def TrueValues(self) -> TrueValues:"""TrueValues { get; } -> TrueValues"""
    @property
    def ValueType(self) -> _n_10_t_14:"""ValueType { get; } -> Type"""
class SysvarMonitorState(_n_15_t_0, _n_10_t_0):
    @property
    def DifferenceNumber(self) -> int:"""DifferenceNumber { get; } -> int"""
    @property
    def HasDifference(self) -> bool:"""HasDifference { get; } -> bool"""
    @property
    def ShowBalloon(self) -> bool:"""ShowBalloon { get; } -> bool"""
    def __init__(self) -> SysvarMonitorState:...
    def ShowDialog(self):...
    def SyncState(self):...
class TextSize(_n_15_t_0, _n_10_t_0):
    m_TextSize: int
    @property
    def FontSizes(self) -> _n_13_t_0[str]:"""FontSizes { get; } -> ObservableCollection"""
    @property
    def TextHeight(self) -> object:"""TextHeight { get; set; } -> object"""
class ThemeEngine(_n_15_t_0, _n_10_t_0):
    @property
    def Brightness(self) -> float:"""Brightness { get; } -> float"""
    @property
    def Hue(self) -> float:"""Hue { get; } -> float"""
    @property
    def Saturation(self) -> float:"""Saturation { get; } -> float"""
    def __init__(self) -> ThemeEngine:...
class TransparencyItem(_n_10_t_1):
    @property
    def ErrorText(self) -> str:"""ErrorText { get; } -> str"""
    @property
    def LayerValue(self) -> int:"""LayerValue { get; } -> int"""
    @property
    def Transparency(self) -> _n_2_t_1:"""Transparency { get; } -> Transparency"""
    def __init__(self, transparency: _n_2_t_1, ErrorText: str) -> TransparencyItem:...
class TrueValues(_n_15_t_0):
    @property
    def AcadColor(self) -> _n_2_t_0:"""AcadColor { get; set; } -> Color"""
    @property
    def HPBACKGROUNDCOLOR(self) -> str:"""HPBACKGROUNDCOLOR { get; set; } -> str"""
    @property
    def HPCOLOR(self) -> str:"""HPCOLOR { get; set; } -> str"""
    @property
    def StringValue(self) -> str:"""StringValue { get; set; } -> str"""
class UIFontInfo(object):
    @property
    def Image(self) -> _n_20_t_0:"""Image { get; } -> ImageSource"""
    @property
    def IsTrueType(self) -> bool:"""IsTrueType { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, fontName: str, isTrueType: bool) -> UIFontInfo:...
    @staticmethod
    def GetFontInfo(fontName: str) -> UIFontInfo:...
    @staticmethod
    def GetFontInfoCollection() -> _n_13_t_1[UIFontInfo]:...
class UndoCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> UndoCommand:...
class UppercaseCommand(IPECommandBase, _n_19_t_0):
    def __init__(self) -> UppercaseCommand:...
class ValueToNamedValueConverter(_n_18_t_0):
    def __init__(self) -> ValueToNamedValueConverter:...
class View2DRibbonItemData(_n_10_t_0):
    mIconKey: int
    mId: int
    mId2: int
    mKey: int
    mText: int
    @property
    def Key(self) -> str:"""Key { get; } -> str"""
    @property
    def Text(self) -> str:"""Text { get; } -> str"""
    def __init__(self) -> View2DRibbonItemData:...
    def __init__(self, id: int, text: _n_10_t_16, iconkey: _n_10_t_16, id2: _n_10_t_13) -> View2DRibbonItemData:...
class Views2DCommands(_n_15_t_0, _n_10_t_0):
    @property
    def AutoUpdate(self) -> bool:"""AutoUpdate { get; set; } -> bool"""
    @property
    def CircularRbt(self) -> bool:"""CircularRbt { get; set; } -> bool"""
    @property
    def CutInheritance_1(self) -> bool:"""CutInheritance_1 { get; set; } -> bool"""
    @property
    def DeferUpdate(self) -> bool:"""DeferUpdate { get; set; } -> bool"""
    @property
    def Depth(self) -> float:"""Depth { get; set; } -> float"""
    @property
    def DepthType(self) -> object:"""DepthType { get; set; } -> object"""
    @property
    def DepthTypeList(self) -> _n_13_t_0[View2DRibbonItemData]:"""DepthTypeList { get; } -> ObservableCollection"""
    @property
    def DesignView(self) -> object:"""DesignView { get; set; } -> object"""
    @property
    def DesignViewList(self) -> _n_13_t_0[str]:"""DesignViewList { get; } -> ObservableCollection"""
    @property
    def DetailLevel(self) -> object:"""DetailLevel { get; set; } -> object"""
    @property
    def DetailLevelList(self) -> _n_13_t_0[str]:"""DetailLevelList { get; } -> ObservableCollection"""
    @property
    def Identifier(self) -> str:"""Identifier { get; set; } -> str"""
    @property
    def IsEmptyMS(self) -> int:"""IsEmptyMS { get; } -> int"""
    @property
    def IsEnabledAccept(self) -> bool:"""IsEnabledAccept { get; } -> bool"""
    @property
    def IsEnabledAutoUpdate(self) -> bool:"""IsEnabledAutoUpdate { get; } -> bool"""
    @property
    def IsEnabledBoundaryRbt(self) -> bool:"""IsEnabledBoundaryRbt { get; } -> bool"""
    @property
    def IsEnabledCancel(self) -> bool:"""IsEnabledCancel { get; } -> bool"""
    @property
    def IsEnabledCutInheritance(self) -> bool:"""IsEnabledCutInheritance { get; } -> bool"""
    @property
    def IsEnabledCutInheritance1(self) -> bool:"""IsEnabledCutInheritance1 { get; } -> bool"""
    @property
    def IsEnabledDeferUpdate(self) -> bool:"""IsEnabledDeferUpdate { get; } -> bool"""
    @property
    def IsEnabledDepth(self) -> bool:"""IsEnabledDepth { get; } -> bool"""
    @property
    def IsEnabledDepthDrag(self) -> bool:"""IsEnabledDepthDrag { get; } -> bool"""
    @property
    def IsEnabledDepthType(self) -> bool:"""IsEnabledDepthType { get; } -> bool"""
    @property
    def IsEnabledDesignView(self) -> bool:"""IsEnabledDesignView { get; } -> bool"""
    @property
    def IsEnabledDetailLevel(self) -> bool:"""IsEnabledDetailLevel { get; } -> bool"""
    @property
    def IsEnabledIdentifier(self) -> bool:"""IsEnabledIdentifier { get; } -> bool"""
    @property
    def IsEnabledMember(self) -> bool:"""IsEnabledMember { get; } -> bool"""
    @property
    def IsEnabledModelEdgeRbt(self) -> bool:"""IsEnabledModelEdgeRbt { get; } -> bool"""
    @property
    def IsEnabledMove(self) -> bool:"""IsEnabledMove { get; } -> bool"""
    @property
    def IsEnabledOption(self) -> bool:"""IsEnabledOption { get; } -> bool"""
    @property
    def IsEnabledOrientation(self) -> bool:"""IsEnabledOrientation { get; } -> bool"""
    @property
    def IsEnabledPosRepresentation(self) -> bool:"""IsEnabledPosRepresentation { get; } -> bool"""
    @property
    def IsEnabledPresentation(self) -> bool:"""IsEnabledPresentation { get; } -> bool"""
    @property
    def IsEnabledProjectionView(self) -> bool:"""IsEnabledProjectionView { get; } -> bool"""
    @property
    def IsEnabledScale(self) -> bool:"""IsEnabledScale { get; } -> bool"""
    @property
    def IsEnabledSelect(self) -> bool:"""IsEnabledSelect { get; } -> bool"""
    @property
    def IsEnabledSheetMetal(self) -> bool:"""IsEnabledSheetMetal { get; } -> bool"""
    @property
    def IsEnabledShowHatch(self) -> bool:"""IsEnabledShowHatch { get; } -> bool"""
    @property
    def IsEnabledSViewLabel(self) -> bool:"""IsEnabledSViewLabel { get; } -> bool"""
    @property
    def IsEnabledViewStyle(self) -> bool:"""IsEnabledViewStyle { get; } -> bool"""
    @property
    def IsEnabledVisibility(self) -> bool:"""IsEnabledVisibility { get; } -> bool"""
    @property
    def IsEnabledVisibility1(self) -> bool:"""IsEnabledVisibility1 { get; } -> bool"""
    @property
    def IsEnabledVisibility2(self) -> bool:"""IsEnabledVisibility2 { get; } -> bool"""
    @property
    def IsEnabledVisibility3(self) -> bool:"""IsEnabledVisibility3 { get; } -> bool"""
    @property
    def IsEnabledVisibility4(self) -> bool:"""IsEnabledVisibility4 { get; } -> bool"""
    @property
    def IsEnabledVisibility5(self) -> bool:"""IsEnabledVisibility5 { get; } -> bool"""
    @property
    def IsEnabledVisibility6(self) -> bool:"""IsEnabledVisibility6 { get; } -> bool"""
    @property
    def IsEnabledWeldment(self) -> bool:"""IsEnabledWeldment { get; } -> bool"""
    @property
    def IsEnableGradientPatern(self) -> bool:"""IsEnableGradientPatern { get; } -> bool"""
    @property
    def IsEnableReturn(self) -> bool:"""IsEnableReturn { get; } -> bool"""
    @property
    def JaggedRbt(self) -> bool:"""JaggedRbt { get; set; } -> bool"""
    @property
    def Member(self) -> object:"""Member { get; set; } -> object"""
    @property
    def MemberList(self) -> _n_13_t_0[View2DRibbonItemData]:"""MemberList { get; } -> ObservableCollection"""
    @property
    def Orientation(self) -> object:"""Orientation { get; set; } -> object"""
    @property
    def OrientationList(self) -> _n_13_t_0[View2DRibbonItemData]:"""OrientationList { get; } -> ObservableCollection"""
    @property
    def PosRepresentation(self) -> object:"""PosRepresentation { get; set; } -> object"""
    @property
    def PosRepresentationList(self) -> _n_13_t_0[str]:"""PosRepresentationList { get; } -> ObservableCollection"""
    @property
    def Presentation(self) -> object:"""Presentation { get; set; } -> object"""
    @property
    def PresentationList(self) -> _n_13_t_0[str]:"""PresentationList { get; } -> ObservableCollection"""
    @property
    def ProjectionView(self) -> object:"""ProjectionView { get; set; } -> object"""
    @property
    def ProjectionViewList(self) -> _n_13_t_0[View2DRibbonItemData]:"""ProjectionViewList { get; } -> ObservableCollection"""
    @property
    def RectangularRbt(self) -> bool:"""RectangularRbt { get; set; } -> bool"""
    @property
    def Scale(self) -> object:"""Scale { get; set; } -> object"""
    @property
    def ScaleList(self) -> _n_13_t_0[str]:"""ScaleList { get; } -> ObservableCollection"""
    @property
    def SheetMetal(self) -> object:"""SheetMetal { get; set; } -> object"""
    @property
    def SheetMetalList(self) -> _n_13_t_0[View2DRibbonItemData]:"""SheetMetalList { get; } -> ObservableCollection"""
    @property
    def ShowHatch(self) -> bool:"""ShowHatch { get; set; } -> bool"""
    @property
    def SmoothRbt(self) -> bool:"""SmoothRbt { get; set; } -> bool"""
    @property
    def SmoothWBRbt(self) -> bool:"""SmoothWBRbt { get; set; } -> bool"""
    @property
    def SmoothWCRbt(self) -> bool:"""SmoothWCRbt { get; set; } -> bool"""
    @property
    def StyleObject(self) -> _n_9_t_1:"""StyleObject { get; set; } -> RibbonListButton"""
    @property
    def SViewLabel(self) -> bool:"""SViewLabel { get; set; } -> bool"""
    @property
    def ViewAccept(self) -> _n_19_t_0:"""ViewAccept { get; } -> ICommand"""
    @property
    def ViewBaseINV(self) -> _n_19_t_0:"""ViewBaseINV { get; } -> ICommand"""
    @property
    def ViewBaseMS(self) -> _n_19_t_0:"""ViewBaseMS { get; } -> ICommand"""
    @property
    def ViewCancel(self) -> _n_19_t_0:"""ViewCancel { get; } -> ICommand"""
    @property
    def ViewMove(self) -> _n_19_t_0:"""ViewMove { get; } -> ICommand"""
    @property
    def ViewOption(self) -> _n_19_t_0:"""ViewOption { get; } -> ICommand"""
    @property
    def ViewReturn(self) -> _n_19_t_0:"""ViewReturn { get; } -> ICommand"""
    @property
    def ViewSelect(self) -> _n_19_t_0:"""ViewSelect { get; } -> ICommand"""
    @property
    def ViewSelectDepth(self) -> _n_19_t_0:"""ViewSelectDepth { get; } -> ICommand"""
    @property
    def ViewStyle(self) -> int:"""ViewStyle { get; set; } -> int"""
    @property
    def ViewStyleFB(self) -> _n_19_t_0:"""ViewStyleFB { get; } -> ICommand"""
    @property
    def ViewStyleFBImage(self) -> object:"""ViewStyleFBImage { get; } -> object"""
    @property
    def ViewStyleFBText(self) -> str:"""ViewStyleFBText { get; } -> str"""
    @property
    def ViewStyleSH(self) -> _n_19_t_0:"""ViewStyleSH { get; } -> ICommand"""
    @property
    def ViewStyleSV(self) -> _n_19_t_0:"""ViewStyleSV { get; } -> ICommand"""
    @property
    def ViewStyleWH(self) -> _n_19_t_0:"""ViewStyleWH { get; } -> ICommand"""
    @property
    def ViewStyleWV(self) -> _n_19_t_0:"""ViewStyleWV { get; } -> ICommand"""
    @property
    def ViewUpdateAll(self) -> _n_19_t_0:"""ViewUpdateAll { get; } -> ICommand"""
    @property
    def Visibility_1(self) -> bool:"""Visibility_1 { get; set; } -> bool"""
    @property
    def Visibility_2(self) -> bool:"""Visibility_2 { get; set; } -> bool"""
    @property
    def Visibility_3(self) -> bool:"""Visibility_3 { get; set; } -> bool"""
    @property
    def Visibility_4(self) -> bool:"""Visibility_4 { get; set; } -> bool"""
    @property
    def Visibility_5(self) -> bool:"""Visibility_5 { get; set; } -> bool"""
    @property
    def Visibility_6(self) -> bool:"""Visibility_6 { get; set; } -> bool"""
    @property
    def Weldment(self) -> object:"""Weldment { get; set; } -> object"""
    @property
    def WeldmentList(self) -> _n_13_t_0[View2DRibbonItemData]:"""WeldmentList { get; } -> ObservableCollection"""
    def ConvertDoubleToStr(self, value: object, targetType: _n_10_t_14, parameter: object, culture: _n_16_t_0) -> object:...
    def convertItemData2Image(self, item: object) -> str:...
    def ConvertStrToDouble(self, value: object, targetType: _n_10_t_14, parameter: object, culture: _n_16_t_0) -> object:...
    def isVetoSetCurrentDetailViewStyle(self) -> bool:...
    def isVetoSetCurrentSectionViewStyle(self) -> bool:...
    def showVetoWarning(self):...
    def vetoSetCurrentDetailViewStyle(self, value: object) -> bool:...
    def vetoSetCurrentSectionViewStyle(self, value: object) -> bool:...
class WorkspaceCollection(_n_13_t_0[_n_9_t_2], _n_12_t_0[_n_9_t_2], _n_11_t_0, _n_12_t_2[_n_9_t_2], _n_14_t_0, _n_15_t_0, typing.Iterable[_n_9_t_2]):
    @property
    def CurrentWorkspace(self) -> _n_9_t_2:"""CurrentWorkspace { get; set; } -> RibbonItem"""
    @property
    def IsEnabled(self) -> bool:"""IsEnabled { get; } -> bool"""
    def CUILoaded(self, sender: object, e: _n_5_t_0):...
    def OnSysvarCmdNamesChanged(self, sender: object, e: _n_15_t_1):...
    def OnSysvarWSCurrentChanged(self, sender: object, e: _n_15_t_1):...
    def WorkspaceSaved(self, sender: object, e: _n_5_t_1):...
    def WorkspaceSettingsSaved(self, sender: object, e: _n_10_t_12):...
