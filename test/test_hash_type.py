'''Tests for the HashType Enum'''

from __future__ import absolute_import
import unittest
from nose.tools import assert_equals, assert_true
from hashit.core.hash_type import HashType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods

class TestHashType(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # CRC 8
    def test_hash_type_crc8_in_hash_type(self):
        assert_true('CRC8' in HashType.__members__)

    def test_hash_type_crc8_lookup(self):
        assert_equals(HashType.CRC8, HashType['CRC8'])

    def test_hash_type_crc8_darc_in_hash_type(self):
        assert_true('CRC8_DARC' in HashType.__members__)

    def test_hash_type_crc8_darc_lookup(self):
        assert_equals(HashType.CRC8_DARC, HashType['CRC8_DARC'])

    def test_hash_type_crc8_i_code_in_hash_type(self):
        assert_true('CRC8_I_CODE' in HashType.__members__)

    def test_hash_type_crc8_i_code_lookup(self):
        assert_equals(HashType.CRC8_I_CODE, HashType['CRC8_I_CODE'])

    def test_hash_type_crc8_itu_in_hash_type(self):
        assert_true('CRC8_ITU' in HashType.__members__)

    def test_hash_type_crc8_itu_lookup(self):
        assert_equals(HashType.CRC8_ITU, HashType['CRC8_ITU'])

    def test_hash_type_crc8_maxim_in_hash_type(self):
        assert_true('CRC8_MAXIM' in HashType.__members__)

    def test_hash_type_crc8_maxim_lookup(self):
        assert_equals(HashType.CRC8_MAXIM, HashType['CRC8_MAXIM'])

    def test_hash_type_crc8_rohc_in_hash_type(self):
        assert_true('CRC8_ROHC' in HashType.__members__)

    def test_hash_type_crc8_rohc_lookup(self):
        assert_equals(HashType.CRC8_ROHC, HashType['CRC8_ROHC'])

    def test_hash_type_crc8_wcdma_in_hash_type(self):
        assert_true('CRC8_WCDMA' in HashType.__members__)

    def test_hash_type_crc8_wcdma_lookup(self):
        assert_equals(HashType.CRC8_WCDMA, HashType['CRC8_WCDMA'])

    # Others
    def test_hash_type_crc16_in_hash_type(self):
        assert_true('CRC16' in HashType.__members__)

    def test_hash_type_crc16_lookup(self):
        assert_equals(HashType.CRC16, HashType['CRC16'])

    def test_hash_type_crc32_in_hash_type(self):
        assert_true('CRC32' in HashType.__members__)

    def test_hash_type_crc32_lookup(self):
        assert_equals(HashType.CRC32, HashType['CRC32'])

    def test_hash_type_crc64_in_hash_type(self):
        assert_true('CRC64' in HashType.__members__)

    def test_hash_type_crc64_lookup(self):
        assert_equals(HashType.CRC64, HashType['CRC64'])

    def test_hash_type_md2_in_hash_type(self):
        assert_true('MD2' in HashType.__members__)

    def test_hash_type_md2_lookup(self):
        assert_equals(HashType.MD2, HashType['MD2'])

    def test_hash_type_md4_in_hash_type(self):
        assert_true('MD4' in HashType.__members__)

    def test_hash_type_md4_lookup(self):
        assert_equals(HashType.MD4, HashType['MD4'])

    def test_hash_type_md5_in_hash_type(self):
        assert_true('MD5' in HashType.__members__)

    def test_hash_type_md5_lookup(self):
        assert_equals(HashType.MD5, HashType['MD5'])

    def test_hash_type_sha1_in_hash_type(self):
        assert_true('SHA1' in HashType.__members__)

    def test_hash_type_sha1_lookup(self):
        assert_equals(HashType.SHA1, HashType['SHA1'])

    def test_hash_type_sha224_in_hash_type(self):
        assert_true('SHA224' in HashType.__members__)

    def test_hash_type_sha224_lookup(self):
        assert_equals(HashType.SHA224, HashType['SHA224'])

    def test_hash_type_sha256_in_hash_type(self):
        assert_true('SHA256' in HashType.__members__)

    def test_hash_type_sha256_lookup(self):
        assert_equals(HashType.SHA256, HashType['SHA256'])

    def test_hash_type_sha384_in_hash_type(self):
        assert_true('SHA384' in HashType.__members__)

    def test_hash_type_sha384_lookup(self):
        assert_equals(HashType.SHA384, HashType['SHA384'])

    def test_hash_type_sha512_in_hash_type(self):
        assert_true('SHA512' in HashType.__members__)

    def test_hash_type_sha512_lookup(self):
        assert_equals(HashType.SHA512, HashType['SHA512'])
