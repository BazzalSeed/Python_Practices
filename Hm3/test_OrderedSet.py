#!/usr/bin/env python3
#------------------------------------------------------------------------------
#Seed Zeng
#test_OrderedSet.py
# unittest associated with the OrderedSet.py source module


import sys
import random
import unittest
from CounterEvent import CounterEvent
from OrderedSet import OrderedSet

class TestOrdedSet(unittest.TestCase):
    '''The unitTest for OrderedSet'''

#Important Notes:
#                1.getset and __str__ methods are tested along the way. So no seperate test for these two
#                2.Getset method is created for later Testing the EXEcute method in CounterEvent



    
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------    
    def testEmptyConstructor(self):
        '''Test For Consturct the empty Set'''
        #Case1
        #Construct empty set first
        b = OrderedSet()
        self.assertEqual('[]',str(b))




        #Case2
        #insert in first the removeFirst to empty
#---------------------------------------------------------------------------------
        a = OrderedSet()
        a.insert(4)
        a.insert(5)
        a.insert(0)
        a.removeFirst()
        a.removeFirst()
        a.removeFirst()
        self.assertEqual('[]',str(a))
                        
        




#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------        
    def test_in_overloading(self):
        ''' Test the "in" operator overloading'''

        a = OrderedSet()
        event1 = CounterEvent(4)
        event2 = CounterEvent(5)
        event3 = CounterEvent(5.5)
        event4 = CounterEvent(4)
        a.insert(event1)
        a.insert(event2)
        a.insert(event3)
        self.assertEqual(True,event1 in a)
        self.assertEqual(False, event4 in a)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------          
    def test_camparison_Operators_overloading(self):
        '''Test Camparison Operators == /< /!= /<= overloading'''
        

        a = OrderedSet()
        event1 = CounterEvent(4)
        event2 = CounterEvent(5)
        event3 = CounterEvent(5.5)
        event4 = CounterEvent(4)
        #---------------------------------------------------------------------------------

        self.assertEqual(True,event1<event2)
        self.assertEqual(False, event1> event2)
        #---------------------------------------------------------------------------------
        self.assertEqual(True, event1==event4)
        self.assertEqual(False,event1!=event4)
        #---------------------------------------------------------------------------------
        self.assertEqual(True,event1 <= event4)
        self.assertEqual(True,event1 >= event4)
        #---------------------------------------------------------------------------------
        self.assertEqual(True,event1<=event3)
        self.assertEqual(False,event2<=event4)
        
        
                            
#---------------------------------------------------------------------------------            
#---------------------------------------------------------------------------------
    def testInsert_number(self):
        '''test the insert method---number(float and integer)'''

        a = OrderedSet()
        b = []

        #Generating Random Numbers to insert
        #so use getset method to check the result(cannot check the string representation
        for i in range(10):
            c = random.random()*random.randrange(100)
            a.insert(c)
            b.append(c)

        b = sorted(b)
        self.assertEqual(a.getset(),b)
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def testInsert_CounterEvent(self):
        temp = []
        event1 = CounterEvent(2)
        event2 = CounterEvent(1)
        event3 = CounterEvent(0.5)
        event4 = CounterEvent(1)

        #case1
        #Distinctive event time
        #CHeck both use str() method and getset method

        #The advantage of getset method is that we can automatically sort the obeject and check it with the set
        # So that donot have to manually check the string version
        #---------------------------------------------------------------------------------
        a = OrderedSet()
        a.insert(event1)
        temp.append(event1)

        a.insert(event2)
        temp.append(event2)

        a.insert(event3)
        temp.append(event3)

        self.assertEqual(a.getset(),sorted(temp))
        self.assertEqual('[<Event: 0.5>*, <Event: 1.0>, <Event: 2.0>]',str(a))
        #Case2
        #Reapted Event Time (different Objects)
        #---------------------------------------------------------------------------------
        temp = []
        a = OrderedSet()
        a.insert(event1)
        temp.append(event1)

        a.insert(event2)
        temp.append(event2)

        a.insert(event3)
        temp.append(event3)

        a.insert(event4)
        temp.append(event4)

        self.assertEqual(a.getset(),sorted(temp))
        self.assertEqual('[<Event: 0.5>*, <Event: 1.0>, <Event: 1.0>, <Event: 2.0>]',str(a))
        #Additional Check
        #Check the event 4 is after event 2(For events with same time, the event inserted later is after)
        b= a.getset()
        self.assertTrue(True,b[2] is event4)
        
    def testInsert_CounterEvent_reposition(self):
        '''Test Case for insertion------When thing to be inserted already in the set'''

        a=OrderedSet()
        event1 = CounterEvent(2)
        event2 = CounterEvent(1)
        event3 = CounterEvent(0.5)
        event4 = CounterEvent(4.5)

        #Insert Events in first
        #Check the result
        #Change Event 3
        #Check again(Event Time Is changed/ Event Order is not chagned (wrong order))
        #Insert Event 3
        #Check again (Now ORder Should be Corrected)
        #---------------------------------------------------------------------------------                      
        a.insert(event1)
        a.insert(event2)
        a.insert(event3)
        a.insert(event4)
        
        self.assertEqual('[<Event: 0.5>*, <Event: 1.0>, <Event: 2.0>, <Event: 4.5>]',str(a))

        event3.item = 4.75
        self.assertEqual('[<Event: 4.75>*, <Event: 1.0>, <Event: 2.0>, <Event: 4.5>]',str(a))
        print (a)

        a.insert(event3)
        self.assertEqual('[<Event: 1.0>*, <Event: 2.0>, <Event: 4.5>, <Event: 4.75>]',str(a))
    def testRemove(self):
        '''Test the remove Method'''
        a = OrderedSet()
        event1 = CounterEvent(2)
        event2 = CounterEvent(1)
        event3 = CounterEvent(0.5)
        event4 = CounterEvent(4.5)
        #Start Inserting
        #---------------------------------------------------------------------------------                      
        a.insert(event1)
        a.insert(event2)
        a.insert(event3)
        a.insert(event4)

        #Testing Remove
        #---------------------------------------------------------------------------------
        self.assertEqual('[<Event: 0.5>*, <Event: 1.0>, <Event: 2.0>, <Event: 4.5>]',str(a))
        
        a.remove(event3)
        self.assertEqual('[<Event: 1.0>*, <Event: 2.0>, <Event: 4.5>]',str(a))
        a.remove(event1)
        self.assertEqual('[<Event: 1.0>*, <Event: 4.5>]',str(a))
        a.remove(event2)
        a.remove(event4)
        self.assertEqual('[]',str(a))


    def testRemove_Exception(self):
        '''Test wether the right type of excpetion is raised when thing to be removed not inside the set'''

        #Case1 Starting from empty
        #---------------------------------------------------------------------------------
        try:
            a = OrderedSet()
            a.remove(3)
            self.assertTrue(False,'No excpetion/or no right type of exception raised')
        except IndexError:
            pass
        
    
                         



    def testRemovefirst(self):
        ''' Test for RemoveFirst method'''

        a = OrderedSet()
        event1 = CounterEvent(2)
        event2 = CounterEvent(1)
        event3 = CounterEvent(0.5)
        event4 = CounterEvent(4.5)
        #Insert the events in first
        #---------------------------------------------------------------------------------                      
        a.insert(event1)
        a.insert(event2)
        a.insert(event3)
        a.insert(event4)

        #Aplly RemoveFirst
        #Check both the thing returned
        #and also the object left in the set
        #---------------------------------------------------------------------------------
        self.assertEqual('[<Event: 0.5>*, <Event: 1.0>, <Event: 2.0>, <Event: 4.5>]',str(a))
        temp = a.removeFirst()
        self.assertEqual(True, temp is event3)
        
        self.assertEqual('[<Event: 1.0>*, <Event: 2.0>, <Event: 4.5>]',str(a))

        temp = a.removeFirst()
        self.assertEqual(True, temp is event2)
        
        self.assertEqual('[<Event: 2.0>*, <Event: 4.5>]',str(a))

        temp = a.removeFirst()
        self.assertEqual(True, temp is event1)
        self.assertEqual('[<Event: 4.5>*]',str(a))

        temp = a.removeFirst()
        self.assertEqual(True, temp is event4)
        self.assertEqual('[]', str(a) )

        temp = a.removeFirst()
        self.assertEqual(None,temp)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    def testLenghtMethod(self):
        a= OrderedSet()
        for i in range(10):
            c = random.random()*random.randrange(100)
            a.insert(c)
        self.assertEqual(10,len(a))
#---------------------------------------------------------------------------------
        a= OrderedSet()
        for i in range(20):
            c = random.random()*random.randrange(100)
            a.insert(c)
        self.assertEqual(20,len(a))

        
        


        
                
        

    

def main(argv):

    unittest.main()


if __name__ == '__main__':

    main(sys.argv)
