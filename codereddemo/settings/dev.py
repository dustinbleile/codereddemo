import logging

from .base import *  # noqa

# Get an instance of a logger
logger = logging.getLogger(__name__)

logger.warning("SECURITY WARNING: DEBUG set to True")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
