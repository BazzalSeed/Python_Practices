import math


def hehe(numsides):

    inangle=360.0/numsides
    halfangle=inangle/2

    halfside=(math.sin(math.radians(halfangle)))
    circume=2*numsides*halfside
    
    pi=circume/2
    return pi




