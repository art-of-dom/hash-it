"""
validate_hash.py
The heavy hitter of hashing.
"""
from __future__ import absolute_import

from hashit.core.hash_type import HashType
from hashit.core.hash_it import HashIt


class ValidateHash(object):
    """The object to validate hashing"""

    def __init__(self, data=None, result='', hash_type=HashType.CRC16):
        self.data = data
        self.expected_result = result
        self.hash_type = hash_type
        self.resulting_hash = None

    def is_vaild(self):
        """
        checks if the given result is valid
        """
        self.resulting_hash = HashIt().hash_it(
            self.hash_type,
            self.data
        )
        return self.expected_result.upper() == self.resulting_hash
