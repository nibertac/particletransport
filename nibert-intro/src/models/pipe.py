from abc import abstractmethod, ABC, abstractproperty

class pipe(ABC): #dont know shape, but know we have to generate coordinate and calculate velocity
    x = abstractproperty 
    y = abstractproperty 
    z = abstractproperty
    vx = abstractproperty 
    vy = abstractproperty 
    vz = abstractproperty  

    @abstractmethod #interface, no implementation of code. the class cylinder and box are gonna implement these methods
    def generate_coordinate(self):
        pass

    @abstractmethod
    def calculate_velocity(self, dp, mu, x, y, z, interval, phi):
        pass

    @abstractmethod
    def get_segmentsize(self):
        pass

    @abstractmethod
    def z_slice(self):
        pass

    @abstractmethod
    def y_slice(self):
        pass
    
    @abstractmethod
    def x_slice(self):
        pass

    @abstractmethod
    def is_out_of_pipe(self, pipe):
        pass