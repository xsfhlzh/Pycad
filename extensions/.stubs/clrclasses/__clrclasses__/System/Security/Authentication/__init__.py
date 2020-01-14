import __clrclasses__.System.Security.Authentication.ExtendedProtection as ExtendedProtection
from __clrclasses__.System import SystemException as _n_0_t_0
from __clrclasses__.System import Exception as _n_0_t_1
from __clrclasses__.System import Enum as _n_0_t_2
from __clrclasses__.System import IComparable as _n_0_t_3
from __clrclasses__.System import IFormattable as _n_0_t_4
from __clrclasses__.System import IConvertible as _n_0_t_5
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_1_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_2_t_0
import typing
class AuthenticationException(_n_0_t_0, _n_2_t_0, _n_1_t_0):
    def __init__(self, message: str, innerException: _n_0_t_1) -> AuthenticationException:...
    def __init__(self, message: str) -> AuthenticationException:...
    def __init__(self) -> AuthenticationException:...
class CipherAlgorithmType(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Aes: int
    Aes128: int
    Aes192: int
    Aes256: int
    Des: int
    _None: int
    Null: int
    Rc2: int
    Rc4: int
    TripleDes: int
    value__: int
class ExchangeAlgorithmType(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    DiffieHellman: int
    _None: int
    RsaKeyX: int
    RsaSign: int
    value__: int
class HashAlgorithmType(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Md5: int
    _None: int
    Sha1: int
    Sha256: int
    Sha384: int
    Sha512: int
    value__: int
class InvalidCredentialException(AuthenticationException, _n_2_t_0, _n_1_t_0):
    def __init__(self, message: str, innerException: _n_0_t_1) -> InvalidCredentialException:...
    def __init__(self, message: str) -> InvalidCredentialException:...
    def __init__(self) -> InvalidCredentialException:...
class SslProtocols(_n_0_t_2, _n_0_t_3, _n_0_t_4, _n_0_t_5):
    Default: int
    _None: int
    Ssl2: int
    Ssl3: int
    Tls: int
    Tls11: int
    Tls12: int
    value__: int
