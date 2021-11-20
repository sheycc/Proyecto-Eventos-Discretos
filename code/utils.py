import math
from random import random

# Variables aletorias
def norm_distribution(m, x):
    r = 0
    while 1:
        rn = random()
        e = expo_distribution(1)
        c = math.exp((-(e - 1)** 2) / 2)
        if rn <= c:
            r = m + x * e
            break 
    return r

def expo_distribution(l):
    rn = random()
    r = - (1 / l) * math.log(rn)
    return r

def unif_distribution(f):
    r, c, rn = 0, 0, random()
    for a, b in f:
        c += b
        if rn < c:
            r = a
            break
    return r