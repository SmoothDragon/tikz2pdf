#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tikz2pdf',
    version='0.1.0',
    description="Command line utility to make standalone PDF files from TikZ code.",
    long_description=readme + '\n\n' + history,
    author="Thomas Draper",
    author_email='draper@idaccr.org',
    url='https://github.com/SmoothDragon/tikz2pdf',
    packages=[
        'tikz2pdf',
    ],
    package_dir={'tikz2pdf':
                 'tikz2pdf'},
    scripts=['bin/tikz2pdf'],
    include_package_data=True,
    install_requires=requirements,
    license="GPL",
    zip_safe=False,
    keywords='tikz2pdf',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License (v3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
