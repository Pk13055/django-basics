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

- _Projects vs. apps_

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

## Wiring the views and writing routes

- To register new views for an application, `touch` the file *urls.py* and add `from django.conf.urls import url` to it. 
- Now declare the `urlpatterns = [ url(r'', <what view>, name = name of view), ...]`
- When to use `include()`
	You should always use include() when you include other URL patterns. _admin.site.urls_ is the only exception to this.
- In `views.py`, you should include `from django.http import HttpResponse`

- For a route `url(r'example/view1', views.foo, name = 'foo')`, corresponding view is as follows:
```python
	from django.http import HttpResponse
	def foo(request):
		return HttpResponse("Hello World")
```

## Database Connectivity

- By default, Django uses SQLite.
- If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings:

	-  ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'. Other backends are also available.
	- NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.

- If you are not using SQLite as your database, additional settings such as USER, PASSWORD, and HOST must be added. For more details, see the reference documentation for DATABASES.

By default, INSTALLED_APPS contains the following apps, all of which come with Django:
	-    django.contrib.admin – The admin site. You’ll use it shortly.
	-    django.contrib.auth – An authentication system.
	-    django.contrib.contenttypes – A framework for content types.
	-    django.contrib.sessions – A session framework.
	-    django.contrib.messages – A messaging framework.
	-    django.contrib.staticfiles – A framework for managing static files.

- These applications are included by default as a convenience for the common case. Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:
	- `$ python manage.py migrate`

- To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file, so its dotted path is 'polls.apps.PollsConfig'. Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting. It’ll look like this:

## Model Creation

- You have to create models within the models.py of your specific application (_within the project_)
- Import `models` from the `django.db` module.
- A typical model will look like:
```python 
	@python_2_unicode_compatible  # only if you need to support Python 2
	class <tablename>(models.model):
		field1 = models.<typeoffield>(_params_)
		...
```
- Once you crete the required classes and tables, you can create the required migration
- `python manage.py makemigrations <app name> `

- Migrations are how Django stores changes to your models (and thus your database schema) - they’re just files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py. 

- Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:
	-    Change your models (_in models.py_).
	-    Run `python manage.py makemigrations` to create migrations for those changes
	-    Run `python manage.py migrate` to apply those changes to the database.

## Adding to the Database

- First to check out CLI code run ` python manage.py shell`
- Adding data is simple. Create a question/choice object as 
	- `Question(question_text = "Example text", pub_date = timezone.now())` (_use timezone from *django.utils* instead of datetime.now() from datetime_)
- Overwrite the str module get proper repr for the Objects
- Query all objects as : `Question.objects.all()`

## Django Admin
