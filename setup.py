#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyque
from setuptools import setup, find_packages


## dependencies 
install_requires = [

]

packages = find_packages()

setup(
    name='pyque',
    version=pyque.__version__,
    author='Bernhard Maeser',
    author_email='bernhard.maeser@gmail.com',
    url='https://github.com/bmaeser/pyque',
    license="MIT",
    description="pythonic devops toolbelt",
    long_description=open('README.rst').read(),
    packages = packages,
    include_package_data=True,
    install_requires = install_requires,
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Systems Administration',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)