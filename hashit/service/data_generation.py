"""
data_generation.py
Make it or break it.
"""
from __future__ import absolute_import

import codecs

from hashit.core.hash_data import HashData
from hashit.core.hash_type import HashType
from hashit.service.validate_hash import ValidateHash

MAX_FOUND_DATA = 5
MAX_DATA_LEN = 3


class DataGeneration(object):
    """
    The object to generate data and hashing it
    """
    def __init__(self, depth=None):
        self.depth = depth

    def run(self, result='', hash_type=HashType.CRC8):
        """
        runs the data generation
        """
        found_data = []
        if result:
            tmp_data = bytearray()
            while len(found_data) < MAX_FOUND_DATA and len(tmp_data) < MAX_DATA_LEN:
                tmp_data = self._get_next_data(tmp_data)
                hash_data = HashData(data=tmp_data)
                validate = ValidateHash(
                    result=result,
                    hash_type=hash_type,
                    data=hash_data
                )
                if validate.is_vaild():
                    data = ''
                    try:
                        data = str(tmp_data).encode('hex')
                    except LookupError:
                        data = tmp_data.hex()

                    found_data.append(data)
        return found_data

    def _get_next_data(self, data):
        """
        gives the next vaild byte array data
        """
        if len(data) is 0:
            data.append(0)
            return data

        for i in range(1, len(data) + 1):
            if data[-i] != 255:
                data[-i] = data[-i] + 1
                return data
            data[-i] = 0

        data.append(0)
        return data