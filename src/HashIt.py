'''
HashIt.py
The heavy hitter of hashing.
'''


import hashlib
import os
from PyCRC.CRC16 import CRC16
from PyCRC.CRC32 import CRC32
from HashType import  HashType

class HashIt(object):
    def __init__(self, hash_type=None, filename=None, size=0):
        self.filename = filename
        self.chunk_size = size
        self.hash_type = hash_type
        self.pos = 0
        if filename != None:
            self.size = os.path.getsize(filename)
        else:
            self.size = 0

    def next_chunk(self):
        data = None
        if self.pos == self.size:
            return None

        with open(self.filename) as fin:
            fin.seek(self.pos)
            data = fin.read(self.chunk_size)
        self.pos = self.pos + self.chunk_size
        return self._hash(data)

    def hash_it(self, hash_type=None, filename=None):
        if hash_type != None:
            self.hash_type = hash_type

        if filename != None:
            self.filename = filename

        return self._hash(open(self.filename, "rb").read())


    def _hash(self, data):
        if self.hash_type == HashType.CRC16:
            return "%04X"%(CRC16().calculate(data) & 0xFFFF)
        elif self.hash_type == HashType.CRC32:
            return "%08X"%(CRC32().calculate(data) & 0xFFFFFFFF)
        elif self.hash_type == HashType.MD5:
            hasher = hashlib.md5()
            hasher.update(data)
            return hasher.hexdigest().upper()
        elif self.hash_type == HashType.SHA1:
            hasher = hashlib.sha1()
            hasher.update(data)
            return hasher.hexdigest().upper()
        elif self.hash_type == HashType.SHA224:
            hasher = hashlib.sha224()
            hasher.update(data)
            return hasher.hexdigest().upper()
        elif self.hash_type == HashType.SHA256:
            hasher = hashlib.sha256()
            hasher.update(data)
            return hasher.hexdigest().upper()
