"""
===============
YNAB Downloader
===============
"""
from os import environ
from distutils.core import setup

__version__ = "0.1.0"


def install_requires():
    """Check for required packages"""
    skip_install_requires = environ.get('SKIP_INSTALL_REQUIRES')
    if not skip_install_requires:
        with open('requirements.pip') as r:
            return r.readlines()
    return []


setup(
    author = "Glen Zangirolami",
    author_email = "glenbot@gmail.com",
    description = "ynab_downloader",
    long_description = __doc__,
    fullname = "ynab_downloader",
    name = "ynab_downloader",
    url = "https://github.com/glenbot/ynab_downloader",
    download_url = "https://github.com/glenbot/ynab_downloader",
    version = __version__,
    platforms = ["Linux"],
    packages = [
        "ynab_downloader",
        "ynab_downloader.bin",
    ],
    install_requires = install_requires(),
    entry_points = {
        'console_scripts': [
            "ynab-downloader = ynab_downloader.bin.download:main"
        ]
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Server Environment",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python",
    ]
)
