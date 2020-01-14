from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_1_t_0
from __clrclasses__.System.Security import CodeAccessPermission as _n_2_t_0
from __clrclasses__.System.Security import IPermission as _n_2_t_1
from __clrclasses__.System.Security import IStackWalk as _n_2_t_2
from __clrclasses__.System.Security.Permissions import IUnrestrictedPermission as _n_3_t_0
from __clrclasses__.System.Security.Permissions import PermissionState as _n_3_t_1
from __clrclasses__.System.Security.Permissions import CodeAccessSecurityAttribute as _n_3_t_2
from __clrclasses__.System.Security.Permissions import SecurityAction as _n_3_t_3
import typing
class AspNetHostingPermission(_n_2_t_0, _n_2_t_1, _n_2_t_2, _n_3_t_0):
    @property
    def Level(self) -> AspNetHostingPermissionLevel:"""Level { get; set; } -> AspNetHostingPermissionLevel"""
    def __init__(self, level: AspNetHostingPermissionLevel) -> AspNetHostingPermission:...
    def __init__(self, state: _n_3_t_1) -> AspNetHostingPermission:...
class AspNetHostingPermissionAttribute(_n_3_t_2, _n_1_t_0):
    @property
    def Level(self) -> AspNetHostingPermissionLevel:"""Level { get; set; } -> AspNetHostingPermissionLevel"""
    def __init__(self, action: _n_3_t_3) -> AspNetHostingPermissionAttribute:...
class AspNetHostingPermissionLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    High: int
    Low: int
    Medium: int
    Minimal: int
    _None: int
    Unrestricted: int
    value__: int
