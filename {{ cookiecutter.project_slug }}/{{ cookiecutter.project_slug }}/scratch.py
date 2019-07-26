import os
import sys

# needed for Sublime Text 3
# sys.path.append('PATHTOPROJECT/{{ cookiecutter.project_slug }}')
# set the Django settings module before initializing Django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_slug }}.settings"
)
import django

django.setup()
