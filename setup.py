#!/usr/bin/env python

from setuptools import setup, find_packages
from pathlib import Path

root_path = Path(__file__).parent

install_requires = [
    'nml>=0.7.4',
    'numpy>=2.0.0',
    'Pillow>=9.4.0',
    'ply==3.11',
    'typeguard>=4.1.5',
]

setup(
    name='grf',
    version=open(root_path / "VERSION").read().strip(),
    description='Framework for making OpenTTD NewGRF files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='dP',
    packages=find_packages(include=['grf', 'grf.*']),
    entry_points={
        'console_scripts': [
            'grftopy = grf.decompile:main',
        ]
    },
    install_requires=install_requires,
    python_requires=">=3.6.9",
    setup_requires=["setuptools-git-versioning<2"],
)
