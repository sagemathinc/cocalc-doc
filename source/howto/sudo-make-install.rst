.. index:: Install compiled software
.. _sudo-make-install:

==================================================
Install compiled software
==================================================

By default, it is not possible to install any software globally via ``sudo`` or other mechanisms.

However, standard `GNU Make <https://www.gnu.org/software/make/>`_ (and other) build frameworks allow to customize the install target,
by setting a ``prefix`` for the ``bin``, ``lib``, ``share``, … directories.

This means, modifying instructions like this::

    $ ./configure
    $ make
    $ sudo make install


to be similar to the following::

    $ ./configure --prefix=$HOME/.local
    $ make
    $ make install

should work!

Then, the compiled software will end up in your ``~/.local`` directory, i.e. binaries will be in ``~/.local/bin/…`` and hence be in your ``$PATH``.

