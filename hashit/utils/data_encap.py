"""
hash_data.py
Keeps track of data for hashing.
"""

from __future__ import absolute_import, division
import os
import sys

from hashit.utils.data_type import DataType


class DataEncap:
    """The object to keep track of raw data"""

    def __init__(self, data_type=None, data=None):
        self.data_type = data_type
        self.size = 0
        self.filename = None
        self.data = None
        self._setup_data(data)

    def _setup_data(self, data):
        """Sets data based on type"""
        if self.data_type == DataType.FILE:
            self.filename = data
            self.size = os.path.getsize(self.filename)
            self.data = None
        elif self.data_type in [DataType.ASCII, DataType.BYTES]:
            self.size = len(data)
            self.data = data
        elif self.data_type == DataType.HEX:
            self.data = str(bytearray.fromhex(data).decode())
            self.size = len(data)
            self.data_type = DataType.ASCII
        elif self.data_type == DataType.STDIN:
            self._get_stdin()

    def _get_stdin(self):
        """Gets data from stdin"""
        self.data = ''
        if not sys.stdin.isatty():
            try:
                infile = sys.stdin.buffer
                self.data = infile.read()
            except AttributeError:
                for line in sys.stdin:
                    self.data += line
        self.size = len(self.data)

    def reverse(self):
        """Reverse the stored data"""
        if self.data:
            if isinstance(self.data, str):
                self.data = bytearray(self.data.encode())
            self.data.reverse()
        elif self.filename:
            with open(self.filename, 'rb') as fin:
                fin.seek(0)
                self.data = bytearray(fin.read(self.size))
            self.data.reverse()
            self.data_type = DataType.ASCII

    def get_chunk(self, start=0, end=None):
        """Gets Next Data Chunk"""
        chunk = None
        if end is None:
            end = self.size

        if self.data_type == DataType.FILE:
            with open(self.filename, 'rb') as fin:
                fin.seek(start)
                chunk = fin.read(end - start)
        else:
            chunk = self.data[start:end]

        return chunk
