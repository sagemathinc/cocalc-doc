.. index:: Assembly language; gnu/gas, nasm

.. _assembly-language:


=======================================
Assembly Language Programming
=======================================

You can use your CoCalc account to learn assembly language.

Both `GNU assembler <https://sourceware.org/binutils/docs/as/>`_ and `Netwide assembler <https://www.nasm.us/>`_ (``nasm``) are available on CoCalc.com. To run assembler programs on CoCalc.com, use instructions for 64-bit Linux, as shown in the examples.

To get started with either assembler, create a source file with the :doc:`frame editor <../frame-editor>`. You can then split the editor tab (as shown in the frame editor docs), and open a :doc:`terminal <../terminal>` in one of the tabs. Run the commands below in the terminal to assemble, link, and run your programs.


GNU assembler
=============

For a tutorial on using the GNU assembler with Linux, see Ray Toal's `GNU Assembler Examples <https://cs.lmu.edu/~ray/notes/gasexamples/>`_.
Here is a link to `the first example from the GNU assembler tutorial <https://cocalc.com/share/public_paths/0481f92026c39a2a9cd1ae35123f702ae7b662eb>`_ on the CoCalc share server.

Here is a one-line command to assemble, link, and execute a GNU assembler program called ``hello.s``::

    gcc -c hello.s && ld hello.o && ./a.out

Netwide assembler
=================

For a tutorial on using the Netwide assembler with Linux, see Ray Toal's `NASM Tutorial <https://cs.lmu.edu/~ray/notes/nasmtutorial/>`_.
Here is a link to `the first example from the nasm tutorial <https://cocalc.com/share/public_paths/dd3d211ef8d16dff2a6407ab00fc572fbe2653e2>`_ on the CoCalc share server.


Here is a one-line command to assemble, link, and execute a NASM program called ``hello.asm``::

    nasm -felf64 hello.asm && ld hello.o && ./a.out
