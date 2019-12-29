# HashIt

[![Build Status](https://travis-ci.org/art-of-dom/hash-it.svg?branch=master)](https://travis-ci.org/art-of-dom/hash-it)
[![CodeFactor](https://www.codefactor.io/repository/github/art-of-dom/hash-it/badge)](https://www.codefactor.io/repository/github/art-of-dom/hash-it)
[![BCH compliance](https://bettercodehub.com/edge/badge/art-of-dom/hash-it?branch=master)](https://bettercodehub.com/)

All file hashing, all the time.

## Usage

Can be used to give a quick hash of a file, for example running against our
support test file like so will yield:

```shell
python -m hashit -f test/support/example.bin --hash-type=CRC32
# file: test/support/example.bin hash: 29058C73
```

If you already have a hash, you can also verify the hash of the file. A
non-zero return is issued for this when the hash does not match. An example
with the test binary is below:

```shell
python -m hashit -f test/support/example.bin --hash-type=CRC32 --verify 29058C73
echo $? # return value is 0
```

The following will return a non zero value:

```shell
python -m hashit -f test/support/example.bin --hash-type=CRC32 --verify DEADBEEF
echo $? # return value is 2
```

## Milestones

- [x] Displaying File hashes
- [x] Verification return value
- [ ] Reverse input
- [ ] Pipe data or raw data instead of using a file
- [ ] Data generation based on hash
- [ ] Data generation depth
- [ ] Brute force verification

## State of the repo

This project started as just a quick how to hash for data integrity in python.
It is a long way from being usable
