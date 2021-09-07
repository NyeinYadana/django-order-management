# Order Management
This project is implemented about the order management with authorization, authentication by python language and django framework.

## Installation

### At Ubuntu 18.0.4
```python

# django-filters
pip3 install django-filter

# widget_tweaks
pip3 install django-widget-tweaks

# Pillow
pip3 install Pillow

# Virtual environment setup
python3 -m venv env

source env/bin/activate

# Runserver
python3 manage.py runserver

```

### At Window
```python

# django-filters
pip install django-filter

# widget_tweaks
pip install django-widget-tweaks

# Pillow
pip install Pillow

# Virtual environment setup
python -m venv env

\env\Scripts\activate.bat

# Runserver
python manage.py runserver

```
After installation, add your app in **settings.py** is ***really important***.
```python

INSTALLED_APPS = [
     .....
    'django_filters',
    'widget_tweaks'
]

```

### Django Filter
You can read about the django-filters documentation [Django Filter](https://django-filter.readthedocs.io/en/stable/).

### Django Widget Tweaks
You can read about the django-widget-tweaks documentation  [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/).
