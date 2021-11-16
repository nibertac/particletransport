import numpy as np


class brownian:
    # initializes brownian w x,y,z parameters. self. walk=brownian(x,y,z) bc telling it to define itself
    def __init__(self, xi, yi, zi): #constructor
        # setting xi parameter position (so self.xi is location x on brownian(x,y,z))
        self.xi = xi
        self.yi = yi
        self.zi = zi

    def path(self, nsteps):  #define path itself, so path(100) means nsteps=100 so move 100 times
        # wiener motion, going to create an array w number of steps particle takes from initial position xi
        wx=np.ones(nsteps+1)*self.xi #array filled w same starting point xi
        wy=np.ones(nsteps+1)*self.yi #add one to include origin w number of steps
        wz=np.ones(nsteps+1)*self.zi
        walk=np.zeros((nsteps+1,3))#nsteps+1 is number of rows (add onw for start position) 3 dimensions
        walk[0]=[self.xi,self.yi,self.zi] #initial start position 0
    
    # randomly generate motion in x or y dir from starting point
        for i in range(1, nsteps+1): 
            xii = np.random.choice([-1, 1])
            yii = np.random.choice([-1, 1])
            zii = np.random.choice([-1, 1])
            # weiner process in each direction
            wx[i]=wx[i-1]+(xii/np.sqrt(nsteps)) #moving from previous point dont need cumsum()
            wy[i]=wy[i-1]+(yii/np.sqrt(nsteps))
            wz[i]=wz[i-1]+(zii/np.sqrt(nsteps))
            walk[i]=[wx[i],wy[i],wz[i]]
        print(walk)

        return walk