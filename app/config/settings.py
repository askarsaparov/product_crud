import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-zxdj_f20tirz^8i&3@+#6g%-@5(u5oz8%1ydl%v0mb73mfn_h9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders",
    "django_elasticsearch_dsl",
]

LOCAL_APPS = [
    "accounts.apps.AccountsConfig",
    "product.apps.ProductConfig",
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # for front
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# Elasticsearch configuration
ELASTICSEARCH_DSL = {
    "default": {
        "hosts": f"http://{os.getenv('ELASTICSEARCH_HOST', 'localhost')}:{os.getenv('ELASTICSEARCH_PORT', '9200')}"
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=180),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=50),
    "UPDATE_LAST_LOGIN": True,
}

SWAGGER_SETTINGS = {
    "LOGIN_URL": "rest_framework:login",
    "LOGOUT_URL": "rest_framework:logout",
    "SECURITY_DEFINITIONS": {
        # 'Session Auth': {
        #     'type': 'apiKey',
        #     'name': 'Authorization',
        #     'in': 'header'
        # },
        # 'Token': {
        # 'type': 'apiKey',
        # 'name': 'Authorization',
        # 'in': 'header'
        # },
        "basic": {"type": "basic"},
    },
    "DEFAULT_MODEL_RENDERING": "example",
}

LOGIN_URL = "rest_framework:login"
LOGOUT_URL = "rest_framework:logout"

CORS_ORIGIN_ALLOW_ALL = True

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379',
#     }
# }
