#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(
    name='sinter_operator',
    version='0.0.1',
    description='Sinter Operator for Airflow',
    author='Fishtown Analytics',
    url='http://sinterdata.com.com',
    py_modules=['sinter_operator'],
    packages=['sinter_operator'],
    install_requires=[
        'requests>=2.18.0,<3',
    ],
)
