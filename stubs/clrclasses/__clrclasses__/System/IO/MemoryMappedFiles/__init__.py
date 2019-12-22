from __clrclasses__.Microsoft.Win32.SafeHandles import SafeMemoryMappedFileHandle as _n_0_t_0
from __clrclasses__.Microsoft.Win32.SafeHandles import SafeMemoryMappedViewHandle as _n_0_t_1
from __clrclasses__.System import IDisposable as _n_1_t_0
from __clrclasses__.System import Enum as _n_1_t_1
from __clrclasses__.System import IComparable as _n_1_t_2
from __clrclasses__.System import IFormattable as _n_1_t_3
from __clrclasses__.System import IConvertible as _n_1_t_4
from __clrclasses__.System.IO import FileStream as _n_2_t_0
from __clrclasses__.System.IO import HandleInheritability as _n_2_t_1
from __clrclasses__.System.IO import FileMode as _n_2_t_2
from __clrclasses__.System.IO import UnmanagedMemoryAccessor as _n_2_t_3
from __clrclasses__.System.IO import UnmanagedMemoryStream as _n_2_t_4
from __clrclasses__.System.Security.AccessControl import ObjectSecurity as _n_3_t_0
import typing
class MemoryMappedFile(_n_1_t_0):
    @property
    def SafeMemoryMappedFileHandle(self) -> _n_0_t_0:"""SafeMemoryMappedFileHandle { get; } -> SafeMemoryMappedFileHandle"""
    @staticmethod
    def CreateFromFile(fileStream: _n_2_t_0, mapName: str, capacity: int, access: MemoryMappedFileAccess, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: _n_2_t_1, leaveOpen: bool) -> MemoryMappedFile:...
    @staticmethod
    def CreateFromFile(fileStream: _n_2_t_0, mapName: str, capacity: int, access: MemoryMappedFileAccess, inheritability: _n_2_t_1, leaveOpen: bool) -> MemoryMappedFile:...
    @staticmethod
    def CreateFromFile(path: str, mode: _n_2_t_2, mapName: str, capacity: int, access: MemoryMappedFileAccess) -> MemoryMappedFile:...
    @staticmethod
    def CreateFromFile(path: str, mode: _n_2_t_2, mapName: str, capacity: int) -> MemoryMappedFile:...
    @staticmethod
    def CreateFromFile(path: str, mode: _n_2_t_2, mapName: str) -> MemoryMappedFile:...
    @staticmethod
    def CreateFromFile(path: str, mode: _n_2_t_2) -> MemoryMappedFile:...
    @staticmethod
    def CreateFromFile(path: str) -> MemoryMappedFile:...
    @staticmethod
    def CreateNew(mapName: str, capacity: int, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: _n_2_t_1) -> MemoryMappedFile:...
    @staticmethod
    def CreateNew(mapName: str, capacity: int, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, inheritability: _n_2_t_1) -> MemoryMappedFile:...
    @staticmethod
    def CreateNew(mapName: str, capacity: int, access: MemoryMappedFileAccess) -> MemoryMappedFile:...
    @staticmethod
    def CreateNew(mapName: str, capacity: int) -> MemoryMappedFile:...
    @staticmethod
    def CreateOrOpen(mapName: str, capacity: int, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, memoryMappedFileSecurity: MemoryMappedFileSecurity, inheritability: _n_2_t_1) -> MemoryMappedFile:...
    @staticmethod
    def CreateOrOpen(mapName: str, capacity: int, access: MemoryMappedFileAccess, options: MemoryMappedFileOptions, inheritability: _n_2_t_1) -> MemoryMappedFile:...
    @staticmethod
    def CreateOrOpen(mapName: str, capacity: int, access: MemoryMappedFileAccess) -> MemoryMappedFile:...
    @staticmethod
    def CreateOrOpen(mapName: str, capacity: int) -> MemoryMappedFile:...
    def CreateViewAccessor(self, offset: int, size: int, access: MemoryMappedFileAccess) -> MemoryMappedViewAccessor:...
    def CreateViewAccessor(self, offset: int, size: int) -> MemoryMappedViewAccessor:...
    def CreateViewAccessor(self) -> MemoryMappedViewAccessor:...
    def CreateViewStream(self, offset: int, size: int, access: MemoryMappedFileAccess) -> MemoryMappedViewStream:...
    def CreateViewStream(self, offset: int, size: int) -> MemoryMappedViewStream:...
    def CreateViewStream(self) -> MemoryMappedViewStream:...
    def GetAccessControl(self) -> MemoryMappedFileSecurity:...
    @staticmethod
    def OpenExisting(mapName: str, desiredAccessRights: MemoryMappedFileRights, inheritability: _n_2_t_1) -> MemoryMappedFile:...
    @staticmethod
    def OpenExisting(mapName: str, desiredAccessRights: MemoryMappedFileRights) -> MemoryMappedFile:...
    @staticmethod
    def OpenExisting(mapName: str) -> MemoryMappedFile:...
    def SetAccessControl(self, memoryMappedFileSecurity: MemoryMappedFileSecurity):...
class MemoryMappedFileAccess(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    CopyOnWrite: int
    Read: int
    ReadExecute: int
    ReadWrite: int
    ReadWriteExecute: int
    value__: int
    Write: int
class MemoryMappedFileOptions(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    DelayAllocatePages: int
    _None: int
    value__: int
class MemoryMappedFileRights(_n_1_t_1, _n_1_t_2, _n_1_t_3, _n_1_t_4):
    AccessSystemSecurity: int
    ChangePermissions: int
    CopyOnWrite: int
    Delete: int
    Execute: int
    FullControl: int
    Read: int
    ReadExecute: int
    ReadPermissions: int
    ReadWrite: int
    ReadWriteExecute: int
    TakeOwnership: int
    value__: int
    Write: int
class MemoryMappedFileSecurity(_n_3_t_0[MemoryMappedFileRights]):
    def __init__(self) -> MemoryMappedFileSecurity:...
class MemoryMappedViewAccessor(_n_2_t_3, _n_1_t_0):
    @property
    def PointerOffset(self) -> int:"""PointerOffset { get; } -> int"""
    @property
    def SafeMemoryMappedViewHandle(self) -> _n_0_t_1:"""SafeMemoryMappedViewHandle { get; } -> SafeMemoryMappedViewHandle"""
    def Flush(self):...
class MemoryMappedViewStream(_n_2_t_4, _n_1_t_0):
    @property
    def PointerOffset(self) -> int:"""PointerOffset { get; } -> int"""
    @property
    def SafeMemoryMappedViewHandle(self) -> _n_0_t_1:"""SafeMemoryMappedViewHandle { get; } -> SafeMemoryMappedViewHandle"""
