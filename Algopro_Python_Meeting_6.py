from time import ctime
from math import pi, sqrt

def currentHour():
    v = ctime()
    return v [11:19]
#####################

# # # # # # # # # # # 
def calculateCircleArea(r):
    a = pi*r**2
    return a
# # # # # # # # # # #

#####################
def camputeHypotenuse(a,b):
    c = sqrt(a**2 + b**2)
    return c
#####################

# # # # # # # # # # #
def onlyEvens(L):
    D=[]
    for fren in L:
        if fren % 2 ==0:
            D.append(fren)
    return D
# # # # # # # # # # #

#####################
def LessThan(L,a):
    A=[]
    for freren in L:
        if freren < a:
            A.append(freren)
    return A




