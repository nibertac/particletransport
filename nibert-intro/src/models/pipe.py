from abc import abstractmethod, ABC, abstractproperty

#allows you to create a set of methods that must be created within any child classes built from the abstract class.
#declaration but does not have an implementation

class pipe(ABC): #dont know shape, but know we have to generate coordinate and calculate velocity
    #x = abstractproperty 
    #y = abstractproperty 
    #z = abstractproperty
    #vx = abstractproperty 
    #vy = abstractproperty 
    #vz = abstractproperty  

    @abstractmethod #interface, no implementation of code. the class cylinder and box are gonna implement these methods

    #only create methods here that are unique to each shape 
    def generate_coordinate(self):
        pass

    @abstractmethod
    def calculate_velocity(self, dp, mu, x, y, z, interval, phi):
        pass

    @abstractmethod #cubic dimension of voxel
    def get_segmentsize(self):
        pass

    @abstractmethod
    def z_slice(self):
        pass

    @abstractmethod #number of slices in y = slice x in cylinder, not box
    def y_slice(self):
        pass
    
    @abstractmethod
    def x_slice(self):
        pass

    @abstractmethod
    def is_out_of_pipe(self, pipe):
        pass