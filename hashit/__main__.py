#!/usr/bin/env python
"""
Usage:
    hash-it [-brfax] <input> [--hash-type=HASH] [--verify=RESULT]

Options:
    -b                 brute force the verify
    -r                 reverse input
    -f                 input is a file
    -a                 input is ascii text
    -x                 input is hex string
    --hash-type=HASH   hash
    --verify=RESULT    verify given result
"""
from __future__ import absolute_import
import sys
from docopt import docopt


def main():
    try:
        from hashit.cli import cli_main
        sys.exit(cli_main(docopt(__doc__)))
    except KeyboardInterrupt:
        sys.exit(130)

if __name__ == '__main__':
    main()
