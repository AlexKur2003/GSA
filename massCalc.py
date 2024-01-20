import numpy


def mass_calculation(fit, populationSize, m):
    mass_max = max(fit)
    mass_min = min(fit)
    if mass_max == mass_min:
        m = numpy.ones(populationSize)
    else:
        best = mass_min
        worst = mass_max

        for p in range(0, populationSize):
            m[p] = (fit[p] - worst) / (best - worst)

    m_sum = sum(m)
    for q in range(0, populationSize):
        m[q] = m[q] / m_sum  # normalization

    return m
