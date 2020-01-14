from __clrclasses__.System import Type as _n_0_t_0
from __clrclasses__.System import Enum as _n_0_t_1
from __clrclasses__.System import IComparable as _n_0_t_2
from __clrclasses__.System import IFormattable as _n_0_t_3
from __clrclasses__.System import IConvertible as _n_0_t_4
from __clrclasses__.System import Func as _n_0_t_5
from __clrclasses__.System import Array as _n_0_t_6
from __clrclasses__.System import Delegate as _n_0_t_7
from __clrclasses__.System import Guid as _n_0_t_8
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_1_t_0
from __clrclasses__.System.Collections.ObjectModel import ReadOnlyCollection as _n_2_t_0
from __clrclasses__.System.Reflection import MethodInfo as _n_3_t_0
from __clrclasses__.System.Reflection import PropertyInfo as _n_3_t_1
from __clrclasses__.System.Reflection import MemberInfo as _n_3_t_2
from __clrclasses__.System.Reflection import ConstructorInfo as _n_3_t_3
from __clrclasses__.System.Reflection.Emit import MethodBuilder as _n_4_t_0
from __clrclasses__.System.Runtime.CompilerServices import CallSiteBinder as _n_5_t_0
from __clrclasses__.System.Runtime.CompilerServices import DebugInfoGenerator as _n_5_t_1
import typing
TDelegate = typing.TypeVar('TDelegate')
class BinaryExpression(Expression):
    @property
    def Conversion(self) -> LambdaExpression:"""Conversion { get; } -> LambdaExpression"""
    @property
    def IsLifted(self) -> bool:"""IsLifted { get; } -> bool"""
    @property
    def IsLiftedToNull(self) -> bool:"""IsLiftedToNull { get; } -> bool"""
    @property
    def Left(self) -> Expression:"""Left { get; } -> Expression"""
    @property
    def Method(self) -> _n_3_t_0:"""Method { get; } -> MethodInfo"""
    @property
    def Right(self) -> Expression:"""Right { get; } -> Expression"""
    def Update(self, left: Expression, conversion: LambdaExpression, right: Expression) -> BinaryExpression:...
class BlockExpression(Expression):
    @property
    def Expressions(self) -> _n_2_t_0[Expression]:"""Expressions { get; } -> ReadOnlyCollection"""
    @property
    def Result(self) -> Expression:"""Result { get; } -> Expression"""
    @property
    def Variables(self) -> _n_2_t_0[ParameterExpression]:"""Variables { get; } -> ReadOnlyCollection"""
    def Update(self, variables: _n_1_t_0[ParameterExpression], expressions: _n_1_t_0[Expression]) -> BlockExpression:...
class CatchBlock(object):
    @property
    def Body(self) -> Expression:"""Body { get; } -> Expression"""
    @property
    def Filter(self) -> Expression:"""Filter { get; } -> Expression"""
    @property
    def Test(self) -> _n_0_t_0:"""Test { get; } -> Type"""
    @property
    def Variable(self) -> ParameterExpression:"""Variable { get; } -> ParameterExpression"""
    def Update(self, variable: ParameterExpression, filter: Expression, body: Expression) -> CatchBlock:...
class ConditionalExpression(Expression):
    @property
    def IfFalse(self) -> Expression:"""IfFalse { get; } -> Expression"""
    @property
    def IfTrue(self) -> Expression:"""IfTrue { get; } -> Expression"""
    @property
    def Test(self) -> Expression:"""Test { get; } -> Expression"""
    def Update(self, test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression:...
class ConstantExpression(Expression):
    @property
    def Value(self) -> object:"""Value { get; } -> object"""
class DebugInfoExpression(Expression):
    @property
    def Document(self) -> SymbolDocumentInfo:"""Document { get; } -> SymbolDocumentInfo"""
    @property
    def EndColumn(self) -> int:"""EndColumn { get; } -> int"""
    @property
    def EndLine(self) -> int:"""EndLine { get; } -> int"""
    @property
    def IsClear(self) -> bool:"""IsClear { get; } -> bool"""
    @property
    def StartColumn(self) -> int:"""StartColumn { get; } -> int"""
    @property
    def StartLine(self) -> int:"""StartLine { get; } -> int"""
class DefaultExpression(Expression):
    pass
class DynamicExpression(Expression, IDynamicExpression):
    @property
    def Arguments(self) -> _n_2_t_0[Expression]:"""Arguments { get; } -> ReadOnlyCollection"""
    @property
    def Binder(self) -> _n_5_t_0:"""Binder { get; } -> CallSiteBinder"""
    def Update(self, arguments: _n_1_t_0[Expression]) -> DynamicExpression:...
class DynamicExpressionVisitor(ExpressionVisitor):
    pass
class ElementInit(IArgumentProvider):
    @property
    def AddMethod(self) -> _n_3_t_0:"""AddMethod { get; } -> MethodInfo"""
    @property
    def Arguments(self) -> _n_2_t_0[Expression]:"""Arguments { get; } -> ReadOnlyCollection"""
    def Update(self, arguments: _n_1_t_0[Expression]) -> ElementInit:...
class Expression(LambdaExpression, typing.Generic[TDelegate]):
    def Update(self, body: Expression, parameters: _n_1_t_0[ParameterExpression]) -> Expression[TDelegate]:...
class ExpressionType(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    Add: int
    AddAssign: int
    AddAssignChecked: int
    AddChecked: int
    And: int
    AndAlso: int
    AndAssign: int
    ArrayIndex: int
    ArrayLength: int
    Assign: int
    Block: int
    Call: int
    Coalesce: int
    Conditional: int
    Constant: int
    Convert: int
    ConvertChecked: int
    DebugInfo: int
    Decrement: int
    Default: int
    Divide: int
    DivideAssign: int
    Dynamic: int
    Equal: int
    ExclusiveOr: int
    ExclusiveOrAssign: int
    Extension: int
    Goto: int
    GreaterThan: int
    GreaterThanOrEqual: int
    Increment: int
    Index: int
    Invoke: int
    IsFalse: int
    IsTrue: int
    Label: int
    Lambda: int
    LeftShift: int
    LeftShiftAssign: int
    LessThan: int
    LessThanOrEqual: int
    ListInit: int
    Loop: int
    MemberAccess: int
    MemberInit: int
    Modulo: int
    ModuloAssign: int
    Multiply: int
    MultiplyAssign: int
    MultiplyAssignChecked: int
    MultiplyChecked: int
    Negate: int
    NegateChecked: int
    New: int
    NewArrayBounds: int
    NewArrayInit: int
    Not: int
    NotEqual: int
    OnesComplement: int
    Or: int
    OrAssign: int
    OrElse: int
    Parameter: int
    PostDecrementAssign: int
    PostIncrementAssign: int
    Power: int
    PowerAssign: int
    PreDecrementAssign: int
    PreIncrementAssign: int
    Quote: int
    RightShift: int
    RightShiftAssign: int
    RuntimeVariables: int
    Subtract: int
    SubtractAssign: int
    SubtractAssignChecked: int
    SubtractChecked: int
    Switch: int
    Throw: int
    Try: int
    TypeAs: int
    TypeEqual: int
    TypeIs: int
    UnaryPlus: int
    Unbox: int
    value__: int
class ExpressionVisitor(object):
    @staticmethod
    def Visit(nodes: _n_2_t_0[typing.Any], elementVisitor: _n_0_t_5[typing.Any, typing.Any]) -> _n_2_t_0[typing.Any]:...
    def Visit(self, nodes: _n_2_t_0[Expression]) -> _n_2_t_0[Expression]:...
    def Visit(self, node: Expression) -> Expression:...
    def VisitAndConvert(self, nodes: _n_2_t_0[typing.Any], callerName: str) -> _n_2_t_0[typing.Any]:...
    def VisitAndConvert(self, node: typing.Any, callerName: str) -> typing.Any:...
class GotoExpression(Expression):
    @property
    def Kind(self) -> GotoExpressionKind:"""Kind { get; } -> GotoExpressionKind"""
    @property
    def Target(self) -> LabelTarget:"""Target { get; } -> LabelTarget"""
    @property
    def Value(self) -> Expression:"""Value { get; } -> Expression"""
    def Update(self, target: LabelTarget, value: Expression) -> GotoExpression:...
class GotoExpressionKind(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    Break: int
    Continue: int
    Goto: int
    Return: int
    value__: int
class IArgumentProvider():
    @property
    def ArgumentCount(self) -> int:"""ArgumentCount { get; } -> int"""
    def GetArgument(self, index: int) -> Expression:...
class IDynamicExpression(IArgumentProvider):
    @property
    def DelegateType(self) -> _n_0_t_0:"""DelegateType { get; } -> Type"""
    def CreateCallSite(self) -> object:...
    def Rewrite(self, args: _n_0_t_6[Expression]) -> Expression:...
class IndexExpression(Expression, IArgumentProvider):
    @property
    def Arguments(self) -> _n_2_t_0[Expression]:"""Arguments { get; } -> ReadOnlyCollection"""
    @property
    def Indexer(self) -> _n_3_t_1:"""Indexer { get; } -> PropertyInfo"""
    @property
    def Object(self) -> Expression:"""Object { get; } -> Expression"""
    def Update(self, object: Expression, arguments: _n_1_t_0[Expression]) -> IndexExpression:...
class InvocationExpression(Expression, IArgumentProvider):
    @property
    def Arguments(self) -> _n_2_t_0[Expression]:"""Arguments { get; } -> ReadOnlyCollection"""
    @property
    def Expression(self) -> Expression:"""Expression { get; } -> Expression"""
    def Update(self, expression: Expression, arguments: _n_1_t_0[Expression]) -> InvocationExpression:...
class LabelExpression(Expression):
    @property
    def DefaultValue(self) -> Expression:"""DefaultValue { get; } -> Expression"""
    @property
    def Target(self) -> LabelTarget:"""Target { get; } -> LabelTarget"""
    def Update(self, target: LabelTarget, defaultValue: Expression) -> LabelExpression:...
class LabelTarget(object):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Type(self) -> _n_0_t_0:"""Type { get; } -> Type"""
class LambdaExpression(Expression):
    @property
    def Body(self) -> Expression:"""Body { get; } -> Expression"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def Parameters(self) -> _n_2_t_0[ParameterExpression]:"""Parameters { get; } -> ReadOnlyCollection"""
    @property
    def ReturnType(self) -> _n_0_t_0:"""ReturnType { get; } -> Type"""
    @property
    def TailCall(self) -> bool:"""TailCall { get; } -> bool"""
    def Compile(self, preferInterpretation: bool) -> _n_0_t_7:...
    def Compile(self, debugInfoGenerator: _n_5_t_1) -> _n_0_t_7:...
    def Compile(self) -> _n_0_t_7:...
    def CompileToMethod(self, method: _n_4_t_0, debugInfoGenerator: _n_5_t_1):...
    def CompileToMethod(self, method: _n_4_t_0):...
class ListInitExpression(Expression):
    @property
    def Initializers(self) -> _n_2_t_0[ElementInit]:"""Initializers { get; } -> ReadOnlyCollection"""
    @property
    def NewExpression(self) -> NewExpression:"""NewExpression { get; } -> NewExpression"""
    def Update(self, newExpression: NewExpression, initializers: _n_1_t_0[ElementInit]) -> ListInitExpression:...
class LoopExpression(Expression):
    @property
    def Body(self) -> Expression:"""Body { get; } -> Expression"""
    @property
    def BreakLabel(self) -> LabelTarget:"""BreakLabel { get; } -> LabelTarget"""
    @property
    def ContinueLabel(self) -> LabelTarget:"""ContinueLabel { get; } -> LabelTarget"""
    def Update(self, breakLabel: LabelTarget, continueLabel: LabelTarget, body: Expression) -> LoopExpression:...
class MemberAssignment(MemberBinding):
    @property
    def Expression(self) -> Expression:"""Expression { get; } -> Expression"""
    def Update(self, expression: Expression) -> MemberAssignment:...
class MemberBinding(object):
    @property
    def BindingType(self) -> MemberBindingType:"""BindingType { get; } -> MemberBindingType"""
    @property
    def Member(self) -> _n_3_t_2:"""Member { get; } -> MemberInfo"""
class MemberBindingType(_n_0_t_1, _n_0_t_2, _n_0_t_3, _n_0_t_4):
    Assignment: int
    ListBinding: int
    MemberBinding: int
    value__: int
class MemberExpression(Expression):
    @property
    def Expression(self) -> Expression:"""Expression { get; } -> Expression"""
    @property
    def Member(self) -> _n_3_t_2:"""Member { get; } -> MemberInfo"""
    def Update(self, expression: Expression) -> MemberExpression:...
class MemberInitExpression(Expression):
    @property
    def Bindings(self) -> _n_2_t_0[MemberBinding]:"""Bindings { get; } -> ReadOnlyCollection"""
    @property
    def NewExpression(self) -> NewExpression:"""NewExpression { get; } -> NewExpression"""
    def Update(self, newExpression: NewExpression, bindings: _n_1_t_0[MemberBinding]) -> MemberInitExpression:...
class MemberListBinding(MemberBinding):
    @property
    def Initializers(self) -> _n_2_t_0[ElementInit]:"""Initializers { get; } -> ReadOnlyCollection"""
    def Update(self, initializers: _n_1_t_0[ElementInit]) -> MemberListBinding:...
class MemberMemberBinding(MemberBinding):
    @property
    def Bindings(self) -> _n_2_t_0[MemberBinding]:"""Bindings { get; } -> ReadOnlyCollection"""
    def Update(self, bindings: _n_1_t_0[MemberBinding]) -> MemberMemberBinding:...
class MethodCallExpression(Expression, IArgumentProvider):
    @property
    def Arguments(self) -> _n_2_t_0[Expression]:"""Arguments { get; } -> ReadOnlyCollection"""
    @property
    def Method(self) -> _n_3_t_0:"""Method { get; } -> MethodInfo"""
    @property
    def Object(self) -> Expression:"""Object { get; } -> Expression"""
    def Update(self, object: Expression, arguments: _n_1_t_0[Expression]) -> MethodCallExpression:...
class NewArrayExpression(Expression):
    @property
    def Expressions(self) -> _n_2_t_0[Expression]:"""Expressions { get; } -> ReadOnlyCollection"""
    def Update(self, expressions: _n_1_t_0[Expression]) -> NewArrayExpression:...
class NewExpression(Expression, IArgumentProvider):
    @property
    def Arguments(self) -> _n_2_t_0[Expression]:"""Arguments { get; } -> ReadOnlyCollection"""
    @property
    def Constructor(self) -> _n_3_t_3:"""Constructor { get; } -> ConstructorInfo"""
    @property
    def Members(self) -> _n_2_t_0[_n_3_t_2]:"""Members { get; } -> ReadOnlyCollection"""
    def Update(self, arguments: _n_1_t_0[Expression]) -> NewExpression:...
class ParameterExpression(Expression):
    @property
    def IsByRef(self) -> bool:"""IsByRef { get; } -> bool"""
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
class RuntimeVariablesExpression(Expression):
    @property
    def Variables(self) -> _n_2_t_0[ParameterExpression]:"""Variables { get; } -> ReadOnlyCollection"""
    def Update(self, variables: _n_1_t_0[ParameterExpression]) -> RuntimeVariablesExpression:...
class SwitchCase(object):
    @property
    def Body(self) -> Expression:"""Body { get; } -> Expression"""
    @property
    def TestValues(self) -> _n_2_t_0[Expression]:"""TestValues { get; } -> ReadOnlyCollection"""
    def Update(self, testValues: _n_1_t_0[Expression], body: Expression) -> SwitchCase:...
class SwitchExpression(Expression):
    @property
    def Cases(self) -> _n_2_t_0[SwitchCase]:"""Cases { get; } -> ReadOnlyCollection"""
    @property
    def Comparison(self) -> _n_3_t_0:"""Comparison { get; } -> MethodInfo"""
    @property
    def DefaultBody(self) -> Expression:"""DefaultBody { get; } -> Expression"""
    @property
    def SwitchValue(self) -> Expression:"""SwitchValue { get; } -> Expression"""
    def Update(self, switchValue: Expression, cases: _n_1_t_0[SwitchCase], defaultBody: Expression) -> SwitchExpression:...
class SymbolDocumentInfo(object):
    @property
    def DocumentType(self) -> _n_0_t_8:"""DocumentType { get; } -> Guid"""
    @property
    def FileName(self) -> str:"""FileName { get; } -> str"""
    @property
    def Language(self) -> _n_0_t_8:"""Language { get; } -> Guid"""
    @property
    def LanguageVendor(self) -> _n_0_t_8:"""LanguageVendor { get; } -> Guid"""
class TryExpression(Expression):
    @property
    def Body(self) -> Expression:"""Body { get; } -> Expression"""
    @property
    def Fault(self) -> Expression:"""Fault { get; } -> Expression"""
    @property
    def Finally(self) -> Expression:"""Finally { get; } -> Expression"""
    @property
    def Handlers(self) -> _n_2_t_0[CatchBlock]:"""Handlers { get; } -> ReadOnlyCollection"""
    def Update(self, body: Expression, handlers: _n_1_t_0[CatchBlock], _finally: Expression, fault: Expression) -> TryExpression:...
class TypeBinaryExpression(Expression):
    @property
    def Expression(self) -> Expression:"""Expression { get; } -> Expression"""
    @property
    def TypeOperand(self) -> _n_0_t_0:"""TypeOperand { get; } -> Type"""
    def Update(self, expression: Expression) -> TypeBinaryExpression:...
class UnaryExpression(Expression):
    @property
    def IsLifted(self) -> bool:"""IsLifted { get; } -> bool"""
    @property
    def IsLiftedToNull(self) -> bool:"""IsLiftedToNull { get; } -> bool"""
    @property
    def Method(self) -> _n_3_t_0:"""Method { get; } -> MethodInfo"""
    @property
    def Operand(self) -> Expression:"""Operand { get; } -> Expression"""
    def Update(self, operand: Expression) -> UnaryExpression:...
