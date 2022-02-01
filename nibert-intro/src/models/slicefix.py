
import numpy as np
import math
from coordinate import coordinate
import random
from decimal import Decimal

#lengths in meters, time in seconds
L=Decimal('.1')
R=Decimal('.0508') #4 inch diameter pipe

phi=Decimal('.2')
dp=Decimal('.0145') #Pa = psi * .000145
mu=Decimal('.001') #.001 Pa*s = 1 cp 

#diffusion coeff in m/s

#zc always=0 since assume inlet of pipe is at z=0
#slicexy=Decimal('25') #Meters

class grid:
    def __init__(self, slicexy, radius): #constructor, empty so grid()
        self.segmentsize = 2*radius/slicexy
        self.sliceZ = math.ceil(L/self.segmentsize)#number of slices, math.ceiling rounds up to nearest interger
        if (L%self.segmentsize == 0): #modulus, if no remainder (pipe is exact number of slices).
            #if pipe ends inbetween slices then add another slice to include edge and exiting particles
            self.sliceZ += 1
        self.sliceXY = slicexy #number of slices in grid is same in xy direction
        

    def build_grid_map(self):
        grid_map = np.zeros((self.sliceZ, self.sliceXY, self.sliceXY))
        return grid_map

    def countBubbles(self, radius, num_steps, num_particles, Deff, interval):
        grid_map = self.build_grid_map()
        row_count = 0
        prev_coordinate = coordinate(R)

        for i in range (0, num_particles):
            prev_coordinate.generateCoordinate(radius, L) #why do i need this, so now can use self.x and self.y from gen coord
            #store location of initial point of each particle in the hashmap/ python dictionary
            grid_x = math.ceil(prev_coordinate.x/self.segmentsize)
            grid_y = math.ceil(prev_coordinate.y/self.segmentsize)
            grid_z = math.ceil(Decimal(prev_coordinate.z)/self.segmentsize)

            grid_map[grid_z-1][grid_x-1][grid_y-1] += 1 #index starts at 0, so slice 5 is index 4

            for j in range (0, num_steps): #creating path of each particle using intial above
                psi_x = Decimal(np.random.normal(0, 1))
                psi_y = Decimal(np.random.normal(0, 1))
                psi_z = Decimal(np.random.normal(0, 1)) #prevcoord=prevcoord bc dont want to store values, just reassign to use for next value
                row_count += 1

                prev_coordinate.calculate_velocity(dp, mu, L, R, interval, phi)

                prev_coordinate.x = prev_coordinate.x + prev_coordinate.vx*interval + Decimal(psi_x*np.sqrt(2*Deff*interval)) #change in time is chosen?
                prev_coordinate.y = prev_coordinate.y + prev_coordinate.vy*interval + Decimal(psi_y*np.sqrt(2*Deff*interval))
                prev_coordinate.z = prev_coordinate.z + prev_coordinate.vz*interval + Decimal(psi_z*np.sqrt(2*Deff*interval))

                #turn x,y,z into array loc
                
                grid_x = math.ceil(prev_coordinate.x/self.segmentsize)
                grid_y = math.ceil(prev_coordinate.y/self.segmentsize)

                if (prev_coordinate.z < 0 or prev_coordinate.z > L):
                    key = 'out-of-pipe'
                #add if statement for x and y being out of pipe
                else:
                    grid_z = math.ceil(prev_coordinate.z/self.segmentsize)
                    grid_map[grid_z-1][grid_x-1][grid_y-1] += 1 
            
        print('The Results')
        print(grid_map)



my_grid = grid(5,R)
my_grid.countBubbles(R, 5,5, Decimal('2.3E-15'), Decimal('.1'))


