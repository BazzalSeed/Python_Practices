#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#test_CounterSim.py




import sys
from CounterEvent import *
from OrderedSet import *

class CounterSim(object):
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
       
    
        if not isinstance(x,CounterEvent):
            raise TypeError

        #insert if right type
        self.event.insert(x)

    #Setup Method
    def setup (self, t=0):

        '''
        pre: t is a numeric Type
        post: 1. construct COunterEvent with time t ( 0.0 if t not inptued)
              2. The constructed CounterEvent is inserted to the event collection (OrderedSet)
        Exception:TypeError if t is not a numeric type
        '''
        #raise typeError if x not the right Type
        if not (isinstance(t,int) or isinstance(t,float)):
            raise TypeError
        #Construct and insert the CounterEvent Object with t
        
        self.insert(CounterEvent(t))

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
            event.execute(self)

    #the getset method to get the ordered set (events collection in the simulator)
    
    def getset(self):
        '''
        pre:None
        post: the orderedSet (events collection) is returned
        '''

        return self.event



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
