"""
hash_data.py
Keeps track of data for hashing.
"""

from __future__ import absolute_import, division
import os


class HashData(object):
    """
    The object to keep track of data being hashed
    """

    def __init__(self, filename=None, data=None, chunk_size=0):
        self.filename = filename
        self.chunk_size = chunk_size
        self.pos = 0
        self.data = data
        self.size = 0

        if filename is not None:
            self.size = os.path.getsize(filename)
        elif data is not None:
            self.size = len(data)

        if self.chunk_size == 0:
            self.chunk_size = self.size

    def reverse(self):
        """Reverse the stored hash data"""
        if self.data:
            self.data = bytearray(self.data)
            self.data.reverse()
        elif self.filename:
            with open(self.filename, 'rb') as fin:
                fin.seek(self.pos)
                self.data = bytearray(fin.read(self.chunk_size))
            self.data.reverse()
        self.data = str(self.data)

    def percent_processed(self):
        """Give the data yet to be processed as a pecentage"""
        try:
            return (self.pos / self.size) * 100.0
        except ZeroDivisionError:
            return 100.0

    def next_chunk(self):
        """Give the next chunk of pure data"""
        data = None
        if self.pos == self.size:
            return None
        end_pos = self.pos + self.chunk_size
        if end_pos > self.size:
            end_pos = self.size

        if self.data:
            data = self.data[self.pos:end_pos]
        elif self.filename:
            with open(self.filename, 'rb') as fin:
                fin.seek(self.pos)
                data = fin.read(self.chunk_size)

        self.pos = end_pos
        return data
