"""Runs the CLI for hash-it"""

from __future__ import absolute_import, print_function

from hashit.cli.cli_status import CliStatus

from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType

from hashit.service.brute_force import BruteForce
from hashit.service.data_generation import DataGeneration
from hashit.service.validate_hash import ValidateHash

from hashit.utils.data_encap import DataEncap
from hashit.utils.data_type import DataType


def arg_exists(args, key):
    '''Checks if arg exists'''
    return key in args and args[key]

def hash_len_valid(hash_str, ht):
    '''Makes sure hash length is valid for given hash type'''
    if len(hash_str) != ht.hash_str_length():
        print('hash invalid. Expected size %d was %d\n' %
            (ht.hash_str_length(), len(hash_str))
        )
        return False
    return True

def extract_args(args):
    """extracts args for the CLI"""
    hash_type = HashType.CRC16
    hash_data = None
    data_type = None

    if arg_exists(args, '--hash-type'):
        hash_type = HashType[args['--hash-type'].upper()]

    if args['-f']:
        data_type = DataType.FILE
    elif args['-a']:
        data_type = DataType.ASCII
    elif args['-x']:
        data_type = DataType.HEX
    else:
        data_type = DataType.STDIN

    hash_data = HashData(DataEncap(data_type, args['<input>']))

    if hash_data.data_encap.size == 0:
        hash_data = None

    if args['-r']:
        hash_data.reverse()

    return hash_type, hash_data


def verify_data(args):
    """verify data for CLI"""
    if hash_len_valid(args['--verify'], args['ht']) is False:
        return CliStatus.ARG_INVALID.value

    if args['-b']:
        brute_force = BruteForce(data=args['hd'])
        if brute_force.run(result=args['--verify'], ht=args['ht']):
            print('found hash %s after brute forcing\n'
                  'data = %s' % (args['<input>'], brute_force.solved_data)
                  )
            return CliStatus.SUCCESS.value
        return CliStatus.VALIDATION_ERROR.value

    validate = ValidateHash(result=args['--verify'], hash_type=args['ht'],
        data=args['hd']
    )
    if validate.is_vaild():
        return CliStatus.SUCCESS.value
    return CliStatus.VALIDATION_ERROR.value


def generate_data(args):
    """generate data for CLI"""


    if arg_exists(args, '--generate'):
        dg = DataGeneration()
        found = dg.run(result=args['--generate'], ht=args['ht'])
        if found:
            for f_hash in found:
                print('data %s matches hash %s' %
                      (f_hash.upper(), args['--generate']))
            return CliStatus.SUCCESS.value
    elif arg_exists(args, '--depth'):
        dg = DataGeneration(int(args['--depth']))
        found = dg.run(ht=args['ht'])
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
    if arg_exists(args, '--verify'):
        return verify_data(args)
    if arg_exists(args, '--generate') or arg_exists(args, '--depth'):
        if arg_exists(args, '--generate') and \
                hash_len_valid(args['--generate'], args['ht']) is False:
            return CliStatus.ARG_INVALID.value
        return generate_data(args)
    if args['hd'] is None:
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
