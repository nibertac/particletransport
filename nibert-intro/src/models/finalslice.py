#tracking particle is same once I choose shape 

import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
#from coordinate import coordinate
import random
from decimal import Decimal
from pipe import pipe
from cylinder import cylinder
from box import box

#lengths in cm, time in seconds
L=Decimal('50')



phi = Decimal('1')
dp = L * Decimal('3.19') 
mu = Decimal('.01') #.001 Pa*s = 1 cp 

#diffusion coeff in m/s

#zc always=0 since assume inlet of pipe is at z=0
#slicexy=Decimal('25') #Meters

class grid: 
    #wanna initialize, build grid, track particles, store location 
    def __init__(self, pipe): #constructor, pipe is parameter (what we're passing in), will be either grid(cylinder) or box 
        self.pipe = pipe   

    def build_grid_map(self): #size of array using slices in x, y, z determined in pipe 
        grid_map = np.zeros((self.pipe.x_slice(), self.pipe.y_slice(), self.pipe.z_slice())) #dont use class cylinder, it is now pipe bc not specific to shape 
        return grid_map


#main function we're calling
    def countBubbles(self, num_steps, num_particles, Deff, interval): #pass in self.deff and interval here and remove from calc vel
        grid_map = self.build_grid_map()
        row_count = 0
        prev_coordinate = self.pipe #reassigning class (pipe is cyl or box) so now prev coord calls all functions in that shape
        #use prev_coord instead of cylinder.generate_coordinate, or box.generate_coordinate, we are generalizing this now 
        out_of_pipe = 0 #originally nothing out of pipe, reassigned later

        x_coord =[]
        y_coord =[]
        z_coord =[]
        
        for i in range (0, num_particles): #white functions are abstract 
            prev_coordinate.generate_coordinate() #pipe.x is initial coord
            #store location of initial point of each particle in slice dictionary
            grid_x = math.ceil(prev_coordinate.x/self.pipe.get_segmentsize())
            grid_y = math.ceil(prev_coordinate.y/self.pipe.get_segmentsize())
            grid_z = math.ceil(Decimal(prev_coordinate.z)/self.pipe.get_segmentsize())
            
            grid_map[grid_x-1][grid_y-1][grid_z-1] += 1 #add one to this  x, y, z voxel. ex: gridmap[5,3,2] index starts at 0, so slice 5 is index 4
            x_coord.append(grid_x - 1)
            y_coord.append(grid_y - 1)
            z_coord.append(grid_z - 1)

            for j in range (0, num_steps): #creating path of each particle in i number of particles
                psi_x = Decimal(np.random.normal(0, 1))
                psi_y = Decimal(np.random.normal(0, 1))
                psi_z = Decimal(np.random.normal(0, 1)) #prevcoord=prevcoord bc dont want to store values, just reassign to use for next value
                #row_count += 1 

                prev_coordinate.calculate_velocity(dp, mu, prev_coordinate.x, prev_coordinate.y, prev_coordinate.z, interval, phi)

                prev_coordinate.x = prev_coordinate.x + prev_coordinate.vx*interval + Decimal(psi_x*np.sqrt(2*Deff*interval)) #change in time is chosen?
                prev_coordinate.y = prev_coordinate.y + prev_coordinate.vy*interval + Decimal(psi_y*np.sqrt(2*Deff*interval))
                prev_coordinate.z = prev_coordinate.z + prev_coordinate.vz*interval + Decimal(psi_z*np.sqrt(2*Deff*interval))

                #print('particle number', i, 'moved', j, 'steps before leaving pipe') #particle then step of particle

                if prev_coordinate.is_out_of_pipe(self.pipe):
                    out_of_pipe += 1
                    #print('particle', i, 'leaves pipe at', prev_coordinate.x, prev_coordinate.y, prev_coordinate.z, 'after', j, 'steps') #dont really need print all out of pipe particles
                    break #stops for this particle, continues for loop for next, once particle is out, its out
        
                 #turn x,y,z into array loc
                else:
                    grid_z = math.ceil(prev_coordinate.z/self.pipe.get_segmentsize())
                    grid_x = math.ceil(prev_coordinate.x/self.pipe.get_segmentsize())
                    grid_y = math.ceil(prev_coordinate.y/self.pipe.get_segmentsize())
                    grid_map[grid_x-1][grid_y-1][grid_z-1] += 1
                    x_coord.append(grid_x - 1)
                    y_coord.append(grid_y - 1)
                    z_coord.append(grid_z - 1)
            
        #print('The Results')
        #print(grid_map)
        print('out-of-pipe', out_of_pipe)
        #print(x_coord)

# creating figures
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
  
# setting color bar
        color_map = plt.cm.ScalarMappable(cmap = plt.cm.Greens_r)
        color_map.set_array(grid_map)
  
# creating the heatmap
        img = ax.scatter(x_coord, y_coord, z_coord, marker='s',
                 s=200, color='green')
        plt.colorbar(color_map)
  
# adding title and labels
        ax.set_title("3D Heatmap")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
  
# displaying plot
        plt.show()

#THIS IS WHAT I CHANGE EACH TIME
my_cylinder = cylinder(1, L, 80) #passing in x (diameter = .1cm), length, number of voxel in x dir
my_grid = grid(my_cylinder) #bc mycylinder is the implementation of pipe (grid takes in parameter of type pipe (which doesnt exist) but cylinder is type pipe)
my_grid.countBubbles(50, 50, Decimal('1E-5'), Decimal('.1')) #num_steps, num_particles, Deff, interval

#my_box = box(2, 1.5, 6, 10) #parameters of box are x, y, z, slicex
#my_boxgrid = grid(my_box) #grid takes in object of type pipe, box is type pipe bc box(pipe)
#my_boxgrid.countBubbles(5, 5, Decimal('2.3E-15'), Decimal('.1'))

#in cm, s, grams

