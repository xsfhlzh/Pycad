import __clrclasses__.System.Linq.Expressions as Expressions
from __clrclasses__.System import Func as _n_0_t_0
from __clrclasses__.System import Array as _n_0_t_1
from __clrclasses__.System import Action as _n_0_t_2
from __clrclasses__.System import Enum as _n_0_t_3
from __clrclasses__.System import IComparable as _n_0_t_4
from __clrclasses__.System import IFormattable as _n_0_t_5
from __clrclasses__.System import IConvertible as _n_0_t_6
from __clrclasses__.System.Collections import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections.Concurrent import Partitioner as _n_2_t_0
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_3_t_0
from __clrclasses__.System.Collections.Generic import IEqualityComparer as _n_3_t_1
from __clrclasses__.System.Collections.Generic import IComparer as _n_3_t_2
from __clrclasses__.System.Collections.Generic import Dictionary as _n_3_t_3
from __clrclasses__.System.Collections.Generic import HashSet as _n_3_t_4
from __clrclasses__.System.Collections.Generic import List as _n_3_t_5
from __clrclasses__.System.Linq.Expressions import Expression as _n_4_t_0
from __clrclasses__.System.Threading import CancellationToken as _n_5_t_0
import typing
T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TElement = typing.TypeVar('TElement')
TSource = typing.TypeVar('TSource')
class Enumerable(object):
    @staticmethod
    def Aggregate(source: _n_3_t_0[typing.Any], seed: typing.Any, func: _n_0_t_0[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: _n_3_t_0[typing.Any], seed: typing.Any, func: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: _n_3_t_0[typing.Any], func: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def All(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> bool:...
    @staticmethod
    def Any(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> bool:...
    @staticmethod
    def Any(source: _n_3_t_0[typing.Any]) -> bool:...
    @staticmethod
    def Append(source: _n_3_t_0[typing.Any], element: typing.Any) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def AsEnumerable(source: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Average(source: _n_3_t_0[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> float:...
    @staticmethod
    def Average(source: _n_3_t_0[int]) -> float:...
    @staticmethod
    def Cast(source: _n_1_t_0) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Concat(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Contains(source: _n_3_t_0[typing.Any], value: typing.Any, comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def Contains(source: _n_3_t_0[typing.Any], value: typing.Any) -> bool:...
    @staticmethod
    def Count(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> int:...
    @staticmethod
    def Count(source: _n_3_t_0[typing.Any]) -> int:...
    @staticmethod
    def DefaultIfEmpty(source: _n_3_t_0[typing.Any], defaultValue: typing.Any) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def DefaultIfEmpty(source: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Distinct(source: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Distinct(source: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def ElementAt(source: _n_3_t_0[typing.Any], index: int) -> typing.Any:...
    @staticmethod
    def ElementAtOrDefault(source: _n_3_t_0[typing.Any], index: int) -> typing.Any:...
    @staticmethod
    def Empty() -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Except(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Except(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def First(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def First(source: _n_3_t_0[typing.Any]) -> typing.Any:...
    @staticmethod
    def FirstOrDefault(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def FirstOrDefault(source: _n_3_t_0[typing.Any]) -> typing.Any:...
    @staticmethod
    def GroupBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def GroupBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def GroupBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_0[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_0[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupJoin(outer: _n_3_t_0[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def GroupJoin(outer: _n_3_t_0[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Intersect(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Intersect(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Join(outer: _n_3_t_0[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Join(outer: _n_3_t_0[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Last(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def Last(source: _n_3_t_0[typing.Any]) -> typing.Any:...
    @staticmethod
    def LastOrDefault(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def LastOrDefault(source: _n_3_t_0[typing.Any]) -> typing.Any:...
    @staticmethod
    def LongCount(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> int:...
    @staticmethod
    def LongCount(source: _n_3_t_0[typing.Any]) -> int:...
    @staticmethod
    def Max(source: _n_3_t_0[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> int:...
    @staticmethod
    def Max(source: _n_3_t_0[int]) -> int:...
    @staticmethod
    def Min(source: _n_3_t_0[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> int:...
    @staticmethod
    def Min(source: _n_3_t_0[int]) -> int:...
    @staticmethod
    def OfType(source: _n_1_t_0) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def OrderBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def OrderBy(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def OrderByDescending(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def OrderByDescending(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def Prepend(source: _n_3_t_0[typing.Any], element: typing.Any) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Range(start: int, count: int) -> _n_3_t_0[int]:...
    @staticmethod
    def Repeat(element: typing.Any, count: int) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Reverse(source: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Select(source: _n_3_t_0[typing.Any], selector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def SelectMany(source: _n_3_t_0[typing.Any], collectionSelector: _n_0_t_0[typing.Any, int, _n_3_t_0[typing.Any]], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def SelectMany(source: _n_3_t_0[typing.Any], selector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any]]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def SequenceEqual(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def SequenceEqual(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any]) -> bool:...
    @staticmethod
    def Single(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def Single(source: _n_3_t_0[typing.Any]) -> typing.Any:...
    @staticmethod
    def SingleOrDefault(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def SingleOrDefault(source: _n_3_t_0[typing.Any]) -> typing.Any:...
    @staticmethod
    def Skip(source: _n_3_t_0[typing.Any], count: int) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def SkipWhile(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Sum(source: _n_3_t_0[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> int:...
    @staticmethod
    def Sum(source: _n_3_t_0[int]) -> int:...
    @staticmethod
    def Take(source: _n_3_t_0[typing.Any], count: int) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def TakeWhile(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def ThenBy(source: IOrderedEnumerable[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def ThenBy(source: IOrderedEnumerable[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def ThenByDescending(source: IOrderedEnumerable[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def ThenByDescending(source: IOrderedEnumerable[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> IOrderedEnumerable[typing.Any]:...
    @staticmethod
    def ToArray(source: _n_3_t_0[typing.Any]) -> _n_0_t_1[typing.Any]:...
    @staticmethod
    def ToDictionary(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToDictionary(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToDictionary(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToDictionary(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToHashSet(source: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_4[typing.Any]:...
    @staticmethod
    def ToHashSet(source: _n_3_t_0[typing.Any]) -> _n_3_t_4[typing.Any]:...
    @staticmethod
    def ToList(source: _n_3_t_0[typing.Any]) -> _n_3_t_5[typing.Any]:...
    @staticmethod
    def ToLookup(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def ToLookup(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def ToLookup(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def ToLookup(source: _n_3_t_0[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def Union(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Union(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Where(source: _n_3_t_0[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def Zip(first: _n_3_t_0[typing.Any], second: _n_3_t_0[typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> _n_3_t_0[typing.Any]:...
class EnumerableExecutor(EnumerableExecutor, typing.Generic[T]):
    def __init__(self, expression: _n_4_t_0) -> EnumerableExecutor:...
class EnumerableQuery(EnumerableQuery, IOrderedQueryable[T], IQueryProvider, typing.Generic[T]):
    def __init__(self, expression: _n_4_t_0) -> EnumerableQuery:...
    def __init__(self, enumerable: _n_3_t_0[T]) -> EnumerableQuery:...
class IGrouping(_n_3_t_0[TElement], typing.Generic[TKey, TElement]):
    @property
    def Key(self) -> TKey:"""Key { get; } -> TKey"""
class ILookup(_n_3_t_0[IGrouping[TKey, TElement]], typing.Generic[TKey, TElement], typing.Iterable[_n_3_t_0[TElement]]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def Item(self) -> _n_3_t_0[TElement]:"""Item { get; } -> IEnumerable"""
    def Contains(self, key: TKey) -> bool:...
class IOrderedEnumerable(_n_3_t_0[TElement], typing.Generic[TElement]):
    def CreateOrderedEnumerable(self, keySelector: _n_0_t_0[TElement, typing.Any], comparer: _n_3_t_2[typing.Any], descending: bool) -> IOrderedEnumerable[TElement]:...
    def ThenBy(self, keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> IOrderedEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ThenBy(self, keySelector: _n_0_t_0[typing.Any, typing.Any]) -> IOrderedEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ThenByDescending(self, keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> IOrderedEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ThenByDescending(self, keySelector: _n_0_t_0[typing.Any, typing.Any]) -> IOrderedEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
class IOrderedQueryable(IQueryable[T], IOrderedQueryable, typing.Generic[T]):
    def ThenBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def ThenBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def ThenByDescending(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def ThenByDescending(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
class IQueryable(_n_3_t_0[T], IQueryable, typing.Generic[T]):
    def Aggregate(self, seed: typing.Any, func: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]], selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Aggregate(self, seed: typing.Any, func: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Aggregate(self, func: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def All(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> bool:
        """Extension from: System.Linq.Queryable"""
    def Any(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> bool:
        """Extension from: System.Linq.Queryable"""
    def Any(self) -> bool:
        """Extension from: System.Linq.Queryable"""
    def Average(self, selector: _n_4_t_0[_n_0_t_0[typing.Any, int]]) -> float:
        """Extension from: System.Linq.Queryable"""
    def Average(self) -> float:
        """Extension from: System.Linq.Queryable"""
    def Cast(self) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Concat(self, source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Contains(self, item: typing.Any, comparer: _n_3_t_1[typing.Any]) -> bool:
        """Extension from: System.Linq.Queryable"""
    def Contains(self, item: typing.Any) -> bool:
        """Extension from: System.Linq.Queryable"""
    def Count(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> int:
        """Extension from: System.Linq.Queryable"""
    def Count(self) -> int:
        """Extension from: System.Linq.Queryable"""
    def DefaultIfEmpty(self, defaultValue: typing.Any) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def DefaultIfEmpty(self) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Distinct(self, comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Distinct(self) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def ElementAt(self, index: int) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def ElementAtOrDefault(self, index: int) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Except(self, source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Except(self, source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def First(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def First(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def FirstOrDefault(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def FirstOrDefault(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def GroupBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def GroupBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def GroupBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Queryable"""
    def GroupBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Queryable"""
    def GroupBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Queryable"""
    def GroupBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Queryable"""
    def GroupJoin(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def GroupJoin(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Intersect(self, source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Intersect(self, source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Join(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Join(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Last(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Last(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def LastOrDefault(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def LastOrDefault(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def LongCount(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> int:
        """Extension from: System.Linq.Queryable"""
    def LongCount(self) -> int:
        """Extension from: System.Linq.Queryable"""
    def Max(self, selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Max(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Min(self, selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Min(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def OfType(self) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def OrderBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def OrderBy(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def OrderByDescending(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def OrderByDescending(self, keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Reverse(self) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Select(self, selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def SelectMany(self, collectionSelector: _n_4_t_0[_n_0_t_0[typing.Any, int, _n_3_t_0[typing.Any]]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def SelectMany(self, selector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any]]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def SequenceEqual(self, source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> bool:
        """Extension from: System.Linq.Queryable"""
    def SequenceEqual(self, source2: _n_3_t_0[typing.Any]) -> bool:
        """Extension from: System.Linq.Queryable"""
    def Single(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Single(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def SingleOrDefault(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def SingleOrDefault(self) -> typing.Any:
        """Extension from: System.Linq.Queryable"""
    def Skip(self, count: int) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def SkipWhile(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Sum(self, selector: _n_4_t_0[_n_0_t_0[typing.Any, int]]) -> int:
        """Extension from: System.Linq.Queryable"""
    def Sum(self) -> int:
        """Extension from: System.Linq.Queryable"""
    def Take(self, count: int) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def TakeWhile(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Union(self, source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Union(self, source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Where(self, predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Zip(self, source2: _n_3_t_0[typing.Any], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> IQueryable[typing.Any]:
        """Extension from: System.Linq.Queryable"""
class IQueryProvider():
    def CreateQuery(self, expression: _n_4_t_0) -> IQueryable:...
    def Execute(self, expression: _n_4_t_0) -> object:...
class Lookup(_n_3_t_0[IGrouping[TKey, TElement]], ILookup[TKey, TElement], typing.Generic[TKey, TElement], typing.Iterable[_n_3_t_0[TElement]]):
    def ApplyResultSelector(self, resultSelector: _n_0_t_0[TKey, _n_3_t_0[TElement], typing.Any]) -> _n_3_t_0[typing.Any]:...
class OrderedParallelQuery(ParallelQuery[TSource], _n_1_t_0, _n_3_t_0[TSource], typing.Generic[TSource]):
    def ThenBy(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ThenBy(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ThenByDescending(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ThenByDescending(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
class ParallelEnumerable(object):
    @staticmethod
    def Aggregate(source: ParallelQuery[typing.Any], seedFactory: _n_0_t_0[typing.Any], updateAccumulatorFunc: _n_0_t_0[typing.Any, typing.Any, typing.Any], combineAccumulatorsFunc: _n_0_t_0[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: ParallelQuery[typing.Any], seed: typing.Any, updateAccumulatorFunc: _n_0_t_0[typing.Any, typing.Any, typing.Any], combineAccumulatorsFunc: _n_0_t_0[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: ParallelQuery[typing.Any], seed: typing.Any, func: _n_0_t_0[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: ParallelQuery[typing.Any], seed: typing.Any, func: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: ParallelQuery[typing.Any], func: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> typing.Any:...
    @staticmethod
    def All(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> bool:...
    @staticmethod
    def Any(source: ParallelQuery[typing.Any]) -> bool:...
    @staticmethod
    def Any(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> bool:...
    @staticmethod
    def AsEnumerable(source: ParallelQuery[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def AsOrdered(source: ParallelQuery) -> ParallelQuery:...
    @staticmethod
    def AsOrdered(source: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def AsParallel(source: _n_1_t_0) -> ParallelQuery:...
    @staticmethod
    def AsParallel(source: _n_2_t_0[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def AsParallel(source: _n_3_t_0[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def AsSequential(source: ParallelQuery[typing.Any]) -> _n_3_t_0[typing.Any]:...
    @staticmethod
    def AsUnordered(source: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Average(source: ParallelQuery[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> float:...
    @staticmethod
    def Average(source: ParallelQuery[int]) -> float:...
    @staticmethod
    def Cast(source: ParallelQuery) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Concat(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Concat(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Contains(source: ParallelQuery[typing.Any], value: typing.Any, comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def Contains(source: ParallelQuery[typing.Any], value: typing.Any) -> bool:...
    @staticmethod
    def Count(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> int:...
    @staticmethod
    def Count(source: ParallelQuery[typing.Any]) -> int:...
    @staticmethod
    def DefaultIfEmpty(source: ParallelQuery[typing.Any], defaultValue: typing.Any) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def DefaultIfEmpty(source: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Distinct(source: ParallelQuery[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Distinct(source: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def ElementAt(source: ParallelQuery[typing.Any], index: int) -> typing.Any:...
    @staticmethod
    def ElementAtOrDefault(source: ParallelQuery[typing.Any], index: int) -> typing.Any:...
    @staticmethod
    def Empty() -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Except(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Except(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Except(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Except(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def First(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def First(source: ParallelQuery[typing.Any]) -> typing.Any:...
    @staticmethod
    def FirstOrDefault(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def FirstOrDefault(source: ParallelQuery[typing.Any]) -> typing.Any:...
    @staticmethod
    def ForAll(source: ParallelQuery[typing.Any], action: _n_0_t_2[typing.Any]):...
    @staticmethod
    def GroupBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def GroupBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def GroupBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any]) -> ParallelQuery[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> ParallelQuery[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupJoin(outer: ParallelQuery[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def GroupJoin(outer: ParallelQuery[typing.Any], inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def GroupJoin(outer: ParallelQuery[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def GroupJoin(outer: ParallelQuery[typing.Any], inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Intersect(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Intersect(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Intersect(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Intersect(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Join(outer: ParallelQuery[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Join(outer: ParallelQuery[typing.Any], inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Join(outer: ParallelQuery[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Join(outer: ParallelQuery[typing.Any], inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Last(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def Last(source: ParallelQuery[typing.Any]) -> typing.Any:...
    @staticmethod
    def LastOrDefault(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def LastOrDefault(source: ParallelQuery[typing.Any]) -> typing.Any:...
    @staticmethod
    def LongCount(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> int:...
    @staticmethod
    def LongCount(source: ParallelQuery[typing.Any]) -> int:...
    @staticmethod
    def Max(source: ParallelQuery[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> int:...
    @staticmethod
    def Max(source: ParallelQuery[int]) -> int:...
    @staticmethod
    def Min(source: ParallelQuery[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> int:...
    @staticmethod
    def Min(source: ParallelQuery[int]) -> int:...
    @staticmethod
    def OfType(source: ParallelQuery) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def OrderBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def OrderBy(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def OrderByDescending(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def OrderByDescending(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def Range(start: int, count: int) -> ParallelQuery[int]:...
    @staticmethod
    def Repeat(element: typing.Any, count: int) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Reverse(source: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Select(source: ParallelQuery[typing.Any], selector: _n_0_t_0[typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def SelectMany(source: ParallelQuery[typing.Any], collectionSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any]], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def SelectMany(source: ParallelQuery[typing.Any], selector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any]]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def SequenceEqual(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def SequenceEqual(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any], comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def SequenceEqual(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any]) -> bool:...
    @staticmethod
    def SequenceEqual(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any]) -> bool:...
    @staticmethod
    def Single(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def Single(source: ParallelQuery[typing.Any]) -> typing.Any:...
    @staticmethod
    def SingleOrDefault(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> typing.Any:...
    @staticmethod
    def SingleOrDefault(source: ParallelQuery[typing.Any]) -> typing.Any:...
    @staticmethod
    def Skip(source: ParallelQuery[typing.Any], count: int) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def SkipWhile(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Sum(source: ParallelQuery[typing.Any], selector: _n_0_t_0[typing.Any, int]) -> int:...
    @staticmethod
    def Sum(source: ParallelQuery[int]) -> int:...
    @staticmethod
    def Take(source: ParallelQuery[typing.Any], count: int) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def TakeWhile(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def ThenBy(source: OrderedParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def ThenBy(source: OrderedParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def ThenByDescending(source: OrderedParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def ThenByDescending(source: OrderedParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> OrderedParallelQuery[typing.Any]:...
    @staticmethod
    def ToArray(source: ParallelQuery[typing.Any]) -> _n_0_t_1[typing.Any]:...
    @staticmethod
    def ToDictionary(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToDictionary(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToDictionary(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToDictionary(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:...
    @staticmethod
    def ToList(source: ParallelQuery[typing.Any]) -> _n_3_t_5[typing.Any]:...
    @staticmethod
    def ToLookup(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def ToLookup(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], elementSelector: _n_0_t_0[typing.Any, typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def ToLookup(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def ToLookup(source: ParallelQuery[typing.Any], keySelector: _n_0_t_0[typing.Any, typing.Any]) -> ILookup[typing.Any, typing.Any]:...
    @staticmethod
    def Union(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Union(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Union(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Union(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Where(source: ParallelQuery[typing.Any], predicate: _n_0_t_0[typing.Any, bool]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def WithCancellation(source: ParallelQuery[typing.Any], cancellationToken: _n_5_t_0) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def WithDegreeOfParallelism(source: ParallelQuery[typing.Any], degreeOfParallelism: int) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def WithExecutionMode(source: ParallelQuery[typing.Any], executionMode: ParallelExecutionMode) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def WithMergeOptions(source: ParallelQuery[typing.Any], mergeOptions: ParallelMergeOptions) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Zip(first: ParallelQuery[typing.Any], second: _n_3_t_0[typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:...
    @staticmethod
    def Zip(first: ParallelQuery[typing.Any], second: ParallelQuery[typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:...
class ParallelExecutionMode(_n_0_t_3, _n_0_t_4, _n_0_t_5, _n_0_t_6):
    Default: int
    ForceParallelism: int
    value__: int
class ParallelMergeOptions(_n_0_t_3, _n_0_t_4, _n_0_t_5, _n_0_t_6):
    AutoBuffered: int
    Default: int
    FullyBuffered: int
    NotBuffered: int
    value__: int
class ParallelQuery(ParallelQuery, _n_1_t_0, _n_3_t_0[TSource], typing.Generic[TSource]):
    def Aggregate(self, seedFactory: _n_0_t_0[typing.Any], updateAccumulatorFunc: _n_0_t_0[typing.Any, TSource, typing.Any], combineAccumulatorsFunc: _n_0_t_0[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Aggregate(self, seed: typing.Any, updateAccumulatorFunc: _n_0_t_0[typing.Any, TSource, typing.Any], combineAccumulatorsFunc: _n_0_t_0[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Aggregate(self, seed: typing.Any, func: _n_0_t_0[typing.Any, TSource, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Aggregate(self, seed: typing.Any, func: _n_0_t_0[typing.Any, TSource, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Aggregate(self, func: _n_0_t_0[TSource, TSource, TSource]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def All(self, predicate: _n_0_t_0[TSource, bool]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Any(self) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Any(self, predicate: _n_0_t_0[TSource, bool]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def AsEnumerable(self) -> _n_3_t_0[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def AsOrdered(self) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def AsSequential(self) -> _n_3_t_0[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def AsUnordered(self) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Average(self, selector: _n_0_t_0[TSource, int]) -> float:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Average(self) -> float:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Cast(self) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Concat(self, second: _n_3_t_0[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Concat(self, second: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Contains(self, value: TSource, comparer: _n_3_t_1[TSource]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Contains(self, value: TSource) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Count(self, predicate: _n_0_t_0[TSource, bool]) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Count(self) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def DefaultIfEmpty(self, defaultValue: TSource) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def DefaultIfEmpty(self) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Distinct(self, comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Distinct(self) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ElementAt(self, index: int) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ElementAtOrDefault(self, index: int) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Except(self, second: _n_3_t_0[TSource], comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Except(self, second: ParallelQuery[TSource], comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Except(self, second: _n_3_t_0[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Except(self, second: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def First(self, predicate: _n_0_t_0[TSource, bool]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def First(self) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def FirstOrDefault(self, predicate: _n_0_t_0[TSource, bool]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def FirstOrDefault(self) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ForAll(self, action: _n_0_t_2[TSource]):
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupBy(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupBy(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupBy(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[IGrouping[typing.Any, typing.Any]]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupBy(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any]) -> ParallelQuery[IGrouping[typing.Any, typing.Any]]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupBy(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[IGrouping[typing.Any, TSource]]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupBy(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> ParallelQuery[IGrouping[typing.Any, TSource]]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupJoin(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupJoin(self, inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupJoin(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def GroupJoin(self, inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Intersect(self, second: _n_3_t_0[TSource], comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Intersect(self, second: ParallelQuery[TSource], comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Intersect(self, second: _n_3_t_0[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Intersect(self, second: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Join(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Join(self, inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Join(self, inner: _n_3_t_0[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Join(self, inner: ParallelQuery[typing.Any], outerKeySelector: _n_0_t_0[typing.Any, typing.Any], innerKeySelector: _n_0_t_0[typing.Any, typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Last(self, predicate: _n_0_t_0[TSource, bool]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Last(self) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def LastOrDefault(self, predicate: _n_0_t_0[TSource, bool]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def LastOrDefault(self) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def LongCount(self, predicate: _n_0_t_0[TSource, bool]) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def LongCount(self) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Max(self, selector: _n_0_t_0[TSource, int]) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Max(self) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Min(self, selector: _n_0_t_0[TSource, int]) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Min(self) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def OfType(self) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def OrderBy(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def OrderBy(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def OrderByDescending(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_2[typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def OrderByDescending(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> OrderedParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Reverse(self) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Select(self, selector: _n_0_t_0[TSource, typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SelectMany(self, collectionSelector: _n_0_t_0[TSource, _n_3_t_0[typing.Any]], resultSelector: _n_0_t_0[TSource, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SelectMany(self, selector: _n_0_t_0[TSource, _n_3_t_0[typing.Any]]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SequenceEqual(self, second: _n_3_t_0[TSource], comparer: _n_3_t_1[TSource]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SequenceEqual(self, second: ParallelQuery[TSource], comparer: _n_3_t_1[TSource]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SequenceEqual(self, second: _n_3_t_0[TSource]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SequenceEqual(self, second: ParallelQuery[TSource]) -> bool:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Single(self, predicate: _n_0_t_0[TSource, bool]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Single(self) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SingleOrDefault(self, predicate: _n_0_t_0[TSource, bool]) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SingleOrDefault(self) -> TSource:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Skip(self, count: int) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def SkipWhile(self, predicate: _n_0_t_0[TSource, bool]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Sum(self, selector: _n_0_t_0[TSource, int]) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Sum(self) -> int:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Take(self, count: int) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def TakeWhile(self, predicate: _n_0_t_0[TSource, bool]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToArray(self) -> _n_0_t_1[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToDictionary(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToDictionary(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any]) -> _n_3_t_3[typing.Any, typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToDictionary(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_1[typing.Any]) -> _n_3_t_3[typing.Any, TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToDictionary(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> _n_3_t_3[typing.Any, TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToList(self) -> _n_3_t_5[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToLookup(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ILookup[typing.Any, typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToLookup(self, keySelector: _n_0_t_0[TSource, typing.Any], elementSelector: _n_0_t_0[TSource, typing.Any]) -> ILookup[typing.Any, typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToLookup(self, keySelector: _n_0_t_0[TSource, typing.Any], comparer: _n_3_t_1[typing.Any]) -> ILookup[typing.Any, TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def ToLookup(self, keySelector: _n_0_t_0[TSource, typing.Any]) -> ILookup[typing.Any, TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Union(self, second: _n_3_t_0[TSource], comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Union(self, second: ParallelQuery[TSource], comparer: _n_3_t_1[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Union(self, second: _n_3_t_0[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Union(self, second: ParallelQuery[TSource]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Where(self, predicate: _n_0_t_0[TSource, bool]) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def WithCancellation(self, cancellationToken: _n_5_t_0) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def WithDegreeOfParallelism(self, degreeOfParallelism: int) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def WithExecutionMode(self, executionMode: ParallelExecutionMode) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def WithMergeOptions(self, mergeOptions: ParallelMergeOptions) -> ParallelQuery[TSource]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Zip(self, second: _n_3_t_0[typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def Zip(self, second: ParallelQuery[typing.Any], resultSelector: _n_0_t_0[typing.Any, typing.Any, typing.Any]) -> ParallelQuery[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
class Queryable(object):
    @staticmethod
    def Aggregate(source: IQueryable[typing.Any], seed: typing.Any, func: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]], selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: IQueryable[typing.Any], seed: typing.Any, func: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> typing.Any:...
    @staticmethod
    def Aggregate(source: IQueryable[typing.Any], func: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> typing.Any:...
    @staticmethod
    def All(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> bool:...
    @staticmethod
    def Any(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> bool:...
    @staticmethod
    def Any(source: IQueryable[typing.Any]) -> bool:...
    @staticmethod
    def AsQueryable(source: _n_1_t_0) -> IQueryable:...
    @staticmethod
    def AsQueryable(source: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Average(source: IQueryable[typing.Any], selector: _n_4_t_0[_n_0_t_0[typing.Any, int]]) -> float:...
    @staticmethod
    def Average(source: IQueryable[int]) -> float:...
    @staticmethod
    def Cast(source: IQueryable) -> IQueryable[typing.Any]:...
    @staticmethod
    def Concat(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Contains(source: IQueryable[typing.Any], item: typing.Any, comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def Contains(source: IQueryable[typing.Any], item: typing.Any) -> bool:...
    @staticmethod
    def Count(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> int:...
    @staticmethod
    def Count(source: IQueryable[typing.Any]) -> int:...
    @staticmethod
    def DefaultIfEmpty(source: IQueryable[typing.Any], defaultValue: typing.Any) -> IQueryable[typing.Any]:...
    @staticmethod
    def DefaultIfEmpty(source: IQueryable[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Distinct(source: IQueryable[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Distinct(source: IQueryable[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def ElementAt(source: IQueryable[typing.Any], index: int) -> typing.Any:...
    @staticmethod
    def ElementAtOrDefault(source: IQueryable[typing.Any], index: int) -> typing.Any:...
    @staticmethod
    def Except(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Except(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def First(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:...
    @staticmethod
    def First(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def FirstOrDefault(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:...
    @staticmethod
    def FirstOrDefault(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def GroupBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def GroupBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def GroupBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], elementSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IQueryable[IGrouping[typing.Any, typing.Any]]:...
    @staticmethod
    def GroupJoin(outer: IQueryable[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def GroupJoin(outer: IQueryable[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any], typing.Any]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Intersect(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Intersect(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Join(outer: IQueryable[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Join(outer: IQueryable[typing.Any], inner: _n_3_t_0[typing.Any], outerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], innerKeySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Last(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:...
    @staticmethod
    def Last(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def LastOrDefault(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:...
    @staticmethod
    def LastOrDefault(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def LongCount(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> int:...
    @staticmethod
    def LongCount(source: IQueryable[typing.Any]) -> int:...
    @staticmethod
    def Max(source: IQueryable[typing.Any], selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> typing.Any:...
    @staticmethod
    def Max(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def Min(source: IQueryable[typing.Any], selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> typing.Any:...
    @staticmethod
    def Min(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def OfType(source: IQueryable) -> IQueryable[typing.Any]:...
    @staticmethod
    def OrderBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def OrderBy(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def OrderByDescending(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def OrderByDescending(source: IQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def Reverse(source: IQueryable[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Select(source: IQueryable[typing.Any], selector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def SelectMany(source: IQueryable[typing.Any], collectionSelector: _n_4_t_0[_n_0_t_0[typing.Any, int, _n_3_t_0[typing.Any]]], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def SelectMany(source: IQueryable[typing.Any], selector: _n_4_t_0[_n_0_t_0[typing.Any, _n_3_t_0[typing.Any]]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def SequenceEqual(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> bool:...
    @staticmethod
    def SequenceEqual(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any]) -> bool:...
    @staticmethod
    def Single(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:...
    @staticmethod
    def Single(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def SingleOrDefault(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> typing.Any:...
    @staticmethod
    def SingleOrDefault(source: IQueryable[typing.Any]) -> typing.Any:...
    @staticmethod
    def Skip(source: IQueryable[typing.Any], count: int) -> IQueryable[typing.Any]:...
    @staticmethod
    def SkipWhile(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Sum(source: IQueryable[typing.Any], selector: _n_4_t_0[_n_0_t_0[typing.Any, int]]) -> int:...
    @staticmethod
    def Sum(source: IQueryable[int]) -> int:...
    @staticmethod
    def Take(source: IQueryable[typing.Any], count: int) -> IQueryable[typing.Any]:...
    @staticmethod
    def TakeWhile(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def ThenBy(source: IOrderedQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def ThenBy(source: IOrderedQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def ThenByDescending(source: IOrderedQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]], comparer: _n_3_t_2[typing.Any]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def ThenByDescending(source: IOrderedQueryable[typing.Any], keySelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any]]) -> IOrderedQueryable[typing.Any]:...
    @staticmethod
    def Union(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any], comparer: _n_3_t_1[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Union(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Where(source: IQueryable[typing.Any], predicate: _n_4_t_0[_n_0_t_0[typing.Any, bool]]) -> IQueryable[typing.Any]:...
    @staticmethod
    def Zip(source1: IQueryable[typing.Any], source2: _n_3_t_0[typing.Any], resultSelector: _n_4_t_0[_n_0_t_0[typing.Any, typing.Any, typing.Any]]) -> IQueryable[typing.Any]:...
