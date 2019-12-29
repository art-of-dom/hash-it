'''
Tests for the HashData object
'''

from __future__ import absolute_import
import unittest
from nose.tools import (assert_equals, assert_is_none, assert_is_not_none, raises)
from hashit.core.hash_data import HashData

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=bad-continuation

EXAMPLE_BIN_DATA = bytearray(list(range(0, 256)))


class TestHashIt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hash_data_no_args(self):
        hd = HashData()
        assert_is_not_none(hd)

    def test_hash_data_no_args_handles_percent_processed(self):
        hd = HashData()
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_no_args_handles_next_chunk(self):
        hd = HashData()
        assert_is_none(hd.next_chunk())

    def test_hash_data_file_handles_percent_processed(self):
        hd = HashData(filename="test/support/example.bin")
        assert_equals(0.0, hd.percent_processed())

    def test_hash_data_file_handles_next_chunk_all(self):
        hd = HashData(filename="test/support/example.bin")
        assert_equals(bytearray(EXAMPLE_BIN_DATA), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_file_handles_next_chunk_even_chunks(self):
        hd = HashData(filename="test/support/example.bin", chunk_size=128)
        assert_equals(bytearray(EXAMPLE_BIN_DATA[:128]), bytearray(hd.next_chunk()))
        assert_equals(50.0, hd.percent_processed())
        assert_equals(bytearray(EXAMPLE_BIN_DATA[128:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_file_handles_next_chunk_uneven_chunks(self):
        hd = HashData(filename="test/support/example.bin", chunk_size=100)
        assert_equals(bytearray(EXAMPLE_BIN_DATA[:100]), bytearray(hd.next_chunk()))
        assert_equals(39.0625, hd.percent_processed())
        assert_equals(bytearray(EXAMPLE_BIN_DATA[100:200]), bytearray(hd.next_chunk()))
        assert_equals(78.125, hd.percent_processed())
        assert_equals(bytearray(EXAMPLE_BIN_DATA[200:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_percent_processed(self):
        hd = HashData(data=EXAMPLE_BIN_DATA)
        assert_equals(0.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_next_chunk_all(self):
        hd = HashData(data=EXAMPLE_BIN_DATA)
        assert_equals(bytearray(EXAMPLE_BIN_DATA), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_next_chunk_even_chunks(self):
        hd = HashData(data=EXAMPLE_BIN_DATA, chunk_size=128)
        assert_equals(bytearray(EXAMPLE_BIN_DATA[:128]), bytearray(hd.next_chunk()))
        assert_equals(50.0, hd.percent_processed())
        assert_equals(bytearray(EXAMPLE_BIN_DATA[128:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_next_chunk_uneven_chunks(self):
        hd = HashData(data=EXAMPLE_BIN_DATA, chunk_size=100)
        assert_equals(bytearray(EXAMPLE_BIN_DATA[:100]), bytearray(hd.next_chunk()))
        assert_equals(39.0625, hd.percent_processed())
        assert_equals(bytearray(EXAMPLE_BIN_DATA[100:200]), bytearray(hd.next_chunk()))
        assert_equals(78.125, hd.percent_processed())
        assert_equals(bytearray(EXAMPLE_BIN_DATA[200:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())
