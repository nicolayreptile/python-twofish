python-twofish
==============

Bindings for the Twofish implementation by Niels Ferguson libtwofish-dev_.

Compatible with Python 3.11+.

The library performs a self-test at each import.

.. _libtwofish-dev: http://packages.debian.org/sid/libtwofish-dev

Installation
------------

::

  pip install twofish

Usage
-----

Create a ``twofish.Twofish`` instance with a key of length ]0, 32] and then use the ``encrypt`` and ``decrypt`` methods on 16 bytes blocks.

All values must be ``bytes``.

**[WARNING]** this should be used in a senseful cipher mode, like CTR or CBC. If you don't know what this mean, you should probably usa a higher level library.

Example
-------

>>> from twofish import Twofish
>>> T = Twofish(b'*secret*')
>>> x = T.encrypt(b'YELLOWSUBMARINES')
>>> print(T.decrypt(x).decode())
YELLOWSUBMARINES
