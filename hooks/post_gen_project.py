import os
import shutil
try:
    from django.utils.crypto import get_random_string
except ImportError:
    import random

    def get_random_string(length=12,
                          allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        return ''.join(random.choice(allowed_chars) for i in range(length))

if not {{cookiecutter.custom_user}}:
    shutil.rmtree('../{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/apps/users')
    shutil.rmtree('../{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/templates/users')

if not {{cookiecutter.account_templates}}:
    shutil.rmtree('../{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/templates/account')

if {{cookiecutter.extract_settings_local}}:
    shutil.copyfile('../{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/config/settings_local.py.example',
        '../{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/config/settings_local.py')

secret_key_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
with open('../{{cookiecutter.repo_name}}/{{cookiecutter.project_name}}/config/settings.py', 'r+') as f:
    data = f.read()
    data = data.replace('__{default_secret_key}__', get_random_string(50, secret_key_chars))
    f.seek(0)
    f.write(data)
