from django.http import HttpResponse
#from ws import settings
import tasks

def index(request):
    #tsk=tasks.task_test.delay()
    #tsk = tasks.gen_prime(10000)
    # mes = 'App: %s' % tsk

    tasks.gen_prime.delay(2000)
    mes = 'App: ignore_result'

    return HttpResponse(mes)


def index2(request):
    print '--> reload'
    return HttpResponse("app index2")
