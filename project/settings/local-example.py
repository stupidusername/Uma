from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE_ME'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uma',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
    }
}

# Debug Toolbar setup

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']

    # The order of MIDDLEWARE is important. You should include the Debug
    # Toolbar middleware as early as possible in the list. However, it must
    # come after any other middleware that encodes the response’s content, such
    # as GZipMiddleware.
    MIDDLEWARE.\
        insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    INSTALLED_APPS += [
       'debug_toolbar',
    ]
