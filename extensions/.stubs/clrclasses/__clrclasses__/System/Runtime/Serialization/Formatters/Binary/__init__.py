from __clrclasses__.System.IO import Stream as _n_0_t_0
from __clrclasses__.System.Runtime.Remoting.Messaging import IRemotingFormatter as _n_1_t_0
from __clrclasses__.System.Runtime.Remoting.Messaging import HeaderHandler as _n_1_t_1
from __clrclasses__.System.Runtime.Remoting.Messaging import IMethodCallMessage as _n_1_t_2
from __clrclasses__.System.Runtime.Serialization import ISurrogateSelector as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import StreamingContext as _n_2_t_1
from __clrclasses__.System.Runtime.Serialization.Formatters import FormatterAssemblyStyle as _n_3_t_0
from __clrclasses__.System.Runtime.Serialization.Formatters import TypeFilterLevel as _n_3_t_1
from __clrclasses__.System.Runtime.Serialization.Formatters import FormatterTypeStyle as _n_3_t_2
import typing
class BinaryFormatter(_n_1_t_0):
    @property
    def AssemblyFormat(self) -> _n_3_t_0:"""AssemblyFormat { get; set; } -> FormatterAssemblyStyle"""
    @property
    def FilterLevel(self) -> _n_3_t_1:"""FilterLevel { get; set; } -> TypeFilterLevel"""
    @property
    def TypeFormat(self) -> _n_3_t_2:"""TypeFormat { get; set; } -> FormatterTypeStyle"""
    def __init__(self, selector: _n_2_t_0, context: _n_2_t_1) -> BinaryFormatter:...
    def __init__(self) -> BinaryFormatter:...
    def DeserializeMethodResponse(self, serializationStream: _n_0_t_0, handler: _n_1_t_1, methodCallMessage: _n_1_t_2) -> object:...
    def UnsafeDeserialize(self, serializationStream: _n_0_t_0, handler: _n_1_t_1) -> object:...
    def UnsafeDeserializeMethodResponse(self, serializationStream: _n_0_t_0, handler: _n_1_t_1, methodCallMessage: _n_1_t_2) -> object:...
