# Enerdjized: a Django Starter Kit

Enerdjized is a batteries-included Django starter project with everything you need to start coding,
using HTMX, AlpineJS and including user authentication, static files, default styling using Tailwind CSS, beautiful 
toast messages custom error pages, and more.

<table>
  <tr>
    <td align="center">
      <a href="assets/1.png" target="_blank" title="Main Page">
        <img src="assets/1.png" alt="Main Page">
      </a>
      <br />
      <em>Main Page</em>
    </td>
    <td  align ="center">
      <a href="" target="_blank" title="Edit Profile">
        <img src="assets/2.png" alt="Edit Profile">
      </a>
      <br />
      <em>Edit Profile</em>
    </td>
    <td align="center">
    <a href="" target="_blank" title="Account Settings">
      <img src="assets/3.png" alt="Account Settings">
    </a>
      <br />
      <em>Account Settings</em>
    </td>
  </tr>
  <tr>
    <td align="center">
    <a href="" target="_blank" title="Inline Form">
        <img src="assets/3.5.png" alt="Inline Form">
      </a>
      <br />
      <em>Inline Form</em>
    </td>
    <td align="center">
      <a href="" target="_blank" title="Beautiful Signup">
        <img src="assets/4.png" alt="Beautiful Signup">
      </a>
      <br />
      <em>Beautiful Signup</em>
    </td>
  </tr>
</table>

#### Includes the following features
- 2 apps - `core` and `accounts` - with URLs, views and basic templates already set up
- Separate settings for local and production
- Tailwind CSS
- Custom User model 
- Profile model
- `django-allauth` for:
  - registration
  - log in/out
  - email change
  - email verification
- account deletion
- Profile settings (view, edit, delete) using HTMX
- Beautiful messages with auto dismissal using AlpineJS
- [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [`django-widget-tweaks`](https://pypi.org/project/django-widget-tweaks/)
- [`django-htmx`](https://pypi.org/project/django-htmx/)
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
