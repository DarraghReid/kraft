"""
Django settings for krafts project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    # (Handles superusers logging into admin)
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    # (Allows users to log into store via email address)
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Log confirmation emails to console to get confirmation links
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
