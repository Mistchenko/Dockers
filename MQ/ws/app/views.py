from django.http import HttpResponse
from ws import settings


def index(request):
    title = 'Index'
    mes = 'App: %s' % title
    return HttpResponse(mes)


def index2(request):
    print '--> reload'
    return HttpResponse("app index2")
