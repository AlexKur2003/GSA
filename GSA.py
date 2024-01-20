import numpy
from Gconstant import g_constant
from massCalc import mass_calculation
from gField import g_field
from move import make_move
from solution import Solution

ElitistCheck = 1
Rpower = 1


def gsa(func, populationSize, upperBound, lowerBound, dimensions, iterations):
    # coef = 1 if mode == "min" else -1
    s = Solution()
    vel = numpy.zeros((populationSize, dimensions))
    positions = numpy.random.randint(lowerBound, upperBound, (populationSize, dimensions))
    masses = numpy.zeros(populationSize)
    fit = numpy.zeros(populationSize)
    g_best = numpy.zeros(dimensions)
    g_best_score = float("inf")
    for k in range(0, iterations):
        for i in range(0, populationSize):

            # Calculate objective function for each particle
            fitness = func(positions[i, :])
            fit[i] = fitness

            if g_best_score > fitness:
                g_best_score = fitness
                g_best = positions[i, :]
        """ Calculating Mass """
        masses = mass_calculation(fit, populationSize, masses)

        """ Calculating Gravitational Constant """
        g = g_constant(k, iterations)

        """ Calculating G field """
        acc = g_field(populationSize, dimensions, positions, masses, k, iterations, g, ElitistCheck, Rpower)

        """ Calculating Position """
        positions, vel = make_move(populationSize, dimensions, positions, vel, acc)

        print(['At iteration ' + str(k + 1) + ' the best fitness is ' + str(g_best_score)])
    s.Algorithm = "GSA"
    s.best = g_best
    s.bestIndividual = g_best_score
    return s
