from django.http import HttpResponse
# import logging
from ws import settings
from xl.apxl import Apxl


# logger = logging.getLogger()

def index(request):
    xl = Apxl('myBook')
    xl.write(1, 1, 'test 1')
    xl.write(1, 2, 'test 2')
    xl.save()

    mes = 'workbook: %s' % xl.name
    return HttpResponse(mes)


def index2(request):
    # logger.warning(settings.LOG_TEMPLATES['LDAP'].format(server='MyServer'))
    print '--> reload'
    return HttpResponse("app rsyslog")
