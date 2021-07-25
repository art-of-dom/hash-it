"""
hashlib_mapping_crc16.py
Mapping hash lib syle functions to hash types crc16.
"""
from __future__ import absolute_import

import crcmod

from hashit.core.hash_type import HashType

HASHLIB_MAPPING_CRC16 = {
    HashType.CRC16: crcmod.predefined.Crc('crc-16').new,
    HashType.CRC16_AUG_CCITT: crcmod.predefined.Crc('crc-aug-ccitt').new,
    HashType.CRC16_BUYPASS: crcmod.predefined.Crc('crc-16-buypass').new,
    HashType.CRC16_CCITT_FALSE: crcmod.predefined.Crc('crc-ccitt-false').new,
    HashType.CRC16_DDS_110: crcmod.predefined.Crc('crc-16-dds-110').new,
    HashType.CRC16_DECT_R: crcmod.predefined.Crc('crc-16-dect').new,
    HashType.CRC16_DNP: crcmod.predefined.Crc('crc-16-dnp').new,
    HashType.CRC16_EN_13757: crcmod.predefined.Crc('crc-16-en-13757').new,
    HashType.CRC16_GENIUS: crcmod.predefined.Crc('crc-16-genibus').new,
    HashType.CRC16_KERMIT: crcmod.predefined.Crc('kermit').new,
    HashType.CRC16_MAXIM: crcmod.predefined.Crc('crc-16-maxim').new,
    HashType.CRC16_MCRF4XX: crcmod.predefined.Crc('crc-16-mcrf4xx').new,
    HashType.CRC16_MODBUS: crcmod.predefined.Crc('modbus').new,
    HashType.CRC16_RIELLO: crcmod.predefined.Crc('crc-16-riello').new,
    HashType.CRC16_T10_DIF: crcmod.predefined.Crc('crc-16-t10-dif').new,
    HashType.CRC16_TELEDISK: crcmod.predefined.Crc('crc-16-teledisk').new,
    HashType.CRC16_USB: crcmod.predefined.Crc('crc-16-usb').new,
    HashType.CRC16_X_25: crcmod.predefined.Crc('x-25').new,
    HashType.CRC16_XMODEM: crcmod.predefined.Crc('xmodem').new,
}
