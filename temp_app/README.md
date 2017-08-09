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

- Directory Structure is as follows:

```bash
.
├── db.sqlite3
├── manage.py
├── polls
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── polls
│   ├── templates
│   │   ├── 403.html
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── polls
│   │   │   ├── form.html.j2
│   │   │   └── index.html.j2
│   │   └── touch
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
└── temp_app
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

15 directories, 72 files
```


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

- Django provides an admin panel to handle data addition etc. You can always implement the admin panel from the normal site routes itself as well.
- Create a new superuser `python manage.py createsuperuser`
- Basically to register any models, the specific classes should be added to the _admin.py_ of the given app (polls in our case). (`admin.site.register(Question)`)

## Querying

### Querying objects

- Objects can be queryed using the `<Classname>.objects.all()` method. This returns a query set containing all the objects of the particular type, given a proper `__str__()` representation of the Class.
- You can get all data **except** certain objects by using the `except()` function. Works with the same _field lookups_ as shown below.

- The behavior of `filter()` for queries that span multi-value relationships is not implemented equivalently for `exclude()`. Instead, the conditions in a single `exclude()` call will not necessarily refer to the same item.

	- For example, the following query would exclude blogs that contain both entries with “Lennon” in the headline and entries published in 2008:

```python
Blog.objects.exclude(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008,
)
```
	- However, unlike the behavior when using filter(), this will not limit blogs based on entries that satisfy both conditions. In order to do that, i.e. to select all blogs that do not contain entries published with “Lennon” that were published in 2008, you need to make two queries:

```python
Blog.objects.exclude(
    entry__in=Entry.objects.filter(
        headline__contains='Lennon',
        pub_date__year=2008,
    ),
)
```

- You can get induvidual classes by `<Classname>.objects.get(__**kwargs_)`. Some common arguments to the _get_ method are
	- Getting the specific attribute:  
		```Question.objects.get(pub_date__year = timezone.now().year)```
		Here the year is a part of the *pub_date* attribute
	- **__exact**: Adding this to the query will match for exact value. (this is the default lookup)
	- **__contains**: This checks for substring or similar containment.
	- **__icontains**: Similar to above but case-insenstive.
	- **__startswith, endswith**: Checks for starting substring, ending substring (or similar).



### Filters

Everything inside a single filter() call is applied simultaneously to filter out items matching all those requirements. Successive filter() calls further restrict the set of objects, but for multi-valued relations, they apply to any object linked to the primary model, not necessarily those objects that were selected by an earlier filter() call.

That may sound a bit confusing, so hopefully an example will clarify. To select all blogs that contain entries with both “Lennon” in the headline and that were published in 2008 (the same entry satisfying both conditions), we would write:

```Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)```

To select all blogs that contain an entry with “Lennon” in the headline as well as an entry that was published in 2008, we would write:

```Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)```

### Queries 

- **Complex lookups with Q objects**

	Keyword argument queries – in `filter()`, etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.

	A Q object (django.db.models.Q) is an object used to encapsulate a collection of keyword arguments. These keyword arguments are specified as in “Field lookups” above.

	For example, this Q object encapsulates a single LIKE query:
	```python
	from django.db.models import Q
	Q(question__startswith='What')

	Q objects can be combined using the & and | operators. When an operator is used on two Q objects, it yields a new Q object.
	```
	For example, this statement yields a single Q object that represents the “OR” of two "question__startswith" queries:
	`Q(question__startswith='Who') | Q(question__startswith='What')`

- **F expressions**
	Django provides F expressions to allow such comparisons. Instances of F() act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.

	For example, to find a list of all blog entries that have had more comments than pingbacks, we construct an F() object to reference the pingback count, and use that F() object in the query:
	
	```python
	>>> from django.db.models import F
	>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
	```
	
	Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with F() objects, both with constants and with other F() objects. To find all the blog entries with more than twice as many comments as pingbacks, we modify the query:
	
	```python
	>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
	```
	
	To find all the entries where the rating of the entry is less than the sum of the pingback count and comment count, we would issue the query:
	
	```python
	>>> Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
	```
	
	You can also use the double underscore notation to span relationships in an F() object. An F() object with a double underscore will introduce any joins needed to access the related object. For example, to retrieve all the entries where the author’s name is the same as the blog name, we could issue the query:

	```python
	>>> Entry.objects.filter(authors__name=F('blog__name'))
	```

## Views 

- Django uses the `jinja` templating engine, similar to the one used in _Flask_.
- Add views to the `views.py` of your app:

```python
	from django.shortcuts import render
	#OR
	from django.http import HttpResponse
	from django.template import loader
	
	def index(request, param1, param2):
		on_the_page = param1
		context = {
			"on the page" : on_the_page,
			"2" : param2
		}
		return HttpResponse(template.render(context, request))
		#OR
		return render(request, 'appname/filename', context)
```

- It becomes challenging to change URLs on projects with a lot of templates. However, since you defined the name argument in the url() functions in the polls.urls module, you can remove a reliance on specific URL paths defined in your url configurations by using the {% url %} template tag:
	- `<li><a href="{% url 'index' question.id %}">{{ question.question_text }}</a></li>`

- In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiates the URL names between themm by adding namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace `app_name = 'polls'` and then modify the url in the html as 
	- `<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>`

### Default Views

- Django provides some default views with which to display data, reducing the amount of HTML one has to write.
- We’re using two generic views here: ListView and DetailView. Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular type of object.”
  -  Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
  -  The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views

- For DetailView the question variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable. However, for ListView, the automatically generated context variable is question_list. 
- To override this we provide the context_object_name attribute, specifying that we want to use latest_question_list instead. As an alternative approach, you could change your templates to match the new default context variables – but it’s a lot easier to just tell Django to use the variable you want.
- `  context_object_name = 'latest_question_list'` : This basically sets the variable that will be used in the template itself.

## Forms

- Forms are almost implemented just as normal forms would be, difference being the _urls_ can be specified as told above to avoid any hard coding. 
- Following example covers most of the form details and fields 
```python
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```

## Testing & Automated Tests

- Tests are a way of ensuring that our app works properly. Tests have to be written once, afterwhich they can be execucted by the system automatically.
- A conventional place for an application’s tests is in the application’s tests.py file; the testing system will automatically find tests in any file whose name begins with test.
- This is an example of a testcase wherein the date of publication is in _30 days_ in the future, yet is marked as published recently. 
```python
class QuestionModelTests(TestCase):
	
	def test_published_recently_with_future_result(self):
	"""
		This test exporses the bug that questions created with
		a future date are also marked as somthing published recently

	"""

	time = timezone.now() + datetime.timedelta(days = 30)
	future_question = Question(pub_date = time)
	self.assertIs(future_question.was_published_recently(), False)
```
- Now to run the tests we simply have to `python manage.py test <app name>`

## Django Test Client

- Django provides a test client to simulate a user interacting with the application.
- `from django.test.utils import setup_test_environment`
- In the terminal, 
```python
>>> setup_test_environment()
```
- After this, you have to create a client and test at client level, ie, with the rendered HTML
```python 
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        ...
```
- It might seem that our tests are growing out of control. At this rate there will soon be more code in our tests than in our application, and the repetition is unaesthetic, compared to the elegant conciseness of the rest of our code.

- It doesn’t matter. Let them grow. For the most part, you can write a test once and then forget about it. It will continue performing its useful function as you continue to develop your program.

- Sometimes tests will need to be updated. Suppose that we amend our views so that only Questions with Choices are published. In that case, many of our existing tests will fail - telling us exactly which tests need to be amended to bring them up to date, so to that extent tests help look after themselves.

- At worst, as you continue developing, you might find that you have some tests that are now redundant. Even that’s not a problem; in testing redundancy is a good thing.

- As long as your tests are sensibly arranged, they won’t become unmanageable. Good rules-of-thumb include having:
	-    a separate TestClass for each model or view
	-    a separate test method for each set of conditions you want to test
	-    test method names that describe their function


## Serving Static Files

```bash
polls
├── static
   	└── polls
```

- Static files (_images, css, js, etc_) must be placed within the structure shown above. .


