#!/usr/bin/env python
import sys

def howto_install_setuptools():
    print("""Error: You need setuptools Python package!

It's very easy to install it, just type (as root on Linux):
   wget http://peak.telecommunity.com/dist/ez_setup.py
   python ez_setup.py
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
 
params.update( {
    'name': 'pysnmp',
    'version': '4.2.3',
    'description': 'SNMP framework',
    'author': 'Ilya Etingof',
    'author_email': 'ilya@glas.net',
    'url': 'http://sourceforge.net/projects/pysnmp/',
    'classifiers': [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Intended Audience :: Telecommunications Industry',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Topic :: Security',
      'Topic :: Communications',
      'Topic :: System :: Monitoring',
      'Topic :: System :: Networking :: Monitoring',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'License :: OSI Approved :: BSD License'
    ],    
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
