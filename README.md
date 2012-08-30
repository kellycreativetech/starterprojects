Original README

django-skel
===========

A modern Django project skeleton, originally based on rdegges work.

Develop
=======

Setup:

    #Assumes you are in the starter-0 directory
    mkvirtualenv starter-0
    pip install -r requirements.txt


In order to try this out you need to make a concrete project from this template.
If something's not right in the new project you have to do it again::

    make
    make clean && make
    # open http://localhost:8000 to look


Install
=======

django-skel currently supports Django 1.4. To create a new django-skel base
project, run the following command (this assumes you have Django 1.4 installed
already):

    $ django-admin.py startproject --template=https://github.com/kellycreativetech//zipball/master woot
    $ heroku config:add DJANGO_SETTINGS_MODULE=myproject.settings.prod

Where ``woot`` is the name of the project you'd like to create.

This is possible because Django 1.4's ``startproject`` command allows you to
fetch a project template over HTTP (which is what we're doing here).
