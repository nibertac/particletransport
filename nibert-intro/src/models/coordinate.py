import numpy as np
import math
import random
from decimal import Decimal

xc=Decimal('.5')
yc=Decimal('.5')

class coordinate:

    x = Decimal('0')
    y = Decimal('0')
    z = Decimal('0')
    vz = Decimal('0')
    vx = Decimal('0')
    vy = Decimal('0')

    #initializes random walk with x,y,z parameters. self. walk=brownian(x,y,z) bc telling it to define itself
    def __init__(self): #constructor
        self.x = 0
    
    def generateCoordinate(self, R, L): #constructor
        theta = random.uniform(0, 2*math.pi)
        self.x = R*Decimal(str(math.cos(theta)))+xc  #on edge of pipe not centered at 0
        self.y = R*Decimal(str(math.sin(theta)))+yc
        self.z = Decimal(str(random.uniform(0, float(L))))
    
    def calculate_velocity(self, dp, mu, L, R, interval, phi):
        radius=Decimal(math.sqrt((self.x-xc)**2+(self.y-yc)**2))
        self.vz=(-dp*(R**2-radius**2))/(4*mu*L*interval*phi)
       
