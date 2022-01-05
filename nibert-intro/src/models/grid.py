import numpy as np
import math
from coordinate import coordinate
import random

#lengths in meters, time in seconds
L=1
R=.5
xc=.5
yc=.5
#zc always=0 since assume inlet of pipe is at z=0
segmentsize=.2 #Meters

class grid:
    def build_grid_map(self):
        sliceZ = math.floor(L/segmentsize) #number of slices, math.floor rounds down to nearest interger
        sliceXY = math.floor(2*R/segmentsize) #number of squares in grid is same in xy direction
        grid_map = {}
        for z in range (0, sliceZ):
            for x in range (0, sliceXY):
                for y in range (0, sliceXY):
                    key = str(math.floor(z/segmentsize)) + str(math.floor(x/segmentsize)) + str(math.floor(y/segmentsize))
                    grid_map[key] = 0
        
        return grid_map

    def countBubbles(self, radius, num_steps, num_particles, Deff, interval):
        sliceZ = math.floor(L/segmentsize) #math.floor rounds down to nearest interger
        sliceXY = math.floor(2*R/segmentsize) #number of squares in grid is same in xy direction
        # gridCoordinates = np.zeros((sliceZ*2*sliceXY,3)) #multidimensional array of every possible location/coordinate cubes, going to populate later
        grid_map = self.build_grid_map()

        for i in range (0, num_particles):
            prev_coordinate = coordinate(radius)

            # Add the starting location as a point in the map
            grid_x = math.floor(prev_coordinate.x/segmentsize)*sliceXY
            grid_y = math.floor(prev_coordinate.y/segmentsize)*sliceXY
            grid_z = math.floor(prev_coordinate.z/segmentsize)*sliceZ

            key = str(grid_z) + str(grid_x) + str(grid_y)
            grid_map[key] += 1

            for j in range (0, num_steps):
                psi = np.random.normal(0, 1) #prevcoord=prevcoord bc dont want to store values, just reassign to use for next value
                prev_coordinate.x=prev_coordinate.x+(psi*np.sqrt(2*Deff*interval)) #change in time is chosen?
                prev_coordinate.y=prev_coordinate.y+(psi*np.sqrt(2*Deff*interval))
                prev_coordinate.z=prev_coordinate.z+(psi*np.sqrt(2*Deff*interval))

                grid_x = math.floor(prev_coordinate.x/segmentsize)
                grid_y = math.floor(prev_coordinate.y/segmentsize)
                grid_z = math.floor(prev_coordinate.z/segmentsize)

                key = str(grid_z) + str(grid_x) + str(grid_y)
                grid_map[key] += 1 

        print(grid_map)

    #def generateOccurence(x, y, z, n_steps): #slice is number in grid/divides we're doing
        # sliceZ = math.floor(L/segmentsize) #math.floor rounds down to nearest interger
        # sliceXY = math.floor(2*R/segmentsize) #number of squares in grid is same in xy direction
        # gridCoordinates = np.zeros((sliceZ*2*sliceXY,3)) #multidimensional array of every possible location/coordinate cubes, going to populate later
        # initCoordinate = coordinate(x, y, z) #initial block that particle started in
        # for i in range(1, n_steps+1): 
        #     psi = np.random.normal(0, 1) #0 is mean, 1 is std, so goes to the left and right of zero by 1, so -1 to 1. Last number is size (we excluded bc default is 1, and we want one number)


        #   #NEW BY ME
        #   #creating initial coordinate
        #     theta = random.uniform(0, 2*math.pi)
        #     x = R*math.cos(theta)+xc  #on edge of pipe not centered at 0
        #     y = R*math.sin(theta)+yc
        #     z = random.uniform(0, L)

        #     nextCoordinate = initCoordinate.generateCoordinate(interval, Deff)
            
        #     rwx[i]=nextCoordinate.x
        #     rwy[i]=nextCoordinate.y
        #     rwz[i]=nextCoordinate.z
my_grid = grid()
my_grid.countBubbles(R, 5,5, .1, .01)