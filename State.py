'''
@author: Devangini Patel
'''

from NavigationData import *

class State:
    '''
    This class retrieves state information for social connection feature
    '''
    
    def __init__(self, name = None):
        if name == None:
            #create initial state
            self.name = self.getInitialState()
        else:
            self.name = name
    
    def getInitialState(self):
        """
        This method returns source place
        """
        initialState = "Bus Stop"
        return initialState


    def successorFunction(self):
        """
        This is the successor function. It finds all the places connected to the
        current place
        """
        return connections[self.name]
        
        
    def checkGoalState(self):
        """
        This method checks whether the current place is AI Lab
        """ 
        #check if the place is AI Lab
        return self.name == "AI Lab"