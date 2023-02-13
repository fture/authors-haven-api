from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='fowm1lsori2mfkxlap1psork2mvjFISL1fFmasfkQr2asfcvda')

ALLOWED_HOSTS = ['localhost', '0.0.0.0','127.0.0.1']


