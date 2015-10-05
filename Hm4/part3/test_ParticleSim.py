#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#test_CounterSim.py
# unittest associated with the CounterSim.py source module

import sys
import random
import unittest

from ParticleSim import *


class TestParticleSim(unittest.TestCase):
    '''The unitTest for CounterSim'''

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def testEmpty_constructor(self):
        ''' Testing Constructor Method'''
        a = ParticleSim()
       
        time = a.now()
        self.assertEqual(0.0,time)
        
        

#---------------------------------------------------------------------------------
    def test_now(self):
        ''' Testing Now Method'''
        a = ParticleSim()

        t = a.now()

        self.assertEqual(0.0,t)

#---------------------------------------------------------------------------------
    def test_Insert(self):
        ''' Testing insertion method'''
        a = ParticleEvent(4)
        a1 = ParticleEvent(1)
        a2 = ParticleEvent(0)
        
        b = ParticleSim()
        b.insert(a)
        b.insert(a1)
        b.insert(a2)

        self.assertEqual(str(b.event),'[<Event: 0.0>*, <Event: 1.0>, <Event: 4.0>]')
        
 #---------------------------------------------------------------------------------       
    def test_Insert_Exception(self):
        ''' Testing insertion method for Exception'''
        try:
            a = ParticleSim()
            a.insert(4)
            self.assertTrue(False,'no exception or/ no right type of excepttion raised')
        except TypeError:
            pass
    
#---------------------------------------------------------------------------------
# The way to test Imporant Do All EVents are pretty primitive
# It will prints out the result, we have to check it manually
# I included the Initial events, will make checking process easier

#Case for n = 10, mean = 5, seed=None
#---------------------------------------------------------------------------------
    def test_DoAllEvents_10(self):
        '''Testing DoallEventsMethod'''
        a = ParticleSim()
        a.setup(10,5)
        print('********************************************************')
        print('##TEST for n = 10    mean = 5    seed=None')
        
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()
#Most Basic Case, one event with all default value
#---------------------------------------------------------------------------------
    def test_DoallEvents_one_initial_envent(self):
        '''Testing DoallEventsMethod'''
        a = ParticleSim()
        a.setup()
        print('********************************************************')
        print('##TEST   for   n = 1   mean = 4   seed =None')
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()



#Case for n = 30 , mean = 10  Seed = 3
#---------------------------------------------------------------------------------
    def test_DoAllEvents_30(self):
        '''Testing DoallEventsMethod'''
        a = ParticleSim()
        a.setup(30,10,3)
        print('********************************************************')
        print(' ##TEST For  n=30    mean = 10   seed = 3   ')
         
        
        print('Pay attention here to check whether the simulation driver is doing the rihgt thing')
        a.doAllEvents()



def main(argv):

    unittest.main()


if __name__ == '__main__':

    main(sys.argv)




