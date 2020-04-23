.. index:: Sharing files
.. index:: Publishing files
.. _sharing-files:

==========================
Sharing Files
==========================

Use sharing to make a file or directory publicly visible to the world.

Publishing Files
==================

You can make individual files and folders public.
First, do either of the following:

* With the file open, click the lock icon |lock| at upper right. Note: if you see the bullhorn icon |bullhorn| instead of the lock, that means your file is already shared; you could click it to change sharing settings.

.. figure:: img/icons/lock.png
     :width: 50%
     :align: center

     *click lock icon to enter file-sharing dialog*

.. figure:: img/icons/bullhorn.png
     :width: 50%
     :align: center

     *lock is replaced by bullhorn if file is already shared*

* In the Files listing for your project, check the box in the leftmost column for your file, and click |square| Share. You can also select more than one file in order to share them together (e.g. an HTML page that includes images)

.. |info| image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/16/info-circle.png
.. |square| image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/16/share-square-o.png
.. |lock| image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/16/lock.png
.. |bullhorn| image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/16/bullhorn.png

After either of these steps, you can see the "Share" dialog.
You may enter a description for the file being shared,
then click ``Make item public`` and your file is shared.

.. image:: img/share-dialog.png
     :width: 100%
     :align: center

.. index:: Sharing files; share server

Using the Share Server
==========================

After clicking ``Make item public`` as above, the **public URL** will be displayed under ``Shared publicly``.
You can click the |external| button to open it at the share server.

.. |external|
    image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/128/external-link.png
    :width: 16px

With that link, your file is available read-only on the CoCalc lightweight `share server`_.
A CoCalc login is not needed to access files on the share server.
Files on the share server are `indexed by Google <https://www.google.com/search?q=site%3Acocalc.com%2Fshare>`_ unless you click the checkbox next to "Unlisted: Only allow those with a link to view this.".

.. index:: Sharing files; direct from project

File-sharing Tips
======================

* If your document depends on auxiliary files (e.g., images embedded in a markdown file) make sure these auxiliary files are also published. A convenient way to do this is to have auxiliary files in a common folder and share that folder.

* Serving raw files: you can host arbitrary html, etc. through the share server. Files can be viewed in "raw" form, i.e. without CoCalc controls, by opening in the share server and clicking "Raw" at upper right, or by removing the parameter setting ``?viewer=share`` from the share server URL for the file.

* Interactive elements that use server processes, such as notebooks with Jupyter widgets and worksheets with Sage ``@interact``, will not operate in files viewed from the share server. That is because documents on the share server are truly static. There is no kernel or Sage server running in the background to facilitate any sort of interactive computing. Controls that run completely in the browser, for example in 3d plots like `this cardiod <https://share.cocalc.com/share/7eee8ccdeb4acf37e6c258df1cd973871373df05/Public/hearts.ipynb?viewer=share>`_, will work when served from the share server.


.. note::

    If you would like to collaborate and chat with other people on documents in your project,
    go the :doc:`project-settings` tab and ":ref:`Add people to project <add-collaborators>`".

.. _share server: https://share.cocalc.com/share/