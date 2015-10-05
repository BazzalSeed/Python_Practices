#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
# Stack.py
# Implementation file for the Python class realizing the Stack ADT
# Originally by Thomas C. Bressoud
# for cs173, Spring 2014
# 02/02/2014
#------------------------------------------------------------------------------

from DLList import DLList
class Stack(DLList):
    '''
    Information:
      Collection of elements with a sequence from Last back to First for
      order of adding to the sequence (push operation), and where removal
      always occurs from the Last element (through pop operation).
    Information assumptions:
      Element data types can be anything, and can be mixed.
      Stack is not bounded.
    Implementation Representation:
      Representation of the Stack is a Self-Defiend Doubly Linked LIst list
    '''
#Constructor Method
#DONOT NEED IT HERE
#-----------------------------------------------------------------------------    
###------------------------------------------------------------------------------
##    def __init__(self):
##        '''
##        post: An Empty Stack (Last In First Out discipline) has been created
##        '''
##        self.items = []

#Top Method        
#------------------------------------------------------------------------------        
#------------------------------------------------------------------------------
    def top(self):
        '''
        pre: Stack must not be empty
        post: Returns value at TOS, but does not modify Stack
        Exceptions: IndexError if stack is empty
        '''
        #if the Stack is Empty
        #Raise IndexError
        if len(self) == 0:
            raise IndexError('the stack is empty')
        #return the top item without removing it
        return self[len(self)-1]


#Push Method        
#------------------------------------------------------------------------------     
#------------------------------------------------------------------------------
    def push(self, item):
        '''
        post: element is added to the top of stack, no return
        '''
        #append the item to the end of list(top of the stack)
        self._append(item)



#Isempty method        
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------
    def isEmpty(self):
        '''
        post: Returns boolean indicating whether or not the Stack has any elements
        '''
        #return true if stack is empty
        #return False if stack is False
        return len(self) == 0

# __str__Method   
# has to be redefined since we want to add our special * symbol to the first element
# ------------------------------------------------------------------------------  
#------------------------------------------------------------------------------
    def __str__(self):
        '''
        post: Returns string representation of stack, which is a list of elements
              starting with a [, comma separated list of elements, a trailing ], and 
              a '*' next to the first element, indicating the TOS
        '''
        
        #if stack is empty
        #return '[]'
        if len(self) == 0:
            return '[]'
        #construct the string representation of the stack
        a= self
        s = '['+ str(a[len(a)-1])+'*'
        for i in range (len(a)-2,-1,-1):
            s = s+', ' + str(a[i])
        s = s+ ']'
        return s

#------------------------------------------------------------------------------

