{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Install
-------
Be sure to have following avaliabe in your system:
- python 2.7
- pip
- virtualenv
- PostgreSQL (optionally)

Install steps (bash commands):
- `virtualenv venv`
- `source venv/bin/activate`
- `cd {{cookiecutter.repo_name}}`
- `pip install -r requirements.txt`
- `python manage.py migrate`

Run
---
- `python manage.py runserver`, to run development server
