#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-vior.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-vior.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-vior")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Electrum-VIOR",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'ltc_scrypt'],
    package_dir={
        'electrum_vior': 'lib',
        'electrum_vior_gui': 'gui',
        'electrum_vior_plugins': 'plugins',
    },
    scripts=['electrum-vior'],
    data_files=data_files,
    py_modules=[
        'electrum_vior.account',
        'electrum_vior.bitcoin',
        'electrum_vior.blockchain',
        'electrum_vior.bmp',
        'electrum_vior.commands',
        'electrum_vior.daemon',
        'electrum_vior.i18n',
        'electrum_vior.interface',
        'electrum_vior.mnemonic',
        'electrum_vior.msqr',
        'electrum_vior.network',
        'electrum_vior.plugins',
        'electrum_vior.pyqrnative',
        'electrum_vior.scrypt',
        'electrum_vior.simple_config',
        'electrum_vior.socks',
        'electrum_vior.synchronizer',
        'electrum_vior.transaction',
        'electrum_vior.util',
        'electrum_vior.verifier',
        'electrum_vior.version',
        'electrum_vior.wallet',
        'electrum_vior.wallet_bitkey',
        'electrum_vior_gui.gtk',
        'electrum_vior_gui.qt.__init__',
        'electrum_vior_gui.qt.amountedit',
        'electrum_vior_gui.qt.console',
        'electrum_vior_gui.qt.history_widget',
        'electrum_vior_gui.qt.icons_rc',
        'electrum_vior_gui.qt.installwizard',
        'electrum_vior_gui.qt.lite_window',
        'electrum_vior_gui.qt.main_window',
        'electrum_vior_gui.qt.network_dialog',
        'electrum_vior_gui.qt.password_dialog',
        'electrum_vior_gui.qt.qrcodewidget',
        'electrum_vior_gui.qt.receiving_widget',
        'electrum_vior_gui.qt.seed_dialog',
        'electrum_vior_gui.qt.transaction_dialog',
        'electrum_vior_gui.qt.util',
        'electrum_vior_gui.qt.version_getter',
        'electrum_vior_gui.stdio',
        'electrum_vior_gui.text',
        'electrum_vior_plugins.exchange_rate',
        'electrum_vior_plugins.labels',
        'electrum_vior_plugins.pointofsale',
        'electrum_vior_plugins.qrscanner',
        'electrum_vior_plugins.virtualkeyboard',
    ],
    description="Lightweight ViorCoin Wallet",
    author="ecdsa",
    author_email="ecdsa@github",
    license="GNU GPLv3",
    url="http://electrum-vior.org",
    long_description="""Lightweight ViorCoin Wallet"""
)
