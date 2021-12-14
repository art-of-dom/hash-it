"""
hashlib_mapping_crc24.py
Mapping hash lib syle functions to hash types crc24.
"""
from __future__ import absolute_import

import crcmod

from hashit.core.hash_type import HashType

HASHLIB_MAPPING_CRC24 = {
    HashType.CRC24: crcmod.predefined.Crc('crc-24').new,
    HashType.CRC24_FLEXRAY_A: crcmod.predefined.Crc('crc-24-flexray-a').new,
    HashType.CRC24_FLEXRAY_B: crcmod.predefined.Crc('crc-24-flexray-b').new,
}
