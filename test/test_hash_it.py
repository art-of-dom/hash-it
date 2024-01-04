'''Tests for the HashIt object'''

import unittest

from parameterized import parameterized
import pytest

from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType

from hashit.utils.data_encap import DataEncap
from hashit.utils.data_type import DataType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=bad-continuation
# pylint: disable=too-many-public-methods

CHECK_STRING = '123456789'


class TestHashIt(unittest.TestCase):
    def setUp(self):
        self.check_str = HashData(DataEncap(DataType.ASCII, CHECK_STRING))
        self.example = HashData(
            DataEncap(DataType.FILE, "test/support/example.bin"))
        self.example_chunk = HashData(DataEncap(DataType.FILE,
                                                "test/support/example.bin"
                                                ), chunk_size=16)

    @parameterized.expand([
        ("CRC8", "F4"), ("CRC8_CDMA2000", "DA"), ("CRC8_DARC", "15"),
        ("CRC8_DVB_S2", "BC"), ("CRC8_EBU", "97"), ("CRC8_I_CODE", "7E"),
        ("CRC8_ITU", "A1"), ("CRC8_MAXIM", "A1"), ("CRC8_ROHC", "D0"),
        ("CRC8_WCDMA", "25"),
    ])
    def test_hash_it_crc8_check_str(self, name, result):
        assert result == HashIt().hash_it(HashType[name], self.check_str)

    def test_hash_it_crc8(self):
        assert "14" == HashIt().hash_it(HashType.CRC8, self.example)

    def test_hash_it_crc8_chunked(self):
        hashit = HashIt(HashType.CRC8, self.example_chunk)
        assert "41" == hashit.next_chunk()
        assert "84" == hashit.next_chunk()
        assert "CC" == hashit.next_chunk()
        assert "09" == hashit.next_chunk()
        assert "5C" == hashit.next_chunk()
        assert "99" == hashit.next_chunk()
        assert "D1" == hashit.next_chunk()
        assert "14" == hashit.next_chunk()

    @parameterized.expand([
        ("CRC16", "BB3D"), ("CRC16_A", "BF05"), ("CRC16_AUG_CCITT", "E5CC"),
        ("CRC16_BUYPASS", "FEE8"), ("CRC16_CMDA2000", "4C06"),
        ("CRC16_CCITT_FALSE", "29B1"), ("CRC16_DDS_110", "9ECF"),
        ("CRC16_DECT_R", "007E"), ("CRC16_DECT_X", "007F"),
        ("CRC16_DNP", "EA82"), ("CRC16_EN_13757", "C2B7"),
        ("CRC16_GENIUS", "D64E"), ("CRC16_KERMIT", "2189"),
        ("CRC16_MAXIM", "44C2"), ("CRC16_MCRF4XX", "6F91"),
        ("CRC16_MODBUS", "4B37"), ("CRC16_RIELLO", "63D0"),
        ("CRC16_T10_DIF", "D0DB"), ("CRC16_TELEDISK", "0FB3"),
        ("CRC16_TMS37157", "26B1"), ("CRC16_USB", "B4C8"),
        ("CRC16_X_25", "906E"), ("CRC16_XMODEM", "31C3")
    ])
    def test_hash_it_crc16_check_str(self, name, result):
        assert result == HashIt().hash_it(HashType[name], self.check_str)

    def test_hash_it_crc16(self):
        assert "BAD3" == HashIt().hash_it(HashType.CRC16, self.example)

    def test_hash_it_crc16_chunked(self):
        hashit = HashIt(HashType.CRC16, self.example_chunk)
        assert "170A" == hashit.next_chunk()
        assert "6ABB" == hashit.next_chunk()
        assert "EC68" == hashit.next_chunk()
        assert "91D9" == hashit.next_chunk()
        assert "A1CD" == hashit.next_chunk()
        assert "DC7C" == hashit.next_chunk()
        assert "5AAF" == hashit.next_chunk()
        assert "271E" == hashit.next_chunk()

    def test_hash_it_crc32(self):
        assert "29058C73" == HashIt().hash_it(
            HashType.CRC32, self.example)

    @parameterized.expand([
        ("CRC24", "21CF02"), ("CRC24_FLEXRAY_A", "7979BD"),
        ("CRC24_FLEXRAY_B", "1F23B8"),
    ])
    def test_hash_it_crc24_check_str(self, name, result):
        assert result == HashIt().hash_it(HashType[name], self.check_str)

    def test_hash_it_crc32_chunked(self):
        hashit = HashIt(HashType.CRC32, self.example_chunk)
        assert "CECEE288" == hashit.next_chunk()
        assert "F4A7FD67" == hashit.next_chunk()
        assert "BA1CDD56" == hashit.next_chunk()
        assert "8075C2B9" == hashit.next_chunk()
        assert "276A9D34" == hashit.next_chunk()
        assert "1D0382DB" == hashit.next_chunk()
        assert "53B8A2EA" == hashit.next_chunk()
        assert "69D1BD05" == hashit.next_chunk()

    def test_hash_it_crc64(self):
        assert "6C27EAA78BA3F822" == HashIt().hash_it(
            HashType.CRC64, self.example)

    def test_hash_it_crc64_chunked(self):
        hashit = HashIt(HashType.CRC64, self.example_chunk)
        assert "D744B0AF58936778" == hashit.next_chunk()
        assert "AF1BEFF007CC3827" == hashit.next_chunk()
        assert "27FA0E11E62DD9C6" == hashit.next_chunk()
        assert "5FA5514EB9728699" == hashit.next_chunk()
        assert "8639CDD225EE1A05" == hashit.next_chunk()
        assert "FE66928D7AB1455A" == hashit.next_chunk()
        assert "7687736C9B50A4BB" == hashit.next_chunk()
        assert "0ED82C33C40FFBE4" == hashit.next_chunk()

    def test_hash_it_md2_not_implemented(self):
        with pytest.raises(NotImplementedError):
            HashIt().hash_it(HashType.MD2, self.example)

    def test_hash_it_md4_not_implemented(self):
        with pytest.raises(NotImplementedError):
            HashIt().hash_it(HashType.MD4, self.example)

    def test_hash_it_md5(self):
        assert ("E2C865DB4162BED963BFAA9EF6AC18F0" ==
                      HashIt().hash_it(HashType.MD5, self.example))

    def test_hash_it_md5_chunked(self):
        hashit = HashIt(HashType.MD5, self.example_chunk)
        assert "1AC1EF01E96CAF1BE0D329331A4FC2A8" == hashit.next_chunk()
        assert "1BF42E241816BA29FF5F307BB1BC1D16" == hashit.next_chunk()
        assert "35BA6D08F0E34C15B9D0B09998960EB6" == hashit.next_chunk()
        assert "BDF2930F973F722E24A3773D61889501" == hashit.next_chunk()
        assert "0D712DEA46B6358A634362733F554587" == hashit.next_chunk()
        assert "3C0F2B607B04F4FD8FD8F9CDF8AE9364" == hashit.next_chunk()
        assert "C0A124EE4E7ADEC252B8DAC8DFCA7E93" == hashit.next_chunk()
        assert "CD4ED69C6078EB63138FEFEE3F03DA9F" == hashit.next_chunk()

    def test_hash_it_sha1(self):
        assert ("4916D6BDB7F78E6803698CAB32D1586EA457DFC8" ==
                      HashIt().hash_it(HashType.SHA1, self.example))

    def test_hash_it_sha1_chunked(self):
        hashit = HashIt(HashType.SHA1, self.example_chunk)
        assert ("56178B86A57FAC22899A9964185C2CC96E7DA589" ==
                      hashit.next_chunk())
        assert ("CA148D05E875BCB8CCE4FD2C2C720BFD2E64753B" ==
                      hashit.next_chunk())
        assert ("5C3F75DDA77EB61EF6D04B5045BDF661F4FA608C" ==
                      hashit.next_chunk())
        assert ("06125DF041AD83637F19BF15CF0AEA101C1DF0AA" ==
                      hashit.next_chunk())
        assert ("82FCD6EA686650AEAB977D7AF3AD6081AB8A10DE" ==
                      hashit.next_chunk())
        assert ("438916A1420915236DD8EC42DAD6B343DDFD1388" ==
                      hashit.next_chunk())
        assert ("148DDC86C22B76616E412D2104706F6D34E627AD" ==
                      hashit.next_chunk())
        assert ("7E1FF3CB5122AF29DC2844E7B05EC779DD4C14AB" ==
                      hashit.next_chunk())

    def test_hash_it_sha224(self):
        assert ("88702E63237824C4EB0D0FCFE41469A462493E8BEB2A75BBE5981734" ==
                      HashIt().hash_it(HashType.SHA224, self.example))

    def test_hash_it_sha224_chunked(self):
        hashit = HashIt(HashType.SHA224, self.example_chunk)
        assert ("529D656A8BC413FEF58DA82E1BF0308DCFE0429DCD80687E69C94633" ==
                      hashit.next_chunk())
        assert ("0E97EA1BD23A0A7CB12CD3B7ECB9A60D6025C8CE105924279833CE85" ==
                      hashit.next_chunk())
        assert ("39E8EB9A3607349FC39A33C5AC6E326CF863AF32E5424F9FAD1B8584" ==
                      hashit.next_chunk())
        assert ("5371E71E799E41C70DE23DA40E283A4A997FBCD2A7B09F9CA91FA836" ==
                      hashit.next_chunk())
        assert ("A0C92632278202BE93F9815D4939A7ECA76E690B3A86C22B10AC154B" ==
                      hashit.next_chunk())
        assert ("FC74DD0B5078C8D1466F85C51B1EDF0DC65FF308035FD32113B83155" ==
                      hashit.next_chunk())
        assert ("E3A6ACADFEF1A97FF76E813F3C9F8ABD8498BDE28C8D295B5F315EBD" ==
                      hashit.next_chunk())
        assert ("F688C227166F7B837FA4C3AB010C08AF8C98FAFE61CB066D72B9B205" ==
                      hashit.next_chunk())

    def test_hash_it_sha256(self):
        assert ("40AFF2E9D2D8922E47AFD4648E6967497158785FBD1DA870E7110266BF944880" ==
                      HashIt().hash_it(HashType.SHA256, self.example))

    def test_hash_it_sha256_chunked(self):
        hashit = HashIt(HashType.SHA256, self.example_chunk)
        assert ("BE45CB2605BF36BEBDE684841A28F0FD43C69850A3DCE5FEDBA69928EE3A8991" ==
                      hashit.next_chunk())
        assert ("FC2E2C73072BFA2BDA03FF9307472DEBD3CC8105028A8A9E235E35BA8D2E37F4" ==
                      hashit.next_chunk())
        assert ("36DB1ADC807AC50E4C85BD86A174B4AA260154E4F172A3659698945D7B16D084" ==
                      hashit.next_chunk())
        assert ("816B9E7C25D559C5766755B3BBB36654AD451E080FFA93694A793D6EED41F40A" ==
                      hashit.next_chunk())
        assert ("BA22B7DC95F6CC8765757BE4BCCF37CD92ECE6D4987DC26A31E274C9BE236921" ==
                      hashit.next_chunk())
        assert ("372AFEFA6BCD01BE7504CFE132D4CDB5151ED08DE35825772BDECAB4C4EB6FBC" ==
                      hashit.next_chunk())
        assert ("2ED1BAD92452DF6752AC09877A37FC86EC876010FAA7D80765BD5131FB8E0226" ==
                      hashit.next_chunk())
        assert ("FBD8C6B1CD3C16E5A21471CD88E33224C138BDCD856586F752C28BEDADC181FD" ==
                      hashit.next_chunk())

    def test_hash_it_sha384(self):
        assert ("FFDAEBFF65ED05CF400F0221C4CCFB4B2104FB6A51F87E40BE6C4309386BFDEC2"
                      "892E9179B34632331A59592737DB5C5" ==
                      HashIt().hash_it(HashType.SHA384, self.example))

    def test_hash_it_sha512(self):
        assert ("1E7B80BC8EDC552C8FEEB2780E111477E5BC70465FAC1A77B29B35980C3F0CE4A"
                      "036A6C9462036824BD56801E62AF7E9FEBA5C22ED8A5AF877BF7DE117DCAC6D" ==
                      HashIt().hash_it(HashType.SHA512, self.example))
