class Stack:
     def __init__(self):
         self.items = []
         

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def __str__(self):
         return str('length is'+' '+str(len(self.items)))
