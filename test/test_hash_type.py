'''
Tests for the HashType Enum
'''

from __future__ import absolute_import
from nose.tools import assert_equals, assert_true
from hashit.hash_type import HashType


def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_hash_type_crc16_in_hash_type():
    assert_true('CRC16' in HashType.__members__)

def test_hash_type_crc16_lookup():
    assert_equals(HashType.CRC16, HashType['CRC16'])

def test_hash_type_crc32_in_hash_type():
    assert_true('CRC32' in HashType.__members__)

def test_hash_type_crc32_lookup():
    assert_equals(HashType.CRC32, HashType['CRC32'])

def test_hash_type_md2_in_hash_type():
    assert_true('MD2' in HashType.__members__)

def test_hash_type_md2_lookup():
    assert_equals(HashType.MD2, HashType['MD2'])

def test_hash_type_md4_in_hash_type():
    assert_true('MD4' in HashType.__members__)

def test_hash_type_md4_lookup():
    assert_equals(HashType.MD4, HashType['MD4'])

def test_hash_type_md5_in_hash_type():
    assert_true('MD5' in HashType.__members__)

def test_hash_type_md5_lookup():
    assert_equals(HashType.MD5, HashType['MD5'])

def test_hash_type_sha1_in_hash_type():
    assert_true('SHA1' in HashType.__members__)

def test_hash_type_sha1_lookup():
    assert_equals(HashType.SHA1, HashType['SHA1'])

def test_hash_type_sha224_in_hash_type():
    assert_true('SHA224' in HashType.__members__)

def test_hash_type_sha224_lookup():
    assert_equals(HashType.SHA224, HashType['SHA224'])

def test_hash_type_sha256_in_hash_type():
    assert_true('SHA256' in HashType.__members__)

def test_hash_type_sha256_lookup():
    assert_equals(HashType.SHA256, HashType['SHA256'])

def test_hash_type_sha384_in_hash_type():
    assert_true('SHA384' in HashType.__members__)

def test_hash_type_sha384_lookup():
    assert_equals(HashType.SHA384, HashType['SHA384'])

def test_hash_type_sha512_in_hash_type():
    assert_true('SHA512' in HashType.__members__)

def test_hash_type_sha512_lookup():
    assert_equals(HashType.SHA512, HashType['SHA512'])
