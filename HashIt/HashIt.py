"""
"""


from PyCRC.CRC16 import CRC16
from PyCRC.CRC32 import CRC32
from HashType import  HashType
import hashlib

class HashIt(object):
    def __init__(self):
        self.filename = None
        self.size = 0

    def start_chunk(self, filename, size):
        self.filename = filename
        self.size = size

    def hash_it(self, hash_type, filename, start=None, size=None):
        if hash_type == HashType.CRC16:
            return "%04X"%(CRC16().calculate(open(filename, "rb").read()) & 0xFFFF)
        elif hash_type == HashType.CRC32:
            return "%08X"%(CRC32().calculate(open(filename, "rb").read()) & 0xFFFFFFFF)
        elif hash_type == HashType.MD5:
            hasher = hashlib.md5()
            hasher.update(open(filename, "rb").read())
            return hasher.hexdigest().upper()
        elif hash_type == HashType.SHA1:
            hasher = hashlib.sha1()
            hasher.update(open(filename, "rb").read())
            return hasher.hexdigest().upper()
        elif hash_type == HashType.SHA224:
            hasher = hashlib.sha224()
            hasher.update(open(filename, "rb").read())
            return hasher.hexdigest().upper()
        elif hash_type == HashType.SHA256:
            hasher = hashlib.sha256()
            hasher.update(open(filename, "rb").read())
            return hasher.hexdigest().upper()
