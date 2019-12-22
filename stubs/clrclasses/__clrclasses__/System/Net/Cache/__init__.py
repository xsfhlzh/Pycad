from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import DateTime as _n_0_t_4
from __clrclasses__.System import TimeSpan as _n_0_t_5
import typing
class HttpCacheAgeControl(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    MaxAge: int
    MaxAgeAndMaxStale: int
    MaxAgeAndMinFresh: int
    MaxStale: int
    MinFresh: int
    _None: int
    value__: int
class HttpRequestCacheLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    BypassCache: int
    CacheIfAvailable: int
    CacheOnly: int
    CacheOrNextCacheOnly: int
    Default: int
    NoCacheNoStore: int
    Refresh: int
    Reload: int
    Revalidate: int
    value__: int
class HttpRequestCachePolicy(RequestCachePolicy):
    @property
    def CacheSyncDate(self) -> _n_0_t_4:"""CacheSyncDate { get; } -> DateTime"""
    @property
    def MaxAge(self) -> _n_0_t_5:"""MaxAge { get; } -> TimeSpan"""
    @property
    def MaxStale(self) -> _n_0_t_5:"""MaxStale { get; } -> TimeSpan"""
    @property
    def MinFresh(self) -> _n_0_t_5:"""MinFresh { get; } -> TimeSpan"""
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, maxAge: _n_0_t_5, freshOrStale: _n_0_t_5, cacheSyncDate: _n_0_t_4) -> HttpRequestCachePolicy:...
    def __init__(self, cacheSyncDate: _n_0_t_4) -> HttpRequestCachePolicy:...
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, maxAge: _n_0_t_5, freshOrStale: _n_0_t_5) -> HttpRequestCachePolicy:...
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: _n_0_t_5) -> HttpRequestCachePolicy:...
    def __init__(self, level: HttpRequestCacheLevel) -> HttpRequestCachePolicy:...
    def __init__(self) -> HttpRequestCachePolicy:...
class RequestCacheLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    BypassCache: int
    CacheIfAvailable: int
    CacheOnly: int
    Default: int
    NoCacheNoStore: int
    Reload: int
    Revalidate: int
    value__: int
class RequestCachePolicy(object):
    @property
    def Level(self) -> RequestCacheLevel:"""Level { get; } -> RequestCacheLevel"""
    def __init__(self, level: RequestCacheLevel) -> RequestCachePolicy:...
    def __init__(self) -> RequestCachePolicy:...
