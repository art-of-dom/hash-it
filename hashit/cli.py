'''
'''

from __future__ import absolute_import
from hashit.hash_it import HashIt
from hashit.hash_type import HashType
from hashit.validate_hash import ValidateHash

def cli_main(args=None):
    if not args:
        return 1
    hash_str = ''
    hash_type = HashType.CRC16

    if args['--hash-type']:
        try:
            hash_type = HashType[args['--hash-type'].upper()]
        except KeyError:
            print("Unknown hash type %s"%args['--hash-type'])
            return 1
    else:
        pass # Assume CRC16

    if not args['--verify']:
        if args['-f']:
            hash_str = HashIt(hash_type=hash_type,
                    filename=args['<input>']).hash_it()
            print('file: %s hash: %s'%(args['<input>'], hash_str))
    else:
        if args['-f']:
            validate = ValidateHash(
                result=args['--verify'],
                hash_type=hash_type,
                filename=args['<input>']
            )
            if validate.is_vaild():
                return 0
            return 2

    return 0
