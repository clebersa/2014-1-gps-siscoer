# -*- coding: utf-8 -*-
import os.path
import smtplib
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP_ORIGINAL
from django.conf.global_settings import MIDDLEWARE_CLASSES as MC_ORIGINAL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Weslley Araujo', 'eng@weslleyaraujo.com'),
)

SECRET_KEY = '$03#4*4p6w9a_!+uz(%j51s-7nu#jj+h=+4wwpkxyrwi=0huta'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'siscoer',
        'USER': 'userlocal',
        'PASSWORD': '123456@',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = [
    '*',
]

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-BR'
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = '.'
DECIMAL_SEPARATOR = ','

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'sitestatic'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = MC_ORIGINAL + (
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates'),
)

ROOT_URLCONF = 'siscoer.urls'

WSGI_APPLICATION = 'siscoer.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    # my apps
    'usuario',
    'estoque',

)

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

# ============================================================================
# Local settings here
# ============================================================================

TEMPLATE_CONTEXT_PROCESSORS = TCP_ORIGINAL + (
    'django.core.context_processors.request',
)

# session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True

# message settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

### Grappelli configs
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'
GRAPPELLI_ADMIN_TITLE = u'SISCOER - Administrativo'
AUTOCOMPLETE_LIMIT = 15
ADMIN_TOOLS_MENU = 'menu.CustomMenu'
GRAPPELLI_INDEX_DASHBOARD = 'siscoer.dashboard.CustomIndexDashboard'


LOGOUT_URL = '/'

LOGIN_URL = '/login'