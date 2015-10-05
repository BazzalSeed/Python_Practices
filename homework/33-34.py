import turtle
turt= turtle.Turtle()
def drawspiral(turt,angle,maxsides):
    for sidelength in range(1,maxsides+1,5):
        turt.forward(sidelength)
        turt.right(angle)

#problem 1.33        
drawspiral(turt,120,100)

#problem 1.34
drawspiral(turt,80,100)

turtle.mainloop()