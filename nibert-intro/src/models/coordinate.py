import numpy as np
import math
import random
from decimal import Decimal

xc=Decimal('.5')
yc=Decimal('.5')

class coordinate:
    #initializes random walk with x,y,z parameters. self. walk=brownian(x,y,z) bc telling it to define itself
    def __init__(self, R, L): #constructor
        theta = random.uniform(0, 2*math.pi)
        self.x = R*Decimal(str(math.cos(theta)))+xc  #on edge of pipe not centered at 0
        self.y = R*Decimal(str(math.sin(theta)))+yc
        self.z = Decimal(str(random.uniform(0, float(L))))
    
#DO I NEED THIS?
    def generateCoordinate(self, interval, Deff): 
    # randomly generate motion in x or y dir from starting point
        psi=np.random.normal(0, 1) #or random.gauss(mu, sigma)
         #0 is mean, 1 is std, so goes to the left and right of zero by 1, so -1 to 1. Last number is size (we excluded bc default is 1, and we want one number)

        #rwpt process in each direction
        calcX=self.x+(psi*np.sqrt(2*Deff*interval)) #change in time is chosen?
        calcY=self.y+(psi*np.sqrt(2*Deff*interval))
        calcZ=self.z+(psi*np.sqrt(2*Deff*interval))
        return coordinate(calcX, calcY, calcZ)