"""Runs the CLI for hash-it"""

from __future__ import absolute_import, print_function

import sys

from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType

from hashit.service.brute_force import BruteForce
from hashit.service.validate_hash import ValidateHash


def extract_args(args):
    """extracts args for the CLI"""
    hash_type = HashType.CRC16
    hash_data = None
    if args['--hash-type']:
        hash_type = HashType[args['--hash-type'].upper()]
    if args['-f']:
        hash_data = HashData(args['<input>'])
    elif args['-a']:
        hash_data = HashData(data=args['<input>'])
    elif args['-x']:
        data = str(bytearray.fromhex(args['<input>']).decode())
        hash_data = HashData(data=data)
    else:
        if not sys.stdin.isatty():
            try:
                infile = sys.stdin.buffer
                data = infile.read()
                hash_data = HashData(data=data)
            except AttributeError:
                data = ''
                for line in sys.stdin:
                    data += line
                hash_data = HashData(data=data)

    if args['-r']:
        hash_data.reverse()

    return hash_type, hash_data


def verify_data(args):
    """verify data for CLI"""
    if len(args['--verify']) != args['ht'].hash_str_length():
        print(
            'verify hash invalid. Expected size %d was %d\n' %
            (args['ht'].hash_str_length(), len(args['--verify']))
        )
        return 1

    if args['-b']:
        brute_force = BruteForce(data=args['hd'])
        if brute_force.run(result=args['--verify'], hash_type=args['ht']):
            print('found hash %s after brute forcing\n'
                'data = %s' % (args['<input>'], brute_force.solved_data)
            )
            return 0
        return 2

    validate = ValidateHash(
        result=args['--verify'],
        hash_type=args['ht'],
        data=args['hd']
    )
    if validate.is_vaild():
        return 0
    return 2


def run_task(args=None):
    """Does the hashing related task for the CLI"""
    if args['--verify']:
        return verify_data(args)

    hash_str = HashIt(hash_type=args['ht'], hash_data=args['hd']).hash_it()

    if args['<input>']:
        print('input: %s | hash: %s' % (args['<input>'], hash_str))
    else:
        print('input: stdin | hash: %s' % (hash_str))
    return 0


def cli_main(args=None):
    """CLI main point of entry"""
    try:
        hash_type, hash_data = extract_args(args)
        args['ht'] = hash_type
        args['hd'] = hash_data
    except KeyError:
        print("Unknown hash type %s" % args['--hash-type'])
        return 1
    except TypeError:
        return 1

    if args['hd'] is None:
        return 0

    return run_task(args)
