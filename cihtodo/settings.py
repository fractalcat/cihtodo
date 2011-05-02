import os.path

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

FORCE_SCRIPT_NAME = ""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'todo.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Australia/Sydney'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

SECRET_KEY = 'r/hH=f}./D#3Ii>}r&p/p\fv:*OhSdSic_S)q{vsN"g01yS0Yo ,]L.yEAqKbBOa'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'cihtodo.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'tmpl')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'todo',
)

TODO_TAG_URL = '/t'
