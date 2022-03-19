import numpy as np
import math
import random
from decimal import Decimal
from pipe import pipe 

class box(pipe):

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
    def __init__(self, x, y, z, slicex): #constructor
        self.x = x
        self.y = y
        self.z = z 
        self.slicex = slicex
        self.xc = self.x/2
        self.yc = self.y/2
       
     
        self.segmentsize = Decimal(self.x/slicex)
        self.sliceZ = math.ceil(self.z/self.segmentsize)
        if (z%self.segmentsize != 0): #modulus, if no remainder (pipe is exact number of slices).
            #if pipe ends inbetween slices then add another slice to include edge and exiting particles
            self.sliceZ += 1
        self.slicey = math.ceil(self.y/self.segmentsize)
        if (y%self.segmentsize != 0):
            self.slicey += 1
        
    
    def generate_coordinate(self):
        self.x = random.uniform(0, float(self.x)) #on edge of pipe not centered at 0
        self.y = random.uniform(0, float(self.y))
        self.z = random.uniform(0, float(self.z)) #need self bc use outside of method, for the whole class
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
        return self.z < 0 or self.z > pipe.z or self.x < 0 or self.x > pipe.x or self.y < 0 or self.y > pipe.y #use pipe bc this is og size