'''
'''

from nose.tools import assert_equals, raises, assert_true
from HashIt import HashIt
from HashType import  HashType


def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_hash_it_crc16():
    assert_equals("BAD3", HashIt().hash_it(HashType.CRC16, "test/support/example.bin"))

def test_hash_it_crc16_chunked():
    hashit = HashIt(hash_type=HashType.CRC16, filename="test/support/example.bin", size=16)
    assert_equals("170A", hashit.next_chunk())
    assert_equals("6ABB", hashit.next_chunk())
    assert_equals("EC68", hashit.next_chunk())
    assert_equals("91D9", hashit.next_chunk())
    assert_equals("A1CD", hashit.next_chunk())
    assert_equals("DC7C", hashit.next_chunk())
    assert_equals("5AAF", hashit.next_chunk())
    assert_equals("271E", hashit.next_chunk())

def test_hash_it_crc32():
    assert_equals("29058C73", HashIt().hash_it(HashType.CRC32, "test/support/example.bin"))

def test_hash_it_crc32_chunked():
    hashit = HashIt(hash_type=HashType.CRC32, filename="test/support/example.bin", size=16)
    assert_equals("CECEE288", hashit.next_chunk())
    assert_equals("F4A7FD67", hashit.next_chunk())
    assert_equals("BA1CDD56", hashit.next_chunk())
    assert_equals("8075C2B9", hashit.next_chunk())
    assert_equals("276A9D34", hashit.next_chunk())
    assert_equals("1D0382DB", hashit.next_chunk())
    assert_equals("53B8A2EA", hashit.next_chunk())
    assert_equals("69D1BD05", hashit.next_chunk())


def test_hash_it_md5():
    assert_equals("E2C865DB4162BED963BFAA9EF6AC18F0",
                  HashIt().hash_it(HashType.MD5, "test/support/example.bin"))

def test_hash_it_md5_chunked():
    hashit = HashIt(hash_type=HashType.MD5, filename="test/support/example.bin", size=16)
    assert_equals("1AC1EF01E96CAF1BE0D329331A4FC2A8", hashit.next_chunk())
    assert_equals("1BF42E241816BA29FF5F307BB1BC1D16", hashit.next_chunk())
    assert_equals("35BA6D08F0E34C15B9D0B09998960EB6", hashit.next_chunk())
    assert_equals("BDF2930F973F722E24A3773D61889501", hashit.next_chunk())
    assert_equals("0D712DEA46B6358A634362733F554587", hashit.next_chunk())
    assert_equals("3C0F2B607B04F4FD8FD8F9CDF8AE9364", hashit.next_chunk())
    assert_equals("C0A124EE4E7ADEC252B8DAC8DFCA7E93", hashit.next_chunk())
    assert_equals("CD4ED69C6078EB63138FEFEE3F03DA9F", hashit.next_chunk())


def test_hash_it_sha1():
    assert_equals("4916D6BDB7F78E6803698CAB32D1586EA457DFC8",
                  HashIt().hash_it(HashType.SHA1, "test/support/example.bin"))

def test_hash_it_sha1_chunked():
    hashit = HashIt(hash_type=HashType.SHA1, filename="test/support/example.bin", size=16)
    assert_equals("56178B86A57FAC22899A9964185C2CC96E7DA589", hashit.next_chunk())
    assert_equals("CA148D05E875BCB8CCE4FD2C2C720BFD2E64753B", hashit.next_chunk())
    assert_equals("5C3F75DDA77EB61EF6D04B5045BDF661F4FA608C", hashit.next_chunk())
    assert_equals("06125DF041AD83637F19BF15CF0AEA101C1DF0AA", hashit.next_chunk())
    assert_equals("82FCD6EA686650AEAB977D7AF3AD6081AB8A10DE", hashit.next_chunk())
    assert_equals("438916A1420915236DD8EC42DAD6B343DDFD1388", hashit.next_chunk())
    assert_equals("148DDC86C22B76616E412D2104706F6D34E627AD", hashit.next_chunk())
    assert_equals("7E1FF3CB5122AF29DC2844E7B05EC779DD4C14AB", hashit.next_chunk())


def test_hash_it_sha224():
    assert_equals("88702E63237824C4EB0D0FCFE41469A462493E8BEB2A75BBE5981734",
                  HashIt().hash_it(HashType.SHA224, "test/support/example.bin"))

def test_hash_it_sha224_chunked():
    hashit = HashIt(hash_type=HashType.SHA224, filename="test/support/example.bin", size=16)
    assert_equals("529D656A8BC413FEF58DA82E1BF0308DCFE0429DCD80687E69C94633", hashit.next_chunk())
    assert_equals("0E97EA1BD23A0A7CB12CD3B7ECB9A60D6025C8CE105924279833CE85", hashit.next_chunk())
    assert_equals("39E8EB9A3607349FC39A33C5AC6E326CF863AF32E5424F9FAD1B8584", hashit.next_chunk())
    assert_equals("5371E71E799E41C70DE23DA40E283A4A997FBCD2A7B09F9CA91FA836", hashit.next_chunk())
    assert_equals("A0C92632278202BE93F9815D4939A7ECA76E690B3A86C22B10AC154B", hashit.next_chunk())
    assert_equals("FC74DD0B5078C8D1466F85C51B1EDF0DC65FF308035FD32113B83155", hashit.next_chunk())
    assert_equals("E3A6ACADFEF1A97FF76E813F3C9F8ABD8498BDE28C8D295B5F315EBD", hashit.next_chunk())
    assert_equals("F688C227166F7B837FA4C3AB010C08AF8C98FAFE61CB066D72B9B205", hashit.next_chunk())


def test_hash_it_sha256():
    assert_equals("40AFF2E9D2D8922E47AFD4648E6967497158785FBD1DA870E7110266BF944880",
                  HashIt().hash_it(HashType.SHA256, "test/support/example.bin"))


def test_hash_it_sha256_chunked():
    hashit = HashIt(hash_type=HashType.SHA256, filename="test/support/example.bin", size=16)
    assert_equals("BE45CB2605BF36BEBDE684841A28F0FD43C69850A3DCE5FEDBA69928EE3A8991", hashit.next_chunk())
    assert_equals("FC2E2C73072BFA2BDA03FF9307472DEBD3CC8105028A8A9E235E35BA8D2E37F4", hashit.next_chunk())
    assert_equals("36DB1ADC807AC50E4C85BD86A174B4AA260154E4F172A3659698945D7B16D084", hashit.next_chunk())
    assert_equals("816B9E7C25D559C5766755B3BBB36654AD451E080FFA93694A793D6EED41F40A", hashit.next_chunk())
    assert_equals("BA22B7DC95F6CC8765757BE4BCCF37CD92ECE6D4987DC26A31E274C9BE236921", hashit.next_chunk())
    assert_equals("372AFEFA6BCD01BE7504CFE132D4CDB5151ED08DE35825772BDECAB4C4EB6FBC", hashit.next_chunk())
    assert_equals("2ED1BAD92452DF6752AC09877A37FC86EC876010FAA7D80765BD5131FB8E0226", hashit.next_chunk())
    assert_equals("FBD8C6B1CD3C16E5A21471CD88E33224C138BDCD856586F752C28BEDADC181FD", hashit.next_chunk())
