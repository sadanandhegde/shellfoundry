#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_file_content(file_name):
    with open(file_name) as f:
        return f.read()


setup(
    name='shellfoundry',
    version=get_file_content('version.txt'),
    description="shellfoundry - Quali tool for creating, building and installing CloudShell shells",
    long_description=get_file_content('README.rst') + '\n\n' + get_file_content('HISTORY.rst'),
    author="Boris Modylevsky",
    author_email='borismod@gmail.com',
    url='https://github.com/QualiSystems/shellfoundry',
    packages=[
        'shellfoundry',
    ],
    package_dir={'shellfoundry':
                     'shellfoundry'},
    include_package_data=True,
    install_requires=get_file_content('requirements.txt'),
    license="Apache 2.0",
    zip_safe=False,
    keywords='shellfoundry sandbox cloud virtualization vcenter cmp cloudshell quali command-line cli',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: Apache Software License",
    ],
    test_suite='tests',
    tests_require=get_file_content('test_requirements.txt')
)
