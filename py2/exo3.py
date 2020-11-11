import math

def rad(nb) :
    x = 180*nb
    res = x/math.pi
    return res

def deg(nb) :
    x = math.pi*nb
    res = x/180
    return(res)
    
print(rad(4.7))
print(deg(269))