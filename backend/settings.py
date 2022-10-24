from pathlib import Path
import os
import dj_database_url
from django_storage_url import dsn_configured_storage_class
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '<a string of random characters>')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG') == "True"

DIVIO_DOMAIN = os.environ.get('DOMAIN', '')
DIVIO_DOMAIN_ALIASES = [
    d.strip()
    for d in os.environ.get('DOMAIN_ALIASES', '').split(',')
    if d.strip()
]
DIVIO_DOMAIN_REDIRECTS = [
    d.strip()
    for d in os.environ.get('DOMAIN_REDIRECTS', '').split(',')
    if d.strip()
]

ALLOWED_HOSTS = [DIVIO_DOMAIN] + DIVIO_DOMAIN_ALIASES + DIVIO_DOMAIN_REDIRECTS

# Redirect to HTTPS by default, unless explicitly disabled
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT') != "False"

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Application definition

INSTALLED_APPS = [
    'backend',
    'cmsapp',

    # optional, but used in most projects
    'djangocms_admin_style',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # key django CMS modules
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    # Django Filer - optional, but used in most projects
    'filer',
    'easy_thumbnails',

    # the default CKEditor - optional, but used in most projects
    'djangocms_text_ckeditor',
    'ckeditor',

    # some content plugins - optional, but used in most projects
    'djangocms_file',
    'djangocms_icon',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',

    # optional django CMS Frontend modules
    'djangocms_frontend',
    'djangocms_frontend.contrib.accordion',
    'djangocms_frontend.contrib.alert',
    'djangocms_frontend.contrib.badge',
    'djangocms_frontend.contrib.card',
    'djangocms_frontend.contrib.carousel',
    'djangocms_frontend.contrib.collapse',
    'djangocms_frontend.contrib.content',
    'djangocms_frontend.contrib.grid',
    'djangocms_frontend.contrib.jumbotron',
    'djangocms_frontend.contrib.link',
    'djangocms_frontend.contrib.listgroup',
    'djangocms_frontend.contrib.media',
    'djangocms_frontend.contrib.image',
    'djangocms_frontend.contrib.tabs',
    'djangocms_frontend.contrib.utilities',

    # auth module
    'social_django',
    'profile',

    'crispy_forms',
    "crispy_bootstrap5",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'backend/templates', BASE_DIR/'cmsapp/templates', BASE_DIR/'profile/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',

                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


CMS_TEMPLATES = [
    # a minimal template to get started with
    ('dynamic.html', 'dynamic page'),
    ('index.html', 'home page'),
    ('about.html', 'about'),
    ('contact.html', 'contact'),
    ('index.html', 'index'),
    # serving static files with whitenoise demo
#    ('whitenoise-static-files-demo.html', 'Static File Demo'),
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Configure database using DATABASE_URL; fall back to sqlite in memory when no
# environment variable is available, e.g. during Docker build
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite://:memory:')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

if not DEBUG:
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_collected')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files
# DEFAULT_FILE_STORAGE is configured using DEFAULT_STORAGE_DSN

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN')

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN')

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = 'backend.settings.DefaultStorageClass'

# only required for local file storage and serving, in development
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join('/data/media/')

AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False

SITE_ID = 1

SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '714074814037-8bnp5oqt4hktqg0fe86hqih16mr7pp0k.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

LOGIN_REDIRECT_URL = '/profile-main'
