#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#test_CounterSim.py
# unittest associated with the CounterSim.py source module

import sys
import random
import unittest

from CounterSim import*



class TestCounterSim(unittest.TestCase):
    '''The unitTest for CounterSim'''

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def testEmpty_constructor(self):
        ''' Testing Constructor Method'''
        a = CounterSim()
        t = a.getset()
        time = a.now()
        self.assertEqual(0.0,time)
        self.assertEqual('[]',str(t))
        

#---------------------------------------------------------------------------------
    def test_now(self):
        ''' Testing Now Method'''
        a = CounterSim()

        t = a.now()

        self.assertEqual(0.0,t)
#---------------------------------------------------------------------------------
    def test_now_not_emp(self):
        ''' Testing Now Method when not start from initial value'''
        a = CounterSim()
        a.setup(4)
        print('********************************************************')
        print('********************************************************')
        print('********************************************************')
   
        print('********************************************************')
        print('********************************************************')
        print('Not A part of DoAllEvents TEST')
        a.doAllEvents()
        t = a.now()
        

        self.assertEqual(10.0,t)
#---------------------------------------------------------------------------------
    def test_Insert(self):
        ''' Testing insertion method'''
        a = CounterEvent(4)
        a1 = CounterEvent(1)
        a2 = CounterEvent(0)
        
        b = CounterSim()
        b.insert(a)
        b.insert(a1)
        b.insert(a2)

        self.assertEqual(str(b.getset()),'[<Event: 0.0>*, <Event: 1.0>, <Event: 4.0>]')
        
 #---------------------------------------------------------------------------------       
    def test_Insert_Exception(self):
        ''' Testing insertion method for Exception'''
        try:
            a = CounterSim()
            a.insert(4)
            self.assertTrue(False,'no exception or/ no right type of excepttion raised')
        except TypeError:
            pass
#---------------------------------------------------------------------------------
    def test_SetUP(self):
        ''' Testing Setup method'''
        a = CounterSim()
        a.setup(3)
        a.setup(5)
        a.setup(1)

        self.assertEqual(str(a.getset()),'[<Event: 1.0>*, <Event: 3.0>, <Event: 5.0>]')
        
    
#---------------------------------------------------------------------------------
# The way to test Imporant Do All EVents are pretty primitive
# It will prints out the result, we have to check it manually
# I included the Initial events, will make checking process easier


#Most Basic Case, one event start at zero. 
#---------------------------------------------------------------------------------

    def test_DoallEvents_one_initial_envent(self):
        '''Testing DoallEventsMethod'''
        a = CounterSim()
        a.setup(0)
        print('********************************************************')
        print('##TEST for one event (time is less than 10)')
        print('##Initial Event: <Event: 0.0>')
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()
#Case for one event bigger than 10
 #---------------------------------------------------------------------------------
    def test_DoallEvents_one_Bigger_than_10(self):
        a = CounterSim()
        a.setup(0)
        print('********************************************************')
        print('##TEST for one event (time is bigger than 10)')
        print('##Initial event: <Event: 20.0>')
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()

#Case for all evnets less than 10
#---------------------------------------------------------------------------------
    def test_DoAllEvents_multiple_all_less_than_10(self):
        '''Testing DoallEventsMethod'''
        a = CounterSim()
        a.setup(0)
        a.setup(2.4)
        a.setup(5.4)
        a.setup(2)
        a.setup(3)
        print('********************************************************')
        print('##TEST for Multiple events_all (times of all less than time 10) ')
        print('##Initial events: <Event: 0.0> <Event: 2.0>  <Event: 2.4> <Event: 3.0> <Event: 5.4>')
        
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()
#Case for some evnets bigger than 10
#---------------------------------------------------------------------------------
    def test_DoAllEvents_multiple_some_bigger_than_10(self):
        '''Testing DoallEventsMethod'''
        a = CounterSim()
        a.setup(0)
        a.setup(2.4)
        a.setup(5.4)
        a.setup(2)
        a.setup(3)
        a.setup(11.4)
        a.setup(15.31415926)
        print('********************************************************')
        print('##TEST for Multiple events_all (times of some bigger than time 10) ')
        print('##Initial events: <Event: 0.0>  <Event: 2.0>  <Event: 2.4>  <Event: 3.0>  <Event: 5.4>  <Event: 11.4>  <Event: 15.1415926>')
        
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()



def main(argv):

    unittest.main()


if __name__ == '__main__':

    main(sys.argv)



