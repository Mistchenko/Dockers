import os
from celery import Celery
import home
import settings


"""
broker='amqp://celery:ZJW46aE9rzkl@192.168.100.51:5672/test'
Exchange: test_celery, type='direct'
Queue: test_celery
routing_key: 'test_celery'



$ export C_FORCE_ROOT=true
$ celery  -A ws worker --loglevel=info

"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ws.settings')

apl = Celery('ws')

apl.config_from_object('django.conf:settings')
# apl.config_from_object('settings')

#apl.autodiscover_tasks(['app'])
apl.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
