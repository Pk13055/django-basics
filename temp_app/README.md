# Django Dev

## Introduction

- To create a new project:
	`$ django-admin startproject mysite`

-  Project Structure
.
 * [manage.py](./manage.py)
 * [temp_app](./temp_app)
   * [__init__.py](./temp_app/__init__.py)
   * [settings.py](./temp_app/settings.py)
   * [urls.py](./temp_app/urls.py)
   * [wsgi.py](./temp_app/wsgi.py)
 * [README.md](./README.md)

 - The uses of the various files:
	- The outer mysite/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
	- manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
	- The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
	- mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
	- mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
	- mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
	- mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details

## Setting Apps

- Projects vs. apps

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

- To create your app, make sure you’re in the same directory as manage.py and type this command:

` $ python manage.py startapp polls`

- Structure will be as follows:

polls
 * [admin.py](polls/admin.py)
 * [apps.py](polls/apps.py)
 * [__init__.py](polls/__init__.py)
 * [migrations](polls/migrations)
   * [__init__.py](polls/migrations/__init__.py)
 * [models.py](polls/models.py)
 * [tests.py](polls/tests.py)
 * [views.py](polls/views.py)

 - To register new views for an application, `touch` the file *urls.py* and add `from django.conf.urls import url` to it. 
 - Now declare the `urlpatterns = [ url(r'', <what view>, name = name of view), ...]`

- When to use `include()`

You should always use include() when you include other URL patterns. _admin.site.urls_ is the only exception to this.

