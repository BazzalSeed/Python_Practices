#!/usr/bin/env python3

#------------------------------------------------------------------------------
# Seed Zeng
# test_RPNCaclulator.py
# unittest associated with the RPNCalculator.py source module
# Originally by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/02/2014
#------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '../src')

from RPNCaculator import *

class RPNCalculatorTest(unittest.TestCase):

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------   
    def testEmptyConstructor(self):
        #initialize the Caculator
        S = RPNCaculator()
        #Check wether the empty stack is constructed
        self.assertEqual(str(S), '[]')
#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------
    def testPushOne(self):
        #Test the push method
        #pushing in only one element each time
        #and check the corresponding stack status

        S = RPNCaculator()
        S.push(5)

        self.assertEqual(str(S), '[5*]')
        S = RPNCaculator()

        S.push(7.5)
        self.assertEqual(str(S), '[7.5*]')

       
#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------          
    def testPushOneBadType(self):
        # Create an RPNCalculator and try to push a non-numeric ValueError

        try:
            s = RPNCaculator()
            s. push('Seed')
        except TypeError:
            pass

#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------
    def testPushTwo(self):
        # Create an RPNCalculator, push two values and compare string result
        s =  RPNCaculator()
        s.push(2)
        s.push(5)
        self.assertEqual(str(s),'[5*, 2]')

        s =  RPNCaculator()
        s.push(2)
        s.push(5.78)
        self.assertEqual(str(s),'[5.78*, 2]')

 

#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------        
    def testAddInt(self):
        #Test the addition of two integers


        # Benign test of two pushes
        # apply the add Method
        # Check just the resultant sum value on the stack
        s = RPNCaculator()
        s.push(2)
        s.push(5)
        s.add()
        #check just the result on the stack

        self.assertEqual(str(s),'[7*]')
        a = s.pop()
        self.assertEqual(a,7)


#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------        
    def testSubInt(self):
        # Test the subtraction of integers


        # Benign test of two pushes
        # Apply the subtraction Method
        # Check just the resultant subtraction value on the stack        
        s = RPNCaculator()
        s.push(2)
        s.push(5)
        s.sub()
        self.assertEqual(str(s),'[-3*]')
        a = s.pop()
        self.assertEqual(a,-3)
        
#------------------------------------------------------------------------------           
#------------------------------------------------------------------------------
    def testAddFloat(self):
        # Test the addition of the floats

        # Push two floats 
        # apply addition method
        # CHeck just the  resultant sum value on the stack
        s = RPNCaculator()
        s.push(2.3)
        s.push(5.7)
        s.add()
        self.assertEqual(str(s),'[8.0*]')
        a = s.pop()
        self.assertEqual(a,8)
        

        
#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------               
    def testAddThree(self):
        #Test adding of three numbers (Mixture of the floats and integers)

        #Push first two values onto the stack
        #Apply the addition (the sum back to the stack)
        #push the third to the stack
        #apply the addition
        #Check just the final resultant sum value on the stack
        s = RPNCaculator()
        s.push(3)
        s.push(5.7)
        s.add()
        s.push(2.3)
        s.add()
        self.assertEqual(str(s),'[11.0*]')
        a = s.pop()
        self.assertEqual(a,11.0)        
#------------------------------------------------------------------------------           
#------------------------------------------------------------------------------             
    def testSimpleEval(self):
        # Sequence of three eval tests, first evaluates a single number as the string
        # checks are both for the return value from the method as well as the contents
        # of the stack.  Next two test do the same for two numbers in string and three
        # numbers in string

        #Test for one number
        s = RPNCaculator()
        a = s.eval('2 ')
        self.assertEqual(str(s),'[2*]')
        self.assertEqual(a,2)
        #Test for two number
        s = RPNCaculator()
        a = s.eval('2 3 ')
        self.assertEqual(a,3)
        self.assertEqual(str(s),'[3*, 2]')
        #Test for three number
        s = RPNCaculator()
        a = s.eval('2 3 5')
        self.assertEqual(str(s),'[5*, 3, 2]')
        self.assertEqual(a,5)
        
       
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------   
    
    def testSimpleEvalWhitespace(self):
        # Number of eval tests with strings just being one or two numbers, but with
        # different cases of leading. trailing whitespace and use of tabs separating
        # tokens

        a = '  2    3    '
        b = ' 2 4        '
        c = '   2 4 '  # containing none-space white space(tab)


        #Test a (by both the return value and the status of the stack)
#------------------------------------------------------------------------------   
        s = RPNCaculator()
        a = s.eval(a)
        self.assertEqual(str(s),'[3*, 2]') 
        self.assertEqual(a,3)

        #Test b (by both the return value and the status of the stack)
#------------------------------------------------------------------------------           
        s = RPNCaculator()
        b = s.eval(b)
        self.assertEqual(str(s),'[4*, 2]') 
        self.assertEqual(b,4)

        #Test c (by both the return value and the status of the stack)
#------------------------------------------------------------------------------           
        s = RPNCaculator()
        c = s.eval(c)
        self.assertEqual(str(s),'[4*, 2]') 
        self.assertEqual(c,4)
        
  
        
    def testEvalAdd(self):
        # Combinations to check evaluate on multiple additions
        a ='3 5 +'
        b = ' 3 5 + 5 + 20 + 7 +'

        # Test a (by both the return value and the status of the stack)
#------------------------------------------------------------------------------   
        s = RPNCaculator()
        a = s.eval(a)
        self.assertEqual(str(s),'[8*]') 
        self.assertEqual(a,8)
        # Test b (by both the return value and the status of the stack)
#------------------------------------------------------------------------------           
        s = RPNCaculator()
        b = s.eval(b)
        self.assertEqual(str(s),'[40*]') 
        self.assertEqual(b,40)




#------------------------------------------------------------------------------   
#------------------------------------------------------------------------------                   
    def testBadAdd(self):
        # First of a sequence of tests intended to get a ValueError from the evaluate
        # method
        a = '3 + 5 '
        b = '3 5 + +'
        
#------------------------------------------------------------------------------   
        #Test a
        try:
            s = RPNCaculator()
            a = s.eval(a)
            self.assertTrue(False,'no excpetion /or not right type excpetion rasied for bad sequences')
        except ValueError:
            pass

#------------------------------------------------------------------------------           
        #Test b
        try:
            s = RPNCaculator()
            b = s.eval(b)
            self.assertTrue(False,'no excpetion /or not right type excpetion rasied for bad sequences')

        except ValueError :
            pass
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------               
    def testBadAdd_just_string_or_operators(self):
        #Second of a sequence of tests intended to get a ValueError from the evaluate

        a = '+ + - - 2'
        b = ' - - - 5 5 5 5'
        c = ' - - - + + +'
#------------------------------------------------------------------------------   
        #Test a
        try:
            s = RPNCaculator()
            a = s.eval(a)
            self.assertTrue(False,'no excpetion /or not right type excpetion rasied for bad sequences')
        except ValueError:
            pass

#------------------------------------------------------------------------------

        #Test b
        try:
            s = RPNCaculator()
            b = s.eval(b)
            self.assertTrue(False,'no excpetion /or not right type excpetion rasied for bad sequences')

        except ValueError :
            pass
#------------------------------------------------------------------------------

        #Test c
        try:
            s = RPNCaculator()
            c = s.eval(c)
            self.assertTrue(False,'no excpetion /or not right type excpetion rasied for bad sequences')

        except ValueError :
            pass        
        
        
          
    def testEvalExample_normal(self):
        # First of a number of tests intended to drive larger and more complicated
        # valid expression strings through eval, checking both the value returned by
        # the method and the final str() version of the value stack.
        a = '3 5 + 7 * 8 11 * - '
        b = '1 3 * 7 + 20 + '
        c = ' 4 2 / 4 + 3 * '
#------------------------------------------------------------------------------

        #Test evaluation of sequence a (by both the return value and the status of the stack)
        t = RPNCaculator()
        a = t.eval(a)
        self.assertEqual(-32,a)
        self.assertEqual(str(t),'[-32*]')
#------------------------------------------------------------------------------
        #Test evaluation of sequence b (by both the return value and the status of the stack)
        t = RPNCaculator()
        b = t.eval(b)
        self.assertEqual(30,b)
        self.assertEqual(str(t),'[30*]')
        #Test evaluation of sequence c (by both the return value and the status of the stack)
#------------------------------------------------------------------------------       
        t = RPNCaculator()
        c = t.eval(c)
        self.assertEqual(18,c)
        self.assertEqual(str(t),'[18*]')

    def testEvalExample_number_first(self):
        # Second of a number of tests intended to drive larger and more complicated
        # valid expression strings through eval, checking both the value returned by
        # the method and the final str() version of the value stack.
        a = '3 3 3 3 + + +'
        b = '2 2 2 2 * / +'
#------------------------------------------------------------------------------

        #Test evaluation of sequence a (by both the return value and the status of the stack)
        t = RPNCaculator()
        a = t.eval(a)
        self.assertEqual(12,a)
        self.assertEqual(str(t),'[12*]')
#------------------------------------------------------------------------------
        #Test evaluation of sequence b (by both the return value and the status of the stack)
        t = RPNCaculator()
        b = t.eval(b)
        self.assertEqual(2.5,b)
        self.assertEqual(str(t),'[2.5*]')
    
        
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
