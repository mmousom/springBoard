import numpy as np

class Forest(object):
    """
        Forest can grow trees which eventually die
    """
    #constructor
    def __init__(self,size=(150,150)):
        self.size = size
        self.trees = np.zeros(self.size, dtype=bool)
        self.fires = np.zeros(self.size, dtype=bool)
        
    # repr or representatoin class
    def __repr__(self):
        my_repr="{}(size={})".format(self.__class__.__name__,self.size)
        return my_repr
        
    def __str__(self):                   
         return self.__class__.__name__
         
    @property
    def num_cells(self):
         """number of cells available for growing trees"""
         return self[0].size * self[1].size
                  
                  