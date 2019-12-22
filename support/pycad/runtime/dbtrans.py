from pycad.system import *
from . import dbdict, upopen

class dbtrans(object):
    """
    事务简化类(上下文管理器) write by xsfhlzh

    dbtrans(owner: typing.Union[acap.Document, acdb.Database, str] = None, commit: bool = True)

    创建数据库事务，默认提交

    owner: acap.Document or acdb.Database or str, 文档或数据库实例或dwg文件名, 默认创建空的数据库

    commit: bool, 指定提交方式
    """
    _tables = (
        'BlockTable', 'LayerTable', 'TextStyleTable',
        'RegAppTable', 'DimStyleTable', 'LinetypeTable',
        'UcsTable', 'ViewTable', 'ViewportTable',
        'GroupDictionary', 'MLeaderStyleDictionary', 'MLStyleDictionary',
        'MaterialDictionary', 'TableStyleDictionary', 'VisualStyleDictionary',
        'ColorDictionary', 'PlotSettingsDictionary', 'PlotStyleNameDictionary',
        'LayoutDictionary')

    def __init__(self, owner = None, commit = True):
        if owner:
            case = switch(owner)
            if case[acap.Document]:
                self.Document = owner
                self.Database = self.Document.Database
            elif case[acdb.Database]:
                self.Database = owner
            elif case[str]:
                import System
                self.Database = acdb.Database(False, True)
                self.Database.ReadDwgFile(owner, System.IO.FileShare.Read, True, None)
                self.Database.CloseInput(True)
            else:
                raise TypeError
        else:
            self.Database = acdb.Database(True, True)
        self.Trans = self.Database.TransactionManager.StartTransaction()
        self.tables = {}
        self.commit = commit
    
    def __enter__(self):
        return self

    def __exit__(self, t, v, b):
        if b:
            self.Trans.Abort()
        elif self.commit:
            self.Trans.Commit()
        self.Trans.Dispose()

    @staticmethod
    def isnullid(id):
        """
        判断id是否为None或acdb.ObjectId.Null
        """
        return id in (None, acdb.ObjectId.Null)

    def getobject(self, objid, mode = acdb.OpenMode.ForRead, erased = False):
        """
        按打开模式和删除状态打开对象，默认以读方式打开
        """
        return self.Trans.GetObject(objid, mode, erased)

    def getobjectid(self, handle):
        """
        将句柄转换为ObjectId
        """
        h = acdb.Handle(long(handle, 16))
        return self.Database.GetObjectId(False, h, 0)

    def getrealobject(self, obj, t = acdb.DBObject):
        """
        按给定类型判断id是否是给定的类型，并返回对象
        """
        if isinstance(obj, acdb.ObjectId):
            obj = self.getobject(obj)
        if isinstance(obj, t):
            return obj

    def erase(self, *ents):
        for e in ents:
            with upopen(e):
                e.Erase()

    def _gettable(self, name):
        if name in self._tables:
            if name not in self.tables:
                tid = getattr(self.Database, name + 'Id')
                self.tables[name] = self.getobject(tid)
            return self.tables[name]

    #{符号表

    def addrecord(self, table, record):
        """
        添加符号表记录
        """
        with upopen(table):
            rid = table.Add(record)
            self.Trans.AddNewlyCreatedDBObject(record, True)
            return rid

    def getrecordfrom(self, souce, target, over, *names):
        """
        从给定的源符号表中复制数据，一般用于两个数据库间的数据拷贝
        """
        ids = acdb.ObjectIdCollection()
        for sid in (souce[name] for name in names):
            if not dbtrans.isnullid(sid): ids.Add(sid)
        idm = acdb.IdMapping()
        mode = over and acdb.DuplicateRecordCloning.Replace or acdb.DuplicateRecordCloning.Ignore
        souce.Database.WblockCloneObjects(ids, target, idm, mode, False)
        return idm  

    @property
    def BlockTable(self):
        """
        块表
        """
        return self._gettable('BlockTable')
        
    def opencurrspace(self, openMode = acdb.OpenMode.ForRead, openErased = False):
        """
        打开当前空间
        """
        return self.getobject(self.Database.CurrentSpaceId, openMode, openErased)

    def addblock(self, name, *ents):
        """
        新建块表记录
        """
        bt = self.BlockTable
        if bt.Has(name): return bt[name]
        btr = acdb.BlockTableRecord()
        btr.Name = name
        btrid = self.addrecord(bt, btr)
        self.addentity(btr, *ents)
        return btrid

    def openblockdef(self, name, openMode = acdb.OpenMode.ForRead, openErased = False):
        """
        打开给定名称或Id的块表记录
        """
        if isinstance(name, str):
            return self.getobject(self.BlockTable[name], openMode, openErased)
        elif isinstance(name, acdb.ObjectId):
            return self.getobject(name, openMode, openErased)

    def openpaperspace(self, openMode = acdb.OpenMode.ForRead, openErased = False):
        """
        打开图纸空间
        """
        return self.getobject(self.BlockTable[acdb.BlockTableRecord.PaperSpace], openMode, openErased)

    def openmodelspace(self, openMode = acdb.OpenMode.ForRead, openErased = False):
        """
        打开模型空间
        """
        return self.getobject(self.BlockTable[acdb.BlockTableRecord.ModelSpace], openMode, openErased)

    @property
    def DimStyleTable(self):
        """
        标注样式表
        """
        return self._gettable('DimStyleTable')

    @property
    def LayerTable(self):
        """
        层表
        """
        return self._gettable('LayerTable')
        
    def createlayer(self, name, color = None, linetypeid = None, lineweight = None):
        """
        在层表中添加记录，并返回层表记录
        """
        ltr = acdb.LayerTableRecord()
        ltr.Name = name
        if color: ltr.Color = color
        if dbtrans.isnullid(linetypeid):
            linetypeid = self.LinetypeTable['Continuous']
        ltr.LineWeight = lineweight or acdb.LineWeight.LineWeight000
        ltr.LinetypeObjectId = linetypeid
        return ltr

    def addlayer(self, name, color = None, linetypeid = None, lineweight = None):
        """
        新建层表记录
        """
        lt = self.LayerTable
        if lt.Has(name): return lt[name]
        ltr = self.createlayer(name, color, linetypeid, lineweight)
        return self.addrecord(lt, ltr)

    @property
    def TextStyleTable(self):
        """
        文字样式表
        """
        return self._gettable('TextStyleTable')
        
    def createtextstyle(self, name, font, xscale = 1, bigfont = None):
        """
        创建文字样式表记录
        """
        tstr = acdb.TextStyleTableRecord()
        tstr.Name = name
        tstr.FileName = font
        if bigfont: tstr.BigFontFileName = bigfont
        tstr.XScale = xscale
        return tstr

    def addtextstyle(self, name, font, xscale = 1, bigfont = None):
        """
        在文字样式表中添加记录，并返回文字样式表记录
        """
        tst = self.TextStyleTable
        if tst.Has(name): return tst[name]
        tstr = self.createtextstyle(name, font, xscale, bigfont)
        return self.addrecord(tst, tstr)

    @property
    def RegAppTable(self):
        """
        应用程序名表
        """
        return self._gettable('RegAppTable')

    def addregapp(self, name):
        """
        在应用程序名表中添加记录，并返回应用程序名表记录
        """
        rat = self.RegAppTable
        if rat.Has(name): return rat[name]
        ratr = acdb.RegAppTableRecord()
        ratr.Name = name
        return self.addrecord(rat, ratr)

    @property
    def LinetypeTable(self):
        """
        线型表
        """
        return self._gettable('LinetypeTable')

    @property
    def UcsTable(self):
        """
        用户坐标系表
        """
        return self._gettable('UcsTable')

    @property
    def ViewTable(self):
        """
        视图表
        """
        return self._gettable('ViewTable')

    @property
    def ViewportTable(self):
        """
        视口表
        """
        return self._gettable('ViewportTable')

    def getdict(self, owner = None, *names):
        """
        按名字序列获取字典的封装

        owner:
        
        如果为空(默认)返回命名字典;
        
        如果是字符串返回命名字典下的子字典;
        
        如果是字典(或字典Id)返回字典的封装;
        
        否则返回对象字典

        names:
        
        子字典名称列表
        """
        if not owner:
            return dbdict(self.Database.NamedObjectsDictionaryId, self)
        if isinstance(owner, acdb.ObjectId):
            owner = self.getobject(owner)
        if isinstance(owner, acdb.DBDictionary):
            d = dbdict(owner, self)
        elif isinstance(owner, acdb.DBObject):
            if owner.ExtensionDictionary == acdb.ObjectId.Null:
                with upopen(owner):
                    owner.CreateExtensionDictionary()
            d = dbdict(owner.ExtensionDictionary, self)
        elif isinstance(owner, str):
            d = dbdict(self.Database.NamedObjectsDictionaryId, self).getchild(owner)
        else:
            return
        for name in names:
            d = d.getchild(name)
        return d

    @property
    def GroupDictionary(self):
        """
        编组字典
        """
        return self._gettable('GroupDictionary')
        
    def addgroup(self, name, *ids):
        """
        添加组，并返回组Id
        """
        gd = self.GroupDictionary
        if gd.Contains(name):
            return acdb.ObjectId.Null
        else:
            with upopen(gd):
                g = acdb.Group()
                for id in ids:
                    g.Append(id)
                gd.SetAt(name, g)
                self.Trans.AddNewlyCreatedDBObject(g, True)
            return g.ObjectId

    def getgroups(self, ent):
        """
        按实体对象获取组
        """
        for id in ent.GetPersistentReactorIds():
            obj = self.getobject(id)
            if isinstance(obj, acdb.Group):
                yield obj

    @property
    def MLeaderStyleDictionary(self):
        """
        多重引线样式字典
        """
        return self._gettable('MLeaderStyleDictionary')

    @property
    def MLStyleDictionary(self):
        """
        多线样式字典
        """
        return self._gettable('MLStyleDictionary')

    @property
    def MaterialDictionary(self):
        """
        材质字典
        """
        return self._gettable('MaterialDictionary')

    @property
    def TableStyleDictionary(self):
        """
        表格样式字典
        """
        return self._gettable('TableStyleDictionary')

    @property
    def VisualStyleDictionary(self):
        """
        视觉样式字典
        """
        return self._gettable('VisualStyleDictionary')

    @property
    def ColorDictionary(self):
        """
        颜色字典
        """
        return self._gettable('ColorDictionary')

    @property
    def PlotSettingsDictionary(self):
        """
        打印设置字典
        """
        return self._gettable('PlotSettingsDictionary')

    @property
    def PlotStyleNameDictionary(self):
        """
        打印样式名字典
        """
        return self._gettable('PlotStyleNameDictionary')

    @property
    def LayoutDictionary(self):
        """
        布局字典
        """
        return self._gettable('LayoutDictionary')

    #实体

    def addentity(self, btr, *ents):
        """
        向块表记录中加入实体[集合]
        """
        ids = []
        with upopen(btr):
            for ent in ents:
                ids.append(btr.AppendEntity(ent))
                self.Trans.AddNewlyCreatedDBObject(ent, True)
        return ids

    def flush(self, ent):
        """
        刷新单个实体的显示图形
        """
        ent.RecordGraphicsModified(True)
        self.Trans.TransactionManager.QueueForGraphicsFlush()

    #块引用

    def clipblockref(self, bref, *pt3ds):
        """
        用多边形剪切块引用
        """
        mat = bref.BlockTransform.Inverse()
        pts = (pt.TransformBy(mat) for pt in pt3ds)
        pts = acge.Point2dCollection(tuple((acge.Point2d(pt.X, pt.Y) for pt in pts)))
        sf = acdb.Filters.SpatialFilter()
        sf.Definition = acdb.Filters.SpatialFilterDefinition(pts, acge.Vector3d.ZAxis, 0, 0, 0, True)
        self.settodict(sf, bref, "ACAD_FILTER", "SPATIAL")

    def appendatts(self, bref, atts):
        """
        向块引用添加属性引用[集合]
        """
        bdef = self.getobject(bref.BlockTableRecord)
        if bdef.HasAttributeDefinitions:
            attribs = {}
            i = 0
            for eid in bdef:
                attdef = self.getobject(i)
                if isinstance(attdef, acdb.AttributeDefinition):
                    if not (attdef.Constant or attdef.Invisible):
                        attref = acdb.AttributeReference()
                        attref.SetAttributeFromBlock(attdef, bref.BlockTransform)
                    if i < atts.Count:
                        attref.TextString = atts[i]
                    else:
                        attref.TextString = attdef.TextString
                    i += 1
                    bref.AttributeCollection.AppendAttribute(attref)
                    self.Trans.AddNewlyCreatedDBObject(attref, True)
                    attribs[attdef] = attref
            return attribs

    def appendattsfromdef(self, bref, atts):
        """
        按给定的属性定义向块引用添加属性引用[集合]
        """
        attribs = {}
        for i in range(atts.Count):
            attdef = atts[i]
            attref = acdb.AttributeReference()
            attref.SetAttributeFromBlock(attdef, bref.BlockTransform)
            attref.TextString = attdef.TextString
            bref.AttributeCollection.AppendAttribute(attref)
            self.Trans.AddNewlyCreatedDBObject(attref, True)
            attribs[attdef] = attref
        return attribs

    def dragblock(self, bref, attribs = None):
        """
        拖动式插入块引用
        """
        jig = brefjig(self.Document.Editor, bref, attribs)
        if jig.move() and jig.rotate():
            return True
        bref.Erase()
        return False

class brefjig(aced.EntityJig):
    '''块引用拖动类'''
    
    def __new__(cls, ed, bref, attribs):
        return aced.EntityJig.__new__(cls, bref)
        
    def __init__(self, ed, bref, attribs):
        self.position = acge.Point3d()
        self.angle = 0
        self.ed = ed
        self.ucs = self.ed.CurrentUserCoordinateSystem
        self.attribs = attribs
        self.Update()

    def Sampler(self, prompts):
        if self.it == 0:
            opts = aced.JigPromptPointOptions("\n请输入基点:")
            opts.UserInputControls = \
                aced.UserInputControls.Accept3dCoordinates | \
                aced.UserInputControls.NoZeroResponseAccepted | \
                aced.UserInputControls.NoNegativeResponseAccepted
            res = prompts.AcquirePoint(opts)
            if res.Status == aced.PromptStatus.OK:
                if self.position == res.Value:
                    return aced.SamplerStatus.NoChange
                else:
                    self.position = res.Value
                    return aced.SamplerStatus.OK
            return aced.SamplerStatus.Cancel
        elif self.it == 1:
            opts = aced.JigPromptAngleOptions("\n请输入旋转角度:")
            opts.UserInputControls = \
                aced.UserInputControls.Accept3dCoordinates | \
                aced.UserInputControls.NoNegativeResponseAccepted | \
                aced.UserInputControls.GovernedByUCSDetect | \
                aced.UserInputControls.UseBasePointElevation
            opts.UseBasePoint = True
            opts.BasePoint = self.position
            opts.Cursor = aced.CursorType.RubberBand
            res = prompts.AcquireAngle(opts)
            if res.Status == aced.PromptStatus.OK:
                if self.angle == res.Value:
                    return aced.SamplerStatus.NoChange
                else:
                    self.angle = res.Value
                    return aced.SamplerStatus.OK
            return aced.SamplerStatus.Cancel
        else:
            return aced.SamplerStatus.Cancel

    def Update(self):
        try:
            bref = self.Entity
            bref.Normal = acge.Vector3d.ZAxis
            bref.Position = self.position.TransformBy(self.ucs.Inverse())
            bref.Rotation = self.angle
            bref.TransformBy(self.ucs)
            #将属性引用按块引用的Ocs矩阵变换
            if self.attribs:
                mat = bref.BlockTransform
                for key, value in self.attribs.items():
                    s = value.TextString
                    value.SetAttributeFromBlock(key, mat)
                    value.TextString = s
            return True
        except:
            return False

    def move(self):
        self.it = 0
        return self.ed.Drag(self).Status == aced.PromptStatus.OK
        
    def rotate(self):
        self.it = 1
        return self.ed.Drag(self).Status == aced.PromptStatus.OK
