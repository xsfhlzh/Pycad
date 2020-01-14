from __clrclasses__.System import IDisposable as _n_0_t_0
from __clrclasses__.System import Guid as _n_0_t_1
from __clrclasses__.System import Enum as _n_0_t_2
from __clrclasses__.System import IComparable as _n_0_t_3
from __clrclasses__.System import IFormattable as _n_0_t_4
from __clrclasses__.System import IConvertible as _n_0_t_5
import typing
class CounterData(object):
    @property
    def RawValue(self) -> int:"""RawValue { get; set; } -> int"""
    @property
    def Value(self) -> int:"""Value { get; set; } -> int"""
    def Decrement(self):...
    def Increment(self):...
    def IncrementBy(self, value: int):...
class CounterSet(_n_0_t_0):
    def __init__(self, providerGuid: _n_0_t_1, counterSetGuid: _n_0_t_1, instanceType: CounterSetInstanceType) -> CounterSet:...
    def AddCounter(self, counterId: int, counterType: CounterType, counterName: str):...
    def AddCounter(self, counterId: int, counterType: CounterType):...
    def CreateCounterSetInstance(self, instanceName: str) -> CounterSetInstance:...
class CounterSetInstance(_n_0_t_0):
    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet:"""Counters { get; } -> CounterSetInstanceCounterDataSet"""
class CounterSetInstanceCounterDataSet(_n_0_t_0, typing.Iterable[CounterData]):
    @property
    def Item(self) -> CounterData:"""Item { get; } -> CounterData"""
class CounterSetInstanceType(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    GlobalAggregate: int
    GlobalAggregateWithHistory: int
    InstanceAggregate: int
    Multiple: int
    MultipleAggregate: int
    Single: int
    value__: int
class CounterType(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    AverageBase: int
    AverageCount64: int
    AverageTimer32: int
    Delta32: int
    Delta64: int
    ElapsedTime: int
    LargeQueueLength: int
    MultiTimerBase: int
    MultiTimerPercentageActive: int
    MultiTimerPercentageActive100Ns: int
    MultiTimerPercentageNotActive: int
    MultiTimerPercentageNotActive100Ns: int
    ObjectSpecificTimer: int
    PercentageActive: int
    PercentageActive100Ns: int
    PercentageNotActive: int
    PercentageNotActive100Ns: int
    PrecisionObjectSpecificTimer: int
    PrecisionSystemTimer: int
    PrecisionTimer100Ns: int
    QueueLength: int
    QueueLength100Ns: int
    QueueLengthObjectTime: int
    RateOfCountPerSecond32: int
    RateOfCountPerSecond64: int
    RawBase32: int
    RawBase64: int
    RawData32: int
    RawData64: int
    RawDataHex32: int
    RawDataHex64: int
    RawFraction32: int
    RawFraction64: int
    SampleBase: int
    SampleCounter: int
    SampleFraction: int
    value__: int
