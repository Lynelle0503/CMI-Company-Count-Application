"""
Django settings for catalystcount project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import environ
import os, inspect
import django_dyn_dt
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j(id3wr50)=nj@d0d+^gqty!q*3c!i2*0&585ow7rl01&7n=8y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #allauth apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    #allauth social
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    #upload file
    'import_export',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'myapp',
    
    #DRF api
    'django_dyn_api',
    'rest_framework',
    'rest_framework.authtoken',
    
    #query builder
    'django_dyn_dt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'catalystcount.urls'

TEMPLATE_DIR_DATATB = os.path.join(BASE_DIR, "django_dyn_dt/templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates", TEMPLATE_DIR_DATATB],
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

WSGI_APPLICATION = 'catalystcount.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        
        #Adding PostgreSQL as the database
        'ENGINE':'django.db.backends.postgresql',
        'NAME': 'dummy-test',
        'USER':'lyn',
        'PASSWORD':'lyn',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

#Query Builder page
DYN_DB_PKG_ROOT = os.path.dirname( inspect.getfile( django_dyn_dt ) ) # <-- NEW App

STATICFILES_DIRS = (
    os.path.join(DYN_DB_PKG_ROOT, "templates/static"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#allauth data
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",  # new
]
SITE_ID = 1 
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = "/"


#parse CSV
IMPORT_EXPORT_USE_TRANSACTIONS = True

#files can be seen in media folder
MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'

# Set the maximum file upload size to 1GB (in bytes)
FILE_UPLOAD_MAX_MEMORY_SIZE = 1073741824  # 1GB

# Increase request timeout for larger files (depending on deployment)
DATA_UPLOAD_MAX_MEMORY_SIZE = 1073741824  # 1GB


# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

#DRF API
DYNAMIC_API = {
    # pattern: 
    # API_SLUG -> Import_PATH 
    'compdata'  : "myapp.models.CompanyData",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

#Query Builder
DYNAMIC_DATATB = {
    # SLUG -> Import_PATH 
    'compdata'  : "myapp.models.CompanyData",
}
