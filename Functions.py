import numpy as np


def coordinates_set(width, height):
    s = set()
    for i in range(width):
        for j in range(height):
            s.add((i, j))
    return s