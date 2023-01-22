#given slice in x direction, y is same, find z
#specific to each shape is slices in x, y, z, veolocity, generate coordinate 

import numpy as np
import math
import random
from decimal import Decimal
from pipe import pipe 

class cylinder(pipe): #telling class cylinder it is a pipe type, all methods defined in pipe must be implemented here

#whenever wanna call cylinder or box in other methods, pipe and cylinder switched, so whereevr we have method(pipe) pass word cylinder or box when implementing it later


#member variables in pipe abstract, must declare here 
#these are pipe.x, pipe.z in outofpipe method
    x = Decimal('0')
    y = Decimal('0')
    z = Decimal('0')
    vz = Decimal('0')
    vx = Decimal('0')
    vy = Decimal('0')
    xc = Decimal('0')
    yc = Decimal('0')

    #initializes class, can initialize w/ diff parameters than box
    def __init__(self, x, z, slicex): #constructor, what we pass in
        self.x = x #diameter
        self.z = z #length
        self.length = self.z
        self.radius = Decimal(x/2)
        self.xc = self.radius #s coord of center of pipe
        self.slicex =  slicex #number of slices
        self.yc = self.radius #is located to the right of the y axis w length of radius
        self.segmentsize = Decimal(2*self.radius/slicex) #we pass in the number of slices, get size (cm or mm of each voxel)
        self.sliceZ = math.ceil(self.z/self.segmentsize) #number of slices, math.ceiling rounds up to nearest interger
        if (self.z%self.segmentsize != 0): #modulus, if  remainder isn't 0...
            #pipe ends inbetween slices then add another slice to include edge and exiting particles
            self.sliceZ += 1
        self.slicey = slicex #same number of slices in x and y dir for circle
    
    def generate_coordinate(self): #starting location of particle is on surface of pipe
        theta = random.uniform(0, 2*math.pi)
        R = self.radius
        self.r = Decimal(R) - Decimal(.01) #decided thickness of where particles can come from is .001 from external radius

#do we wanna be able to change thickness a lot, so should we pass it in vs setting it as always .001 less than R
        Rad =  random.uniform(float(self.r), float(R)) #choose radius for origin of particle
    
        self.x = Decimal(Rad)*Decimal(str(math.cos(theta)))+self.xc  #on edge of pipe not centered at 0
        self.y = Decimal(Rad)*Decimal(str(math.sin(theta)))+self.yc
        self.z = Decimal(str(random.uniform(0, float(self.length)))) #need self bc use outside of method, for the whole class, reassigned from init
        #R and theta only used in this method so local variables 
    
    def calculate_velocity(self, dp, mu, x, y, z, interval, phi): #even tho dont use y, need it bc box needs a y
        #R = x/2
        radius = Decimal(math.sqrt((self.x-self.xc)**2+(self.y-self.yc)**2))
        self.vz = (-dp*(self.radius**2-radius**2))/(4*mu*self.length) 
        self.vx = 0
        self.vy = 0

    def get_segmentsize(self): 
        return self.segmentsize #length and width of each voxel

    def z_slice(self):
        return self.sliceZ

    def y_slice(self):
        return self.slicey
        
    def x_slice(self):
        return self.slicex
    
    def is_out_of_pipe(self, pipe): #only return if the conditions below exist?
        return self.z < 0 or self.z > self.length or math.sqrt((self.x-self.xc)**2+(self.y-self.yc)**2) > self.radius #use pipe bc this is og size
# self.z is class variable (same variable for every method), the z coordinate we constantly reassign. 
# pipe.z is original length of pipe, the length we pass into cylinder()

#add separate counter for back at wall and out of pipe in dir of flow