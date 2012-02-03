#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
import pygithub3

setup(
    name='python-github3',
    version=pygithub3.__version__,
    author='David Medina',
    author_email='davidmedina9@gmail.com',
    url='https://github.com/copitux/python-github3',
    description='Python wrapper for the github v3 api',
    long_description=open('README.rst').read(),
    license='ISC',
    packages=find_packages(),
    install_requires=map(str.strip, open('requirements.txt')),
    package_data={'': ['README.rst', 'AUTHORS.rst', 'LICENSE']},
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
    ),
)
