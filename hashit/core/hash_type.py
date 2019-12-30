"""
HashType.py

Enumerates the hash types to easily allow choosing a hash.
"""

from enum import Enum


class HashType(Enum):
    '''
    An Enumerated representation of a hash used for parsing
    '''
    CRC8 = 0
    CRC16 = 1
    CRC32 = 2
    CRC64 = 3
    MD2 = 4
    MD4 = 5
    MD5 = 6
    SHA1 = 7
    SHA224 = 8
    SHA256 = 9
    SHA384 = 10
    SHA512 = 11
