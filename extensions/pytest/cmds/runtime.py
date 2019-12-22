from pycad.system import *
from pycad.runtime import *

@command()
def cstest(doc):
    with cs.opencprofile() as cpf:
        tpaths = cpf.Variables['TRUSTEDPATHS']
        s = 'c:\\nfox'
        patt = '(^|;)%s(;|$)' % s
        import re
        m = re.search(patt, tpaths, re.IGNORECASE)
        if not m:
            print(';'.join((tpaths, s)))

@command(lock=False)
def switchtotest(doc):
    ed = doc.Editor #type: aced.Editor
    if doc.Database.TileMode: ed.SwitchToPaperSpace()
    else: ed.SwitchToModelSpace()

@command()
def cmdtest(doc):
    ed = doc.Editor #type: aced.Editor
    from random import uniform
    ed.Command(
        '._line',
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        '')
    ed.Command(
        '._line',
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        acge.Point3d(uniform(0, 100), uniform(0, 100), 0),
        '')
    print('\nOK!')

@command()
def dbxtest(doc):
    filename = 'd:\\test.dwg'
    with dbtrans(filename) as tr:
        btr = tr.openmodelspace()
        mat = acge.Matrix3d.Displacement(acge.Vector3d(10,0,0))
        for  eid in btr:
            ent = tr.getobject(eid) #type: acdb.Entity
            with upopen(ent):
                case = switch(ent)
                if case[acdb.Line]:
                    ent.LayerId = tr.LayerTable['1']
                elif case[acdb.DBText]:
                    ent.TransformBy(mat)
        tr.Database.SaveAs(filename, acdb.DwgVersion.Current)