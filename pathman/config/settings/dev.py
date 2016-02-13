# It's ok to import * in a settings file
from .base import *  # noqa

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pathman',
        'USER': 'pathman',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += ('debug_toolbar', )
