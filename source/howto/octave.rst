.. index:: Octave


============================================================
Octave Images and Plots
============================================================

`GNU Octave <https://octave.org/>`_ is a scientific programming language that provides drop-in compatibility with many Matlab scripts.

Octave can create graphics images. Here are two ways to do that:

#####################################
Octave with Jupyter Kernel
#####################################

If you select the Octave Jupyter kernel, you will be able to view Octave plots in a Jupyter notebook. The first time `plot` is run in a cell, there is a warning about the gnuplot graphics toolkit. Just clear the cell output and run the cell again. Note that CoCalc support for Octave in Jupyter is limited at this time. Some dependent packages may fail to load.

.. image:: img/octave-jupyter.png
     :width: 90%
     :align: center
     :alt: octave in a jupyter notebook


#####################################
Octave with X11 Desktop
#####################################

You can run Octave in the terminal in the :doc:`X11 Graphical Desktop <../x11>`. Do: +New --> Graphical Desktop, then type "octave" in the terminal in the upper left or click the "Octave" button at lower left. It can take a few seconds for the X11 server to start the first time.

Whe Octave opens at the right, select your file under the File browser and run it from there. Your plot should appear to the right in a new tab, e.g. "Figure "

.. image:: img/octave-x11.png
     :width: 100%
     :align: center
     :alt: octave with the CoCalc X11 server

