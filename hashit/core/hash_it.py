"""
hash_type.py
The heavy hitter of hashing.
"""
from __future__ import absolute_import

import hashlib

import crcmod

from hashit.core.hash_type import HashType

HASHLIB_MAPPING = {
    HashType.CRC8: crcmod.predefined.Crc('crc-8').new,
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


class HashIt(object):
    """
    The object to preform hashing
    """
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
        else:
            raise NotImplementedError
        return hash_str


    def _hashlib_hash(self, data):
        """
        Internal hashing mapping specifically for hashlib like interfaces
        """
        try:
            data = data.encode('utf-8')
        except (UnicodeDecodeError, AttributeError):
            pass

        hasher = HASHLIB_MAPPING[self.hash_type]()
        hasher.update(data)
        return hasher.hexdigest().upper()
