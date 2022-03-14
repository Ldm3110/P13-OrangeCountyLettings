from oc_lettings_site.settings import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# Install this MIDDLEWARE to manage the CSS display
MIDDLEWARE += [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ALLOWED_HOSTS = ['orange-county-lettings.herokuapp.com']

# SENTRY
sentry_sdk.init(
    dsn="https://5cb6d34c87ee461299c0caf179d55938@o1155628.ingest.sentry.io/6258479",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
