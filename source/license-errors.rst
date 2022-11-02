.. index:: Licenses; error messages
.. _license-errors:

=======================
License error messages
=======================

Sometimes, adding a license to a project can result in an error, rather than resources being added. In such cases, if you open project Settings (wrench icon) and look under "Licenses" and then "status", you will see a word other than "active" displayed for the license status. In all cases, we make an effort to explain what is going on.

* exhausted - license run limit has already been reached by other projects using the license

* expired - license expiration date has occurred

* future - license start date has not yet occurred

* ineffective - there is another license active on this project that is not compatible with the license showing the error

You can see an expanded explanation by putting your cursor over the license status:

.. figure:: img/incompat-licenses.png
     :width: 60%
     :align: center
     :alt: pop-up status explaining incompatible licenses

     example: if two licenses are incompatible, only one can be active


.. note::

    If you are an instructor and it appears that your license has not been applied to a student project after the key has been entered in the course file "Configuration" tab, start the student project and wait for a moment to see if the license has been applied.

For more examples and images, see the `pull request for this feature <https://github.com/sagemathinc/cocalc/pull/6169>`_ in the CoCalc public source code repository.