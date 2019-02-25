'''
'''

from __future__ import absolute_import
from hashit.HashIt import HashIt
from hashit.HashType import HashType

def cli_main(args=None):
    if not args:
        return 1
    hash_str = ''

    if args['-f']:
        hash_str = HashIt(hash_type=HashType.CRC16,
                filename=args['<input>']).hash_it()
        print('file: %s hash: %s'%(args['<input>'], hash_str))

    return 0
