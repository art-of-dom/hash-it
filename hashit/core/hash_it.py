'''
hash_type.py
The heavy hitter of hashing.
'''
from __future__ import absolute_import
import hashlib
import os
from PyCRC.CRC16 import CRC16
from PyCRC.CRC32 import CRC32
from hashit.core.hash_type import HashType

HASHLIB_MAPPING = {
    HashType.MD5: hashlib.md5,
    HashType.SHA1: hashlib.sha1,
    HashType.SHA224: hashlib.sha224,
    HashType.SHA256: hashlib.sha256
}


class HashIt(object):
    '''
    The object to preform hashing
    '''
    def __init__(self, hash_type=None, hash_data=None):
        self.hash_type = hash_type
        self.data = hash_data

    def next_chunk(self):
        '''
        Hash the next chunk of data
        '''
        return self._hash(self.data.next_chunk())

    def hash_it(self, hash_type=None, hash_data=None):
        '''
        Hash all of the data
        '''
        if hash_type != None:
            self.hash_type = hash_type

        if hash_data != None:
            self.data = hash_data

        return self._hash(self.data.next_chunk())


    def _hash(self, data):
        hash_str = ""
        if self.hash_type == HashType.CRC16:
            hash_str = "%04X"%(CRC16().calculate(data) & 0xFFFF)
        elif self.hash_type == HashType.CRC32:
            hash_str = "%08X"%(CRC32().calculate(data) & 0xFFFFFFFF)
        elif self.hash_type in HASHLIB_MAPPING:
            hasher = HASHLIB_MAPPING[self.hash_type]()
            hasher.update(data)
            hash_str = hasher.hexdigest().upper()
        else:
            raise NotImplementedError
        return hash_str
