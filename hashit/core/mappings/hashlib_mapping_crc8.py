"""
hashlib_mapping_crc8.py
Mapping hash lib syle functions to hash types for CRC8.
"""
from __future__ import absolute_import

import crcmod

from hashit.core.hash_type import HashType


HASHLIB_MAPPING_CRC8 = {
    HashType.CRC8: crcmod.predefined.Crc('crc-8').new,
    HashType.CRC8_DARC: crcmod.predefined.Crc('crc-8-darc').new,
    HashType.CRC8_I_CODE: crcmod.predefined.Crc('crc-8-i-code').new,
    HashType.CRC8_ITU: crcmod.predefined.Crc('crc-8-itu').new,
    HashType.CRC8_MAXIM: crcmod.predefined.Crc('crc-8-maxim').new,
    HashType.CRC8_ROHC: crcmod.predefined.Crc('crc-8-rohc').new,
    HashType.CRC8_WCDMA: crcmod.predefined.Crc('crc-8-wcdma').new,
}
