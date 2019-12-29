'''
Tests for the cli interface
'''

from __future__ import absolute_import
import unittest
import sys
from nose.tools import assert_equals
from hashit.cli import cli_main

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=bad-continuation


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.args = {
            '--hash-type': None,
            '--verify': None,
            '-f': False,
            '-a': False,
            '-x': False,
            '<input>': None
        }

    def tearDown(self):
        pass

    def test_cil_retruns_error_if_no_args(self):
        assert_equals(1, cli_main(None))

    def test_cil_retruns_success_no_vaild_args(self):
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_success_known_hash_uppercase(self):
        self.args['--hash-type'] = 'CRC32'
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_success_known_hash_lowercase(self):
        self.args['--hash-type'] = 'crc32'
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_success_known_hash_mixedcase(self):
        self.args['--hash-type'] = 'cRc32'
        assert_equals(0, cli_main(self.args))

    def test_cil_retruns_error_unknown_hash(self):
        self.args['--hash-type'] = 'foobar'
        assert_equals(1, cli_main(self.args))
        self.assertEqual("Unknown hash type foobar",
            sys.stdout.getvalue().strip()
        )

    def test_cil_uses_default_hash_on_file(self):
        self.args['-f'] = True
        self.args['<input>'] = 'test/support/example.bin'
        assert_equals(0, cli_main(self.args))
        self.assertEqual("input: test/support/example.bin hash: BAD3",
            sys.stdout.getvalue().strip()
        )

    def test_cil_uses_default_hash_on_ascii(self):
        self.args['-a'] = True
        self.args['<input>'] = '123456789'
        assert_equals(0, cli_main(self.args))
        self.assertEqual("input: 123456789 hash: BB3D",
            sys.stdout.getvalue().strip()
        )

    def test_cil_uses_default_hash_on_hex(self):
        self.args['-x'] = True
        self.args['<input>'] = '010203040506070809'
        assert_equals(0, cli_main(self.args))
        self.assertEqual("input: 010203040506070809 hash: 4204",
            sys.stdout.getvalue().strip()
        )

    def test_cil_verify_good_result_returns_zero_file(self):
        self.args['-f'] = True
        self.args['<input>'] = 'test/support/example.bin'
        self.args['--verify'] = 'BAD3'
        assert_equals(0, cli_main(self.args))

    def test_cil_verify_bad_result_returns_error_file(self):
        self.args['-f'] = True
        self.args['<input>'] = 'test/support/example.bin'
        self.args['--verify'] = 'F00D'
        assert_equals(2, cli_main(self.args))

    def test_cil_verify_good_result_returns_zero_ascii(self):
        self.args['-a'] = True
        self.args['<input>'] = '123456789'
        self.args['--verify'] = 'BB3D'
        assert_equals(0, cli_main(self.args))

    def test_cil_verify_bad_result_returns_error_ascii(self):
        self.args['-a'] = True
        self.args['<input>'] = '123456789'
        self.args['--verify'] = 'F00D'
        assert_equals(2, cli_main(self.args))

    def test_cil_verify_good_result_returns_zero_hex(self):
        self.args['-x'] = True
        self.args['<input>'] = '010203040506070809'
        self.args['--verify'] = '4204'
        assert_equals(0, cli_main(self.args))

    def test_cil_verify_bad_result_returns_error_hex(self):
        self.args['-x'] = True
        self.args['<input>'] = '010203040506070809'
        self.args['--verify'] = 'F00D'
        assert_equals(2, cli_main(self.args))
