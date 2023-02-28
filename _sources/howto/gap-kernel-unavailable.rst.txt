.. index:: GAP; jupyter kernel unavailable

.. _gap-kernel-unavailable:

=================================
GAP Jupyter kernel not available
=================================

For persons wanting to use `GAP - Groups, Algorithms, Programming <https://www.gap-system.org/>`_, note that there is a `long-standing bug <https://github.com/sagemathinc/cocalc/issues/1706>`_. For that reason, we removed the GAP Jupyter kernel from CoCalc.

As a workaround, you can work with GAP in a :doc:`Sage worksheet <../sagews>` (file in CoCalc ending in .sagews). Start that file in a single block of code with::

    %auto
    %default_mode gap

and then run it via shift-return. At this point, you are working with GAP in Sage.



