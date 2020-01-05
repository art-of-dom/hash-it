'''
Tests for the HashData object
'''

from __future__ import absolute_import
import unittest
from nose.tools import (assert_equals, assert_is_none, assert_is_not_none)
from hashit.core.hash_data import HashData

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=bad-continuation


class TestHashData(unittest.TestCase):
    def setUp(self):
        self.bin_data = bytearray(list(range(0, 256)))

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
        assert_equals(bytearray(self.bin_data), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_file_handles_next_chunk_even_chunks(self):
        hd = HashData(filename="test/support/example.bin", chunk_size=128)
        assert_equals(bytearray(self.bin_data[:128]), bytearray(hd.next_chunk()))
        assert_equals(50.0, hd.percent_processed())
        assert_equals(bytearray(self.bin_data[128:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_file_handles_next_chunk_uneven_chunks(self):
        hd = HashData(filename="test/support/example.bin", chunk_size=100)
        assert_equals(bytearray(self.bin_data[:100]), bytearray(hd.next_chunk()))
        assert_equals(39.0625, hd.percent_processed())
        assert_equals(bytearray(self.bin_data[100:200]), bytearray(hd.next_chunk()))
        assert_equals(78.125, hd.percent_processed())
        assert_equals(bytearray(self.bin_data[200:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_file_can_be_reversed(self):
        reverse_data = bytearray(list(range(0, 256)))
        reverse_data.reverse()
        hd = HashData(filename="test/support/example.bin")
        hd.reverse()
        assert_equals(reverse_data, hd.next_chunk())

    def test_hash_data_arg_data_handles_percent_processed(self):
        hd = HashData(data=self.bin_data)
        assert_equals(0.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_next_chunk_all(self):
        hd = HashData(data=self.bin_data)
        assert_equals(bytearray(self.bin_data), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_next_chunk_even_chunks(self):
        hd = HashData(data=self.bin_data, chunk_size=128)
        assert_equals(bytearray(self.bin_data[:128]), bytearray(hd.next_chunk()))
        assert_equals(50.0, hd.percent_processed())
        assert_equals(bytearray(self.bin_data[128:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_arg_data_handles_next_chunk_uneven_chunks(self):
        hd = HashData(data=self.bin_data, chunk_size=100)
        assert_equals(bytearray(self.bin_data[:100]), bytearray(hd.next_chunk()))
        assert_equals(39.0625, hd.percent_processed())
        assert_equals(bytearray(self.bin_data[100:200]), bytearray(hd.next_chunk()))
        assert_equals(78.125, hd.percent_processed())
        assert_equals(bytearray(self.bin_data[200:]), bytearray(hd.next_chunk()))
        assert_equals(100.0, hd.percent_processed())

    def test_hash_data_arg_data_can_be_reversed(self):
        reverse_data = bytearray(list(range(0, 256)))
        reverse_data.reverse()
        hd = HashData(data=self.bin_data)
        hd.reverse()
        assert_equals(reverse_data, hd.next_chunk())
