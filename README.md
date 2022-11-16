# Django Bootstrap Starter Kit

#### Includes the following features
- 2 apps - core and accounts - with URLs, views and basic templates already set up
- Bootstrap 5
- Custom User model 
- Registration, log in/out using `django-allauth` (with email for authentication method)
- [`django-extensions`](https://github.com/django-extensions/django-extensions)
- [`django-debug-toolbar`](https://github.com/jazzband/django-debug-toolbar)
- [`django-widget-tweaks`](https://github.com/jazzband/django-widget-tweaks)
- Tests for Custom User and sign up

## Installation

### Create a virtual environment
```
python -m venv <virtual_env_name>
```

### Activate it

(windows)
```
<virtual_env_name>\Scripts\activate
```

### Run startproject command
Use this repository as Django project template (don't forget the dot at the end to create project in the same directory):

```
django-admin startproject --template https://github.com/igorims/django-project-template/archive/master.zip <projectname> .
```

### Install everything from requirements.txt
```
pip install -r requirements.txt
```

### Make migrations:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

### Run server:

```
python manage.py runserver
```

Note:
Whenever you need to call User, put this at the top of the file (e.g. in views.py, models.py):
```
from django.contrib.auth import get_user_model
User = get_user_model()
```
