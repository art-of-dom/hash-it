'''Tests for the DataType Enum'''

import unittest
from hashit.utils.data_type import DataType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods


class TestDataType(unittest.TestCase):
    def test_data_type_ascii_in_data_type(self):
        assert 'ASCII' in DataType.__members__

    def test_data_type_ascii_lookup(self):
        assert DataType.ASCII == DataType['ASCII']

    def test_data_type_hex_in_data_type(self):
        assert 'HEX' in DataType.__members__

    def test_data_type_hex_lookup(self):
        assert DataType.HEX == DataType['HEX']

    def test_data_type_file_in_data_type(self):
        assert 'FILE' in DataType.__members__

    def test_data_type_file_lookup(self):
        assert DataType.FILE == DataType['FILE']

    def test_data_type_stdin_in_data_type(self):
        assert 'STDIN' in DataType.__members__

    def test_data_type_stdin_lookup(self):
        assert DataType.STDIN == DataType['STDIN']

    def test_data_type_bytes_in_data_type(self):
        assert 'BYTES' in DataType.__members__

    def test_data_type_bytes_lookup(self):
        assert DataType.BYTES == DataType['BYTES']
