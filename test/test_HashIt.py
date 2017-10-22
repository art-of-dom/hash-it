'''
'''

from nose.tools import assert_equals, raises, assert_true
from HashIt.HashIt import HashIt
from HashIt.HashType import  HashType


def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_hash_it_crc16():
    assert_equals("BAD3", HashIt().hash_it(HashType.CRC16, "test/support/example.bin"))

def test_hash_it_crc32():
    assert_equals("29058C73", HashIt().hash_it(HashType.CRC32, "test/support/example.bin"))

def test_hash_it_md5():
    assert_equals("E2C865DB4162BED963BFAA9EF6AC18F0",
                  HashIt().hash_it(HashType.MD5, "test/support/example.bin"))

def test_hash_it_sha1():
    assert_equals("4916D6BDB7F78E6803698CAB32D1586EA457DFC8",
                  HashIt().hash_it(HashType.SHA1, "test/support/example.bin"))

def test_hash_it_sha224():
    assert_equals("88702E63237824C4EB0D0FCFE41469A462493E8BEB2A75BBE5981734",
                  HashIt().hash_it(HashType.SHA224, "test/support/example.bin"))

def test_hash_it_sha256():
    assert_equals("40AFF2E9D2D8922E47AFD4648E6967497158785FBD1DA870E7110266BF944880",
                  HashIt().hash_it(HashType.SHA256, "test/support/example.bin"))
