#!/usr/bin/env python3
#------------------------------------------------------------------------------
# test_CounterEvent.py
# unittest associated with the CounterEvent.py source module
# by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/22/2014
#------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '../src')

from CounterEvent import CounterEvent

class Simulator(object):
    def __init__(self):
        self.t = 0.0
        self.list = []

    def __str__(self):
        s = '<' + str(self.t) + ': ['
        if len(self.list) == 0:
            return s + ']>'
        s += str(self.list[0])
        for i in range(1, len(self.list)):
            s += ', ' + str(self.list[i])
        s += ']>'
        return s
    
    def now(self):
        return self.t
    
    def insert(self, e):
        i = 0
        while i < len(self.list) and e >= self.list[i]:
            i += 1
        self.list.insert(i, e)
        
class CounterEventTest(unittest.TestCase):
        
    def testConstructor(self):
        e = CounterEvent(4)
        self.assertEqual(str(e), '<Event: 4.0>')
        e = CounterEvent(2)
        self.assertEqual(str(e), '<Event: 2.0>')
        e = CounterEvent(2.5)
        self.assertEqual(str(e), '<Event: 2.5>')
    
    def testBadConstructor(self):
        try:
            val = 'cat'
            CounterEvent(val)
            self.assertTrue(False, 'no exception non number CounterEvent')
        except TypeError:
            self.assertTrue(True)
            
    def testTime(self):
        e = CounterEvent(4)
        self.assertEqual(e.time(), 4.0)
        e = CounterEvent(9.4)
        self.assertEqual(e.time(), 9.4)
        
    def testEquals(self):
        e = CounterEvent(5)
        r = CounterEvent(9)
        self.assertFalse(e == r)
        e = CounterEvent(4)
        r = CounterEvent(4)
        self.assertTrue(e == r)
        self.assertTrue(r == e)
        e = CounterEvent(2)
        r = CounterEvent(2.0)
        self.assertTrue(e == r)
        
    def testLessThan(self):
        e = CounterEvent(5)
        r = CounterEvent(9)
        self.assertTrue(e < r)
        e = CounterEvent(4)
        r = CounterEvent(4)
        self.assertFalse(e < r)
        e = CounterEvent(2.5)
        r = CounterEvent(6.0)
        self.assertTrue(e < r)
        
    def testLessThanOrEquals(self):
        e = CounterEvent(5)
        r = CounterEvent(9)
        self.assertTrue(e <= r)
        e = CounterEvent(4)
        r = CounterEvent(4)
        self.assertTrue(e <= r)
        e = CounterEvent(2)
        r = CounterEvent(2.0)
        self.assertTrue(e <= r)
        e = CounterEvent(1.0)
        r = CounterEvent(13.2)
        self.assertTrue(e <= r)
        
    def testNotEqual(self):
        e = CounterEvent(5)
        r = CounterEvent(9)
        self.assertTrue(e != r)
        e = CounterEvent(4)
        r = CounterEvent(4)
        self.assertFalse(e != r)
        e = CounterEvent(2)
        r = CounterEvent(2.0)
        self.assertFalse(e != r)
        e = CounterEvent(1.0)
        r = CounterEvent(13.2)
        self.assertTrue(e != r)
    
    def testExecuteReturn(self):
        s = Simulator()
        e = CounterEvent(0)
        retval = e.execute(s).lower()
        self.assertEqual(retval, "the event time is 0.0")

        s = Simulator()
        e = CounterEvent(5.25)
        retval = e.execute(s).lower()
        self.assertEqual(retval, "the event time is 5.25")
        
        s = Simulator()
        e = CounterEvent(2)
        retval = e.execute(s).lower()
        self.assertEqual(retval, "the event time is 2.0")

    def testExecuteInsert(self):
        s = Simulator()
        e = CounterEvent(0)
        e.execute(s)
        self.assertEqual(str(s), "<0.0: [<Event: 2.0>]>")
        e = CounterEvent(5)
        e.execute(s)
        self.assertEqual(str(s), "<0.0: [<Event: 2.0>, <Event: 7.0>]>")

    def testExecuteInsertBig(self):
        s = Simulator()
        e = CounterEvent(12)
        e.execute(s)
        self.assertEqual(str(s), "<0.0: []>")

    def testExecuteInsert10(self):
        s = Simulator()
        e = CounterEvent(10)
        e.execute(s)
        self.assertEqual(str(s), "<0.0: []>")


def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)