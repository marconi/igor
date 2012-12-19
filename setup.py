#!/usr/bin/env python

import os
import sys
import igor

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist register upload')
    sys.exit()

packages = ['igor']
requires = ['fapws3==0.11.dev',
            'Fabric==1.5.1',
            'docopt==0.5.0',
            'Mako==0.7.3']

setup(
    name='igor',
    version=igor.__version__,
    packages=packages,
    license=open('LICENSE.txt').read(),
    description='A sort-of download proxy.',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author='Marconi Moreto',
    author_email='caketoad@gmail.com',
    url='https://github.com/marconi/igor',
    zip_safe=False,
    package_data={'': ['LICENSE.txt']},
    install_requires=requires,
    entry_points={
        'console_scripts': ['igor = igor.scripts:igor_cmd',
                            'igor_download = igor.scripts:igor_download']
    }
)
