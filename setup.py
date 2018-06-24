#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (3, 4, 0):
    sys.exit("Error: Electron Cash requires Python version >= 3.4.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['commerciumelectro.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/commerciumelectro.png'])
    ]

setup(
    name="CommerciumElectro",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib-pelix',
        'PySocks>=1.6.6',
    ],
    packages=[
        'commerciumelectro',
        'commerciumelectro_gui',
        'commerciumelectro_gui.qt',
        'commerciumelectro_plugins',
        'commerciumelectro_plugins.audio_modem',
        'commerciumelectro_plugins.cosigner_pool',
        'commerciumelectro_plugins.email_requests',
        'commerciumelectro_plugins.hw_wallet',
        'commerciumelectro_plugins.keepkey',
        'commerciumelectro_plugins.labels',
        'commerciumelectro_plugins.ledger',
        'commerciumelectro_plugins.trezor',
        'commerciumelectro_plugins.digitalbitbox',
        'commerciumelectro_plugins.virtualkeyboard',
    ],
    package_dir={
        'commerciumelectro': 'lib',
        'commerciumelectro_gui': 'gui',
        'commerciumelectro_plugins': 'plugins',
    },
    package_data={
        'commerciumelectro': [
            'servers.json',
            'servers_testnet.json',
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['commerciumelectro'],
    data_files=data_files,
    description="Lightweight Bitcoin Cash Wallet",
    author="Jonald Fyookball",
    author_email="jonf@electroncash.org",
    license="MIT Licence",
    url="http://www.electroncash.org",
    long_description="""Lightweight Bitcoin Cash Wallet"""
)
