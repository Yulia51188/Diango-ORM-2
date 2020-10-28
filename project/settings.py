import dj_database_url
import os

from environs import Env


env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = env.str("SECRET_KEY")

DATABASES = {
    'default': dj_database_url.parse(env.str("DB_URL"))
}


INSTALLED_APPS = ['datacenter']
ROOT_URLCONF = "project.urls"
ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
