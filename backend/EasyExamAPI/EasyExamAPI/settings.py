"""
Django settings for EasyExamAPI project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Media Root Path

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "media"))
MEDIA_URL = "/media/"

# Project Settings

SCRIPT_DIR = os.path.join(BASE_DIR, "script")
CREDITS_GAINED_PER_PROBLEM = 100
CREDITS_GAINED_PER_VERIFICATION = 50
PROBLEM_COST = 50
CRITERION_TOLERANCE = 0.5
CRITERION_QUORUM = 10
CRITERION_VALUE = 30
CHALLENGE_SIZE = 3

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "mter*!@r=ms*y2v0@!^(=mh9h-m+ksoly4bd#q89l(tv@nk*2("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third Party
    "rest_framework",
    "rest_framework_docs",
    "corsheaders",
    # First Party
    "api",
    "user",
    "exam",
    "challenge",
]

MIDDLEWARE = [
    # these should be placed as high as possible
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "EasyExamAPI.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "EasyExamAPI.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = "/home/pastudil/easyexam/backend/EasyExamAPI/static/"

# User Model

AUTH_USER_MODEL = "user.User"

# Django Rest Framework

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        #        'rest_framework.authentication.SessionAuthentication',
        #        'rest_framework.authentication.BasicAuthentication',
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
    ),
}

# JWT Authentication

JWT_AUTH = {
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=7),
}

# https://pypi.org/project/django-cors-headers/

# TODO fix
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     # react server
#     'localhost:3000',
#     'http://dev.repositorium.cl:3000',
# )

# enable if cookies are needed
# CORS_ALLOW_CREDENTIALS = True

# enable if CSRF is needed
# CSRF_TRUSTED_ORIGINS = (
#     # react server
#     'localhost:3000',
# )

# django-sendfile Settings

SENDFILE_BACKEND = "sendfile.backends.development"
SENDFILE_ROOT = MEDIA_ROOT
SENDFILE_URL = "/protected"

# pdf preview
# X_FRAME_OPTIONS = 'ALLOW-FROM http://localhost:3000/'
X_FRAME_OPTIONS = "ALLOW-FROM https://easyexam.repositorium.cl/1"

# HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
