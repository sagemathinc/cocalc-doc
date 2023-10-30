.. index:: AWS command-line
.. _install-awscli:

Install AWS CLI
=====================

Here is how you can install AWS command-line utility in a CoCalc project.
The main idea is to unpack the distribution in your project and tell the installation script to put it into your project.

This works for any kind of utility, which comes pre-packaged and can be installed in your ``$HOME``-directory.

.. code:: bash

    cd                     # make sure you're in your $HOME directory
    mkdir awscli           # where it will end up
    cd awscli/
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    ./aws/install -i ~/awscli -b ~/bin            # the installation
    rm -rf aws awscliv2.zip                       # remove temporary files


What remains are installation artifacts in ``~/awscli`` and a symlink from your ``~/bin`` directory to the entry point where it has been installed. Confirm this by running ``which aws``.

With that, you can run

.. code:: bash

    $ aws --version gives

    aws-cli/2.13.28 Python/3.11.6 Linux/5.15.0-1038-gcp exe/x86_64.ubuntu.22 prompt/off

Ref: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html