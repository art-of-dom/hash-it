"""
data_generation.py
Make it or break it.
"""
from __future__ import absolute_import

from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType
from hashit.service.validate_hash import ValidateHash

from hashit.utils.data_encap import DataEncap
from hashit.utils.data_type import DataType

import os

MAX_FOUND_DATA = 5
MAX_DATA_LEN = 3

ALLOWED_HASH_TYPES_WITH_RESULTS = [
    HashType.CRC8,
    HashType.CRC8_DARC,
    HashType.CRC8_I_CODE,
    HashType.CRC8_ITU,
    HashType.CRC8_MAXIM,
    HashType.CRC8_ROHC,
    HashType.CRC8_WCDMA,
    HashType.CRC16
]


class DataGeneration(object):
    """The object to generate data and hashing it"""

    def __init__(self, depth=None):
        self.depth = depth
        self.hash_result = ''

    def run(self, result='', ht=HashType.CRC8):
        """runs the data generation"""
        found_data = []
        if result and ht in ALLOWED_HASH_TYPES_WITH_RESULTS:
            found_data = self._search_for_hash(result, ht)
        elif self.depth:
            hash_data = HashData(DataEncap(DataType.BYTES,
                                           bytearray(os.urandom(self.depth))
                                           ))
            self.hash_result = HashIt().hash_it(ht, hash_data)
            found_data.append(hash_data.data_encap.data)
        return found_data

    def _search_for_hash(self, result, ht):
        """searches for a hash by itterating over data"""
        found_data = []
        tmp_data = bytearray()
        while len(found_data) < MAX_FOUND_DATA and len(tmp_data) < MAX_DATA_LEN:
            tmp_data = self._get_next_data(tmp_data)
            hash_data = HashData(DataEncap(DataType.BYTES, tmp_data))
            if ValidateHash(result=result, hash_type=ht, data=hash_data).is_vaild():
                data = ''
                try:
                    data = str(tmp_data).encode('hex')
                except LookupError:
                    data = tmp_data.hex()

                found_data.append(data)
        return found_data

    def _get_next_data(self, data):
        """gives the next vaild byte array data"""
        if len(data) == 0:
            data.append(0)
            return data

        for i in range(1, len(data) + 1):
            if data[-i] != 255:
                data[-i] = data[-i] + 1
                return data
            data[-i] = 0

        data.append(0)
        return data
