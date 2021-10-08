"""
Django settings for krafts project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path
if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

ALLOWED_HOSTS = ['krafts-dreid.herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Used along with SITE_ID setting by social account below to
    # create proper call back urls when connecting via social media
    'django.contrib.sites',
    'allauth',
    # Allows basic user account functionality like
    # loggining in/out, user registration, password resets
    'allauth.account',
    # Handles logging in via social media providers
    'allauth.socialaccount',
    'home',
    'products',
    'cart',
    'checkout',
    'profiles',

    # Allows forms to be formatted using Bootstrap
    'crispy_forms',
    'storages',
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

ROOT_URLCONF = 'krafts.urls'

# Specify which Bootstrap template pack for crispy forms to use
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add root templates directory and custom Allauth directory to template DIR setting
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # Allow Django and Allauth to access http request object in templates
                # (eg, access request.user in django templates)
                # Required from Django by Allauth as Allauth templates use request object frequently
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # To access noimage file in media folder for products with no image
                'django.template.context_processors.media',
                'cart.contexts.cart_contents'
            ],
            # All tags to be made available across all templates
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    # (Handles superusers logging into admin)
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    # (Allows users to log into store via email address)
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Tell Allauth to allow authentication useing either username or email
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# Email required to register for site
ACCOUNT_EMAIL_REQUIRED = True
# Verifying email is mandatory (ensure email is real)
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# User must enter email twice for typo purposes
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# Username must be at lest 4 characters
ACCOUNT_USERNAME_MIN_LENGTH = 4
# Specify login url
LOGIN_URL = '/accounts/login/'
# Specify url to redirect back to after logging in
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'krafts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# When app is runing on Heroku (DATABASE_URL environment variable defined there)
if 'DATABASE_URL' in os.environ:
    # Connect to Postrgres
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Otherwise, connect to sqlite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# Tuple telling Django where all static files are located (in the project level 'static' folder)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Use static function in urls.py to add media url to list of urls so Django can see it
MEDIA_URL = '/media/'
# All uploaded media files go here
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Tell Django which S3 bucket to communicate with
# Only to be done on Heroku
if 'USE_AWS' in os.environ:
    # Cache control
    # Inform browser it can cache static files for long periods of time
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

# Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'krafts-dreid'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Static and media files
    # Use storage class in custom_storages.py
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    # Set location to save static files to 'static' folder
    STATICFILES_LOCATION = 'static'
    # Use storage class in custom_storages.py
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    # Set location to save media files to 'media' folder
    MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# For use is cart views.py to calculate free delivery
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10

# Set stripe currency to usd
STRIPE_CURRENCY = 'usd'
# Get STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET from environment,
# give them empty default values
# Getting them from Gitpod environment keeps secret key safe from exposure
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

# If DEVELOPMENT variable is set in environment
if 'DEVELOPMENT' in os.environ:   
    # Log confirmation emails to console to get confirmation links
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # Email address from which emails will be sent to customers
    DEFAULT_FROM_EMAIL = 'krafts@example.com'
# Otherwise, set the following variables
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
