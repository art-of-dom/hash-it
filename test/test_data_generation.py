"""Tests for the DataGeneration object"""

from __future__ import absolute_import

import unittest
from nose.tools import assert_true, assert_false, assert_equal

from hashit.service.data_generation import DataGeneration
from hashit.core.hash_type import HashType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use

EXAMPLE_PAYLOAD = bytearray([0x0F, 0x1E, 0x2D, 0x3C, 0x4B, 0x5A, 0x69, 0x78])


class TestDataGeneration(unittest.TestCase):
    def test_data_generation_with_result_crc8(self):
        dg = DataGeneration()
        found = dg.run(result="1C")
        assert_true(found)

    def test_data_generation_with_failed_result_crc8(self):
        dg = DataGeneration()
        found = dg.run(result="1C01")
        assert_false(found)

    def test_data_generation_rejects_crc32(self):
        dg = DataGeneration()
        found = dg.run(result="83DCEFB7", hasht=HashType.CRC32)
        assert_false(found)

    def test_data_generation_with_depth(self):
        dg = DataGeneration(depth=5)
        found = dg.run(hasht=HashType.CRC32)
        assert_true(found)
        assert_equal(5, len(found[0]))
