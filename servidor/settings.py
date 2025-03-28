"""
Django settings for servidor project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# Importaciones y configuraciones
import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-vy5*l8q-el7!e&i&#ihnhbo)t6e(3o5pc45f(^1*&k0%kcku)u'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'accounts',
    'empresas',
    'productos',
    'axes',
]

MIDDLEWARE = [
    'axes.middleware.AxesMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'servidor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'servidor.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de Autenticación
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'axes.backends.AxesBackend',
]

SITE_ID = 1  # Identificador del sitio actual.

# Configuraciones de Caché
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
    'axes': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',
    },
}




# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Nuevo ajuste para métodos de inicio de sesión
ACCOUNT_LOGIN_METHODS = {'email'}

# Opcional: Configuraciones de contraseña
ACCOUNT_PASSWORD_MIN_LENGTH = 8  # Longitud mínima de la contraseña
ACCOUNT_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Login y logout
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = reverse_lazy('home_empresas')
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True  # Cerrar sesión al acceder al enlace

# Configuraciones de Seguridad (Axes)
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1  # 1 hora de bloqueo
AXES_LOCKOUT_URL = '/locked/'  # URL de redirección en caso de bloqueo
AXES_RESET_ON_SUCCESS = True

# Duración de la sesión (30 minutos)
SESSION_COOKIE_AGE = 1800  # 30 minutos en segundos

# Autenticación Allauth

# Reemplaza con la configuración recomendada
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']


ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Añadir al final del archivo
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm',
}

# Configuraciones de password reset
ACCOUNT_PASSWORD_RESET_TIMEOUT_DAYS = 3  # Días de validez del enlace de reseteo



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yjra8918@gmail.com'  # Tu correo de Gmail
EMAIL_HOST_PASSWORD = 'ikne xwbw hleu aobw'  # Contraseña de aplicaciones (ver abajo)
DEFAULT_FROM_EMAIL = 'yjra8918@gmail.com'


