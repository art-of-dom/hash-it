"""
CliStatus.py

Enumerates the cli status.
"""

from enum import Enum


class CliStatus(Enum):
    """
    An Enumerated representation of a cli status used in hash it
    """
    SUCCESS = 0
    ARG_INVALID = 1
    VALIDATION_ERROR = 2
    GENERATION_ERROR = 4
