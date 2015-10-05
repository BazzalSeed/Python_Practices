#dsdfsdf ds

import math
import turtle
turt=turtle.Turtle()
def circle(turt,radius):
    '''draw a circle'''
    side= (2.0*math.pi*radius)/360
    for x in range(360):
        turt.forward(side)
        turt.right(1)

def main():
    circle(turt,150)

    turtle.mainloop()
    
main()
    
    
        