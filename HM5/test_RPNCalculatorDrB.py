#!/usr/bin/env python3
#------------------------------------------------------------------------------
# test_RPNCaclulator.py
# unittest associated with the RPNCalculator.py source module
# by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/02/2014
#------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '../src')

from RPNCalculator import RPNCalculator

class RPNCalculatorTest(unittest.TestCase):
        
    def testEmptyConstructor(self):
        S = RPNCalculator()
        self.assertEqual(str(S), '[]')

    def testPushOne(self):
        S = RPNCalculator()
        S.push(5)
        self.assertEqual(str(S), '[5*]')
        S = RPNCalculator()
        S.push(7.5)
        self.assertEqual(str(S), '[7.5*]')
          
    def testPushOneBadType(self):
        S = RPNCalculator()
        try:
            S.push('5')
            self.assertTrue(False, 'RPN Calc push of non-number failed to raise exception')
        except Exception as e:
            self.assertTrue(isinstance(e, TypeError), 'RPN Calc exception on push of non-number not a TypeError')

    def testPushTwo(self):
        S = RPNCalculator()
        S.push(5)
        S.push(3)
        self.assertEqual(str(S), '[3*, 5]')
        
    def testPushTwoBadType(self):
        S = RPNCalculator()
        try:
            S.push(5)
            S.push("a")
            self.assertTrue(False, 'No exception on RPNCalc push of non-numeric')
        except Exception as e:
            self.assertTrue(isinstance(e, TypeError), 'RPN Calc exception on push of non-number not a TypeError')

    def testAddInt(self):
        S = RPNCalculator()
        S.push(5)
        S.push(3)
        S.add()
        self.assertEqual(str(S), '[8*]')
        
    def testMulInt(self):
        S = RPNCalculator()
        S.push(5)
        S.push(3)
        S.multiply()
        self.assertEqual(str(S), '[15*]')
        
    def testSubInt(self):
        S = RPNCalculator()
        S.push(56)
        S.push(88)
        S.subtract()
        self.assertEqual(str(S), '[-32*]')

    def testAddFloat(self):
        S = RPNCalculator()
        S.push(5.5)
        S.push(3.75)
        S.add()
        self.assertEqual(str(S), '[9.25*]')
        
    def testDivInt(self):
        S = RPNCalculator()
        S.push(8)
        S.push(4)
        S.divide()
#        print(S)
        self.assertTrue(str(S) == '[2*]' or str(S) =='[2.0*]')

    def testAddThree(self):
        S = RPNCalculator()
        S.push(5)
        S.push(3)
        S.push(7)
        S.add()
        S.add()
        self.assertEqual(str(S), '[15*]')
        
    def testSimpleEval(self):
        S = RPNCalculator()
        val = S.evaluate('3')
        self.assertEqual(val, 3)
        self.assertEqual(str(S), '[3*]')
        
        S = RPNCalculator()
        val = S.evaluate('3 5')
        self.assertEqual(val, 5)
        self.assertEqual(str(S), '[5*, 3]')
        
        S = RPNCalculator()
        val = S.evaluate('3 5 7')
        self.assertEqual(val, 7)
        self.assertEqual(str(S), '[7*, 5, 3]')
        
    def testSimpleEvalWhitespace(self):
        S = RPNCalculator()
        val = S.evaluate(' 3')
        self.assertEqual(val, 3)
        self.assertEqual(str(S), '[3*]')
        
        S = RPNCalculator()
        val = S.evaluate('3 ')
        self.assertEqual(val, 3)
        self.assertEqual(str(S), '[3*]')

        S = RPNCalculator()
        val = S.evaluate(' 3 ')
        self.assertEqual(val, 3)
        self.assertEqual(str(S), '[3*]')

        S = RPNCalculator()
        val = S.evaluate('3\t5')
        self.assertEqual(val, 5)
        self.assertEqual(str(S), '[5*, 3]')
        
        S = RPNCalculator()
        val = S.evaluate('3  5')
        self.assertEqual(val, 5)
        self.assertEqual(str(S), '[5*, 3]')

        S = RPNCalculator()
        val = S.evaluate('3\t\t5')
        self.assertEqual(val, 5)
        self.assertEqual(str(S), '[5*, 3]')

    def testEvalAdd(self):
        S = RPNCalculator()
        val = S.evaluate('3 5 +')
        self.assertEqual(val, 8)
        self.assertEqual(str(S), '[8*]')

        S = RPNCalculator()
        val = S.evaluate('3 5 + 2 +')
        self.assertEqual(val, 10)
        self.assertEqual(str(S), '[10*]')

        S = RPNCalculator()
        val = S.evaluate('2 3 5 + +')
        self.assertEqual(val, 10)
        self.assertEqual(str(S), '[10*]')
        
    def testBadAdd(self):
        S = RPNCalculator()
        try:
            val = S.evaluate('2 + 3')
            self.assertTrue(False, 'Evaluate of bad combo failed to raise exception')
        except Exception as e:
            if not isinstance(e, ValueError):
                raise self.fail('RPN eval raised exception that is not ValueError')
            self.assertTrue(True)

    def testEvalExample3(self):
        S = RPNCalculator()
        val = S.evaluate('3 5 + 7 * 8 11 * -')
        self.assertEqual(val, -32)
        self.assertEqual(str(S), '[-32*]')
        
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)