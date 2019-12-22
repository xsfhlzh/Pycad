from __clrclasses__.System import IDisposable as _n_0_t_0
from __clrclasses__.System import IntPtr as _n_0_t_1
from __clrclasses__.System.Runtime.InteropServices import CriticalHandle as _n_1_t_0
from __clrclasses__.System.Runtime.InteropServices import SafeHandle as _n_1_t_1
from __clrclasses__.System.Runtime.InteropServices import SafeBuffer as _n_1_t_2
import typing
class CriticalHandleMinusOneIsInvalid(_n_1_t_0, _n_0_t_0):
    pass
class CriticalHandleZeroOrMinusOneIsInvalid(_n_1_t_0, _n_0_t_0):
    pass
class SafeAccessTokenHandle(_n_1_t_1, _n_0_t_0):
    @property
    def InvalidHandle(self) -> SafeAccessTokenHandle:"""InvalidHandle { get; } -> SafeAccessTokenHandle"""
    def __init__(self, handle: _n_0_t_1) -> SafeAccessTokenHandle:...
class SafeFileHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    def __init__(self, preexistingHandle: _n_0_t_1, ownsHandle: bool) -> SafeFileHandle:...
class SafeHandleMinusOneIsInvalid(_n_1_t_1, _n_0_t_0):
    pass
class SafeHandleZeroOrMinusOneIsInvalid(_n_1_t_1, _n_0_t_0):
    pass
class SafeMemoryMappedFileHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    pass
class SafeMemoryMappedViewHandle(_n_1_t_2, _n_0_t_0):
    pass
class SafeNCryptHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    pass
class SafeNCryptKeyHandle(SafeNCryptHandle, _n_0_t_0):
    def __init__(self) -> SafeNCryptKeyHandle:...
    def __init__(self, handle: _n_0_t_1, parentHandle: _n_1_t_1) -> SafeNCryptKeyHandle:...
class SafeNCryptProviderHandle(SafeNCryptHandle, _n_0_t_0):
    def __init__(self) -> SafeNCryptProviderHandle:...
class SafeNCryptSecretHandle(SafeNCryptHandle, _n_0_t_0):
    def __init__(self) -> SafeNCryptSecretHandle:...
class SafePipeHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    def __init__(self, preexistingHandle: _n_0_t_1, ownsHandle: bool) -> SafePipeHandle:...
class SafeProcessHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    def __init__(self, existingHandle: _n_0_t_1, ownsHandle: bool) -> SafeProcessHandle:...
class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    def __init__(self, preexistingHandle: _n_0_t_1, ownsHandle: bool) -> SafeRegistryHandle:...
class SafeWaitHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    def __init__(self, existingHandle: _n_0_t_1, ownsHandle: bool) -> SafeWaitHandle:...
class SafeX509ChainHandle(SafeHandleZeroOrMinusOneIsInvalid, _n_0_t_0):
    pass
