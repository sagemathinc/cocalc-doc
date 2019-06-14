.. index:: Ruby

.. _ruby:

Ruby Programming
=========================

There are several ways to run Ruby in CoCalc:


Ruby files in the frame editor
-------------------------------

You can create Ruby programs in the :doc:`../frame-editor`.

Create a file ending in .rb by clicking "+New", then typing in a filename ending in .rb. You'll get syntax highlighting, indentation, code folding, etc.
To run the program, open a :doc:`terminal <../terminal>` and type ``ruby filename.rb``.
You can get a terminal by either splitting your .rb edit session and selecting Terminal at upper right in one of the frames of the split (see screenshot), or starting a new .term file.

.. figure:: img/ruby-fe.png
     :width: 85%
     :align: center

     editing and running Ruby from the frame editor

Ruby code in a Sage worksheet
-------------------------------
Create a Sage worksheet, then type ``%ruby`` at the beginning a cell.
You can then put Ruby code in the cell, and it will be evaluated when you hit shift+enter.

Or...

Type ``%default_mode ruby`` in a Sage worksheet and execute that cell. The rest of the worksheet uses Ruby.


