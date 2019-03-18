
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'kmpx4w^#uojn@r@0b2kst6m^5-_tpkovnc-h%05#yx4s$*_759'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
	'sportscrud.apps.SportscrudConfig',
	'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'sports.urls'

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

WSGI_APPLICATION = 'sports.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sports',
        'USER': 'phdk',
		'PASSWORD': 'fraekfyr69',
		'HOST': 'localhost',
		'OPTIONS': {
			'charset': 'utf8',
			'use_unicode': True,
		},
    }
}

# LOGGING = {
# 	'version': 1,
# 	'formatters': {
# 		'console': {
# 			# exact format is not important, this is the minimum information
# 			'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s\n',
# 		},
# 	},
# 	'handlers': {
# 		'console': {
# 			'level': 'DEBUG',
# 			'class': 'logging.StreamHandler',
# 			'formatter': 'console',
# 		},
# 	},
# 	'loggers': {
# 		'django.db.backends': {
# 			'level': 'DEBUG',
# 			'handlers': ['console', ],
# 		},
# 	}
# }


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
