import numpy

g0 = 100
alfa = 20


def g_constant(t, iters):
    return g0 * numpy.exp(-alfa * float(t) / iters)
