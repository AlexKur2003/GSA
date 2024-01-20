import random


def make_move(populationSize, dimensions, positions, velocities, accelerations):
    for i in range(0, populationSize):
        for j in range(0, dimensions):
            r1 = random.random()
            velocities[i, j] = r1 * velocities[i, j] + accelerations[i, j]
            positions[i, j] = positions[i, j] + velocities[i, j]

    return positions, velocities
