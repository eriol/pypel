# -*- coding: utf-8 -*-
"""pypel setup file.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2012 Daniele Tricoli <eriol@mornie.org>

Read LICENSE for more informations.
"""

import distutils.core

from pypel import get_version

classifiers = '''
Development Status :: 3 - Alpha
Environment :: Console
Intended Audience :: End Users/Desktop
License :: OSI Approved :: BSD License
Operating System :: POSIX
Programming Language :: Python
Programming Language :: Python :: 2
Topic :: Office/Business :: Financial
'''.strip().splitlines()

distutils.core.setup(
    name = 'pypel',
    version = get_version(),
    license = 'BSD',
    description = 'simple tool to manage receipts',
    #long_description = ,
    classifiers = classifiers,
    url = 'http://mornie.org/projects/pypel/',
    author = 'Daniele Tricoli',
    author_email = 'eriol@mornie.org',
    packages = ['pypel'],
    package_dir = dict(pypel='pypel'),
    scripts = ['bin/pypel']
)