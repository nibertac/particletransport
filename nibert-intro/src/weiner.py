import numpy as np
import math
import random
from models.brownian import brownian #from models folder
import matplotlib.pyplot as plt

from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
colors=cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')



R = .2  # radius of pipe (ft)
L = 15  # length of pipe (ft)
runs=5 #particles 

#plotttingggggggg

fig=plt.figure(figsize=(10,10),dpi=250)
ax=fig.add_subplot(111, projection='3d')
ax.grid(False)
ax.xaxis.pane.fill=ax.yaxis.pane.fill=ax.zaxis.pane.fill=False
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ziprun=list(range(1,runs+1))
for i, col in zip(ziprun, colors):    
    theta = random.uniform(0, 2*math.pi)  # pick any theta 0 to 2pi
    x = R*math.cos(theta)  # on edge of pipe
    y = R*math.sin(theta)
    z = random.uniform(0, L)  # random length
    b = brownian(x, y, z)
    path=b.path(10) #number of steps    
    start=path[:1] #0th index ([start:end],':' mean everything before or after, before 1 (0) then stop position is 1 )
    stop=path[-1:] #end is start -1
    #Plot the path
    ax.scatter3D(path[:,0], path[:,1], path[:,2], c=col,alpha=0.15,s=.05); #syntax w comma:for path x,y,z is 0th,1st,2nd element of path
    ax.plot3D(path[:,0], path[:,1], path[:,2], c=col, alpha=0.5,lw=1.25, ls='--')
    ax.plot3D(start[:,0], start[:,1], start[:,2], c=col, marker='*')
    ax.plot3D(stop[:,0], stop[:,1], stop[:,2], c=col, marker='o');
plt.title('brownian walk')
plt.show()