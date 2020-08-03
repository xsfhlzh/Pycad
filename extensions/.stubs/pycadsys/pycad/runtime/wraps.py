from pycad.system import *
import typing

class dbtrans:
    def __init__(self, owner: typing.Union[acap.Document, acdb.Database, str], commit: bool):
        """
        事务简化类(上下文管理器) write by xsfhlzh
        
        创建数据库事务，默认提交

            owner: 文档或数据库实例或dwg文件名, 默认创建空的数据库
            commit: 指定提交方式, 默认提交
        """
        self.Document: acap.Document
        self.Database: acdb.Database
        self.Trans: acdb.Transaction

    def __enter__(self) -> dbtrans:...

    @staticmethod
    def isnullid(id: acdb.ObjectId) -> bool:
        """
        判断id是否为None或acdb.ObjectId.Null
        """

    def erase(self, *objs: typing.Iterable[acdb.DBObject]):
        """
        删除数据库对象
        """

    def getobject(self, objid: acdb.ObjectId, mode: acdb.OpenMode = acdb.OpenMode.ForRead, erased:bool = False) -> acdb.DBObject:
        """
        按打开模式和删除状态打开对象，默认以读方式打开
        """
    def getobjectid(self, handle: str) -> acdb.ObjectId:
        """
        将句柄转换为ObjectId
        """
    def getrealobject(self, obj: typing.Union[acdb.ObjectId, acdb.DBObject], type: type = acdb.DBObject) -> acdb.DBObject:
        """
        按给定类型判断id是否是给定的类型，并返回对象
        """
    def addrecord(self, table: acdb.SymbolTable, record: acdb.SymbolTableRecord) -> acdb.ObjectId:
        """
        添加符号表记录
        """
    def getrecordfrom(self, souce: acdb.SymbolTable, target: acdb.SymbolTable, over: bool, *names: typing.Iterable[str]) -> acdb.IdMapping:
        """
        从给定的源符号表中复制数据，一般用于两个数据库间的数据拷贝
        """
    @property
    def BlockTable(self) -> acdb.BlockTable:
        """
        块表
        """
    def opencurrspace(self, openMode: acdb.OpenMode = acdb.OpenMode.ForRead, openErased: bool = False) -> acdb.BlockTableRecord:
        """
        打开当前空间
        """
    def addblock(self, name: str, *ents: typing.Iterable[acdb.Entity]) -> acdb.ObjectId:
        """
        新建块表记录
        """
    def openblockdef(self, name: str, openMode: acdb.OpenMode = acdb.OpenMode.ForRead, openErased: bool = False):
        """
        打开给定名称或Id的块表记录
        """
    def openpaperspace(self, openMode: acdb.OpenMode = acdb.OpenMode.ForRead, openErased: bool = False) -> acdb.BlockTableRecord:
        """
        打开图纸空间
        """
    def openmodelspace(self, openMode: acdb.OpenMode = acdb.OpenMode.ForRead, openErased: bool = False) -> acdb.BlockTableRecord:
        """
        打开模型空间
        """

    @property
    def DimStyleTable(self) -> acdb.DimStyleTable:
        """
        标注样式表
        """

    @property
    def LayerTable(self) -> acdb.LayerTable:
        """
        层表
        """
    def createlayer(self, name, color = None, linetypeid: typing.Optional[acdb.ObjectId] = None, lineweight: typing.Optional[acdb.LineWeight] = None) -> acdb.LayerTableRecord:
        """
        在层表中添加记录，并返回层表记录
        """
    def addlayer(self, name, color = None, linetypeid: typing.Optional[acdb.ObjectId] = None, lineweight: typing.Optional[acdb.LineWeight] = None) -> acdb.LayerTableRecord:
        """
        新建层表记录
        """

    @property
    def TextStyleTable(self) -> acdb.TextStyleTable:
        """
        文字样式表
        """
    def createtextstyle(self, name: str, font: str, xscale: float = 1, bigfont: typing.Optional[str] = None) -> acdb.TextStyleTable:
        """
        创建文字样式表记录
        """
    def addtextstyle(self, name: str, font: str, xscale: float = 1, bigfont: typing.Optional[str] = None) -> acdb.TextStyleTable:
        """
        在文字样式表中添加记录，并返回文字样式表记录
        """

    @property
    def RegAppTable(self) -> acdb.RegAppTable:
        """
        应用程序名表
        """
    def addregapp(self, name: str) -> acdb.RegAppTable:
        """
        在应用程序名表中添加记录，并返回应用程序名表记录
        """

    @property
    def LinetypeTable(self) -> acdb.LinetypeTable:
        """
        线型表
        """

    @property
    def UcsTable(self) -> acdb.UcsTable:
        """
        用户坐标系表
        """

    @property
    def ViewTable(self) -> acdb.ViewTable:
        """
        视图表
        """

    @property
    def ViewportTable(self) -> acdb.ViewportTable:
        """
        视口表
        """

    def getdict(self, owner: typing.Union[acdb.ObjectId, acdb.DBObject, str]=None, *names: typing.Iterable[str]) -> dbdict:
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

    @property
    def GroupDictionary(self) -> acdb.DBDictionary:
        """
        编组字典
        """
    def addgroup(self, name: str, *ids: typing.Iterable[acdb.ObjectId]) -> acdb.ObjectId:
        """
        添加组，并返回组Id
        """
    def getgroups(self, ent: acdb.Entity) -> typing.Iterable[acdb.Group]:
        """
        按实体对象获取组
        """

    @property
    def MLeaderStyleDictionary(self) -> acdb.DBDictionary:
        """
        多重引线样式字典
        """

    @property
    def MLStyleDictionary(self) -> acdb.DBDictionary:
        """
        多线样式字典
        """

    @property
    def MaterialDictionary(self) -> acdb.DBDictionary:
        """
        材质字典
        """

    @property
    def TableStyleDictionary(self) -> acdb.DBDictionary:
        """
        表格样式字典
        """

    @property
    def VisualStyleDictionary(self) -> acdb.DBDictionary:
        """
        视觉样式字典
        """

    @property
    def ColorDictionary(self) -> acdb.DBDictionary:
        """
        颜色字典
        """

    @property
    def PlotSettingsDictionary(self) -> acdb.DBDictionary:
        """
        打印设置字典
        """

    @property
    def PlotStyleNameDictionary(self) -> acdb.DBDictionary:
        """
        打印样式名字典
        """

    @property
    def LayoutDictionary(self) -> acdb.DBDictionary:
        """
        布局字典
        """

    def addentity(self, btr: acdb.BlockTableRecord, *ent: typing.Iterable[acdb.Entity]) -> typing.List[acdb.ObjectId]:
        """
        向块表记录中加入实体[集合]
        """

    def flush(self, ent: acdb.DBObject):
        """
        刷新单个实体的显示图形
        """

    def clipblockref(self, bref: acdb.BlockReference, *pt3ds: typing.Iterable[acgd.Point3d]):
        """
        用多边形裁剪块引用
        """

    def appendatts(self, bref: acdb.BlockReference, atts: typing.Iterable[str]) -> typing.Dict[acdb.AttributeDefinition ,acdb.AttributeReference]:
        """
        向块引用添加属性引用[集合]
        """
    
    def appendattsfromdef(self, bref: acdb.BlockReference, atts: typing.Iterable[acdb.AttributeDefinition]) -> typing.Dict[acdb.AttributeDefinition ,acdb.AttributeReference]:
        """
        按给定的属性定义向块引用添加属性引用[集合]
        """

    def dragblock(self, bref: acdb.BlockReference, attribs: typing.Dict[acdb.AttributeDefinition ,acdb.AttributeReference] = None) -> bool:
        """
        拖动式插入块引用
        """

class upopen:
    """
    提升acdb.DBObject对象的打开权限(上下文管理器)

    with upopen(obj): dosomething()
    """
    def __init__(self, obj: acdb.DBObject):...
    def __enter__(self):...

class cs(object):
    """
    读取注册表配置

    with cs.opencprofile() as cpf:

    tpaths = cpf.Variables['TRUSTEDPATHS']
    """
    @classmethod
    def opencprofile(cls) -> cs:
        """
        读取当前配置的数据
        """
    @classmethod
    def openglobal(cls) -> cs:
        """
        读取公共配置的数据
        """
    @classmethod
    def opendialog(cls, dialog) -> cs:
        """
        读取对话框配置的数据
        """
    def __enter__(self) -> cs:...
    def __getattr__(self, key: str) -> cs:...

class dbdict(typing.Mapping[str, acdb.DBObject]):
    """
    字典封装类
    """
    def __init__(self, d: typing.Union(acdb.ObjectId, acdb.DBObject), tr: dbtrans, parent: dbdict, othervalue: bool):...
    def __setitem__(self, key: str, value: acdb.DBObject):...
    def __getitem__(self, key: str) -> acdb.DBObject:...
    def __delitem__(self, key):...
    def getchild(self, key) -> dbdict:
        """
        获取子字典
        """
    def setxrecord(self, key: str, value: typing.Iterable):
        """
        将数据集转换为扩展数据,存入字典

        setxrecord(key, [[1000, "mydata"]])
        """
    def getxrecord(self, key: str) -> list:
        """
        从字典中获取扩展数据,并转换为数据集
        """

class serializable(object):
    class property(object):
        def __init__(self, objtype: typing.Optional[type] = None):...
        def __call__(self, fget) -> property:...
        def setter(self, fset) -> property:...
    def serialize(self) -> dict:...
    @classmethod
    def deserialize(cls, objdict: dict) -> serializable:...
    def dumps(self, stype: str = 'json') -> str:...
    @classmethod
    def loads(cls, s: str, stype: str = 'json') -> serializable:...
    @staticmethod
    def Type(objtype: type) -> serializable.property:...
    @staticmethod
    def Str(fget) -> serializable.property:...
    @staticmethod
    def Int(fget) -> serializable.property:...
    @staticmethod
    def Float(fget) -> serializable.property:...
    @staticmethod
    def Bool(fget) -> serializable.property:...

class invokeArx(object):
    @classmethod
    def load(cls, name):...
    @classmethod
    def lib(cls, name):...
    @classmethod
    def apply32(cls, entry, ver=-1):...
    @classmethod
    def apply64(cls, entry, ver=-1):...
    @classmethod
    def lisp(cls, *args):...