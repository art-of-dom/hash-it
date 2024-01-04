'''Tests for the CliStatus Enum'''

import unittest
from hashit.cli.cli_status import CliStatus

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods


class TestCliStatus(unittest.TestCase):
    def test_cli_status_success_in_cli_status(self):
        assert 'SUCCESS' in CliStatus.__members__

    def test_cli_status_success_lookup(self):
        assert CliStatus.SUCCESS == CliStatus['SUCCESS']

    def test_cli_status_arg_invalid_in_cli_status(self):
        assert 'ARG_INVALID' in CliStatus.__members__

    def test_cli_status_arg_invalid_lookup(self):
        assert CliStatus.ARG_INVALID == CliStatus['ARG_INVALID']

    def test_cli_status_validation_error_in_cli_status(self):
        assert 'VALIDATION_ERROR' in CliStatus.__members__

    def test_cli_status_validation_error_lookup(self):
        assert (CliStatus.VALIDATION_ERROR ==
                      CliStatus['VALIDATION_ERROR'])

    def test_cli_status_generation_error_in_cli_status(self):
        assert 'GENERATION_ERROR' in CliStatus.__members__

    def test_cli_status_generation_error_lookup(self):
        assert (CliStatus.GENERATION_ERROR ==
                      CliStatus['GENERATION_ERROR'])
