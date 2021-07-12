# HashIt

[![Build Status](https://travis-ci.org/art-of-dom/hash-it.svg?branch=master)](https://travis-ci.org/art-of-dom/hash-it)
[![CodeFactor](https://www.codefactor.io/repository/github/art-of-dom/hash-it/badge)](https://www.codefactor.io/repository/github/art-of-dom/hash-it)
[![BCH compliance](https://bettercodehub.com/edge/badge/art-of-dom/hash-it?branch=master)](https://bettercodehub.com/)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gh/art-of-dom/hash-it/?ref=repository-badge)

All file hashing, all the time.

## Dev Set up

Being a python project the assumption is that you have it already installed
along with some way to set up a development environment. For the rest of this we
will be using virtualenv.

From the clone all you need to do is the following:

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Can be used to give a quick hash of a file, for example running against our
support test file like so will yield:

```shell
python -m hashit -f test/support/example.bin --hash-type=CRC32
# input: test/support/example.bin hash: 29058C73
```

Can also be given an ASCII character string. Running against the input
'123456789' will yield the following.

```shell
python -m hashit -a 123456789 --hash-type=CRC32
# input: 123456789 hash: CBF43926
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
- [x] ASCII and Hex inputs
- [x] Brute force verification
- [x] Reverse input
- [x] Pipe data to hash-it
- [x] Data generation based on hash
- [x] Data generation depth

## State of the repo

This project started as just a quick how to hash for data integrity in python.
It is a long way from being usable, but feel free to hack around.
