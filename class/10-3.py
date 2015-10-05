#LiSTTTTTTTT

L = [3,4,5,'Hi']
Lista = [3,4,5,0]


def sum(L):
    sum = 0 
    for i in L:
        sum = sum + i
    return sum

print sum(Lista)

def min(L):
    min = L[0]
    for i in L:
        if i < min:
          min = i
    return min

print min(Lista)

def median(L):
    L.sort()
    b = len(a)
    if b%2 = 0:
       return (L[b/2]+L[(b/2)-1])/2.0
    else:
       return L(b/2)
    
    