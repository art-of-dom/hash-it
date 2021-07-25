"""
hashlib_mapping.py
Mapping hash lib syle functions to hash types.
"""
from __future__ import absolute_import

import hashlib

import crcmod

from hashit.core.hash_type import HashType
from hashit.core.mappings.hashlib_mapping_crc8 import HASHLIB_MAPPING_CRC8
from hashit.core.mappings.hashlib_mapping_crc16 import HASHLIB_MAPPING_CRC16


HASHLIB_MAPPING = {
    HashType.CRC32: crcmod.predefined.Crc('crc-32').new,
    HashType.CRC64: crcmod.predefined.Crc('crc-64').new,
    HashType.MD5: hashlib.md5,
    HashType.SHA1: hashlib.sha1,
    HashType.SHA224: hashlib.sha224,
    HashType.SHA256: hashlib.sha256,
    HashType.SHA384: hashlib.sha384,
    HashType.SHA512: hashlib.sha512
}

HASHLIB_MAPPING.update(HASHLIB_MAPPING_CRC8)
HASHLIB_MAPPING.update(HASHLIB_MAPPING_CRC16)
