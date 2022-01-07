import numpy as np
import math
from coordinate import coordinate
import random
from decimal import Decimal

#lengths in meters, time in seconds
L=Decimal('1')
R=Decimal('.5')
phi=Decimal('.2')
dp=Decimal('1500')
mu=Decimal('.000001')

#zc always=0 since assume inlet of pipe is at z=0
segmentsize=Decimal('.2') #Meters

class grid:
    def __init__(self): #constructor
        self.sliceZ = math.floor(L/segmentsize) #number of slices, math.floor rounds down to nearest interger
        self.sliceXY = math.floor(2*R/segmentsize) #number of slices in grid is same in xy direction

    def build_grid_map(self):
        grid_map = {}
        # adding 1 to go to the outside slice (things that would be at the wall)
        for z in range (0, self.sliceZ + 1):
            for x in range (0, self.sliceXY + 1): #for every possible value x for every z
                for y in range (0, self.sliceXY + 1): #ever possible value y for every possible combo zx
                    key = str(z*segmentsize) + '-' + str(x*segmentsize) + '-' + str(y*segmentsize)
                    grid_map[key] = 0
        
        grid_map['out-of-pipe'] = 0
        return grid_map

    def countBubbles(self, radius, num_steps, num_particles, Deff, interval):
        grid_map = self.build_grid_map()
        row_count = 0
        prev_coordinate = coordinate()

        for i in range (0, num_particles):
            prev_coordinate.generateCoordinate(radius, L)
            # Add the starting location as a point in the map
            grid_x = math.floor(prev_coordinate.x/segmentsize)*segmentsize
            grid_y = math.floor(prev_coordinate.y/segmentsize)*segmentsize
            grid_z = math.floor(Decimal(prev_coordinate.z)/segmentsize)*segmentsize

            key = str(grid_z) + '-' + str(grid_x) + '-' + str(grid_y)
            grid_map[key] += 1

            for j in range (0, num_steps):
                psi = Decimal(np.random.normal(0, 1)) #prevcoord=prevcoord bc dont want to store values, just reassign to use for next value
                row_count += 1

                prev_coordinate.calculate_velocity(dp, mu, L, R, interval, phi)

                prev_coordinate.x=prev_coordinate.x+prev_coordinate.vx + Decimal(psi*np.sqrt(2*Deff*interval)) #change in time is chosen?
                prev_coordinate.y=prev_coordinate.y+prev_coordinate.vy + Decimal(psi*np.sqrt(2*Deff*interval))
                prev_coordinate.z=prev_coordinate.z+prev_coordinate.vz + Decimal(psi*np.sqrt(2*Deff*interval))

                grid_x = math.floor(prev_coordinate.x/segmentsize)*segmentsize
                grid_y = math.floor(prev_coordinate.y/segmentsize)*segmentsize

                if (prev_coordinate.z < 0 or prev_coordinate.z > L):
                    key = 'out-of-pipe'
                else:
                    grid_z = math.floor(prev_coordinate.z/segmentsize)*segmentsize
                    key = str(grid_z) + '-' + str(grid_x) + '-' + str(grid_y)

                grid_map[key] += 1 

my_grid = grid()
my_grid.countBubbles(R, 5,5, Decimal('.00001'), Decimal('.1'))