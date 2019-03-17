#!/usr/bin/env python3
import setuptools

VERSION = '0.1'


REQUIREMENTS = [
    'flasgger==0.9.2',
    'flask==1.0.2',
    'flask-limiter==1.0.1'
    'flask-migrate==2.4.0',
    'flask-script==2.0.6',
    'flask-sqlalchemy==2.3.2',
    'gunicorn==19.9.0',
    'psycopg2-binary==2.7.7',
    'scipy==1.2.1'
]


DEV_REQUIREMENTS = [
    'flake8==3.7.7',
    'ipython==7.3.0',
]


setuptools.setup(
    name='wg-forge-backend-test',
    author="Vadim Kulyba",
    author_email="kulyba.vadim@gmail.com",
    url="https://github.com/VadimKulyba/wg-forge-backend-test",
    version=VERSION,
    install_requires=REQUIREMENTS,
    extras_require={'dev': DEV_REQUIREMENTS},
    entry_points={
        'console_scripts': [
            'prepare_db=wg_forge_backend_test.helpers:prepare_db',
        ]
    },
)
