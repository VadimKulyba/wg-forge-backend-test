#!/usr/bin/env python3
import setuptools

VERSION = '0.1'


REQUIREMENTS = [
]


DEV_REQUIREMENTS = [
]


setuptools.setup(
    name='wg-forge-backend-test',
    author="Vadim Kulyba",
    author_email="kulyba.vadim@gmail.com",
    url="https://github.com/VadimKulyba/wg-forge-backend-test",
    version=VERSION,
    install_requires=REQUIREMENTS,
    extras_require={'dev': DEV_REQUIREMENTS},
)
