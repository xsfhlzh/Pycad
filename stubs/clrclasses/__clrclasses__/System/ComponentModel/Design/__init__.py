import __clrclasses__.System.ComponentModel.Design.Serialization as Serialization
from __clrclasses__.System import EventArgs as _n_0_t_0
from __clrclasses__.System import MulticastDelegate as _n_0_t_1
from __clrclasses__.System import ICloneable as _n_0_t_2
from __clrclasses__.System import IntPtr as _n_0_t_3
from __clrclasses__.System import IAsyncResult as _n_0_t_4
from __clrclasses__.System import AsyncCallback as _n_0_t_5
from __clrclasses__.System import Exception as _n_0_t_6
from __clrclasses__.System import Guid as _n_0_t_7
from __clrclasses__.System import Array as _n_0_t_8
from __clrclasses__.System import IDisposable as _n_0_t_9
from __clrclasses__.System import EventHandler as _n_0_t_10
from __clrclasses__.System import IServiceProvider as _n_0_t_11
from __clrclasses__.System import Enum as _n_0_t_12
from __clrclasses__.System import IComparable as _n_0_t_13
from __clrclasses__.System import IFormattable as _n_0_t_14
from __clrclasses__.System import IConvertible as _n_0_t_15
from __clrclasses__.System import Attribute as _n_0_t_16
from __clrclasses__.System import Type as _n_0_t_17
from __clrclasses__.System.Collections import ICollection as _n_1_t_0
from __clrclasses__.System.Collections import IList as _n_1_t_1
from __clrclasses__.System.Collections import CollectionBase as _n_1_t_2
from __clrclasses__.System.Collections import IDictionary as _n_1_t_3
from __clrclasses__.System.ComponentModel import MemberDescriptor as _n_2_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_2_t_1
from __clrclasses__.System.ComponentModel import PropertyDescriptorCollection as _n_2_t_2
from __clrclasses__.System.ComponentModel import LicenseContext as _n_2_t_3
from __clrclasses__.System.ComponentModel import IContainer as _n_2_t_4
from __clrclasses__.System.ComponentModel import EventDescriptor as _n_2_t_5
from __clrclasses__.System.ComponentModel import PropertyDescriptor as _n_2_t_6
from __clrclasses__.System.ComponentModel import EventDescriptorCollection as _n_2_t_7
from __clrclasses__.System.ComponentModel import IExtenderProvider as _n_2_t_8
from __clrclasses__.System.ComponentModel import InheritanceAttribute as _n_2_t_9
from __clrclasses__.System.ComponentModel import TypeDescriptionProvider as _n_2_t_10
from __clrclasses__.System.Globalization import CultureInfo as _n_3_t_0
from __clrclasses__.System.IO import Stream as _n_4_t_0
from __clrclasses__.System.Reflection import Assembly as _n_5_t_0
from __clrclasses__.System.Reflection import AssemblyName as _n_5_t_1
from __clrclasses__.System.Resources import IResourceReader as _n_6_t_0
from __clrclasses__.System.Resources import IResourceWriter as _n_6_t_1
from __clrclasses__.System.Runtime.InteropServices import ExternalException as _n_7_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_7_t_1
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_7_t_2
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_8_t_0
import typing
class ActiveDesignerEventArgs(_n_0_t_0):
    @property
    def NewDesigner(self) -> IDesignerHost:"""NewDesigner { get; } -> IDesignerHost"""
    @property
    def OldDesigner(self) -> IDesignerHost:"""OldDesigner { get; } -> IDesignerHost"""
    def __init__(self, oldDesigner: IDesignerHost, newDesigner: IDesignerHost) -> ActiveDesignerEventArgs:...
class ActiveDesignerEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> ActiveDesignerEventHandler:...
    def BeginInvoke(self, sender: object, e: ActiveDesignerEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: ActiveDesignerEventArgs):...
class CheckoutException(_n_7_t_0, _n_8_t_0, _n_7_t_1):
    Canceled: int
    def __init__(self, message: str, innerException: _n_0_t_6) -> CheckoutException:...
    def __init__(self, message: str, errorCode: int) -> CheckoutException:...
    def __init__(self, message: str) -> CheckoutException:...
    def __init__(self) -> CheckoutException:...
class CommandID(object):
    @property
    def Guid(self) -> _n_0_t_7:"""Guid { get; } -> Guid"""
    @property
    def ID(self) -> int:"""ID { get; } -> int"""
    def __init__(self, menuGroup: _n_0_t_7, commandID: int) -> CommandID:...
class ComponentChangedEventArgs(_n_0_t_0):
    @property
    def Component(self) -> object:"""Component { get; } -> object"""
    @property
    def Member(self) -> _n_2_t_0:"""Member { get; } -> MemberDescriptor"""
    @property
    def NewValue(self) -> object:"""NewValue { get; } -> object"""
    @property
    def OldValue(self) -> object:"""OldValue { get; } -> object"""
    def __init__(self, component: object, member: _n_2_t_0, oldValue: object, newValue: object) -> ComponentChangedEventArgs:...
class ComponentChangedEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> ComponentChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: ComponentChangedEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: ComponentChangedEventArgs):...
class ComponentChangingEventArgs(_n_0_t_0):
    @property
    def Component(self) -> object:"""Component { get; } -> object"""
    @property
    def Member(self) -> _n_2_t_0:"""Member { get; } -> MemberDescriptor"""
    def __init__(self, component: object, member: _n_2_t_0) -> ComponentChangingEventArgs:...
class ComponentChangingEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> ComponentChangingEventHandler:...
    def BeginInvoke(self, sender: object, e: ComponentChangingEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: ComponentChangingEventArgs):...
class ComponentEventArgs(_n_0_t_0):
    @property
    def Component(self) -> _n_2_t_1:"""Component { get; } -> IComponent"""
    def __init__(self, component: _n_2_t_1) -> ComponentEventArgs:...
class ComponentEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> ComponentEventHandler:...
    def BeginInvoke(self, sender: object, e: ComponentEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: ComponentEventArgs):...
class ComponentRenameEventArgs(_n_0_t_0):
    @property
    def Component(self) -> object:"""Component { get; } -> object"""
    @property
    def NewName(self) -> str:"""NewName { get; } -> str"""
    @property
    def OldName(self) -> str:"""OldName { get; } -> str"""
    def __init__(self, component: object, oldName: str, newName: str) -> ComponentRenameEventArgs:...
class ComponentRenameEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> ComponentRenameEventHandler:...
    def BeginInvoke(self, sender: object, e: ComponentRenameEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: ComponentRenameEventArgs):...
class DesignerCollection(_n_1_t_0, typing.Iterable[IDesignerHost]):
    @property
    def Item(self) -> IDesignerHost:"""Item { get; } -> IDesignerHost"""
    def __init__(self, designers: _n_1_t_1) -> DesignerCollection:...
    def __init__(self, designers: _n_0_t_8[IDesignerHost]) -> DesignerCollection:...
class DesignerEventArgs(_n_0_t_0):
    @property
    def Designer(self) -> IDesignerHost:"""Designer { get; } -> IDesignerHost"""
    def __init__(self, host: IDesignerHost) -> DesignerEventArgs:...
class DesignerEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> DesignerEventHandler:...
    def BeginInvoke(self, sender: object, e: DesignerEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: DesignerEventArgs):...
class DesignerOptionService(IDesignerOptionService):
    @property
    def Options(self) -> DesignerOptionService.DesignerOptionCollection:"""Options { get; } -> DesignerOptionService.DesignerOptionCollection"""
    class DesignerOptionCollection(_n_1_t_1, typing.Iterable[DesignerOptionService.DesignerOptionCollection]):
        @property
        def Name(self) -> str:"""Name { get; } -> str"""
        @property
        def Parent(self) -> DesignerOptionService.DesignerOptionCollection:"""Parent { get; } -> DesignerOptionService.DesignerOptionCollection"""
        @property
        def Properties(self) -> _n_2_t_2:"""Properties { get; } -> PropertyDescriptorCollection"""
        def ShowDialog(self) -> bool:...
class DesignerTransaction(_n_0_t_9):
    @property
    def Canceled(self) -> bool:"""Canceled { get; } -> bool"""
    @property
    def Committed(self) -> bool:"""Committed { get; } -> bool"""
    @property
    def Description(self) -> str:"""Description { get; } -> str"""
    def Cancel(self):...
    def Commit(self):...
class DesignerTransactionCloseEventArgs(_n_0_t_0):
    @property
    def LastTransaction(self) -> bool:"""LastTransaction { get; } -> bool"""
    @property
    def TransactionCommitted(self) -> bool:"""TransactionCommitted { get; } -> bool"""
    def __init__(self, commit: bool, lastTransaction: bool) -> DesignerTransactionCloseEventArgs:...
    def __init__(self, commit: bool) -> DesignerTransactionCloseEventArgs:...
class DesignerTransactionCloseEventHandler(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> DesignerTransactionCloseEventHandler:...
    def BeginInvoke(self, sender: object, e: DesignerTransactionCloseEventArgs, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4):...
    def Invoke(self, sender: object, e: DesignerTransactionCloseEventArgs):...
class DesignerVerb(MenuCommand):
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def Text(self) -> str:"""Text { get; } -> str"""
    def __init__(self, text: str, handler: _n_0_t_10, startCommandID: CommandID) -> DesignerVerb:...
    def __init__(self, text: str, handler: _n_0_t_10) -> DesignerVerb:...
class DesignerVerbCollection(_n_1_t_2, _n_1_t_1, typing.Iterable[DesignerVerb]):
    def __init__(self, value: _n_0_t_8[DesignerVerb]) -> DesignerVerbCollection:...
    def __init__(self) -> DesignerVerbCollection:...
    def AddRange(self, value: DesignerVerbCollection):...
    def AddRange(self, value: _n_0_t_8[DesignerVerb]):...
class DesigntimeLicenseContext(_n_2_t_3, _n_0_t_11):
    def __init__(self) -> DesigntimeLicenseContext:...
class DesigntimeLicenseContextSerializer(object):
    @staticmethod
    def Serialize(o: _n_4_t_0, cryptoKey: str, context: DesigntimeLicenseContext):...
class HelpContextType(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    Ambient: int
    Selection: int
    ToolWindowSelection: int
    value__: int
    Window: int
class HelpKeywordAttribute(_n_0_t_16, _n_7_t_2):
    Default: int
    @property
    def HelpKeyword(self) -> str:"""HelpKeyword { get; } -> str"""
    def __init__(self, t: _n_0_t_17) -> HelpKeywordAttribute:...
    def __init__(self, keyword: str) -> HelpKeywordAttribute:...
    def __init__(self) -> HelpKeywordAttribute:...
class HelpKeywordType(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    F1Keyword: int
    FilterKeyword: int
    GeneralKeyword: int
    value__: int
class IComponentChangeService():
    @property
    def ComponentAdded(self) -> ComponentEventHandler:
        """ComponentAdded Event: ComponentEventHandler"""
    @property
    def ComponentAdding(self) -> ComponentEventHandler:
        """ComponentAdding Event: ComponentEventHandler"""
    @property
    def ComponentChanged(self) -> ComponentChangedEventHandler:
        """ComponentChanged Event: ComponentChangedEventHandler"""
    @property
    def ComponentChanging(self) -> ComponentChangingEventHandler:
        """ComponentChanging Event: ComponentChangingEventHandler"""
    @property
    def ComponentRemoved(self) -> ComponentEventHandler:
        """ComponentRemoved Event: ComponentEventHandler"""
    @property
    def ComponentRemoving(self) -> ComponentEventHandler:
        """ComponentRemoving Event: ComponentEventHandler"""
    @property
    def ComponentRename(self) -> ComponentRenameEventHandler:
        """ComponentRename Event: ComponentRenameEventHandler"""
    def OnComponentChanged(self, component: object, member: _n_2_t_0, oldValue: object, newValue: object):...
    def OnComponentChanging(self, component: object, member: _n_2_t_0):...
class IComponentDiscoveryService():
    def GetComponentTypes(self, designerHost: IDesignerHost, baseType: _n_0_t_17) -> _n_1_t_0:...
class IComponentInitializer():
    def InitializeExistingComponent(self, defaultValues: _n_1_t_3):...
    def InitializeNewComponent(self, defaultValues: _n_1_t_3):...
class IDesigner(_n_0_t_9):
    @property
    def Component(self) -> _n_2_t_1:"""Component { get; } -> IComponent"""
    @property
    def Verbs(self) -> DesignerVerbCollection:"""Verbs { get; } -> DesignerVerbCollection"""
    def DoDefaultAction(self):...
    def Initialize(self, component: _n_2_t_1):...
class IDesignerEventService():
    @property
    def ActiveDesigner(self) -> IDesignerHost:"""ActiveDesigner { get; } -> IDesignerHost"""
    @property
    def Designers(self) -> DesignerCollection:"""Designers { get; } -> DesignerCollection"""
    @property
    def ActiveDesignerChanged(self) -> ActiveDesignerEventHandler:
        """ActiveDesignerChanged Event: ActiveDesignerEventHandler"""
    @property
    def DesignerCreated(self) -> DesignerEventHandler:
        """DesignerCreated Event: DesignerEventHandler"""
    @property
    def DesignerDisposed(self) -> DesignerEventHandler:
        """DesignerDisposed Event: DesignerEventHandler"""
    @property
    def SelectionChanged(self) -> _n_0_t_10:
        """SelectionChanged Event: EventHandler"""
class IDesignerFilter():
    def PostFilterAttributes(self, attributes: _n_1_t_3):...
    def PostFilterEvents(self, events: _n_1_t_3):...
    def PostFilterProperties(self, properties: _n_1_t_3):...
    def PreFilterAttributes(self, attributes: _n_1_t_3):...
    def PreFilterEvents(self, events: _n_1_t_3):...
    def PreFilterProperties(self, properties: _n_1_t_3):...
class IDesignerHost(IServiceContainer):
    @property
    def Container(self) -> _n_2_t_4:"""Container { get; } -> IContainer"""
    @property
    def InTransaction(self) -> bool:"""InTransaction { get; } -> bool"""
    @property
    def Loading(self) -> bool:"""Loading { get; } -> bool"""
    @property
    def RootComponent(self) -> _n_2_t_1:"""RootComponent { get; } -> IComponent"""
    @property
    def RootComponentClassName(self) -> str:"""RootComponentClassName { get; } -> str"""
    @property
    def TransactionDescription(self) -> str:"""TransactionDescription { get; } -> str"""
    @property
    def Activated(self) -> _n_0_t_10:
        """Activated Event: EventHandler"""
    @property
    def Deactivated(self) -> _n_0_t_10:
        """Deactivated Event: EventHandler"""
    @property
    def LoadComplete(self) -> _n_0_t_10:
        """LoadComplete Event: EventHandler"""
    @property
    def TransactionClosed(self) -> DesignerTransactionCloseEventHandler:
        """TransactionClosed Event: DesignerTransactionCloseEventHandler"""
    @property
    def TransactionClosing(self) -> DesignerTransactionCloseEventHandler:
        """TransactionClosing Event: DesignerTransactionCloseEventHandler"""
    @property
    def TransactionOpened(self) -> _n_0_t_10:
        """TransactionOpened Event: EventHandler"""
    @property
    def TransactionOpening(self) -> _n_0_t_10:
        """TransactionOpening Event: EventHandler"""
    def Activate(self):...
    def CreateComponent(self, componentClass: _n_0_t_17, name: str) -> _n_2_t_1:...
    def CreateComponent(self, componentClass: _n_0_t_17) -> _n_2_t_1:...
    def CreateTransaction(self, description: str) -> DesignerTransaction:...
    def CreateTransaction(self) -> DesignerTransaction:...
    def DestroyComponent(self, component: _n_2_t_1):...
    def GetDesigner(self, component: _n_2_t_1) -> IDesigner:...
    def GetType(self, typeName: str) -> _n_0_t_17:...
class IDesignerHostTransactionState():
    @property
    def IsClosingTransaction(self) -> bool:"""IsClosingTransaction { get; } -> bool"""
class IDesignerOptionService():
    def GetOptionValue(self, pageName: str, valueName: str) -> object:...
    def SetOptionValue(self, pageName: str, valueName: str, value: object):...
class IDictionaryService():
    def GetKey(self, value: object) -> object:...
    def GetValue(self, key: object) -> object:...
    def SetValue(self, key: object, value: object):...
class IEventBindingService():
    def CreateUniqueMethodName(self, component: _n_2_t_1, e: _n_2_t_5) -> str:...
    def GetCompatibleMethods(self, e: _n_2_t_5) -> _n_1_t_0:...
    def GetEvent(self, property: _n_2_t_6) -> _n_2_t_5:...
    def GetEventProperties(self, events: _n_2_t_7) -> _n_2_t_2:...
    def GetEventProperty(self, e: _n_2_t_5) -> _n_2_t_6:...
    def ShowCode(self, component: _n_2_t_1, e: _n_2_t_5) -> bool:...
    def ShowCode(self, lineNumber: int) -> bool:...
    def ShowCode(self) -> bool:...
class IExtenderListService():
    def GetExtenderProviders(self) -> _n_0_t_8[_n_2_t_8]:...
class IExtenderProviderService():
    def AddExtenderProvider(self, provider: _n_2_t_8):...
    def RemoveExtenderProvider(self, provider: _n_2_t_8):...
class IHelpService():
    def AddContextAttribute(self, name: str, value: str, keywordType: HelpKeywordType):...
    def ClearContextAttributes(self):...
    def CreateLocalContext(self, contextType: HelpContextType) -> IHelpService:...
    def RemoveContextAttribute(self, name: str, value: str):...
    def RemoveLocalContext(self, localContext: IHelpService):...
    def ShowHelpFromKeyword(self, helpKeyword: str):...
    def ShowHelpFromUrl(self, helpUrl: str):...
class IInheritanceService():
    def AddInheritedComponents(self, component: _n_2_t_1, container: _n_2_t_4):...
    def GetInheritanceAttribute(self, component: _n_2_t_1) -> _n_2_t_9:...
class IMenuCommandService():
    @property
    def Verbs(self) -> DesignerVerbCollection:"""Verbs { get; } -> DesignerVerbCollection"""
    def AddCommand(self, command: MenuCommand):...
    def AddVerb(self, verb: DesignerVerb):...
    def FindCommand(self, commandID: CommandID) -> MenuCommand:...
    def GlobalInvoke(self, commandID: CommandID) -> bool:...
    def RemoveCommand(self, command: MenuCommand):...
    def RemoveVerb(self, verb: DesignerVerb):...
    def ShowContextMenu(self, menuID: CommandID, x: int, y: int):...
class IReferenceService():
    def GetComponent(self, reference: object) -> _n_2_t_1:...
    def GetName(self, reference: object) -> str:...
    def GetReference(self, name: str) -> object:...
    def GetReferences(self, baseType: _n_0_t_17) -> _n_0_t_8[object]:...
    def GetReferences(self) -> _n_0_t_8[object]:...
class IResourceService():
    def GetResourceReader(self, info: _n_3_t_0) -> _n_6_t_0:...
    def GetResourceWriter(self, info: _n_3_t_0) -> _n_6_t_1:...
class IRootDesigner(IDesigner):
    @property
    def SupportedTechnologies(self) -> _n_0_t_8[ViewTechnology]:"""SupportedTechnologies { get; } -> Array"""
    def GetView(self, technology: ViewTechnology) -> object:...
class ISelectionService():
    @property
    def PrimarySelection(self) -> object:"""PrimarySelection { get; } -> object"""
    @property
    def SelectionCount(self) -> int:"""SelectionCount { get; } -> int"""
    @property
    def SelectionChanged(self) -> _n_0_t_10:
        """SelectionChanged Event: EventHandler"""
    @property
    def SelectionChanging(self) -> _n_0_t_10:
        """SelectionChanging Event: EventHandler"""
    def GetComponentSelected(self, component: object) -> bool:...
    def GetSelectedComponents(self) -> _n_1_t_0:...
    def SetSelectedComponents(self, components: _n_1_t_0, selectionType: SelectionTypes):...
    def SetSelectedComponents(self, components: _n_1_t_0):...
class IServiceContainer(_n_0_t_11):
    def AddService(self, serviceType: _n_0_t_17, callback: ServiceCreatorCallback, promote: bool):...
    def AddService(self, serviceType: _n_0_t_17, callback: ServiceCreatorCallback):...
    def AddService(self, serviceType: _n_0_t_17, serviceInstance: object, promote: bool):...
    def AddService(self, serviceType: _n_0_t_17, serviceInstance: object):...
    def RemoveService(self, serviceType: _n_0_t_17, promote: bool):...
    def RemoveService(self, serviceType: _n_0_t_17):...
class ITreeDesigner(IDesigner):
    @property
    def Children(self) -> _n_1_t_0:"""Children { get; } -> ICollection"""
    @property
    def Parent(self) -> IDesigner:"""Parent { get; } -> IDesigner"""
class ITypeDescriptorFilterService():
    def FilterAttributes(self, component: _n_2_t_1, attributes: _n_1_t_3) -> bool:...
    def FilterEvents(self, component: _n_2_t_1, events: _n_1_t_3) -> bool:...
    def FilterProperties(self, component: _n_2_t_1, properties: _n_1_t_3) -> bool:...
class ITypeDiscoveryService():
    def GetTypes(self, baseType: _n_0_t_17, excludeGlobalTypes: bool) -> _n_1_t_0:...
class ITypeResolutionService():
    def GetAssembly(self, name: _n_5_t_1, throwOnError: bool) -> _n_5_t_0:...
    def GetAssembly(self, name: _n_5_t_1) -> _n_5_t_0:...
    def GetPathOfAssembly(self, name: _n_5_t_1) -> str:...
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> _n_0_t_17:...
    def GetType(self, name: str, throwOnError: bool) -> _n_0_t_17:...
    def GetType(self, name: str) -> _n_0_t_17:...
    def ReferenceAssembly(self, name: _n_5_t_1):...
class MenuCommand(object):
    @property
    def Checked(self) -> bool:"""Checked { get; set; } -> bool"""
    @property
    def CommandID(self) -> CommandID:"""CommandID { get; } -> CommandID"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def OleStatus(self) -> int:"""OleStatus { get; } -> int"""
    @property
    def Properties(self) -> _n_1_t_3:"""Properties { get; } -> IDictionary"""
    @property
    def Supported(self) -> bool:"""Supported { get; set; } -> bool"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    @property
    def CommandChanged(self) -> _n_0_t_10:
        """CommandChanged Event: EventHandler"""
    def __init__(self, handler: _n_0_t_10, command: CommandID) -> MenuCommand:...
    def Invoke(self, arg: object):...
    def Invoke(self):...
class SelectionTypes(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    Add: int
    Auto: int
    Click: int
    MouseDown: int
    MouseUp: int
    Normal: int
    Primary: int
    Remove: int
    Replace: int
    Toggle: int
    Valid: int
    value__: int
class ServiceContainer(IServiceContainer, _n_0_t_9):
    def __init__(self, parentProvider: _n_0_t_11) -> ServiceContainer:...
    def __init__(self) -> ServiceContainer:...
class ServiceCreatorCallback(_n_0_t_1, _n_0_t_2, _n_8_t_0):
    def __init__(self, object: object, method: _n_0_t_3) -> ServiceCreatorCallback:...
    def BeginInvoke(self, container: IServiceContainer, serviceType: _n_0_t_17, callback: _n_0_t_5, object: object) -> _n_0_t_4:...
    def EndInvoke(self, result: _n_0_t_4) -> object:...
    def Invoke(self, container: IServiceContainer, serviceType: _n_0_t_17) -> object:...
class StandardCommands(object):
    AlignBottom: int
    AlignHorizontalCenters: int
    AlignLeft: int
    AlignRight: int
    AlignToGrid: int
    AlignTop: int
    AlignVerticalCenters: int
    ArrangeBottom: int
    ArrangeIcons: int
    ArrangeRight: int
    BringForward: int
    BringToFront: int
    CenterHorizontally: int
    CenterVertically: int
    Copy: int
    Cut: int
    Delete: int
    DocumentOutline: int
    F1Help: int
    Group: int
    HorizSpaceConcatenate: int
    HorizSpaceDecrease: int
    HorizSpaceIncrease: int
    HorizSpaceMakeEqual: int
    LineupIcons: int
    LockControls: int
    MultiLevelRedo: int
    MultiLevelUndo: int
    Paste: int
    Properties: int
    PropertiesWindow: int
    Redo: int
    Replace: int
    SelectAll: int
    SendBackward: int
    SendToBack: int
    ShowGrid: int
    ShowLargeIcons: int
    SizeToControl: int
    SizeToControlHeight: int
    SizeToControlWidth: int
    SizeToFit: int
    SizeToGrid: int
    SnapToGrid: int
    TabOrder: int
    Undo: int
    Ungroup: int
    VerbFirst: int
    VerbLast: int
    VertSpaceConcatenate: int
    VertSpaceDecrease: int
    VertSpaceIncrease: int
    VertSpaceMakeEqual: int
    ViewCode: int
    ViewGrid: int
    def __init__(self) -> StandardCommands:...
class StandardToolWindows(object):
    ObjectBrowser: int
    OutputWindow: int
    ProjectExplorer: int
    PropertyBrowser: int
    RelatedLinks: int
    ServerExplorer: int
    TaskList: int
    Toolbox: int
    def __init__(self) -> StandardToolWindows:...
class TypeDescriptionProviderService(object):
    def GetProvider(self, type: _n_0_t_17) -> _n_2_t_10:...
    def GetProvider(self, instance: object) -> _n_2_t_10:...
class ViewTechnology(_n_0_t_12, _n_0_t_13, _n_0_t_14, _n_0_t_15):
    Default: int
    Passthrough: int
    value__: int
    WindowsForms: int
