from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectIdCollection as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Database as _n_0_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import PlotPaperUnit as _n_0_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import PlotRotation as _n_0_t_5
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import PlotType as _n_0_t_6
from __clrclasses__.Autodesk.AutoCAD.PlottingServices import DsdData as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.PlottingServices import PlotLogger as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.PlottingServices import DsdEntry as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.PlottingServices import PlotConfig as _n_1_t_3
from __clrclasses__.Autodesk.AutoCAD.PlottingServices import PlotProgressDialog as _n_1_t_4
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_2_t_0
from __clrclasses__.System import EventArgs as _n_3_t_0
from __clrclasses__.System import MulticastDelegate as _n_3_t_1
from __clrclasses__.System import ICloneable as _n_3_t_2
from __clrclasses__.System import IntPtr as _n_3_t_3
from __clrclasses__.System import IAsyncResult as _n_3_t_4
from __clrclasses__.System import AsyncCallback as _n_3_t_5
from __clrclasses__.System import Array as _n_3_t_6
from __clrclasses__.System import IDisposable as _n_3_t_7
from __clrclasses__.System import ValueType as _n_3_t_8
from __clrclasses__.System import Nullable as _n_3_t_9
from __clrclasses__.System import MarshalByRefObject as _n_3_t_10
from __clrclasses__.System.Collections import IDictionaryEnumerator as _n_4_t_0
from __clrclasses__.System.Collections import ICollection as _n_4_t_1
from __clrclasses__.System.Collections.Specialized import StringCollection as _n_5_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_6_t_0
import typing
class AboutToBeginBackgroundPublishingEventArgs(_n_3_t_0):
    @property
    def DsdData(self) -> _n_1_t_0:"""DsdData { get; } -> DsdData"""
    @property
    def JobWillPublishInBackground(self) -> bool:"""JobWillPublishInBackground { get; } -> bool"""
    def ReadPrivateSection(self, sectionName: str) -> _n_4_t_0:...
    def WritePrivateSection(self, sectionName: str, data: _n_4_t_0):...
class AboutToBeginBackgroundPublishingEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> AboutToBeginBackgroundPublishingEventHandler:...
    def BeginInvoke(self, sender: object, e: AboutToBeginBackgroundPublishingEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: AboutToBeginBackgroundPublishingEventArgs):...
class AboutToBeginPublishingEventArgs(_n_3_t_0):
    @property
    def DsdData(self) -> _n_1_t_0:"""DsdData { get; } -> DsdData"""
    @property
    def JobWillPublishInBackground(self) -> bool:"""JobWillPublishInBackground { get; } -> bool"""
    @property
    def PlotLogger(self) -> _n_1_t_1:"""PlotLogger { get; } -> PlotLogger"""
    def ReadPrivateSection(self, sectionName: str) -> _n_4_t_0:...
    def WritePrivateSection(self, sectionName: str, data: _n_4_t_0):...
class AboutToBeginPublishingEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> AboutToBeginPublishingEventHandler:...
    def BeginInvoke(self, sender: object, e: AboutToBeginPublishingEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: AboutToBeginPublishingEventArgs):...
class AboutToEndPublishingEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> AboutToEndPublishingEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishEventArgs):...
class AboutToMoveFileEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> AboutToMoveFileEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishEventArgs):...
class BeginAggregationEventArgs(_n_3_t_0):
    @property
    def DwfFileName(self) -> str:"""DwfFileName { get; } -> str"""
    @property
    def DwfPassword(self) -> str:"""DwfPassword { get; } -> str"""
    @property
    def PlotLogger(self) -> _n_1_t_1:"""PlotLogger { get; } -> PlotLogger"""
    def AddGlobalPropertyRange(self, properties: _n_3_t_6[EPlotProperty]):...
    def AddGlobalResourceRange(self, resources: _n_3_t_6[EPlotResource]):...
class BeginAggregationEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> BeginAggregationEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginAggregationEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: BeginAggregationEventArgs):...
class BeginEntityEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> BeginEntityEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishEntityEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishEntityEventArgs):...
class BeginPublishingSheetEventArgs(_n_3_t_0):
    @property
    def DsdEntry(self) -> _n_1_t_2:"""DsdEntry { get; } -> DsdEntry"""
    @property
    def PlotLogger(self) -> _n_1_t_1:"""PlotLogger { get; } -> PlotLogger"""
    @property
    def UniqueId(self) -> str:"""UniqueId { get; } -> str"""
class BeginPublishingSheetEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> BeginPublishingSheetEventHandler:...
    def BeginInvoke(self, sender: object, e: BeginPublishingSheetEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: BeginPublishingSheetEventArgs):...
class BeginSheetEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> BeginSheetEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishSheetEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishSheetEventArgs):...
class CancelledOrFailedPublishingEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> CancelledOrFailedPublishingEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishEventArgs):...
class Dwf3dNavigationTreeNode(_n_2_t_0, _n_3_t_7, _n_3_t_2):
    @property
    def Children(self) -> Dwf3dNavigationTreeNodeCollection:"""Children { get; } -> Dwf3dNavigationTreeNodeCollection"""
    @property
    def DisplayName(self) -> str:"""DisplayName { get; set; } -> str"""
    @property
    def IsBlock(self) -> bool:"""IsBlock { get; set; } -> bool"""
    @property
    def IsGroup(self) -> bool:"""IsGroup { get; set; } -> bool"""
    def __init__(self) -> Dwf3dNavigationTreeNode:...
    def __init__(self, displayName: str, isGroup: bool, isBlock: bool) -> Dwf3dNavigationTreeNode:...
    def GetKeys(self) -> _n_3_t_6[int]:...
    def SetKeys(self, keys: _n_3_t_6[int]):...
class Dwf3dNavigationTreeNodeCollection(typing.Iterable[Dwf3dNavigationTreeNode]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def Item(self) -> Dwf3dNavigationTreeNode:"""Item { get; } -> Dwf3dNavigationTreeNode"""
    def Add(self, node: Dwf3dNavigationTreeNode):...
    def Remove(self, node: Dwf3dNavigationTreeNode):...
class DwfNode(object):
    @property
    def NodeId(self) -> int:"""NodeId { get; set; } -> int"""
    @property
    def NodeName(self) -> str:"""NodeName { get; set; } -> str"""
    def __init__(self) -> DwfNode:...
    def __init__(self, nodeId: int, nodeName: str) -> DwfNode:...
class EndEntityEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> EndEntityEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishEntityEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishEntityEventArgs):...
class EndPublishEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> EndPublishEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishEventArgs):...
class EndSheetEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> EndSheetEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishSheetEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishSheetEventArgs):...
class EPlotAttribute(object):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Ns(self) -> str:"""Ns { get; set; } -> str"""
    @property
    def NsUrl(self) -> str:"""NsUrl { get; set; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; set; } -> str"""
    def __init__(self) -> EPlotAttribute:...
    def __init__(self, ns: str, nsUrl: str, name: str, value: str) -> EPlotAttribute:...
class EPlotAttributeCollection(_n_4_t_1, typing.Iterable[EPlotAttribute]):
    @property
    def Item(self) -> EPlotAttribute:"""Item { get; set; } -> EPlotAttribute"""
    def Add(self, value: EPlotAttribute):...
    def Clear(self):...
class EPlotProperty(object):
    @property
    def Attributes(self) -> EPlotAttributeCollection:"""Attributes { get; } -> EPlotAttributeCollection"""
    @property
    def Category(self) -> str:"""Category { get; set; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def Type(self) -> str:"""Type { get; set; } -> str"""
    @property
    def Units(self) -> str:"""Units { get; set; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; set; } -> str"""
    def __init__(self) -> EPlotProperty:...
    def __init__(self, name: str, val: str) -> EPlotProperty:...
    def AddEplotAttribute(self, att: EPlotAttribute):...
    def AddEPlotAttribute(self, ns: str, nsUrl: str, attName: str, attValue: str):...
class EPlotPropertyBag(object):
    @property
    def Id(self) -> str:"""Id { get; set; } -> str"""
    @property
    def NamespaceLocation(self) -> str:"""NamespaceLocation { get; set; } -> str"""
    @property
    def NamespaceUrl(self) -> str:"""NamespaceUrl { get; set; } -> str"""
    @property
    def Properties(self) -> EPlotPropertyCollection:"""Properties { get; } -> EPlotPropertyCollection"""
    @property
    def References(self) -> _n_5_t_0:"""References { get; set; } -> StringCollection"""
    def __init__(self) -> EPlotPropertyBag:...
    def __init__(self, id: str, namespaceUrl: str, namespaceLocation: str) -> EPlotPropertyBag:...
class EPlotPropertyCollection(_n_4_t_1, typing.Iterable[EPlotProperty]):
    @property
    def Item(self) -> EPlotProperty:"""Item { get; set; } -> EPlotProperty"""
    def Add(self, value: EPlotProperty):...
    def Clear(self):...
class EPlotResource(object):
    @property
    def Mime(self) -> str:"""Mime { get; set; } -> str"""
    @property
    def Path(self) -> str:"""Path { get; set; } -> str"""
    @property
    def Role(self) -> str:"""Role { get; set; } -> str"""
    def __init__(self) -> EPlotResource:...
    def __init__(self, role: str, mime: str, path: str) -> EPlotResource:...
class InitPublishOptionsDialogEventHandler(_n_3_t_1, _n_3_t_2, _n_6_t_0):
    def __init__(self, A_0: object, A_1: _n_3_t_3) -> InitPublishOptionsDialogEventHandler:...
    def BeginInvoke(self, sender: object, e: PublishUIEventArgs, callback: _n_3_t_5, obj: object) -> _n_3_t_4:...
    def EndInvoke(self, result: _n_3_t_4):...
    def Invoke(self, sender: object, e: PublishUIEventArgs):...
class OptionsDialogResult(_n_3_t_8):
    @property
    def DsdData(self) -> _n_1_t_0:"""DsdData { get; } -> DsdData"""
    @property
    def PlotConfig(self) -> _n_1_t_3:"""PlotConfig { get; } -> PlotConfig"""
    @property
    def Status(self) -> _n_3_t_9[bool]:"""Status { get; } -> Nullable"""
class PublishEntityEventArgs(_n_3_t_0):
    @property
    def EffectiveBlockLayerId(self) -> _n_0_t_0:"""EffectiveBlockLayerId { get; } -> ObjectId"""
    @property
    def Entity(self) -> _n_0_t_1:"""Entity { get; } -> Entity"""
    @property
    def IsCancelled(self) -> bool:"""IsCancelled { get; } -> bool"""
    @property
    def PlotLogger(self) -> _n_1_t_1:"""PlotLogger { get; } -> PlotLogger"""
    @property
    def UniqueEntityId(self) -> str:"""UniqueEntityId { get; } -> str"""
    def Add3DDwfProperty(self, category: str, name: str, value: str) -> bool:...
    def AddNodeToMap(self, entityId: _n_0_t_0, objIds: _n_0_t_2, nodeId: int) -> bool:...
    def AddPropertiesIds(self, properties: EPlotPropertyBag, node: DwfNode) -> bool:...
    def AddPropertyBag(self, properties: EPlotPropertyBag) -> bool:...
    def Cancel(self):...
    def Flush(self):...
    def GetCurrentEntityNode(self, objIds: _n_0_t_2) -> DwfNode:...
    def getEntityBlockRefPath(self) -> _n_0_t_2:...
    def GetEntityNode(self, entityId: _n_0_t_0, objIds: _n_0_t_2) -> int:...
    def GetGraphicIDs(self) -> _n_3_t_6[int]:...
    def GetNextAvailableNode(self) -> int:...
    def GetNode(self, nodeId: int) -> DwfNode:...
    def SetCurrentNode(self, nodeId: int, objIds: _n_0_t_2) -> bool:...
    def SetNodeName(self, nodeId: int, nodeName: str) -> bool:...
class Publisher(_n_3_t_10):
    @property
    def CurrentPublishedSheetSetPath(self) -> str:"""CurrentPublishedSheetSetPath { get; } -> str"""
    @property
    def AboutToBeginBackgroundPublishing(self) -> AboutToBeginBackgroundPublishingEventHandler:
        """AboutToBeginBackgroundPublishing Event: AboutToBeginBackgroundPublishingEventHandler"""
    @property
    def AboutToBeginPublishing(self) -> AboutToBeginPublishingEventHandler:
        """AboutToBeginPublishing Event: AboutToBeginPublishingEventHandler"""
    @property
    def AboutToEndPublishing(self) -> AboutToEndPublishingEventHandler:
        """AboutToEndPublishing Event: AboutToEndPublishingEventHandler"""
    @property
    def AboutToMoveFile(self) -> AboutToMoveFileEventHandler:
        """AboutToMoveFile Event: AboutToMoveFileEventHandler"""
    @property
    def BeginAggregation(self) -> BeginAggregationEventHandler:
        """BeginAggregation Event: BeginAggregationEventHandler"""
    @property
    def BeginEntity(self) -> BeginEntityEventHandler:
        """BeginEntity Event: BeginEntityEventHandler"""
    @property
    def BeginPublishingSheet(self) -> BeginPublishingSheetEventHandler:
        """BeginPublishingSheet Event: BeginPublishingSheetEventHandler"""
    @property
    def BeginSheet(self) -> BeginSheetEventHandler:
        """BeginSheet Event: BeginSheetEventHandler"""
    @property
    def CancelledOrFailedPublishing(self) -> CancelledOrFailedPublishingEventHandler:
        """CancelledOrFailedPublishing Event: CancelledOrFailedPublishingEventHandler"""
    @property
    def EndEntity(self) -> EndEntityEventHandler:
        """EndEntity Event: EndEntityEventHandler"""
    @property
    def EndPublish(self) -> EndPublishEventHandler:
        """EndPublish Event: EndPublishEventHandler"""
    @property
    def EndSheet(self) -> EndSheetEventHandler:
        """EndSheet Event: EndSheetEventHandler"""
    @property
    def InitPublishOptionsDialog(self) -> InitPublishOptionsDialogEventHandler:
        """InitPublishOptionsDialog Event: InitPublishOptionsDialogEventHandler"""
    def FireAboutToBeginBackgroundPublishing(self, e: AboutToBeginBackgroundPublishingEventArgs):...
    def FireAboutToBeginPublishing(self, e: AboutToBeginPublishingEventArgs):...
    def FireAboutToEndPublishing(self, e: PublishEventArgs):...
    def FireAboutToMoveFile(self, e: PublishEventArgs):...
    def FireBeginAggregation(self, e: BeginAggregationEventArgs):...
    def FireBeginEntity(self, e: PublishEntityEventArgs):...
    def FireBeginPublishingSheet(self, e: BeginPublishingSheetEventArgs):...
    def FireBeginSheet(self, e: PublishSheetEventArgs):...
    def FireCancelledOrFailedPublishing(self, e: PublishEventArgs):...
    def FireEndEntity(self, e: PublishEntityEventArgs):...
    def FireEndPublish(self, e: PublishEventArgs):...
    def FireEndSheet(self, e: PublishSheetEventArgs):...
    def FireInitPublishOptionsDialog(self, e: PublishUIEventArgs):...
    def PublishDsd(self, dsdFile: str, plotProgressDialog: _n_1_t_4) -> int:...
    def PublishExecute(self, dsdData: _n_1_t_0, plotConfig: _n_1_t_3):...
    def PublishSelectedLayouts(self, bOverride: bool):...
    def ShowDwfOptionsDialog(self, dsdData: _n_1_t_0, plotConfig: _n_1_t_3, optionsDialogTitle: str) -> OptionsDialogResult:...
    def ShowPublishDialog(self, dsdData: _n_1_t_0, plotConfig: _n_1_t_3, namePageSetups: _n_5_t_0, namePageSetupPaths: _n_5_t_0, optionsDialogTitle: str, optionsButtonText: str):...
class PublishEventArgs(_n_3_t_0):
    @property
    def DwfFileName(self) -> str:"""DwfFileName { get; } -> str"""
    @property
    def DwfPassword(self) -> str:"""DwfPassword { get; } -> str"""
    @property
    def IsMultiSheetDwf(self) -> bool:"""IsMultiSheetDwf { get; } -> bool"""
    @property
    def TemporaryDwfFileName(self) -> str:"""TemporaryDwfFileName { get; } -> str"""
class PublishSheetEventArgs(_n_3_t_0):
    @property
    def AreLinesHidden(self) -> bool:"""AreLinesHidden { get; } -> bool"""
    @property
    def ArePlottingLineWeights(self) -> bool:"""ArePlottingLineWeights { get; } -> bool"""
    @property
    def AreScalingLineWeights(self) -> bool:"""AreScalingLineWeights { get; } -> bool"""
    @property
    def CanonicalMediaName(self) -> str:"""CanonicalMediaName { get; } -> str"""
    @property
    def Configuration(self) -> str:"""Configuration { get; } -> str"""
    @property
    def Database(self) -> _n_0_t_3:"""Database { get; } -> Database"""
    @property
    def DisplayMaxX(self) -> float:"""DisplayMaxX { get; } -> float"""
    @property
    def DisplayMaxY(self) -> float:"""DisplayMaxY { get; } -> float"""
    @property
    def DisplayMinX(self) -> float:"""DisplayMinX { get; } -> float"""
    @property
    def DisplayMinY(self) -> float:"""DisplayMinY { get; } -> float"""
    @property
    def DrawingScale(self) -> float:"""DrawingScale { get; } -> float"""
    @property
    def Dwf3dNavigationTreeNode(self) -> Dwf3dNavigationTreeNode:"""Dwf3dNavigationTreeNode { get; set; } -> Dwf3dNavigationTreeNode"""
    @property
    def EffectivePlotOffsetX(self) -> float:"""EffectivePlotOffsetX { get; } -> float"""
    @property
    def EffectivePlotOffsetXDevice(self) -> int:"""EffectivePlotOffsetXDevice { get; } -> int"""
    @property
    def EffectivePlotOffsetY(self) -> float:"""EffectivePlotOffsetY { get; } -> float"""
    @property
    def EffectivePlotOffsetYDevice(self) -> int:"""EffectivePlotOffsetYDevice { get; } -> int"""
    @property
    def IsModelLayout(self) -> bool:"""IsModelLayout { get; } -> bool"""
    @property
    def IsPlotJobCancelled(self) -> bool:"""IsPlotJobCancelled { get; } -> bool"""
    @property
    def IsScaleSpecified(self) -> bool:"""IsScaleSpecified { get; } -> bool"""
    @property
    def LayoutBoundsMaxX(self) -> float:"""LayoutBoundsMaxX { get; } -> float"""
    @property
    def LayoutBoundsMaxY(self) -> float:"""LayoutBoundsMaxY { get; } -> float"""
    @property
    def LayoutBoundsMinX(self) -> float:"""LayoutBoundsMinX { get; } -> float"""
    @property
    def LayoutBoundsMinY(self) -> float:"""LayoutBoundsMinY { get; } -> float"""
    @property
    def LayoutMarginMaxX(self) -> float:"""LayoutMarginMaxX { get; } -> float"""
    @property
    def LayoutMarginMaxY(self) -> float:"""LayoutMarginMaxY { get; } -> float"""
    @property
    def LayoutMarginMinX(self) -> float:"""LayoutMarginMinX { get; } -> float"""
    @property
    def LayoutMarginMinY(self) -> float:"""LayoutMarginMinY { get; } -> float"""
    @property
    def MaxBoundsX(self) -> float:"""MaxBoundsX { get; } -> float"""
    @property
    def MaxBoundsY(self) -> float:"""MaxBoundsY { get; } -> float"""
    @property
    def OriginX(self) -> float:"""OriginX { get; } -> float"""
    @property
    def OriginY(self) -> float:"""OriginY { get; } -> float"""
    @property
    def PaperScale(self) -> float:"""PaperScale { get; } -> float"""
    @property
    def PlotBoundsMaxX(self) -> float:"""PlotBoundsMaxX { get; } -> float"""
    @property
    def PlotBoundsMaxY(self) -> float:"""PlotBoundsMaxY { get; } -> float"""
    @property
    def PlotBoundsMinX(self) -> float:"""PlotBoundsMinX { get; } -> float"""
    @property
    def PlotBoundsMinY(self) -> float:"""PlotBoundsMinY { get; } -> float"""
    @property
    def PlotLayoutId(self) -> _n_0_t_0:"""PlotLayoutId { get; } -> ObjectId"""
    @property
    def PlotLogger(self) -> _n_1_t_1:"""PlotLogger { get; } -> PlotLogger"""
    @property
    def PlotPaperUnit(self) -> _n_0_t_4:"""PlotPaperUnit { get; } -> PlotPaperUnit"""
    @property
    def PlotRotation(self) -> _n_0_t_5:"""PlotRotation { get; } -> PlotRotation"""
    @property
    def PlotToFileName(self) -> str:"""PlotToFileName { get; } -> str"""
    @property
    def PlotToFilePath(self) -> str:"""PlotToFilePath { get; } -> str"""
    @property
    def PlotType(self) -> _n_0_t_6:"""PlotType { get; } -> PlotType"""
    @property
    def PlotWindowMaxX(self) -> float:"""PlotWindowMaxX { get; } -> float"""
    @property
    def PlotWindowMaxY(self) -> float:"""PlotWindowMaxY { get; } -> float"""
    @property
    def PlotWindowMinX(self) -> float:"""PlotWindowMinX { get; } -> float"""
    @property
    def PlotWindowMinY(self) -> float:"""PlotWindowMinY { get; } -> float"""
    @property
    def PrintableBoundsX(self) -> float:"""PrintableBoundsX { get; } -> float"""
    @property
    def PrintableBoundsY(self) -> float:"""PrintableBoundsY { get; } -> float"""
    @property
    def PublishingTo3DDwf(self) -> bool:"""PublishingTo3DDwf { get; } -> bool"""
    @property
    def StepsPerInch(self) -> float:"""StepsPerInch { get; } -> float"""
    @property
    def UniqueLayoutId(self) -> str:"""UniqueLayoutId { get; } -> str"""
    @property
    def ViewPlotted(self) -> str:"""ViewPlotted { get; } -> str"""
    def AddPagePropertyRange(self, properties: _n_3_t_6[EPlotProperty]):...
    def AddPageResourceRange(self, resources: _n_3_t_6[EPlotResource]):...
class PublishUIEventArgs(_n_3_t_0):
    @property
    def DsdData(self) -> _n_1_t_0:"""DsdData { get; } -> DsdData"""
    @property
    def IUnknown(self) -> object:"""IUnknown { get; } -> object"""
    @property
    def JobWillPublishInBackground(self) -> bool:"""JobWillPublishInBackground { get; } -> bool"""
    def ReadPrivateSection(self, sectionName: str) -> _n_4_t_0:...
    def WritePrivateSection(self, sectionName: str, data: _n_4_t_0):...
