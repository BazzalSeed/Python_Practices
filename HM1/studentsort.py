#This file contains two sorting methods: the selection sort and insertion sort

#The selection sort method
#precondtion: L is a list of integers
#Postcondition: L is sorted in an ascending order
def selection_sort(L):
 
    # The main function
    for i in range( len(L) ):
        
        # Start with the current position
        minindex = i
         
        # Scan to the end of list to find the smalles element(except the current)
        for j in range(i+1, len(L) ):
         
            
            if L[j] < L[minindex]:
             
                # Get the index of the minimum
                minindex = j
         
        # Swap the two values
        temp = L[minindex]
        L[minindex] = L[i]
        L[i] = temp
    return L
    
###################################################################################



#The insertion_sort method
#precondtion: L is a list of integers
#Postcondition: L is sorted in an ascending order
def insertion_sort(L):
 
    # The main function
    for i in range(1, len(L)):
        # Start at the second element
        # Get the value of the element to insert
        value = L[i]
        
        # Scan to the start of the list( right t oleft)
        scan = i-1
        # Loop each element, moving them up one postion
        # stop at where we find the element that is bigger than the current value
        while ( scan >= 0) and (L[scan] > value):
            L[scan + 1] = L[scan]
            scan = scan - 1
             
        #  Since element we looped through moved up one postion already
        # the space is clear for the insertion
        # do the insertion
        L[scan +  1] = value
    return L
