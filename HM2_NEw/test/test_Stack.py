#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#test_Stack.py
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
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------            
    def testEmptyConstructor(self):
        #Initialize the stack
        S = Stack()
        # check wether the stack is constructed
        self.assertEqual(str(S), '[]')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------    
    def testPushOne(self):
        # test push method
        # test 3 different elements into the stack
        # wether the stack status is correct
        S= Stack()
        S.push(5)
        self.assertEqual(str(S), '[5*]')
        S= Stack()
        S.push('a')
        self.assertEqual(str(S), '[a*]')
        S= Stack()
        S.push(1.5)
        self.assertEqual(str(S), '[1.5*]')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------    
    def testPushTwo(self):
        # Test to (multiple times) push two elements on the stack and verify
        # the str() version of the stack with the expected

        #First Test Case

        #Initialize the stack
        s = Stack()
        #push in two elements
        s.push(5)
        s.push(2)
        #Check the status of the stack
        self.assertEqual(str(s),'[2*, 5]')
#------------------------------------------------------------------------------  
        #Second Test Case (float)

        #Initialize the stack
        s = Stack()
        #push in two elements
        s.push(3)
        s.push(1)
        #Check the status of the stack
        self.assertEqual(str(s),'[1*, 3]')
#------------------------------------------------------------------------------        
        #Third Test Case(string)

        #Initialize the stack
        s = Stack()
        #push in two elements
        s.push('seed')
        s.push('silly')
        #Check the status of the stack
        self.assertEqual(str(s),'[silly*, seed]')
       
                
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------            
    def testPushMany(self):
        # Test to push many elements on the stack and verify
        # the str() version of the stack with the expected

        #first Test Case/ numbers(float and integers)
        s = Stack()
        s.push(5)
        s.push(2)
        s.push(1.5)
        self.assertEqual(str(s),'[1.5*, 2, 5]')
#------------------------------------------------------------------------------   
        #Second Test Case/strings
        s = Stack()
        s.push('silly')
        s.push('is')
        s.push('seed')
        self.assertEqual(str(s),'[seed*, is, silly]')

        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------    
    def testpop(self):
        # Test pushing one, and then two values, and performing a pop and checking
        # that the right value is returned by each pop and that the str() version
        # of the stack is correct.

        #Initialize the stack 
        s = Stack()
        #push 2 itmes in
        s.push(5)
        s.push(3)

        #test pop by both return value and the stack status
        self.assertEqual(str(s.pop()),'3')
        self.assertEqual(str(s),'[5*]')
                    
        self.assertEqual(str(s.pop()),'5')
        self.assertEqual(str(s),'[]')
        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------            
    def testpopEmpty_empty(self):
        # First of a series of tests to check proper exception being thrown by a
        # violation of precondition.  In this case, the pop() from an empty stack.
        s = Stack()

        #first Test Case
        try:
            val = s.pop()
            self.assertTrue(False, "No exception / or not right type of excpetion rasied for pop of empty stack")
        except IndexError:
            self.assertTrue(True)
    def testpopEmpty_full_first(self):
    # Second of a series of tests to check proper exception being thrown by a
    # violation of precondition.
    #Second Test Case: push items to stack first then pop it to empty
        try:
            s = Stack()
            s.push(3)
            s.push(5)
            s.pop()
            s.pop()
            s.pop()
            self.assertTrue(False, "No exception / or not right type of excpetion rasied for pop of empty stack")
        except IndexError:
            self.assertTrue(True)
        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------            
    def testisEmpty(self):
        # Number of variations of testing the isEmpty() method, for both True and
        # False cases, and with 0, 1 , 2, and many elements in the stack, and after
        # a push/pop combination that takes the stack from empty to non-empty back
        # to empty.


        #Initialize the stack
        s = Stack()
        #Test True/False Cases
        self.assertEqual(True,s.isEmpty())
        s.push(1)
        self.assertEqual(False,s.isEmpty())
        s.push(1)
        self.assertEqual(False,s.isEmpty())

        #So now already have 2 items in stack s
        #Pop itmes off from the stack
        #meanwhile test the False case
        #stop when one item left
        for i in range(2):
            
            self.assertEqual(False,s.isEmpty())
            s.pop()

        #Check the True Case
        self.assertEqual(True,s.isEmpty())
        
#Extra Test for Len Method       
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------           
    #Test the len method
    def testLen(self):
        #initialize the stack
        s = Stack()
        #push three itmes into the stack
        for i in range(3):
            s.push(i)

        #Check the length
        self.assertEqual(len(s),3)
        
        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------                    
#Main Function
def main(argv):
    unittest.main()

#activate the main function
if __name__ == '__main__':
    main(sys.argv)
