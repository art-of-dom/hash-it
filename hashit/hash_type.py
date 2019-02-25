"""
HashType.py

Enumerates the hash types to easily allow choosing a hash.
"""

from enum import Enum
class HashType(Enum):
    CRC16 = 0
    CRC32 = 1
    MD2 = 2
    MD4 = 3
    MD5 = 4
    SHA1 = 5
    SHA224 = 6
    SHA256 = 7
    SHA384 = 8
    SHA512 = 9
