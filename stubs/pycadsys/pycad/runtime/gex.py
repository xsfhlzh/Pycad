from pycad.system import acge, acdb
import typing

def get_endpoints(curve3d: acge.Curve3d) -> typing.Tuple[acge.Point3d, acge.Point3d]:
    """
    获取GE曲线的端点

        curve3d: GE曲线
    """

def conv_to_nurb(curve3d: acge.Curve3d) -> acge.NurbCurve3d:
    """
    转换GE曲线为B样条, 支持直线/圆(弧)/椭圆(弧)/多段线
    
        curve3d: GE曲线
    """

def conv_to_db(curve3d: acge.Curve3d) -> acdb.Curve:
    """
    转换GE曲线为DB曲线
    
        curve3d: GE曲线
    """