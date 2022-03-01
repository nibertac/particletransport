import numpy as np
import math
import random
from decimal import Decimal

# xc=Decimal('.0508') #in meters
# yc=Decimal('.0508') #in meters

# 1) create intial coordinate
# 2) create gridmap
# 3) create other coordinate and populate grid at same time

class coordinate:

    x = Decimal('0')
    y = Decimal('0')
    z = Decimal('0')
    vz = Decimal('0')
    vx = Decimal('0')
    vy = Decimal('0')
    xc = Decimal('0')
    yc = Decimal('0')

    #initializes class
    def __init__(self, radius): #constructor
        self.x = 0 
        self.xc = radius
        self.yc = radius #is located to the right of the y axis w length of radius
    
    def generateCoordinate(self, R, L): #constructor
        theta = random.uniform(0, 2*math.pi)
        #random_radius = Decimal(random.uniform(0, float(R))) #do you want particle to start on pipe wall
        self.x = R*Decimal(str(math.cos(theta)))+self.xc  #on edge of pipe not centered at 0
        self.y = R*Decimal(str(math.sin(theta)))+self.yc
        self.z = Decimal(str(random.uniform(0, float(L))))
    
    def calculate_velocity(self, dp, mu, L, R, interval, phi):
        radius=Decimal(math.sqrt((self.x-self.xc)**2+(self.y-self.yc)**2))
        self.vz=(-dp*(R**2-radius**2))/(4*mu*L) #do I need time interval in equation
       
# dont need self for radius bc already defined outside method?
# use self bc is a class variable/class member. it exists for every method inside the class. w/o self it only exists within the method block (ex: theta is only for gencoord)