"""
custom_crc_mapping.py
Custom CRC mappings.
"""
from __future__ import absolute_import

import crcmod
from hashit.core.hash_type import HashType

CRCMOD_CUSTOM_MAPPING = {
    HashType.CRC8_CDMA2000: crcmod.mkCrcFun(0x19B,
        initCrc=0xFF, rev=False, xorOut=0x00
    ),
    HashType.CRC8_DVB_S2: crcmod.mkCrcFun(0x1D5,
        initCrc=0x00, rev=False, xorOut=0x00
    ),
    HashType.CRC8_EBU: crcmod.mkCrcFun(0x11D,
        initCrc=0xFF, rev=True, xorOut=0x00
    )
}
