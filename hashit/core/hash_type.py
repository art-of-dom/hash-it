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
