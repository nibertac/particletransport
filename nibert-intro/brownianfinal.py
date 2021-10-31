import numpy as np
import math
import random
import matplotlib as plt
from models.brownian1 import brownianClass

def main():
    R = .2  # radius of pipe (ft)
    L = 15  # length of pipe (ft)

    for i in range(2):  # number of trials
        print("running for loop")
        theta = random.uniform(0, 2*math.pi)  # pick any theta 0 to 2pi
        x = R*math.cos(theta)  # on edge of pipe
        y = R*math.sin(theta)
        z = random.uniform(0, L)  # random length
        loc = brownian(x, y, z)
        loc.joe("Hello World")
        loc.path(10)

if __name__ == '__main__':
    main()