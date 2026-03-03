"""
This file is part of Python Twofish
a Python bridge to the C Twofish library by Niels Ferguson

Released under The BSD 3-Clause License
Copyright (c) 2013 Keybase

setup.py - build and package info (C extension; project metadata in pyproject.toml)
"""

from setuptools import setup, Extension

twofish_module = Extension(
    '_twofish',
    sources=['twofish-0.3/twofish.c', 'twofish.c'],
    include_dirs=['twofish-0.3'],
)

setup(py_modules=['twofish'], ext_modules=[twofish_module])
