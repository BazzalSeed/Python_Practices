import turtle
t=turtle.Turtle()
def graph(t,interval):
    t.up()
    t.goto(-interval*10,interval**2)
    t.down()
    for i in range(-interval,interval+1):
        x=i*10
        y=i*i
        t.goto(x,y)
    
        
        
def main(interval):
    graph(t,interval)
    
    turtle.mainloop()

main(20)






        
        