#SEED

myList = [7,9,'a','cat',False]
X = 'agcttttcattctgactgcaacgggcaatatgtctctgtgtggattaaaaaaagagtgtctgatagcagcttctgaactggttacctgccgtgagtaaattaaaattttattgacttaggtcactaaatactttaaccaatataggcatagcgcacagacagataaaaattacagagtacacaacatccatgaaacgcattagcaccaccattaccaccaccatcaccattaccacaggtaacggtgcgggctgacgcgtacaggaaacacagaaaaaagcccgcacctgacagtgcgggcttttttttcgaccaaaggtaacgaggtaacaaccatgcgagtgttgaagttcggcggtacatcagtggcaaatgcagaacgttttctgcgggttgccgatattctggaaagcaatgccaggcaggggcaggtggccaccgtcctctctgcccccgccaaaatcaccaaccatctggtagcgatgattgaaaaaaccatt'
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

import random      
def shuffle(List):
	length = len(List)
	NEW = []
	for i in range (length):
		r = random.randrange(length-i)
		NEW.append(List[r])
		List.pop(r)
	return NEW

#4.7 use insert


#4.8
import random
def shuffle(List):
    random.shuffle(List)
    return List


#4.8
def shuffle2(L):
    for i in range(len(L)**10)
        item = L.pop()
        L.insert(random.randrange(0,len(L)),item)
        
                
#4.9
#diagram

#4.10
#a list consisted of three empty lists

#4.11
#the second item in myList will become [2]
#4.12
dirgram
#4.13
M = []
def sep(L):
  
    N= []
    for i in L:
        M.append([i])
    return M


        

#4.14
def getMin(List):
    Min = alist[0]
    for i in range(1,len(List)):
        if Min > List[i]:
            Min = List[i]
    return Min

#4.15
def getMin(List):
    Min = List[0]
    for i in List:
        if i < Min:
            Min = i
    return Min

#4.16
def getmax(List):
    Max = List[0]
    for i in List:
        if i > Max:
            Max = i
    return Max

def getRange(List):
	Range = getMax(List)-getMin(List)
	return Range

# 4.17
A=[13,16,15,22]
def mean(l):
    mean = sum(l)/len(l)
    return mean
#4.18
def SUM(List):
    SUM = 0
    for i in List:
        SUM = SUM + i
    return SUM

#1
#same as 4.15

#2
def median(L):
    L.sort
    if len(L)%2 == 0:
        average = (L[len(L)/2]+L[(len(L)/2)-1])/2
        return average
    else:
        return L[len(L)/2]

#3
def validateLuhn(number):
    number.reverse()
    Sum = 0
    for i in range(0,len(number),2):
        a = number[i]%10
        if a != 0:
            Sum = Sum + a
        return Sum%10 == 0
        
        
        
        
    



#4
def getCodons(dna):
    dna = dna.upper()
    L = list(dna)
    M=[]
    for i in range(0,len(L),3):
        M.append(L[i:i+3])
    
    return M
        
        
#5
def countSerine(dna):
    M = getCodons(dna)
    print M
    count = 0
    for i in M:
        if i == ['T','C','T'] or i == ['T','C','C'] or i== ['T','C','A'] or i== ['T','C','G'] or i== ['A','G','T']or i==['A','G','C']:
            count = count+1
    return count

print countSerine(X)
