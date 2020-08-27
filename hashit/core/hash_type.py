"""
HashType.py

Enumerates the hash types to easily allow choosing a hash.
"""

from enum import Enum


class HashType(Enum):
    """
    An Enumerated representation of a hash used for parsing
    """
    CRC8 = 0
    CRC8_DARC = 1
    CRC8_I_CODE = 2
    CRC8_ITU = 3
    CRC8_MAXIM = 4
    CRC8_ROHC = 5
    CRC8_WCDMA = 6
    CRC16 = 7
    CRC32 = 8
    CRC64 = 9
    MD2 = 10
    MD4 = 11
    MD5 = 12
    SHA1 = 13
    SHA224 = 14
    SHA256 = 15
    SHA384 = 16
    SHA512 = 17

    def hash_byte_length(self):
        """Gives the length in bytes of the hash"""
        if self in CRC8_LIST:
            return 1
        if self is HashType.CRC16:
            return 2
        if self is HashType.CRC32:
            return 4
        if self is HashType.CRC64:
            return 8
        if self in MD_LIST:
            return 16
        if self is HashType.SHA1:
            return 20
        if self is HashType.SHA224:
            return 28
        if self is HashType.SHA256:
            return 32
        if self is HashType.SHA384:
            return 48
        if self is HashType.SHA512:
            return 64
        return 0

    def hash_str_length(self):
        """Gives the length in characters of the hash"""
        return self.hash_byte_length() * 2


CRC8_LIST = [
    HashType.CRC8,
    HashType.CRC8_DARC,
    HashType.CRC8_I_CODE,
    HashType.CRC8_ITU,
    HashType.CRC8_MAXIM,
    HashType.CRC8_ROHC,
    HashType.CRC8_WCDMA
]


MD_LIST = [
    HashType.MD2,
    HashType.MD4,
    HashType.MD5,
]
