import os
import sys
import shutil
import subprocess
try:
    from django.utils.crypto import get_random_string
except ImportError:
    import random

    def get_random_string(length=12,
                          allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        return ''.join(random.choice(allowed_chars) for i in range(length))

if not {{cookiecutter.custom_user}}:
    shutil.rmtree('../{{cookiecutter.repo_name}}/apps/users')
    shutil.rmtree('../{{cookiecutter.repo_name}}/templates/users')

if not {{cookiecutter.account_templates}}:
    shutil.rmtree('../{{cookiecutter.repo_name}}/templates/account')

if {{cookiecutter.extract_settings_local}}:
    shutil.copyfile('../{{cookiecutter.repo_name}}/config/settings_local.py.example',
        '../{{cookiecutter.repo_name}}/config/settings_local.py')

if not {{cookiecutter.heroku}}:
    os.remove('../{{cookiecutter.repo_name}}/Procfile')

secret_key_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
with open('../{{cookiecutter.repo_name}}/config/settings.py', 'r+') as f:
    data = f.read()
    data = data.replace('__{default_secret_key}__', get_random_string(50, secret_key_chars))
    f.seek(0)
    f.write(data)

# must be the last
if {{cookiecutter.gitinit}}:
    run_thru_shell = sys.platform.startswith('win')
    cwd = '../{{cookiecutter.repo_name}}'
    # init
    proc = subprocess.Popen(
        ['git', 'init'],
        shell=run_thru_shell,
        cwd=cwd
    )
    proc.wait()

    # add
    proc = subprocess.Popen(
        ['git', 'add', '-A'],
        shell=run_thru_shell,
        cwd=cwd
    )
    proc.wait()

    if {{cookiecutter.gitcommit}}:
        # commit
        proc = subprocess.Popen(
            ['git', 'commit', '-m', '"First commit"'],
            shell=run_thru_shell,
            cwd=cwd
        )
        proc.wait()
