import os
import django

# Make filepaths relative to settings.
ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

DEBUG = True
TEMPLATE_DEBUG = True

if django.VERSION < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
else:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

JINJA_CONFIG = {}

SITE_ID = 1

SECRET_KEY = 'foobar'

DATABASES = {
    'default': {
        'NAME': 'test.db',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'waffle',
    'test_app',
    'import_export',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'waffle.middleware.WaffleMiddleware',
)

ROOT_URLCONF = 'test_app.urls'

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

JINGO_EXCLUDE_APPS = (
    'django',
    'waffle',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

WAFFLE_FLAG_DEFAULT = False
WAFFLE_SWITCH_DEFAULT = False
WAFFLE_SAMPLE_DEFAULT = False
WAFFLE_OVERRIDE = False

if django.VERSION < (1, 7):
    INSTALLED_APPS += ('south', )

    SOUTH_MIGRATION_MODULES = {
        'waffle': 'waffle.south_migrations'
    }

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WSGI_APPLICATION = 'wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))

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
