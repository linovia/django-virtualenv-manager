Django Virtual environment Manager
==================================

This is a small application that will help maintain the various virtualenv used on different servers.

The goal is to ease the maintainance and quickly see what needs to be upgraded.

This has been created after I needed to upgrade several Django instances on different servers and at different places.
The application is able to summarize the package usage for several python environments.
It is planned to allow upgrades from it too.

Requirements
------------

Fabric should be available where this application runs.
Also pip should be installed on the destination hosts.
You should have access with an authorized key on the destination hosts.


TODO
----

* Create a front design instead of using the Django's admin
* Exports CSV
* Create usage summaries (what server / virtual env uses a given package version, what versions of that package are used in all the environments...).
* Allow remote upgrades.

