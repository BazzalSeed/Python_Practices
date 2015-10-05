#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
#! GROUP MEMBERS: Seed Zeng £¦ Shunxin Xiao
#! The answers to all the questions and graphs are documented in the WORD attached

import matplotlib.pyplot as mpl#import the pyplot in matplotlib module


#Part ~1

''' define the pred-prey function'''
def PP1(preyPop,predPop,dt,months):
#preypop for the initial predator population
#predpop for the initial prey population
#dt      for the time interval
#months  for  total months

    poplistpred = [ ]#creat a list for predator population
    timelist = [ ]   #creat a list for time(x axis)
    poplistprey = [ ]#creat a list for prey population
    pppred=predPop   #assign initial population of predator
    ppprey=preyPop   #assign initial population of prey
    poplistpred.append (predPop)#append initial predator population to the list
    poplistprey.append (preyPop)#append the initial prey population to the list
    timelist.append(0)          #append the initial value of time to the list
    bm = 0.5   # birth rate of prey
    dm = 0.02  # death rate of prey
    bw = 0.005 # birth rate of predator
    dw = 0.75  # death rate of predator
    runs=int(months/dt)
    t = 0.00
    '''use for loop to simulate the change of populationof prey, predator'''
    for i in range (1,runs):            
        #pppred for the population of predator
        #ppprey for the population of prey
        #temp assures that ppprey gain the right value of pppred(the value from previous step£©
        temp = pppred  
        pppred = pppred+(bw*pppred*ppprey-dw*pppred)*dt
        ppprey = ppprey+(bm*ppprey-dm*temp*ppprey)*dt
        t = i*dt
        #if statment assures that when the population of wolves drops under 1 wolves will be defined as die out 
        if pppred < 1:
            pppred = 0
        if ppprey < 1:
            ppprey = 0
        timelist.append(t)#append t value to the t list
        poplistprey.append (ppprey)#append the value of prey population in each run to the list
        poplistpred.append (pppred)#append the value of predator population in each run to the list
    mpl.plot(timelist,poplistpred,label = "predator")#name this line as predator
    mpl.plot(timelist,poplistprey, label = "prey")   #name this line as prey
    mpl.legend()
    mpl.xlabel("months")    #name the x-axis
    mpl.ylabel("Population")#name the y-axis
    mpl.show()# FINALLY SHOW THE GRAPH!!!
    


###################################################################
####################################################################

# P A R T ~2: raise the detah rate of wolf'''
def PP2(preyPop,predPop,dt,months):
#preypop for the initial predator population
#predpop for the initial prey population
#dt      for the time interval
#months  for  total months

    poplistpred = [ ]#creat a list for predator population
    timelist = [ ]   #creat a list for time(x axis)
    poplistprey = [ ]#creat a list for prey population
    pppred=predPop   #assign initial population of predator
    ppprey=preyPop   #assign initial population of prey
    poplistpred.append (predPop)#append initial predator population to the list
    poplistprey.append (preyPop)#append the initial prey population to the list
    timelist.append(0)          #append the initial value of time to the list

    bm = 0.5   # birth rate of prey
    dm = 0.02  # death rate of prey
    bw = 0.005 # birth rate of predator
    dw = 4.022  # death rate of predator;raise from 0.75 to 4.022
    runs=int(months/dt)
    t = 0.00
    #if statment assures that when the population of wolves drops under 1 wolves will be defined as die out 
    for i in range (1,runs):            
        #pppred for the population of predator
        #ppprey for the population of prey
        #temp assures that ppprey gain the right value of pppred(the value from previous step£©
        temp = pppred
        pppred = pppred+(bw*pppred*ppprey-dw*pppred)*dt
        ppprey = ppprey+(bm*ppprey-dm*temp*ppprey)*dt
        #if statment assures that when the population of wolves drops under 1 wolves will be defined as die out 
        if pppred < 1:
            pppred = 0
        if ppprey < 1:
            ppprey = 0
        t = i*dt

        timelist.append(t)#append t value to the t list
        poplistprey.append (ppprey)#append the value of prey population in each run to the list
        poplistpred.append (pppred)#append the value of predator population in each run to the list

    mpl.plot(timelist,poplistpred,label = "predator")#name this line as predator
    mpl.plot(timelist,poplistprey, label = "prey")   #name this line as prey
    mpl.legend()
    mpl.xlabel("months")    #name the x-axis
    mpl.ylabel("Population")#name the y-axis
    mpl.show()# FINALLY SHOW THE GRAPH!!!
    


#############################################################################
#############################################################################

#P a r t~3£ºconstrained model
''' define the pred-prey function'''
def PP3(preyPop,predPop,dt,months):
#preypop for the initial predator population
#predpop for the initial prey population
#dt      for the time interval
#months  for  total months

    poplistpred = [ ]#creat a list for predator population
    timelist = [ ]   #creat a list for time(x axis)
    poplistprey = [ ]#creat a list for prey population
    pppred=predPop   #assign initial population of predator
    ppprey=preyPop   #assign initial population of prey
    poplistpred.append (predPop)#append initial predator population to the list
    poplistprey.append (preyPop)#append the initial prey population to the list
    timelist.append(0)          #append the initial value of time to the list

    bm = 0.5   # birth rate of prey
    dm = 0.02  # death rate of prey
    bw = 0.005 # birth rate of predator
    dw = 0.75  # death rate of predator
    runs=int(months/dt)
    t = 0.00
    #MMC is the carrying capacity of the prey population
    MMC = 750# assgien valule 750 to carrying capacity
    for i in range (1,runs):
        #pppred for the population of predator
        #ppprey for the population of prey
        #temp assures that ppprey gain the right value of pppred(the value from previous step£©

        temp = pppred
        pppred = pppred+(bw*pppred*ppprey-dw*pppred)*dt
        ppprey = ppprey+(bm*ppprey*(1-(ppprey/MMC))-dm*temp*ppprey)*dt#notice that carrying capacity has been introduced
        #if statment assures that when the population of wolves drops under 1 wolves will be defined as die out 
        if pppred < 1:
            pppred = 0
        if ppprey < 1:
            ppprey = 0
        t = i*dt

        timelist.append (t)
        poplistprey.append (ppprey)
        poplistpred.append (pppred)
        timelist.append(t)#append t value to the t list
        poplistprey.append (ppprey)#append the value of prey population in each run to the list
        poplistpred.append (pppred)#append the value of predator population in each run to the list

    mpl.plot(timelist,poplistpred,label = "predator")#name this line as predator
    mpl.plot(timelist,poplistprey, label = "prey")   #name this line as prey
    mpl.legend()
    mpl.xlabel("months")    #name the x-axis
    mpl.ylabel("Population")#name the y-axis
    mpl.show()# FINALLY SHOW THE GRAPH!!!
#############################################################################
############################################################################


#introducing the hunters(raising death rate of predator) to the model

'''define the new function'''

def PP4(preyPop,predPop,dt,months):

#preypop for the initial predator population
#predpop for the initial prey population
#dt      for the time interval
#months  for  total months

    poplistpred = [ ]#creat a list for predator population
    timelist = [ ]   #creat a list for time(x axis)
    poplistprey = [ ]#creat a list for prey population
    pppred=predPop   #assign initial population of predator
    ppprey=preyPop   #assign initial population of prey
    poplistpred.append (predPop)#append initial predator population to the list
    poplistprey.append (preyPop)#append the initial prey population to the list
    timelist.append(0)          #append the initial value of time to the list


    bm = 0.5   # birth rate of prey
    dm = 0.02  # death rate of prey
    bw = 0.005 # birth rate of predator
    dw = 3.209 # death rate of predator
    runs=int(months/dt)
    t = 0.00
    #MMC is the carrying capacity of the prey population
    MMC = 750# assgien valule 750 to carrying capacity
    for i in range (1,runs):
        #pppred for the population of predator
        #ppprey for the population of prey
        #temp assures that ppprey gain the right value of pppred(the value from previous step£©

        temp = pppred
        pppred = pppred+(bw*pppred*ppprey-dw*pppred)*dt
        ppprey = ppprey+(bm*ppprey*(1-(ppprey/MMC))-dm*temp*ppprey)*dt#notice that carrying capacity has been introduced
        #if statment assures that when the population of wolves drops under 1 wolves will be defined as die out 
        if pppred < 1:
            pppred = 0
        if ppprey < 1:
            ppprey = 0
        t = i*dt

        timelist.append (t)
        poplistprey.append (ppprey)
        poplistpred.append (pppred)
        timelist.append(t)#append t value to the t list
        poplistprey.append (ppprey)#append the value of prey population in each run to the list
        poplistpred.append (pppred)#append the value of predator population in each run to the list

    mpl.plot(timelist,poplistpred,label = "predator")#name this line as predator
    mpl.plot(timelist,poplistprey, label = "prey")   #name this line as prey
    mpl.legend()
    mpl.xlabel("months")    #name the x-axis
    mpl.ylabel("Population")#name the y-axis
    mpl.show()# FINALLY SHOW THE GRAPH!!!
    

''' define main function'''


def main():
    PP1(500,25,0.01,60)
    PP2(500,25,0.01,60)
    PP3(500,25,0.01,120)
    PP4(500,25,0.01,60)
main()#call the main function

#Done................Thx for grading
    
