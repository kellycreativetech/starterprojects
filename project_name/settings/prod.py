"""Production settings and globals."""


from os import environ
from sys import exc_info
from urlparse import urlparse, uses_netloc

from common import *
DEBUG = False

# Helper lambda for gracefully degrading environmental variables:
env = lambda e, d: environ[e] if environ.has_key(e) else d

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', 'email-smtp.us-east-1.amazonaws.com')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', 'formsender@servee.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', 'Ak//5EKRBR7Qc660N88vEQV5N2gFTguom18QQ4OZTfmS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', 'AKIAJFJXRFBLDYNOBR5A')
EMAIL_PORT = env('EMAIL_PORT', 587)
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
EMAIL_USE_TLS = True if env('EMAIL_USE_TLS', 'True') == 'True'  else False
SERVER_EMAIL = DEFAULT_FROM_EMAIL



########## DATABASE CONFIGURATION
# See: http://devcenter.heroku.com/articles/django#postgres_database_config
uses_netloc.append('postgres')
uses_netloc.append('mysql')

try:
    if environ.has_key('DATABASE_URL'):
        url = urlparse(environ['DATABASE_URL'])
        DATABASES['default'] = {
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        }
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print "Unexpected error:", exc_info()

