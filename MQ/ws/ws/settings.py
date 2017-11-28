import os
from kombu import Exchange, Queue

# from logging.handlers import SysLogHandler

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'k0zg0kibq7lv3$vcodk0*6g&nq8yzgue_wfxvai%k1yy@5=myd'
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0']


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ws.urls'
WSGI_APPLICATION = 'ws.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'

# CELERY_BROKER_URL = 'amqp://localhost'
# CELERY_BROKER_URL = 'amqp://celery:ZJW46aE9rzkl@192.168.100.51:5672/test'
# CELERY_DEFAULT_QUEUE = 'test_celery'


BROKER_URL = 'amqp://celery:ZJW46aE9rzkl@192.168.100.51:5672/test'

CELERY_DEFAULT_QUEUE = 'test_celery'
CELERY_DEFAULT_EXCHANGE = 'test_exchange'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'test_celery'
CELERY_ACCEPT_CONTENT = ['json']

CELERY_QUEUES = (
    Queue('test_celery', exchange=Exchange('test_celery', type='direct'), routing_key='test_celery'),
)
