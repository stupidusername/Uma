import os
import uma

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Application definition.

INSTALLED_APPS = [
    'uma.apps.UmaConfig',
    'baton',  # Needs to be placed before the admin app.
    'djmoney',  # Support for money fields.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_db_logger',
    'alteradmin.apps.AlterAdminConfig',  # After admin models are registered.
    'channels',
    'baton.autodiscover'  # Needs to be placed at the end of the list.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Password validation.
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization.
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CURRENCIES = ['ARS']  # Restrict the currencies listed on the project.

DEFAULT_CURRENCY = 'ARS'

# Static files (CSS, JavaScript, Images).
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Media files (upload by the user).

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Baton configuration.
# https://django-baton.readthedocs.io/en/latest/configuration.html

BATON = {
    'SITE_HEADER': uma.APP_NAME,
    'SITE_TITLE': uma.APP_NAME,
    'SUPPORT_HREF': None,
    'COPYRIGHT': None,
    'POWERED_BY': None
}

# Set your ASGI_APPLICATION setting to point to that routing object as your
# root application.

ASGI_APPLICATION = "project.routing.application"

# Logging configuration.
# All SGHConsummer log records will be saved to the DB.
# Only those log records from django.channels.server that start with
# "WebSocket" will be saved to the DB.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(name)s - %(message)s'
        }
    },
    'filters': {
        'is_websocket_action': {
            '()': 'project.logging.StartsWithFilter',
            'prefix': 'WebSocket'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'db': {
            'level': 'INFO',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
        'db_websocket_action': {
            'level': 'INFO',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler',
            'filters': ['is_websocket_action']
        }
    },
    'loggers': {
        'django.channels.server': {
            'level': 'DEBUG',
            'handlers': ['db_websocket_action', 'console'],
            'propagate': False
        },
        'uma.consumers.SGHConsumer': {
            'level': 'DEBUG',
            'handlers': ['db', 'console']
        }
    }
}
