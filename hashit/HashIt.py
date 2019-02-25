'''
HashIt.py
The heavy hitter of hashing.
'''
from __future__ import absolute_import
import hashlib
import os
from PyCRC.CRC16 import CRC16
from PyCRC.CRC32 import CRC32
from hashit.HashType import HashType

class HashIt(object):
    def __init__(self, data=None, hash_type=None, filename=None, chunk_size=0):
        self.filename = filename
        self.chunk_size = chunk_size
        self.hash_type = hash_type
        self.pos = 0
        self.data = data
        if filename != None:
            self.size = os.path.getsize(filename)
        else:
            self.size = 0

    def next_chunk(self):
        data = None
        if self.pos == self.size:
            return None

        with open(self.filename, 'rb') as fin:
            fin.seek(self.pos)
            data = fin.read(self.chunk_size)
        self.pos = self.pos + self.chunk_size
        return self._hash(data)

    def hash_it(self, hash_type=None, filename=None):
        data = self.data
        if hash_type != None:
            self.hash_type = hash_type

        if filename != None:
            self.filename = filename

        if self.filename != None:
            data = open(self.filename, "rb").read()
        return self._hash(data)


    def _hash(self, data):
        hash_str = ""
        if self.hash_type == HashType.CRC16:
            hash_str = "%04X"%(CRC16().calculate(data) & 0xFFFF)
        elif self.hash_type == HashType.CRC32:
            hash_str = "%08X"%(CRC32().calculate(data) & 0xFFFFFFFF)
        elif self.hash_type == HashType.MD5:
            hasher = hashlib.md5()
            hasher.update(data)
            hash_str = hasher.hexdigest().upper()
        elif self.hash_type == HashType.SHA1:
            hasher = hashlib.sha1()
            hasher.update(data)
            hash_str = hasher.hexdigest().upper()
        elif self.hash_type == HashType.SHA224:
            hasher = hashlib.sha224()
            hasher.update(data)
            hash_str = hasher.hexdigest().upper()
        elif self.hash_type == HashType.SHA256:
            hasher = hashlib.sha256()
            hasher.update(data)
            hash_str = hasher.hexdigest().upper()
        return hash_str
