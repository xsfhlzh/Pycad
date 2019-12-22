from __clrclasses__.System import Exception as _n_0_t_0
from __clrclasses__.System.Diagnostics.Contracts import ContractFailureKind as _n_1_t_0
import typing
class ContractHelper(object):
    @staticmethod
    def RaiseContractFailedEvent(failureKind: _n_1_t_0, userMessage: str, conditionText: str, innerException: _n_0_t_0) -> str:...
    @staticmethod
    def TriggerFailure(kind: _n_1_t_0, displayMessage: str, userMessage: str, conditionText: str, innerException: _n_0_t_0):...
