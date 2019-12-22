
mgds = {
    'acad': {
        'mgds': (
            ('acmgd.dll', 'acdbmgd.dll', 'accoremgd.dll'), 
            ('acmgdinternal.dll'), 
            ('System', 'System.Core')),
        'nss': {
            "acap": "Autodesk.AutoCAD.ApplicationServices",
            "acdb": "Autodesk.AutoCAD.DatabaseServices",
            "aced": "Autodesk.AutoCAD.EditorInput",
            "acge": "Autodesk.AutoCAD.Geometry",
            "acrx": "Autodesk.AutoCAD.Runtime",
            "acws": "Autodesk.AutoCAD.Windows",
            "acgi": "Autodesk.AutoCAD.GraphicsInterface",
            "acgs": "Autodesk.AutoCAD.GraphicsSystem",
            "acin": "Autodesk.AutoCAD.Internal",
            "acps": "Autodesk.AutoCAD.PlottingServices",
            "acco": "Autodesk.AutoCAD.Colors",
            }
        },
    'acore': {
        'mgds': (
            ('acdbmgd.dll', 'accoremgd.dll'), 
            ('System', 'System.Core')),
        'nss': {
            "acap": "Autodesk.AutoCAD.ApplicationServices",
            "acdb": "Autodesk.AutoCAD.DatabaseServices",
            "aced": "Autodesk.AutoCAD.EditorInput",
            "acge": "Autodesk.AutoCAD.Geometry",
            "acrx": "Autodesk.AutoCAD.Runtime",
            "acws": "Autodesk.AutoCAD.Windows",
            "acgi": "Autodesk.AutoCAD.GraphicsInterface",
            "acgs": "Autodesk.AutoCAD.GraphicsSystem",
            "acin": "Autodesk.AutoCAD.Internal",
            "acps": "Autodesk.AutoCAD.PlottingServices",
            "acco": "Autodesk.AutoCAD.Colors",
            }
        },
    'gcad': {
        'mgds': (
            ('gmap.dll', 'gmdb.dll'),
            ('System', 'System.Core')),
        'nss': {
            "acap": "GrxCAD.ApplicationServices",
            "acdb": "GrxCAD.DatabaseServices",
            "aced": "GrxCAD.EditorInput",
            "acge": "GrxCAD.Geometry",
            "acrx": "GrxCAD.Runtime",
            "acws": "GrxCAD.Windows",
            "acgi": "GrxCAD.GraphicsInterface",
            "acgs": "GrxCAD.GraphicsSystem",
            "acin": "GrxCAD.Internal",
            "acps": "GrxCAD.PlottingServices",
            "acco": "GrxCAD.Colors",
            }
        }
    }

from NFox.Pycad.Core.Application import CurrSystem
_mgds = mgds[CurrSystem]['mgds']
_nss = mgds[CurrSystem]['nss']

#加载程序集
import clr
_gen = (mgd for cmgds in _mgds for mgd in cmgds)
for mgd in _gen:
    try: clr.AddReference(mgd)
    except: pass

for _key, _value in _nss.items():
    try: exec("import %s as %s" % (_value, _key))
    except: pass

__all__ = _nss.keys()