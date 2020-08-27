"""
brute_force.py
Where there's a will, we'll force it.
"""
from __future__ import absolute_import

from hashit.core.hash_data import HashData
from hashit.core.hash_type import HashType
from hashit.service.validate_hash import ValidateHash


class BruteForce(object):
    """
    The object to facilitating reverse engineering of hashes based on data
    """

    def __init__(self, data=None):
        self.org_data = data.next_chunk()
        self.solved_data = None

    def run(self, result='', hash_type=HashType.CRC16):
        """
        runs the brute forcing of a hash
        """
        for i in range(len(self.org_data)):
            for j in range(0, len(self.org_data) - i):
                if j == 0:
                    tmpdata = self.org_data[i:]
                else:
                    tmpdata = self.org_data[i:-j]

                hash_data = HashData(data=tmpdata)

                validate = ValidateHash(
                    result=result,
                    hash_type=hash_type,
                    data=hash_data
                )

                if validate.is_vaild():
                    self.solved_data = tmpdata
                    return True
        return False
