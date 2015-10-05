import turtle
turt= turtle.Turtle()

turt1= turtle.Turtle()

def drawspiral(turt,angle,maxsides):
    for sidelength in range(50,maxsides+1,5):
        turt.forward(sidelength)
        turt.right(angle)
        turt1.forward(sidelength)
        turt1.left(angle)

drawspiral(turt,90,100)

turtle.mainloop()