"""
hash_type.py
The heavy hitter of hashing.
"""
from __future__ import absolute_import

import hashlib

import crcmod
import six

from hashit.core.hash_type import HashType


HASHLIB_MAPPING = {
    HashType.CRC8: crcmod.predefined.Crc('crc-8').new,
    HashType.CRC8_DARC: crcmod.predefined.Crc('crc-8-darc').new,
    HashType.CRC8_I_CODE: crcmod.predefined.Crc('crc-8-i-code').new,
    HashType.CRC8_ITU: crcmod.predefined.Crc('crc-8-itu').new,
    HashType.CRC8_MAXIM: crcmod.predefined.Crc('crc-8-maxim').new,
    HashType.CRC8_ROHC: crcmod.predefined.Crc('crc-8-rohc').new,
    HashType.CRC8_WCDMA: crcmod.predefined.Crc('crc-8-wcdma').new,
    HashType.CRC16: crcmod.predefined.Crc('crc-16').new,
    HashType.CRC32: crcmod.predefined.Crc('crc-32').new,
    HashType.CRC64: crcmod.predefined.Crc('crc-64').new,
    HashType.MD5: hashlib.md5,
    HashType.SHA1: hashlib.sha1,
    HashType.SHA224: hashlib.sha224,
    HashType.SHA256: hashlib.sha256,
    HashType.SHA384: hashlib.sha384,
    HashType.SHA512: hashlib.sha512
}

CRCMOD_CUSTOM_MAPPING = {
    HashType.CRC8_CDMA2000: crcmod.mkCrcFun(0x19B, initCrc=0xFF, rev=False, xorOut=0x00),
    HashType.CRC8_DVB_S2: crcmod.mkCrcFun(0x1D5, initCrc=0x00, rev=False, xorOut=0x00),
    HashType.CRC8_EBU: crcmod.mkCrcFun(0x11D, initCrc=0xFF, rev=True, xorOut=0x00)
}


class HashIt(object):
    """The object to preform hashing"""

    def __init__(self, hash_type=None, hash_data=None):
        self.hash_type = hash_type
        self.data = hash_data

    def next_chunk(self):
        """Hash the next chunk of data"""
        return self._hash(self.data.next_chunk())

    def hash_it(self, hash_type=None, hash_data=None):
        """Hash all of the data"""
        if hash_type is not None:
            self.hash_type = hash_type

        if hash_data is not None:
            self.data = hash_data

        return self._hash(self.data.next_chunk())

    def _hash(self, data):
        """Internal hashing mapping"""
        hash_str = ""
        if self.hash_type in HASHLIB_MAPPING:
            hash_str = self._hashlib_hash(data)
        elif self.hash_type in CRCMOD_CUSTOM_MAPPING:
            hash_str = hex(CRCMOD_CUSTOM_MAPPING[self.hash_type](data))[2:].upper()
        else:
            raise NotImplementedError
        return hash_str

    def _hashlib_hash(self, data):
        """Internal hashing mapping specifically for hashlib like interfaces"""
        if six.PY3:
            try:
                data = data.encode('utf-8')
            except (UnicodeDecodeError, AttributeError):
                pass
        else:
            data = str(data)

        hasher = HASHLIB_MAPPING[self.hash_type]()
        hasher.update(data)
        return hasher.hexdigest().upper()
