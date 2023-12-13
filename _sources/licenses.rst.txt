.. index:: Licenses; general information
.. _license-info:

===============
Licenses
===============

CoCalc licenses allow you to flexibly acquire resources for your projects. Not sure what you need and how much? No problem! You can easily edit your license at any time and either pay the difference if you need more or get a prorated credit to your account if you need less. So make an educated guess and go ahead - there are no penalties for later adjustments!


Maximum Number of Simultaneously Upgraded Projects
---------------------------------------------------

You can apply a license to any number of projects. These projects are upgraded as they start, until the maximum number of concurrent running projects for the license is reached. Any project with the same license that starts while the maximum concurrent number is running will be started without upgrades from that license. When a project using a license stops, its upgrades are released and can be used by the next  project to start that is configured for that license.

For example, if you have ten personal projects but plan to *actively work* only with one project at a time, it makes sense to buy a license with "Run limit" set to 1, apply it to *all your projects*, and then remember to stop a previous project when you need to switch to another one.


Buy and Apply a License
-------------------------

To buy a license, or to just get pricing information, `visit our store <https://cocalc.com/store/site-license>`_.

Then you need to :ref:`add your license to a project <project-add-license>` or, if you are running a course, :ref:`install your license in the course file <install-course-license>`.


.. _manage-licenses:

Manage Licenses
---------------------------------------------------

See https://cocalc.com/licenses for information about your licenses and licensed projects, including the following (note that each topic has its own dedicated URL):

* `licenses you manage <https://cocalc.com/settings/licenses>`_ here you can click on any license to see all details and reveal the "Edit License..." button, please note that you can only edit licenses that *you* have purchased
* `licensed projects you collaborate on <https://cocalc.com/licenses/projects>`_
* `how a specific license is being used <https://cocalc.com/licenses/how-used>`_
* `subscriptions <https://cocalc.com/settings/subscriptions>`_


.. _license-errors:

License Error Messages
------------------------

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