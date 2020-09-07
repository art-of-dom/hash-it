'''Tests for the DataType Enum'''

from __future__ import absolute_import
import unittest
from nose.tools import assert_equals, assert_true
from hashit.utils.data_type import DataType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods


class TestDataType(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_type_ascii_in_data_type(self):
        assert_true('ASCII' in DataType.__members__)

    def test_data_type_ascii_lookup(self):
        assert_equals(DataType.ASCII, DataType['ASCII'])

    def test_data_type_hex_in_data_type(self):
        assert_true('HEX' in DataType.__members__)

    def test_data_type_hex_lookup(self):
        assert_equals(DataType.HEX, DataType['HEX'])

    def test_data_type_file_in_data_type(self):
        assert_true('FILE' in DataType.__members__)

    def test_data_type_file_lookup(self):
        assert_equals(DataType.FILE, DataType['FILE'])

    def test_data_type_stdin_in_data_type(self):
        assert_true('STDIN' in DataType.__members__)

    def test_data_type_stdin_lookup(self):
        assert_equals(DataType.STDIN, DataType['STDIN'])

    def test_data_type_bytes_in_data_type(self):
        assert_true('BYTES' in DataType.__members__)

    def test_data_type_bytes_lookup(self):
        assert_equals(DataType.BYTES, DataType['BYTES'])
