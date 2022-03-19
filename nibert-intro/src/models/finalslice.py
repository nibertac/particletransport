#tracking particle is same once I choose shape 

import numpy as np
import math
from coordinate import coordinate
import random
from decimal import Decimal
from pipe import pipe
from cylinder import cylinder
from box import box

#lengths in meters, time in seconds
L=Decimal('.1')
R=Decimal('.0508') #also where it is centered 4 inch diameter pipe

phi=Decimal('1')
dp=Decimal('.0145') #Pa = psi * .000145
mu=Decimal('.001') #.001 Pa*s = 1 cp 

#diffusion coeff in m/s

#zc always=0 since assume inlet of pipe is at z=0
#slicexy=Decimal('25') #Meters

class grid:
    def __init__(self, pipe): #constructor, pipe will be either cylinder or box 
        self.pipe = pipe   

    def build_grid_map(self): #size of array sing slices in z, x, y determined in pipe 
        grid_map = np.zeros((self.pipe.z_slice(), self.pipe.x_slice(), self.pipe.y_slice())) #dont use class cylinder, it is now pipe bc not specific to shape 
        return grid_map

    def countBubbles(self, num_steps, num_particles, Deff, interval):
        grid_map = self.build_grid_map()
        row_count = 0
        prev_coordinate = self.pipe #pipe isn't a method. its an object, pipe is either cylinder or box 
        out_of_pipe = 0

        for i in range (0, num_particles):
            prev_coordinate.generate_coordinate() #pipe.x is initial coord
            #store location of initial point of each particle in the hashmap/ python dictionary
            grid_x = math.ceil(prev_coordinate.x/self.pipe.get_segmentsize())
            grid_y = math.ceil(prev_coordinate.y/self.pipe.get_segmentsize())
            grid_z = math.ceil(Decimal(prev_coordinate.z)/self.pipe.get_segmentsize())
            

            grid_map[grid_z-1][grid_x-1][grid_y-1] += 1 #add one to this z, x, y location. ex: gridmap[5,3,2] index starts at 0, so slice 5 is index 4

            for j in range (0, num_steps): #creating path of each particle in i number of particles
                psi_x = Decimal(np.random.normal(0, 1))
                psi_y = Decimal(np.random.normal(0, 1))
                psi_z = Decimal(np.random.normal(0, 1)) #prevcoord=prevcoord bc dont want to store values, just reassign to use for next value
                #row_count += 1 

                prev_coordinate.calculate_velocity(dp, mu, prev_coordinate.x, prev_coordinate.y, prev_coordinate.z, interval, phi)

                prev_coordinate.x = prev_coordinate.x + prev_coordinate.vx*interval + Decimal(psi_x*np.sqrt(2*Deff*interval)) #change in time is chosen?
                prev_coordinate.y = prev_coordinate.y + prev_coordinate.vy*interval + Decimal(psi_y*np.sqrt(2*Deff*interval))
                prev_coordinate.z = prev_coordinate.z + prev_coordinate.vz*interval + Decimal(psi_z*np.sqrt(2*Deff*interval))

                print(i, j) #particle then step of particle
               
                #turn x,y,z into array loc
                grid_x = math.ceil(prev_coordinate.x/self.pipe.get_segmentsize())
                grid_y = math.ceil(prev_coordinate.y/self.pipe.get_segmentsize())

                if prev_coordinate.is_out_of_pipe(self.pipe):
                    out_of_pipe += 1
                    print(i, prev_coordinate.x, prev_coordinate.y, prev_coordinate.z) #dont really need print all out of pipe particles
                    break #stops for this particle, continues for loop for next, once particle is out, its out
                    #key = 'out-of-pipe'
                    #grid_map[key] += 1
        
                #add if statement for x and y being out of pipe
                else:
                    grid_z = math.ceil(prev_coordinate.z/self.pipe.get_segmentsize())
                    grid_map[grid_z-1][grid_x-1][grid_y-1] += 1 
            
        print('The Results')
        print(grid_map)
        print('out-of-pipe', out_of_pipe)


#THIS IS WHAT I CHANGE EACH TIME
my_cylinder = cylinder(.116, L, 5) #passing in x, length, number of slices in x dir
my_grid = grid(my_cylinder) #bc mycylinder is the implementation of pipe (grid takes in parameter of type pipe (which doesnt exist) but cylinder is type pipe)
my_grid.countBubbles(5, 5, Decimal('2.3E-15'), Decimal('.1')) #num_steps, num_particles, Deff, interval

#my_box = box(2, 1.5, 6, 10) 
#my_boxgrid = grid(my_box) #grid takes in object of type pipe, box is type pipe bc box(pipe)
#my_boxgrid.countBubbles(5, 5, Decimal('2.3E-15'), Decimal('.1'))