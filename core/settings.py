import os.path
from pathlib import Path
import environ
from datetime import timedelta
from corsheaders.defaults import default_headers

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env.str('SECRET_KEY', default='0g5+cj7@be%61a+o)!h0qf)+&-w6(jnmnubg!$3p_)*5tw2ds$')

DEBUG = env.bool('DEBUG', default=True)
APPEND_SLASH = False

ALLOWED_HOSTS = ['*']

CUSTOM_APPS = [
    'core.account_management',
    'core.dashboard_site',
    'core.doctor',
    'core.patient',
    'core.appointment'
]

EXTERNAL_APPS = [
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_cleanup.apps.CleanupConfig',
    'corsheaders',
]

INSTALLED_APPS = [
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                 ] + EXTERNAL_APPS + CUSTOM_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # core middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'core.wsgi.application'
if env.bool('USE_MYSQL', default=False):
    DATABASES = {
        'default': {

            'ENGINE': 'django.db.backends.mysql',
            'NAME': env.str('MYSQL_DATABASE'),
            'USER': env.str('MYSQL_USER'),
            'PASSWORD': env.str('MYSQL_PASSWORD'),
            'HOST': env.str('MYSQL_HOST'),
            'PORT': env.str('MYSQL_PORT'),

            'OPTIONS': {
                'charset': 'utf8mb4',
                # 'collation': 'utf8mb4_unicode_ci',
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },

            "ATOMIC_MUTATIONS": True,

        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
        }
    }

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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, '../static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "core", "../static")
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../template'),
)

AUTH_USER_MODEL = 'account.UserBase'

# Basket session ID
BASKET_SESSION_ID = 'basket'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

################################################
# All Auth
################################################

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# Email Verification
ACCOUNT_EMAIL_VERIFICATION = False
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# redirect after confirmation
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/activation/done/'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/activation/done/'
# after registration the activation email has been sent to your mail box check it out
# ACCOUNT_SIGNUP_REDIRECT_URL = '/activation/sent/'
# DEFAULT_FROM_EMAIL = 'mohamedalmujtaba@mohamedalmujtaba.com'


ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'account_manager.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

# Custom user model
AUTH_USER_MODEL = 'account_management.User'
LOGIN_REDIRECT_URL = '/dashboard/admin/'
# LOGIN_URL = '/account/login/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 500
}

# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
