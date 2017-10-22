import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="hash-it",
    version="0.0.1",
    author="Domenic Postorivo",
    author_email="depostorivo@gmail.com",
    description=("Simple file hashing so you don't have to."),
    license="MIT",
    keywords="hash file-integrity",
    url="https://github.com/art-of-dom/hash-it",
    packages=['hash-it'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
