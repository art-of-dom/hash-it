"""
brute_force.py
Where there's a will, we'll force it.
"""
from __future__ import absolute_import

from hashit.core.hash_data import HashData
from hashit.core.hash_type import HashType
from hashit.service.validate_hash import ValidateHash
from hashit.utils.data_encap import DataEncap
from hashit.utils.data_type import DataType


class BruteForce(object):
    """The object to facilitating reverse engineering of hashes based on data"""

    def __init__(self, data=None):
        self.data_encap = data.data_encap
        self.org_data = data.next_chunk()
        self.solved_data = None
        self.data_type = self.data_encap.data_type
        if self.data_type == DataType.FILE:
            self.data_type = DataType.BYTES

    def run(self, result='', ht=HashType.CRC16):
        """runs the brute forcing of a hash"""

        for i in range(len(self.org_data)):
            for j in range(len(self.org_data) - i):
                tmpdata = self.org_data[i:] if j == 0 else self.org_data[i:-j]
                hash_data = HashData(DataEncap(self.data_type, tmpdata))

                if ValidateHash(result=result, hash_type=ht, data=hash_data).is_vaild():
                    self.solved_data = tmpdata
                    return True
        return False
