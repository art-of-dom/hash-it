'''
Tests for the ValidateHash object
'''

from __future__ import absolute_import
import unittest
from nose.tools import assert_true, assert_false
from hashit.validate_hash import ValidateHash
from hashit.hash_type import HashType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use


class TestHashIt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_verify_hash_crc16_expected_result(self):
        assert_true(ValidateHash(
            result="BAD3",
            hash_type=HashType.CRC16,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_crc16_bad_result(self):
        assert_false(ValidateHash(
            result="78E7",
            hash_type=HashType.CRC16,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_crc32_expected_result(self):
        assert_true(ValidateHash(
            result="29058C73",
            hash_type=HashType.CRC32,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_crc32_bad_result(self):
        assert_false(ValidateHash(
            result="ACEF2345",
            hash_type=HashType.CRC32,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_md5_expected_result(self):
        assert_true(ValidateHash(
            result="E2C865DB4162BED963BFAA9EF6AC18F0",
            hash_type=HashType.MD5,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_md5_bad_result(self):
        assert_false(ValidateHash(
            result="11223344556677889900AECF431304065",
            hash_type=HashType.MD5,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_sha1_expected_result(self):
        assert_true(ValidateHash(
            result="4916D6BDB7F78E6803698CAB32D1586EA457DFC8",
            hash_type=HashType.SHA1,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_sha1_bad_result(self):
        assert_false(ValidateHash(
            result="987654321AC12345876543BCC34567862737FF20",
            hash_type=HashType.SHA1,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_sha224_expected_result(self):
        assert_true(ValidateHash(
            result="88702E63237824C4EB0D0FCFE41469A462493E8BEB2A75BBE5981734",
            hash_type=HashType.SHA224,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_sha224_bad_result(self):
        assert_false(ValidateHash(
            result="AACCEEDDFF928173647D0FBC09375847268EB88EEFF378592047583",
            hash_type=HashType.SHA224,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_sha256_expected_result(self):
        assert_true(ValidateHash(
            result="40AFF2E9D2D8922E47AFD4648E6967497158785FBD1DA870E7110266BF944880",
            hash_type=HashType.SHA256,
            filename="test/support/example.bin"
        ).is_vaild())

    def test_verify_hash_sha256_bad_result(self):
        assert_false(ValidateHash(
            result="AF82E982D8922E47AFD4648E674ACE587BEEF85FBD1D0266BF944880123455FF",
            hash_type=HashType.SHA256,
            filename="test/support/example.bin"
        ).is_vaild())
