"""Runs the CLI for hash-it"""

from __future__ import absolute_import, print_function

import sys

from hashit.cli.cli_status import CliStatus

from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType

from hashit.service.brute_force import BruteForce
from hashit.service.data_generation import DataGeneration
from hashit.service.validate_hash import ValidateHash


def arg_exists(args, key):
    return key in args and args[key]

def extract_args(args):
    """extracts args for the CLI"""
    hash_type = HashType.CRC16
    hash_data = None
    if arg_exists(args, '--hash-type'):
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
        return CliStatus.ARG_INVALID.value

    if args['-b']:
        brute_force = BruteForce(data=args['hd'])
        if brute_force.run(result=args['--verify'], hash_type=args['ht']):
            print('found hash %s after brute forcing\n'
                  'data = %s' % (args['<input>'], brute_force.solved_data)
                  )
            return CliStatus.SUCCESS.value
        return CliStatus.VALIDATION_ERROR.value

    validate = ValidateHash(
        result=args['--verify'],
        hash_type=args['ht'],
        data=args['hd']
    )
    if validate.is_vaild():
        return CliStatus.SUCCESS.value
    return CliStatus.VALIDATION_ERROR.value


def generate_data(args):
    """generate data for CLI"""
    if arg_exists(args, '--generate') and \
            len(args['--generate']) != args['ht'].hash_str_length():
        print(
            'generate hash invalid. Expected size %d was %d\n' %
            (args['ht'].hash_str_length(), len(args['--generate']))
        )
        return CliStatus.ARG_INVALID.value

    if arg_exists(args, '--generate'):
        dg = DataGeneration()
        found = dg.run(result=args['--generate'], hash_type=args['ht'])
        if found:
            for f_hash in found:
                print('data %s matches hash %s' % (f_hash.upper(), args['--generate']))
            return CliStatus.SUCCESS.value
    elif arg_exists(args, '--depth'):
        dg = DataGeneration(int(args['--depth']))
        found = dg.run(hash_type=args['ht'])
        if found:
            print('Generated %s byte(s) of data with hash %s : %r' % (
                args['--depth'],
                dg.hash_result,
                found[0]
            ))
            return CliStatus.SUCCESS.value

    return CliStatus.GENERATION_ERROR.value


def run_task(args=None):
    """Does the hashing related task for the CLI"""
    if '--verify' in args and args['--verify']:
        return verify_data(args)
    elif ('--generate' in args and args['--generate']) or '--depth' in args:
        return generate_data(args)
    elif args['hd'] is None:
        return CliStatus.SUCCESS.value

    hash_str = HashIt(hash_type=args['ht'], hash_data=args['hd']).hash_it()

    if args['<input>']:
        print('input: %s | hash: %s' % (args['<input>'], hash_str))
    else:
        print('input: stdin | hash: %s' % (hash_str))
    return CliStatus.SUCCESS.value


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

    return run_task(args)
