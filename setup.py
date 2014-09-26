#!/usr/bin/env python

from distutils.core import setup

setup(name='python-gamerscoinrpc',
      version='0.1',
      description='Enhanced version of python-jsonrpc for use with gamerscoin',
      long_description=open('README').read(),
      author='Jeff Garzik',
      author_email='<jgarzik@exmulti.com>',
      maintainer='Jeff Garzik',
      maintainer_email='<jgarzik@exmulti.com>',
      url='https://github.com/johngame/python-gamerscoinrpc',
      packages=['gamerscoinrpc'],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])
