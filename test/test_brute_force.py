"""Tests for the BruteForce object"""

from __future__ import absolute_import

import unittest

from hashit.core.hash_data import HashData
from hashit.service.brute_force import BruteForce
from hashit.utils.data_encap import DataEncap
from hashit.utils.data_type import DataType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use

EXAMPLE_PAYLOAD = bytearray([0x0F, 0x1E, 0x2D, 0x3C, 0x4B, 0x5A, 0x69, 0x78])


class TestBruteForce(unittest.TestCase):
    def setUp(self):
        self.data = HashData(
            DataEncap(DataType.BYTES, EXAMPLE_PAYLOAD)
        )

    def test_brute_force_crc16_no_solution(self):
        bf = BruteForce(self.data)
        assert not bf.run(result="0000")
        assert bf.solved_data is None

    def test_brute_force_crc16_exact_hash(self):
        bf = BruteForce(self.data)
        assert bf.run(result="BCF1")
        assert EXAMPLE_PAYLOAD == bf.solved_data

    def test_brute_force_crc16_one_byte_header(self):
        bf = BruteForce(self.data)
        assert bf.run(result="FCB1")
        assert EXAMPLE_PAYLOAD[1:] == bf.solved_data

    def test_brute_force_crc16_one_byte_footer(self):
        bf = BruteForce(self.data)
        assert bf.run(result="70D6")
        assert EXAMPLE_PAYLOAD[:-1] == bf.solved_data

    def test_brute_force_crc16_one_byte_header_footer(self):
        bf = BruteForce(self.data)
        assert bf.run(result="7029")
        assert EXAMPLE_PAYLOAD[1:-1] == bf.solved_data

    def test_brute_force_crc16_two_byte_header(self):
        bf = BruteForce(self.data)
        assert bf.run(result="FD4F")
        assert EXAMPLE_PAYLOAD[2:] == bf.solved_data

    def test_brute_force_crc16_two_byte_footer(self):
        bf = BruteForce(self.data)
        assert bf.run(result="56D7")
        assert EXAMPLE_PAYLOAD[:-2] == bf.solved_data

    def test_brute_force_crc16_two_byte_header_footer(self):
        bf = BruteForce(self.data)
        assert bf.run(result="AB7F")
        assert EXAMPLE_PAYLOAD[2:-2] == bf.solved_data
