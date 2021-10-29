import numpy as np
class brownianClass:
    def __init__(self,xi,yi,zi): #initializes brownian w x,y,z parameters. self. walk=brownian(x,y,z) bc telling it to define itself
        self.xi=xi #setting xi parameter position (so self.xi is location x on brownian(x,y,z))
        self.yi=yi
        self.zi=zi

    def joe(self, message):
        print("brownian message")
        print(message)

    def path(self,nsteps=100): #move 100 times
        #wiener motion, going to create an array w number of steps particle takes from initial position xi
        wx=np.ones(nsteps)*self.xi #array filled w same starting point xi
        print("brownian path method call")
        print(np.ones(nsteps))
        wy=np.ones(nsteps)*self.yi
        wz=np.ones(nsteps)*self.zi
        #randomly generate motion in x or y dir
        for i in range(1,nsteps):
            xii=np.random.choice([-1,1])
            yii=np.random.choice([-1,1])
            zii=np.random.choice([-1,1])
            wx[i] = wx[i-1]+(xii/np.sqrt(nsteps)) #weiner process in each direction
            wy[i] = wy[i-1]+(yii/np.sqrt(nsteps))
            wz[i] = wz[i-1]+(zii/np.sqrt(nsteps))