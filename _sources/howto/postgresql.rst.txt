.. index:: PostgreSQL

===============================
PostgreSQL Server
===============================


You can easily run your own `PostgreSQL`_ server inside any CoCalc project to manage data (or just learn about SQL and databases).

.. _PostgreSQL: https://www.postgresql.org/

Step 1: Setup
==================

(only needed once)

In a :doc:`../terminal` (Files tab → ``+ Create`` → ``Terminal``), paste this::

    cd
    pg_ctl initdb -D postgres_data
    echo "unix_socket_directories = '$HOME/postgres_data'" >> postgres_data/postgresql.conf
    echo "unix_socket_permissions = 0700" >> postgres_data/postgresql.conf

The ``postgres_data`` subdirectory is where the data files and the communication socket are stored.

The ``unix_socket_*`` settings make sure that local communication with the database runs through the files in your own project.

The ``*_permissions`` setting disables reading and writing for anyone else.
This isn't necessary because CoCalc uses a Docker container for each project,
so there are no other users to worry about.

Step 2: Start Server
======================

Again in the Terminal::

    pg_ctl -D postgres_data -l logfile -o "-h ''" start

This command starts the PostgreSQL server listening on a Unix domain socket and not on an IP address and port number.
To check the status, either run ``cat logfile`` to see the logfile's content or run


::

    pg_ctl -D postgres_data status

**Tip**: you can add the 'pg_ctl...start' line at the bottom of your ``~/.bashrc`` file.

Step 3: Connect to the database
==================================

::

    export PGHOST="$HOME/postgres_data"
    createdb test
    psql test

Output::

    psql (9.6.1)
    Type "help" for help.

    test=#

and now you're off to the races!

::

    test=# create table people (name varchar, age int);
    CREATE TABLE
    test=# insert into people values ('joe', 10), ('fred', 20);
    INSERT 0 2
    test=# select * from people;
     name | age
    ------+-----
     joe  |  10
     fred |  20
    (2 rows)
    test=# \q


You can also use PostgreSQL from Python (e.g., a Sage worksheet, Jupyter notebook, script, etc.) like so::

    import psycopg2
    conn = psycopg2.connect("dbname='test' host=/home/user/postgres_data")
    cur = conn.cursor()
    cur.execute("SELECT * FROM people")
    rows = cur.fetchall()
    print("\nShow me the databases:\n")
    for row in rows:
        print("   ", row[0])

See https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

.. note::

    With this setup, you will not have the usual worries about passwords and users,
    because the database is not accessible from outside your project.

Step 4: Shutting Down
==================================

After you have finished working with PostgreSQL, the following step prevents data loss::

    pg_ctl -D postgres_data stop

