import __clrclasses__.Autodesk.AutoCAD.DatabaseServices as DatabaseServices
import __clrclasses__.Autodesk.AutoCAD.Geometry as Geometry
import __clrclasses__.Autodesk.AutoCAD.GraphicsInterface as GraphicsInterface
import __clrclasses__.Autodesk.AutoCAD.Colors as Colors
import __clrclasses__.Autodesk.AutoCAD.LayerManager as LayerManager
import __clrclasses__.Autodesk.AutoCAD.ComponentModel as ComponentModel
import __clrclasses__.Autodesk.AutoCAD.Windows as Windows
import __clrclasses__.Autodesk.AutoCAD.Internal as Internal
import __clrclasses__.Autodesk.AutoCAD.ApplicationServices as ApplicationServices
import __clrclasses__.Autodesk.AutoCAD.EditorInput as EditorInput
import __clrclasses__.Autodesk.AutoCAD.Runtime as Runtime
import __clrclasses__.Autodesk.AutoCAD.PlottingServices as PlottingServices
import __clrclasses__.Autodesk.AutoCAD.Publishing as Publishing
import __clrclasses__.Autodesk.AutoCAD.GraphicsSystem as GraphicsSystem
from __clrclasses__.Autodesk.AutoCAD.Runtime import DisposableWrapper as _n_0_t_0
from __clrclasses__.System import IDisposable as _n_1_t_0
import typing
class UniqueString(_n_0_t_0, _n_1_t_0):
    @staticmethod
    def Intern(A_0: str) -> UniqueString:...
