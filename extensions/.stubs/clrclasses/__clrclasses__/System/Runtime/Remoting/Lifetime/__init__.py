from __clrclasses__.System import MarshalByRefObject as _n_0_t_0
from __clrclasses__.System import TimeSpan as _n_0_t_1
from __clrclasses__.System import Enum as _n_0_t_2
from __clrclasses__.System import IComparable as _n_0_t_3
from __clrclasses__.System import IFormattable as _n_0_t_4
from __clrclasses__.System import IConvertible as _n_0_t_5
import typing
class ClientSponsor(_n_0_t_0, ISponsor):
    @property
    def RenewalTime(self) -> _n_0_t_1:"""RenewalTime { get; set; } -> TimeSpan"""
    def __init__(self, renewalTime: _n_0_t_1) -> ClientSponsor:...
    def __init__(self) -> ClientSponsor:...
    def Close(self):...
    def Register(self, obj: _n_0_t_0) -> bool:...
    def Unregister(self, obj: _n_0_t_0):...
class ILease():
    @property
    def CurrentLeaseTime(self) -> _n_0_t_1:"""CurrentLeaseTime { get; } -> TimeSpan"""
    @property
    def CurrentState(self) -> LeaseState:"""CurrentState { get; } -> LeaseState"""
    @property
    def InitialLeaseTime(self) -> _n_0_t_1:"""InitialLeaseTime { get; set; } -> TimeSpan"""
    @property
    def RenewOnCallTime(self) -> _n_0_t_1:"""RenewOnCallTime { get; set; } -> TimeSpan"""
    @property
    def SponsorshipTimeout(self) -> _n_0_t_1:"""SponsorshipTimeout { get; set; } -> TimeSpan"""
    def Register(self, obj: ISponsor):...
    def Register(self, obj: ISponsor, renewalTime: _n_0_t_1):...
    def Renew(self, renewalTime: _n_0_t_1) -> _n_0_t_1:...
    def Unregister(self, obj: ISponsor):...
class ISponsor():
    def Renewal(self, lease: ILease) -> _n_0_t_1:...
class LeaseState(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Active: int
    Expired: int
    Initial: int
    Null: int
    Renewing: int
    value__: int
class LifetimeServices(object):
    @property
    def LeaseManagerPollTime(self) -> _n_0_t_1:"""LeaseManagerPollTime { get; set; } -> TimeSpan"""
    @property
    def LeaseTime(self) -> _n_0_t_1:"""LeaseTime { get; set; } -> TimeSpan"""
    @property
    def RenewOnCallTime(self) -> _n_0_t_1:"""RenewOnCallTime { get; set; } -> TimeSpan"""
    @property
    def SponsorshipTimeout(self) -> _n_0_t_1:"""SponsorshipTimeout { get; set; } -> TimeSpan"""
    def __init__(self) -> LifetimeServices:...
