#!/usr/bin/env python
"""
Virtual env manager
===================

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
]

install_requires = [
    'Django>=1.2',
    'South>=0.7',
    'Fabric==1.3.3',
]

setup(
    name='virtualenv-manager',
    version='0.0.1',
    author='Xavier Ordoquy',
    author_email='xordoquy@linovia.com',
    url='http://github.com/linovia/django-virtualenv-manager',
    description='A virtualenv manager application.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests', 'demo']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    license='BSD',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: System :: Installation/Setup'
    ],
)
