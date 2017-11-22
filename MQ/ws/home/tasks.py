from celery import shared_task
import time


@shared_task
def task_test():
    time.sleep(30)
    return 'task test'


@shared_task(ignore_result=True)
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    # return results
