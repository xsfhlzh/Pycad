from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import Type as _n_0_t_4
from __clrclasses__.System import Array as _n_0_t_5
from __clrclasses__.System.Collections import IList as _n_1_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_2_t_0
from __clrclasses__.System.Runtime.Remoting.Contexts import ContextAttribute as _n_3_t_0
from __clrclasses__.System.Runtime.Remoting.Contexts import IContextAttribute as _n_3_t_1
from __clrclasses__.System.Runtime.Remoting.Contexts import IContextProperty as _n_3_t_2
from __clrclasses__.System.Runtime.Remoting.Messaging import IMethodCallMessage as _n_4_t_0
from __clrclasses__.System.Runtime.Remoting.Messaging import IMethodReturnMessage as _n_4_t_1
import typing
class ActivatorLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AppDomain: int
    Construction: int
    Context: int
    Machine: int
    Process: int
    value__: int
class IActivator():
    @property
    def Level(self) -> ActivatorLevel:"""Level { get; } -> ActivatorLevel"""
    @property
    def NextActivator(self) -> IActivator:"""NextActivator { get; set; } -> IActivator"""
    def Activate(self, msg: IConstructionCallMessage) -> IConstructionReturnMessage:...
class IConstructionCallMessage(_n_4_t_0):
    @property
    def ActivationType(self) -> _n_0_t_4:"""ActivationType { get; } -> Type"""
    @property
    def ActivationTypeName(self) -> str:"""ActivationTypeName { get; } -> str"""
    @property
    def Activator(self) -> IActivator:"""Activator { get; set; } -> IActivator"""
    @property
    def CallSiteActivationAttributes(self) -> _n_0_t_5[object]:"""CallSiteActivationAttributes { get; } -> Array"""
    @property
    def ContextProperties(self) -> _n_1_t_0:"""ContextProperties { get; } -> IList"""
class IConstructionReturnMessage(_n_4_t_1):
    pass
class UrlAttribute(_n_3_t_0, _n_2_t_0, _n_3_t_1, _n_3_t_2):
    @property
    def UrlValue(self) -> str:"""UrlValue { get; } -> str"""
    def __init__(self, callsiteURL: str) -> UrlAttribute:...
