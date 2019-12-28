from pycad.system import *
from pycad.runtime import *

from random import uniform
pts = [acge.Point3d(uniform(0, 100), uniform(0, 100), 0) for i in range(10000)]

@command()
@showtime
def pysort(doc):
    #用py的方式对点集排序,按索引排序,对应点的XY坐标
    from operator import itemgetter, attrgetter
    lst = sorted(pts, key = itemgetter(0, 1))
    #lst = sorted(pts, key = attrgetter("X", "Y"))
    

@command()
@showtime
def linqsort(doc):
    #linq排序,先按X排序,X相同的再按Y排序
    import clr, System
    clr.ImportExtensions(System.Linq)
    q = (
    pts.Cast[acge.Point3d]()
    .OrderBy(lambda p: p.X)
    .ThenBy(lambda p: p.Y))
    print(q)