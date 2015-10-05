#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
#raido decay simulation
#decay rate = -0.000120968
#Q(t) = Q(t-1)+(-0.000120968)Q(t-1)

def decay(initialnum,time,dt):
    rate = -0.000120968
    amount = initialnum
    amountlist = [ ]
    t= 0.0
    
    for i in range(int(time/dt)+1):
        amount = amount + (rate*amount)*dt
        t = t+dt
        timelist.append(t)
        print i,amount


decay(100,5000,0.01)