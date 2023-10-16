"""
Django settings for pms project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = ['pmdsdata12', '10.4.1.234', '127.0.0.1',
                 'localhost', '10.4.1.234:8081', '10.4.1.234:8082']
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))

# Application definition

# def show_toolbar(request):
#     return True
# SHOW_TOOLBAR_CALLBACK = show_toolbar
# DEBUG_TOOLBAR_CONFIG = {'INSERT_BEFORE':'</head>'}
INTERNAL_IPS = ['pmdsdata12', '10.4.1.234', '127.0.0.1',
                 'localhost', '10.4.1.234:8081', '10.4.1.234:8082']
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
# }

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_bootstrap5',
    'widget_tweaks',
    'corsheaders',
    'prod_query',
    'barcode',
    'dashboards',
    'site_variables',
    'query_tracking',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'pms.middleware.timezone.TimezoneMiddleware',
    'pms.middleware.site_variables.SiteVariableMiddleware',

]
if DEBUG:
    MIDDLEWARE.remove('whitenoise.middleware.WhiteNoiseMiddleware')


ROOT_URLCONF = 'pms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pms/templates')],
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

WSGI_APPLICATION = 'pms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_PMS_NAME', 'django_pms'),
        'USER': os.environ.get('DB_PMS_USER', 'muser'),
        'PASSWORD': os.environ.get('DB_PMS_PASSWORD', 'wsj.231.kql'),
        'HOST': os.environ.get('DB_PMS_HOST', '10.4.1.245'),
        'PORT': os.environ.get('DB_PMS_PORT', 6601),
    },
    'prodrpt-md': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_PRDRPT_NAME', 'prodrptdb'),
        'USER': os.environ.get('DB_PRDRPT_USER', 'stuser'),
        'PASSWORD': os.environ.get('DB_PRDRPT_PASSWORD', 'stp383'),
        'HOST': os.environ.get('DB_PRDRPT_HOST', '10.4.1.245'),
        'PORT': os.environ.get('DB_PRDRPT_PORT', 3306),
    }
}
# DATABASES = {
#     'default': env.db('DEFAULT_DB_URL'),
#     'prodrpt-md': env.db('MDPRODRPT_URL'),
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

STATIC_ROOT = '/vol/web/static'
MEDIA_ROOT = '/vol/web/media'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'common_static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # },
        'django.request': {
            'level': 'INFO',
            'handlers': ['console',]
        },
        'prod-query': {
            'level': 'INFO',
            'handlers': ['console',],
        }

    }
}
