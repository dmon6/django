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

Use django's built-in tools to start up structure for an app

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
