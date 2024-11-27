# Django Bootstrap Starter Kit

#### Includes the following features
- 2 apps - core and accounts - with URLs, views and basic templates already set up
- Bootstrap 5
- Custom User model 
- Registration, log in/out using `django-allauth` (with email as authentication method)
- [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [`django-widget-tweaks`](https://pypi.org/project/django-widget-tweaks/)
- [`django-environ`](https://pypi.org/project/django-environ/)
- Tests for Custom User, sign up, views, and templates

## Installation


### Create a new folder for your project

### Create a virtual environment
```shell
python -m venv <virtual_env_name>
```

### Activate it

(windows)
```shell
<virtual_env_name>\Scripts\activate
```

(macOS)
```shell
source <virtual_env_name>/bin/activate
```

### Clone this repository
Don't forget the dot at the end if you want to create project in the same directory.
```shell
 git clone git@github.com:igorsimb/django-project-template.git .
```

### Install everything from requirements.txt
```shell
pip install -r requirements.txt
```

### Make migrations:

```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```

### Run tests
```shell
python manage.py test
```

### Run server:

```shell
python manage.py runserver
```

Note:
Whenever you need to call User, put this at the top of the file (e.g. in views.py, models.py):
```python
from django.contrib.auth import get_user_model
User = get_user_model()
```

You are all set! :)
