from __clrclasses__.System import EventHandler as _n_0_t_0
import typing
class ICommand():
    @property
    def CanExecuteChanged(self) -> _n_0_t_0:
        """CanExecuteChanged Event: EventHandler"""
    def CanExecute(self, parameter: object) -> bool:...
    def Execute(self, parameter: object):...
