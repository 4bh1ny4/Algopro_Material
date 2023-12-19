#-----------------------------------------------------------#

def CountOccurrence(n):
    t = set(n)
    D = {} 
    for i in t:
        c = 0
        for j in n:
            if j in i:
                c += 1
        D[i] = c
    return D

#-----------------------------------------------------------#

def CountOccurrence1(n):
    t = set(n.lower())
    D = {} 
    for i in t:
        c = 0
        for j in n.lower():
            if j in i:
                c += 1
        D[i] = c
    return D
#-----------------------------------------------------------#