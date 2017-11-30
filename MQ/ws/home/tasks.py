from __future__ import absolute_import, unicode_literals
import time
from ws.celery import app


@app.task
def sleep_test():
    time.sleep(30)
    return 'sleep test'


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    # return results
