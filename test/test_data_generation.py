"""Tests for the DataGeneration object"""

from __future__ import absolute_import

import unittest
from nose.tools import assert_true, assert_equals, assert_false, assert_is_none
import six

from hashit.core.hash_data import HashData
from hashit.service.data_generation import DataGeneration

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use

EXAMPLE_PAYLOAD = bytearray([0x0F, 0x1E, 0x2D, 0x3C, 0x4B, 0x5A, 0x69, 0x78])


class TestDataGeneration(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_generation_with_result_crc8(self):
        dg = DataGeneration()
        found = dg.run(result="1C")
        assert_true(found)

    def test_data_generation_with_failed_result_crc8(self):
        dg = DataGeneration()
        found = dg.run(result="1C01")
        assert_false(found)