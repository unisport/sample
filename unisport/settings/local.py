from unisport.settings.base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

database_dir = os.path.join(BASE_DIR, 'databases')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': database_dir,
    }
}


#===========================
# Apps for local development
#===========================

INSTALLED_APPS += (
	'debug_toolbar',
	'django_extensions',
)


#==============================================================================
# Local Static Files location
#==============================================================================
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#==============================================================================
# Additional Local Middleware
#==============================================================================
MIDDLEWARE += [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]


#==============================================================================
# Third party app settings
#==============================================================================
#Django Debug Toolbar settings
#=============================
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]