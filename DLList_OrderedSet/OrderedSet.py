#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#OrderedSet.py



import random
from DLList import DLList
class OrderedSet(object):
    '''The OrderedSet is an ordered collection of unique elements. with following operations
       Construction/Insertion/str/len/in/getset/remove/removeFirst
   '''
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def __init__(self):
        '''pre: None
           post: Construct the empty ordered Set
           
        '''

        self.set = DLList()
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def insert(self,x):
        '''pre: X is of the same type as the objects in OrderedSet
           post: X is inserted into OrderedSet (to the right position)
           
           
        '''
        
       

        #if x is already in the set
        #remove the existing one
        #insert x to the right position
        if x in self:
            self.remove(x)
            self.insert(x)
            return
        
            
        #if x not in the set
        #insert x to the right position
        index = len(self.set)
        
        for i in range(len(self.set)-1,-1,-1):
            
                
            if x <= self.set[i]:
                index = i
        if index == len(self.set):
            self.set.insert(index,x)
            return
        if self.set[index] == x:
            self.set.insert(index+1,x)
            return
             
            
        self.set.insert(index,x)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------    
    def __str__(self):
        '''
        pre:NOne
        Post: return a string representation of the orderedset
        '''

        #retur [] if the set is empty
        if len(self.set) == 0:
            return '[]'

        #generate the correct string representation for non-empty set
        s = '['
        s = s + str(self.set[0])+'*'
        
        for i in range (1,len(self.set)):

            s = s + ', ' + str(self.set[i])
        s = s + ']'
        return s
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def __contains__(self,x):
        '''pre: None
           post: 1. return True if x is inside the orderedset
                 2. return False otherwise
        '''

        #Check whether i 
        for i in self.set:
            if i is x:
                return True
        return False

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def remove(self,x):
        '''pre:element x is in the list
           post:elemnt x is removed from the list
           exception: IndexError if x is not in the list in the frist place
        '''
        #go into the set to check whether x is in the set
        #if it is, remove item x
        for i in self.set:
            if i is x:
                print(i)
                self.set.remove(i)
                return
        #raise IndexError if not found
        raise IndexError

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def removeFirst(self):
        '''
        pre:NOne
        post:1.removes and return the first element from the ordered set
             2. return None if the ordered set is empty
        '''

        #return None if the set is empty
        print(len(self))
        if len(self)==0:
            return None
        #pop the first item if not empty
        return self.set.pop(0)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def __len__(self):
        '''
        pre: None
        post:return the length of the ordered set
        '''

        return len(self.set)
                
