from django.http import HttpResponse
import logging
from ws import settings


logger = logging.getLogger()


def index(request):
    logger.warning(settings.LOG_TEMPLATES['LDAP'].format(server='MyServer'))
    print '--> reload'
    return HttpResponse("app rsyslog")
