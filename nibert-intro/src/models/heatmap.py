# 3D Heatmap in Python using matplotlib
  
# to make plot interactive 
#%matplotlib
  
# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from decimal import Decimal
from pipe import pipe
from cylinder import cylinder
from box import box
from finalslice import grid
  
# creating a dummy dataset
grid = finals
# creating figures
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
  
# setting color bar
color_map = cm.ScalarMappable(cmap=cm.Greens_r)
color_map.set_array(colo)
  
# creating the heatmap
img = ax.scatter(x, y, z, marker='s',
                 s=200, color='green')
plt.colorbar(color_map)
  
# adding title and labels
ax.set_title("3D Heatmap")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
  
# displaying plot
plt.show()