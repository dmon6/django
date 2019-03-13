# Django startup

Following the Corey Schafer tutorial on youtube



[Django tutorial video 1][d6f4fb88]

  [d6f4fb88]: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p "Django tutorial video 1"

## Setting up your environment

I'll be using **pipenv** so modify as needed

Create django directory and create environment

```sh
mkdir ~/django && cd ~/django
pipenv --python 3.7
pipenv install django
pipenv run python -m django --version #version was 2.1.7 in time of the video
```
The 'pipenv install django' command will create a Pipfile as well as a Pipfile.lock. ==**DO NOT DELETE**==

## Create a new project

Look at all different options of django
```sh
django-admin

  Type 'django-admin help <subcommand>' for help on a specific subcommand.

  Available subcommands:

  [django]
      check
      compilemessages
      createcachetable
      dbshell
      diffsettings
      dumpdata
      flush
      inspectdb
      loaddata
      makemessages
      makemigrations
      migrate
      runserver
      sendtestemail
      shell
      showmigrations
      sqlflush
      sqlmigrate
      sqlsequencereset
      squashmigrations
      startapp
      startproject
      test
      testserver
  Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
```
This creates the project structure with all the folders and initial files needed for the project
```sh
django-admin startproject <project_name>
```
View project structure
```sh
#tree <directory of project>
tree . #if you're inside the directory

  ├── Pipfile
  ├── Pipfile.lock
  └── django_project
      ├── db.sqlite3
      ├── django_project
      │   ├── __init__.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      └── manage.py
```

Run django server
```sh
python manage.py runserver
```
To access the site that was just created in the command ran above, open a browser and got to the default page of 127.0.0.1:8000 alternatively you can use localhost:8000.

---
Video 2 of Corey Schafer guide on youtube:

[Django tutorial 2][a026bf6d]

  [a026bf6d]: https://www.youtube.com/watch?v=a48xeeo5Vnk&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2 "Django tutorial 2"

## Create a blog app for the website

Use django's built-in tools to create an app folder using their template/structures.

```sh
#python manage.py startapp <app name>
python manage.py startapp blog
```

The data structure created by the last comnand is very similar to the 'django-admin startproject' command
```sh
tree .

  ├── blog
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations
  │   │   └── __init__.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  ├── db.sqlite3
  ├── django_project
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── manage.py

```
At this point, the app doesn't do much we'll need to do some modifications to the existing files to make it work.

We need to be able to point to the 'blog' app that we just created, add this to the django_project/urls.py file

```py
from django.urls import path, include #this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), #this
]

```
We're importing  'include' because it's being used in the 'path('blog')...' line,  it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URL conf for further processing.

Now we need to make /blog do stuff. Lets modify the blog/views.py file with the following

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

The app still can't do anything because there's no actual url for blog yet. So create a new file named urls.py in the blog directory.
Include the following.

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
```

Again this file is very similar to the django_project/urls.py file

---

# Templates

By default django looks for a 'templates' sub folder in an app folder to handle html stuff. Create a templates folder in the blog directory

```sh
mkdir blog/templates
```

create database tables to send and receive data 
```sh
python manage.py makemigrations
python manage.py migrate
```

create admin for localhost:8000/admin
```sh
python manage.py createsuperuser

```

create new app to handle user login
```bash
python manage.py startapp users
```

after creating the app be sure to update the /django_project