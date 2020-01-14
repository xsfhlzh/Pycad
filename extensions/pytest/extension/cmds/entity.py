from pycad.system import *
from pycad.runtime import *


@command()
def helloworld(doc):
    #显示hello world!
    print('hello world!')
    #打开事务
    with dbtrans(doc) as tr:
        #打开当前空间
        btr = tr.opencurrspace()
        #向当前空间添加直线
        tr.addentity(btr, acdb.Line(acge.Point3d(0,0,0), acge.Point3d(10,10,0)))


@command()
def mtexttest(doc):
    with dbtrans(doc) as tr:
        #新建多行文字
        mt = acdb.MText()
        #设置属性
        mt.Location = acge.Point3d()
        mt.Contents = "123"
        mt.TextHeight = 5
        mt.Width = 10
        mt.Attachment = acdb.AttachmentPoint.BottomCenter
        #向当前空间添加
        tr.addentity(tr.opencurrspace(), mt)


@command()
def mtexttest2(doc):
    #获取文字图元
    res = edx.entsel("\n请选择文字:")
    if not res.ok(): return
    with dbtrans(doc) as tr:
        #获取对象
        txt = tr.getobject(res.ObjectId)
        #对象读写提权
        with upopen(txt):
            if isinstance(txt, acdb.DBText):
                txt.TextString = 'abc'
            elif isinstance(txt, acdb.MText):
                txt.Contents = 'abc'


@command()
def randtest(doc):
    #生成1w个测试点
    with dbtrans(doc) as tr:
        btr = tr.opencurrspace()
        from System import Guid, Random
        r = Random(Guid.NewGuid().GetHashCode())
        for i in range(10000):
            tr.addentity(btr, acdb.DBPoint(acge.Point3d(r.Next(0, 1000), r.Next(0, 1000), 0)))


@command()
@showtime
def mycir(doc):
    #测试使用cad标准方式生成10W个随机圆的时间
    db = doc.Database
    from random import uniform
    with db.TransactionManager.StartTransaction() as tr:
        btr = tr.GetObject(db.CurrentSpaceId, acdb.OpenMode.ForRead)
        btr.UpgradeOpen()
        cirs = (
            acdb.Circle(acge.Point3d(uniform(0, 10000), uniform(0, 10000), 0), acge.Vector3d.ZAxis, 2)
            for i in range(100000))
        for cir in cirs:
            btr.AppendEntity(cir)
            tr.AddNewlyCreatedDBObject(cir, True)
        btr.DowngradeOpen()
        tr.Commit()


@command()
@showtime
def mycir2(doc):
    #测试使用dbtrans类生成10W个随机圆的时间
    from random import uniform
    with dbtrans(doc) as tr:
        btr = tr.opencurrspace()
        cirs = (
            acdb.Circle(acge.Point3d(uniform(0, 10000), uniform(0, 10000), 0), acge.Vector3d.ZAxis, 2)
            for i in range(100000))
        tr.addentity(btr, *cirs)


@command()
@showtime
def mycir3(doc):
    #测试使用多事务生成10W个随机圆的时间
    db = doc.Database  #type: acdb.Database
    from random import uniform
    cirs = (
        acdb.Circle(acge.Point3d(uniform(0, 10000), uniform(0, 10000), 0), acge.Vector3d.ZAxis, 2)
        for i in range(100000))
    for cir in cirs:
        with db.TransactionManager.StartTransaction() as tr:
            btr = tr.GetObject(db.CurrentSpaceId, acdb.OpenMode.ForRead)  #type: acdb.BlockTableRecord
            btr.UpgradeOpen()
            btr.AppendEntity(cir)
            tr.AddNewlyCreatedDBObject(cir, True)
            btr.DowngradeOpen()
            tr.Commit()


@command()
def myline(doc):
    with dbtrans(doc) as tr:
        #获取起点
        respt = edx.getpoint('指定第一个点:')
        if not respt.ok(): return
        start = respt.value
        #获取第二点
        opts = aced.PromptPointOptions('\n指定下一点')
        opts.AllowNone = True
        opts.BasePoint = start
        opts.UseBasePoint = True
        opts.UseDashedLine = False
        respt2 = edx.getpoint(opts)
        btr = tr.opencurrspace()
        while respt2.ok():
            end = respt2.value
            #循环生成直线并显示
            line = acdb.Line(start, end)
            tr.addentity(btr, line)
            tr.flush(line)
            #获取下一点
            opts.BasePoint = start = end
            respt2 = edx.getpoint(opts)


@command()
def myline2(doc):
    #模拟直线命令
    with dbtrans(doc) as tr:
        btr = tr.opencurrspace()
        lines, pts = [], []
        while True:
            n = len(pts)
            if n == 0:
                #获取起点
                respt = edx.getpoint('\n指定第一个点:')
                if not respt.ok(): return
                pts.append(respt.value)
            else:
                if n > 2:
                    opts = aced.PromptPointOptions(
                        '\n指定下一点或[闭合(C)/放弃(U)]', 'C U')
                else:
                    opts = aced.PromptPointOptions(
                        '\n指定下一点或[放弃(U)]', 'U')
                #获取下一点
                opts.AllowNone = True
                opts.BasePoint = pts[-1]
                opts.UseBasePoint = True
                opts.UseDashedLine = False
                respt = edx.getpoint(opts)
                if respt.ok():
                    #如果正确输入点就添加一条直线
                    pt = respt.value
                    if n > 0:
                        line = acdb.Line(pts[-1], pt)
                        tr.addentity(btr, line)
                        tr.flush(line)
                        lines.append(line)
                        pts.append(pt)
                elif respt.keyword('C'):
                    #如果输入关键字C则闭合并退出
                    line = acdb.Line(pts[-1], pts[0])
                    tr.addentity(btr, line)
                    break
                elif respt.keyword('U'):
                    #如果输入关键字U则回退
                    del pts[-1]
                    if n > 1:
                        lines[-1].Erase()
                        tr.flush(line)
                        del lines[-1]
                else: break


@command()
def mypl3d(doc):
    #获取图元时按类型过滤
    opts = aced.PromptEntityOptions('\n选择三维多段线')
    opts.SetRejectMessage('错误类型')
    opts.AddAllowedClass(acdb.Polyline3d, False)
    res = edx.entsel(opts)
    if not res.ok(): return
    with dbtrans(doc, False) as tr:
        pl = tr.getobject(res.ObjectId)
        #遍历三维多段线, 显示折点坐标
        for i in pl:
            print(tr.getobject(i).Position)
