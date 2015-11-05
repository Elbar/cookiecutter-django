"""
Django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)


# Settings checklist https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '__{default_secret_key}__')

DEBUG = os.environ.get('DJANGO_DEBUG', False)

ALLOWED_HOSTS = [os.environ.get('DJANGO_ALLOWED_HOSTS')] if os.environ.get('DJANGO_ALLOWED_HOSTS', None) else []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
{% if cookiecutter.custom_user.lower() == 'true' %}    'apps.users',{% endif %}
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': os.environ.get('DJANGO_TEMPLATE_DEBUG', os.environ.get('DJANGO_DEBUG', False)),
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
        'NAME': os.environ.get('DJANGO_DB_NAME', '{{cookiecutter.project_name}}'),
        'USER': os.environ.get('DJANGO_DB_USER', '{{cookiecutter.project_name}}'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', '{{cookiecutter.project_name}}'),
        'TEST_CHARSET': 'utf8',
        'CONN_MAX_AGE': os.environ.get('DJANGO_DB_CONN_MAX_AGE', 60),
        'ATOMIC_REQUESTS': os.environ.get('DJANGO_DB_ATOMIC_REQUESTS', 'True').capitalize() == 'True',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = '/var/www/{{cookiecutter.project}}/static'  # dir must have corresponding access rights

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = '/var/www/{{cookiecutter.project}}/media'  # dir must have corresponding access rights
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
{% if cookiecutter.custom_user.lower() == 'true' %}
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
{% endif %}
# Mail settings
# dummy server:
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', "localhost")
EMAIL_PORT = os.environ.get('DJANGO_EMAIL_PORT', 1025)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
            '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console'],
            'level': "INFO",
        },
    }
}

try:
    from settings_local import *
except ImportError:
    pass
