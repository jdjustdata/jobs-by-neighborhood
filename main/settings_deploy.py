"""
Django settings for a deployed project

Deployed settings are specific to the server
or production environment and should protect
sensitive information and web vulnerabilities.

These settings will be publicly available on a
Git Repository, and should not include any sensitive
keys or information.

Sensitive settings should be saved in:
1) Your local developer's settings_sensitive.py
for development environments
2) The server's environment variables
for production environments
In this way, sensitive keys and password information
will never be submitted to a public Git Repository
"""
import os
import dj_database_url
from settings import *
from settings_environ import *
from django.urls import reverse


DEBUG = True
# List of strings representing the host/domain names that can server this Django site
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'jobsbyneighborhood.herokuapp.com',
    'livelihoodjobs.org',
    '.herokuapp.com'
]

# Domain Name used to display on template views
DOMAIN_NAME = "liveliHOOD"
DOMAIN_ACRONYM = "JBN"
DOMAIN_URL = ""

# Media File Storage on Amazon S3
if AWS_STORAGE_BUCKET_NAME is None: AWS_STORAGE_BUCKET_NAME = ''
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'main.storage_backends.MediaStorage'
MEDIA_ROOT = 'https://s3.us-east-2.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME
MEDIA_URL = MEDIA_ROOT + '/assets/'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
