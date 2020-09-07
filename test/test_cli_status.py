'''Tests for the CliStatus Enum'''

from __future__ import absolute_import
import unittest
from nose.tools import assert_equals, assert_true
from hashit.cli.cli_status import CliStatus

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods


class TestCliStatus(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cli_status_success_in_cli_status(self):
        assert_true('SUCCESS' in CliStatus.__members__)

    def test_cli_status_success_lookup(self):
        assert_equals(CliStatus.SUCCESS, CliStatus['SUCCESS'])

    def test_cli_status_arg_invalid_in_cli_status(self):
        assert_true('ARG_INVALID' in CliStatus.__members__)

    def test_cli_status_arg_invalid_lookup(self):
        assert_equals(CliStatus.ARG_INVALID, CliStatus['ARG_INVALID'])

    def test_cli_status_validation_error_in_cli_status(self):
        assert_true('VALIDATION_ERROR' in CliStatus.__members__)

    def test_cli_status_validation_error_lookup(self):
        assert_equals(CliStatus.VALIDATION_ERROR,
                      CliStatus['VALIDATION_ERROR'])

    def test_cli_status_generation_error_in_cli_status(self):
        assert_true('GENERATION_ERROR' in CliStatus.__members__)

    def test_cli_status_generation_error_lookup(self):
        assert_equals(CliStatus.GENERATION_ERROR,
                      CliStatus['GENERATION_ERROR'])
