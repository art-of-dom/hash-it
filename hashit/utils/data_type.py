"""
DataType.py

Enumerates the hash types to easily encapsulte data.
"""

from enum import Enum


class DataType(Enum):
    """An Enumerated representation of data used for parsing"""
    ASCII = 0
    HEX = 1
    FILE = 2
    STDIN = 3
    BYTES = 4
