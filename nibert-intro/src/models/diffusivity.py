import numpy as np

class rwalk:
    #initializes random walk with x,y,z parameters. self. walk=brownian(x,y,z) bc telling it to define itself
    def __init__(self, x, y, z): #constructor
        self.x = x
        self.y = y
        self.z = z

    def path(self, n_steps, interval, Deff):  #define path itself, so path(10) means nsteps=10 so move 10 times
        #wiener motion, going to create an array w number of steps particle takes from initial position x
        rwx=np.ones(n_steps+1)*self.x #array of starting point (single line/ no rows) of size nsteps
        rwy=np.ones(n_steps+1)*self.y #add one to include origin w number of steps
        rwz=np.ones(n_steps+1)*self.z
        psi=np.zeros(n_steps+1)
        #interval time increment, between each step in seconds (assume constant number)
        randomwalk=np.zeros((n_steps+1,3))#all 0's, just determing size:nsteps+1 is # columns/length (add one for start position), 3 rows
        randomwalk[0]=[self.x,self.y,self.z] #initial start position 0
    
    # randomly generate motion in x or y dir from starting point
        for i in range(1, n_steps+1): 
            psi[i]=np.random.normal(0, 1) #0 is mean, 1 is std, so goes to the left and right of zero by 1, so -1 to 1. Last number is size (we excluded bc default is 1, and we want one number)
            #rwpt process in each direction
            rwx[i]=rwx[i-1]+(psi[i]*np.sqrt(2*Deff*interval)) #change in time is 1?
            rwy[i]=rwy[i-1]+(psi[i]*np.sqrt(2*Deff*interval))
            rwz[i]=rwz[i-1]+(psi[i]*np.sqrt(2*Deff*interval))
            randomwalk[i]=[rwx[i],rwy[i],rwz[i]]
        print(randomwalk)
        return randomwalk


mywalk = rwalk(.3,.3,.3)
#assume diffusive coeff of water is .0016mm2/s
mywalk.path(5,.001, .0000016)