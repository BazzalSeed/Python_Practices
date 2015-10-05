#Peiyun Zeng
#DLList


import math
from ListNode import DListNode


#-----------------------------------------------------------------------------
class DLList(object):
    ''' The glorious Doublely Linked List Class'''

    # Constructor
    # Used the default to allow construct empty list and also be able to Create a whole list directly
    def __init__(self,seq=None):
        """
        pre:  if enter the sequence. Sequence needs to be either a list or string
        post: Creates an LList containing items in seq
        exception: TypeError if seq is neither List nor String 
        """

        #TypeError if seq not the right type
        if not ( isinstance(seq,str) or isinstance(seq,list) ) and seq != None:
            raise TypeError
        self.head=None
        self.tail=None
        self.size=0
        if seq == None:
            return
        for x in seq:
            self._append(x)

    #The __Str__ method        
#-----------------------------------------------------------------------------

    def __str__(self):
        '''
        post: returns a string representation of self
        '''
        l=[]
        node=self.head
        for i in self:
            l.append(i)
        
        return str(l)
    
    def __len__(self):
        '''
        post: returns number of items in the list
        '''
        return self.size
    

#The Find Method
#private method that returns node that is at location position
#in the list (0 is first item, size-1 is last item)
#-----------------------------------------------------------------------------

    def _find(self, position):
        '''
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the list
        Exception: Assertion Error if pre violated
        '''
        #Raise assertion error if pre not satisefied for my private method
        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

    #the accessor
#-----------------------------------------------------------------------------

    def __getitem__(self,index):
        '''
        pre: 0 <= abs(position) < size. allow use -1,-2... to index from the end
        post: returns data item at the specified position
        Exception: Exception Error if pre violated
        '''
        #Raise IndexError if pre violated
        if not (0 <= abs(index) < self.size):
            raise IndexError

        #convert index to the correct positive version
        if index < 0:
            index = self.size+index
         

        node = self._find(index)
        return node.value

    #the setitem method
    #allows changing list items via indexing and assingnment
#-----------------------------------------------------------------------------

    def __setitem__(self,index,value):
        '''
        pre: 0<=index<self.size, value should be an integer or a float or a string
        post: changes the value of the node at position index in the list to value
        Exception: IndexError if pre violated
        '''
        #Raise IndexError if pre violated
        if not (0 <= abs(index) < self.size):
            raise IndexError
        #convert index to the correct positive version
        if index < 0:
            index = self.size+index
        self._find(index).value=value



#the append method
#a private method to append to the end of the doubly linked list
#-----------------------------------------------------------------------------

    def _append(self,x):
        """appends x onto end of the list
        post: x is appended onto the end of the list"""
        newNode=DListNode(x)
        #General Case (not empty)
        if self.head is not None:
            node=self.tail
            newNode.link = node.link
            node.link=newNode
            newNode.rev=node
        #Empty MEthod
        else:
            self.head=newNode
            
        self.tail=newNode    
        self.size+=1

    #the insert method
    # insert value in position index
#-----------------------------------------------------------------------------

    def insert(self,index,value):
       
        '''
        pre: 0<=index<self.size, value should be an integer or a float or a string
        post: insert a new node whose value is value at the position index in the list
        Exception: IndexError if pre violated
        '''
        #IndexError if Pre Violated
        if not (0 <= abs(index) <= self.size):
            raise IndexError
        #Convert the index to the positive version
        if index < 0:
            index = self.size+index
        
        #If the index is the last position
        # apply append directly 
        if index == self.size:
            self._append(value)
            return

        #Other Cases
        newNode = DListNode(value)
        #when index is the 0, first position
        if index == 0:
            node = self._find(0)
            newNode.link = self.head
            self.head = newNode
            node.rev = newNode
        #general case
        else:
            node = self._find(index)
            prev = node.rev
            newNode.link = prev.link
            prev.link = newNode
            newNode.rev = prev
            node.rev = newNode
        self.size += 1


    #The del method
    #delete the value in position index   
#-----------------------------------------------------------------------------

    def __delitem__(self,position):
        '''
        pre: 1. position should be an integer to indicate the index of the value
             2. 0<= Abs(position) < self.size
        post: delete the value in position index in the list
        Exception: IndexError if pre violated
        '''
        #Raise IndexError if pre violated
        if not (0 <= abs(position) < self.size):
            raise IndexError


        #Convert negative number to correct positive index
        if position < 0:
            index = self.size+index

        #Delete Item at the begining
        if position==0:
            temp = self.head
            self.head=self.head.link
            temp.link == None
            
        #Delete Item at the end   
        elif position==self.size-1:
            

            temp = self.tail.rev
            self.tail=self.tail.rev
            
            d = temp.link
            temp.link=d.link
            d.rev = None
            
        #Delete item for general case   
        else:
           
            d = self._find(position)
            Next = d.link
            prev = d.rev
            
            Next.rev = prev
            prev.link = Next
            d.rev = None
            d.link = None

        
        self.size = self.size-1
        return



    #The pop method
    #return and remove the item at index of the list
#-----------------------------------------------------------------------------

    def pop(self,index=-1):
        '''
        pre: 0 <= abs(index) <= self.size
        post: 1. the item at index is returned
              2. the item at index is removed
        Exception: IndexError if pre violated
        '''
        if not (0 <= abs(index) < self.size):
            raise IndexError


        #Taking adavtange of well-constructed _find and __delitem__ method
        #GEt the item first
        #Delete it
        #Return it
        if index < 0 :
            index = index+self.size
        a = self._find(index).value
        self.__delitem__(index)
        return a



    #The index method
    #return the position of the first element that has value (value). iterating from the begining
#-----------------------------------------------------------------------------

    def index(self,value):
        '''
        pre: value should be the value of Listnode element that is inside the list
        post: return the first index of this value
        exception: ValueError if Pre Violated
        '''
        #Raise ValueError if pre violated
        if not value in self.__iter__():
            raise ValueError

        #Use iterator to go through the loop
        #Check which element has the value
        #Return the index
        a = 0
        for i in self:
            if i==value:
                return a
            a = a + 1
        
    # The remove method
    # remove the first element in the list with value (value). iterating from begining
#-----------------------------------------------------------------------------

    def remove(self,value):
        '''

        pre: value should be the value of Listnode element that is inside the list
        post: remove the first target "value" appears in the lis
        Exception: ValueError if pre violated
        '''

        #Raise ValueError if pre violated
        if not value in self.__iter__():
            raise ValueError


        #Check the index first
        #use __delitem__ to delete it
        index = 0
        for i in self:
            index = index +1
            if i==value:
                self.__delitem__(index-1)
                return
        self.size-=1
        
##    def _copy(self):
##        copyDLList=DLList()
##        for i in self.__iter__():
##            copyDLList.append(i)
##        return copyDLList
    
    def __iter__(self):
        """return an iterator for the list 
        post:return an iterator for the list """
        node=self.head
        while node is not None:
            yield node.value
            node=node.link
##    #        
##    def __reversed__(self):
##        """return a reversed iterator for the list
##        post:return a reversed iterator for the list"""
##        node=self.tail
##        while node is not None:
##            yield node.value
##            node=node.rev
##
##    

