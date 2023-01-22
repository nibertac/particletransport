import numpy as np
import math
import random
from decimal import Decimal
from pipe import pipe 

class box(pipe): #box is type pipe, pipe here is not parameter

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
        self.width = self.x
        self.height = self.y
        self.length = self.z
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
        
    #check this math, generatin spot on perimeter
    #on edge of pipe not centered at 0. if x = 0 or x, then y is anything. if x isnt 0 or x, y is either 0 or y
    def generate_coordinate(self):
        self.x = random.uniform(0, float(self.x)) 
        if self.x != 0 or self.x != pipe.x: #pipe.x is original x value passed as parameter into box, not new one reassigned
            self.y = random.choice([0, self.y])  #anywhere on x axis on bottom (y=0) or top (y=slicey)
        else:
            self.y = random.uniform(0, self.y) #if particle along top or bottom, then y is either top or bottom
        self.z = random.uniform(0, float(self.z)) 
    
    def calculate_velocity(self, dp, mu, x, y, z, interval, phi): 
        self.vz = 5
        #NEED AN EQUATION FOR VELOCITY IN A BOX 

    def get_segmentsize(self): 
        return self.segmentsize #length and width of each voxel

    def z_slice(self):
        return self.sliceZ

    def y_slice(self):
        return self.slicey
        
    def x_slice(self):
        return self.slicex

    def is_out_of_pipe(self, pipe):
        return self.z < 0 or self.z > self.length or self.x < 0 or self.x > self.width or self.y < 0 or self.y > self.height #use pipe bc this is og size