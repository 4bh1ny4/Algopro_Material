def f(x):
    y = x**2 + 1
    return y

def Myfun(a, b):
    return a**2 + 2*b -10

##########################################
def IsItEven(a):
    b = a % 2 == 0
    c = a == 0
    return b
##########################################

##########################################
def getMark(x):
    if x >= 80:
        nilai = "A"
    elif x >= 75:
        nilai ="AB"
    elif x >= 70:
        nilai ="B"
    elif x >= 65:
        nilai ="BC"
    elif x >= 55:
        nilai ="C"
    elif x >= 45:
        nilai ="D"
    else:
        nilai ="E"
        
    return nilai
###########################################

# # # # # # # # # # # # # # # # # # # # # #
def makeTriangle(x):
    for neko in range(x+1):
         print('*'*(neko))
# # # # # # # # # # # # # # # # # # # # # #
def makeTriangle2(x = 5):
    for neko in range(x+1):
        print('*'*(neko))
# # # # # # # # # # # # # # # # # # # # # # 
def makeTriangle3(x = 3, y = '*'): 
    for neko in range(1, x+1):
        print(neko, y+neko)
# # # # # # # # # # # # # # # # # # # # # #

# #---------------------------------------#
def HowManyEvenNumbers(X):
    c = 0
    for fren in X:
        if fren % 2 == 0:
            c = c + 1 
    return c
#-----------------------------------------#        
        
        
        
        
        
        
        
        
        
        
        
        