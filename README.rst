Django Virtual environment Manager
==================================

This is a small application that will help maintain the various virtualenv used on different servers.

The goal is to ease the maintainance and quickly see what needs to be upgraded.

This has been created after I needed to upgrade several Django instances on different servers and at different places.
The application is able to summarize the package usage for several python environments.
It is planned to allow upgrades from it too.


Requirements
------------

* pip should be installed on the destination hosts.
* You should have access with an authorized key on the destination hosts.

Usage
-----

You are strongly adviced to create a virtualenv before installing that application.
Please refer to http://pypi.python.org/pypi/virtualenv for more informations.
We'll assume you are in an environment where you can install packages.

    
    git clone git://github.com/linovia/django-virtualenv-manager.git
    cd django-virtualenv-manager
    python setup.py develop
    cd demo
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver


Now you can point your browser to http://localhost:8000/admin/ and login with
the user you just created.

* Create your servers (http://localhost:8000/admin/venvmanager/server/add/)
* Create your virtual environments (http://localhost:8000/admin/venvmanager/virtualenv/add/)
* Go on the virtual env. list (http://localhost:8000/admin/venvmanager/virtualenv/),
select one or many and choose the "Update the virtualenv" action.
* Now go to the version list () and enjoy the centralized informations.


TODO
----

* Create a front design instead of using the Django's admin
* Exports CSV
* Create usage summaries (what server / virtual env uses a given package version, what versions of that package are used in all the environments...).
* Allow remote upgrades.

