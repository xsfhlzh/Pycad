import __clrclasses__.System.Diagnostics.Contracts.Internal as Internal
from __clrclasses__.System import EventHandler as _n_0_t_0
from __clrclasses__.System import Predicate as _n_0_t_1
from __clrclasses__.System import Attribute as _n_0_t_2
from __clrclasses__.System import Type as _n_0_t_3
from __clrclasses__.System import EventArgs as _n_0_t_4
from __clrclasses__.System import Exception as _n_0_t_5
from __clrclasses__.System import Enum as _n_0_t_6
from __clrclasses__.System import IComparable as _n_0_t_7
from __clrclasses__.System import IFormattable as _n_0_t_8
from __clrclasses__.System import IConvertible as _n_0_t_9
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_0
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_2_t_0
import typing
class Contract(object):
    @property
    def ContractFailed(self) -> _n_0_t_0[ContractFailedEventArgs]:
        """ContractFailed Event: EventHandler"""
    @staticmethod
    def Assert(condition: bool, userMessage: str):...
    @staticmethod
    def Assert(condition: bool):...
    @staticmethod
    def Assume(condition: bool, userMessage: str):...
    @staticmethod
    def Assume(condition: bool):...
    @staticmethod
    def EndContractBlock():...
    @staticmethod
    def Ensures(condition: bool, userMessage: str):...
    @staticmethod
    def Ensures(condition: bool):...
    @staticmethod
    def EnsuresOnThrow(condition: bool, userMessage: str):...
    @staticmethod
    def EnsuresOnThrow(condition: bool):...
    @staticmethod
    def Exists(collection: _n_1_t_0[typing.Any], predicate: _n_0_t_1[typing.Any]) -> bool:...
    @staticmethod
    def Exists(fromInclusive: int, toExclusive: int, predicate: _n_0_t_1[int]) -> bool:...
    @staticmethod
    def ForAll(collection: _n_1_t_0[typing.Any], predicate: _n_0_t_1[typing.Any]) -> bool:...
    @staticmethod
    def ForAll(fromInclusive: int, toExclusive: int, predicate: _n_0_t_1[int]) -> bool:...
    @staticmethod
    def Invariant(condition: bool, userMessage: str):...
    @staticmethod
    def Invariant(condition: bool):...
    @staticmethod
    def OldValue(value: typing.Any) -> typing.Any:...
    @staticmethod
    def Requires(condition: bool, userMessage: str):...
    @staticmethod
    def Requires(condition: bool):...
    @staticmethod
    def Result() -> typing.Any:...
    @staticmethod
    def ValueAtReturn(value: object) -> typing.Any:...
class ContractAbbreviatorAttribute(_n_0_t_2, _n_2_t_0):
    def __init__(self) -> ContractAbbreviatorAttribute:...
class ContractArgumentValidatorAttribute(_n_0_t_2, _n_2_t_0):
    def __init__(self) -> ContractArgumentValidatorAttribute:...
class ContractClassAttribute(_n_0_t_2, _n_2_t_0):
    @property
    def TypeContainingContracts(self) -> _n_0_t_3:"""TypeContainingContracts { get; } -> Type"""
    def __init__(self, typeContainingContracts: _n_0_t_3) -> ContractClassAttribute:...
class ContractClassForAttribute(_n_0_t_2, _n_2_t_0):
    @property
    def TypeContractsAreFor(self) -> _n_0_t_3:"""TypeContractsAreFor { get; } -> Type"""
    def __init__(self, typeContractsAreFor: _n_0_t_3) -> ContractClassForAttribute:...
class ContractFailedEventArgs(_n_0_t_4):
    @property
    def Condition(self) -> str:"""Condition { get; } -> str"""
    @property
    def FailureKind(self) -> ContractFailureKind:"""FailureKind { get; } -> ContractFailureKind"""
    @property
    def Handled(self) -> bool:"""Handled { get; } -> bool"""
    @property
    def Message(self) -> str:"""Message { get; } -> str"""
    @property
    def OriginalException(self) -> _n_0_t_5:"""OriginalException { get; } -> Exception"""
    @property
    def Unwind(self) -> bool:"""Unwind { get; } -> bool"""
    def __init__(self, failureKind: ContractFailureKind, message: str, condition: str, originalException: _n_0_t_5) -> ContractFailedEventArgs:...
    def SetHandled(self):...
    def SetUnwind(self):...
class ContractFailureKind(_n_0_t_6, _n_0_t_7, _n_0_t_8, _n_0_t_9):
    Assert: int
    Assume: int
    Invariant: int
    Postcondition: int
    PostconditionOnException: int
    Precondition: int
    value__: int
class ContractInvariantMethodAttribute(_n_0_t_2, _n_2_t_0):
    def __init__(self) -> ContractInvariantMethodAttribute:...
class ContractOptionAttribute(_n_0_t_2, _n_2_t_0):
    @property
    def Category(self) -> str:"""Category { get; } -> str"""
    @property
    def Enabled(self) -> bool:"""Enabled { get; } -> bool"""
    @property
    def Setting(self) -> str:"""Setting { get; } -> str"""
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def __init__(self, category: str, setting: str, value: str) -> ContractOptionAttribute:...
    def __init__(self, category: str, setting: str, enabled: bool) -> ContractOptionAttribute:...
class ContractPublicPropertyNameAttribute(_n_0_t_2, _n_2_t_0):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, name: str) -> ContractPublicPropertyNameAttribute:...
class ContractReferenceAssemblyAttribute(_n_0_t_2, _n_2_t_0):
    def __init__(self) -> ContractReferenceAssemblyAttribute:...
class ContractRuntimeIgnoredAttribute(_n_0_t_2, _n_2_t_0):
    def __init__(self) -> ContractRuntimeIgnoredAttribute:...
class ContractVerificationAttribute(_n_0_t_2, _n_2_t_0):
    @property
    def Value(self) -> bool:"""Value { get; } -> bool"""
    def __init__(self, value: bool) -> ContractVerificationAttribute:...
class PureAttribute(_n_0_t_2, _n_2_t_0):
    def __init__(self) -> PureAttribute:...
