from studentsort import *
import time
import random


## Initializing variables and Testing lists

l1 = []
l2 = []
l3 = []
a = 1000
b = 1000
c = 2000 
#############################################################################################################################################




## The function "create" creates three Test lists that are gonna be used to test respectively, Insertion_sort, Selection_sort, and built-in sort
#precondtion:NONE
#postconditon: Generates lists l1,l2,l3 which contain wanted test lists inside. (also global variable a,b,c got changed)

def create():
    #define global variable
    global a
    global b
    global c

    #generate list 1 for testing insertion sort
    while  a <= 256000:
        l1.append(random.sample(range(1000000),a))
        a = a*2
    #generate list 2 for testing insertion sort
    while b <= 64000:
        l2.append ( random.sample(range(1000000),b))
        b = b*2
    #generate list 3 for testing insertion sort
    while c <= 1000000:
        l3.append ( random.sample(range(1000000),c))
        c = c*2


#Drive is the main test function to test all three sorting functions
#Precondition:None
#Postcondtion:print out the runing time of each sorting method for all itmes in l1,l2 and l3. The format will be steps,time

def drive():

    #Start testing insertion sort
    print ('insertion sort')
    #Loop through the testing lists whithin in l1
    for i in l1:
        start = time.time()
        insertion_sort(i)
        stop = time.time()
        print (len(i),stop-start)

    #Start testing selection sort
    print ('selection sort')
    #Loop through the testing lists within l2
    for j in l2:
        start = time.time()
        selection_sort(j)
        stop = time.time()
        print (len(j), stop- start)

    #Start testing The built-in sort
    print (' the glorious python sort')
    #Loop thourgh the testing lists whithin l3
    for k in l3:
        start = time.time()
        sorted(k)
        stop = time.time()
        print (len(k),stop-start)

#Main is the function to call for both "create" and "drive". it activates the whole process
#preconditon:None
#postcondition:Crate 5 sets of testing lists and run the test(and print out the results) 5 times
def main():
    for i in range(5):
        create()
        drive()
#Call the function to activate the whole process
main()

