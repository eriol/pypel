Installing pypel
================

Dependencies
------------

``pypel`` requires `GExiv2 <https://wiki.gnome.org/Projects/gexiv2>`_
Python binding version 0.6.1 or superior and
`Six <http://pypi.python.org/pypi/six/>`_ version 1.3.0 or superior.

Optionally you can also install `Pygments <http://pygments.org/>`_ version 1.5
or superior (for console coloured output) and
`python-gnupg <https://pythonhosted.org/python-gnupg/>`_  version 0.3.0 or
superior (for signing and verifying receipts).

To run the testsuite you need `Pillow <https://python-pillow.github.io/>`_
version 2.0.0 or superior.

Installation
------------

Simply install ``pypel`` using ``pip``::

    $ pip install pypel

Alternatively you can directly install from the git repository using ``pip``.

For example, if you want to install version 0.3 from the git repository
you have to do::

    $ pip install -e git+https://github.com/eriol/pypel/@0.3#egg=pypel
