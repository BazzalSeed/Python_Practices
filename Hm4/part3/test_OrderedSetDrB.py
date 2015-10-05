#!/usr/bin/env python3
#------------------------------------------------------------------------------
# test_OrderedSetDrB.py
# unittest associated with the OrderedSet.py source module
# by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/22/2014
#------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '../src')

from OrderedSet import OrderedSet

class Event(object):
    def __init__(self, time=0.0, ident=None):
        self.t = float(time)
        self.ident = ident

    def __str__(self):
        if self.ident is None:
            return '<Event: %s>' % str(self.t)
        else:
            return '<Event: %s (%d)>' % (str(self.t), self.ident)

    def __lt__(self, other):
        if not isinstance(other, Event):
            raise TypeError("Attempt to use relational operator between Event and a non-Event")
        return self.t < other.t

    def __eq__(self, other):
        if not isinstance(other, Event):
            raise TypeError("Attempt to use relational operator between Event and a non-Event")
        return self.t == other.t

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return self < other or self == other

    def time(self):
        return self.t
    
class OrderedSetTest(unittest.TestCase):
        
    def testEmptyConstructor(self):
        S = OrderedSet()
        self.assertEqual(str(S), '[]')
        self.assertEqual(len(S), 0)

    def testInsertOne(self):
        S= OrderedSet()
        S.insert(5)
        self.assertEqual(str(S), '[5*]')
        S= OrderedSet()
        S.insert('a')
        self.assertEqual(str(S), '[a*]')
        S= OrderedSet()
        S.insert(1.5)
        self.assertEqual(str(S), '[1.5*]')

    def testInsertOneEvent(self):
        S= OrderedSet()
        evt = Event(5)
        S.insert(evt)
        self.assertEqual(str(S), '[<Event: 5.0>*]')
        S= OrderedSet()
        evt = Event(1.5)
        S.insert(evt)
        self.assertEqual(str(S), '[<Event: 1.5>*]')

    def testInsertTwoSameFloat(self):
        S= OrderedSet()
        val = 2.5
        S.insert(val)
        self.assertEqual(str(S), '[2.5*]')
        S.insert(val)
        self.assertEqual(str(S), '[2.5*]')
        self.assertEqual(len(S), 1)

    def testInsertTwoSameInt(self):
        S= OrderedSet()
        val = 10
        S.insert(val)
        self.assertEqual(str(S), '[10*]')
        S.insert(val)
        self.assertEqual(str(S), '[10*]')
        self.assertEqual(len(S), 1)

    def testInsertTwoSameEvent(self):
        S= OrderedSet()
        val = Event(2.5)
        S.insert(val)
        self.assertEqual(str(S), '[<Event: 2.5>*]')
        S.insert(val)
        self.assertEqual(str(S), '[<Event: 2.5>*]')
        
    def testInsertTwoSameEventModVal(self):
        S= OrderedSet()
        val = Event(2.5)
        S.insert(val)
        self.assertEqual(str(S), '[<Event: 2.5>*]')
        val.t = 5.0
        S.insert(val)
        self.assertEqual(str(S), '[<Event: 5.0>*]')

    def testInsertTwoDifferent(self):
        # Start with an inorder test
        S= OrderedSet()
        S.insert(2.5)
        self.assertEqual(str(S), '[2.5*]')
        S.insert(3.5)
        self.assertEqual(str(S), '[2.5*, 3.5]')
        self.assertEqual(len(S), 2)
        #Then an out of order test
        S= OrderedSet()
        S.insert(3.5)
        self.assertEqual(str(S), '[3.5*]')
        S.insert(2.5)
        self.assertEqual(str(S), '[2.5*, 3.5]')
        self.assertEqual(len(S), 2)

    def testInsertTwoDifferentEventDiffVal(self):
        # Start with an inorder test
        S= OrderedSet()
        evt1 = Event(2.5)
        S.insert(evt1)
        self.assertEqual(str(S), '[<Event: 2.5>*]')
        evt2 = Event(3.5)
        S.insert(evt2)
        self.assertEqual(str(S), '[<Event: 2.5>*, <Event: 3.5>]')

        #Then an out of order test
        S= OrderedSet()
        evt1 = Event(3.5)
        S.insert(evt1)
        self.assertEqual(str(S), '[<Event: 3.5>*]')
        evt2 = Event(2.5)
        S.insert(evt2)
        self.assertEqual(str(S), '[<Event: 2.5>*, <Event: 3.5>]')
    
    def testInsertTwoDifferentEventSameVal(self):
        # Start with an inorder test
        S= OrderedSet()
        evt1 = Event(2.5)
        S.insert(evt1)
        self.assertEqual(str(S), '[<Event: 2.5>*]')
        evt2 = Event(2.5)
        S.insert(evt2)
        self.assertEqual(str(S), '[<Event: 2.5>*, <Event: 2.5>]')

    def testInsertTwoDifferentEventSameValLastCheck(self):
        # Start with an inorder test
        S= OrderedSet()
        evt1 = Event(2.5, 1)
        S.insert(evt1)
        self.assertEqual(str(S), '[<Event: 2.5 (1)>*]')
        evt2 = Event(2.5, 2)
        S.insert(evt2)
        self.assertEqual(str(S), '[<Event: 2.5 (1)>*, <Event: 2.5 (2)>]')

    def testInsertMultiple(self):
        s = OrderedSet()
        s.insert(5)
        s.insert(-3)
        self.assertEqual(str(s), '[-3*, 5]')
        s = OrderedSet()
        s.insert(3.0)
        s.insert(2)
        s.insert(7)
        self.assertEqual(str(s), '[2*, 3.0, 7]')
        s = OrderedSet()
        s.insert('a')
        s.insert('c')
        s.insert('z')
        self.assertEqual(str(s), '[a*, c, z]')
        s = OrderedSet()
        s.insert(5)
        s.insert(2)
        self.assertEqual(str(s), '[2*, 5]')

    def testInsertMultipleEvent(self):
        s = OrderedSet()
        evt1 = Event(5)
        evt2 = Event(2.5)
        evt3 = Event(4.25)
        s.insert(evt1)
        s.insert(evt2)
        s.insert(evt1)
        s.insert(evt3)
        self.assertEqual(str(s), '[<Event: 2.5>*, <Event: 4.25>, <Event: 5.0>]')
        
    def testInsertMultipleEventChangeTime(self):
        s = OrderedSet()
        evt1 = Event(5, 1)
        evt2 = Event(2.5, 2)
        evt3 = Event(4.25, 3)
        s.insert(evt1)
        s.insert(evt2)
        s.insert(evt3)
        self.assertEqual(str(s), '[<Event: 2.5 (2)>*, <Event: 4.25 (3)>, <Event: 5.0 (1)>]')
        evt3.t = 6.0
        s.insert(evt3)
        self.assertEqual(str(s), '[<Event: 2.5 (2)>*, <Event: 5.0 (1)>, <Event: 6.0 (3)>]')

    def testRemoveFirstEmpty(self):
        #Then an out of order test
        S= OrderedSet()
        val = S.removeFirst()
        self.assertEqual(val, None)

    def testRemoveFirstEmptyInOut(self):
        #Then an out of order test
        S= OrderedSet()
        S.insert(5)
        val = S.removeFirst()
        self.assertEqual(val, 5)
        val = S.removeFirst()
        self.assertEqual(val, None)

    def testRemoveFirst(self):
        #Then an out of order test
        S= OrderedSet()
        
        S.insert(3.5)
        S.insert(2.5)
        val = S.removeFirst()
        self.assertEqual(val, 2.5)
        self.assertEqual(str(S), '[3.5*]')
        
        val = S.removeFirst()
        self.assertEqual(val, 3.5)
        self.assertEqual(str(S), '[]')

    def testRemove(self):
        s = OrderedSet()
        val1 = 5
        s.insert(val1)
        val2 = 3
        s.insert(val2)
        s.remove(val1)
        self.assertEqual(str(s), '[3*]')
        s = OrderedSet()

        val1 = 5
        s.insert(val1)
        val2 = 3
        s.insert(val2)
        val3 = 7
        s.insert(val3)
        s.remove(val1)
        self.assertEqual(str(s), '[3*, 7]')
        
        s = OrderedSet()
        val1 = 2.5
        s.insert(val1)
        val2 = 1.5
        s.insert(val2)
        val3 = 3.5
        s.insert(val3)
        s.remove(val1)
        self.assertEqual(str(s), '[1.5*, 3.5]')

        s = OrderedSet()
        val1 = 2.5
        s.insert(val1)
        val2 = 1.5
        s.insert(val2)
        val3 = 3.5
        s.insert(val3)
        s.remove(val2)
        self.assertEqual(str(s), '[2.5*, 3.5]')

        s = OrderedSet()
        val1 = 2.5
        s.insert(val1)
        val2 = 1.5
        s.insert(val2)
        val3 = 3.5
        s.insert(val3)
        s.remove(val3)
        self.assertEqual(str(s), '[1.5*, 2.5]')

    def testLen(self):
        s = OrderedSet()
        self.assertEqual(len(s), 0)
        s.insert(3)
        self.assertEqual(len(s), 1)
        s.insert(5)
        self.assertEqual(len(s), 2)
        s.insert(7)
        self.assertEqual(len(s), 3)

    def testBadRemove(self):
        try:
            s = OrderedSet()
            s.insert(9)
            s.insert(10.3)
            s.remove(4)
            self.assertTrue(False, 'no error on removing item not in set')
        except IndexError:
            self.assertTrue(True)
            
        try:
            s = OrderedSet()
            s.remove(6)
            self.assertTrue(False, ' no error on removing item from empty set')
        except IndexError:
            self.assertTrue(True)

    def testContains(self):
        s = OrderedSet()
        val1 = 2.0
        val2 = 3.0
        val3 = 4.0
        
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        
        self.assertTrue(s.__contains__(val1))
        self.assertTrue(s.__contains__(val2))
        self.assertTrue(s.__contains__(val3))
        
    def testNotContains(self):
        s = OrderedSet()
        val1 = 2.0
        val2 = 3.0
        val3 = 4.0
        s.insert(val1)
        s.insert(val3)
        self.assertFalse(s.__contains__(val2))
        
        s = OrderedSet()
        val1 = 2.0
        val2 = 3.0
        val3 = 4.0
        s.insert(val1)
        s.insert(val2)
        self.assertFalse(s.__contains__(val3))
        
        s = OrderedSet()
        val1 = 2.0
        val2 = 3.0
        val3 = 4.0
        s.insert(val2)
        s.insert(val3)
        self.assertFalse(s.__contains__(val1))

        s = OrderedSet()
        val1 = 2.0
        val2 = 3.0
        val3 = 4.0
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        s.removeFirst()
        self.assertFalse(s.__contains__(val1))

    def testContainsEvent(self):
        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(3.0)
        val3 = Event(4.0)
        
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        
        self.assertTrue(s.__contains__(val1))
        self.assertTrue(s.__contains__(val2))
        self.assertTrue(s.__contains__(val3))

        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(2.0)
        val3 = Event(2.0)
        
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        
        self.assertTrue(s.__contains__(val1))
        self.assertTrue(s.__contains__(val2))
        self.assertTrue(s.__contains__(val3))
        
    def testNotContainsEvent(self):
        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(2.0)
        val3 = Event(4.0)
        s.insert(val1)
        s.insert(val3)
        self.assertFalse(s.__contains__(val2))
        
        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(2.0)
        val3 = Event(4.0)
        s.insert(val1)
        s.insert(val2)
        self.assertFalse(s.__contains__(val3))
        
        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(2.0)
        val3 = Event(4.0)
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        s.removeFirst()
        self.assertFalse(s.__contains__(val1))

    def testIn(self):
        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(3.0)
        val3 = Event(4.0)
        
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        
        self.assertTrue(val1 in s)
        self.assertTrue(val2 in s)
        self.assertTrue(val3 in s)

        s = OrderedSet()
        val1 = Event(2.0)
        val2 = Event(2.0)
        val3 = Event(2.0)
        
        s.insert(val1)
        s.insert(val2)
        s.insert(val3)
        
        self.assertTrue(val1 in s)
        self.assertTrue(val2 in s)
        self.assertTrue(val3 in s)
        

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
