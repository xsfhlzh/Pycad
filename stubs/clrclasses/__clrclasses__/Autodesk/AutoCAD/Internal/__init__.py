import __clrclasses__.Autodesk.AutoCAD.Internal.Reactors as Reactors
import __clrclasses__.Autodesk.AutoCAD.Internal.Render as Render
import __clrclasses__.Autodesk.AutoCAD.Internal.DatabaseServices as DatabaseServices
import __clrclasses__.Autodesk.AutoCAD.Internal.Forms as Forms
import __clrclasses__.Autodesk.AutoCAD.Internal.Calculator as Calculator
import __clrclasses__.Autodesk.AutoCAD.Internal.PreviousInput as PreviousInput
import __clrclasses__.Autodesk.AutoCAD.Internal.PropertyInspector as PropertyInspector
import __clrclasses__.Autodesk.AutoCAD.Internal.Windows as Windows
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import Document as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.Colors import Color as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectId as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectIdCollection as _n_2_t_1
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LineWeight as _n_2_t_2
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Database as _n_2_t_3
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Dimension as _n_2_t_4
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ColumnType as _n_2_t_5
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import AttachmentPoint as _n_2_t_6
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LayerTable as _n_2_t_7
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import LayerTableRecord as _n_2_t_8
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DBObject as _n_2_t_9
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ObjectContext as _n_2_t_10
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Handle as _n_2_t_11
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Entity as _n_2_t_12
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import Table as _n_2_t_13
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import CellRange as _n_2_t_14
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import TableStyle as _n_2_t_15
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import DataType as _n_2_t_16
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import UnitType as _n_2_t_17
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import CellAlignment as _n_2_t_18
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import CellStates as _n_2_t_19
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import UnitsValue as _n_2_t_20
from __clrclasses__.Autodesk.AutoCAD.EditorInput import PromptOpenFileOptions as _n_3_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point2d as _n_4_t_0
from __clrclasses__.Autodesk.AutoCAD.Geometry import Point3d as _n_4_t_1
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import DrawableType as _n_5_t_0
from __clrclasses__.Autodesk.AutoCAD.GraphicsInterface import ImageBGRA32 as _n_5_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_6_t_0
from __clrclasses__.Autodesk.AutoCAD.Runtime import ErrorStatus as _n_6_t_1
from __clrclasses__.Autodesk.AutoCAD.Runtime import CommandFlags as _n_6_t_2
from __clrclasses__.Autodesk.AutoCAD.Runtime import RXObject as _n_6_t_3
from __clrclasses__.Autodesk.AutoCAD.Windows import DocumentWindow as _n_7_t_0
from __clrclasses__.System import IntPtr as _n_8_t_0
from __clrclasses__.System import Uri as _n_8_t_1
from __clrclasses__.System import Enum as _n_8_t_2
from __clrclasses__.System import IComparable as _n_8_t_3
from __clrclasses__.System import IFormattable as _n_8_t_4
from __clrclasses__.System import IConvertible as _n_8_t_5
from __clrclasses__.System import MulticastDelegate as _n_8_t_6
from __clrclasses__.System import ICloneable as _n_8_t_7
from __clrclasses__.System import IAsyncResult as _n_8_t_8
from __clrclasses__.System import AsyncCallback as _n_8_t_9
from __clrclasses__.System import ValueType as _n_8_t_10
from __clrclasses__.System import IDisposable as _n_8_t_11
from __clrclasses__.System import UInt32 as _n_8_t_12
from __clrclasses__.System import Array as _n_8_t_13
from __clrclasses__.System import EventArgs as _n_8_t_14
from __clrclasses__.System import EventHandler as _n_8_t_15
from __clrclasses__.System import UInt64 as _n_8_t_16
from __clrclasses__.System import Byte as _n_8_t_17
from __clrclasses__.System import DateTime as _n_8_t_18
from __clrclasses__.System import Type as _n_8_t_19
from __clrclasses__.System import Guid as _n_8_t_20
from __clrclasses__.System.Collections import ArrayList as _n_9_t_0
from __clrclasses__.System.Collections.Generic import List as _n_10_t_0
from __clrclasses__.System.Collections.Generic import Dictionary as _n_10_t_1
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_10_t_2
from __clrclasses__.System.Collections.ObjectModel import Collection as _n_11_t_0
from __clrclasses__.System.Collections.ObjectModel import ObservableCollection as _n_11_t_1
from __clrclasses__.System.Collections.Specialized import StringCollection as _n_12_t_0
from __clrclasses__.System.ComponentModel import IComponent as _n_13_t_0
from __clrclasses__.System.ComponentModel import ISynchronizeInvoke as _n_13_t_1
from __clrclasses__.System.Drawing import Color as _n_14_t_0
from __clrclasses__.System.Drawing import Bitmap as _n_14_t_1
from __clrclasses__.System.Drawing import Icon as _n_14_t_2
from __clrclasses__.System.Globalization import CultureInfo as _n_15_t_0
from __clrclasses__.System.IO import Stream as _n_16_t_0
from __clrclasses__.System.Net import HttpWebRequest as _n_17_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_18_t_0
from __clrclasses__.System.Windows import FrameworkElement as _n_19_t_0
from __clrclasses__.System.Windows import Rect as _n_19_t_1
from __clrclasses__.System.Windows import Point as _n_19_t_2
from __clrclasses__.System.Windows import UIElement as _n_19_t_3
from __clrclasses__.System.Windows.Controls import MenuItem as _n_20_t_0
from __clrclasses__.System.Windows.Forms import UnsafeNativeMethods as _n_21_t_0
from __clrclasses__.System.Windows.Forms import ISupportOleDropSource as _n_21_t_1
from __clrclasses__.System.Windows.Forms import IDropTarget as _n_21_t_2
from __clrclasses__.System.Windows.Forms import IWin32Window as _n_21_t_3
from __clrclasses__.System.Windows.Forms import IBindableComponent as _n_21_t_4
from __clrclasses__.System.Windows.Forms import ComboBox as _n_21_t_5
from __clrclasses__.System.Windows.Forms import Control as _n_21_t_6
from __clrclasses__.System.Windows.Forms import DrawItemState as _n_21_t_7
from __clrclasses__.System.Windows.Forms import TextBox as _n_21_t_8
from __clrclasses__.System.Windows.Forms import DialogResult as _n_21_t_9
from __clrclasses__.System.Windows.Forms import Form as _n_21_t_10
from __clrclasses__.System.Windows.Forms.Layout import IArrangedElement as _n_22_t_0
from __clrclasses__.System.Windows.Input import ICommand as _n_23_t_0
from __clrclasses__.System.Windows.Media import Color as _n_24_t_0
from __clrclasses__.System.Windows.Media import ImageSource as _n_24_t_1
import typing
class AcadTaskDialogs(object):
    AcadAppNoAcVBA: int
    AcadContainsLargeObjects: int
    AcadContainsLargeObjects_TurnOffSysvarButon: int
    AcadContainsLargeObjects_TurnOnSysvarButon: int
    AcadDigitallySignedDWFx: int
    AcadLowMemoryAlert: int
    AcadRenameSheetLayout: int
    AcadRenameSheetLayout_DiscardNameChangeButon: int
    AcadRenameSheetLayout_RenameLayoutAndSheetButon: int
    AcadRenameSheetLayout_RenameLayoutOnlyButon: int
    AcadRenameSheetSetLocked: int
    AcadRenameSheetSetLocked_CancelRenameButon: int
    AcadRenameSheetSetLocked_RenameOnlyLayoutButon: int
    AcadUnresolvedFontFiles: int
    AcadUnresolvedFontFiles_IgnoreUnresolvedFontButon: int
    AcadUnresolvedFontFiles_UpdateFontButon: int
    AcadUnresolvedReferenceFiles: int
    AcadUnresolvedReferenceFiles_IgnoreUnresolvedRefButon: int
    AcadUnresolvedReferenceFiles_UpdateLocationButon: int
    AcArrayArrayClose: int
    AcArrayArrayClose_CancelButon: int
    AcArrayArrayClose_NoButon: int
    AcArrayArrayClose_YesButon: int
    AcArrayCreateNonAssocArrayForCustomObj: int
    AcArrayCustomObjSelected: int
    AcArrayCustomObjSelected_NonAssocButon: int
    AcArrayCustomObjSelected_RemoveCustomObjButon: int
    AcArrayEditSource: int
    AcArrayMaxArrayObject: int
    AcAuthEnvironBTableAuditCellEvalError: int
    AcAuthEnvironBTableAuditCellNotMatchConstant: int
    AcAuthEnvironBTableAuditDefinitionNotMatch: int
    AcAuthEnvironBTableAuditDefinitionNotMatch_AddRowButon: int
    AcAuthEnvironBTableAuditDunplicateRow: int
    AcAuthEnvironBTableAuditDunplicateRow_DeleteRowButon: int
    AcAuthEnvironBTableAuditEmptyCell: int
    AcAuthEnvironBTableAuditNotInValueSet: int
    AcAuthEnvironBTableAuditNotInValueSet_UpdateValueButon: int
    AcAuthEnvironBTableAuditNotInValueSetAndReadOnly: int
    AcAuthEnvironBTableAuditReferenceNotFound: int
    AcAuthEnvironBTableErrorClosing: int
    AcAuthEnvironBTableErrorClosing_ReturnToBTableButon: int
    AcAuthEnvironBTableErrorClosing_SaveTheBTableButon: int
    AcAuthEnvironBTableInvalidCharacter: int
    AcAuthEnvironBTableNoErrorsFound: int
    AcAuthEnvironBTableOutofValueSet: int
    AcAuthEnvironBTablePasteError: int
    AcAuthEnvironBTablePasteError_ContinuePasteButon: int
    AcAuthEnvironChangesNotSaved: int
    AcAuthEnvironChangesNotSaved_DiscardChangesButon: int
    AcAuthEnvironChangesNotSaved_SaveTheBlockButon: int
    AcAuthEnvironLookupParameterNotDefined: int
    AcAuthEnvironNoErrorsFound: int
    AcAuthEnvironNotShowBlockActionPanel: int
    AcAuthEnvironParameterChangesNotSaved: int
    AcAuthEnvironParameterChangesNotSaved_DiscardTheChangesButon: int
    AcAuthEnvironParameterChangesNotSaved_SaveTheParameterButon: int
    AcAuthEnvironParameterChangesNotSavedUnderConstrained: int
    AcAuthEnvironParameterChangesNotSavedUnderConstrained_SaveItButon: int
    AcAuthEnvironParameterChangesNotSavedUnderConstrainedClosingEditor: int
    AcAuthEnvironParameterChangesNotSavedUnderConstrainedClosingEditor_DiscardTheChangesButon: int
    AcAuthEnvironParameterChangesNotSavedUnderConstrainedClosingEditor_SaveTheParameterButon: int
    AcAuthEnvironProxyObjectsFound: int
    AcAuthEnvironRedefineBlock: int
    AcAuthEnvironRedefineBlock_RedefineBlockAndUpdateButon: int
    AcAuthEnvironRedefineBlock_UnRedefineBlockButon: int
    AcBattmanSynchronizeBlocks: int
    AcBattManValueChange: int
    AcBlockAnnotivePropertyChanged: int
    AcBlockAnnotivePropertyChanged_NotSaveChangesButon: int
    AcBlockAnnotivePropertyChanged_SaveChangesButon: int
    AcBlockBlockNameNotSpecified: int
    AcBlockCannotInsertAnnotiveBlocks: int
    AcBlockCircularBlockReference: int
    AcBlockCustomPropMightLost: int
    AcBlockCustomPropMightLost_RetainCurrentScaleButon: int
    AcBlockCustomPropMightLost_SetUniformScaleButon: int
    AcBlockFileNotFound: int
    AcBlockInvalidBlockName: int
    AcBlockInvalidBlockName_Continue2Buton: int
    AcBlockInvalidCoordianteVaule: int
    AcBlockInvalidCoordianteVaule_Continue1Buton: int
    AcBlockMismatchGeoCS: int
    AcBlockNoObjectsSelected: int
    AcBlockNoObjectsSelected_ContinueDefineButon: int
    AcBlockNoObjectsSelected_SelObjectsButon: int
    AcBlockNotModified: int
    AcBlockObjectsOnLockedLayer: int
    AcBlockRedefineBlock: int
    AcBlockRedefineBlock_RedefineBlockButon: int
    AcBlockWriteBlockNoObjectsSelected: int
    AcBlockWriteBlockNoObjectsSelected_SelectObjectsButon: int
    AcBlockXrefConflict: int
    AcCloudCreateFolderExists: int
    AcCloudCreateFolderInvalid: int
    AcCloudCreateFolderPathnameLength: int
    AcCmMgrAlreadyInGroup: int
    AcCmMgrAutoconNoTypeSelected: int
    AcCmMgrConstrBarFilterZero: int
    AcCmMgrCovertAssocDimTooMany: int
    AcCmMgrDeleteDimConstraint: int
    AcCmMgrDeleteDimParameter: int
    AcCmMgrDeleteDimParameter_ConvertDimensionalConstraintButon: int
    AcCmMgrDeleteDimParameter_DeleteParameterNameButon: int
    AcCmMgrDeleteUserParameter: int
    AcCmMgrDeleteUserParameter_DeleteUserParameterButon: int
    AcCmMgrDimOverConstrain: int
    AcCmMgrDimOverConstrain_CreateRefButon: int
    AcCmMgrDimOverConstrain_ReselectButon: int
    AcCmMgrEntityBlockSame: int
    AcCmMgrEvaluationFail: int
    AcCmMgrRefeditWithConstraint: int
    AcCmMgrReferencedInEquation: int
    AcCmMgrRelaxDragging: int
    AcCmMgrToleranceTooLarge: int
    AcCmMgrToleranceTooLarge_ProceedAutoConstrainButon: int
    AcContentBlockImportMultiple: int
    AcContentBlockImportSingle: int
    AcCoreBHCreatFailure: int
    AcCoreCheckSpellBlock: int
    AcCoreCheckSpellXref: int
    AcCoreIncompatibleArxApplication: int
    AcCoreIncompatibleArxApplication_LoadAllButon: int
    AcCoreIncompatibleArxApplication_LoadAppButon: int
    AcCoreIncompatibleArxApplication_SkipAllButon: int
    AcCoreIncompatibleArxApplication_SkipThisButon: int
    AcCoreMissingLanguagePack: int
    AcCoreMissingLanguagePack_CancelAndInstallButon: int
    AcCoreMissingLanguagePack_OpenDrawingButon: int
    AcCoreOpenACopy: int
    AcCorePartialOpenDrawing: int
    AcCorePartialOpenDrawing_PartialOpenButon: int
    AcCorePartialOpenDrawing_RestorePartialOpenStateButon: int
    AcCorePartialOpenFileLocked: int
    AcCorePartialOpenLastSaved: int
    AcCorePartialOpenLastSaved_OpenButon: int
    AcCorePartialOpenLastSaved_RestoreButon: int
    AcCorePartialOpenLocked: int
    AcCorePointInBoundary: int
    AcCorePointOutsideBoundary: int
    AcCoreRasteroutput: int
    AcCoreRasteroutput_IgnoreRasterButon: int
    AcCoreTrueConvert: int
    AcCoreWelcomeScreenNotFound: int
    AcDataLinkCannotUpdateData: int
    AcDataLinkExcelNotFound: int
    AcDataLinkExcelSheetNotFound: int
    AcDataLinkInvalidExcelFile: int
    AcDataLinkInvalidRange: int
    AcDataLinkOverwrittenDatalinkCells: int
    AcDataLinkOverwrittenDatalinkCells_RetainCellsButon: int
    AcDataLinkOverwrittenDatalinkCells_UpdateCellsButon: int
    AcDimInvalidStyleName: int
    AcDimRedefineDimStyle: int
    AcDwgFeedSaveFile: int
    AcDwgFeedSaveFile_SaveButon: int
    AcDwgFeedSaveFile_SyncToA360Buton: int
    AcDxFilesNotFound: int
    AcDxFilesNotFound_ContinueUpdateButon: int
    AcDxFilesNotFound_DoNotUpdateButon: int
    AcDxOutdatedTable: int
    AcDxOutdatedTable_SkipAllUpdatesButon: int
    AcDxOutdatedTable_SkipUpdateButon: int
    AcDxOutdatedTable_UpdateAllButon: int
    AcDxOutdatedTable_UpdateButon: int
    AcDxUpdateMCCells: int
    AcDxUpdateMCCells_SkipManuallyChangedCellsButon: int
    AcDxUpdateMCCells_UpdateAllCellsButon: int
    AcDxWizardDataExtractionFilesNotFound: int
    AcDxWizardQuitWizard: int
    AcDxWizardRemoveDrawing: int
    AcDxWizardRemoveDrawings: int
    AcDxWizardRemoveFolder: int
    AcDxWizardUnsavedDrawing: int
    AcDxWizardUnsavedDrawing_SaveDrawingButon: int
    AcEtransmitKeepDesignFeed: int
    AcGeoLocationUICoordSysAlreadyDefined: int
    AcGeoLocationUIDGLGEInstalled: int
    AcGeoLocationUIDGLGENotInstalled: int
    AcGeoLocationUIGoogleEarthNotOpen: int
    AcGeoLocationUIImportFromGoogleEarth: int
    AcGeoLocationUIInitialNotification: int
    AcGeoLocationUIInvalidKMLFile: int
    AcGeoLocationUIInvalidValue: int
    AcGeoLocationUILocationAlreadyExists: int
    AcGeoLocationUIMultipleLocationsFound: int
    AcGeoLocationUIOptimizeGeomapImage: int
    AcGeoLocationUIOptimizeGeomapImage_OptimizeButon: int
    AcGeoLocationUIOptimizeGeomapImage_ReloadButon: int
    AcGeoLocationUIOxygenDisabled: int
    AcGeoLocationUIOxygenUpdateAvailable: int
    AcGeoLocationUIPlotLiveMapWarning: int
    AcGeoLocationUIRemove: int
    AcGeoLocationUIReorientMarker: int
    AcGeoLocationUITimeZoneChanged: int
    AcGeoLocationUITimeZoneUpdated: int
    AcGeoLocationUIUnitMismatch: int
    AcGeoLocationUIUnitMismatch_ContinueButon: int
    AcGeoLocationUIUnitMismatch_ResetButon: int
    AcGuSMInvalidEntry: int
    AcGuSMReuildCurveDialogBoxInvalidEntry: int
    AcGuSMReuildSurfaceDialogBoxInvalidEntry: int
    AcLayerAppsCannotRestoreLayerState: int
    AcLayerAppsDleteLayerState: int
    AcLayerAppsLayerMergeVerify: int
    AcLayerAppsLayerNotMerged: int
    AcLayerAppsLayerStateAddLayer: int
    AcLayerAppsLayerStateDuplicates: int
    AcLayerAppsLayerstateInvalidFile: int
    AcLayerAppsLayerstateInvalidFile2: int
    AcLayerAppsLayerStateNoneFound: int
    AcLayerAppsLayerStateNoneSelected: int
    AcLayerAppsLayerStateSuccessfulImport: int
    AcLayerAppsOverwriteLayerState: int
    AcLaytransChangesNotSaved: int
    AcLaytransChangesNotSaved_TranslateAndSaveButon: int
    AcLaytransChangesNotSaved_TranslateOnlyButon: int
    AcLayTransInvalidTransparencyValue: int
    AcModelDocInventorImport: int
    AcModelDocSketchModeEnteringViewSketch: int
    AcOpmExtZeroValueParameter: int
    AcParameterParameterFiltered: int
    AcPlotGuiPlotFileExists: int
    AcPlotGuiPlotScaleConfirm: int
    AcPointCloudCompatibility: int
    AcPointCloudGeoMismatch: int
    AcPublish3DDWFCreated: int
    AcPublishDSDSettingConflict: int
    AcPublishLoadSheetList: int
    AcPublishNoPasswordSpecified: int
    AcPublishSaveSheetList: int
    AcPurgeConfirmPurge: int
    AcPurgeConfirmSinglePurge: int
    AcPurgeConfirmSinglePurge_PurgeThisItemButon: int
    AcPurgeConfirmSinglePurge_SkipThisItemButon: int
    AcSignAppDigitalIDNotAvailable: int
    AcSignApplyDigitalSignaturePreviouslySignedFile: int
    AcSignApplyDigitalSignatureReadOnlyFile: int
    AcSMConersonToASpline: int
    AcSmNavCalloutBlockImportMultiple: int
    AcSmNavCalloutBlockImportMultiple_MultipleFileMultipleBlockButon: int
    AcSmNavCalloutBlockImportMultiple_MultipleFileOneBlockButon: int
    AcSmNavCalloutBlockImportSingle: int
    AcSmNavCalloutBlockImportSingle_SingleFileMultipleBlockButon: int
    AcSmNavCalloutBlockImportSingle_SingleFileOneBlockButon: int
    AcSMNavDrawingFileNotFound: int
    AcSmNavInvalidNameTooLong: int
    AcSmNavLayoutDrawingMissing: int
    AcSmNavLayoutDrawingMissing_AcSmNav_BrowseRemapLayoutButon: int
    AcSmNavLayoutDrawingMissing_AcSmNav_RemoveLayoutButon: int
    AcSmNavLayoutIssueWithDrawing: int
    AcSmNavLayoutIssueWithDrawing_DiscardDuplicateButon: int
    AcSmNavLayoutIssueWithDrawing_DuplicateButon: int
    AcSmNavLayoutMissing: int
    AcSmNavLayoutMissing_BrowseRemapLayoutButon: int
    AcSmNavLayoutMissing_RemapLayoutButon: int
    AcSmNavLayoutMissing_RemoveLayoutButon: int
    AcSmNavProjectManagerProjectsFolderCreation: int
    AcSmNavProjectManagerProjectsFolderCreation_SELECTFOLDERButon: int
    AcSmNavProjectManagerProjectsFolderCreation_UseDocumentsFolderButon: int
    AcStdCheckComplete: int
    AcStdStandardsViolationFound: int
    AcSubDCannotRefineAtMinLevel: int
    AcSubDConvertToASM: int
    AcSubDConvertToASM_ConvertToFacetedASMButon: int
    AcSubDConvertToASM_ConvertToSmoothASMButon: int
    AcSubDConvertToASM_FilterMeshObjectsButon: int
    AcSubDConvertToASMInvalidTopology: int
    AcSubDConvertToMesh: int
    AcSubDConvertToMesh_ConvertObjectsButon: int
    AcSubDConvertToMesh_FilterObjectsButon: int
    AcSubDMaxSmoothLevel: int
    AcSubDMeshPrimitiveDialogBoxInvalidEntry: int
    AcSubDMeshSmoothInvalidSelection: int
    AcSubDMeshSmoothNonPrimitiveObject: int
    AcSubDMeshSmoothNonPrimitiveObject_CreateMeshButon: int
    AcSubDMeshSmoothNonPrimitiveObject_DoNotConvertToMeshButon: int
    AcSubDMeshSmoothTooManyFaces: int
    AcSubDMinSmoothLevel: int
    AcSubDOptionsDialogBoxInvalidEntry: int
    AcSubDTessellationDialogBoxInvalidEntry: int
    AcSubDUnsupportedObject: int
    AcSubDUnsupportedSubObject: int
    AcSynergyDeferUpdatesQueuedChanges: int
    AcSynergyFinishSymbolSketchDeleteSymbol: int
    AcSynergyFinishSymbolSketchInvalidSymbol: int
    AcSynergyFinishSymbolSketchInvalidSymbol_DiscardInvalidChangesButon: int
    AcSynergyFinishSymbolSketchInvalidSymbol_RepairSymbolButon: int
    AcSynergyFinishSymbolSketchSaveExit: int
    AcSynergyFinishSymbolSketchSaveExit_DiscardSymbolSketchChangesButon: int
    AcSynergyFinishSymbolSketchSaveExit_SaveSymbolSketchButon: int
    AcSynergyInventorReferencesOutOfDate: int
    AcSynergyLabelExcludeCharactersInvalid: int
    AcSynergyLODUnresolved: int
    AcSynergyOpenDrawingLostFunctionality: int
    AcSynergyPublishNotification: int
    AcSynergyUnresolvedBeingOpened: int
    AcSynergyUnresolvedInventorFiles: int
    AcSynergyUnresolvedInventorFiles_SelectProjectButon: int
    AcSynergyVIEWBASEUnresolved: int
    AcSynergyViewSTDHighResolution: int
    AcSynergyViewStyleRestoreDefaults: int
    AcSynergyViewUpdateAssociativeAnnotations: int
    AcSynergyViewUpdateAssociativeLossDetected: int
    AcTableCanNotPasteIntoLockedCells: int
    AcTableConfirmDeleteTableStyle: int
    AcTableConfirmDeleteTableStyle_DeleteTableStyleButon: int
    AcTableDetachDataLink: int
    AcTableInvalidTbCellValue: int
    AcTableInvalidTbCellValue_ChangeDataTypeButon: int
    AcTableInvalidTbCellValue_ChangeDataValueButon: int
    AcTableLargeNBOfCells: int
    AcTableMergeCells: int
    AcTableOverwriteStartingTable: int
    AcTableOverwriteStartingTable_OverwriteButon: int
    AcTableRangeMismatch: int
    AcTableRangeOverlap: int
    AcTableRedefineCellStyle: int
    AcTableRedefineTableStyle: int
    AcTableRemoveStartingTable: int
    ActionRecorderCommandNotRecordedOnDYNMODE: int
    ActionRecorderConfirmDeletionOfActionMacro: int
    ActionRecorderConfirmDeletionOfItem: int
    ActionRecorderConfirmMultipleDeletion: int
    ActionRecorderConflictWithCommandName: int
    ActionRecorderConflictWithExistingMacroName: int
    ActionRecorderError: int
    ActionRecorderFileNameAlreadyExists: int
    ActionRecorderInconsistency: int
    ActionRecorderInvalidName: int
    ActionRecorderNameAlreadyExists: int
    ActionRecorderNoDirectorySpecified: int
    ActionRecorderNoObjectsSelected: int
    ActionRecorderPlaybackComplete: int
    ActionRecorderPlaybackError: int
    ActionRecorderUnableToAccessDefaultFolder: int
    ActionRecorderUserMessage: int
    ActionRecorderValueNotRecorded: int
    ActionRecorderValueTypeMismatch: int
    AcTranslatorsExportTranslationProcessIsRunning: int
    AcTranslatorsRunExportTranslationInBackground: int
    AcTranslatorsRunTranslationInBackground: int
    AcTranslatorsTranslationProcessIsRunning: int
    AcUnderlayInvalidFile: int
    AdRefManAddXRefs: int
    AdRefManRemoveFolderPaths: int
    AssocFilletExplodePolyline: int
    AssocNetworkEvaluationFail: int
    AssocSurfaceCreationFail: int
    AssocSurfaceModificationFail: int
    AssocVariableEvaluationFail: int
    AutoCADAcCloudConnectDocCloseBlocker: int
    AutoCADAcCloudConnectSyncFileNotSaved: int
    AutoCADApplicationRestart: int
    AutoCADAssociativePathArray: int
    AutoCADAssociativePathArray_AssociativePathArray_CancelButon: int
    AutoCADAssociativePathArray_AssociativePathArray_ContinueButon: int
    AutoCADAutodeskMaterialLibNotFound: int
    AutoCADAutodeskMaterialLibNotInstalled: int
    AutoCADAutodeskMaterialTexNotFound: int
    AutoCADAutodeskMaterialTexNotInstalled: int
    AutoCADAutodeskMediumTexDownloadError: int
    AutoCADAutodeskMediumTexNotInstalled: int
    AutoCADAutodeskMediumTexNotInstalledLight: int
    AutoCADAutodeskMediumTexTobeInstalled: int
    AutoCADCannotGripEdit: int
    AutoCADCannotGripEdit_CannotGripEdit_CancelButon: int
    AutoCADCannotGripEdit_CannotGripEdit_continueButon: int
    AutoCADCannotRelax: int
    AutoCADCannotRotate: int
    AutoCADCannotRotate_CannotRotate_MaintainButon: int
    AutoCADCannotRotate_CannotRotate_RelaxButon: int
    AutoCADChangesNotSaved: int
    AutoCADChangesNotSaved_DiscardAndCloseButon: int
    AutoCADChangesNotSaved_SaveAndCloseButon: int
    AutoCADCleanScreenOn: int
    AutoCADConflictingSettings: int
    AutoCADConnectionError: int
    AutoCADCustomizationSyncInProgress: int
    AutoCADDependencyOnTrimAction: int
    AutoCADDependencyOnTrimAction_DependencyOnTrimAction_CancelButon: int
    AutoCADDependencyOnTrimAction_DependencyOnTrimAction_continueButon: int
    AutoCADDisableCustomizationSync: int
    AutoCADDWGAssociation: int
    AutoCADEnableCustomizationSync: int
    AutoCADExceededSizeLimit: int
    AutoCADExceededSizeLimit_SaveDWGXButon: int
    AutoCADExceededSizeLimit_ShowDetailsButon: int
    AutoCADHelpFileNotFound: int
    AutoCADHelpFileNotFound_NotLaunchHelpButon: int
    AutoCADHelpFileNotFound_UpdateHelpFileLocationButon: int
    AutoCADMissingDWFViewer: int
    AutoCADMissingOrCorruptDisplayDriver: int
    AutoCADMissingOrCorruptDisplayDriverMac: int
    AutoCADMissingPDFViewer: int
    AutoCADNearingSizeLimit: int
    AutoCADNearingSizeLimit_LargeObjectSupportOffButon: int
    AutoCADNearingSizeLimit_LargeObjectSupportOnButon: int
    AutoCADNewComputer: int
    AutoCADOfflineHelpNotInstalled: int
    AutoCADOfflineHelpNotInstalled_CopyToClipboardButon: int
    AutoCADOfflineHelpNotInstalled_DownloadOfflineHelpButon: int
    AutoCADOfflineHelpNotInstalled_UseOnlineHelpButon: int
    AutoCADOnlineHelpNotAccessible: int
    AutoCADOnlineHelpNotAccessible_TryConnectInternetButon: int
    AutoCADOnlineHelpNotAccessible_UseOfflineHelpButon: int
    AutoCADParametricExpression: int
    AutoCADParametricExpression_ParametricExpression_CancelButon: int
    AutoCADParametricExpression_ParametricExpression_ContinueButon: int
    AutoCADRelaxDragging: int
    AutoCADRelaxDragging_DeleteButon: int
    AutoCADRelaxDragging_RelaxButon: int
    AutoCADRenderScaleSettings: int
    AutoCADRenderScaleSettings_CancelRenderButon: int
    AutoCADRenderScaleSettings_ConvertToMetersButon: int
    AutoCADSignOut: int
    AutoCADSubtractSurface: int
    AutoCADSubtractSurface_SubtractSurface_CancelButon: int
    AutoCADSubtractSurface_SubtractSurface_ContinueButon: int
    AutoCADTooManyControlVertices: int
    AutoCADTooManyControlVertices_TooManyControlVertices_CancelButon: int
    AutoCADTooManyControlVertices_TooManyControlVertices_ContinueButon: int
    AutoCADUnionSurface: int
    AutoCADUnionSurface_UnionSurface_CancelButon: int
    AutoCADUnionSurface_UnionSurface_ContinueButon: int
    AutoCADUnsupportedObjects: int
    AutoCADUnsupportedObjects_DoNotShowUnsupportedObjects_ButtonButon: int
    AutoCADUnsupportedObjects_ShowBoundingBox_ButtonButon: int
    AutoCADUnsupportedObjects_ShowObjectsIfAvailable_ButtonButon: int
    AutoCADXrefLockFail: int
    AutodeskMismatchGeoCS: int
    AutodeskRemoveSectionJogs: int
    AutodeskReqVersionNoOpen: int
    AutodeskReqVersionOpenForWrite: int
    AutodeskReqVersionReadOnly: int
    AutodeskSharedCloudFile: int
    AutoLISPLoadSettings: int
    BatchStandardsCheckerReportFile: int
    BEDITConstraintsFound: int
    BlockCircularReference: int
    BlockCircularReferenceToTable: int
    BoundaryBoundaryDefinitionError: int
    ColorDlgMissingColorBook: int
    ConstraintDynamicBlockGripsWillBeHidden: int
    ConstraintNonAssociativeSelection: int
    ConstraintNonDimConstraintSelection: int
    ConstraintOverConstraint: int
    ConstraintWouldOverContrain: int
    ConvertHatchObjectsWarning: int
    CUICannotCopyNestedToolbarFlyouts: int
    CUIDeleteReferencedImage: int
    CUIDeleteUnreferencedImage: int
    CUIFoldPanelContents: int
    CUIImageNameAlreadyExist: int
    CUIImageNameInvalid: int
    CUIReset: int
    CUIReset_CUIResetCancelButon: int
    CUIReset_CUIResetContinueButon: int
    CUIRestoreBackup: int
    CUIRestoreBackup_CUIRestoreBackupCancelButon: int
    CUIRestoreBackup_CUIRestoreBackupContinueButon: int
    CustomizationComfirmCopytoRibbonPanels: int
    CustomizationSaveChanges: int
    CustomizationUndefinedObjectType: int
    CustomizationUnsavedCUIChanges: int
    DGN3DSeedFileRequired: int
    DGNIncompatibleSeedFile: int
    DGNIncompatibleSeedFile_SelectAnotherDGNExportButon: int
    DGNIncompatibleSeedFile_SelectAnotherSeedButon: int
    DGNInvalidDGNFile: int
    DGNNoDesignModelsFound: int
    DGNUIConfirmMappingRemoval: int
    DgnUIDGNImportUnsupportObjects: int
    DGNUIIncompatibleSeedFileSettings: int
    DGNUIIncompatibleSeedFileSettings_ContinueExportButon: int
    DGNUIInvalidPropertyName: int
    DGNUIInvalidSeedFile: int
    DGNUINumberOfElementsExceededLimit: int
    DgnUIUnsupportDGNExportObjects: int
    DigitalSignaturesUnsupportedDrawingFormat: int
    DimensionFrozenLayer: int
    DimensionNoDimensionsSelected: int
    DimMLeaderStyleRedefineStyle: int
    DimMLeaderStyleRedefineStyle_DoNotRedefineStyleButon: int
    DimMLeaderStyleRedefineStyle_RedefineStyleButon: int
    DrawingOpenForeignDWGFile: int
    DrawingSaveAsAcModelDoc: int
    DwgAidsRestoreAllContexts: int
    DwgAidsRestoreClassicColors: int
    DwgAidsRestoreCurrentContext: int
    DwgAidsRestoreCurrentContext_RestoreCurrentContextButon: int
    DWGRecoveryDamagedFile: int
    DWGRecoveryDrawingRecovery: int
    DWGRecoveryErrorsFound: int
    DWGRecoveryRecoverSummary: int
    EnterpriseWorkspaceCannotSaveChanges: int
    ExportLayoutFileCreated: int
    ExportLayoutFileCreatedSDI: int
    ExportSelectWindow: int
    ExportSelectWindowSuccessful: int
    FBXExportMissingTextures: int
    FBXExportNoEntitiesSelected: int
    FBXExportNothingToExport: int
    FBXExportUnsupportedObjects: int
    FBXImportCancel: int
    FBXImportFileNotFound: int
    FBXImportNoEntitiesSelected: int
    FBXImportOptionsDialogBoxInvalidEntry: int
    FBXImportOptionsInsertAndCameras: int
    FBXImportProcessingFile: int
    FBXImportTextureNotFound: int
    FBXImportUnsupportedFile: int
    HatchBoundaryDefinitionErrorNRC: int
    HatchBoundaryDefinitionErrorRC: int
    HatchDenseHatchCreation: int
    HatchDrawingHasLargeHatches: int
    HatchDuplicatePatternSelected: int
    HatchDuplicatePatternSelected_OverwriteButon: int
    HatchDuplicatePatternSelected_SkipButon: int
    HatchFrozenLayer: int
    HatchInvalidPatternSelected: int
    HatchInvalidPatternSelected_CancelButon: int
    HatchInvalidPatternSelected_RevealInFinderButon: int
    HatchInvalidPatternSelectedSandboxed: int
    HatchInvalidPatternSelectedSandboxed_RemoveButon: int
    HatchOpenBoundary: int
    LayerManagerCannotAdjustPlotSetting: int
    LayerManagerCannotMakeCurrent: int
    LayerManagerCurrentLayerOff: int
    LayerManagerCurrentLayerOffMac: int
    LayerManagerDeletedBlockRefs: int
    LayerManagerDeleteGroupWarning: int
    LayerManagerDeleteGroupWarning_DeleteGroupAndLayersButon: int
    LayerManagerDeleteGroupWarning_DeleteGroupWithoutLayersButon: int
    LayerManagerExcessLayerFilters: int
    LayerManagerHideSystemGroup: int
    LayerManagerLayerCannotFreeze: int
    LayerManagerLayerCannotFreezeMac: int
    LayerManagerLayerDeleteMac: int
    LayerManagerLayerDeleteMac_Calcel_DeleteButon: int
    LayerManagerLayerDeleteMac_DeleteLayerAndMoveObjectsButon: int
    LayerManagerLayerDeleteMac_DeleteLayerAndObjectsButon: int
    LayerManagerLayerRename: int
    LayerManagerMultipleDeleteConfirmation: int
    LayerManagerMutipleLayerNotDeleted: int
    LayerManagerNewLayerFilteredWarning: int
    LayerManagerNoMatchingLayers: int
    LayerManagerNoMatchingLayers_CreateGroupAnywayButon: int
    LayerManagerNoMatchingLayers_EditTheGroupButon: int
    LayerManagerShowMessageClose: int
    LayerManagerShowMessageYesNo: int
    LayerManagerSingleDeleteConfirmation: int
    LayerManagerSingleLayerNotDeleted: int
    LayerManagerUnableToModifyLayersWarning: int
    LayerToolsIncompatibleVisualStyle: int
    LayerWalkLayerStatesChange: int
    LinetypeReloadLinetype: int
    MainFrameCommandLineHideWindow: int
    MaterialDeleteNestedMaps: int
    MaterialsDesynchronizeMaps: int
    MaterialsLibraryInUse: int
    MaterialsMaterialInUseOnLockedLayer: int
    MaterialsSynchronizeMaps: int
    MaterialUIMaterialInUse: int
    MaterialUIMigrateMaterial: int
    MTEUnknownTextFonts: int
    MTEXTAutoStackProperties1: int
    MTEXTAutoStackProperties1WithoutDoNotShow: int
    MTEXTAutoStackProperties2: int
    MTextStyleChange: int
    MTextUnsavedChanges: int
    MTextWarningAboutBullets: int
    MTextWarningAboutPasting: int
    NavToolsNeedGreaterEqualNumber: int
    NavToolsNeedGreaterNumber: int
    NavToolsNeedNumInRange: int
    ObjectNameNoFolderAccess: int
    OPMAcPEXCtlCannotModifyProperty: int
    OPMAcPEXCtlPatternNameNotFound: int
    OpmNoObjectsFound: int
    OptionOnlineTabDisableCloudDocuments: int
    PhotoViewerFileNotFound: int
    PhotoViewerFileOrFolderNotFound: int
    PhotoViewerInvalidFileFormat: int
    PhotoViewerRemoveImage: int
    PlotAndPublishCancelEntireJob: int
    PlotAndPublishCancelEntireSheet: int
    PlotBatchPlotFromPlot: int
    PlotBatchPlotFromPlot_BatchPlotFromPlot_CancelButon: int
    PlotBatchPlotFromPlot_BatchPlotFromPlot_ContinueButon: int
    PlotBatchPlotFromPlot_BatchPlotFromPlot_LearnMoreButon: int
    PlotGuiPlotModelSpaceAlert: int
    PlotGuiPlotModelSpaceAlert_TaskPlotDialogButton_181Buton: int
    PlotGuiPlotModelSpaceAlert_TaskPlotDialogButton_182Buton: int
    PlotPaperSizeNotFound: int
    PlotProcessingBackgroundJob: int
    PlotShadePlot: int
    Printing3DNoInternetConn: int
    Printing3DObjectsOnLockedLayer: int
    Printing3DPrepareModel: int
    PropertiesObjectsMoveToFrozenOrOffLayers: int
    PropertiesObjectsOnLockedLayers: int
    PulishNoPreset: int
    PulishPresetIllegalChar: int
    PulishPresetInvalidName: int
    PulishPresetInvalidResolution: int
    PulishPresetNameExist: int
    PulishSaveDSD: int
    QPDockToRibbon: int
    QPOffPanelWarning: int
    QPRemoveUndefObjType: int
    QPRestoreDefault: int
    QPRestoreDefault_KeepQPCustomButon: int
    QPRestoreDefault_RestorQPeSettingsButon: int
    QPSwitchToFloatMode: int
    QPSyncWithTooptip: int
    QVDrawingCloseAllOtherDrawings: int
    QVDrawingCloseReadOnly: int
    RecoverAllWarning: int
    RenderIBLWarnSetBackgroundWithDisplayImageOn: int
    RenderNoFacesToRender: int
    RenderOutOfMemory: int
    RenderSoftOutOfMemory: int
    RibbonUnableToAddControlIntoQAT: int
    RibbonUnableToAddSeparatorIntoQAT: int
    RibbonUnableToRemoveFromQAT: int
    RollOverRestoreDefault: int
    RollOverRestoreDefault_KeepCustomButon: int
    RollOverRestoreDefault_RestoreSettingsButon: int
    ScaleListLargeScaleAlert: int
    ScaleListResetScaleList: int
    SceneUIPhotometricDistantLights: int
    SceneUISunlightAndExposure: int
    SceneUIViewportLightingMode: int
    SecurityStartAutoCADInAdminMode: int
    SecurityWritablePathWarning: int
    SecurityWritablePathWarning_ContinueButon: int
    SeekFileNameTooLong: int
    seekSaveChanges: int
    seekSaveChanges_TranslateAndSave1Buton: int
    seekSaveChanges_TranslateAndSave2Buton: int
    seekSaveFile: int
    seekSaveFile_SaveFileButon: int
    seekWebsiteNotAvailable: int
    SheetSetManagerConfirmChanges: int
    SheetSetManagerConfirmChangesForGroups: int
    SheetSetManagerDrawingFileNotFound: int
    SheetSetManagerLostSetAssociation: int
    ShowMotionDeleteAllView: int
    ShowMotionQuickViewDeleteCategoryViews: int
    ShowMotionQuickViewRenameError: int
    ShowMotionUpdateAll: int
    SpellerCheckLayersLocked: int
    StandardCloseReadOnly: int
    StandardDeleteConfirmation: int
    StandardDuplicateNameCopyOverwrite: int
    StandardDuplicateNameError: int
    StandardDuplicateNameReplaceCancel: int
    StandardFileAlreadyExists: int
    StandardFileAlreadyExists_RenameButon: int
    StandardFileAlreadyExists_ReplaceButon: int
    StandardFileConfirmationWithNoToAll: int
    StandardFileConfirmationWithoutNoToAll: int
    StandardFileInUse: int
    StandardFileNotFound: int
    StandardFilePathTooLong: int
    StandardInvalidNameEmptyName: int
    StandardInvalidNameTooLong: int
    StandardInvalidNameUnsupportedCharacters: int
    StandardInvalidPath: int
    StandardInValidPropertyName: int
    StandardObjectTypeCannotBeDeleted: int
    StandardObjectUnsupportCharacters: int
    StandardOffsetObjectIsNotPlanar: int
    StandardPathOrFileNameNotSpecified: int
    StandardWriteProtectedFile: int
    SurfaceCVEditing: int
    TextFindBlockRef: int
    TextFindBlockRef_ReplaceAllButon: int
    TextFindBlockRef_ReplaceThisButon: int
    TextFindBlockRef_SkipButon: int
    UnitsInsertUnits: int
    UnitsRenderEngine: int
    VMToolsUIOverwriteAnimationFrames: int
    VMToolsUIWalkFlyToPerspectiveView: int
    def __init__(self) -> AcadTaskDialogs:...
    @staticmethod
    def ShowCurrentLayerOff() -> int:...
    @staticmethod
    def ShowDuplicateNameCopyReplaceTD(objectname: str, duplicatename: str, copyname: str, pParentWnd: _n_8_t_0) -> int:...
    @staticmethod
    def ShowDuplicateNameErrorTD(objectname: str, duplicatename: str, pParentWnd: _n_8_t_0) -> int:...
    @staticmethod
    def ShowDuplicateNameReplaceCancelTD(objectname: str, duplicatename: str, pParentWnd: _n_8_t_0) -> int:...
    @staticmethod
    def ShowFileConfirmationWithNoToAll(featureName: str, featureType: str, fullFileName: str, fileName: str, pParentWnd: _n_8_t_0) -> int:...
    @staticmethod
    def ShowFileConfirmationWithoutNoToAll(featureName: str, featureType: str, fullFileName: str, fileName: str, pParentWnd: _n_8_t_0) -> int:...
    @staticmethod
    def ShowInvalidNameEmptyNameTD(objectname: str, fieldname: str, pParentWnd: _n_8_t_0):...
    @staticmethod
    def ShowInvalidNameTooLongTD(objectname: str, fieldname: str, pParentWnd: _n_8_t_0):...
    @staticmethod
    def ShowInvalidNameUnsupportedCharactersTD(objectname: str, fieldname: str, pParentWnd: _n_8_t_0):...
    @staticmethod
    def ShowLayerCannotFreeze():...
    @staticmethod
    def Source() -> _n_8_t_1:...
class AcAeUtilities(object):
    def __init__(self) -> AcAeUtilities:...
    @staticmethod
    def GetBeditConstraintColor(constraintType: AcAeUtilities.ConstraintType) -> _n_1_t_0:...
    @staticmethod
    def GetBlockName() -> str:...
    @staticmethod
    def GetCurrentVisibilityStateName() -> str:...
    @staticmethod
    def GetVisibilitySets(visibilities: _n_10_t_0[str]):...
    @staticmethod
    def IsAuthorPaletteVisible() -> bool:...
    @staticmethod
    def IsInBlockEditor() -> bool:...
    @staticmethod
    def IsInBVMode() -> bool:...
    @staticmethod
    def IsVisibilityParameterPresent() -> bool:...
    @staticmethod
    def LearnBlockEditor():...
    @staticmethod
    def PickFirstBeforeInvokeBvHide() -> bool:...
    @staticmethod
    def PickFirstBeforeInvokeBvShow() -> bool:...
    @staticmethod
    def SetBeditConstraintColor(constraintType: AcAeUtilities.ConstraintType, color: _n_1_t_0):...
    @staticmethod
    def ShowAuthorPalette(bShow: bool):...
    class ConstraintType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        FullyConstrained: int
        OverConstrained: int
        PartiallyConstrained: int
        Unconstrained: int
        value__: int
class AcDownloadCallback(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> AcDownloadCallback:...
    def BeginInvoke(self, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self):...
class AcNavisworksProtocolAdapter(_n_8_t_10):
    pass
class AcNavisworksService(INavisworksService, _n_8_t_11):
    def __init__(self) -> AcNavisworksService:...
class ActiveThemeColor(object):
    @property
    def CurrentTheme(self) -> ColorThemeEnum:"""CurrentTheme { get; } -> ColorThemeEnum"""
    @property
    def InspectorBGHighlight(self) -> _n_14_t_0:"""InspectorBGHighlight { get; } -> Color"""
    @property
    def InspectorItem(self) -> _n_14_t_0:"""InspectorItem { get; } -> Color"""
    @property
    def PaletteBackground(self) -> _n_14_t_0:"""PaletteBackground { get; } -> Color"""
    @property
    def ColorThemeChanged(self) -> ColorThemeChangedEventHandler:
        """ColorThemeChanged Event: ColorThemeChangedEventHandler"""
    @staticmethod
    def Instance() -> ActiveThemeColor:...
class AppLoaderDownloadUtils(object):
    def __init__(self) -> AppLoaderDownloadUtils:...
    @staticmethod
    def CancelDownloadJob(nToken: _n_8_t_12):...
class AppMenuUtil(object):
    def __init__(self) -> AppMenuUtil:...
    @staticmethod
    def IsApplicationRegistered(appName: str) -> bool:...
    @staticmethod
    def OpenDocument(fileName: str):...
class AttachUtil(_n_8_t_11):
    def __init__(self) -> AttachUtil:...
    @staticmethod
    def CheckDwgFile(csDwgPath: str) -> bool:...
    @staticmethod
    def CheckImageFile(csImagePath: str) -> bool:...
    @staticmethod
    def CmdLineImageAttach(strImageFile: str):...
    @staticmethod
    def CmdLineNavisworksAttach(strNavisworksFile: str):...
    @staticmethod
    def CmdLinePointCloudAttach(strPointCloudFile: str):...
    @staticmethod
    def CmdLineXAttach(strDWGFile: str) -> bool:...
    @staticmethod
    def GetImageFileExtensions() -> str:...
    @staticmethod
    def GetImageFilterString() -> str:...
    @staticmethod
    def GetOpenFilesResult(opt: _n_3_t_0, multiSelArray: _n_8_t_13[str]) -> _n_8_t_13[str]:...
    @staticmethod
    def ImageAdjust(objIds: _n_8_t_13[_n_2_t_0]):...
    @staticmethod
    def ImageAttach(strImageFile: str):...
    @staticmethod
    def ImageClip(objId: _n_2_t_0):...
    @staticmethod
    def isDialogShow() -> bool:...
    @staticmethod
    def IsPCAttachAllowed() -> bool:...
    @staticmethod
    def LoadBIMUnderlayArx():...
    @staticmethod
    def LoadBIMUnderlayCrx():...
    @staticmethod
    def LoadISM():...
    @staticmethod
    def LoadPointCloudArx():...
    @staticmethod
    def LoadPointCloudCrx():...
    @staticmethod
    def NavisworksAttach(strNavisworksFile: str):...
    @staticmethod
    def PointCloudAttach(strPointCloudFile: str):...
    @staticmethod
    def PointCloudClip(objId: _n_2_t_0):...
    @staticmethod
    def VPClip():...
    @staticmethod
    def XAttach(strDWGFileArray: _n_8_t_13[str]):...
    @staticmethod
    def XClip():...
class CipUtils(object):
    def getMacroString(self, macro: str) -> str:...
    @staticmethod
    def Instance() -> CipUtils:...
    def IsOperational(self) -> bool:...
    def LogApplicationMenuCommandExecute(self, id: str, sCmd: str):...
    def LogIcLaunch(self, icType: int, group: str, category: str, title: str, url: str):...
    def LogIcQuery(self, queryString: str, buttonIndex: int):...
    def LogModelessLayerItem(self, cmdStr: str, bInRibbon: bool):...
    def LogQuickAccessToolbarCommandExecute(self, id: str, sCmd: str):...
    def LogRibbonItemCommandExecute(self, sCmd: str, sTabName: str, sPanelName: str, bMenuMacro: bool, dockSide: int):...
    def LogStatusBarElementVisibility(self, elementName: str, isVisible: bool):...
    def SetUaLaunchType(self, uaLaunchType: str):...
    def WaypointReachedWithStringAtt(self, waypoint: str, state: str, att: str, strAttValue: str):...
class CloudPrintingServiceManager(object):
    @property
    def Host(self) -> ICloudPrintingService:"""Host { get; set; } -> ICloudPrintingService"""
    def __init__(self) -> CloudPrintingServiceManager:...
class ColorThemeChangedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> ColorThemeChangedEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_8_t_14, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: object, e: _n_8_t_14):...
class ColorThemeEnum(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    Dark: int
    Light: int
    User: int
    value__: int
class ComboBoxWrapper(_n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    @property
    def SelectionChanged(self) -> _n_8_t_15:
        """SelectionChanged Event: EventHandler"""
class CommandCallback(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> CommandCallback:...
    def BeginInvoke(self, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self):...
class CommandPiper(_n_8_t_11):
    @property
    def BlockingCommands(self) -> int:"""BlockingCommands { get; set; } -> int"""
    @property
    def LayerCount(self) -> int:"""LayerCount { get; set; } -> int"""
    @property
    def QueueCount(self) -> int:"""QueueCount { get; } -> int"""
    def __init__(self, layerMgrCtrlId: int, bInRibbon: bool) -> CommandPiper:...
    def __init__(self) -> CommandPiper:...
    @staticmethod
    def CommandsSentButNotStartedClear():...
    @staticmethod
    def CommandWillStart(layerMgrCtrlId: int) -> bool:...
    @staticmethod
    def GetRegenLayers(layerIds: _n_2_t_1) -> int:...
    @staticmethod
    def IsBlockingCommand(cmdName: str) -> bool:...
    def LayerClose(self):...
    def LayerColor(self, value: _n_1_t_0, layerName: str) -> bool:...
    def LayerColor(self, value: _n_1_t_0, layerNames: _n_9_t_0) -> bool:...
    def LayerCurrent(self, layerName: str):...
    def LayerDelete(self, layerName: str):...
    def LayerDelete(self, layerNames: _n_9_t_0):...
    def LayerDescription(self, value: str, existingValueEmpty: bool, layerName: str):...
    def LayerDescription(self, value: str, existingValueEmpty: bool, layerNames: _n_9_t_0):...
    def LayerFilterDelete(self, filtersNames: _n_9_t_0):...
    def LayerFilterEditGroup(self, add: bool, filterName: str, layerName: str):...
    def LayerFilterEditGroup(self, add: bool, filterName: str, layerNames: _n_9_t_0):...
    def LayerFilterEditGroupReplace(self, filterName: str, parentName: str, layerNames: _n_9_t_0):...
    def LayerFilterEditPropertyConvert(self, filterName: str):...
    def LayerFilterEditPropertyDef(self, filterName: str, filterExpression: str):...
    def LayerFilterNewGroup(self, filterName: str, parentName: str):...
    def LayerFilterNewProperty(self, filterName: str, filterExpression: str, parentName: str):...
    def LayerFilterRename(self, value: str, filterName: str):...
    def LayerFilterSet(self, filterName: str):...
    def LayerFrozen(self, value: bool, layerName: str, layerId: _n_2_t_0):...
    def LayerFrozen(self, value: bool, layerNames: _n_9_t_0, layerIds: _n_2_t_1):...
    def LayerLinetype(self, value: str, layerName: str):...
    def LayerLinetype(self, value: str, layerNames: _n_9_t_0):...
    def LayerLineWeight(self, value: _n_2_t_2, layerName: str):...
    def LayerLineWeight(self, value: _n_2_t_2, layerNames: _n_9_t_0):...
    def LayerLocked(self, value: bool, layerName: str):...
    def LayerLocked(self, value: bool, layerNames: _n_9_t_0):...
    def LayerNew(self, layerName: str):...
    def LayerOffCurrent(self, layerName: str):...
    def LayerOn(self, value: bool, layerName: str):...
    def LayerOn(self, value: bool, layerNames: _n_9_t_0):...
    def LayerPlot(self, value: bool, layerName: str):...
    def LayerPlot(self, value: bool, layerNames: _n_9_t_0):...
    def LayerPlotStyle(self, value: str, layerName: str):...
    def LayerPlotStyle(self, value: str, layerNames: _n_9_t_0):...
    def LayerReconcile(self, layerName: str):...
    def LayerReconcile(self, layerNames: _n_9_t_0):...
    def LayerRename(self, value: str, layerName: str):...
    def LayerTemplate(self, protoName: str, layerName: str, showUsed: bool, freezeInAllVPs: bool):...
    def LayerTransparency(self, value: str, layerName: str):...
    def LayerTransparency(self, value: str, layerNames: _n_9_t_0):...
    @staticmethod
    def OnCommandEnded() -> bool:...
    @staticmethod
    def QueueClear():...
    @staticmethod
    def QueueSend():...
    def Send(self):...
    @staticmethod
    def SkipUpdate() -> bool:...
    def VplayerColor(self, value: _n_1_t_0, all: bool, layerName: str) -> bool:...
    def VplayerColor(self, value: _n_1_t_0, all: bool, layerNames: _n_9_t_0) -> bool:...
    def VplayerFrozen(self, value: bool, flag: CommandPiper.VPType, layerName: str, layerId: _n_2_t_0):...
    def VplayerFrozen(self, value: bool, flag: CommandPiper.VPType, layerNames: _n_9_t_0, layerIds: _n_2_t_1):...
    def VplayerLinetype(self, value: str, all: bool, layerName: str):...
    def VplayerLinetype(self, value: str, all: bool, layerNames: _n_9_t_0):...
    def VplayerLineWeight(self, value: _n_2_t_2, all: bool, layerName: str):...
    def VplayerLineWeight(self, value: _n_2_t_2, all: bool, layerNames: _n_9_t_0):...
    def VplayerPlotStyle(self, value: str, all: bool, layerName: str):...
    def VplayerPlotStyle(self, value: str, all: bool, layerNames: _n_9_t_0):...
    def VplayerRemoveOverrides(self, theProperty: str, all: bool, layerName: str):...
    def VplayerRemoveOverrides(self, theProperty: str, all: bool, layerNames: _n_9_t_0):...
    def VplayerReset(self, all: bool, layerName: str):...
    def VplayerReset(self, all: bool, layerNames: _n_9_t_0):...
    def VplayerTransparency(self, value: str, all: bool, layerName: str):...
    def VplayerTransparency(self, value: str, all: bool, layerNames: _n_9_t_0):...
    def VplayerViewportVisibilityDefault(self, bFrozen: bool, all: bool, layerName: str):...
    def VplayerViewportVisibilityDefault(self, bFrozen: bool, all: bool, layerNames: _n_9_t_0):...
    class VPType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        kVPAll: int
        kVPAllButCurrent: int
        kVPCurrent: int
        kVPNone: int
        value__: int
class CommandTypeFlags(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    ActionMacroCmd: int
    ARXCmd: int
    CoreCmd: int
    LispCmd: int
    NoneCmd: int
    SetvarCmd: int
    value__: int
class CompareReturnStatus(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    HistoryCompare: int
    RawBinaryCompare: int
    UnableToCompare: int
    value__: int
class ContentSearchUtils(object):
    def __init__(self) -> ContentSearchUtils:...
    @staticmethod
    def PerformContentSearch(keyword: str):...
class CoreLayerUtilities(object):
    @property
    def RegenPending(self) -> int:"""RegenPending { get; } -> int"""
    @staticmethod
    def LayerNameCompareNatural(str1: str, str2: str) -> int:...
    @staticmethod
    def RegenLayers(layers: _n_8_t_13[_n_2_t_0], regenPending: int):...
    @staticmethod
    def RegenLayers(layers: _n_8_t_13[_n_2_t_0], regenPending: int, regenRequired: int):...
class CoreUtils(object):
    def __init__(self) -> CoreUtils:...
    @staticmethod
    def GraphScr():...
    @staticmethod
    def SetUndoRequiresRegen(db: _n_2_t_3) -> bool:...
    @staticmethod
    def TextScr():...
    @staticmethod
    def WcMatch(str: str, pattern: str) -> bool:...
class COwnerDrawComboBoxWrapper(_n_21_t_5, _n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    pass
class CSyncManagerReactorImpl(_n_8_t_10):
    pass
class CustomizationUtilities(object):
    @staticmethod
    def SetCustomizationInterface(customization: object):...
class DataSyncError(_n_6_t_0, _n_8_t_11):
    def GetSettingId(self) -> str:...
class DataSyncManager(_n_6_t_0, _n_8_t_11):
    @property
    def IsBackupAvailable(self) -> bool:"""IsBackupAvailable { get; } -> bool"""
    @property
    def State(self) -> DataSyncState:"""State { get; } -> DataSyncState"""
    @property
    def DownloadBegin(self) -> SyncStateChangedEventHandler:
        """DownloadBegin Event: SyncStateChangedEventHandler"""
    @property
    def DownloadEnd(self) -> SyncStateChangedEventHandler:
        """DownloadEnd Event: SyncStateChangedEventHandler"""
    @property
    def ErrorsOccured(self) -> SyncStateChangedEventHandler:
        """ErrorsOccured Event: SyncStateChangedEventHandler"""
    @property
    def LoggedIn(self) -> SyncStateChangedEventHandler:
        """LoggedIn Event: SyncStateChangedEventHandler"""
    @property
    def LoggedOut(self) -> SyncStateChangedEventHandler:
        """LoggedOut Event: SyncStateChangedEventHandler"""
    @property
    def SettingsLoaded(self) -> SyncStateChangedEventHandler:
        """SettingsLoaded Event: SyncStateChangedEventHandler"""
    @property
    def SettingsReady(self) -> SyncStateChangedEventHandler:
        """SettingsReady Event: SyncStateChangedEventHandler"""
    @property
    def SyncStatusUpdated(self) -> SyncStatusChangedEventHandler:
        """SyncStatusUpdated Event: SyncStatusChangedEventHandler"""
    @property
    def UploadBegin(self) -> SyncStateChangedEventHandler:
        """UploadBegin Event: SyncStateChangedEventHandler"""
    @property
    def UploadEnd(self) -> SyncStateChangedEventHandler:
        """UploadEnd Event: SyncStateChangedEventHandler"""
    def BackupPreviousSettings(self) -> bool:...
    def DeleteBackupSettings(self) -> bool:...
    def DisableSync(self) -> bool:...
    def EnableSync(self) -> bool:...
    def FireDownloadBeginEvent(self):...
    def FireDownloadEndEvent(self):...
    def FireErrorsOccuredEvent(self):...
    def FireLoggedInEvent(self):...
    def FireLoggedOutEvent(self):...
    def FireSettingsLoadedEvent(self):...
    def FireSettingsReadyEvent(self):...
    def FireSyncStatusUpdatedEvent(self, status: SyncStatus):...
    def FireUploadBeginEvent(self):...
    def FireUploadEndEvent(self):...
    def GetErrors(self) -> _n_11_t_0[DataSyncError]:...
    @staticmethod
    def GetManager() -> DataSyncManager:...
    def IsCustomizationDataAvailableInCloud(self) -> bool:...
    def IsCustomizationDataAvailableInSyncFolder(self) -> bool:...
    def IsCustomizationDataUpdated(self) -> bool:...
    def IsLoggedIn(self) -> bool:...
    def LoadCustomSettings(self):...
    def RestorePreviousSettings(self) -> bool:...
    def SyncNow(self) -> bool:...
    def SyncSettingsFirstTime(self) -> bool:...
    def TriggerUpdate(self, settingId: str) -> bool:...
    def ViewOnlineAccount(self):...
class DataSyncState(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    Idle: int
    PendingApplyCloudSettings: int
    PendingDownload: int
    value__: int
class DebugUtil(object):
    def __init__(self) -> DebugUtil:...
    @staticmethod
    def Assert(condition: bool):...
    @staticmethod
    def Assert(condition: bool, message: str):...
    @staticmethod
    def Assert(condition: bool, message: str, detailMessage: str):...
    @staticmethod
    def Verify(b: bool) -> bool:...
    @staticmethod
    def Verify(b: bool, t: str) -> bool:...
class DocumentWindowUtil(object):
    def __init__(self) -> DocumentWindowUtil:...
    @staticmethod
    def CanClose(docWindow: _n_7_t_0) -> bool:...
    @staticmethod
    def SetNextActiveWindow(docWindow: _n_7_t_0):...
class DrawingCompare(object):
    m_ObjectDiffEvent: int
    @property
    def ObjectDiffEvent(self) -> ObjectDiffEventHandler:
        """ObjectDiffEvent Event: ObjectDiffEventHandler"""
    def __init__(self) -> DrawingCompare:...
    def CompareDwgFiles(self, file1name: str, file2name: str) -> CompareReturnStatus:...
    def OnDiffDetected(self, drawingId: int, handle: _n_8_t_16, changeType: int):...
class DxLegacyBinaryTemplate(object):
    @property
    def AttributeList(self) -> _n_9_t_0:"""AttributeList { get; } -> ArrayList"""
    @property
    def BlockList(self) -> _n_9_t_0:"""BlockList { get; } -> ArrayList"""
    def __init__(self) -> DxLegacyBinaryTemplate:...
    def LoadFromFile(self, filename: str):...
class FocusChangedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> FocusChangedEventHandler:...
    def BeginInvoke(self, sender: GroupControl, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: GroupControl):...
class GroupControl(_n_21_t_6, _n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    @property
    def HeaderHeight(self) -> int:"""HeaderHeight { get; set; } -> int"""
    @property
    def Hidden(self) -> bool:"""Hidden { get; set; } -> bool"""
    @property
    def Minimized(self) -> bool:"""Minimized { get; set; } -> bool"""
    @property
    def RestoredHeight(self) -> int:"""RestoredHeight { get; set; } -> int"""
    @property
    def Title(self) -> str:"""Title { get; set; } -> str"""
    @property
    def UseDialogTheme(self) -> bool:"""UseDialogTheme { get; set; } -> bool"""
    @property
    def FocusChanged(self) -> FocusChangedEventHandler:
        """FocusChanged Event: FocusChangedEventHandler"""
    @property
    def HiddenChanged(self) -> HiddenChangedEventHandler:
        """HiddenChanged Event: HiddenChangedEventHandler"""
    def __init__(self) -> GroupControl:...
    def AddStyle(self, styleAdd: GroupControlStyles):...
    def AddTitleButton(self, button: GroupControlHeaderButton) -> bool:...
    def RemoveBitmap(self, button: GroupControlHeaderButton) -> bool:...
    def RemoveStyle(self, styleRemove: GroupControlStyles):...
    def SetActive(self, bActive: bool):...
class GroupControlEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> GroupControlEventHandler:...
    def BeginInvoke(self, sender: object, e: _n_8_t_14, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: object, e: _n_8_t_14):...
class GroupControlEventIndex(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    ChevronClick: int
    FocusChange: int
    Hide: int
    Resize: int
    Show: int
    TitleButtonClick: int
    value__: int
class GroupControlHeaderButton(_n_8_t_11):
    @property
    def Bitmap(self) -> _n_14_t_1:"""Bitmap { get; set; } -> Bitmap"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    @property
    def Parent(self) -> GroupControl:"""Parent { get; set; } -> GroupControl"""
    @property
    def ToolTip(self) -> str:"""ToolTip { get; set; } -> str"""
    @property
    def Click(self) -> _n_8_t_15:
        """Click Event: EventHandler"""
    def __init__(self, bmp: _n_14_t_1, tooltip: str) -> GroupControlHeaderButton:...
    def __init__(self) -> GroupControlHeaderButton:...
class GroupControlStyles(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    ShowButtonBorder: int
    ShowButtonForce: int
    ShowChevron: int
    ShowNoBorder: int
    ShowNonActive: int
    ShowOpaqueImage: int
    ShowTransparentButton: int
    value__: int
class GroupResizedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> GroupResizedEventHandler:...
    def BeginInvoke(self, sender: GroupControl, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: GroupControl):...
class HiddenChangedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> HiddenChangedEventHandler:...
    def BeginInvoke(self, sender: GroupControl, bHidden: bool, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: GroupControl, bHidden: bool):...
class HPPrinter(object):
    @property
    def HPUserId(self) -> str:"""HPUserId { get; set; } -> str"""
    @property
    def PrinterId(self) -> str:"""PrinterId { get; set; } -> str"""
    @property
    def PrinterName(self) -> str:"""PrinterName { get; set; } -> str"""
    @property
    def WSUserId(self) -> str:"""WSUserId { get; set; } -> str"""
    def __init__(self) -> HPPrinter:...
class HPPrinterPlotOption(object):
    @property
    def Copies(self) -> int:"""Copies { get; set; } -> int"""
    @property
    def Quality(self) -> HPPrinterPlotQuality:"""Quality { get; set; } -> HPPrinterPlotQuality"""
    def __init__(self) -> HPPrinterPlotOption:...
class HPPrinterPlotQuality(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    Best: int
    Fast: int
    Normal: int
    value__: int
class HPPrinterPlotResult(object):
    @property
    def Code(self) -> str:"""Code { get; set; } -> str"""
    @property
    def Message(self) -> str:"""Message { get; set; } -> str"""
    @property
    def Status(self) -> int:"""Status { get; set; } -> int"""
    def __init__(self) -> HPPrinterPlotResult:...
class HttpMethod(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    Delete: int
    Get: int
    Head: int
    Post: int
    Put: int
    value__: int
class ICloudPrintingService():
    def ListHPPrinters(self) -> _n_8_t_13[HPPrinter]:...
    def PlotHPPrinter(self, pdfFilePath: str, printer: HPPrinter, option: HPPrinterPlotOption) -> HPPrinterPlotResult:...
    def ShowHPUserLoginDialog(self) -> bool:...
class ILivePreviewControl(IPreviewContext):
    @property
    def ControlType(self) -> PreviewControlType:"""ControlType { get; set; } -> PreviewControlType"""
    @property
    def PreviewDelay(self) -> int:"""PreviewDelay { get; set; } -> int"""
    @property
    def Rule(self) -> str:"""Rule { get; set; } -> str"""
class ILivePreviewRule():
    @property
    def IsPreviewAble(self) -> bool:"""IsPreviewAble { get; } -> bool"""
class INavisworksFileProtocol():
    def CloseFile(self, filehandle: _n_8_t_0):...
    def GetAggregateInfo(self, filename: str, aggregateJson: str) -> NavisworksFileType:...
    def GetFileInfo(self, filename: str) -> NavisworksFileInfo:...
    def OpenFile(self, filename: str) -> _n_8_t_0:...
    def ReadFile(self, filehandle: _n_8_t_0, offset: _n_8_t_16, numbytes: _n_8_t_16, bytes: _n_8_t_13[_n_8_t_17]) -> bool:...
class INavisworksService():
    def RegisterFileProtocol(self, scheme: str, fileprotocol: INavisworksFileProtocol):...
class IPECallbackType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPECallbackCreateToolbar: int
    IPECallbackCreateUI: int
    IPECallbackEnableUI: int
    IPECallbackRemoveToolbar: int
    IPECallbackRemoveUI: int
    IPECallbackUpdateUI: int
    value__: int
class IPECharFlags(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    BoldFlag: int
    ColorFlag: int
    FlowAlignFlag: int
    FontFlag: int
    HeightFlag: int
    ItalicFlag: int
    LanguageFlag: int
    ObliqueAngleFlag: int
    OverlineFlag: int
    TrackingFactorFlag: int
    UnderlineFlag: int
    value__: int
    WidthScaleFlag: int
class IPECharFlowType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    FlowBase: int
    FlowCenter: int
    FlowTop: int
    value__: int
class IPECharStateWrapper(_n_6_t_0, _n_8_t_11, _n_8_t_7):
    @property
    def Bold(self) -> bool:"""Bold { get; set; } -> bool"""
    @property
    def Color(self) -> _n_1_t_0:"""Color { get; set; } -> Color"""
    @property
    def Flags(self) -> IPECharFlags:"""Flags { get; set; } -> IPECharFlags"""
    @property
    def FlowAlign(self) -> IPECharFlowType:"""FlowAlign { get; set; } -> IPECharFlowType"""
    @property
    def FontName(self) -> str:"""FontName { get; set; } -> str"""
    @property
    def Height(self) -> float:"""Height { get; set; } -> float"""
    @property
    def Italic(self) -> bool:"""Italic { get; set; } -> bool"""
    @property
    def Language(self) -> int:"""Language { get; set; } -> int"""
    @property
    def ObliqueAngle(self) -> float:"""ObliqueAngle { get; set; } -> float"""
    @property
    def Overline(self) -> bool:"""Overline { get; set; } -> bool"""
    @property
    def TrackingFactor(self) -> float:"""TrackingFactor { get; set; } -> float"""
    @property
    def TrueType(self) -> bool:"""TrueType { get; set; } -> bool"""
    @property
    def Underline(self) -> bool:"""Underline { get; set; } -> bool"""
    @property
    def WidthScale(self) -> float:"""WidthScale { get; set; } -> float"""
    def __init__(self) -> IPECharStateWrapper:...
class IPEColumnCommandType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPEColumnSettingsCommand: int
    IPEDynamicColumnsCommand: int
    IPEInsertColumnBreakCommand: int
    IPEMoreStaticColumnsCommand: int
    IPENoColumnsCommand: int
    IPEStaticColumnsCommand: int
    value__: int
class IPECommands(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPEAttachmentMenuCmd: int
    IPEChangeCaseCmd: int
    IPECloseCmd: int
    IPEColumnsMenuCmd: int
    IPEContextMenuCmd: int
    IPEFieldDialogCmd: int
    IPEHandleColumnsCmd: int
    IPEHandleJustificationCmd: int
    IPEHandleLineSpacingCmd: int
    IPEHandleNumberingCmd: int
    IPEHandleOptionsCmd: int
    IPEHandleSymbolCmd: int
    IPEInsertCustomStringCmd: int
    IPEInsertMTextCmd: int
    IPELineSpacingMenuCmd: int
    IPENumberingMenuCmd: int
    IPEParagraphDialogCmd: int
    IPERedoCmd: int
    IPEReinstateEditorCmd: int
    IPERemoveCustomStringCmd: int
    IPEReplaceContentsCmd: int
    IPESetColorCmd: int
    IPESetCustomStringCmd: int
    IPESetFontCmd: int
    IPESetObliqueAngleCmd: int
    IPESetParagraphAlignmentCmd: int
    IPESetStyleCmd: int
    IPESetTextHeightCmd: int
    IPESetTrackingFactorCmd: int
    IPESetWidthScaleCmd: int
    IPEStackCmd: int
    IPESuspendEditorCmd: int
    IPESymbolMenuCmd: int
    IPEToggleAnnotativeCmd: int
    IPEToggleBoldCmd: int
    IPEToggleDimAlternateCmd: int
    IPEToggleDimParenthesesCmd: int
    IPEToggleDimPrimaryCmd: int
    IPEToggleDimUnderlineCmd: int
    IPEToggleItalicCmd: int
    IPEToggleOverlineCmd: int
    IPEToggleRulerCmd: int
    IPEToggleUnderlineCmd: int
    IPETweakDimensionCmd: int
    IPEUndoCmd: int
    IPEUnknownCmd: int
    value__: int
class IPEConstants(object):
    IPEAcctachmentInfo: int
    IPECharsetInfo: int
    IPEColumnAutoHeightInfo: int
    IPEColumnCounts: int
    IPEColumnTypeInfo: int
    IPELineSpacingMultiples: int
    IPEParaAlignmentInfo: int
    IPESymbolInfo: int
    def __init__(self) -> IPEConstants:...
class IPEControlIconType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPEBoldButtonIcon: int
    IPEItalicButtonIcon: int
    IPEObliqueAngleSpinnerIcon: int
    IPEOverlineButtonIcon: int
    IPEUnderlineButtonIcon: int
    value__: int
class IPEDimensionStateWrapper(_n_6_t_0, _n_8_t_11, _n_8_t_7):
    @property
    def AlternateFound(self) -> bool:"""AlternateFound { get; set; } -> bool"""
    @property
    def Dimension(self) -> _n_2_t_4:"""Dimension { get; set; } -> Dimension"""
    @property
    def EnclosedWithParentheses(self) -> bool:"""EnclosedWithParentheses { get; set; } -> bool"""
    @property
    def EverythingUnderlined(self) -> bool:"""EverythingUnderlined { get; set; } -> bool"""
    @property
    def PrimaryFound(self) -> bool:"""PrimaryFound { get; set; } -> bool"""
    def __init__(self) -> IPEDimensionStateWrapper:...
class IPEExitType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    ExitQuit: int
    ExitSave: int
    ExitSaveAndGoAbove: int
    ExitSaveAndGoBelow: int
    ExitSaveAndGoLeft: int
    ExitSaveAndGoRight: int
    value__: int
class IPELineSpacingCommandType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPEClearLineSpaceCommand: int
    IPEMoreLineSpaceCommand: int
    IPEMultiLineSpaceCommand: int
    value__: int
class IPELineSpacingStyle(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    LineSpacingAtLeast: int
    LineSpacingDefault: int
    LineSpacingExactly: int
    LineSpacingMultiple: int
    NumLineSpacingStyles: int
    value__: int
class IPENumberingCommandType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPENumberingAutoListCommand: int
    IPENumberingBulletCommand: int
    IPENumberingContinueCommand: int
    IPENumberingEnabledCommand: int
    IPENumberingLetterLowCaseCommand: int
    IPENumberingLetterUpperCaseCommand: int
    IPENumberingNumberedCommand: int
    IPENumberingOffCommand: int
    IPENumberingRestartCommand: int
    IPENumberingTabOnlyDelimiterCommand: int
    value__: int
class IPENumberingType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    NumberingBullet: int
    NumberingLetterLower: int
    NumberingLetterUpper: int
    NumberingNumber: int
    NumberingNumTypes: int
    NumberingOff: int
    value__: int
class IPEOptionsCommandType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPEAutoCAPSCommand: int
    IPEBackgroundMaskCommand: int
    IPECharaterSetCommand: int
    IPECheckSpellingCommand: int
    IPECheckSpellingSettingsCommand: int
    IPECombineParagraphsCommand: int
    IPEConvertCustomCommand: int
    IPEConvertFieldCommand: int
    IPEDictionariesCommand: int
    IPEEditFieldCommand: int
    IPEFindReplaceCommand: int
    IPEHelpCommand: int
    IPEImportTextCommand: int
    IPEInsertFieldCommand: int
    IPELowerCaseCommand: int
    IPENewFeaturesCommand: int
    IPEOpaqueBackgroundCommand: int
    IPEParagraphAlignCommand: int
    IPEParagraphCommand: int
    IPERemoveAllFormattingCommand: int
    IPERemoveCharaterFormattingCommand: int
    IPERemoveParagraphFormattingCommand: int
    IPEShowOptionsCommand: int
    IPEShowRibbonCommand: int
    IPEShowRulerCommand: int
    IPEShowToolbarCommand: int
    IPEStackCommand: int
    IPEStackPropertyCommand: int
    IPETextHeightlightColorCommand: int
    IPEUnstackCommand: int
    IPEUpdateFieldCommand: int
    IPEUpperCaseCommand: int
    IPEWYSIWYGCommand: int
    value__: int
class IPEParagraphAlignmentType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    AlignmentCenter: int
    AlignmentDefault: int
    AlignmentDistribute: int
    AlignmentJustify: int
    AlignmentLeft: int
    AlignmentRight: int
    NumAlignmentTypes: int
    value__: int
class IPEParagraphFlags(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    AlignmentFlag: int
    FirstIndentFlag: int
    LeftIndentFlag: int
    LineSpacingFlag: int
    NumberingFlag: int
    RightIndentFlag: int
    SpaceAfterFlag: int
    SpaceBeforeFlag: int
    value__: int
class IPEParagraphStateWrapper(_n_6_t_0, _n_8_t_11, _n_8_t_7):
    @property
    def Alignment(self) -> IPEParagraphAlignmentType:"""Alignment { get; set; } -> IPEParagraphAlignmentType"""
    @property
    def AutoListEnabled(self) -> bool:"""AutoListEnabled { get; } -> bool"""
    @property
    def FirstIndent(self) -> float:"""FirstIndent { get; set; } -> float"""
    @property
    def Flags(self) -> IPEParagraphFlags:"""Flags { get; set; } -> IPEParagraphFlags"""
    @property
    def LeftIndent(self) -> float:"""LeftIndent { get; set; } -> float"""
    @property
    def LineSpacingFactor(self) -> float:"""LineSpacingFactor { get; set; } -> float"""
    @property
    def LineSpacingStyle(self) -> IPELineSpacingStyle:"""LineSpacingStyle { get; set; } -> IPELineSpacingStyle"""
    @property
    def NumberingType(self) -> IPENumberingType:"""NumberingType { get; set; } -> IPENumberingType"""
    @property
    def RightIndent(self) -> float:"""RightIndent { get; set; } -> float"""
    @property
    def SpaceAfter(self) -> float:"""SpaceAfter { get; set; } -> float"""
    @property
    def SpaceBefore(self) -> float:"""SpaceBefore { get; set; } -> float"""
    @property
    def TabOnlyDelimitedEnabled(self) -> bool:"""TabOnlyDelimitedEnabled { get; } -> bool"""
    def __init__(self) -> IPEParagraphStateWrapper:...
class IPESettingsWrapper(_n_6_t_0, _n_8_t_11, _n_8_t_7):
    @property
    def AllowTabs(self) -> bool:"""AllowTabs { get; set; } -> bool"""
    @property
    def AuthoringEntity(self) -> bool:"""AuthoringEntity { get; set; } -> bool"""
    @property
    def DefinedHeight(self) -> float:"""DefinedHeight { get; set; } -> float"""
    @property
    def Dimension(self) -> bool:"""Dimension { get; set; } -> bool"""
    @property
    def DimensionObject(self) -> _n_2_t_4:"""DimensionObject { get; set; } -> Dimension"""
    @property
    def DimensionScale(self) -> float:"""DimensionScale { get; set; } -> float"""
    @property
    def EditFlags(self) -> int:"""EditFlags { get; set; } -> int"""
    @property
    def HorizontalMargin(self) -> float:"""HorizontalMargin { get; set; } -> float"""
    @property
    def InputString(self) -> str:"""InputString { get; set; } -> str"""
    @property
    def MultilineAttribute(self) -> bool:"""MultilineAttribute { get; set; } -> bool"""
    @property
    def RotateForFont(self) -> bool:"""RotateForFont { get; set; } -> bool"""
    @property
    def SimpleMText(self) -> bool:"""SimpleMText { get; set; } -> bool"""
    @property
    def TableCell(self) -> bool:"""TableCell { get; set; } -> bool"""
    @property
    def TableId(self) -> _n_2_t_0:"""TableId { get; set; } -> ObjectId"""
    @property
    def ToolbarRectangle(self) -> _n_8_t_10:"""ToolbarRectangle { get; set; } -> ValueType"""
    @property
    def VerticalMargin(self) -> float:"""VerticalMargin { get; set; } -> float"""
    def __init__(self) -> IPESettingsWrapper:...
class IPEStateWrapper(_n_6_t_0, _n_8_t_11, _n_8_t_7):
    @property
    def Annotative(self) -> bool:"""Annotative { get; set; } -> bool"""
    @property
    def AnnotativeAvailable(self) -> bool:"""AnnotativeAvailable { get; set; } -> bool"""
    @property
    def AutoCapsEnabled(self) -> bool:"""AutoCapsEnabled { get; } -> bool"""
    @property
    def AutoHeightColumns(self) -> bool:"""AutoHeightColumns { get; } -> bool"""
    @property
    def ChangeCaseAvailable(self) -> bool:"""ChangeCaseAvailable { get; set; } -> bool"""
    @property
    def CharState(self) -> IPECharStateWrapper:"""CharState { get; set; } -> IPECharStateWrapper"""
    @property
    def ColumnsAvailable(self) -> bool:"""ColumnsAvailable { get; set; } -> bool"""
    @property
    def CopyAvailable(self) -> bool:"""CopyAvailable { get; set; } -> bool"""
    @property
    def DefinedWidth(self) -> float:"""DefinedWidth { get; } -> float"""
    @property
    def Dimension(self) -> bool:"""Dimension { get; } -> bool"""
    @property
    def DimensionState(self) -> IPEDimensionStateWrapper:"""DimensionState { get; set; } -> IPEDimensionStateWrapper"""
    @property
    def EmptySelection(self) -> bool:"""EmptySelection { get; } -> bool"""
    @property
    def FieldsAvailable(self) -> bool:"""FieldsAvailable { get; set; } -> bool"""
    @property
    def ForceOpaqueBackground(self) -> bool:"""ForceOpaqueBackground { get; } -> bool"""
    @property
    def HideOptions(self) -> bool:"""HideOptions { get; } -> bool"""
    @property
    def HideToolbar(self) -> bool:"""HideToolbar { get; } -> bool"""
    @property
    def IPEColumnType(self) -> _n_2_t_5:"""IPEColumnType { get; } -> ColumnType"""
    @property
    def IsAuthoringEntity(self) -> bool:"""IsAuthoringEntity { get; } -> bool"""
    @property
    def IsDText(self) -> bool:"""IsDText { get; } -> bool"""
    @property
    def IsSimpleMText(self) -> bool:"""IsSimpleMText { get; } -> bool"""
    @property
    def Justification(self) -> _n_2_t_6:"""Justification { get; } -> AttachmentPoint"""
    @property
    def LanguageIndex(self) -> int:"""LanguageIndex { get; } -> int"""
    @property
    def LayerColor(self) -> _n_24_t_0:"""LayerColor { get; } -> Color"""
    @property
    def MTextFixed(self) -> int:"""MTextFixed { get; } -> int"""
    @property
    def NumberingAvailable(self) -> bool:"""NumberingAvailable { get; set; } -> bool"""
    @property
    def OpaqueBackground(self) -> bool:"""OpaqueBackground { get; } -> bool"""
    @property
    def ParaAttsAvailable(self) -> bool:"""ParaAttsAvailable { get; set; } -> bool"""
    @property
    def ParagraphState(self) -> IPEParagraphStateWrapper:"""ParagraphState { get; set; } -> IPEParagraphStateWrapper"""
    @property
    def PasteAvailable(self) -> bool:"""PasteAvailable { get; set; } -> bool"""
    @property
    def QuickStartLinkAvailable(self) -> bool:"""QuickStartLinkAvailable { get; } -> bool"""
    @property
    def RedoAvailable(self) -> bool:"""RedoAvailable { get; set; } -> bool"""
    @property
    def RibbonOn(self) -> bool:"""RibbonOn { get; } -> bool"""
    @property
    def RulerAvailable(self) -> bool:"""RulerAvailable { get; set; } -> bool"""
    @property
    def RulerVisible(self) -> bool:"""RulerVisible { get; set; } -> bool"""
    @property
    def SingleCustom(self) -> bool:"""SingleCustom { get; } -> bool"""
    @property
    def SingleField(self) -> bool:"""SingleField { get; } -> bool"""
    @property
    def SpellingEnabled(self) -> bool:"""SpellingEnabled { get; } -> bool"""
    @property
    def StackAvailable(self) -> bool:"""StackAvailable { get; set; } -> bool"""
    @property
    def StaticColumnsCount(self) -> int:"""StaticColumnsCount { get; } -> int"""
    @property
    def StyleId(self) -> _n_2_t_0:"""StyleId { get; set; } -> ObjectId"""
    @property
    def StyleName(self) -> str:"""StyleName { get; set; } -> str"""
    @property
    def TableCell(self) -> bool:"""TableCell { get; } -> bool"""
    @property
    def UndoAvailable(self) -> bool:"""UndoAvailable { get; set; } -> bool"""
    @property
    def UnstackAvailable(self) -> bool:"""UnstackAvailable { get; set; } -> bool"""
    @property
    def VerticalSHX(self) -> bool:"""VerticalSHX { get; set; } -> bool"""
    def __init__(self) -> IPEStateWrapper:...
class IPESymbolCommandType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    IPECustomSymbolCommand: int
    IPEStandardSymbolCommand: int
    value__: int
class IPETableFlags(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    CursorAtEndFlag: int
    DisableAutoStackFlag: int
    kForceNoUIWhenScript: int
    SelectAllFlag: int
    StartInOpaqueBackground: int
    TableFlipFlag: int
    TableGoAboveFlag: int
    TableGoBelowFlag: int
    TableGoLeftFlag: int
    TableGoRightFlag: int
    TableSubsequentCellFlag: int
    value__: int
class IPETestingEventArgs(_n_8_t_14):
    @property
    def Data(self) -> object:"""Data { get; } -> object"""
    def __init__(self, data: object) -> IPETestingEventArgs:...
class IPETestingHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> IPETestingHandler:...
    def BeginInvoke(self, sender: object, e: IPETestingEventArgs, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: object, e: IPETestingEventArgs):...
class IPETestingWrapper(object):
    @property
    def Data(self) -> object:"""Data { set; } -> object"""
    @property
    def IPETestingManager(self) -> IPETestingWrapper:"""IPETestingManager { get; } -> IPETestingWrapper"""
    @property
    def IPETest(self) -> IPETestingHandler:
        """IPETest Event: IPETestingHandler"""
    def FireIPETestingHandler(self):...
class IPEUpdateUIEventArgs(_n_8_t_14):
    @property
    def ForceUpdate(self) -> bool:"""ForceUpdate { get; } -> bool"""
    def __init__(self, forceUpdate: bool) -> IPEUpdateUIEventArgs:...
class IPEWrapper(object):
    @property
    def IPEEventManager(self) -> IPEWrapper:"""IPEEventManager { get; } -> IPEWrapper"""
    @property
    def UpdateUI(self) -> UpdateUIEventHandler:
        """UpdateUI Event: UpdateUIEventHandler"""
    def FireUpdateUIEvent(self, forceUpdate: bool):...
class IPreviewContext():
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
class IPreviewContextProvider():
    def GetPreviewControl(self, name: str) -> ILivePreviewControl:...
    def GetPreviewRule(self, name: str) -> ILivePreviewRule:...
class LayerUtilities(object):
    @property
    def ApplyLayerFilterToToolbar(self) -> bool:"""ApplyLayerFilterToToolbar { get; set; } -> bool"""
    @property
    def InvertLayerFilter(self) -> bool:"""InvertLayerFilter { get; set; } -> bool"""
    @property
    def IsMultiDocumentActivationEnabled(self) -> bool:"""IsMultiDocumentActivationEnabled { get; } -> bool"""
    @property
    def UseCurrentLayerFilter(self) -> bool:"""UseCurrentLayerFilter { get; set; } -> bool"""
    @property
    def VpOverrideBackgroundColor(self) -> _n_1_t_0:"""VpOverrideBackgroundColor { get; set; } -> Color"""
    @staticmethod
    def FocusMainFrameIfPossible():...
    @staticmethod
    def GetCurViewportObjectId() -> _n_2_t_0:...
    @staticmethod
    def GetRestoreFlags() -> int:...
    @staticmethod
    def LineWeightToPixel(lineWeight: _n_2_t_2) -> int:...
    @staticmethod
    def SetAllLayersUsed(layerTable: _n_2_t_7):...
    @staticmethod
    def SetLayerUsed(layerTableRecord: _n_2_t_8):...
    @staticmethod
    def SetNotDefaultCommand(bNotDefaultCommand: bool):...
    @staticmethod
    def ShowLayerMergeDialog(layers: _n_8_t_13[_n_2_t_0]):...
    @staticmethod
    def ShowLayerStateManagerDialog():...
    @staticmethod
    def ShowLayerStateSaveDialog():...
class LayoutContextMenu(object):
    def __init__(self, handler: LayoutContextMenu.CommandHandler, removeFlag: _n_8_t_12, enableFlag: _n_8_t_12, disableFlag: _n_8_t_12) -> LayoutContextMenu:...
    def __init__(self, handler: LayoutContextMenu.CommandHandler) -> LayoutContextMenu:...
    def Invoke(self, doc: _n_0_t_0, nTabIndex: int, hWndOwner: _n_8_t_0) -> int:...
    class Command(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        ActivateLast: int
        ActivateModel: int
        Delete: int
        DockAboveStatusBar: int
        DockInLineStatusBar: int
        ExportToModel: int
        FromTemplate: int
        HideTab: int
        ImportAsSheet: int
        Move: int
        New: int
        _None: int
        PageSetup: int
        Plot: int
        Publish: int
        Rename: int
        SelectAll: int
        value__: int
    class CommandHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
        def __init__(self, A_0: object, A_1: _n_8_t_0) -> LayoutContextMenu.CommandHandler:...
        def BeginInvoke(self, cmd: LayoutContextMenu.Command, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
        def EndInvoke(self, result: _n_8_t_8) -> bool:...
        def Invoke(self, cmd: LayoutContextMenu.Command) -> bool:...
class LayoutThumbnailEnumerator(_n_6_t_0, _n_8_t_11):
    @property
    def Count(self) -> _n_8_t_12:"""Count { get; } -> UInt32"""
    @property
    def Index(self) -> int:"""Index { get; } -> int"""
    @property
    def IsLayoutEmpty(self) -> bool:"""IsLayoutEmpty { get; } -> bool"""
    @property
    def LayoutName(self) -> str:"""LayoutName { get; } -> str"""
    @property
    def Thumbnail(self) -> _n_14_t_1:"""Thumbnail { get; } -> Bitmap"""
    @staticmethod
    def EnumerateLayoutThumbnails(doc: _n_0_t_0, nFlag: LayoutThumbnailEnumerator.ThumbnailCaptureFlags) -> LayoutThumbnailEnumerator:...
    def Locate(self, layoutName: str) -> bool:...
    def MoveNext(self) -> bool:...
    def Reset(self) -> bool:...
    class ThumbnailCaptureFlags(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        CaptureAll: int
        CaptureEmpty: int
        CaptureNone: int
        value__: int
class LightUtil(object):
    def __init__(self) -> LightUtil:...
    @staticmethod
    def GetBackgroundType(type: _n_5_t_0) -> bool:...
    @staticmethod
    def GetSkyStatus() -> bool:...
    @staticmethod
    def RegSceneUI() -> bool:...
    @staticmethod
    def SetSunAngle(db: _n_2_t_3, sunId: _n_8_t_10, dateTime: _n_8_t_18):...
class LineWeightPicker(ComboBoxWrapper, _n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    def __init__(self) -> LineWeightPicker:...
class LivePreviewUtil(object):
    @property
    def PreviewContextProvider(self) -> IPreviewContextProvider:"""PreviewContextProvider { get; } -> IPreviewContextProvider"""
    def __init__(self) -> LivePreviewUtil:...
    @staticmethod
    def IsControlLivePreviewAble(element: _n_19_t_0) -> bool:...
    @staticmethod
    def SetPreviewContextProvider(provider: IPreviewContextProvider) -> IPreviewContextProvider:...
class MgdAcViewTransitions(object):
    @staticmethod
    def GetSettings(enable2d: bool, enable3d: bool, enableDuringScripts: bool, timeMs: _n_8_t_12, fps: float):...
    @staticmethod
    def SetSettings(enable2d: bool, enable3d: bool, enableDuringScripts: bool, timeMs: _n_8_t_12, fps: float):...
class MLibDownloadUtils(object):
    def __init__(self) -> MLibDownloadUtils:...
    @staticmethod
    def BeginToExtract():...
    @staticmethod
    def CancelDownloadJob():...
    @staticmethod
    def DownloadCurrentSize() -> _n_8_t_16:...
    @staticmethod
    def DownloadServicEndUp():...
    @staticmethod
    def DownloadServiceStartUp():...
    @staticmethod
    def DownloadTotalSize() -> _n_8_t_16:...
    @staticmethod
    def IsMLibCancelled() -> bool:...
    @staticmethod
    def IsMLibDownloadComplete() -> bool:...
    @staticmethod
    def IsMLibDownloading() -> bool:...
    @staticmethod
    def IsMLibError() -> bool:...
    @staticmethod
    def IsMLibExtracting() -> bool:...
    @staticmethod
    def IsMLibReadyToInstall() -> bool:...
    @staticmethod
    def RegisterTimerCallback(fp: AcDownloadCallback):...
    @staticmethod
    def ShowErrorTaskDialog():...
class MlinesMgdServices(object):
    @staticmethod
    def AdjustColorToBackground(mgForeground: _n_14_t_0, mgBackground: _n_14_t_0):...
    @staticmethod
    def CloseCachedMLStyle():...
    @staticmethod
    def GetDefaultMlnFilename() -> str:...
    @staticmethod
    def GetDisplayBGColor(mgColor: _n_1_t_0):...
    @staticmethod
    def GetLinetypeNameForDisplay(linetypeId: _n_2_t_0) -> str:...
    @staticmethod
    def IsStyleAlterable(mgName: str) -> bool:...
    @staticmethod
    def IsValidStyleName(mgName: str) -> bool:...
    @staticmethod
    def LoadAndUpdateMlnStyle(mlnFile: str, fileOffset: int) -> MlinesMgdServices.MLError:...
    @staticmethod
    def MlnFileReadStyles(filename: str, nameList: _n_9_t_0, positionList: _n_9_t_0) -> MlinesMgdServices.MLError:...
    @staticmethod
    def ProcessMlEditCommand(commandCode: MlinesMgdServices.CommandCode):...
    @staticmethod
    def ShowOpenMlnFileDialog(currentMlnFile: str) -> str:...
    @staticmethod
    def ShowSaveDialog(styleId: _n_2_t_0, mlnFilename: str) -> MlinesMgdServices.MLError:...
    class CommandCode(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        AddVertex: int
        Cancel: int
        ClosedCross: int
        ClosedTee: int
        CornerJoint: int
        CutAll: int
        CutSingle: int
        DelVertex: int
        MaxCommandCode: int
        MergedCross: int
        MergedTee: int
        OpenCross: int
        OpenTee: int
        value__: int
        WeldAll: int
    class MLError(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        CouldNotOpenFile: int
        CouldNotReadFile: int
        GeneralError: int
        InvalidAngle: int
        InvalidDescription: int
        InvalidName: int
        InvalidOffset: int
        InvalidStyle: int
        MaxErrorCode: int
        MaxLinesReached: int
        Ok: int
        StyleInUse: int
        value__: int
class MonitoredSysvarValueWrapper(_n_6_t_0, _n_8_t_11):
    def __init__(self, p: _n_8_t_0, _auto_delete: bool) -> MonitoredSysvarValueWrapper:...
    def __init__(self, p: _n_8_t_0) -> MonitoredSysvarValueWrapper:...
    def clone(self) -> MonitoredSysvarValueWrapper:...
    def isEqualTo(self, sysvar_value: MonitoredSysvarValueWrapper) -> bool:...
    def setFromString(self, value: str) -> bool:...
    def toString(self, unit: int, prec: int) -> str:...
    def toString(self) -> str:...
    def type(self) -> str:...
class MonitoredSysvarWrapper(_n_6_t_0, _n_8_t_11):
    def __init__(self, p: _n_8_t_0) -> MonitoredSysvarWrapper:...
    def currentValue(self) -> MonitoredSysvarValueWrapper:...
    def isValidValue(self, value: MonitoredSysvarValueWrapper) -> bool:...
    def name(self) -> str:...
    def perferedValue(self) -> MonitoredSysvarValueWrapper:...
    def resetToPreferedValue(self):...
    def setPreferedValue(self, value: str) -> int:...
    def setPreferedValue(self, prefered_value: MonitoredSysvarValueWrapper):...
    def syncCurrentValue(self):...
class NavigationUtils(object):
    def __init__(self) -> NavigationUtils:...
    @staticmethod
    def GetNavStatus() -> int:...
    @staticmethod
    def IsNavActive() -> bool:...
    @staticmethod
    def NavPauseRecording():...
    @staticmethod
    def NavPlayAnimation():...
    @staticmethod
    def NavRecordAnimation():...
    @staticmethod
    def NavSaveAnimation():...
    @staticmethod
    def NavShowAnimationSetting():...
class NavisworksFileInfo(object):
    fileSize: int
    hasModificationTime: int
    modificationTime: int
    revisionId: int
    def __init__(self, obj: NavisworksFileInfo) -> NavisworksFileInfo:...
    def __init__(self) -> NavisworksFileInfo:...
class NavisworksFileType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    Aggregate: int
    Error: int
    Model: int
    value__: int
class NavisworksServiceManager(object):
    @property
    def Host(self) -> INavisworksService:"""Host { get; set; } -> INavisworksService"""
    def __init__(self) -> NavisworksServiceManager:...
class NewTabPageUtil(object):
    def __init__(self) -> NewTabPageUtil:...
    @staticmethod
    def SwitchToStartPage() -> bool:...
class NonMonitoredSysvarEnumerator(_n_6_t_0, _n_8_t_11):
    def __init__(self, p: _n_8_t_0) -> NonMonitoredSysvarEnumerator:...
    def Current(self) -> MonitoredSysvarWrapper:...
    def Done(self) -> bool:...
    def MoveNext(self):...
    def Reset(self):...
class ObjectContexts(object):
    def __init__(self) -> ObjectContexts:...
    @staticmethod
    def AddContext(obj: _n_2_t_9, ctxt: _n_2_t_10):...
    @staticmethod
    def GetContexts(obj: _n_2_t_9, collectionName: str) -> _n_10_t_0[_n_2_t_10]:...
    @staticmethod
    def HasContext(obj: _n_2_t_9, ctxt: _n_2_t_10) -> bool:...
    @staticmethod
    def RemoveContext(obj: _n_2_t_9, ctxt: _n_2_t_10):...
class ObjectDiffEventArgs(_n_8_t_14):
    @property
    def ChangeType(self) -> int:"""ChangeType { get; } -> int"""
    @property
    def DrawingId(self) -> int:"""DrawingId { get; } -> int"""
    @property
    def ObjHandle(self) -> _n_2_t_11:"""ObjHandle { get; } -> Handle"""
    def __init__(self, drawingId: int, handle: _n_8_t_16, changeType: int) -> ObjectDiffEventArgs:...
class ObjectDiffEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> ObjectDiffEventHandler:...
    def BeginInvoke(self, sender: object, e: ObjectDiffEventArgs, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: object, e: ObjectDiffEventArgs):...
class OPMModeFlags(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    FromCommand: int
    HatchPattern: int
    InvokeDialog: int
    InvokeHatchDialog: int
    Selection: int
    value__: int
    ZeroSelection: int
class OPMStatus(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    Failed: int
    InvalidProperty: int
    InvalidPropertyCategory: int
    InvalidPropertyType: int
    InvalidPropertyValue: int
    OK: int
    value__: int
class OwnerDrawComboBox(COwnerDrawComboBoxWrapper, _n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    @property
    def VistaTheme(self) -> bool:"""VistaTheme { get; } -> bool"""
    def __init__(self) -> OwnerDrawComboBox:...
    def IsInEdit(self, state: _n_21_t_7) -> bool:...
class PreviewControl(_n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    def __init__(self) -> PreviewControl:...
    def ClearAll(self):...
    def CreateModel(self) -> _n_6_t_1:...
    def ErasePreview(self):...
    def Init(self):...
    def RefreshPreview(self) -> _n_6_t_1:...
    def ShowEntity(self, fieldWidth: float, fieldHeight: float, entity: _n_2_t_12, added: bool):...
    def ShowEntity(self, fieldWidth: float, fieldHeight: float, entity: _n_2_t_12):...
class PreviewControlType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    PropertyPaletteControl: int
    RibbonItemControl: int
    value__: int
class QuickStartLink(_n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    def __init__(self) -> QuickStartLink:...
    def SetHelpTopic(self, helpTopic: str):...
    def SetNewFeatureWorkshopTopic(self, topic: str):...
class ResourceUtil(object):
    def __init__(self) -> ResourceUtil:...
    @staticmethod
    def FormatByLocale(type: _n_8_t_19, formatId: str, paramlist: _n_8_t_13[object]) -> str:...
    @staticmethod
    def FormatByLocale(formatString: str, paramlist: _n_8_t_13[object]) -> str:...
    @staticmethod
    def FormatInvariant(format: str, paramlist: _n_8_t_13[object]) -> str:...
    @staticmethod
    def GetCultureInfo() -> _n_15_t_0:...
    @staticmethod
    def GetString(type: _n_8_t_19, id: str) -> str:...
    @staticmethod
    def StringToDouble(text: str) -> float:...
class ScaleListHelpers(object):
    def __init__(self) -> ScaleListHelpers:...
    @staticmethod
    def getDefaultScaleList(returnPredefinedScales: bool, measurement: int, scaleStr: _n_10_t_0[str], scaleNum: _n_10_t_0[float], scaleDenom: _n_10_t_0[float], scaleCount: _n_8_t_13[int]) -> str:...
    @staticmethod
    def GetReferencedScaleNames(db: _n_2_t_3, scaleIds: _n_2_t_1, scaleStr: _n_10_t_0[str], scaleCount: _n_8_t_13[int]):...
    @staticmethod
    def GetUnitScaleName(db: _n_2_t_3) -> str:...
    @staticmethod
    def loadScaleList(referencedScaleIds: _n_2_t_1, referencedScaleCount: _n_8_t_13[int], scaleStr: _n_10_t_0[str], scaleNum: _n_10_t_0[float], scaleDenom: _n_10_t_0[float], scaleCount: _n_8_t_13[int]):...
    @staticmethod
    def loadScaleUnitStrings(unitStrings: _n_8_t_13[str]):...
    @staticmethod
    def resetScaleList(measurement: int, scaleStr: _n_10_t_0[str], scaleNum: _n_10_t_0[float], scaleDenom: _n_10_t_0[float], scaleCount: _n_8_t_13[int]):...
    @staticmethod
    def saveScaleList(scaleStr: _n_10_t_0[str], scaleNum: _n_10_t_0[float], scaleDenom: _n_10_t_0[float], scaleCount: int):...
    @staticmethod
    def setDefaultScaleList(newScaleStr: _n_10_t_0[str], scaleNum: _n_10_t_0[float], scaleDenom: _n_10_t_0[float], scaleType: _n_10_t_0[int], scaleCount: int):...
    @staticmethod
    def updateScaleList(oldScaleStr: _n_10_t_0[str], newScaleStr: _n_10_t_0[str], scaleNum: _n_10_t_0[float], scaleDenom: _n_10_t_0[float], scaleCount: int):...
class SearchBox(_n_21_t_8, _n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    @property
    def DefaultText(self) -> str:"""DefaultText { set; } -> str"""
    @property
    def IsEditEmpty(self) -> bool:"""IsEditEmpty { get; } -> bool"""
    @property
    def Notification(self) -> str:"""Notification { set; } -> str"""
    def __init__(self) -> SearchBox:...
    def ClearEditor(self):...
    def SetButtonBackgroundColorForThemeChange(self, color: _n_14_t_0, bThemeIsDark: bool):...
class SetReadOnlySysvar(object):
    def __init__(self) -> SetReadOnlySysvar:...
    @staticmethod
    def SetLayerManagerState(eState: int):...
class SMManager(object):
    def __init__(self) -> SMManager:...
    @staticmethod
    def CIP_LogTargetShot(strShotName: str) -> bool:...
    @staticmethod
    def DeleteSequenceShot(bSequence: bool, strName: str):...
    @staticmethod
    def EndPlay():...
    @staticmethod
    def GetPlayStatus(activeShotName: str, activeSeqName: str, playMode: SMManager.PlayMode, playAction: SMManager.PlayAction, bPause: bool) -> bool:...
    @staticmethod
    def GetSequenceIds() -> _n_8_t_13[_n_8_t_10]:...
    @staticmethod
    def GetShotIds(strName: str) -> _n_8_t_13[_n_8_t_10]:...
    @staticmethod
    def IsShotPlaying() -> bool:...
    @staticmethod
    def LoopStatusChanged(bLoop: bool):...
    @staticmethod
    def MoveSequenceShot(bSequence: bool, strName: str, bLeft: bool):...
    @staticmethod
    def PauseOrResumePlayBack(bPause: bool):...
    @staticmethod
    def RenameSequenceShot(bSequence: bool, oldName: str, newName: str) -> bool:...
    @staticmethod
    def UIToBeHidden():...
    @staticmethod
    def UIToBeShown():...
    @staticmethod
    def UpdateCachedData():...
    @staticmethod
    def UpdateThumbnailAll() -> bool:...
    @staticmethod
    def UpdateThumbnailSequenceShot(bSequence: bool, strName: str) -> bool:...
    class PlayAction(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        PlayEnd: int
        PlayNoAction: int
        PlayPause: int
        PlayResume: int
        PlayStart: int
        value__: int
    class PlayMode(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        NoPlay: int
        PlayAll: int
        PlaySequnce: int
        PlayView: int
        value__: int
class SmManagerUtilities(object):
    @staticmethod
    def SetSmManagerInterface(mgr: object):...
class StartupToolsEventArgs(_n_8_t_14):
    def __init__(self) -> StartupToolsEventArgs:...
    def Add(self, toolName: str, commandName: str):...
class SubSetting(object):
    def __init__(self) -> SubSetting:...
    @staticmethod
    def IsCommandEnabled(command: str) -> bool:...
    @staticmethod
    def IsSysVarEnabled(sysvar: str) -> bool:...
class SyncStateChangedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> SyncStateChangedEventHandler:...
    def BeginInvoke(self, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self):...
class SyncStatus(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    BeginSync: int
    OutOfSync: int
    Synchronized: int
    value__: int
class SyncStatusChangedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> SyncStatusChangedEventHandler:...
    def BeginInvoke(self, status: SyncStatus, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, status: SyncStatus):...
class SysvarMonitorIteratorWrapper(_n_6_t_0, _n_8_t_11):
    def __init__(self, p: _n_8_t_0) -> SysvarMonitorIteratorWrapper:...
    def isEqual(self, sysvarMonitorIter: SysvarMonitorIteratorWrapper) -> bool:...
    def isnotEqual(self, sysvarMonitorIter: SysvarMonitorIteratorWrapper) -> bool:...
    def next(self) -> SysvarMonitorIteratorWrapper:...
    def sysvar(self) -> MonitoredSysvarWrapper:...
class SysvarMonitorWrapper(_n_6_t_0, _n_8_t_11):
    @property
    def BalloonAlertEnabled(self) -> bool:"""BalloonAlertEnabled { get; set; } -> bool"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; set; } -> bool"""
    def addMonitoredSysvar(self, sysvar: MonitoredSysvarWrapper) -> MonitoredSysvarWrapper:...
    def begin(self) -> SysvarMonitorIteratorWrapper:...
    @staticmethod
    def createSysvarMonitorWrapper(p: _n_8_t_0) -> SysvarMonitorWrapper:...
    def end(self) -> SysvarMonitorIteratorWrapper:...
    def getNonMonitoredSysvarEnumerator(self) -> NonMonitoredSysvarEnumerator:...
    def isDifferenceDetected(self) -> bool:...
    def isSysvarMonitored(self, sysvar_name: str) -> bool:...
    def removeMonitoredSysvar(self, sysvar: MonitoredSysvarWrapper):...
    def resetMonitoredSysvar(self, sysvar: MonitoredSysvarWrapper):...
class TableItem(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    TableItemCell: int
    TableItemColumn: int
    TableItemInvalid: int
    TableItemRow: int
    value__: int
class TableStylePreview(_n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    @property
    def Database(self) -> _n_2_t_3:"""Database { get; set; } -> Database"""
    @property
    def DataText(self) -> str:"""DataText { set; } -> str"""
    @property
    def HeaderText(self) -> str:"""HeaderText { set; } -> str"""
    @property
    def NumColumns(self) -> int:"""NumColumns { set; } -> int"""
    @property
    def NumRows(self) -> int:"""NumRows { set; } -> int"""
    @property
    def Table(self) -> _n_2_t_13:"""Table { get; } -> Table"""
    @property
    def TableStyle(self) -> _n_2_t_0:"""TableStyle { get; set; } -> ObjectId"""
    @property
    def TitleText(self) -> str:"""TitleText { set; } -> str"""
    def __init__(self) -> TableStylePreview:...
    def EnablePreview(self, bEnable: bool) -> bool:...
    def InitializeTable(self) -> bool:...
    def ShowTablePreview(self, bUpdateTable: bool) -> bool:...
class TableUtilities(object):
    def __init__(self) -> TableUtilities:...
    @staticmethod
    def CanDelete(table: _n_2_t_13, selRange: _n_2_t_14, row: bool) -> bool:...
    @staticmethod
    def CanInsert(table: _n_2_t_13, selRange: _n_2_t_14, row: bool, rightOrBottom: bool) -> bool:...
    @staticmethod
    def CanMergeCells(table: _n_2_t_13, selRange: _n_2_t_14) -> bool:...
    @staticmethod
    def CanUnMergeCells(table: _n_2_t_13, selRange: _n_2_t_14) -> bool:...
    @staticmethod
    def GetBackgroundColor(table: _n_2_t_13) -> _n_1_t_0:...
    @staticmethod
    def GetCellStyle(table: _n_2_t_13, selRange: _n_2_t_14, item: TableItem, localized: bool, varies: bool) -> str:...
    @staticmethod
    def GetCellStyles(tableStyle: _n_2_t_15, count: int, localized: bool, sort: bool) -> _n_8_t_13[str]:...
    @staticmethod
    def GetCellStyles(tableStyle: _n_2_t_15, count: int) -> _n_8_t_13[str]:...
    @staticmethod
    def GetDataType(table: _n_2_t_13, dateType: _n_2_t_16, unitType: _n_2_t_17):...
    @staticmethod
    def GetPickFirstTable(tableId: _n_2_t_0, selRange: _n_2_t_14, tableIndex: int) -> bool:...
    @staticmethod
    def GetReadOnlyState(table: _n_2_t_13, selRange: _n_2_t_14, readOnlyContent: bool, readOnlyFormat: bool):...
    @staticmethod
    def GetSelectionAlignment(tableId: _n_8_t_10, alignment: _n_2_t_18) -> bool:...
    @staticmethod
    def GetSelectionLock(table: _n_2_t_13, cellState: _n_2_t_19) -> bool:...
    @staticmethod
    def IsDataLinkCommandAllowed() -> bool:...
    @staticmethod
    def IsFieldCommandAllowed() -> bool:...
    @staticmethod
    def IsSingleCell(table: _n_2_t_13, selRange: _n_2_t_14) -> bool:...
    @staticmethod
    def SetBackgroundColor(table: _n_2_t_13, color: _n_1_t_0):...
class TextIPEUtils(object):
    @property
    def MaxmumObliqueAngle(self) -> float:"""MaxmumObliqueAngle { get; } -> float"""
    @property
    def MaxmumTrackingFactor(self) -> float:"""MaxmumTrackingFactor { get; } -> float"""
    @property
    def MaxmumWidthScale(self) -> float:"""MaxmumWidthScale { get; } -> float"""
    @property
    def MinimumObliqueAngle(self) -> float:"""MinimumObliqueAngle { get; } -> float"""
    @property
    def MinimumTrackingFactor(self) -> float:"""MinimumTrackingFactor { get; } -> float"""
    @property
    def MinimumWidthScale(self) -> float:"""MinimumWidthScale { get; } -> float"""
    @staticmethod
    def ContinueAutoNumbering() -> bool:...
    @staticmethod
    def Diagonal() -> bool:...
    @staticmethod
    def GetAllFontNames(trueTypeFonts: _n_10_t_0[str], shxFonts: _n_10_t_0[str], bigFonts: _n_10_t_0[str]):...
    @staticmethod
    def GetCustomMacors(marcroList: _n_10_t_0[str]):...
    @staticmethod
    def GetFontTypeImage(IsTrueType: bool) -> _n_8_t_0:...
    @staticmethod
    def GetIconFromAcadResource(iconType: IPEControlIconType, image: _n_24_t_1, largeImage: _n_24_t_1) -> bool:...
    @staticmethod
    def GetIPEState() -> IPEStateWrapper:...
    @staticmethod
    def Horizontal() -> bool:...
    @staticmethod
    def MgdIPESendCommand(command: IPECommands, param1: object, param2: object) -> bool:...
    @staticmethod
    def NoUnitsNumberToString(dValue: float) -> str:...
    @staticmethod
    def NumberToString(dValue: float) -> str:...
    @staticmethod
    def RedoAutoNumbering() -> bool:...
    @staticmethod
    def RestartAutoNumbering() -> bool:...
    @staticmethod
    def StackProperties() -> bool:...
    @staticmethod
    def StringToNoUnitsNumber(sText: str, dValue: float) -> bool:...
    @staticmethod
    def StringToNumber(sText: str, dValue: float) -> bool:...
    @staticmethod
    def UndoAutoNumbering() -> bool:...
    @staticmethod
    def Unstack() -> bool:...
class ThemeChangedEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> ThemeChangedEventHandler:...
    def BeginInvoke(self, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self):...
class TrueColorPicker(ComboBoxWrapper, _n_13_t_0, _n_21_t_0IOleControl, _n_21_t_0IOleObject, _n_21_t_0IOleInPlaceObject, _n_21_t_0IOleInPlaceActiveObject, _n_21_t_0IOleWindow, _n_21_t_0IViewObject, _n_21_t_0IViewObject2, _n_21_t_0IPersist, _n_21_t_0IPersistStreamInit, _n_21_t_0IPersistPropertyBag, _n_21_t_0IPersistStorage, _n_21_t_0IQuickActivate, _n_21_t_1, _n_21_t_2, _n_13_t_1, _n_21_t_3, _n_22_t_0, _n_21_t_4):
    @property
    def CurrentSelectionIndex(self) -> int:"""CurrentSelectionIndex { get; set; } -> int"""
    def __init__(self) -> TrueColorPicker:...
    def AddOtherItemToList(self, name: str, cargo: int) -> int:...
    def GetCurrentItemColor(self) -> _n_1_t_0:...
    def SetCurrentByColor(self, mgColor: _n_1_t_0):...
class UiCallback(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> UiCallback:...
    def BeginInvoke(self, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self):...
class UndoBoundaryEnum(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    CommandBoundaryEnd: int
    CommandBoundaryStart: int
    SubCommandBoundary: int
    SubCommandWall: int
    value__: int
class UnmanagedResource(object):
    @property
    def AcadResourceHandle(self) -> _n_8_t_0:"""AcadResourceHandle { get; } -> IntPtr"""
    def __init__(self) -> UnmanagedResource:...
    @staticmethod
    def GetResourceHandle(moduleName: str) -> _n_8_t_0:...
    @staticmethod
    def LoadString(resourceHandle: _n_8_t_0, resourceId: int) -> str:...
class UpdateTitleBarEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> UpdateTitleBarEventHandler:...
    def BeginInvoke(self, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self):...
class UpdateUIEventHandler(_n_8_t_6, _n_8_t_7, _n_18_t_0):
    def __init__(self, A_0: object, A_1: _n_8_t_0) -> UpdateUIEventHandler:...
    def BeginInvoke(self, sender: object, e: IPEUpdateUIEventArgs, callback: _n_8_t_9, obj: object) -> _n_8_t_8:...
    def EndInvoke(self, result: _n_8_t_8):...
    def Invoke(self, sender: object, e: IPEUpdateUIEventArgs):...
class Utils(object):
    @property
    def ApplicationStatusBarMenu(self) -> _n_20_t_0:"""ApplicationStatusBarMenu { get; } -> MenuItem"""
    @property
    def ApplicationToolbarsMenu(self) -> _n_20_t_0:"""ApplicationToolbarsMenu { get; } -> MenuItem"""
    @property
    def CaptureOnLayoutSwitch(self) -> bool:"""CaptureOnLayoutSwitch { set; } -> bool"""
    @property
    def ImpliedSelectionIsActive(self) -> bool:"""ImpliedSelectionIsActive { get; } -> bool"""
    @property
    def IsCuiCommandEnabled(self) -> bool:"""IsCuiCommandEnabled { get; } -> bool"""
    @property
    def IsEditorReady(self) -> bool:"""IsEditorReady { get; } -> bool"""
    @property
    def IsOsThemed(self) -> bool:"""IsOsThemed { get; } -> bool"""
    @property
    def IsScriptActive(self) -> bool:"""IsScriptActive { get; } -> bool"""
    @property
    def SysVarInProgress(self) -> str:"""SysVarInProgress { get; } -> str"""
    @property
    def SavingStartupTools(self) -> _n_8_t_15[StartupToolsEventArgs]:
        """SavingStartupTools Event: EventHandler"""
    def __init__(self) -> Utils:...
    @staticmethod
    def ActivateDocument(hWndDoc: _n_8_t_0):...
    @staticmethod
    def ActivateLayout(doc: _n_0_t_0, index: int):...
    @staticmethod
    def AddCommand(cmdGroupName: str, cmdGlobalName: str, cmdLocalName: str, cmdFlags: _n_6_t_2, func: CommandCallback):...
    @staticmethod
    def AngleToString(dValue: float) -> str:...
    @staticmethod
    def ApplyAcValueFormat(objValue: object, formatString: str) -> str:...
    @staticmethod
    def AreFilesSame(file1: str, file2: str) -> bool:...
    @staticmethod
    def CallButtonEditor(resId: str, packageName: str) -> str:...
    @staticmethod
    def CallButtonEditorWithBitmap(bitmap: _n_14_t_1, resId: str, packageName: str) -> str:...
    @staticmethod
    def CancelAndRunCmds(pStrCmd: str) -> bool:...
    @staticmethod
    def CloseCommandLine():...
    @staticmethod
    def ConvertBitmapToAcGiImageBGRA32(bmp: _n_14_t_1) -> _n_5_t_1:...
    @staticmethod
    def ConvertBitmapToAcGiImageBGRA32Ex(bmp: _n_14_t_1) -> _n_5_t_1:...
    @staticmethod
    def ConvertCMenuToMenuItem(pMenu: object, menuItem: _n_20_t_0):...
    @staticmethod
    def ConvertOSnapCMenuToMenuItem(pMenu: object, menuItem: _n_20_t_0, b3DOsnap: bool):...
    @staticmethod
    def CreateCommandToolTip(pTooltipInfo: _n_8_t_10) -> object:...
    @staticmethod
    def CreateNativeTrayItemInstance() -> _n_8_t_0:...
    @staticmethod
    def CUIEndTransferBitmaps():...
    @staticmethod
    def CUIIsUsingSmallIcon() -> bool:...
    @staticmethod
    def CUIRequestBitmap(resId: str):...
    @staticmethod
    def CUISaveMenuAndToolbarState():...
    @staticmethod
    def CUIStartTransferBitmaps():...
    @staticmethod
    def DeleteDimConstraints(db: _n_2_t_3, bKeepAnnotativeDimensions: bool) -> bool:...
    @staticmethod
    def DisableUndoRecording(db: _n_2_t_3, bDisable: bool) -> bool:...
    @staticmethod
    def DisplaySettingsDialog():...
    @staticmethod
    def Do_Cmd(menuString: str, IsSSetNeedRestore: bool, bMenuMacro: bool, IsHiddenCmd: bool, bSynchronous: bool):...
    @staticmethod
    def DoHelpForCommand(cmdName: str):...
    @staticmethod
    def DragDropLayoutTab(doc: _n_0_t_0, index: int, isMoveOrCopy: bool):...
    @staticmethod
    def DrawLineTypePattern(ltypeID: _n_2_t_0, left: int, top: int, right: int, bottom: int) -> _n_8_t_0:...
    @staticmethod
    def DrawLineWeightLine(lineWeight: _n_2_t_2, left: int, top: int, right: int, bottom: int) -> _n_8_t_0:...
    @staticmethod
    def DrawLineWeightSquare(lineWeight: _n_2_t_2, left: int, top: int, right: int, bottom: int) -> _n_8_t_0:...
    @staticmethod
    def DropOpenFile(file: str):...
    @staticmethod
    def EnableDockControlBars(bEnable: bool):...
    @staticmethod
    def EnableFloatingWindows(bEnable: bool):...
    @staticmethod
    def EnableSysButtons(bEnable: bool):...
    @staticmethod
    def EntFirst() -> _n_2_t_0:...
    @staticmethod
    def EntLast() -> _n_2_t_0:...
    @staticmethod
    def EntNext(entId: _n_2_t_0, skipSubEnt: bool) -> _n_2_t_0:...
    @staticmethod
    def EntNext(entId: _n_2_t_0) -> _n_2_t_0:...
    @staticmethod
    def EvaluateTopLevelNetwork(db: _n_2_t_3, bRelaxEvaluate: bool) -> bool:...
    @staticmethod
    def ExecuteApplicationStatusBarMenu(nId: int):...
    @staticmethod
    def FlushGraphics():...
    @staticmethod
    def ForceRunCommandAsTransparent(bEnabled: bool):...
    @staticmethod
    def GetAcadFrameHandle() -> _n_8_t_0:...
    @staticmethod
    def GetAcadResourceIcon(sResId: str) -> _n_14_t_2:...
    @staticmethod
    def GetActualIndex(index: int) -> int:...
    @staticmethod
    def GetApplicationFrameHWnd() -> _n_8_t_0:...
    @staticmethod
    def GetBlockImage(objectId: _n_2_t_0, nImgWidth: int, nImgHeight: int, backgroundColor: _n_1_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetCommandAtLevelForDocument(level: int) -> str:...
    @staticmethod
    def GetCommandPromptString() -> str:...
    @staticmethod
    def GetCommandVersion() -> int:...
    @staticmethod
    def GetCurrentEditBlock() -> _n_2_t_0:...
    @staticmethod
    def GetCurrentFindingContent() -> str:...
    @staticmethod
    def GetCurrentObjectColor() -> _n_1_t_0:...
    @staticmethod
    def GetCurrentViewportVisualStyleId() -> _n_2_t_0:...
    @staticmethod
    def GetCustomSwatchImage(name: str, nWidth: int, nHeight: int) -> _n_8_t_0:...
    @staticmethod
    def GetDieselEvalString(text: str, bGrayed: bool, bChecked: bool) -> str:...
    @staticmethod
    def GetDieselEvalString(text: str) -> str:...
    @staticmethod
    def GetDimStyleImage(objectId: _n_2_t_0, nImgWidth: int, nImgHeight: int, backgroundColor: _n_1_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetDockClientRect(excludeLayoutBar: bool) -> _n_19_t_1:...
    @staticmethod
    def GetDockClientRect() -> _n_19_t_1:...
    @staticmethod
    def GetDwgFrameIcon(doc: _n_0_t_0) -> _n_14_t_2:...
    @staticmethod
    def GetFontImage(fontID: _n_2_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetGradientDisplayText(nHatchGradientNameEnum: int) -> str:...
    @staticmethod
    def GetGradientDisplayText(gradientName: str) -> str:...
    @staticmethod
    def GetGradientName(displayText: str) -> str:...
    @staticmethod
    def GetGradientSwatchImage(displayText: str, angle: float, bShifted: bool, startColor: _n_1_t_0, stopColor: _n_1_t_0, nWidth: int, nHeight: int) -> _n_8_t_0:...
    @staticmethod
    def GetGradientValue(displayText: str) -> int:...
    @staticmethod
    def GetHideWarningDialogs(nType: _n_8_t_12) -> bool:...
    @staticmethod
    def GetLastCommandLines(lastLines: int, ignoreNull: bool) -> _n_10_t_0[str]:...
    @staticmethod
    def GetLastInsertBlockData(specifyScaleOnScreen: bool, specifyRotationOnScreen: bool):...
    @staticmethod
    def GetLayoutThumbnail(doc: _n_0_t_0, layoutName: str) -> _n_14_t_1:...
    @staticmethod
    def GetMLeaderStyleImage(objectId: _n_2_t_0, nImgWidth: int, nImgHeight: int, backgroundColor: _n_1_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetMoreHideWarningDialogs(nType: _n_8_t_12) -> bool:...
    @staticmethod
    def GetOpmWindow() -> _n_8_t_0:...
    @staticmethod
    def GetPatSwatchImage(name: str, patternColor: _n_1_t_0, backgroundColor: _n_1_t_0, nWidth: int, nHeight: int) -> _n_8_t_0:...
    @staticmethod
    def GetPredefinedVisualStyleGlobalName(localName: str) -> str:...
    @staticmethod
    def GetProductbrandingName() -> str:...
    @staticmethod
    def GetQpWindow() -> _n_8_t_0:...
    @staticmethod
    def GetRealHatchPreviewImage(nWidth: int, nHeight: int) -> _n_8_t_0:...
    @staticmethod
    def GetRedoHistory() -> _n_11_t_1[str]:...
    @staticmethod
    def GetRefEditName() -> str:...
    @staticmethod
    def GetStatusBarOsnapMenu(b3DOsnap: bool, isDarkTheme: bool) -> _n_20_t_0:...
    @staticmethod
    def GetTableCellStyleImage(cellStyleName: str, nImgWidth: int, nImgHeight: int, backgroundColor: _n_1_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetTableStyleImage(objectId: _n_2_t_0, nImgWidth: int, nImgHeight: int, backgroundColor: _n_1_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetTextExtents(styleId: _n_2_t_0, text: str, dHeight: float) -> _n_4_t_0:...
    @staticmethod
    def GetToolPaletteGroups(schemeName: str, pGroups: _n_12_t_0) -> bool:...
    @staticmethod
    def GetUndoHistory() -> _n_11_t_1[str]:...
    @staticmethod
    def GetUnitsConversion(fromUnits: _n_2_t_20, toUnits: _n_2_t_20) -> float:...
    @staticmethod
    def GetUnknownPatternSwatchImage(nWidth: int, nHeight: int) -> _n_8_t_0:...
    @staticmethod
    def GetUserDefinedSwatchImage(bDouble: bool, patternColor: _n_1_t_0, backgroundColor: _n_1_t_0, nWidth: int, nHeight: int) -> _n_8_t_0:...
    @staticmethod
    def GetVisualStyleEdgeColor(visualStyleId: _n_8_t_10) -> _n_1_t_0:...
    @staticmethod
    def GetVisualStyleImage(objectId: _n_2_t_0) -> _n_8_t_0:...
    @staticmethod
    def GetVisualStyleIntersectionEdgeColor(visualStyleId: _n_8_t_10) -> _n_1_t_0:...
    @staticmethod
    def GetVisualStyleObscuredEdgeColor(visualStyleId: _n_8_t_10) -> _n_1_t_0:...
    @staticmethod
    def GetVisualStyles(objectIds: _n_2_t_1, imageList: _n_10_t_0[_n_24_t_1]):...
    @staticmethod
    def GetWSUID(sWSName: str) -> str:...
    @staticmethod
    def HistoryStatus() -> bool:...
    @staticmethod
    def IconFilePath() -> str:...
    @staticmethod
    def InitDialog(bUseDialog: bool) -> bool:...
    @staticmethod
    def InitializeCommandLineFont():...
    @staticmethod
    def InvokeDataLinkManagerDialog(database: _n_2_t_3, dialogMode: int, parentForm: _n_21_t_10, objectId: _n_2_t_0) -> _n_21_t_9:...
    @staticmethod
    def InvokeDataTypeDialog(inDataType: _n_2_t_16, inUnitType: _n_2_t_17, sFormatIn: str, objValue: object, dialogOptions: int, parentForm: _n_21_t_10, sTitle: str, sHelp: str, outDataType: _n_2_t_16, outUnitType: _n_2_t_17, sFormatOut: str) -> _n_21_t_9:...
    @staticmethod
    def InvokeOpmSetPropertyValue(prop: object, val: object, objIds: _n_2_t_1, guid: _n_8_t_20, mode: OPMModeFlags) -> OPMStatus:...
    @staticmethod
    def InvokeOptionsDialog(strPos: str, bInvokedAsChildDlg: bool, defaultLabelIdInFileTab: _n_8_t_12, bExpanded: bool):...
    @staticmethod
    def InvokeStatusBarItemDeleted(ptr: _n_8_t_0):...
    @staticmethod
    def InvokeStatusBarItemMouseDown(ptr: _n_8_t_0, type: int, flag: int, point: _n_19_t_2):...
    @staticmethod
    def InvokeTableStyleDialog():...
    @staticmethod
    def InvokeTrayItemCloseBubbleWindow(trayItemPtr: _n_8_t_0):...
    @staticmethod
    def InvokeTrayItemShowBubbleWindow(title: str, description: str, iconType: Utils.BubbleWindowIconType, hyperlink: str, hypertext: str, text: str, trayItemPtr: _n_8_t_0):...
    @staticmethod
    def Is3dVisualStyle(styleName: str) -> bool:...
    @staticmethod
    def IsAssociativeArrayRibbonContextApplicable(type: str, dataItem: object) -> bool:...
    @staticmethod
    def IsCommandActive(name: str) -> bool:...
    @staticmethod
    def IsCommandDefined(cmdName: str) -> bool:...
    @staticmethod
    def IsCommandNameInUse(name: str) -> CommandTypeFlags:...
    @staticmethod
    def IsCommandReEntered(name: str) -> bool:...
    @staticmethod
    def IsCoreCommand(name: str) -> bool:...
    @staticmethod
    def IsCustSyncEnabled() -> bool:...
    @staticmethod
    def IsDiesel(text: str) -> bool:...
    @staticmethod
    def IsDocumentInBlockEditor(doc: _n_0_t_0) -> bool:...
    @staticmethod
    def IsDroppableExtension(extension: str) -> bool:...
    @staticmethod
    def IsFlagOn(id: _n_8_t_12, bDefault: bool) -> bool:...
    @staticmethod
    def IsInBlockEditor() -> bool:...
    @staticmethod
    def IsInCommandStack(flags: _n_6_t_2) -> bool:...
    @staticmethod
    def IsInCustomizeMode() -> bool:...
    @staticmethod
    def IsInPaperSpace() -> bool:...
    @staticmethod
    def IsInputPending() -> bool:...
    @staticmethod
    def IsInQuiescentState() -> bool:...
    @staticmethod
    def IsInStartup() -> bool:...
    @staticmethod
    def IsInTilemode() -> bool:...
    @staticmethod
    def IsLinkedObjectExist(doc: _n_0_t_0) -> bool:...
    @staticmethod
    def IsLispCommandDefined(name: str) -> bool:...
    @staticmethod
    def IsMultiRedoAvaliable() -> bool:...
    @staticmethod
    def IsNewTabCommandAllowed() -> bool:...
    @staticmethod
    def IsNonDrawingDocumentDisabled() -> bool:...
    @staticmethod
    def IsOEM() -> bool:...
    @staticmethod
    def IsOverrideActive() -> bool:...
    @staticmethod
    def IsPasteClipCommandAllowed() -> bool:...
    @staticmethod
    def IsPointOverToolbar(x: int, y: int) -> bool:...
    @staticmethod
    def IsT2P() -> bool:...
    @staticmethod
    def IsTextEditorActive() -> bool:...
    @staticmethod
    def IsUndoAvailable() -> bool:...
    @staticmethod
    def IsVisualStyleDefault(visualStyleId: _n_8_t_10) -> bool:...
    @staticmethod
    def NewDocument():...
    @staticmethod
    def NotifyStatusBarServiceReady() -> bool:...
    @staticmethod
    def NumberToUnitsString(dValue: float) -> str:...
    @staticmethod
    def OpenDocument():...
    @staticmethod
    def Orbit():...
    @staticmethod
    def Pan():...
    @staticmethod
    def PointOnScreen(pt: _n_4_t_1) -> bool:...
    @staticmethod
    def PostCommandPrompt():...
    @staticmethod
    def PostRouteMessageToDwgView(handle: _n_8_t_0, message: int, wParam: _n_8_t_0, lParam: _n_8_t_0) -> bool:...
    @staticmethod
    def PreRouteMessageToDwgView(handle: _n_8_t_0, message: int, wParam: _n_8_t_0, lParam: _n_8_t_0) -> bool:...
    @staticmethod
    def RawAngleToString(dValue: float) -> str:...
    @staticmethod
    def RedrawGrips():...
    @staticmethod
    def RefreshDragCursor(hasDrawArea: bool, isCopy: bool, point: _n_19_t_2):...
    @staticmethod
    def RegenEntity(entId: _n_2_t_0):...
    @staticmethod
    def RegisterCommandLineWindow(window: _n_8_t_0):...
    @staticmethod
    def RegisterLeaveStartupUiCallback(func: UiCallback) -> bool:...
    @staticmethod
    def RegisterLispCommand(cmdName: str, lispName: str):...
    @staticmethod
    def RegisterStartupUiCallback(ordering: float, func: UiCallback, delayInMs: int) -> bool:...
    @staticmethod
    def ReloadMenus(wsCurrentStr: str, bResetWorkspace: bool, bIncrementalReloading: bool):...
    @staticmethod
    def RemoveCommand(cmdGroupName: str, cmdGlobalName: str):...
    @staticmethod
    def RestoreApplicationStatusBar():...
    @staticmethod
    def RunFindText(pStrCmd: str):...
    @staticmethod
    def SelectObjects(ids: _n_8_t_13[_n_2_t_0]) -> bool:...
    @staticmethod
    def SendMenuStringToExecute(doc: _n_0_t_0, menuString: str, bEchoString: bool):...
    @staticmethod
    def SendToCloud(alreadyOnServer: bool) -> str:...
    @staticmethod
    def SetApplicationStatusBarProgressMeter(nPos: int):...
    @staticmethod
    def SetApplicationStatusBarProgressMeter(str: str, minimum: int, maximum: int):...
    @staticmethod
    def SetCurrentViewportVisualStyle(visualStyleId: _n_2_t_0):...
    @staticmethod
    def SetCurrentWorkspace(wsCurrent: str, bRestoreUI: bool, bAutoSaveWS: bool) -> bool:...
    @staticmethod
    def SetFocusToDwgView():...
    @staticmethod
    def SetHideWarningDialogs(nType: _n_8_t_12, bValue: bool):...
    @staticmethod
    def SetIsDragLayout(isDragging: bool):...
    @staticmethod
    def SetMoreHideWarningDialogs(nType: _n_8_t_12, bValue: bool):...
    @staticmethod
    def SetPropertiesInDatabaseForTPPlayback(itemId: _n_8_t_20, bSet: bool):...
    @staticmethod
    def SetQnewTemplateAfterInitialSetup():...
    @staticmethod
    def SetQuickViewWindowHandle(hWnd: _n_8_t_0):...
    @staticmethod
    def SetRecoverAllMode(bOn: bool):...
    @staticmethod
    def SetRecoverRequestedMode(bOn: bool):...
    @staticmethod
    def SetStatusBarContainerHeight(height: int):...
    @staticmethod
    def SetStatusBarContent(rootVisual: _n_19_t_3) -> bool:...
    @staticmethod
    def SetUndoMark(begin: bool) -> bool:...
    @staticmethod
    def ShowConflictingSettingsTaskDialog() -> bool:...
    @staticmethod
    def ShowHideTextWindow(bShow: bool):...
    @staticmethod
    def ShowLineTypeDialog():...
    @staticmethod
    def ShowMeshConversionTaskDialog() -> Utils.MeshConversionType:...
    @staticmethod
    def ShowNewComputerTaskDialog() -> bool:...
    @staticmethod
    def ShowOldLayoutTab(bShowTab: bool):...
    @staticmethod
    def ShowPADialog():...
    @staticmethod
    def StartToolbarDragDrop(menuGroups: _n_12_t_0, names: _n_12_t_0, tags: _n_12_t_0, commands: _n_12_t_0, helpStrs: _n_12_t_0, smallImages: _n_12_t_0, largeImages: _n_12_t_0, resourceFiles: _n_12_t_0) -> bool:...
    @staticmethod
    def StrCompareNatural(str1: str, str2: str) -> int:...
    @staticmethod
    def StringToAngle(sText: str, dValue: float) -> bool:...
    @staticmethod
    def StringToRawAngle(sText: str, dValue: float) -> bool:...
    @staticmethod
    def TransferBitmap(resId: str):...
    @staticmethod
    def TransferToolbarBitmaps():...
    @staticmethod
    def UcsToDisplay(ucsPoint: _n_4_t_1, bPaperSpace: bool) -> _n_4_t_1:...
    @staticmethod
    def UnitsStringToNumber(sText: str, dValue: float) -> bool:...
    @staticmethod
    def UnregisterCommandLineWindow(window: _n_8_t_0):...
    @staticmethod
    def UpdateLayoutSelection():...
    @staticmethod
    def ViewHasChanged() -> bool:...
    @staticmethod
    def ViewportChange(x: int, y: int):...
    @staticmethod
    def ViewportCycle():...
    @staticmethod
    def ViewportResize(sx: float, sy: float, ex: float, ey: float, split: bool):...
    @staticmethod
    def ViewportTypeChange(id: int):...
    @staticmethod
    def visualStyleId(visualStyleName: str) -> _n_2_t_0:...
    @staticmethod
    def visualStyleName(id: _n_2_t_0) -> str:...
    @staticmethod
    def VpMaxCommand():...
    @staticmethod
    def VpMinCommand():...
    @staticmethod
    def WcMatchEx(str: str, pattern: str, ignoreCase: bool) -> bool:...
    @staticmethod
    def WorkspaceVisible(strWS: str) -> bool:...
    @staticmethod
    def WriteToCommandLine(message: str):...
    @staticmethod
    def WriteUndoBoundary(db: _n_2_t_3, boundary: UndoBoundaryEnum, name: str) -> bool:...
    @staticmethod
    def Zoom():...
    @staticmethod
    def ZoomAuto(type: int, a1: float, a2: float, a3: float, a4: float):...
    @staticmethod
    def ZoomObjects(use3d: bool):...
    class BubbleWindowIconType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        Critical: int
        Information: int
        _None: int
        value__: int
        Warning: int
    class MenuBuilder(object):
        @property
        def Root(self) -> _n_20_t_0:"""Root { get; } -> MenuItem"""
        def __init__(self) -> Utils.MenuBuilder:...
        def GetFirstLevelFunctionPointer(self) -> _n_8_t_0:...
        def GetSecondLevelFunctionPointer(self) -> _n_8_t_0:...
    class MeshConversionType(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        ConvertToFacetedASM: int
        ConvertToSmoothASM: int
        FilterMeshObjects: int
        UserBreak: int
        value__: int
    class OSnapCommand(_n_23_t_0):
        def __init__(self, b3DOsnap: bool) -> Utils.OSnapCommand:...
class ViewUtil(object):
    @property
    def GsLensLength(self) -> float:"""GsLensLength { get; set; } -> float"""
    def __init__(self) -> ViewUtil:...
    @staticmethod
    def acquireView(nVPNum: int, pView: object, pGraphicsKernel: object):...
    @staticmethod
    def GetCurrentViewportNumber() -> int:...
    @staticmethod
    def releaseView(pView: object, pGraphicsKernel: object):...
class VisualStyleSet(_n_6_t_3, _n_8_t_11, _n_8_t_7):
    def __init__(self) -> VisualStyleSet:...
    def Intialize(self, objIds: _n_2_t_1, pRemoveFromSet: VisualStyleSet, pOverrideColor: _n_1_t_0):...
    def RemoveAll(self):...
    def Replace(self, objIds: _n_2_t_1, pRemoveFromSet: VisualStyleSet):...
class WebServiceMultipartRequest(object):
    @property
    def Parameters(self) -> _n_10_t_1[str, str]:"""Parameters { get; } -> Dictionary"""
    @property
    def Request(self) -> _n_17_t_0:"""Request { get; } -> HttpWebRequest"""
    def __init__(self, request: _n_17_t_0, boundary: str) -> WebServiceMultipartRequest:...
    def __init__(self, request: _n_17_t_0) -> WebServiceMultipartRequest:...
    def AddFileContentPart(self, fileStream: _n_16_t_0, paramName: str, fileName: str, contentType: str):...
    def AddFileContentPart(self, fileStream: _n_16_t_0, name: str, fileName: str):...
    def BeginMultipartContent(self):...
    def EndMultipartContent(self):...
class WebServicePostRequest(object):
    @property
    def Parameters(self) -> _n_10_t_1[str, str]:"""Parameters { get; } -> Dictionary"""
    @property
    def Request(self) -> _n_17_t_0:"""Request { get; } -> HttpWebRequest"""
    def __init__(self, request: _n_17_t_0) -> WebServicePostRequest:...
    def __init__(self, request: _n_17_t_0, skipParameterFormatting: bool) -> WebServicePostRequest:...
    def UpdateRequestContent(self):...
class WebServiceRequestParam(object):
    def __init__(self, name: str, value: str) -> WebServiceRequestParam:...
    def __init__(self, name: _n_8_t_13[_n_8_t_17], value: _n_8_t_13[_n_8_t_17]) -> WebServiceRequestParam:...
class WebServiceRequestParsingMode(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    ParseForHeaderArguments: int
    ParseForInlineQuery: int
    ParseForRequestContent: int
    ParseForSignatureBaseString: int
    value__: int
class WebServicesRequestUrlCode(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
    AccountServerUrl: int
    ExchangeUrl: int
    LoggedInUrlEndPoint: int
    NitrogenStorageEndPoint: int
    NitrousStorageEndPoint: int
    RegisterEndPoint: int
    ShareUrl: int
    StorageApiUrl: int
    StorageOnlineUrl: int
    StorageRoot: int
    UpdateProfileEndPoint: int
    value__: int
class WSUtils(object):
    def __init__(self) -> WSUtils:...
    @staticmethod
    def GetLoginUserName() -> str:...
    @staticmethod
    def GetServer() -> WSUtils.Server:...
    @staticmethod
    def GetUrl(urlCode: WebServicesRequestUrlCode) -> str:...
    @staticmethod
    def IsLoggedIn() -> bool:...
    @staticmethod
    def IsLoginValid() -> bool:...
    @staticmethod
    def Login() -> bool:...
    @staticmethod
    def SignRequest(url: str, params: _n_8_t_13[WebServiceRequestParam], httpMethod: HttpMethod, parsingMode: WebServiceRequestParsingMode, consumerKey: str, consumerSecret: str) -> str:...
    @staticmethod
    def SignUrlForBrowser(url: str, isEncoded: bool) -> str:...
    class Server(_n_8_t_2, _n_8_t_3, _n_8_t_4, _n_8_t_5):
        DevelopmentServer: int
        ProductionServer: int
        StagingServer: int
        value__: int
class ZipExtractor(_n_8_t_11):
    @property
    def Files(self) -> _n_10_t_2[ZipExtractor.ZipFileInfo]:"""Files { get; } -> IEnumerable"""
    def __init__(self, zipFile: str, password: str) -> ZipExtractor:...
    def __init__(self, zipFile: str) -> ZipExtractor:...
    def Extract(self, file: ZipExtractor.ZipFileInfo, destination: str):...
    def ExtractAll(self, destination: str):...
    class ZipFileInfo(object):
        @property
        def CompressedSize(self) -> int:"""CompressedSize { get; set; } -> int"""
        @property
        def Crc(self) -> int:"""Crc { get; set; } -> int"""
        @property
        def FilePath(self) -> str:"""FilePath { get; set; } -> str"""
        @property
        def IsDirectory(self) -> bool:"""IsDirectory { get; } -> bool"""
        @property
        def LastWriteTime(self) -> _n_8_t_18:"""LastWriteTime { get; set; } -> DateTime"""
        @property
        def UncompressedSize(self) -> int:"""UncompressedSize { get; set; } -> int"""
