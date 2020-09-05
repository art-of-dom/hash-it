"""
HashType.py

Enumerates the hash types to easily allow choosing a hash.
"""

from enum import Enum


class HashType(Enum):
    """An Enumerated representation of a hash used for parsing"""
    CRC8 = 0
    CRC8_CDMA2000 = 1
    CRC8_DARC = 2
    CRC8_DVB_S2 = 3
    CRC8_EBU = 4
    CRC8_I_CODE = 5
    CRC8_ITU = 6
    CRC8_MAXIM = 7
    CRC8_ROHC = 8
    CRC8_WCDMA = 9
    CRC16 = 10
    CRC32 = 11
    CRC64 = 12
    MD2 = 13
    MD4 = 14
    MD5 = 15
    SHA1 = 16
    SHA224 = 17
    SHA256 = 18
    SHA384 = 19
    SHA512 = 20

    def is_crc(self):
        return self.name.startswith('CRC')

    def is_md(self):
        return self.name.startswith('MD')

    def is_sha(self):
        return self.name.startswith('SHA')

    def hash_byte_length(self):
        """Gives the length in bytes of the hash"""
        if self.is_crc():
            return self._crc_byte_len()
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

    def _crc_byte_len(self):
        if self in CRC8_LIST:
            return 1
        if self is HashType.CRC16:
            return 2
        if self is HashType.CRC32:
            return 4
        if self is HashType.CRC64:
            return 8
        return 0

CRC8_LIST = [
    HashType.CRC8,
    HashType.CRC8_CDMA2000,
    HashType.CRC8_DARC,
    HashType.CRC8_DVB_S2,
    HashType.CRC8_EBU,
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
