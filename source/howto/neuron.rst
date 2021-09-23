.. index:: NEURON

.. _howto-neuron:

NEURON simulation environment
===============================

From `their website <https://www.neuron.yale.edu/neuron/>`_:

    The NEURON simulation environment is used in laboratories and classrooms around the world
    for building and using computational models of neurons and networks of neurons.

In order to work with it on CoCalc, you need to add a bit of setup code.


Jupyter Notebook
--------------------------

To use NEURON in a :doc:`../jupyter`, we have to delete the ``$DISPLAY`` variable and add it to the ``PYTHONPATH``::

    import os
    if 'DISPLAY' in os.environ:
        del os.environ['DISPLAY']
    import sys
    sys.path.insert(0, '/usr/local/nrn/lib/python/')

Only then import ``h``::

    from neuron import h, __version__
    __version__

If it doesn't work, restart the kernel and run the first cell again and then import ``h``.
If there is still a problem, please `contact us <mailto:help@cocalc.com>`_.


Example worksheet: `neron-yale.ipynb <https://cocalc.com/share/public_paths/dd2c8e5f6f062e1b0475158e7332e3a371be35c8>`_.

.. image:: img/neuron-jupyter.png
    :width: 75%
    :align: center

Graphical Application
---------------------------

CoCalc supports :doc:`graphical applications <../x11>`, but there are limits to how it works with NEURON.
Open up ``X11`` file to start such a virtual desktop environment,
and then run ``nrngui``.

