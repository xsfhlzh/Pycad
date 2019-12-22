import typing as __typing
from .mgdnss import *

acapp = None #type: acap.Application

def guid(gid : __typing.Optional[str] = None):...

class switch:
    """
    case = switch(value)

    if case(somevalue): dosomething

    if case[sometype]: dosomething

    if case > 0: dosomething

    if case.match(func): dosomething
    """
def flatten(nested) -> typing.Iterable:
    """
    展开生成器

    flatten([[1,'2'],3]) -> (1, '2', 3)
    """
