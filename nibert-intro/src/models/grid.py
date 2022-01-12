import numpy as np
import math
from coordinate import coordinate
import random
from decimal import Decimal

#lengths in meters, time in seconds
L=Decimal('1')
R=Decimal('.0508') #4 inch diameter pipe

phi=Decimal('.2')
dp=Decimal('.0145') #Pa = psi * .000145
mu=Decimal('.001') #.001 Pa*s = 1 cp 

#diffusion coeff in m/s

#zc always=0 since assume inlet of pipe is at z=0
segmentsize=Decimal('.1') #Meters

class grid:
    def __init__(self): #constructor
        self.sliceZ = math.ceil(L/segmentsize) #number of slices, math.ceiling rounds up to nearest interger
        if (L%segmentsize == 0): #modulus, if no remainder (pipe is exact number of slices).
            #if pipe ends inbetween slices then add another slice to include edge and exiting particles
            self.sliceZ += 1
        self.sliceXY = math.ceil(2*R/segmentsize) #number of slices in grid is same in xy direction
        if ((2*R)%segmentsize == 0):
            self.sliceXY += 1

    def build_grid_map(self):
        grid_map = {}
        # adding 1 to go to the outside slice (things that would be at the wall or leaving pipe)
        for z in range (0, self.sliceZ):
            for x in range (0, self.sliceXY): #for every possible value x for every z
                for y in range (0, self.sliceXY): #ever possible value y for every possible combo zx
                    key = str(z*segmentsize) + '-' + str(x*segmentsize) + '-' + str(y*segmentsize)
                    grid_map[key] = 0
        
        grid_map['out-of-pipe'] = 0
        return grid_map

    def countBubbles(self, radius, num_steps, num_particles, Deff, interval):
        grid_map = self.build_grid_map()
        row_count = 0
        prev_coordinate = coordinate(R)

        for i in range (0, num_particles):
            prev_coordinate.generateCoordinate(radius, L)
            #store location of point in the hashmap/ python dictionary
            grid_x = math.floor(prev_coordinate.x/segmentsize)*segmentsize
            grid_y = math.floor(prev_coordinate.y/segmentsize)*segmentsize
            grid_z = math.floor(Decimal(prev_coordinate.z)/segmentsize)*segmentsize

            key = str(grid_z) + '-' + str(grid_x) + '-' + str(grid_y)
            grid_map[key] += 1

            for j in range (0, num_steps):
                psi = Decimal(np.random.normal(0, 1)) #prevcoord=prevcoord bc dont want to store values, just reassign to use for next value
                row_count += 1

                prev_coordinate.calculate_velocity(dp, mu, L, R, interval, phi)

                prev_coordinate.x = prev_coordinate.x + prev_coordinate.vx + Decimal(psi*np.sqrt(2*Deff*interval)) #change in time is chosen?
                prev_coordinate.y = prev_coordinate.y + prev_coordinate.vy + Decimal(psi*np.sqrt(2*Deff*interval))
                prev_coordinate.z = prev_coordinate.z + prev_coordinate.vz + Decimal(psi*np.sqrt(2*Deff*interval))

                grid_x = math.floor(prev_coordinate.x/segmentsize)*segmentsize
                grid_y = math.floor(prev_coordinate.y/segmentsize)*segmentsize

                if (prev_coordinate.z < 0 or prev_coordinate.z > L):
                    key = 'out-of-pipe'
                else:
                    grid_z = math.floor(prev_coordinate.z/segmentsize)*segmentsize
                    key = str(grid_z) + '-' + str(grid_x) + '-' + str(grid_y)

                grid_map[key] += 1 
            
        for key in grid_map.keys():
            print(key + ':  ' + str(grid_map[key]))

my_grid = grid()
my_grid.countBubbles(R, 5,5, Decimal('2.3E-15'), Decimal('.1')) #i messed this up