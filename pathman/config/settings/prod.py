# It's ok to import * in a settings file
from .base import *  # noqa

DEBUG = False

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
