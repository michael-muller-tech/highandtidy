from highandtidy.settings import *

#Remove debug toolbar from installed apps and middleware for tests
INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'debug_toolbar']
MIDDLEWARE = [mw for mw in MIDDLEWARE if mw != 'debug_toolbar.middleware.DebugtoolbarMiddleware']