from __clrclasses__.System.Collections import IList as _n_0_t_0
from __clrclasses__.System.Collections import IDictionary as _n_0_t_1
from __clrclasses__.System.Collections import ICollection as _n_0_t_2
from __clrclasses__.System.Collections.Generic import IList as _n_1_t_0
from __clrclasses__.System.Collections.Generic import IReadOnlyList as _n_1_t_1
from __clrclasses__.System.Collections.Generic import IEqualityComparer as _n_1_t_2
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_3
from __clrclasses__.System.Collections.Generic import List as _n_1_t_4
from __clrclasses__.System.Collections.Generic import IDictionary as _n_1_t_5
from __clrclasses__.System.Collections.Generic import IReadOnlyDictionary as _n_1_t_6
from __clrclasses__.System.Collections.Generic import ICollection as _n_1_t_7
from __clrclasses__.System.Collections.Generic import IReadOnlyCollection as _n_1_t_8
from __clrclasses__.System.Collections.Specialized import INotifyCollectionChanged as _n_2_t_0
from __clrclasses__.System.ComponentModel import INotifyPropertyChanged as _n_3_t_0
import typing
T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TItem = typing.TypeVar('TItem')
TValue = typing.TypeVar('TValue')
class Collection(_n_1_t_0[T], _n_0_t_0, _n_1_t_1[T], typing.Generic[T], typing.Iterable[T]):
    def __init__(self) -> Collection:...
    def __init__(self, list: _n_1_t_0[T]) -> Collection:...
class KeyedCollection(Collection[TItem], _n_1_t_0[TItem], _n_0_t_0, _n_1_t_1[TItem], typing.Generic[TKey, TItem], typing.Iterable[TItem]):
    @property
    def Comparer(self) -> _n_1_t_2[TKey]:"""Comparer { get; } -> IEqualityComparer"""
class ObservableCollection(Collection[T], _n_1_t_0[T], _n_0_t_0, _n_1_t_1[T], _n_2_t_0, _n_3_t_0, typing.Generic[T], typing.Iterable[T]):
    def __init__(self, collection: _n_1_t_3[T]) -> ObservableCollection:...
    def __init__(self, list: _n_1_t_4[T]) -> ObservableCollection:...
    def __init__(self) -> ObservableCollection:...
    def Move(self, oldIndex: int, newIndex: int):...
class ReadOnlyCollection(_n_1_t_0[T], _n_0_t_0, _n_1_t_1[T], typing.Generic[T], typing.Iterable[T]):
    def __init__(self, list: _n_1_t_0[T]) -> ReadOnlyCollection:...
class ReadOnlyDictionary(_n_1_t_5[TKey, TValue], _n_0_t_1, _n_1_t_6[TKey, TValue], typing.Generic[TKey, TValue], typing.Iterable[TValue]):
    def __init__(self, dictionary: _n_1_t_5[TKey, TValue]) -> ReadOnlyDictionary:...
    class KeyCollection(_n_1_t_7[TKey], _n_0_t_2, _n_1_t_8[TKey], typing.Generic[TKey, TValue]):
        pass
    class ValueCollection(_n_1_t_7[TValue], _n_0_t_2, _n_1_t_8[TValue], typing.Generic[TKey, TValue]):
        pass
class ReadOnlyObservableCollection(ReadOnlyCollection[T], _n_1_t_0[T], _n_0_t_0, _n_1_t_1[T], _n_2_t_0, _n_3_t_0, typing.Generic[T], typing.Iterable[T]):
    def __init__(self, list: ObservableCollection[T]) -> ReadOnlyObservableCollection:...
