#!/usr/bin/env python3
#------------------------------------------------------------------------------
# test_CounterSim.py
# unittest associated with the CounterSim.py source module
# by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/22/2014
#------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '../src')

from CounterEvent import CounterEvent
from CounterSim import CounterSim

class CounterSimTest(unittest.TestCase):
        
    def testStartZero(self):
        sim = CounterSim()
        sim.setup(0.0)
        sim.doAllEvents()
        self.assertTrue(True)

    def testStartNotZero(self):
        sim = CounterSim()
        sim.setup(1.25)
        sim.doAllEvents()
        self.assertTrue(True)
        
    def testEmptySimulation(self):
        sim = CounterSim()
        sim.doAllEvents()
    
    def testSimulateTwo(self):
        sim = CounterSim()
        sim.setup(5)
        extra = CounterEvent(3)
        sim.insert(extra)
        sim.doAllEvents()
        self.assertTrue(True)
        
    def testSimulateBig(self):
        sim = CounterSim()
        sim.setup(20)
        sim.doAllEvents()    
        self.assertTrue(True)

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
