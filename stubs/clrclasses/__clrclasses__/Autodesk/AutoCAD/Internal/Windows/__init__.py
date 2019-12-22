from __clrclasses__.System import EventArgs as _n_0_t_0
from __clrclasses__.System import MulticastDelegate as _n_0_t_1
from __clrclasses__.System import ICloneable as _n_0_t_2
from __clrclasses__.System import IntPtr as _n_0_t_3
from __clrclasses__.System import IAsyncResult as _n_0_t_4
from __clrclasses__.System import AsyncCallback as _n_0_t_5
from __clrclasses__.System import IDisposable as _n_0_t_6
from __clrclasses__.System import Enum as _n_0_t_7
from __clrclasses__.System import IComparable as _n_0_t_8
from __clrclasses__.System import IFormattable as _n_0_t_9
from __clrclasses__.System import IConvertible as _n_0_t_10
from __clrclasses__.System import Char as _n_0_t_11
from __clrclasses__.System import Uri as _n_0_t_12
from __clrclasses__.System.Collections.Generic import List as _n_1_t_0
from __clrclasses__.System.Collections.Generic import Dictionary as _n_1_t_1
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
from __clrclasses__.System.Windows import Size as _n_4_t_0
from __clrclasses__.System.Windows.Media import ImageSource as _n_5_t_0
import typing
class CommandThroat(object):
    @property
    def InputCharactersQueued(self) -> InputCharactersQueuedEventHandler:
        """InputCharactersQueued Event: InputCharactersQueuedEventHandler"""
    def __init__(self) -> CommandThroat:...
class CommandToolTipData(object):
    @property
    def BasicContent(self) -> str:"""BasicContent { get; set; } -> str"""
    @property
    def CLICommand(self) -> str:"""CLICommand { get; set; } -> str"""
    @property
    def EnableHelp(self) -> bool:"""EnableHelp { get; set; } -> bool"""
    @property
    def ExtendedContentKey(self) -> str:"""ExtendedContentKey { get; set; } -> str"""
    @property
    def ExtendedContentSource(self) -> str:"""ExtendedContentSource { get; set; } -> str"""
    @property
    def HelpSource(self) -> str:"""HelpSource { get; set; } -> str"""
    @property
    def HelpTopic(self) -> str:"""HelpTopic { get; set; } -> str"""
    @property
    def Macro(self) -> str:"""Macro { get; set; } -> str"""
    @property
    def Shortcut(self) -> str:"""Shortcut { get; set; } -> str"""
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    @property
    def UserTag(self) -> str:"""UserTag { get; set; } -> str"""
    def __init__(self) -> CommandToolTipData:...
class InputCharactersQueuedEventArgs(_n_0_t_0):
    @property
    def Characters(self) -> str:"""Characters { get; } -> str"""
class InputCharactersQueuedEventHandler(_n_0_t_1, _n_0_t_2, _n_3_t_0):
    def __init__(self, A_0: object, A_1: _n_0_t_3) -> InputCharactersQueuedEventHandler:...
    def BeginInvoke(self, sender: object, e: InputCharactersQueuedEventArgs, callback: _n_0_t_5, obj: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: InputCharactersQueuedEventArgs):...
class MenuGroupData(_n_0_t_6):
    @property
    def DefaultToolTipHelpSource(self) -> str:"""DefaultToolTipHelpSource { get; } -> str"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def MenuGroupType(self) -> MenuGroupTypeEnum:"""MenuGroupType { get; } -> MenuGroupTypeEnum"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def PartialMenus(self) -> _n_1_t_0[MenuGroupData]:"""PartialMenus { get; } -> List"""
    def __init__(self, nMenuGroupType: MenuGroupTypeEnum, sName: str, sFileName: str, pMenuGroupData: object) -> MenuGroupData:...
    def GetMenuMacro(self, sId: str) -> RibbonMenuMacro:...
    def GetMenuMacro(self) -> _n_1_t_1[str, RibbonMenuMacro]:...
class MenuGroupTypeEnum(_n_0_t_7, _n_0_t_8, _n_0_t_9, _n_0_t_10):
    Enterprise: int
    Main: int
    Partial: int
    value__: int
class ProfileManager(object):
    def __init__(self) -> ProfileManager:...
    @staticmethod
    def GetProfileNode(pNode: object, pszNodePath: _n_0_t_11, bCreateIfNotExists: bool, bCurrentProfile: bool) -> bool:...
    @staticmethod
    def LoadData(sNodePath: str, sWSName: str, bCurrentProfile: bool) -> str:...
    @staticmethod
    def LoadHideableDialogSettingsDictionary() -> bool:...
    @staticmethod
    def SaveData(sXmlData: str, sNodePath: str, sWorkspaceName: str, bCurrentProfile: bool) -> bool:...
    @staticmethod
    def SaveHideableDialogSettingsDictionary() -> bool:...
class RibbonData(object):
    def __init__(self) -> RibbonData:...
    @staticmethod
    def CreateHwndControl(sControlName: str, sModule: str, hwndParent: _n_0_t_3) -> _n_0_t_3:...
    @staticmethod
    def CreateInvalidHwndControl(hWndParent: _n_0_t_3) -> _n_0_t_3:...
    @staticmethod
    def GetDefaultToolTipContentSources() -> _n_2_t_0[_n_0_t_12]:...
    @staticmethod
    def GetMenuGroups() -> _n_1_t_0[MenuGroupData]:...
    @staticmethod
    def GetProfileStorageFilename() -> str:...
    @staticmethod
    def GetWindowSize(hWnd: _n_0_t_3) -> _n_4_t_0:...
    @staticmethod
    def Load(sImage: str, sModule: str, sGroupName: str, bSmall: bool) -> _n_5_t_0:...
    @staticmethod
    def Load(sCompoundName: str, sGroupName: str, bSmall: bool) -> _n_5_t_0:...
    @staticmethod
    def LoadXml(sNodeName: str, sWSName: str) -> str:...
    @staticmethod
    def SaveXml(sData: str, sWSName: str) -> bool:...
class RibbonMenuMacro(object):
    @property
    def CLICommand(self) -> str:"""CLICommand { get; } -> str"""
    @property
    def Command(self) -> str:"""Command { get; } -> str"""
    @property
    def ElementID(self) -> str:"""ElementID { get; } -> str"""
    @property
    def LargeImage(self) -> _n_5_t_0:"""LargeImage { get; } -> ImageSource"""
    @property
    def LargeImageStr(self) -> str:"""LargeImageStr { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Shortcut(self) -> str:"""Shortcut { get; } -> str"""
    @property
    def SmallImage(self) -> _n_5_t_0:"""SmallImage { get; } -> ImageSource"""
    @property
    def SmallImageStr(self) -> str:"""SmallImageStr { get; } -> str"""
    @property
    def ToolTipData(self) -> CommandToolTipData:"""ToolTipData { get; } -> CommandToolTipData"""
    @property
    def UserTag(self) -> str:"""UserTag { get; } -> str"""
    def __init__(self, pAcMenuMacroData: object) -> RibbonMenuMacro:...
