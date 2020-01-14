import typing as __typing
import System as __System
import Microsoft as __Microsoft

IsDebug: bool
IsMacOS: bool
IsMono: bool
IsNetCoreApp: bool
References: __typing.Tuple[__System.Reflection.Assembly]
TargetFramework: str

def AddReference(*references: __typing.Iterable):
    """
    Adds a reference to a .NET assembly.  Parameters can be an already loaded
    Assembly object, a full assembly name, or a partial assembly name. After the
    load the assemblies namespaces and top-level types will be available via
    import Namespace.
    """

def AddReferenceByName(*names: __typing.Iterable[str]):
    """
    Adds a reference to a .NET assembly.  Parameters are an assembly name.
    After the load the assemblies namespaces and top-level types will be available via
    import Namespace.
    """

def AddReferenceByPartialName(*names: __typing.Iterable[str]):
    """
    Adds a reference to a .NET assembly.  Parameters are a partial assembly name.
    After the load the assemblies namespaces and top-level types will be available via
    import Namespace.
    """

def AddReferenceToFile(*files: __typing.Iterable[str]):
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided.  The assembly is searched for in the directories specified in
    sys.path and dependencies will be loaded from sys.path as well.  The assembly
    name should be the filename on disk without a directory specifier and
    optionally including the .EXE or .DLL extension. After the load the assemblies
    namespaces and top-level types will be available via import Namespace.
    """

def AddReferenceToFileAndPath(*files: __typing.Iterable[str]):
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided which are fully qualified names to the file on disk.  The
    directory is added to sys.path and AddReferenceToFile is then called. After the
    load the assemblies namespaces and top-level types will be available via
    import Namespace.
    """

@__typing.overload
def AddReferenceToTypeLibrary(rcw: object):
    """
    Makes the type lib desc available for importing. See also LoadTypeLibrary.
    """

@__typing.overload
def AddReferenceToTypeLibrary(typeLibGuid: __System.Guid):...

def ClearProfilerData():
    """
    Resets all profiler counters back to zero.
    """

def CompileModules(assemblyName: str, **kwArgs: __typing.Dict[str, object], *filenames: __typing.Iterable[str]):...

def CompileSubclassTypes(assemblyName: str, *newTypes: __typing.Iterable):...

def Convert(obj: object, toType: __System.Type) -> object:...

def Deserialize(serializationFormat: str, data: str) -> object:...

def Dir(obj: object) -> list:...

def DirClr(obj: object) -> list:...

def EnableProfiler(enable: bool):...

def GetBytes(s: str) -> __System.Array[__System.Byte]:
    """
    Converts a string to an array of bytesConverts maxCount of a string to an array of bytes.
    """

def GetClrType(type: type) -> __System.Type:...

def GetCurrentRuntime() -> __Microsoft.Scripting.Runtime.ScriptDomainManager:...

def GetDynamicType(t: __System.Type) -> type:...

def GetProfilerData(includeUnused: bool) -> __typing.Tuple:...

def GetPythonType(t: __System.Type) -> type:...

def GetString(bytes: __System.Array[Byte], maxCount: int):
    """
    Converts an array of bytes to a string.Converts maxCount of an array of bytes to a string
    """

def GetSubclassedTypes() -> __typing.Tuple:...

def ImportExtensions(type: type):...

def LoadAssemblyByName(name: str) -> __System.Reflection.Assembly:
    """
    Loads an assembly from the specified assembly name and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from
    the assembly object.
    """

def LoadAssemblyByPartialName(name: str) -> __System.Reflection.Assembly:
    """
    Loads an assembly from the specified partial assembly name and returns the
    assembly object.  Namespaces or types in the assembly can be accessed directly
    from the assembly object.
    """

def LoadAssemblyFromFileWithPath(file: str) -> __System.Reflection.Assembly:
    """
    Adds a reference to a .NET assembly.  Parameters are a full path to an.
    assembly on disk. After the load the assemblies namespaces and top-level types
    will be available via import Namespace.
    """

@__typing.overload
def LoadTypeLibrary(rcw: object) -> ComTypeLibInfo:...

@__typing.overload
def LoadTypeLibrary(typeLibGuid: __System.Guid) -> ComTypeLibInfo:...

def Reference(type: type):...

def Serialize(self: object) -> __typing.Tuple:...

def SetCommandDispatcher(dispatcher: __System.Action[System.Action]) -> __System.Action[__System.Action]:...

@__typing.overload
def Use(path: str, language: str) -> object:...

@__typing.overload
def Use(name: str) -> object:...

def accepts(*types: Array[object]) -> object:...

def returns(type: object) -> object:...

class ArgChecker(object):
    def __init__(self, prms: __typing.Tuple):...
