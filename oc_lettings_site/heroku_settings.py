from oc_lettings_site.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# Install this MIDDLEWARE to manage the CSS display
MIDDLEWARE += [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
