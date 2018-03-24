"""
Settings_environ will import environmental settings
and sensitive information if the app is in production

If the app is run locally in a development
environment settings_developer will use settings in
your local settings_sensitive.py (not included in the
Git Repository)

If the app is run on a server in a production
environment settings_deploy will use sensitive keys set in
the server's environmental variables and then retrieved
through settings_environ: os.environ.get()
"""
import os

# Django Application Secret Key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
DOMAIN_NAME = os.environ.get('DOMAIN_NAME')

# ADMINS will receive error code notifications from the server when DEBUG=False
ADMINS = os.environ.get('ADMINS')
# MANAGERS will receive broken link notifications from the server when BrokenLinkEmailsMiddleware is enabled
MANAGERS = os.environ.get('ADMINS')

# Google reCaptcha
RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

# Google Maps
GOOGLE_MAPS_KEY = os.environ.get('GOOGLE_MAPS_KEY')

# Mapbox Key
MAPBOX_KEY = os.environ.get('MAPBOX_KEY')

# AWS S3 API Keys for Media File Upload and Storage
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Email Server Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get('EMAIL_PORT')
GUEST_USERNAME = os.environ.get('GUEST_USERNAME')
GUEST_PASSWORD = os.environ.get('GUEST_PASSWORD')
PERMISSION_REQUIRED = os.environ.get('PERMISSION_REQUIRED')
SERVER_EMAIL = os.environ.get('EMAIL_HOST_USER')
