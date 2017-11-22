import os
from celery import Celery
import home
import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ws.settings')

apl = Celery('ws')

apl.config_from_object('django.conf:settings')
# apl.config_from_object('settings')

#apl.autodiscover_tasks(['app'])
apl.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
