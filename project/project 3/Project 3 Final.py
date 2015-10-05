# -*- coding: cp936 -*-
#Seed Zeng ＆ Shunxin Xiao
#Project 3
import turtle
import random
import math
import matplotlib.pyplot as mpl

'''pashe 1 randomwalkers(turtle graph simiulation)'''
def RandomWalk(moves):
    x = 0
    y = 0
    t = turtle.Turtle()
    #set the screen
    screen = turtle.Screen()
    t.tracer(10)
    screen.setworldcoordinates(-100,-100,100,100)
    for i in range (moves):
        # random walking process
        # for each step, there are 4 possibilities:x-1, x+1, y+1, y-1
        # use 4 numbers to represent each possibility and move the turtle according to the accumulated x,y value after four runs

        ran = random.randrange(4)
        if ran == 0:
            x = x+1
        elif ran == 1:
            x = x-1
        elif ran == 2:
            y = y+1
        else:
            y = y-1
        t.goto(x,y)
    distance = math.sqrt(x**2 + y**2)
    return distance


###################################################################################
#################################################################################
'''pahse TWo--------Plot the Average Distance Simulation Graph and Model Function'''

#First Step
#New randomWalk Function -------------adding Boolean parameter
def randomWalk(moves,draw):
    # random walking process
    # for each step, there are 4 possibilities:x-1, x+1, y+1, y-1
    # use 4 numbers to represent each possibility and move the turtle according to the accumulated x,y value after four runs


    x = 0          # x coordinate 
    y = 0          # y coordinate
    if draw:  # case for drawing graph
        #call turtle
        t = turtle.Turtle()
        # move it faster!!
        t.tracer(10)
        #set the screen
        screen = turtle.Screen()
        screen.setworldcoordinates(-100,-100,100,100)    
        for i in range (moves):
            # random walking process
            # for each step, there are 4 possibilities, x -or+1 or y -or+1
            ran = random.randrange(4)
            if ran == 0:
                x = x+1
            elif ran == 1:
                x = x-1
            elif ran == 2:
                y = y+1
            else:
                y = y-1
            t.goto(x,y)
    else:      # case for not drawing graph
        for i in range (moves):
    # random walking process
    # for each step, there are 4 possibilities:x-1, x+1, y+1, y-1
    # use 4 numbers to represent each possibility and move the turtle according to the accumulated x,y value after four runs
            ran = random.randrange(4)
            if ran == 0:
                x = x+1
            elif ran == 1:
                x = x-1
            elif ran == 2:
                y = y+1
            else:
                y = y-1
    distance = math.sqrt(x**2 + y**2)     # calculating the final distance
    return distance
###########################################################################
#Second Step
#Plot the Graph the Average Distance Simulation Graph
def  plotdistance(maxMoves,trials):
    totalDistance = 0
    numsteps = [ ]
    avgdistance = [ ]
 
    for i in range (100,maxMoves+1,100):
        totalDistance = 0
        numsteps.append(i)
        for j in range(trials):
            totalDistance = randomWalk(i,False)+totalDistance
        avg = totalDistance/trials
        avgdistance.append(avg)
    mpl.plot(numsteps,avgdistance,label = "Simulation")#name this line as simulation
    mpl.legend()
    mpl.xlabel("Number of Steps")    #name the x-axis
    mpl.ylabel("Average Distance From Origin")#name the y-axis
    mpl.show()
#After running this function as plotdistance(10000,500),We have a graph looks teriibly like y = sqrt(x)
#So we try to plot the y = sqrt(x) graph with the Average Distance Simulation to See whether they are similiar
################################################################################################################


#Now Plot The Graph Of Average Distance and the possible Model Function(y=sqrt(x)) together

def  plotRWDistance(maxMoves,trials):
    totalDistance = 0
    numsteps = [ ]
    avgdistance = [ ]
    xvalue = [ ]
    yvalue = [ ]
    
    for i in range (100,maxMoves+1,100):
        totalDistance = 0
        numsteps.append(i)
        x = i
        y = math.sqrt(x)
        xvalue.append(x)
        yvalue.append(y)
        for j in range(trials):
            totalDistance = randomWalk(i,False)+totalDistance
        avg = totalDistance/trials
        avgdistance.append(avg)
    
    mpl.plot(xvalue,yvalue,label = "Model Function")#name the line as Model Function
    mpl.plot(numsteps,avgdistance,label = "Simulation")#name the line as Simulation
    mpl.legend()
    mpl.xlabel("Number of Steps")    #name the x-axis
    mpl.ylabel("Average Distance From Origin")#name the y-axis
    mpl.show()

def main():
    randomwalk(1000,True)
    plotRwDistance(10000,500)
    

main()
#Conclusion
#It turns out that the y = sqrt(x) and Average Distance Simulation graph are really close
#So We believe that the Model Function for the randomwalk average distance should be y=sqrt(x)



        
        

