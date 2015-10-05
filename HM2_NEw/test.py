from Stack import *
import sys
var = input('NPR'+' '+':')
a = Stack()
for i in reversed(var):
    if i != ' ':
        a.push(i)

print (a) 
    
