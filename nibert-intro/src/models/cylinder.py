#given slice in x direction, y is same, find z
#specific to each shape is slices in x, y, z, veolocity, generate coordinate 

import numpy as np
import math
import random
from decimal import Decimal
from pipe import pipe 

class cylinder(pipe): #telling class cylinder it is a pipe type, all methods defined in pipe must be implemented here

#member variables in pipe abstract, must declare here 
    x = Decimal('0')
    y = Decimal('0')
    z = Decimal('0')
    vz = Decimal('0')
    vx = Decimal('0')
    vy = Decimal('0')
    xc = Decimal('0')
    yc = Decimal('0')

    #initializes class
    def __init__(self, x, z, slicex): #constructor
        self.x = x
        self.z = z 
        radius = Decimal(x/2)
        self.xc = radius
        self.slicex =  slicex
        self.yc = radius #is located to the right of the y axis w length of radius
        self.segmentsize = Decimal(2*radius/slicex)
        self.sliceZ = math.ceil(self.z/self.segmentsize) #number of slices, math.ceiling rounds up to nearest interger
        if (z%self.segmentsize != 0): #modulus, if  remainder isn't 0...
            #pipe ends inbetween slices then add another slice to include edge and exiting particles
            self.sliceZ += 1
        self.slicey = slicex
    
    def generate_coordinate(self):
        theta = random.uniform(0, 2*math.pi)
        R = Decimal(self.x/2)
        self.x = R*Decimal(str(math.cos(theta)))+self.xc  #on edge of pipe not centered at 0
        self.y = R*Decimal(str(math.sin(theta)))+self.yc
        self.z = Decimal(str(random.uniform(0, float(self.z)))) #need self bc use outside of method, for the whole class
        #R and theta only used in this method so local variables 
    
    def calculate_velocity(self, dp, mu, x, y, z, interval, phi): #even tho dont use y, need it bc box needs a y
        R = x/2
        radius=Decimal(math.sqrt((self.x-self.xc)**2+(self.y-self.yc)**2))
        self.vz=(-dp*(R**2-radius**2))/(4*mu*z) 

    def get_segmentsize(self): 
        return self.segmentsize #length and width of each voxel

    def z_slice(self):
        return self.sliceZ

    def y_slice(self):
        return self.slicey
        
    def x_slice(self):
        return self.slicex
    
    def is_out_of_pipe(self, pipe):
        return self.z < 0 or self.z > pipe.z or math.sqrt((self.x-self.xc)**2+(self.y-self.yc)**2) > 2*pipe.x #use pipe bc this is og size
#why is it pipe.z not cylinder? cylinder is type pipe but isn't this unique to clinder?
    