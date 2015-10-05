#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
# Stack.py
# Implementation file for the Python class realizing the Stack ADT
# Originally by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/02/2014
#------------------------------------------------------------------------------

import math
import sys
from Stack import *
import ast
'''
#Special Notes. The way i implement the stack is to use python list
# I used the end of the list as the top of stack
# yet in __str__ method, when apply str to the object. It's gonna return a string representation in which the FIRST element is the TOP of the stack.
'''



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# RPN caculator Class
class RPNCaculator(object):
    
    '''
    Information assumptions:
      Maintains a stack containing current RPN expression evaluation values;
      these are always numbers, but never the operators from an RPN expression.
    '''

#------------------------------------------------------------------------------
    #Constractor
    def __init__(self):
        '''
        Pre:None
        post: Creates an RPNCalculator object instance with an empty value stack
        '''
        self.stack = Stack()
        
        
      
#------------------------------------------------------------------------------       
    # push method
    def push(self,item):
        '''
        pre: element is a numeric type
        post: element is added to the value stack and becomes the current TOS,
              with subsequent elements further along
        Exceptions: TypeError if element is not a number
        '''

        #Raise an Type Error if the thing pushed in is not numeric
        if not (isinstance(item,int) or isinstance(item,float) ):
            raise TypeError('Give me a number please')
    
        self.stack.push(item)

#------------------------------------------------------------------------------
    #pop method
    def pop(self):
        
        '''
        pre: value stack is not empty
        post: value stack has the top-of-stack element removed and this is the
              return value of the method
        Exceptions: IndexError if stack is empty
        '''

        # If the stack is empty, Raise the Index Error
        if len(self.stack) ==0:
            raise IndexError('The Stack is already empty')
        return self.stack.pop()
        
#------------------------------------------------------------------------------
    #add method
    def add(self):
        '''
        pre: value stack has at least two elements
        post: top two elements have been popped off the value stack and their sum
              has been pushed onto the value stack
        Exceptions: IndexError if value stack does not have two elements
        '''

        #If the stack does not have at least two elements
        #Raise IndexError
        if len(self.stack) < 2:
            raise IndexError ('Less than 2 numbers inside the stack')

        #The Addition Process
        # pop two elements off
        # add/get result
        #push it back to the top of the stack
        a= self.stack.pop()
        b = self.stack.pop()
        c = b+a
        self.stack.push(c)


#------------------------------------------------------------------------------

    #Subtraction Method
    def sub(self):
        '''
        pre: value stack has at least two elements
        post: Top two elements have been popped off the value stack and their subtraction result has been pushed onto the value stack
        Exceptions: IndexError if value stack does not have two elements
        '''
        #If the stack does not have at least two elements
        #Raise IndexError
        if len(self.stack) < 2:
            raise IndexError ('Less than 2 numbers inside the stack')

        #The Subtraction Process
        # pop two elements off
        # subtract/get result
        #push it back to the top of the stack
        a= self.stack.pop()
        b = self.stack.pop()
        c = b-a
        self.stack.push(c)

#------------------------------------------------------------------------------
    #Multiply method
    def mul(self):
        '''
        pre: value stack has at least two elements
        post: Top two elements have been popped off the value stack and their division result has been pushed onto the value stack
        Exceptions: IndexError if value stack does not have two elements
       
        '''


        #If the stack does not have at least two elements
        #Raise IndexError  
        if len(self.stack) < 2:
            raise IndexError ('Less than 2 numbers inside the stack')

        #The Multiplcation Process
        # pop two elements off
        # Multiply/get result
        #push it back to the top of the stack
        a= self.stack.pop()
        b = self.stack.pop()
        c = b*a
        self.stack.push(c)
        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

    #division method
    def div(self):
        '''
        pre: value stack has at least two elements
        post: Top two elements have been popped off the value stack and their division result has been pushed onto the value stack
        Exceptions: IndexError if value stack does not have two elements
        '''


        #If the stack does not have at least two elements
        #Raise IndexError  
        if len(self.stack) < 2:
            raise IndexError ('Less than 2 numbers inside the stack')


        #The Division Process
        # pop two elements off
        # Divide/get result
        #push it back to the top of the stack
        a= self.stack.pop()
        b = self.stack.pop()
        #Check the remainder to decide which division method i should apply
        d = b%a
        if d==0:
            c = b//a
            self.stack.push(c)
        else:
            c = b/a
            self.stack.push(c)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#Evaluation Method
#Task sequence is derived from the sequence user entered in
    def eval(self,task):
        '''
        pre: s is a string with a valid RPN (partial) expression where
             tokens in s (numbers and operators) are whitespace separated
        post: evaluates as much of the value of s as possible, using
              the rules of RPN expression evaluation, and return (without
              removing) the value on the top of the stack after eval
        Exceptions: TypeError if s is not a string
                    ValueError if problems occur in evaluation or there is not
                    an element at the top of the value stack on completion
                    
        '''
        # The operators
        OPS = ['+','-','*', '/']
        #if the input object is not a string
        #Raise TypeError
        if not isinstance(task, str):
            raise TypeError(' Enter a string man')

        #Split the string into python list
        task = str.split(task)

        #This loop is the real evaluation Method
        for i in task:

            #if the item in the input string is not whitespace/ not operator
            #push the numeric value back to the stack
            if i not in OPS and i != ' ':
                self.push(ast.literal_eval(i))

#------------------------------------------------------------------------------

            #When see the operator applying the corresponding method (addition/subtraction/Multplication/Division)
            else:

                #if problem happens during the process
                #raise ValueError
                if len(self.stack)<2:
                    raise ValueError ('The string you enter might not be in correct RPN Form')
                if i == '+':
                    self.add()
                if i == '-':
                    self.sub()
                if i == '*':
                    self.mul()
                if i == '/':
                    self.div()
            #on Completion, if there is not an item on the top of stack
            #Raise ValueError
            if len(self.stack) == 0:
                
                raise ValueError ('The string you enter might not be in correct RPN Form')
        return self.stack.top()


    #The __Str__ Method
    def __str__(self):
        '''
        Pre:none
        post: Returns string representation of stack, which is a list of elements
              starting with a [, comma separated list of elements, a trailing ], and 
              a '*' next to the first element, indicating the TOS
        '''
        

        #Take advantage of already contructed str method in Stack object
        return str(self.stack)


