#_________________________________________________________________#

def MakeMydict(A,B):
    D={}
    for i in range(len(A)):
        D[A[i]] = B[i]
        for i in D.keys():
            print()
    return D

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def xtractExt(b):
    a = b[::-1]
    c = a.find(".")
    return b[-c:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def addTowDicts(A,B):
    d = A.copy()
    key_B = B.keys()
    for key in key_B:
        d[key] = B[key]
    return d

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def printEnchLine(filename):
    f = open(filename, "r")
    l = f.readlines()
    for i in l:
        k = i.find("#")
        print(i[:k])
    f.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    