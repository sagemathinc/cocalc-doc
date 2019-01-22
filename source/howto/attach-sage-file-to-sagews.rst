.. index:: Attach Sage Files

===========================================
Attach Sage files to Sage Worksheets
===========================================

**Is there a way to write functions in one worksheet, and then important them to another and use them there?**

Not exactly, but you can write code in a ``.sage`` file and then load it into another :doc:`../sagews` as illustrated at
https://cocalc.com/share/4a5f0542-5873-4eed-a85c-a18c706e8bcd/support/2018-06-12-sage-code/?viewer=share

#. Put code in a new file with extension ``.sage``, e.g. ``code.sage``
#. In a Sage worksheet or the terminal, run this: ``%attach code.sage`` or ``attach("code.sage")``
#. Now all code in ``code.sage`` is available in your worksheet, and whenever it changes, it will get reloaded automatically.
#. If you're using Jupyter, this is all broken (see https://github.com/sagemathinc/cocalc/issues/2916), but at least you can use ``load("code.sage")`` instead.