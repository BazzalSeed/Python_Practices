#!/usr/bin/env python3 
#------------------------------------------------------------------------------ 
# Seed Zeng 
# Test_CounterEvent Class
# A Unitest for COunterEvent Class
import sys
import unittest
from CounterSim import *

class CounterSimTest(unittest.TestCase):


#Important Notes: The str() method is tested along the way



#Test constructor
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------     
    def testConstructor(self):
        #Test Constructing two counterevents
        #Test through wether the CounterEvent info is correct
        a = CounterEvent(3)
        b = CounterEvent(3.5)
        self.assertEqual('<Event: 3.0>', str(a))
        self.assertEqual('<Event: 3.5>', str(b))


#Test Exception for constructor
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------  
    def testCounstructor_Exception(self):
        #Check the exception

        try:
            a = CounterEvent('Seed Is Silly')
            self.assertTure(False,'No Exception/or right type of Exception has been raised')
        except TypeError:
            pass
        #------------------------------------------------------------------------------
        try:
            a = CounterEvent([3,4])
            
            self.assertTure(False,'No Exception/or right type of Exception has been raised')
        except TypeError:
            pass


#Test the Camparision operators(overloaded    
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------          
    def test_Camparison_Operator_overloading(self):

        #Check Four Camparison methods(overloaded)


        #Construct First
        a = CounterEvent(3)
        b = CounterEvent(3.5)
        c = CounterEvent(0)


        #Check Them
        self.assertEqual(True, a!= b)
        self.assertEqual(False,a==b)

        self.assertEqual(True, a<b)
        self.assertEqual(False,a>b)
        
        self.assertEqual(True, a <= b)
        self.assertEqual(False,a >= b)

        

#Test the camparision exception
    def test_Camparison_Operator_overloading_Exception(self):

        a = CounterEvent(3)
        b = CounterEvent(3.5)

#Test all operators
#------------------------------------------------------------------------------ 
        try:
            a == 3.0
            self.assertTrue(False,'No Exception/or right type of Exception has been raised')

        except TypeError:
            pass
#------------------------------------------------------------------------------ 

        try:
            a != 3.0
            self.assertTrue(False,'No Exception/or right type of Exception has been raised')

        except TypeError:
            pass



#------------------------------------------------------------------------------ 

        try:
            a < 3.0
            self.assertTrue(False,'No Exception/or right type of Exception has been raised')

        except TypeError:
            pass

#------------------------------------------------------------------------------ 

        try:
            a > 3.0
            self.assertTrue(False,'No Exception/or right type of Exception has been raised')

        except TypeError:
            pass
#------------------------------------------------------------------------------ 

        try:
            a <= 3.0
            self.assertTrue(False,'No Exception/or right type of Exception has been raised')

        except TypeError:
            pass
    
#------------------------------------------------------------------------------ 

        try:
            a >= 3.0
            self.assertTrue(False,'No Exception/or right type of Exception has been raised')

        except TypeError:
            pass
        


#Test for time method
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------
    def test_time(self):
        a = CounterEvent(4)
        b = CounterEvent(5)
        c= CounterEvent(3.5)

        self.assertEqual(a.time(),4)
        self.assertEqual(b.time(),5)
        self.assertEqual(c.time(),3.5)
        


        



#Test for the most important Execute method
#1. Test both the value it retunrs(it prints)2.Whether it changed value after then
#3.and whether it has inserted itsel back to the right position ofEvents Collection of CounterSim
#------------------------------------------------------------------------------             
#Two Similar Test Cases
#------------------------------------------------------------------------------ 
    def test_execute(self):

#Case 1 event time at 0.0
#------------------------------------------------------------------------------ 
        a = CounterSim()
        a.setup(1)
        b = CounterEvent(0)

        self.assertEqual(b.time(),0.0)


        p = b.execute(a)

        #get the real list object
        l = a.getset().getset()

        #Check wether it has been rescheduled correclty
        self.assertEqual(b.time(),2.0)
        #Check the thing it retunrs(It prints out)
        self.assertEqual('The event time is 0.0',p)
        #CHeck whether it has been reinserted  back to the events collection correctly after rescheduleing
        self.assertTrue(l[1] is b)

#Case 2 event time at 2.0
#------------------------------------------------------------------------------ 
        a = CounterSim()
        a.setup(1)
        a.setup(13)
        b = CounterEvent(2.0)

        self.assertEqual(b.time(),2.0)


        p = b.execute(a)

        #get the real list object
        l = a.getset().getset()

        self.assertEqual(b.time(),4.0) 
        self.assertEqual('The event time is 2.0',p)
        self.assertTrue(l[1] is b)        
#Case 3 event time at 14.0 (So won't be reschedued and reinserted)
#------------------------------------------------------------------------------
        a = CounterSim()
        a.setup(1)
        a.setup(13)
        b = CounterEvent(14.0)

        self.assertEqual(b.time(),14.0)


        p = b.execute(a)

        #get the real list object
        l = a.getset().getset()

        self.assertEqual(b.time(),14.0) 
        self.assertEqual('The event time is 14.0',p)
        self.assertTrue(b not in l)        

def main(argv):

    unittest.main()


if __name__ == '__main__':

    main(sys.argv)
