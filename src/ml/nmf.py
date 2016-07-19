"""
nmf.py

Daniel Wang
May 2016
"""

import numpy
import random
import math
import sys


def __dif_cost(a, b):
    dif = 0

    for i in range(numpy.shape(a)[0]):
        for j in range(numpy.shape(b)[1]):
            dif += pow(a[i, j] - b[i, j], 2)

    return dif


def factorize(v, pc=10, it=50, rate=None):
    ic = numpy.shape(v)[0]
    fc = numpy.shape(v)[1]

    w = numpy.matrix([[random.random() for j in range(pc)] for i in range(ic)])
    h = numpy.matrix([[random.random() for i in range(fc)] for i in range(pc)])

    cost = 0.0

    sys.stdout.write("nmf iteration - ")

    for i in range(it):
        wh = w * h
        pre_cost = cost
        cost = __dif_cost(v, wh) * 1.0

        # log
        if i % 10 == 0:
            sys.stdout.write("%d > " % i)

        if cost == 0 or math.fabs(pre_cost - cost) / cost < rate:
            break

        if rate is not None and math.fabs(pre_cost - cost) / cost < rate:
            print("End in iteration %d, pre_cost = %f, cost = %f" % (i, pre_cost, cost))
            break

        # update feature matrix
        hn = (numpy.transpose(w) * v)
        hd = (numpy.transpose(w) * w * h)

        h = numpy.matrix(numpy.array(h) * numpy.array(hn) / numpy.array(hd))

        # update weight matrix
        wn = (v * numpy.transpose(h))
        wd = (w * h * numpy.transpose(h))

        w = numpy.matrix(numpy.array(w) * numpy.array(wn) / numpy.array(wd))

    print(".")

    return w, h
