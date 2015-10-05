import sys
import unittest

sys.path.insert(0, '..')
from DLList import *

class DLListTest(unittest.TestCase):
    """ test each method in class set"""


    #Test Empty Constructor
    def test_Empty_Constructor(self):

        r = DLList()
        self.assertEqual(str(r),'[]')



#Test for Construction and Exception of it
#-----------------------------------------------------------------------
    #Test Construct with a sequence
    def test_Constructor_seq(self):
        r = DLList([1,2,'cat'])
        self.assertEqual(str(r),str([1,2,'cat']))


    def test_Constructor_Exception(self):

        try:
            r = DLList(55)
        except TypeError:
            pass
        


#-----------------------------------------------------------------------   
    #Test the length method
    def testLength(self):
        r = DLList([1,2,'cat'])
        self.assertEqual(len(r),3)


#-----------------------------------------------------------------------
    #Test Append Method   
    def testAppend(self):
        r = DLList()
        r._append(1)
        r._append(2)
        r._append('cat')
        r._append(4)
        self.assertEqual(str(r),str([1,2,'cat',4]))



#Test for __getitem__method and Exception of it
#-----------------------------------------------------------------------
    # Test __getitem__ method    
    def testGetitem(self):
        r = DLList([1,2,'cat'])
        s = r.__getitem__(2)
        self.assertEqual(s,'cat')
        s = r.__getitem__(1)
        self.assertEqual(s,2)
    # Test the excpetion for __getitem__method
    def test_get_Exception(self):
        r = DLList([1,2,'cat'])
        try:
            r[3]
            self.assertTrue(False,'No Exception or right type of exception raised')
        except IndexError:
            pass


#Test for __setitem__method and Exception of it
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
    #Test __setitem__method
    #-----------------------------------------------------------------------
    def testSetitem(self):
        r=DLList([1,2,'cat'])
        r.__setitem__(2,0)
        self.assertEqual(str(r),str([1,2,0]))
        r.__setitem__(0,0)
        r.__setitem__(1,0)
        self.assertEqual(str(r),str([0,0,0]))

    # Test the excpetion for __Setitem__method
    #-----------------------------------------------------------------------
    def test_set_Exception(self):
        r = DLList([1,2,'cat'])
        try:
            r[3]
            self.assertTrue(False,'No Exception or right type of exception raised')
        except IndexError:
            pass


#Test for _find method and Exception of it
#-----------------------------------------------------------------------        
#-----------------------------------------------------------------------
    #Test __find method   
    #-----------------------------------------------------------------------
    def test_find(self):
        r = DLList([1,2,'cat'])
        a = r._find(2)
        #Check it's the listNode object
        #also check it's the right value 
        self.assertTrue(isinstance(a,DListNode))
        self.assertEqual(a.value,'cat')

    #Test the exception of _find method
    #-----------------------------------------------------------------------
    def test_find(self):
        r = DLList([1,2,'cat'])
        try:
            a = r._find(3)
            self.assertTrue(False,'no AssertionError rasied when needed for _find')
        except AssertionError:
            pass
       


#Test the insertion method and Exception of it
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


    #Test for Insertion
    #-----------------------------------------------------------------------
    def testInsert_start(self):
        r=DLList([1,2,'cat'])
        r.insert(0,0)
        
        self.assertEqual(str(r),str([0,1,2,'cat']))
        self.assertEqual(4,len(r))
    
        
    def testInsert_end(self):
        r=DLList([1,2,'cat',3])
        r.insert(4,10)
        
        self.assertEqual(str(r),str([1,2,'cat',3,10]))

    def testInsert_mid(self):
        r=DLList([1,2,'cat',3])
        r.insert(2,3)
        self.assertEqual(str(r),str([1,2,3,'cat',3]))

    #Test the Exception for Insertion Method
    #-----------------------------------------------------------------------
    def test_insert_Exception(self):
        r = DLList([1,2,'cat'])
        try:
            r.insert(4,'dog')
            self.assertTrue(False,'no Exception/or tight type of exception raised')
        except IndexError:
            pass
        
        

        
        
#Test the Delete Method and exception of it
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------    

    #The Delete Method
    #-----------------------------------------------------------------------
    def testDelitem_begin(self):
        r=DLList([1,2,'boy','cat',9])
        del r[0]
        self.assertEqual(str(r),str([2,'boy','cat',9]))
        
    def testDelitem_mid(self):
        r=DLList([1,2,'boy','cat',9])
        del r[2]
        self.assertEqual(str(r),str([1,2,'cat',9]))
        
    def testDelitem_end(self):
        r=DLList([1,2,'boy','cat',9])
        del r[4]
        self.assertEqual(str(r),str([1,2,'boy','cat']))


    #Test The exception of delete method    
    #-----------------------------------------------------------------------
    def test_del_exception(self):
        r = DLList([1,2,3,'cat'])
        try:
            del r[5]
            self.assertTrue(False,'no exception/ or right type of exception raised')
        except IndexError:
            pass


#Test for Pop Method and exception of it
#-----------------------------------------------------------------------            
#-----------------------------------------------------------------------


    #Test pop method
    #-----------------------------------------------------------------------
    def testpop_end(self):
        r=DLList([1,2,'boy','cat',9])
        a = r.pop()
        self.assertEqual(a,9)
        self.assertEqual(str(r),str([1,2,'boy','cat']))

    def testpop_mid(self):

        r=DLList([1,2,'boy','cat',9])
        a = r.pop(2)
        self.assertEqual(a,'boy')
        self.assertEqual(str(r),str([1,2,'cat',9]))

    def testpop_start(self):

        r=DLList([1,2,'boy','cat',9])
        a = r.pop(0)
        self.assertEqual(a,1)
        self.assertEqual(str(r),str([2,'boy','cat',9]))

    #Test the exception of pop method
    #-----------------------------------------------------------------------
    def testpop_exception(self):
        r=DLList([1,2,'boy','cat',9])
        try:
            a = r.pop(20)
            self.assertTrue(False,'No Exception or/ right type of exception raised')
        except IndexError:
            pass



#Test for the Index Method and the exception of it        
#-----------------------------------------------------------------------            
#-----------------------------------------------------------------------        


    #Test for Index method
    #-----------------------------------------------------------------------
    def testIndex_mid(self):
        r=DLList([1,2,'boy','cat',9])
        b=r.index('boy')
        self.assertEqual(b,2)

    def testIndex_start(self):
        r=DLList([1,2,'boy','cat',9])
        b=r.index(1)
        self.assertEqual(b,0)

    def testIndex_end(self):
        r=DLList([1,2,'boy','cat',9])
        b=r.index(9)
        self.assertEqual(b,4)

    #Test for the Exception of Index
    #-----------------------------------------------------------------------
    def testIndex_Exception(self):
        r=DLList([1,2,'boy','cat',9])
        try:
            b=r.index('seed')
            self.assertTrue(False,'No Exception/or Right Type of Error Raised')
        except ValueError:
            pass
        



#Test for Remove Method and the exception of it
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------           

    #Test Remove Method
    #-----------------------------------------------------------------------  
    def testRemove_end(self):
        r=DLList([1,2,'boy','cat',9])
        r.remove(9)
        self.assertEqual(str(r),str([1,2,'boy','cat']))

    def testRemove_start(self):
        r=DLList([1,2,'boy','cat',9])
        r.remove(1)
        self.assertEqual(str(r),str([2,'boy','cat',9]))

    def testRemove_mid(self):
        r=DLList([1,2,'boy','cat',9])
        r.remove('boy')
        self.assertEqual(str(r),str([1,2,'cat',9]))

    #Test Exception of remove method
    #-----------------------------------------------------------------------  
    def testRemove_Exception(self):
        r=DLList([1,2,'boy','cat',9])
        try:
            r.remove('seed')
            self.assertTrue(False,'No excpetion /or right type of Exception is raised')
        except ValueError:
            pass
        

        

#Visualize the iterating Method
#-----------------------------------------------------------------------
    def testIter_visual(self):
        r=DLList([0,1,2,3,4,5,6,7])
        for i in r:
            print (i)

#Test The Iterator (generator method)
#-----------------------------------------------------------------------
    def test_iter(self):
        r = DLList()
        r._append(0)
        r._append(1)
        r._append(2)
        r._append(3)
        r._append(4)
        r._append(5)        

        i = 0
        _iter = r.__iter__()
        while True:
            try:
                
                a = _iter.__next__()
                self.assertEqual(i,a)
                i = i +1
            except StopIteration:
                return
            except:
                self.assertTrue(False,'Iterating Is not working properly')

 

        
def main(argv):
    unittest.main()

if __name__ == '__main__':
    unittest.main()
