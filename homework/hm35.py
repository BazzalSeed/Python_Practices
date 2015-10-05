import turtle
turt= turtle.Turtle()
def drawspiral(turt,sidelength,maxsides):
    for angle in range(10,maxsides+1,5):
        turt.forward(sidelength)
        turt.right(angle)
     
#hm1.35     
drawspiral(turt,50,200)
turtle.mainloop()
