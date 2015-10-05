#!/usr/bin/env python3
#------------------------------------------------------------------------------
# test_Stack.py
# unittest associated with the Stack.py source module
# by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/02/2014
#------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '../src')

from Stack import Stack

class StackTest(unittest.TestCase):
        
    def testEmptyConstructor(self):
        S = Stack()
        self.assertEqual(str(S), '[]')

    def testPushOne(self):
        S= Stack()
        S.push(5)
        self.assertEqual(str(S), '[5*]')
        S= Stack()
        S.push('a')
        self.assertEqual(str(S), '[a*]')
        S= Stack()
        S.push(1.5)
        self.assertEqual(str(S), '[1.5*]')

    def testPushTwo(self):
        S= Stack()
        S.push(5)
        self.assertEqual(str(S), '[5*]')
        S.push(3)
        self.assertEqual(str(S), '[3*, 5]')

    def testPushMany(self):
        S= Stack()
        S.push(5)
        S.push(3)
        S.push(7)
        S.push(8)
        S.push(3)
        self.assertEqual(str(S), '[3*, 8, 7, 3, 5]')

    def testpop(self):
        S = Stack()
        S.push(5)
        val = S.pop()
        self.assertEqual(val, 5)
        self.assertEqual(str(S), '[]')
        
        S = Stack()
        S.push(5)
        S.push(3)
        val = S.pop()
        self.assertEqual(val, 3)
        self.assertEqual(str(S), '[5*]')

    def testpopEmpty(self):
        S = Stack()
        try:
            S.pop()
            self.assertTrue(False, 'No exception on empty-stack pop()')
        except IndexError as e:
            self.assertTrue(True)

        S = Stack()
        try:
            S.push(1)
            S.push(2)
            S.pop()
            S.pop()
            S.pop()
            self.assertTrue(False, 'No exception on empty-stack pop()')
        except IndexError as e:
            self.assertTrue(True)

    def testisEmpty(self):
        
        S= Stack()
        self.assertEqual(S.isEmpty(), True, "failed initial creation empty")
        S.push(5)
        self.assertEqual(S.isEmpty(), False, "failed one push not empty")
        S.push(7)
        self.assertEqual(S.isEmpty(), False, "failed two push not empty")

        S= Stack()
        S.push(5)
        S.pop()
        self.assertEqual(S.isEmpty(), True, "failed push-pop empty")

        S= Stack()
        S.push(5)
        S.push(7)
        S.pop()
        self.assertEqual(S.isEmpty(), False)
        S.pop()
        self.assertEqual(S.isEmpty(), True)
        
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
