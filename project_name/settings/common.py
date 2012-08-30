"""Common settings and globals."""
from os.path import abspath, basename, dirname, join, normpath


DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('Issac Kelly', 'issac@servee.com'),
    ('Josh Boles', 'josh@servee.com'),
)
MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True


MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'packaged', 'media'))
MEDIA_URL = '/site_media/media/'
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'packaged', 'static'))
STATIC_URL = '/site_media/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_URL = STATIC_URL
COMPRESS_PARSER = 'compressor.parser.LxmlParser'
COMPRESS_PRECOMPILERS = [
    ('text/less', 'lessc {infile} {outfile}'),
]

STATICFILES_DIRS = [
    normpath(join(DJANGO_ROOT, 'static')),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


SECRET_KEY = "{{ secret_key }}"


FIXTURE_DIRS = [
    normpath(join(DJANGO_ROOT, 'fixtures')),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
]


TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]


TEMPLATE_DIRS = [
    normpath(join(DJANGO_ROOT, 'templates')),
]



MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


ROOT_URLCONF = '%s.urls' % SITE_NAME


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'compressor',
    'gunicorn',
    'south',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
