
myList = [7,9,'a','cat',False]

#4.2
#a
myList.append(3.14)
myList.append(7)
#b
myList.insert(3,'dog')
#c
print myList.index('cat')

#d
print myList.count(7)

#e
myList.remove(7)

#f

a = myList.index('dog')
myList.pop(a)

#4.3
a = 'the quick brown fox'
print a.split()
#4.4
b = 'mississippi'
print b.split('i')
#4.5
def wordcounter(s):
    x = s.split()
    return len(x)
#4.6

#a----count
def count(myList,count):
    Sum = 0
    for i in myList:
        if i == count:
            Sum = Sum +1
    return Sum
#b----in

def inlist(myList,thingin):
    for i in myList:
        if thingin == i:
            return True
    return False

#c------reverse
def reverse(myList):
    ListNew = []
    for i in range (len(myList)):
        ListNew.insert(0,myList[i])
    return ListNew




#d

def index(myList,thing):
    index = 0
    for i in myList:
        index = index+1
        if i == thing:
            return index
    return -1

#e
def insert(myList,position,thing):
    listnew = []
    for i in range(0,position):
        listnew.append(myList[i])
    listnew.append(thing)
    for b in range(position,len(myList)):
        listnew.append(myList[b])
    return listnew

#4.7

import random      # The input list changed. Immutable and Mutable
def shuffle(List):
	length = len(List)
	NEW = []
	for i in range (length):
		r = random.randrange(length-i)
		NEW.append(List[r])
		List.pop(r)
	return NEW


#4.8
import random
def shuffle(List):
    random.shuffle(List)
    return List
        
                
#4.9

#4.10


#4.13

def fragment(List):
    new = []
    for i in range(0, len(List)):
        yield List[i]
    return 

print fragment(myList)
        


        
