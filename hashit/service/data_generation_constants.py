"""
data_generation_constants.py
Constants to make it or break it.
"""
from __future__ import absolute_import

from hashit.core.hash_type import HashType

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
