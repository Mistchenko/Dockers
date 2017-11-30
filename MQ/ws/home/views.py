from django.http import HttpResponse
#from ws import settings
import tasks

def index(request):
    tasks.sleep_test.delay()  # sleep 30c

    #tasks.gen_prime.delay(2000)

    mes = 'App: ignore_result'
    return HttpResponse(mes)


def index2(request):
    print '--> reload'
    return HttpResponse("app index2")
