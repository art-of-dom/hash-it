'''
Runs the CLI for hash-it
'''

from __future__ import absolute_import, print_function
from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType
from hashit.service.validate_hash import ValidateHash

def extract_args(args):
    '''
    extracts args for the CLI
    '''
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
    return hash_type, hash_data

def verify_data(args):
    validate = ValidateHash(
        result=args['--verify'],
        hash_type=args['ht'],
        data=args['hd']
    )
    if not validate.is_vaild():
        return 2
    return 0

def run_hash(args=None):
    '''
    Does the hashing actions for the CLI
    '''
    if args['--verify']:
        return verify_data(args)
    if args['<input>']:
        hash_str = HashIt(hash_type=args['ht'],
            hash_data=args['hd']
        ).hash_it()
        print('input: %s hash: %s'%(args['<input>'], hash_str))
    return 0

def cli_main(args=None):
    '''
    CLI main point of entry
    '''
    try:
        hash_type, hash_data = extract_args(args)
        args['ht'] = hash_type
        args['hd'] = hash_data
    except KeyError:
        print("Unknown hash type %s"%args['--hash-type'])
        return 1
    except TypeError:
        return 1

    return run_hash(args)
