
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_m0s6z$y7-zbgw_7w26v%5r=hq!1+4)1ex5sov#16lfo2p^t9b'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'forums_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}