"""
hash_data.py
Keeps track of data for hashing.
"""

from __future__ import absolute_import, division

from hashit.utils.data_encap import DataEncap


class HashData(object):
    """The object to keep track of data being hashed"""

    def __init__(self, data_encap=None, chunk_size=0):
        self.data_encap = data_encap
        self.chunk_size = chunk_size
        self.pos = 0

        if data_encap is None:
           self.data_encap = DataEncap()
        if self.chunk_size == 0:
            self.chunk_size = self.data_encap.size

    def reverse(self):
        """Reverse the stored hash data"""
        self.data_encap.reverse()

    def percent_processed(self):
        """Give the data yet to be processed as a pecentage"""
        try:
            return (self.pos / self.data_encap.size) * 100.0
        except ZeroDivisionError:
            return 100.0

    def next_chunk(self):
        """Give the next chunk of pure data"""
        data = None
        if self.pos == self.data_encap.size:
            return None
        end_pos = self.pos + self.chunk_size
        if end_pos > self.data_encap.size:
            end_pos = self.data_encap.size

        data = self.data_encap.get_chunk(self.pos, end_pos)
        self.pos = end_pos
        return data
