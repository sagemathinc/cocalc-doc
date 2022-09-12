======================================
Add Capacity to an Existing License
======================================

You may want to increase the amount of resources provided with an existing CoCalc license. Possible situations include:

* exceeding expected utilization on an individual project
* an expected short-term increase in use, for example during exam week with a course

The approaches discussed below are also applicable if you already have more than one license applied to a project or course.

There are two solutions, depending on what resources need to be increased.

.. contents::
     :local:
     :depth: 1

#################
Boost Licenses
#################

If all you need is an increase in CPU, RAM, or disk capacity, a boost license will cost significantly less than buying an additional ordinary license. To buy a boost license, use the self-service form at https://cocalc.com/store/boost.

*Boost licenses cannot be used to add to the run limit or idle timeout of an existing license, or to add member hosting to a license that does not already have it.*

Example: you have a course configured with a "Student" quota license and you want to add 2 GB of RAM to all student projects. Do the following:

#. Browse to https://cocalc.com/store/boost.
#. Select the Start and End Dates you need for the boost.
#. Under "Select license", select the existing license you would like to boost. This step ensures compatibility between your existing license and the boost license you're about to buy.
#. Select 2 G RAM.

    .. figure:: img/boost-add-2GB.png
         :width: 80%
         :align: center
         :alt: 2GB RAM boost

         adding 2 GB of RAM in boost dialog

#. After buying the license, open the course file and select the Configuration tab. Add the new boost license to the course.
#. Under License strategy, select "Maximize upgrades to each project".
#. The increase in capacity will happen in each student project the next time that project is (re)started. 

#################
Stacked Licenses
#################

For any other capacity increase, buy an additional ordinary license for only the capacity you want to add. When adding capacity to a course, be sure to select the appropriate :ref:`license strategy <license-strategy>`.

Example: you have a course configured with a "Student" quota license and you want to add 3 more students. Do the following:

#. Browse to https://cocalc.com/store/site-license.
#. Select the Start and End Dates needed.
#. Set run limit to 3 because you are adding 3 students.
#. Choose the "Student" quota preset. In general, you want to match all the parameters other than dates and run limit to your existing license.
#. After buying the license, open the course file and select the Configuration tab. Add the new license to the course.
#. Under License strategy, select "Maximize number of covered students".
#. In the course file under the Students tab, add email addresses for the student accounts to be added.
#. The increase in capacity will happen in each student project the next time that project is (re)started. It may also be necessary to open the course Configuration tab and click "Reconfigure all projects" at lower right.

