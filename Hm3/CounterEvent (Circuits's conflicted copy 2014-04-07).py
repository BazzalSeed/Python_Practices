#!/usr/bin/env python3 
#------------------------------------------------------------------------------ 
# Seed Zeng 
# CounterEvent Class



from CounterSim import*
class CounterEvent(object):
    '''CounterEvent maintains the time information of the event and a execute semnatics.
       It is a building block of the DES.
       Important Notes: Two CounterEvent Objects can have the same time info but they are not the same events(objects)
    '''
    def __init__(self,t):
        '''
        pre: t is a number (float, int)
        post : a CounterEvent object, containing the time of event is created
        exception: TypeError if t is not a numeric type
        '''
        #Raise TypeError if t is neither float nor integer
        if not (isinstance(t,int) or isinstance(t,float) ):
            raise TypeError

        #Store in the time info
        self.item = float(t)
 #---------------------------------------------------------------------------------

    #string method
    def __str__(self):
        '''
        pre:None
        post:return a string represeantion of Counterevent Object
        '''

        #generate the string representation
        a = '<Event: '
        a = a + str(self.item) + '>'
        return a
 #---------------------------------------------------------------------------------

    #time method  
    def time(self):

        
        '''
        pre:None
        post:the time of the CounterEvent Object is returned
        '''
        #return the time
        return self.item
 #---------------------------------------------------------------------------------

    def __eq__(self,event):
        '''
        pre: event is a CounterEvent Object(given that self is a CounterEvent Object)
        post: 1. return true if self and event has the same time value
              2. return false if self and event has different time value
        exception: TypeError if event is not a CounterEvent Object
        '''
        #raise TypeError if event is not CounterEvent type
        if not isinstance(event,CounterEvent):
            raise TypeError

        
        return self.item == event.time()
 #---------------------------------------------------------------------------------

    def __lt__(self,event):
        '''
        pre: event is a CounterEvent Object(given that self is a CounterEvent Object)
        post: 1. return true if time of self < time of event
              2. return false otherwise
        exception: TypeError if event is not a CounterEvent Object
        '''
        #raise TypeError if event is not CounterEvent type
        if not isinstance(event,CounterEvent):
            raise TypeError
        return self.item < event.time()
 #---------------------------------------------------------------------------------

    def __ne__(self,event):
        '''
        pre: event is a CounterEvent Object(given that self is a CounterEvent Object)
        post: 1. return False if self and event has the same time value
              2. return True if self and event has different time value
        exception: TypeError if event is not a CounterEvent Object
        '''
        #raise TypeError if event is not CounterEvent type
        if not isinstance(event,CounterEvent):
            raise TypeError
        return not (self == event)


 #---------------------------------------------------------------------------------

    def __le__(self,event):
        '''
        pre: event is a CounterEvent Object(given that self is a CounterEvent Object)
        post: 1. return true if the time of self < =  the time of event
              2. return false otherwise
        exception: TypeError if event is not a CounterEvent Object
        '''

        #raise TypeError if event is not CounterEvent type
        if not isinstance(event,CounterEvent):
            raise TypeError
        return ( self == event or self < event)

 #---------------------------------------------------------------------------------

    def execute(self,sim):
        #Important note: Exception handling not supported here
        '''pre: sim is a CounterSim object/self is a correct CounterEvent Object
           post: the Counter event is executed as described 
                  1. print out The event time is : str(CounterEvent)
                  2. reschedule itself it time < 10
           exception: TypeError if sim is not a counterSim Object
           #YET! Canont do the excpetion handling here
        '''

        #raise TypeError if sim is not CounterSim type
       
        #if not (isinstance(sim,CounterSim)):
           #raise TypeError


        #Print The happen of the event
        #in the form of 'The event time is str(self)'
        p = 'The event time is '
        p = p + str(self)
        print (p)

        #if the current time is less than 10
        #Add 2 to the current time
        #insert the changed CounterEvent ojbect to the Event collection in CounterSim Object
        current = self.time()
        if current <10:
            current = current +2.0
            self.item = current
            sim.insert(self)
        return p
        
