#!/usr/bin/env python
"""
Usage:
    hash-it [-f] <input> [--hash-type=HASH]

Options:
    -f                 input is a file
    --hash-type=HASH   hash
"""
import sys
from docopt import docopt

def main():
    try:
        from cli import cli_main
        sys.exit(cli_main(docopt(__doc__)))
    except KeyboardInterrupt:
        sys.exit(130)

if __name__ == '__main__':
    main()
