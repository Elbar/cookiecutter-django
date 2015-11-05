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

{% if cookiecutter.heroku.lower() == 'true' %}
Heroku
------
To setup, follow this [guide](https://devcenter.heroku.com/articles/getting-started-with-django).

In short:
- remember to init git repo
- `heroku local` to test locally
- `heroku create` one time, before the project deploy to heroku
- `git push heroku master` to deploy
- `heroku run python manage.py syncdb` one time, before launching the project
- `heroku open` open project url in browser
- `heroku ps:scale web=1` debug
- `heroku ps` debug
- `heroku run python manage.py shell` debug
- `heroku logs` logs
- `heroku apps` app list
- `heroku apps:destroy --app <app-name> --confirm <app-name>` completely destroy app on heroku
{% endif %}
