"""
hashlib_mapping.py
Mapping hash lib syle functions to hash types.
"""
from __future__ import absolute_import

import crcmod
import hashlib

from hashit.core.hash_type import HashType


HASHLIB_MAPPING = {
    HashType.CRC8: crcmod.predefined.Crc('crc-8').new,
    HashType.CRC8_DARC: crcmod.predefined.Crc('crc-8-darc').new,
    HashType.CRC8_I_CODE: crcmod.predefined.Crc('crc-8-i-code').new,
    HashType.CRC8_ITU: crcmod.predefined.Crc('crc-8-itu').new,
    HashType.CRC8_MAXIM: crcmod.predefined.Crc('crc-8-maxim').new,
    HashType.CRC8_ROHC: crcmod.predefined.Crc('crc-8-rohc').new,
    HashType.CRC8_WCDMA: crcmod.predefined.Crc('crc-8-wcdma').new,
    HashType.CRC16: crcmod.predefined.Crc('crc-16').new,
    HashType.CRC32: crcmod.predefined.Crc('crc-32').new,
    HashType.CRC64: crcmod.predefined.Crc('crc-64').new,
    HashType.MD5: hashlib.md5,
    HashType.SHA1: hashlib.sha1,
    HashType.SHA224: hashlib.sha224,
    HashType.SHA256: hashlib.sha256,
    HashType.SHA384: hashlib.sha384,
    HashType.SHA512: hashlib.sha512
}
