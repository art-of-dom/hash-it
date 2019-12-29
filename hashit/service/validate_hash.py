'''
validate_hash.py
The heavy hitter of hashing.
'''
from __future__ import absolute_import
from hashit.core.hash_type import HashType
from hashit.core.hash_it import HashIt

class ValidateHash(object):
    '''
    The object to validate hashing
    '''
    def __init__(self, data=None, result='', hash_type=HashType.CRC16):
        self.data = data
        self.expected_result = result
        self.hash_type = hash_type

    def is_vaild(self):
        return self.expected_result.upper() == HashIt().hash_it(
            self.hash_type,
            self.data
        )
