import numpy
import random
import math


def g_field(populationSize, dimensions, pos, M, l, iters, G, ElitistCheck, Rpower):
    final_per = 2
    if ElitistCheck == 1:
        kbest = final_per + (1 - l / iters) * (100 - final_per)
        kbest = round(populationSize * kbest / 100)
    else:
        kbest = populationSize

    kbest = int(kbest)
    ds = sorted(range(len(M)), key=lambda k: M[k], reverse=True)

    forces = numpy.zeros((populationSize, dimensions))

    for r in range(0, populationSize):
        for i in range(0, kbest):
            z = ds[i]
            if z != r:
                x = pos[r, :]
                y = pos[z, :]
                esum = 0
                for t in range(0, dimensions):
                    esum += ((x[t] - y[t]) ** 2)

                R = math.sqrt(esum)  # distance between particles

                for k in range(0, dimensions):
                    randnum = random.random()
                    forces[r, k] = forces[r, k] + randnum * (M[z]) * (
                                (pos[z, k] - pos[r, k]) / (R ** Rpower + numpy.finfo(float).eps))

    accelerations = numpy.zeros((populationSize, dimensions))
    for x in range(0, populationSize):
        for y in range(0, dimensions):
            accelerations[x, y] = forces[x, y] * G
    return accelerations
