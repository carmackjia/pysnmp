#!/usr/bin/env python
"""SNMP framework

   SNMP v1/v2c/v3 engine and apps written in pure-Python.
   Supports Manager/Agent/Proxy roles, scriptable MIBs,
   asynchronous operation and multiple transports.
"""
import sys

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Information Technology
Intended Audience :: System Administrators
Intended Audience :: Telecommunications Industry
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Communications
Topic :: Software Development :: Libraries :: Python Modules
Topic :: System :: Monitoring
Topic :: System :: Networking :: Monitoring
Topic :: Software Development :: Libraries :: Python Modules
"""

def howto_install_distribute():
    print("""
   Error: You need the distribute Python package!

   It's very easy to install it, just type (as root on Linux):

   wget http://python-distribute.org/distribute_setup.py
   python distribute_setup.py

   Then you could make eggs from this package.
""")

def howto_install_setuptools():
    print("""
   Error: You need setuptools Python package!

   It's very easy to install it, just type (as root on Linux):

   wget http://peak.telecommunity.com/dist/ez_setup.py
   python ez_setup.py

   Then you could make eggs from this package.
""")

try:
    from setuptools import setup
    params = {
        'install_requires': [ 'pyasn1>=0.1.2' ],
        'zip_safe': True
        }
    if sys.platform.lower()[:3] != 'win':
        params['install_requires'].append('pycrypto>=2.4.1')

except ImportError:
    for arg in sys.argv:
        if arg.find('egg') != -1:
            if sys.version_info[0] > 2:
                howto_install_distribute()
            else:
                howto_install_setuptools()
            sys.exit(1)
    from distutils.core import setup
    params = {}
    if sys.version_info[:2] > (2, 4):
        params['requires'] = [ 'pyasn1(>=0.1.2)' ]
        if sys.platform.lower()[:3] != 'win':
            params['requires'].append('pycrypto(>=2.4.1)')

if sys.platform.lower()[:3] == 'win':
    try:
        import Crypto
    except ImportError:
        sys.stderr.write("""WARNING! WARNING! WARNING!
PyCrypto binaries are required for SNMPv3 encryption to work.
You may wish to grab them from http://www.voidspace.org.uk/python/modules.shtml
and install into your system.
""")

doclines = [ x.strip() for x in __doc__.split('\n') if x ]
 
params.update( {
    'name': 'pysnmp',
    'version': open('pysnmp/__init__.py').read().split('\'')[1]+'rc7',
    'description': doclines[0],
    'long_description': ' '.join(doclines[1:]),
    'maintainer': 'Ilya Etingof <ilya@glas.net>',
    'author': 'Ilya Etingof',
    'author_email': 'ilya@glas.net',
    'url': 'http://sourceforge.net/projects/pysnmp/',
    'classifiers': [ x for x in classifiers.split('\n') if x ],
    'platforms': ['any'],
    'license': 'BSD',
    'packages': [ 'pysnmp',
                  'pysnmp.smi',
                  'pysnmp.smi.mibs',
                  'pysnmp.smi.mibs.instances',
                  'pysnmp.carrier',
                  'pysnmp.carrier.asynsock',
                  'pysnmp.carrier.asynsock.dgram',
                  'pysnmp.carrier.twisted',
                  'pysnmp.carrier.twisted.dgram',                   
                  'pysnmp.entity',
                  'pysnmp.entity.rfc3413',
                  'pysnmp.entity.rfc3413.oneliner',
                  'pysnmp.entity.rfc3413.twisted',
                  'pysnmp.proto',
                  'pysnmp.proto.mpmod',
                  'pysnmp.proto.secmod',
                  'pysnmp.proto.secmod.rfc3414',
                  'pysnmp.proto.secmod.rfc3414.auth',
                  'pysnmp.proto.secmod.rfc3414.priv',
                  'pysnmp.proto.secmod.rfc3826',
                  'pysnmp.proto.secmod.rfc3826.priv',
                  'pysnmp.proto.secmod.eso',
                  'pysnmp.proto.secmod.eso.priv',
                  'pysnmp.proto.acmod',
                  'pysnmp.proto.proxy',
                  'pysnmp.proto.api' ],
    'scripts': [ 'tools/libsmi2pysnmp', 'tools/build-pysnmp-mib' ]
    } )

setup(**params)
