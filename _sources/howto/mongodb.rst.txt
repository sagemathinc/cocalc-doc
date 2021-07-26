.. index:: MongoDB

===============================
MongoDB Server
===============================


You can easily run your own `MongoDB`_ server inside any CoCalc project to manage data (or just learn about NoSQL and databases).

.. _MongoDB: https://www.mongodb.com/

Step 1: Startup
==================

In a :doc:`../terminal` (Files tab → ``+ Create`` → ``Terminal``), paste this::

    cd
    mkdir -p mongodb-data
    mongod --dbpath mongodb-data

The directory ``~/mongodb-data`` will contain the data files.
It should greet you with ``waiting for connections on port 27017`` … which is where you have to point your client to (i.e. ``127.0.0.1:27017``)

Step 2: Connect
=================================

In a second terminal, maybe just split the one you already have, run this::

    mongo 127.0.0.1:27017


Step 3: Shutting Down
==================================

After you have finished working with MongoDB, send a term signal by pressing ``Ctrl + c`` keys in the Terminal where MongoDB is running in order to prevent data loss.

Screenshot
============================================

.. figure:: img/mongodb.png
     :width: 100%
     :align: center

