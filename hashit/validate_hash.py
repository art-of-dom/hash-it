'''
validate_hash.py
The heavy hitter of hashing.
'''
from __future__ import absolute_import
from hashit.hash_type import HashType
from hashit.hash_it import HashIt

class ValidateHash(object):
    '''
    The object to validate hashing
    '''
    def __init__(self, result='', data=None, hash_type=HashType.CRC16, filename=None):
        self.filename = filename
        self.hash_type = hash_type
        self.data = data
        self.expected_result = result

    def is_vaild(self):
        return self.expected_result.upper() == HashIt().hash_it(
            self.hash_type,
            self.filename
        )
