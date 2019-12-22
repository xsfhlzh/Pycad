from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import FullSubentityPath as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import TypedValue as _n_1_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_1_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectIdCollection as _n_1_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import PointCloudEx as _n_1_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import HostApplicationServices as _n_1_t_5
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import EntityAlignmentEventHandler as _n_1_t_6
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ReservedStringEnumType as _n_1_t_7
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3d as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector3dCollection as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector2d as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.Geometry import Vector2dCollection as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2d as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2dCollection as _n_2_t_5
from __clrclasses__.Autodesk.AutoCAD.Geometry import IntegerCollection as _n_2_t_6
from __clrclasses__.Autodesk.AutoCAD.Geometry import DoubleCollection as _n_2_t_7
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_2_t_8
from __clrclasses__.Autodesk.AutoCAD.Geometry import CircularArc2d as _n_2_t_9
from __clrclasses__.Autodesk.AutoCAD.Geometry import LineSegment2d as _n_2_t_10
from __clrclasses__.Microsoft.Win32 import RegistryKey as _n_3_t_0
from __clrclasses__.Microsoft.Win32 import RegistryKeyPermissionCheck as _n_3_t_1
from __clrclasses__.Microsoft.Win32 import RegistryOptions as _n_3_t_2
from __clrclasses__.Microsoft.Win32 import RegistryHive as _n_3_t_3
from __clrclasses__.Microsoft.Win32 import RegistryValueOptions as _n_3_t_4
from __clrclasses__.Microsoft.Win32 import RegistryValueKind as _n_3_t_5
from __clrclasses__.Microsoft.Win32 import RegistryView as _n_3_t_6
from __clrclasses__.System import Enum as _n_4_t_0
from __clrclasses__.System import IComparable as _n_4_t_1
from __clrclasses__.System import IFormattable as _n_4_t_2
from __clrclasses__.System import IConvertible as _n_4_t_3
from __clrclasses__.System import Attribute as _n_4_t_4
from __clrclasses__.System import Type as _n_4_t_5
from __clrclasses__.System import IDisposable as _n_4_t_6
from __clrclasses__.System import ICloneable as _n_4_t_7
from __clrclasses__.System import MarshalByRefObject as _n_4_t_8
from __clrclasses__.System import IntPtr as _n_4_t_9
from __clrclasses__.System import EventArgs as _n_4_t_10
from __clrclasses__.System import Exception as _n_4_t_11
from __clrclasses__.System import EventHandler as _n_4_t_12
from __clrclasses__.System import Array as _n_4_t_13
from __clrclasses__.System import MulticastDelegate as _n_4_t_14
from __clrclasses__.System import IAsyncResult as _n_4_t_15
from __clrclasses__.System import AsyncCallback as _n_4_t_16
from __clrclasses__.System import Version as _n_4_t_17
from __clrclasses__.System.Collections import IDictionary as _n_5_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_5_t_1
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_6_t_0
from __clrclasses__.System.Collections.Specialized import StringCollection as _n_7_t_0
from __clrclasses__.System.Drawing import Icon as _n_8_t_0
from __clrclasses__.System.Drawing import Bitmap as _n_8_t_1
from __clrclasses__.System.Reflection import Assembly as _n_9_t_0
from __clrclasses__.System.Resources import ResourceManager as _n_10_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_11_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_11_t_1
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_12_t_0
from __clrclasses__.System.Security.AccessControl import RegistrySecurity as _n_13_t_0
from __clrclasses__.System.Security.AccessControl import RegistryRights as _n_13_t_1
from __clrclasses__.System.Threading import SynchronizationContext as _n_14_t_0
import typing
class AngularUnitFormat(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Current: int
    Degrees: int
    DegreesMinutesSeconds: int
    Grads: int
    Radians: int
    Surveyor: int
    value__: int
class CommandClassAttribute(_n_4_t_4, _n_11_t_0):
    @property
    def Type(self) -> _n_4_t_5:"""Type { get; } -> Type"""
    def __init__(self, name: _n_4_t_5) -> CommandClassAttribute:...
class CommandFlags(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    ActionMacro: int
    Defun: int
    DocExclusiveLock: int
    DocReadLock: int
    InProgress: int
    Interruptible: int
    Modal: int
    NoActionRecording: int
    NoBlockEditor: int
    NoHistory: int
    NoInferConstraint: int
    NoInternalLock: int
    NoMultiple: int
    NoNewStack: int
    NoOem: int
    NoPaperSpace: int
    NoPerspective: int
    NoTileMode: int
    NoUndoMarker: int
    Redraw: int
    Session: int
    TempShowDynDimension: int
    Transparent: int
    Undefined: int
    UsePickSet: int
    value__: int
class CommandMethodAttribute(_n_4_t_4, _n_11_t_0, ICommandLineCallable):
    def __init__(self, groupName: str, globalName: str, localizedNameId: str, flags: CommandFlags, contextMenuExtensionType: _n_4_t_5, helpFileName: str, helpTopic: str) -> CommandMethodAttribute:...
    def __init__(self, groupName: str, globalName: str, localizedNameId: str, flags: CommandFlags, helpTopic: str) -> CommandMethodAttribute:...
    def __init__(self, groupName: str, globalName: str, localizedNameId: str, flags: CommandFlags, contextMenuExtensionType: _n_4_t_5) -> CommandMethodAttribute:...
    def __init__(self, groupName: str, globalName: str, localizedNameId: str, flags: CommandFlags) -> CommandMethodAttribute:...
    def __init__(self, groupName: str, globalName: str, flags: CommandFlags) -> CommandMethodAttribute:...
    def __init__(self, globalName: str, flags: CommandFlags) -> CommandMethodAttribute:...
    def __init__(self, globalName: str) -> CommandMethodAttribute:...
class Converter(object):
    @staticmethod
    def AngleToString(value: float) -> str:...
    @staticmethod
    def AngleToString(value: float, units: AngularUnitFormat, precision: int) -> str:...
    @staticmethod
    def DistanceToString(value: float) -> str:...
    @staticmethod
    def DistanceToString(value: float, units: DistanceUnitFormat, precision: int) -> str:...
    @staticmethod
    def RawAngleToString(value: float) -> str:...
    @staticmethod
    def RawAngleToString(value: float, units: AngularUnitFormat, precision: int) -> str:...
    @staticmethod
    def StringToAngle(value: str) -> float:...
    @staticmethod
    def StringToAngle(value: str, units: AngularUnitFormat) -> float:...
    @staticmethod
    def StringToDistance(value: str) -> float:...
    @staticmethod
    def StringToDistance(value: str, units: DistanceUnitFormat) -> float:...
    @staticmethod
    def StringToRawAngle(value: str) -> float:...
    @staticmethod
    def StringToRawAngle(value: str, units: AngularUnitFormat) -> float:...
class Dictionary(RXObject, _n_4_t_6, _n_4_t_7, _n_5_t_0, typing.Iterable[typing.Any]):
    @property
    def DeletesObjects(self) -> bool:"""DeletesObjects { get; } -> bool"""
    @property
    def IsCaseSensitive(self) -> bool:"""IsCaseSensitive { get; } -> bool"""
    @property
    def IsSorted(self) -> bool:"""IsSorted { get; } -> bool"""
    def At(self, id: int) -> RXObject:...
    def At(self, key: str) -> RXObject:...
    def AtKeyAndIdPut(self, newKey: str, id: int, value: RXObject):...
    def AtPut(self, id: int, value: RXObject) -> RXObject:...
    def AtPut(self, key: str, value: RXObject, retId: int) -> RXObject:...
    def AtPut(self, key: str, value: RXObject) -> RXObject:...
    def IdAt(self, key: str) -> int:...
    def KeyAt(self, id: int) -> str:...
    def ResetKey(self, id: int, newKey: str):...
    def ResetKey(self, oldKey: str, newKey: str):...
class DisposableWrapper(_n_4_t_8, _n_4_t_6):
    @property
    def AutoDelete(self) -> bool:"""AutoDelete { get; set; } -> bool"""
    @property
    def IsDisposed(self) -> bool:"""IsDisposed { get; } -> bool"""
    @property
    def UnmanagedObject(self) -> _n_4_t_9:"""UnmanagedObject { get; } -> IntPtr"""
    @staticmethod
    def Create(type: _n_4_t_5, unmanagedPointer: _n_4_t_9, autoDelete: bool) -> DisposableWrapper:...
class DistanceUnitFormat(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Architectural: int
    Current: int
    Decimal: int
    Engineering: int
    Fractional: int
    Scientific: int
    value__: int
class DynamicLinker(RXObject, _n_4_t_6, _n_4_t_7):
    @property
    def ProductLcid(self) -> int:"""ProductLcid { get; } -> int"""
    @property
    def ModuleLoadAborted(self) -> ModuleLoadAbortedEventHandler:
        """ModuleLoadAborted Event: ModuleLoadAbortedEventHandler"""
    @property
    def ModuleLoaded(self) -> ModuleLoadedEventHandler:
        """ModuleLoaded Event: ModuleLoadedEventHandler"""
    @property
    def ModuleLoading(self) -> ModuleLoadingEventHandler:
        """ModuleLoading Event: ModuleLoadingEventHandler"""
    @property
    def ModuleUnloadAborted(self) -> ModuleUnloadAbortedEventHandler:
        """ModuleUnloadAborted Event: ModuleUnloadAbortedEventHandler"""
    @property
    def ModuleUnloaded(self) -> ModuleUnloadedEventHandler:
        """ModuleUnloaded Event: ModuleUnloadedEventHandler"""
    @property
    def ModuleUnloading(self) -> ModuleUnloadingEventHandler:
        """ModuleUnloading Event: ModuleUnloadingEventHandler"""
    def GetLoadedModules(self) -> _n_7_t_0:...
    def IsAppBusy(self, moduleName: str) -> bool:...
    def IsApplicationLocked(self, moduleName: str) -> bool:...
    def IsAppMdiAware(self, moduleName: str) -> bool:...
    def IsModuleLoaded(self, fileName: str) -> bool:...
    def LoadApp(self, appName: str, printIt: bool, asCmd: bool):...
    def LoadModule(self, fileName: str, printIt: bool, asCmd: bool):...
    def SetAppBusy(self, moduleName: str, busyFlag: bool):...
    def UnloadApp(self, appName: str, asCmd: bool):...
    def UnloadModule(self, fileName: str, asCmd: bool):...
class DynamicLinkerEventArgs(_n_4_t_10):
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    def __init__(self, fileName: str) -> DynamicLinkerEventArgs:...
class ErrorStatus(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    AlreadyActive: int
    AlreadyInactive: int
    AlreadyInDB: int
    AlreadyInGroup: int
    AmbiguousInput: int
    AmbiguousOutput: int
    AnonymousEntry: int
    AtMaxReaders: int
    BackgroundPlotInProgress: int
    BadColor: int
    BadColorIndex: int
    BadDwgHeader: int
    BadDxfFile: int
    BadDxfSequence: int
    BadLayerName: int
    BadLinetypeName: int
    BadLinetypeScale: int
    BadLineWeightValue: int
    BadlyNestedAppData: int
    BadPaperspaceView: int
    BadPlotStyleName: int
    BadPlotStyleNameHandle: int
    BadPlotStyleType: int
    BadUcs: int
    BadVisibilityValue: int
    BinaryDataSizeExceeded: int
    BlockDefInEntitySection: int
    BrokenHandle: int
    BufferTooSmall: int
    CannotBeErasedByCaller: int
    CannotBeResurrected: int
    CannotChangeActiveViewport: int
    CannotChangeColumnType: int
    CannotExplodeEntity: int
    CannotNestBlockDefinitions: int
    CannotPlotToFile: int
    CannotRestoreFromAcisFile: int
    CannotScaleNonUniformly: int
    CantOpenFile: int
    CloseFailObjectDamaged: int
    CloseModifyAborted: int
    ClosePartialFailure: int
    CloseWasNotifying: int
    CommandWasInProgress: int
    ContainerNotEmpty: int
    CopyDoesNotExist: int
    CopyFailed: int
    CopyInvalidName: int
    CopyIsModelSpace: int
    CopyNameExists: int
    CreateFailed: int
    CreateInvalidName: int
    CustomSizeNotPossible: int
    DatabaseObjectsOpen: int
    DataLinkAdapterNotFound: int
    DataLinkBadConnectionString: int
    DataLinkConnectionFailed: int
    DataLinkInvalidAdapterId: int
    DataLinkNotFound: int
    DataLinkNotUpdatedYet: int
    DataLinkOtherError: int
    DataLinkSourceIsWriteProtected: int
    DataLinkSourceNotFound: int
    DegenerateGeometry: int
    DelDoesNotExist: int
    DeletedEntry: int
    DeleteEntity: int
    DelIsModelSpace: int
    DelLastLayout: int
    DelUnableToFind: int
    DelUnableToSetCurrent: int
    DeviceNotFound: int
    DocumentSwitchDisabled: int
    DuplicateBlockDefinition: int
    DuplicateBlockName: int
    DuplicateDxfField: int
    DuplicateIndex: int
    DuplicateKey: int
    DuplicateLayerName: int
    DuplicateRecordName: int
    DwgCrcDoesNotMatch: int
    DwgNeedsAFullSave: int
    DwgNeedsRecovery: int
    DwgNotRecoverable: int
    DwgObjectImproperlyRead: int
    DwgRecoveredOK: int
    DwgSentinelDoesNotMatch: int
    DwgShareDemandLoad: int
    DwgShareReadAccess: int
    DwgShareWriteAccess: int
    DwkLockFileFound: int
    DxbPartiallyRead: int
    DxbReadAborted: int
    DxfPartiallyRead: int
    DxfReadAborted: int
    EndOfFile: int
    EndOfObject: int
    EntityInInactiveLayout: int
    ExcessiveItemCount: int
    ExplodeBeforeTransform: int
    ExternalDataSizeExceeded: int
    FileAccessErr: int
    FileExists: int
    FileInternalErr: int
    FileLockedByAutoCAD: int
    FileMissingSections: int
    FileNotFound: int
    FilerError: int
    FileSharingViolation: int
    FileSystemErr: int
    FileTooManyOpen: int
    FiniteStateMachineError: int
    FixedAllErrors: int
    GeneralModelingFailure: int
    GraphicsNotGenerated: int
    GuidNoAddress: int
    HadMultipleReaders: int
    HandleExists: int
    HandleInUse: int
    HatchTooDense: int
    IgnoredLinetypeRedefinition: int
    IllegalEntityType: int
    IllegalReplacement: int
    IncompatiblePlotSettings: int
    IncompleteBlockDefinition: int
    IncompleteComplexObject: int
    InProcessOfCommitting: int
    InsertAfter: int
    InternetBadPath: int
    InternetBase: int
    InternetCreateInternetSessionFailed: int
    InternetDirectoryFull: int
    InternetDiskFull: int
    InternetFileAccessDenied: int
    InternetFileGenericError: int
    InternetFileNotFound: int
    InternetFileOpenFailed: int
    InternetGenericException: int
    InternetHardwareError: int
    InternetHttpAccessDenied: int
    InternetHttpBadGateway: int
    InternetHttpBadMethod: int
    InternetHttpBadRequest: int
    InternetHttpConflict: int
    InternetHttpGatewayTimeout: int
    InternetHttpLengthRequired: int
    InternetHttpNoAcceptableResponse: int
    InternetHttpNotSupported: int
    InternetHttpObjectNotFound: int
    InternetHttpOpenRequestFailed: int
    InternetHttpPaymentRequired: int
    InternetHttpPreconditionFailure: int
    InternetHttpProxyAuthorizationRequired: int
    InternetHttpRequestForbidden: int
    InternetHttpRequestTooLarge: int
    InternetHttpResourceGone: int
    InternetHttpServerError: int
    InternetHttpServiceUnavailable: int
    InternetHttpTimedOut: int
    InternetHttpUnsupportedMedia: int
    InternetHttpUriTooLong: int
    InternetHttpVersionNotSupported: int
    InternetInCache: int
    InternetInternetError: int
    InternetInternetSessionConnectFailed: int
    InternetInternetSessionOpenFailed: int
    InternetInvalidAccessType: int
    InternetInvalidFileHandle: int
    InternetNoInternetSupport: int
    InternetNotAnUrl: int
    InternetNotImplemented: int
    InternetNoWinInternet: int
    InternetOK: int
    InternetOldWinInternet: int
    InternetProtocolNotSupported: int
    InternetSharingViolation: int
    InternetTooManyOpenFiles: int
    InternetUnknownError: int
    InternetUserCancelledTransfer: int
    InternetValidUrl: int
    InvalidAdsName: int
    InvalidAxis: int
    InvalidBlockName: int
    InvalidContext: int
    InvalidDimStyle: int
    InvalidDwgVersion: int
    InvalidDxf2dPoint: int
    InvalidDxf3dPoint: int
    InvalidDxfCode: int
    InvalidDxfSectionName: int
    InvalidEngineState: int
    InvalidExtents: int
    InvalidFaceVertexIndex: int
    InvalidFileExtension: int
    InvalidFix: int
    InvalidIdMap: int
    InvalidIndex: int
    InvalidInput: int
    InvalidInterfaceId: int
    InvalidKey: int
    InvalidLayer: int
    InvalidMeshVertexIndex: int
    InvalidNormal: int
    InvalidObjectId: int
    InvalidOffset: int
    InvalidOpenState: int
    InvalidOwnerObject: int
    InvalidPlotArea: int
    InvalidPlotInfo: int
    InvalidProfileName: int
    InvalidResultBuffer: int
    InvalidStyle: int
    InvalidSymbolTableName: int
    InvalidSymTableFlag: int
    InvalidTextStyle: int
    InvalidView: int
    InvalidWindowArea: int
    InvalidXrefObjectId: int
    IsAnEntity: int
    IsReading: int
    IsWriteProtected: int
    IsWriting: int
    IsXRefObject: int
    IteratorDone: int
    KeyNotFound: int
    LayerGroupCodeMissing: int
    LayoutNotCurrent: int
    LeftErrorsUnfixed: int
    LispActive: int
    LoadFailed: int
    LockChangeInProgress: int
    LockConflict: int
    LockViolation: int
    LongTransReferenceError: int
    MakeMeProxy: int
    MakeMeProxyAndResurrect: int
    MaxLayouts: int
    MissingBlockName: int
    MissingDxfField: int
    MissingDxfSection: int
    MissingSymbolTable: int
    MissingSymbolTableRecord: int
    MustBe0to2: int
    MustBe0to3: int
    MustBe0to4: int
    MustBe0to5: int
    MustBe0to8: int
    MustBe1to15: int
    MustBe1to6: int
    MustBe1to8: int
    MustBeNonNegative: int
    MustBeNonZero: int
    MustBePositive: int
    MustFirstAddBlockToDB: int
    MustOpenThruOwner: int
    MustPlotToFile: int
    NegativeValueNotAllowed: int
    NlsFileNotAvailable: int
    NoActiveTransactions: int
    NoBlockBegin: int
    NoClassId: int
    NoCurrentConfig: int
    NoDatabase: int
    NoDocument: int
    NoErrorHandler: int
    NoFileName: int
    NoInputFiler: int
    NoInternalSpace: int
    NoLabelBlock: int
    NoLayout: int
    NoMatchingMedia: int
    NonCoplanarGeometry: int
    NonePlotDevice: int
    NonPlanarEntity: int
    NoPlotStyleTranslationTable: int
    NotAllowedForThisProxy: int
    NotAnEntity: int
    NotApplicable: int
    NotCurrentDatabase: int
    NotDxfHeaderGroupCode: int
    NotFromThisDocument: int
    NotHandled: int
    NoThumbnailBitmap: int
    NotImplementedYet: int
    NotInBlock: int
    NotInDatabase: int
    NotInGroup: int
    NotInitializedYet: int
    NotInPaperspace: int
    NotMultiPageCapable: int
    NotNewlyCreated: int
    NotOpenForRead: int
    NotOpenForWrite: int
    NotSupportedInDwgApi: int
    NotThatKindOfClass: int
    NotTopTransaction: int
    NoViewAssociation: int
    NoWorkSet: int
    NullBlockName: int
    NullEntityPointer: int
    NullExtents: int
    NullHandle: int
    NullIterator: int
    NullObjectId: int
    NullObjectPointer: int
    NullPtr: int
    NumberOfCopiesNotSupported: int
    ObjectIsReferenced: int
    ObjectToBeDeleted: int
    ObsoleteFileFormat: int
    OK: int
    OnLockedLayer: int
    OpenFileCancelled: int
    OtherObjectsBusy: int
    OutOfDisk: int
    OutOfMemory: int
    OutOfPagerMemory: int
    OutOfRange: int
    OwnerNotInDatabase: int
    OwnerNotOpenForRead: int
    OwnerNotOpenForWrite: int
    OwnerNotSet: int
    PageCancelled: int
    PagerError: int
    PagerWriteError: int
    PermanentlyErased: int
    PlotAlreadyStarted: int
    PlotCancelled: int
    PlotStyleInColorDependentMode: int
    PointNotOnEntity: int
    PolyWidthLost: int
    ProfileDoesNotExist: int
    ProfileIsInUse: int
    ProperClassSeparatorExpected: int
    RecordNotInTable: int
    RegisteredApplicationIdNotFound: int
    RegistryAccessError: int
    RegistryCreateError: int
    RenameDoesNotExist: int
    RenameInvalidLayoutName: int
    RenameInvalidName: int
    RenameIsModelSpace: int
    RenameLayoutAlreadyExists: int
    RepeatedDwgRead: int
    RepeatEntity: int
    RowsMustMatchColumns: int
    SecErrorCipherNotSupported: int
    SecErrorComputingSignature: int
    SecErrorDecryptingData: int
    SecErrorEncryptingData: int
    SecErrorGeneratingTimestamp: int
    SecErrorReadingFile: int
    SecErrorWritingFile: int
    SecErrorWritingSignature: int
    SecInitializationFailure: int
    SecInvalidDigitalId: int
    SelfReference: int
    SetFailed: int
    SingularPoint: int
    SomeInputDataLeftUnread: int
    StringTooLong: int
    SubentitiesStillOpen: int
    SubSelectionSetEmpty: int
    TargetDocNotQuiescent: int
    TooFewLineTypeElements: int
    TooFewVertices: int
    TooManyLineTypeElements: int
    TooManyVertices: int
    TransactionOpenWhileCommandEnded: int
    UnableToGetLabelBlock: int
    UnableToGetViewAssociation: int
    UnableToRemoveAssociation: int
    UnableToSetLabelBlock: int
    UnableToSetViewAssociation: int
    UnableToSyncModelView: int
    UndefinedDxfGroupCode: int
    UndefinedLineType: int
    UndefineShapeName: int
    UndoNoGroupBegin: int
    UndoOperationNotAvailable: int
    UnknownDxfFileFormat: int
    UnknownHandle: int
    UnrecoverableErrors: int
    UnsupportedFileFormat: int
    UserBreak: int
    value__: int
    VertexAfterFace: int
    Vetoed: int
    WasErased: int
    WasNotErased: int
    WasNotForwarding: int
    WasNotifying: int
    WasNotOpenForWrite: int
    WasOpenForNotify: int
    WasOpenForRead: int
    WasOpenForUndo: int
    WasOpenForWrite: int
    WrongCellType: int
    WrongDatabase: int
    WrongObjectType: int
    WrongSubentityType: int
    XRefDependent: int
class Exception(_n_4_t_11, _n_12_t_0, _n_11_t_1):
    @property
    def ErrorStatus(self) -> ErrorStatus:"""ErrorStatus { get; set; } -> ErrorStatus"""
    def __init__(self, es: ErrorStatus, message: str, innerException: _n_4_t_11) -> Exception:...
    def __init__(self, es: ErrorStatus, message: str) -> Exception:...
    def __init__(self, es: ErrorStatus) -> Exception:...
    def __init__(self) -> Exception:...
class ExceptionFilter(object):
    def Invoke(self):...
class ExtensionApplicationAttribute(_n_4_t_4, _n_11_t_0):
    @property
    def Type(self) -> _n_4_t_5:"""Type { get; } -> Type"""
    def __init__(self, entryPointType: _n_4_t_5) -> ExtensionApplicationAttribute:...
class ExtensionLoader(_n_4_t_8):
    @staticmethod
    def IsLoaded(fileName: str) -> bool:...
    @staticmethod
    def Load(fileName: str) -> _n_9_t_0:...
class ExtractionType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    AllLine: int
    OutLine: int
    value__: int
class ExtractOption(object):
    ExtractType: int
    FillGap: int
    MiniumSegmentLength: int
    ProcessPoints: int
    SnapAngle: int
    UseLineSegmentOnly: int
    def __init__(self) -> ExtractOption:...
class Factory(object):
    def __init__(self) -> Factory:...
    @staticmethod
    def Create(type: _n_4_t_5) -> object:...
class FileExistsConditionAttribute(_n_4_t_4, _n_11_t_0, ICondition):
    def __init__(self, fileName: str) -> FileExistsConditionAttribute:...
class ICommandLineCallable():
    @property
    def ContextMenuExtensionType(self) -> _n_4_t_5:"""ContextMenuExtensionType { get; } -> Type"""
    @property
    def Flags(self) -> CommandFlags:"""Flags { get; } -> CommandFlags"""
    @property
    def GlobalName(self) -> str:"""GlobalName { get; } -> str"""
    @property
    def GroupName(self) -> str:"""GroupName { get; } -> str"""
    @property
    def HelpFileName(self) -> str:"""HelpFileName { get; } -> str"""
    @property
    def HelpTopic(self) -> str:"""HelpTopic { get; } -> str"""
    @property
    def LocalizedNameId(self) -> str:"""LocalizedNameId { get; } -> str"""
class ICondition():
    def Evaluate(self) -> bool:...
class IExtensionApplication():
    def Initialize(self):...
    def Terminate(self):...
class IJavaScriptCallable():
    @property
    def EntryPoint(self) -> str:"""EntryPoint { get; } -> str"""
class IMenuItem():
    @property
    def Checked(self) -> bool:"""Checked { get; set; } -> bool"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def Icon(self) -> _n_8_t_0:"""Icon { get; set; } -> Icon"""
    @property
    def Items(self) -> _n_6_t_0[IMenuItem]:"""Items { get; } -> IEnumerable"""
    @property
    def Text(self) -> str:"""Text { get; set; } -> str"""
    @property
    def Visible(self) -> bool:"""Visible { get; set; } -> bool"""
    @property
    def Click(self) -> _n_4_t_12:
        """Click Event: EventHandler"""
    def OnClicked(self, eventArgs: _n_4_t_10):...
class Interop(object):
    @staticmethod
    def AttachUnmanagedObject(obj: DisposableWrapper, unmanagedPointer: _n_4_t_9, autoDelete: bool):...
    @staticmethod
    def Check(returnValue: int):...
    @staticmethod
    def CheckAds(returnValue: int):...
    @staticmethod
    def CheckAdsForCancel(returnValue: int) -> bool:...
    @staticmethod
    def CheckBool(returnValue: bool):...
    @staticmethod
    def CheckBoolean(returnValue: int):...
    @staticmethod
    def CheckNull(returnValue: _n_4_t_9):...
    @staticmethod
    def DetachUnmanagedObject(obj: DisposableWrapper):...
    @staticmethod
    def SetAutoDelete(obj: DisposableWrapper, value: bool):...
    @staticmethod
    def ThrowExceptionForErrorStatus(errorStatus: int):...
class IPointCloudExtractionProgressCallback():
    def Cancel(self):...
    def Cancelled(self) -> bool:...
    def End(self):...
    def UpdateCaption(self, caption: str):...
    def UpdateProgress(self, progress: int):...
    def UpdateRemainTime(self, remainTime: float):...
class JavaScriptCallbackAttribute(_n_4_t_4, _n_11_t_0, IJavaScriptCallable):
    def __init__(self, entryPoint: str) -> JavaScriptCallbackAttribute:...
class JavaScriptClassAttribute(_n_4_t_4, _n_11_t_0):
    @property
    def Type(self) -> _n_4_t_5:"""Type { get; } -> Type"""
    def __init__(self, name: _n_4_t_5) -> JavaScriptClassAttribute:...
class LenientResourceManager(_n_10_t_0):
    def __init__(self, t: _n_4_t_5) -> LenientResourceManager:...
class LispDataType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Angle: int
    DottedPair: int
    Double: int
    Int16: int
    Int32: int
    ListBegin: int
    ListEnd: int
    Nil: int
    _None: int
    ObjectId: int
    Orientation: int
    Point2d: int
    Point3d: int
    SelectionSet: int
    T_atom: int
    Text: int
    value__: int
    Void: int
class LispFunctionAttribute(_n_4_t_4, _n_11_t_0, ICommandLineCallable):
    def __init__(self, globalName: str) -> LispFunctionAttribute:...
    def __init__(self, globalName: str, localizedNameId: str) -> LispFunctionAttribute:...
    def __init__(self, globalName: str, localizedNameId: str, helpFileName: str, helpTopic: str) -> LispFunctionAttribute:...
    def __init__(self, globalName: str, localizedNameId: str, helpTopic: str) -> LispFunctionAttribute:...
class ManagedHost(object):
    def __init__(self) -> ManagedHost:...
    def Entry(self):...
class Marshaler(object):
    @staticmethod
    def AcValueToObject(acValueObj: _n_4_t_9) -> object:...
    @staticmethod
    def BitmapInfoToBitmap(bitmapInfo: _n_4_t_9) -> _n_8_t_1:...
    @staticmethod
    def BitmapToBitmapInfo(bitmap: _n_8_t_1) -> _n_4_t_9:...
    @staticmethod
    def CopyToManagedFullSubentityPath(path: _n_4_t_9) -> _n_1_t_0:...
    @staticmethod
    def CopyToUnmanagedFullSubentityPath(path: _n_1_t_0, newPath: _n_4_t_9):...
    @staticmethod
    def GetInternalArray(col: _n_2_t_1) -> _n_4_t_13[_n_2_t_0]:...
    @staticmethod
    def GetInternalArray(col: _n_2_t_3) -> _n_4_t_13[_n_2_t_2]:...
    @staticmethod
    def GetInternalArray(col: _n_2_t_5) -> _n_4_t_13[_n_2_t_4]:...
    @staticmethod
    def GetInternalArray(col: _n_2_t_6) -> _n_4_t_13[int]:...
    @staticmethod
    def GetInternalArray(col: _n_2_t_7) -> _n_4_t_13[float]:...
    @staticmethod
    def ObjectsToResbuf(objects: _n_4_t_13[object]) -> _n_4_t_9:...
    @staticmethod
    def ObjectToAcValue(obj: object, acValueObj: _n_4_t_9):...
    @staticmethod
    def ObjectToResbuf(o: object) -> _n_4_t_9:...
    @staticmethod
    def ObjectToResbuf(o: object, rb: _n_4_t_9):...
    @staticmethod
    def ResbufToObject(rb: _n_4_t_9) -> object:...
    @staticmethod
    def ResbufToTypedValues(resbuf: _n_4_t_9) -> _n_4_t_13[_n_1_t_1]:...
    @staticmethod
    def SetInternalArray(col: _n_2_t_1, newArray: _n_4_t_13[_n_2_t_0], count: int):...
    @staticmethod
    def SetInternalArray(col: _n_2_t_3, newArray: _n_4_t_13[_n_2_t_2], count: int):...
    @staticmethod
    def SetInternalArray(col: _n_2_t_5, newArray: _n_4_t_13[_n_2_t_4], count: int):...
    @staticmethod
    def SetInternalArray(col: _n_2_t_6, newArray: _n_4_t_13[int], count: int):...
    @staticmethod
    def SetInternalArray(col: _n_2_t_7, newArray: _n_4_t_13[float], count: int):...
    @staticmethod
    def TypedValuesToResbuf(values: _n_4_t_13[_n_1_t_1]) -> _n_4_t_9:...
class ModuleLoadAbortedEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ModuleLoadAbortedEventHandler:...
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs):...
class ModuleLoadedEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ModuleLoadedEventHandler:...
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs):...
class ModuleLoadingEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ModuleLoadingEventHandler:...
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs):...
class ModuleUnloadAbortedEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ModuleUnloadAbortedEventHandler:...
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs):...
class ModuleUnloadedEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ModuleUnloadedEventHandler:...
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs):...
class ModuleUnloadingEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ModuleUnloadingEventHandler:...
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs):...
class Overrule(RXObject, _n_4_t_6, _n_4_t_7):
    @property
    def Overruling(self) -> bool:"""Overruling { get; set; } -> bool"""
    @staticmethod
    def AddOverrule(targetClass: RXClass, overrule: Overrule, bAtLast: bool):...
    @staticmethod
    def HasOverrule(overruledSubject: RXObject, targetClass: RXClass) -> bool:...
    def IsApplicable(self, overruledSubject: RXObject) -> bool:...
    @staticmethod
    def RemoveOverrule(targetClass: RXClass, overrule: Overrule):...
    def SetCustomFilter(self):...
    def SetExtensionDictionaryEntryFilter(self, entryName: str):...
    def SetIdFilter(self, ids: _n_4_t_13[_n_1_t_2]):...
    def SetNoFilter(self):...
    def SetXDataFilter(self, registeredApplicationName: str):...
class PerDocumentClassAttribute(_n_4_t_4, _n_11_t_0):
    @property
    def Type(self) -> _n_4_t_5:"""Type { get; } -> Type"""
    def __init__(self, name: _n_4_t_5) -> PerDocumentClassAttribute:...
class PointCloudExtractor(DisposableWrapper, _n_4_t_6):
    def __init__(self) -> PointCloudExtractor:...
    @staticmethod
    def AppendLineProfile(profile: PointCloudExtractResult, spaceId: _n_1_t_2, layer: str, color: _n_0_t_0) -> _n_1_t_3:...
    @staticmethod
    def AppendPolylineProfile(profile: PointCloudExtractResult, spaceId: _n_1_t_2, layer: str, color: _n_0_t_0, polylineWidth: float) -> _n_1_t_3:...
    @staticmethod
    def Extract(pointCloud: _n_1_t_4, planZDirection: _n_2_t_0, planXDirection: _n_2_t_0, pointOnPlan: _n_2_t_8, extractOption: ExtractOption, progress: IPointCloudExtractionProgressCallback) -> PointCloudExtractResult:...
class PointCloudExtractResult(object):
    Curves: int
    transform: int
    def __init__(self) -> PointCloudExtractResult:...
class ProfileCurve2d(DisposableWrapper, _n_4_t_6):
    @property
    def Arc(self) -> _n_2_t_9:"""Arc { get; set; } -> CircularArc2d"""
    @property
    def IsArc(self) -> bool:"""IsArc { get; } -> bool"""
    @property
    def IsSegment(self) -> bool:"""IsSegment { get; } -> bool"""
    @property
    def LineSeg(self) -> _n_2_t_10:"""LineSeg { get; set; } -> LineSegment2d"""
    def __init__(self, arc: _n_2_t_9) -> ProfileCurve2d:...
    def __init__(self, seg: _n_2_t_10) -> ProfileCurve2d:...
    def __init__(self) -> ProfileCurve2d:...
class ProfileCurveType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
    Arc: int
    LineSeg: int
    value__: int
class ProgressMeter(DisposableWrapper, _n_4_t_6):
    def __init__(self) -> ProgressMeter:...
    def MeterProgress(self):...
    def SetLimit(self, max: int):...
    def Start(self):...
    def Start(self, displayString: str):...
    def Stop(self):...
class Registry(object):
    @property
    def ClassesRoot(self) -> RegistryKey:"""ClassesRoot { get; } -> RegistryKey"""
    @property
    def CurrentConfig(self) -> RegistryKey:"""CurrentConfig { get; } -> RegistryKey"""
    @property
    def CurrentUser(self) -> RegistryKey:"""CurrentUser { get; } -> RegistryKey"""
    @property
    def LocalMachine(self) -> RegistryKey:"""LocalMachine { get; } -> RegistryKey"""
class RegistryKey(_n_4_t_6):
    @property
    def SubKeyCount(self) -> int:"""SubKeyCount { get; } -> int"""
    @property
    def ValueCount(self) -> int:"""ValueCount { get; } -> int"""
    def __init__(self, hKey: _n_3_t_0) -> RegistryKey:...
    def Close(self):...
    def CreateSubKey(self, subkey: str, permissionCheck: _n_3_t_1, registryOptions: _n_3_t_2, registrySecurity: _n_13_t_0) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, permissionCheck: _n_3_t_1, registrySecurity: _n_13_t_0) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, permissionCheck: _n_3_t_1, options: _n_3_t_2) -> RegistryKey:...
    def CreateSubKey(self, subkey: str, permissionCheck: _n_3_t_1) -> RegistryKey:...
    def CreateSubKey(self, subkey: str) -> RegistryKey:...
    def DeleteSubKey(self, subkey: str):...
    def DeleteSubKeyTree(self, subkey: str):...
    def DeleteValue(self, name: str):...
    @staticmethod
    def GetBaseKey(hKey: _n_3_t_3) -> RegistryKey:...
    def GetSubKeyNames(self) -> _n_4_t_13[str]:...
    def GetValue(self, name: str, defaultValue: object, options: _n_3_t_4) -> object:...
    def GetValue(self, name: str, defaultValue: object) -> object:...
    def GetValue(self, name: str) -> object:...
    def GetValueKind(self, name: str) -> _n_3_t_5:...
    def GetValueNames(self) -> _n_4_t_13[str]:...
    @staticmethod
    def OpenBaseKey(hKey: _n_3_t_3, view: _n_3_t_6) -> RegistryKey:...
    def OpenSubKey(self, name: str, permissionCheck: _n_3_t_1, rights: _n_13_t_1) -> RegistryKey:...
    def OpenSubKey(self, name: str, writable: bool) -> RegistryKey:...
    def OpenSubKey(self, name: str, permissionCheck: _n_3_t_1) -> RegistryKey:...
    def OpenSubKey(self, name: str) -> RegistryKey:...
    def SetValue(self, name: str, value: object, kind: _n_3_t_5):...
    def SetValue(self, name: str, value: object):...
class RuntimeSystem(object):
    @staticmethod
    def Initialize(hostServices: _n_1_t_5, localId: int):...
    @staticmethod
    def Terminate():...
class RXClass(RXObject, _n_4_t_6, _n_4_t_7):
    @property
    def AppName(self) -> str:"""AppName { get; } -> str"""
    @property
    def ClassVersion(self) -> _n_4_t_17:"""ClassVersion { get; } -> Version"""
    @property
    def DxfName(self) -> str:"""DxfName { get; } -> str"""
    @property
    def MyParent(self) -> RXClass:"""MyParent { get; } -> RXClass"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def ProxyFlags(self) -> int:"""ProxyFlags { get; } -> int"""
    @property
    def EntityAlignment(self) -> _n_1_t_6:
        """EntityAlignment Event: EntityAlignmentEventHandler"""
    def AddX(self, runtimeClass: RXClass, protocolExtension: RXObject) -> _n_4_t_9:...
    def DelX(self, runtimeClass: RXClass) -> _n_4_t_9:...
    def GetRuntimeType(self) -> _n_4_t_5:...
    def GetX(self, runtimeClass: RXClass) -> _n_4_t_9:...
    def IsDerivedFrom(self, runtimeClass: RXClass) -> bool:...
class RXObject(DisposableWrapper, _n_4_t_6, _n_4_t_7):
    def CompareTo(self, obj: object) -> int:...
    def CopyFrom(self, source: RXObject):...
    @staticmethod
    def GetClass(type: _n_4_t_5) -> RXClass:...
    def GetRXClass(self) -> RXClass:...
    def QueryX(self, protocolClass: RXClass) -> _n_4_t_9:...
    def X(self, protocolClass: RXClass) -> _n_4_t_9:...
class SecuredApplicationAttribute(_n_4_t_4, _n_11_t_0):
    @property
    def ClientPublicKey(self) -> str:"""ClientPublicKey { get; } -> str"""
    @property
    def ClientSignature(self) -> str:"""ClientSignature { get; } -> str"""
    @property
    def License(self) -> str:"""License { get; } -> str"""
    @property
    def OurSignature(self) -> str:"""OurSignature { get; } -> str"""
    def __init__(self, license: str, ourSignature: str, clientSignature: str, clientPublicKey: str) -> SecuredApplicationAttribute:...
class ShowExceptionDialogHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> ShowExceptionDialogHandler:...
    def BeginInvoke(self, e: _n_4_t_11, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, e: _n_4_t_11):...
class SynchronizationContext(_n_14_t_0):
    def __init__(self) -> SynchronizationContext:...
class SystemObjects(object):
    @property
    def ClassDictionary(self) -> Dictionary:"""ClassDictionary { get; } -> Dictionary"""
    @property
    def DynamicLinker(self) -> DynamicLinker:"""DynamicLinker { get; } -> DynamicLinker"""
    @property
    def ServiceDictionary(self) -> Dictionary:"""ServiceDictionary { get; } -> Dictionary"""
    @property
    def Variables(self) -> Variables:"""Variables { get; } -> Variables"""
class SystemVariableEnumerator(DisposableWrapper, _n_4_t_6, _n_5_t_1):
    def __init__(self) -> SystemVariableEnumerator:...
class UnhandledExceptionFilter(object):
    @staticmethod
    def CerOrShowExceptionDialog(e: _n_4_t_11):...
class Utilities(object):
    def __init__(self) -> Utilities:...
    @staticmethod
    def GetErrorStatus(eStatus: ErrorStatus) -> str:...
    @staticmethod
    def GetReservedString(reservedType: _n_1_t_7, bGetLocalized: bool) -> str:...
    @staticmethod
    def RegRedirectEnumKeys(subPath: str, handler: object) -> bool:...
    @staticmethod
    def RegRedirectOpenKey(subPath: str, writable: bool) -> _n_3_t_0:...
    @staticmethod
    def TranslateReservedString(pGlobalName: str) -> str:...
class Variable(DisposableWrapper, _n_4_t_6):
    @property
    def IsLocked(self) -> bool:"""IsLocked { get; } -> bool"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; set; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def PrimaryType(self) -> int:"""PrimaryType { get; } -> int"""
    @property
    def Range(self) -> Variable.RangeInfo:"""Range { get; } -> Variable.RangeInfo"""
    @property
    def SecondaryType(self) -> Variable.SecondaryTypeInfo:"""SecondaryType { get; } -> Variable.SecondaryTypeInfo"""
    @property
    def Storage(self) -> Variable.StorageType:"""Storage { get; } -> Variable.StorageType"""
    @property
    def TypeFlags(self) -> int:"""TypeFlags { get; } -> int"""
    @property
    def Value(self) -> object:"""Value { get; set; } -> object"""
    @property
    def Changed(self) -> VariableChangedEventHandler:
        """Changed Event: VariableChangedEventHandler"""
    @property
    def Changing(self) -> VariableChangingEventHandler:
        """Changing Event: VariableChangingEventHandler"""
    def __init__(self, pImp: _n_4_t_9, autoDelete: bool) -> Variable:...
    def Reset(self):...
    class RangeInfo(DisposableWrapper, _n_4_t_6):
        @property
        def LowerBound(self) -> int:"""LowerBound { get; set; } -> int"""
        @property
        def UpperBound(self) -> int:"""UpperBound { get; set; } -> int"""
        def __init__(self, lb: int, ub: int) -> Variable.RangeInfo:...
        def __init__(self) -> Variable.RangeInfo:...
    class SecondaryTypeInfo(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
        Angle: int
        Area: int
        Boolean: int
        Distance: int
        Last: int
        _None: int
        SymbolName: int
        UnitlessReal: int
        value__: int
    class StorageType(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
        PerDatabase: int
        PerProfile: int
        PerSession: int
        PerUser: int
        PerViewport: int
        value__: int
    class TypeFlagsInfo(_n_4_t_0, _n_4_t_1, _n_4_t_2, _n_4_t_3):
        Chatty: int
        DotMeansEmpty: int
        _None: int
        NoUndo: int
        SpacesAllowed: int
        value__: int
class VariableChangedEventArgs(_n_4_t_10, _n_4_t_6):
    @property
    def NewValue(self) -> object:"""NewValue { get; } -> object"""
    @property
    def OldValue(self) -> object:"""OldValue { get; } -> object"""
class VariableChangedEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> VariableChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: VariableChangedEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: VariableChangedEventArgs):...
class VariableChangingEventArgs(_n_4_t_10, _n_4_t_6):
    @property
    def IsResetting(self) -> bool:"""IsResetting { get; } -> bool"""
    @property
    def NewValue(self) -> object:"""NewValue { get; set; } -> object"""
    @property
    def OldValue(self) -> object:"""OldValue { get; } -> object"""
    def Veto(self, reason: str):...
class VariableChangingEventHandler(_n_4_t_14, _n_4_t_7, _n_12_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_9) -> VariableChangingEventHandler:...
    def BeginInvoke(self, sender: object, e: VariableChangingEventArgs, callback: _n_4_t_16, obj: object) -> _n_4_t_15:...
    def EndInvoke(self, result: _n_4_t_15):...
    def Invoke(self, sender: object, e: VariableChangingEventArgs):...
class Variables(DisposableWrapper, _n_4_t_6, _n_6_t_0[Variable], typing.Iterable[typing.Any]):
    @property
    def Item(self) -> Variable:"""Item { get; } -> Variable"""
    @property
    def Changed(self) -> VariableChangedEventHandler:
        """Changed Event: VariableChangedEventHandler"""
    @property
    def Changing(self) -> VariableChangingEventHandler:
        """Changing Event: VariableChangingEventHandler"""
    def GetAllNames(self) -> _n_4_t_13[str]:...
    def Reset(self, filter: Variable.StorageType):...
class WrapperAttribute(_n_4_t_4, _n_11_t_0):
    @property
    def WrappedClass(self) -> str:"""WrappedClass { get; } -> str"""
    def __init__(self, wrappedClass: str) -> WrapperAttribute:...
