'''Tests for the HashType Enum'''

from __future__ import absolute_import
import unittest

from nose.tools import assert_equals, assert_true, assert_false
from parameterized import parameterized

from hashit.core.hash_type import HashType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods


class TestHashType(unittest.TestCase):

    @parameterized.expand([
        "CRC8", "CRC8_CDMA2000", "CRC8_DARC", "CRC8_DVB_S2", "CRC8_EBU",
        "CRC8_I_CODE", "CRC8_ITU", "CRC8_MAXIM", "CRC8_ROHC", "CRC8_WCDMA",
        "CRC16", "CRC16_A", "CRC16_AUG_CCITT", "CRC16_BUYPASS",
        "CRC16_CMDA2000", "CRC16_CCITT_FALSE", "CRC16_DDS_110", "CRC16_DECT_R",
        "CRC16_DECT_X", "CRC16_DNP", "CRC16_EN_13757", "CRC16_GENIUS",
        "CRC16_KERMIT", "CRC16_MAXIM", "CRC16_MCRF4XX", "CRC16_MODBUS",
        "CRC16_RIELLO", "CRC16_T10_DIF", "CRC16_TELEDISK", "CRC16_TMS37157",
        "CRC16_USB", "CRC16_X_25", "CRC16_XMODEM", "CRC24", "CRC24_FLEXRAY_A",
        "CRC24_FLEXRAY_B", "CRC32", "CRC64", "MD2", "MD4", "MD5",
        "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"
    ])
    def test_hash_type_in_enum(self, name):
        assert_true(name in HashType.__members__)

    @parameterized.expand([
        ("CRC8", HashType.CRC8), ("CRC8_CDMA2000", HashType.CRC8_CDMA2000),
        ("CRC8_DARC", HashType.CRC8_DARC), ("CRC8_DVB_S2", HashType.CRC8_DVB_S2),
        ("CRC8_EBU", HashType.CRC8_EBU), ("CRC8_I_CODE", HashType.CRC8_I_CODE),
        ("CRC8_ITU", HashType.CRC8_ITU), ("CRC8_MAXIM", HashType.CRC8_MAXIM),
        ("CRC8_ROHC", HashType.CRC8_ROHC), ("CRC8_WCDMA", HashType.CRC8_WCDMA),
        ("CRC16", HashType.CRC16), ("CRC16_A", HashType.CRC16_A),
        ("CRC16_AUG_CCITT", HashType.CRC16_AUG_CCITT),
        ("CRC16_BUYPASS", HashType.CRC16_BUYPASS),
        ("CRC16_CMDA2000", HashType.CRC16_CMDA2000),
        ("CRC16_CCITT_FALSE", HashType.CRC16_CCITT_FALSE),
        ("CRC16_DDS_110", HashType.CRC16_DDS_110), ("CRC16_DECT_R", HashType.CRC16_DECT_R),
        ("CRC16_DECT_X", HashType.CRC16_DECT_X), ("CRC16_DNP", HashType.CRC16_DNP),
        ("CRC16_EN_13757", HashType.CRC16_EN_13757),
        ("CRC16_GENIUS", HashType.CRC16_GENIUS), ("CRC16_KERMIT", HashType.CRC16_KERMIT),
        ("CRC16_MAXIM", HashType.CRC16_MAXIM), ("CRC16_MCRF4XX", HashType.CRC16_MCRF4XX),
        ("CRC16_MODBUS", HashType.CRC16_MODBUS), ("CRC16_RIELLO", HashType.CRC16_RIELLO),
        ("CRC16_T10_DIF", HashType.CRC16_T10_DIF),
        ("CRC16_TELEDISK", HashType.CRC16_TELEDISK),
        ("CRC16_TMS37157", HashType.CRC16_TMS37157),
        ("CRC16_USB", HashType.CRC16_USB), ("CRC16_X_25", HashType.CRC16_X_25),
        ("CRC16_XMODEM", HashType.CRC16_XMODEM), ("CRC24", HashType.CRC24),
        ("CRC24_FLEXRAY_A", HashType.CRC24_FLEXRAY_A),
        ("CRC24_FLEXRAY_B", HashType.CRC24_FLEXRAY_B), ("CRC32", HashType.CRC32),
        ("CRC64", HashType.CRC64), ("MD2", HashType.MD2),
        ("MD4", HashType.MD4), ("MD5", HashType.MD5), ("SHA1", HashType.SHA1),
        ("SHA224", HashType.SHA224), ("SHA256", HashType.SHA256),
        ("SHA384", HashType.SHA384), ("SHA512", HashType.SHA512)
    ])
    def test_hash_type_lookup(self, name, htype):
        assert_equals(htype, HashType[name])

    @parameterized.expand([
        "CRC8", "CRC8_CDMA2000", "CRC8_DARC", "CRC8_DVB_S2", "CRC8_EBU",
        "CRC8_I_CODE", "CRC8_ITU", "CRC8_MAXIM", "CRC8_ROHC", "CRC8_WCDMA",
        "CRC16", "CRC16_A", "CRC16_AUG_CCITT", "CRC16_BUYPASS",
        "CRC16_CMDA2000", "CRC16_CCITT_FALSE", "CRC16_DDS_110", "CRC16_DECT_R",
        "CRC16_DECT_X", "CRC16_DNP", "CRC16_EN_13757", "CRC16_GENIUS",
        "CRC16_KERMIT", "CRC16_MAXIM", "CRC16_MCRF4XX", "CRC16_MODBUS",
        "CRC16_RIELLO", "CRC16_T10_DIF", "CRC16_TELEDISK", "CRC16_TMS37157",
        "CRC16_USB", "CRC16_X_25", "CRC16_XMODEM", "CRC24", "CRC24_FLEXRAY_A",
        "CRC24_FLEXRAY_B", "CRC32", "CRC64"
    ])
    def test_hash_type_is_crc(self, name):
        assert_true(HashType[name].is_crc())

    @parameterized.expand([
        "MD2", "MD4", "MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"
    ])
    def test_hash_type_is_not_crc(self, name):
        assert_false(HashType[name].is_crc())

    @parameterized.expand([
        "MD2", "MD4", "MD5"
    ])
    def test_hash_type_is_md(self, name):
        assert_true(HashType[name].is_md())

    @parameterized.expand([
        "CRC8", "CRC8_CDMA2000", "CRC8_DARC", "CRC8_DVB_S2", "CRC8_EBU",
        "CRC8_I_CODE", "CRC8_ITU", "CRC8_MAXIM", "CRC8_ROHC", "CRC8_WCDMA",
        "CRC16", "CRC16_A", "CRC16_AUG_CCITT", "CRC16_BUYPASS",
        "CRC16_CMDA2000", "CRC16_CCITT_FALSE", "CRC16_DDS_110", "CRC16_DECT_R",
        "CRC16_DECT_X", "CRC16_DNP", "CRC16_EN_13757", "CRC16_GENIUS",
        "CRC16_KERMIT", "CRC16_MAXIM", "CRC16_MCRF4XX", "CRC16_MODBUS",
        "CRC16_RIELLO", "CRC16_T10_DIF", "CRC16_TELEDISK", "CRC16_TMS37157",
        "CRC16_USB", "CRC16_X_25", "CRC16_XMODEM", "CRC24", "CRC24_FLEXRAY_A",
        "CRC24_FLEXRAY_B", "CRC32", "CRC64",
        "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"
    ])
    def test_hash_type_is_not_md(self, name):
        assert_false(HashType[name].is_md())

    @parameterized.expand([
        "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"
    ])
    def test_hash_type_is_sha(self, name):
        assert_true(HashType[name].is_sha())

    @parameterized.expand([
        "CRC8", "CRC8_CDMA2000", "CRC8_DARC", "CRC8_DVB_S2", "CRC8_EBU",
        "CRC8_I_CODE", "CRC8_ITU", "CRC8_MAXIM", "CRC8_ROHC", "CRC8_WCDMA",
        "CRC16", "CRC16_A", "CRC16_AUG_CCITT", "CRC16_BUYPASS",
        "CRC16_CMDA2000", "CRC16_CCITT_FALSE", "CRC16_DDS_110", "CRC16_DECT_R",
        "CRC16_DECT_X", "CRC16_DNP", "CRC16_EN_13757", "CRC16_GENIUS",
        "CRC16_KERMIT", "CRC16_MAXIM", "CRC16_MCRF4XX", "CRC16_MODBUS",
        "CRC16_RIELLO", "CRC16_T10_DIF", "CRC16_TELEDISK", "CRC16_TMS37157",
        "CRC16_USB", "CRC16_X_25", "CRC16_XMODEM", "CRC24", "CRC24_FLEXRAY_A",
        "CRC24_FLEXRAY_B", "CRC32", "CRC64", "MD2", "MD4", "MD5"
    ])
    def test_hash_type_is_not_sha(self, name):
        assert_false(HashType[name].is_sha())

    # CRC 8

    def test_hash_type_crc8_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8.hash_byte_length())

    def test_hash_type_crc8_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8.hash_str_length())

    def test_hash_type_crc8_cdma2000_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_CDMA2000.hash_byte_length())

    def test_hash_type_crc8_cdma2000_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_CDMA2000.hash_str_length())

    def test_hash_type_crc8_darc_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_DARC.hash_byte_length())

    def test_hash_type_crc8_darc_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_DARC.hash_str_length())

    def test_hash_type_crc8_dvb_s2_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_DVB_S2.hash_byte_length())

    def test_hash_type_crc8_dvb_s2_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_DVB_S2.hash_str_length())

    def test_hash_type_crc8_ebu_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_EBU.hash_byte_length())

    def test_hash_type_crc8_ebu_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_EBU.hash_str_length())

    def test_hash_type_crc8_i_code_has_hash_str_length_1(self):
        assert_equals(1, HashType.CRC8_I_CODE.hash_byte_length())

    def test_hash_type_crc8_i_code_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_I_CODE.hash_str_length())

    def test_hash_type_crc8_itu_has_hash_str_length_1(self):
        assert_equals(1, HashType.CRC8_ITU.hash_byte_length())

    def test_hash_type_crc8_itu_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_ITU.hash_str_length())

    def test_hash_type_crc8_maxim_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_MAXIM.hash_byte_length())

    def test_hash_type_crc8_maxim_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_MAXIM.hash_str_length())

    def test_hash_type_crc8_rohc_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_ROHC.hash_byte_length())

    def test_hash_type_crc8_rohc_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_ROHC.hash_str_length())

    def test_hash_type_crc8_wcdma_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_WCDMA.hash_byte_length())

    def test_hash_type_crc8_wcdma_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_WCDMA.hash_str_length())

    # CRC16

    def test_hash_type_crc16_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16.hash_byte_length())

    def test_hash_type_crc16_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16.hash_str_length())

    def test_hash_type_crc16_a_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_A.hash_byte_length())

    def test_hash_type_crc16_a_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_A.hash_str_length())

    def test_hash_type_crc16_aug_ccitt_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_AUG_CCITT.hash_byte_length())

    def test_hash_type_crc16_aug_ccitt_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_AUG_CCITT.hash_str_length())

    def test_hash_type_crc16_buypass_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_BUYPASS.hash_byte_length())

    def test_hash_type_crc16_buypass_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_BUYPASS.hash_str_length())

    def test_hash_type_crc16_cmda2000_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_CMDA2000.hash_byte_length())

    def test_hash_type_crc16_cmda2000_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_CMDA2000.hash_str_length())

    def test_hash_type_crc16_ccitt_false_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_CCITT_FALSE.hash_byte_length())

    def test_hash_type_crc16_ccitt_false_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_CCITT_FALSE.hash_str_length())

    def test_hash_type_crc16_dds_110_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DDS_110.hash_byte_length())

    def test_hash_type_crc16_dds_110_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DDS_110.hash_str_length())

    def test_hash_type_crc16_dect_r_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DECT_R.hash_byte_length())

    def test_hash_type_crc16_dect_r_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DECT_R.hash_str_length())

    def test_hash_type_crc16_dect_x_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DECT_X.hash_byte_length())

    def test_hash_type_crc16_dect_x_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DECT_X.hash_str_length())

    def test_hash_type_crc16_dnp_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DNP.hash_byte_length())

    def test_hash_type_crc16_dnp_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DNP.hash_str_length())

    def test_hash_type_crc16_en_13757_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_EN_13757.hash_byte_length())

    def test_hash_type_crc16_en_13757_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_EN_13757.hash_str_length())

    def test_hash_type_crc16_genius_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_GENIUS.hash_byte_length())

    def test_hash_type_crc16_genius_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_GENIUS.hash_str_length())

    def test_hash_type_crc16_kermit_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_KERMIT.hash_byte_length())

    def test_hash_type_crc16_kermit_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_KERMIT.hash_str_length())

    def test_hash_type_crc16_maxim_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_MAXIM.hash_byte_length())

    def test_hash_type_crc16_maxim_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_MAXIM.hash_str_length())

    def test_hash_type_crc16_mcrf4xx_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_MCRF4XX.hash_byte_length())

    def test_hash_type_crc16_mcrf4xx_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_MCRF4XX.hash_str_length())

    def test_hash_type_crc16_modbus_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_MODBUS.hash_byte_length())

    def test_hash_type_crc16_modbus_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_MODBUS.hash_str_length())

    def test_hash_type_crc16_riello_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_RIELLO.hash_byte_length())

    def test_hash_type_crc16_riello_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_RIELLO.hash_str_length())

    def test_hash_type_crc16_t10_dif_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_T10_DIF.hash_byte_length())

    def test_hash_type_crc16_t10_dif_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_T10_DIF.hash_str_length())

    def test_hash_type_crc16_teledisk_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_TELEDISK.hash_byte_length())

    def test_hash_type_crc16_teledisk_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_TELEDISK.hash_str_length())

    def test_hash_type_crc16_tms37157_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_TMS37157.hash_byte_length())

    def test_hash_type_crc16_tms37157_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_TMS37157.hash_str_length())

    def test_hash_type_crc16_usb_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_USB.hash_byte_length())

    def test_hash_type_crc16_usb_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_USB.hash_str_length())

    def test_hash_type_crc16_x_25_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_X_25.hash_byte_length())

    def test_hash_type_crc16_x_25_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_X_25.hash_str_length())

    def test_hash_type_crc16_xmodem_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_XMODEM.hash_byte_length())

    def test_hash_type_crc16_xmodem_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_XMODEM.hash_str_length())

    # Others

    def test_hash_type_crc32_has_hash_byte_length_4(self):
        assert_equals(4, HashType.CRC32.hash_byte_length())

    def test_hash_type_crc32_has_hash_str_length_8(self):
        assert_equals(8, HashType.CRC32.hash_str_length())

    def test_hash_type_crc64_has_hash_byte_length_8(self):
        assert_equals(8, HashType.CRC64.hash_byte_length())

    def test_hash_type_crc64_has_hash_str_length_16(self):
        assert_equals(16, HashType.CRC64.hash_str_length())

    def test_hash_type_md2_has_hash_byte_length_16(self):
        assert_equals(16, HashType.MD2.hash_byte_length())

    def test_hash_type_md2_has_hash_str_length_32(self):
        assert_equals(32, HashType.MD2.hash_str_length())

    def test_hash_type_md4_has_hash_byte_length_16(self):
        assert_equals(16, HashType.MD4.hash_byte_length())

    def test_hash_type_md4_has_hash_str_length_32(self):
        assert_equals(32, HashType.MD4.hash_str_length())

    def test_hash_type_md5_has_hash_byte_length_16(self):
        assert_equals(16, HashType.MD5.hash_byte_length())

    def test_hash_type_md5_has_hash_str_length_32(self):
        assert_equals(32, HashType.MD5.hash_str_length())

    def test_hash_type_sha1_has_hash_byte_length_20(self):
        assert_equals(20, HashType.SHA1.hash_byte_length())

    def test_hash_type_sha1_has_hash_str_length_40(self):
        assert_equals(40, HashType.SHA1.hash_str_length())

    def test_hash_type_sha224_has_hash_byte_length_28(self):
        assert_equals(28, HashType.SHA224.hash_byte_length())

    def test_hash_type_sha224_has_hash_str_length_56(self):
        assert_equals(56, HashType.SHA224.hash_str_length())

    def test_hash_type_sha256_has_hash_byte_length_32(self):
        assert_equals(32, HashType.SHA256.hash_byte_length())

    def test_hash_type_sha256_has_hash_str_length_64(self):
        assert_equals(64, HashType.SHA256.hash_str_length())

    def test_hash_type_sha2384_has_hash_byte_length_48(self):
        assert_equals(48, HashType.SHA384.hash_byte_length())

    def test_hash_type_sha2384_has_hash_str_length_96(self):
        assert_equals(96, HashType.SHA384.hash_str_length())

    def test_hash_type_sha512_has_hash_byte_length_64(self):
        assert_equals(64, HashType.SHA512.hash_byte_length())

    def test_hash_type_sha256_has_hash_str_length_128(self):
        assert_equals(128, HashType.SHA512.hash_str_length())
