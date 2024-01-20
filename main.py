import math
import numpy as np
from GSA import gsa


def sphere(x):
    return sum([element ** 2 for element in x])


def banana_func(xyz):
    x, y, z = xyz
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2 + (1 - y) ** 2 + 100 * (z - y ** 2) ** 2


def schwefels_function(x):
    n = len(x)
    sum_term = sum(-x[i] * math.sin(math.sqrt(abs(x[i]))) for i in range(n))
    return 418.9829 * n + sum_term


def ackleys_function(x):
    n = len(x)
    sum1 = np.sum(x**2)
    sum2 = np.sum(np.cos(2*math.pi*x))
    term1 = -20 * math.exp(-0.2 * math.sqrt(sum1/n))
    term2 = -math.exp(sum2/n)
    return term1 + term2 + 20 + math.e


def rastrigin(x):
    a = 10
    n = len(x)
    return a * n + sum([(xi**2 - a * np.cos(2 * np.pi * xi)) for xi in x])


print(rastrigin([-0.027477090998366815,0.01746835095420529,-0.054655771430109024]))
