from django.http import HttpResponse
#from ws import settings
import tasks

def index(request):
    #tsk=tasks.task_test()
    tsk = tasks.gen_prime(10000)

    mes = 'App: %s' % tsk

    return HttpResponse(mes)


def index2(request):
    print '--> reload'
    return HttpResponse("app index2")