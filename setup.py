from setuptools import setup

import sys

setup(
    name='romfilter-flask',
    version='0.2.3',

    description='serves a rom filter website',
    long_description=open("README.md").read(),
    license='WTFPL',
    url='http://localhost/',
    download_url='http://localhost/',

    author='makefu',
    author_email='github.com@syntax-fehler.de',

    packages=['romfilter'],
    entry_points={ },
    install_requires= [ "Flask" ],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
