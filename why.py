#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
import random
import matplotlib.pyplot as mpl
import math
##def randomWalk2(moves,drawOrNot):
##    # Function for simulating motion and calculating the final distance
##    # The Boolean parameter available
##    x = 0          # x coordinate 
##    y = 0          # y coordinate
##    if drawOrNot:  # case for drawing graph
##        screen = turtle.Screen()
##        t = turtle.Turtle()
##        t.tracer(10)
##        screen.setworldcoordinates(-100,-100,100,100)    # set screen
##        for i in range (moves):
##            # random walking process
##            # for each step, there are 4 possibilities, x -or+1 or y -or+1
##            ran = random.randrange(4)
##            if ran == 0:
##                x = x+1
##            elif ran == 1:
##                x = x-1
##            elif ran == 2:
##                y = y+1
##            else:
##                y = y-1
##            t.goto(x,y)
##    else:      # case for not drawing graph
##        for i in range (moves):
##            ran = random.randrange(4)
##            if ran == 0:
##                x = x+1
##            elif ran == 1:
##                x = x-1
##            elif ran == 2:
##                y = y+1
##            else:
##                y = y-1
##    distance = math.sqrt(x**2 + y**2)     # calculating the final distance
##    return distance

def ok(moves):
    # This is just for simplicity.
    # Boolean parameter not available.
    # This program requires less time to run, which grants efficiency for later function
    # Result of this program is the same as randomWalk(moves,False)
    x = 0.0
    y = 0.0
    for i in range (moves):
        ran = random.randrange(4)
        if ran == 0:
            x = x+1
        elif ran == 1:
            x = x-1
        elif ran == 2:
            y = y+1
        else:
            y = y-1
    distance = math.sqrt(x**2 + y**2)
    return distance

def plot(maxMoves,trials):
    # Program to calculate the average and plot graph
    numsteps = [ ]
    avgdistance = [ ]
    
    for i in range (100,maxMoves+1,100):
        totalDistance = 0.0
        numsteps.append(i)
        for j in range(trials):
            totalDistance = ok(i)+totalDistance
        avg = totalDistance/trials
        avgdistance.append(avg)
    mpl.plot(numsteps,avgdistance)
    mpl.show()
    

plot(10000,500)
        
