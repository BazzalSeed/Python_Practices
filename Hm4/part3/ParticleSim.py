#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#test_CounterSim.py


import random
from ParticleEvent import ParticleEvent
from OrderedSet import OrderedSet
class ParticleSim:
    '''
    CounterSim is the real driver for the DES simulation.
    The info 1. is an OrderedSet Whose Elements are CounterEvents
             2. and also a Virtual Time Keeper initially at 0.0
    '''

    #Constructor
    def __init__(self):
        '''
        pre: None
        post: An initial empty OrderedSet (the collection of CounterEvents later)
        '''
        #Construct the Empty CounterSim Object
        #Initialize the virtual time
        self.event = OrderedSet()
        self.t = 0.0

    #Current time method
    def now(self):
        '''
        pre:None
        post:return the current virtual time
        '''
        return self.t
    
    #Insertion Method
    def insert(self,x):
        
        '''
        pre: X is a CounterEvent Ojbect
        post: insert the CounterEvent to the event Collection(OrderedSet)
        exception:TypeErro if x  is not CounterEvent Object
        '''
        
        #raise typeError if x not the right Type
       
    
        if not isinstance(x,ParticleEvent):
            raise TypeError

        #insert if right type
        self.event.insert(x)

    #Setup Method
    def setup(self, n = 5, mean = 4, seed =None):
        

        
        
        #raise typeError if x not the right Type
        if not (isinstance(n,int)):
            raise TypeError
        if not (isinstance(mean,int) or isinstance(mean,float)):
            raise TypeError

        random.seed()
        for i in range(n):
            
            self.insert(ParticleEvent(random.expovariate(1/4)))

   # the simulation Engine method
    def doAllEvents(self):
        '''
        pre:None
        post:THe SImulator has porperly run
        '''
        #The main loop for carrying out DES

        #going through the Events collection
        #applying right method to it
        while len(self.event) > 0:
           
            event = self.event.removeFirst()

          
            self.t = event.time()
            event.execute()


##
##def main(argv):
##    #Construct the CounterSim obeject
##    #Set up the events Frist
##    #THen run
##    a = CounterSim()
##    a.setup()
##
##    a.doAllEvents()
##
##
##if __name__ == '__main__':
##
##    main(sys.argv)
