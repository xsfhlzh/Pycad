from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import IDisposable as _n_0_t_4
from __clrclasses__.System.IO import Stream as _n_1_t_0
import typing
class CompressionLevel(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Fastest: int
    NoCompression: int
    Optimal: int
    value__: int
class CompressionMode(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Compress: int
    Decompress: int
    value__: int
class DeflateStream(_n_1_t_0, _n_0_t_4):
    @property
    def BaseStream(self) -> _n_1_t_0:"""BaseStream { get; } -> Stream"""
    def __init__(self, stream: _n_1_t_0, compressionLevel: CompressionLevel, leaveOpen: bool) -> DeflateStream:...
    def __init__(self, stream: _n_1_t_0, compressionLevel: CompressionLevel) -> DeflateStream:...
    def __init__(self, stream: _n_1_t_0, mode: CompressionMode, leaveOpen: bool) -> DeflateStream:...
    def __init__(self, stream: _n_1_t_0, mode: CompressionMode) -> DeflateStream:...
class GZipStream(_n_1_t_0, _n_0_t_4):
    @property
    def BaseStream(self) -> _n_1_t_0:"""BaseStream { get; } -> Stream"""
    def __init__(self, stream: _n_1_t_0, compressionLevel: CompressionLevel, leaveOpen: bool) -> GZipStream:...
    def __init__(self, stream: _n_1_t_0, compressionLevel: CompressionLevel) -> GZipStream:...
    def __init__(self, stream: _n_1_t_0, mode: CompressionMode, leaveOpen: bool) -> GZipStream:...
    def __init__(self, stream: _n_1_t_0, mode: CompressionMode) -> GZipStream:...
