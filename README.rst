python-twofish
==============

A fork of keybase/python-twofish_ migrated to Python 3.11+.

Bindings for the Twofish implementation by Niels Ferguson libtwofish-dev_.

The library performs a self-test at each import.

.. _python-twofish: https://github.com/keybase/python-twofish
.. _libtwofish-dev: http://packages.debian.org/sid/libtwofish-dev

Installation
------------

Install from the repository::

  git clone https://github.com/nicolayreptile/python-twofish.git
  cd python-twofish
  pip install .

Usage
-----

Create a ``twofish.Twofish`` instance with a key of length ]0, 32] and then use the ``encrypt`` and ``decrypt`` methods on 16 bytes blocks.

All values must be ``bytes``.

**[WARNING]** this should be used in a sensible cipher mode, like CTR or CBC. If you don't know what this means, you should probably use a higher level library.

Example
-------

>>> from twofish import Twofish
>>> T = Twofish(b'*secret*')
>>> x = T.encrypt(b'YELLOWSUBMARINES')
>>> print(T.decrypt(x).decode())
YELLOWSUBMARINES
