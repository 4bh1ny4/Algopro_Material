#-------------------------------------------------------------------------------------#

def addThis(*a):
    count = 0
    for i in a:
        if type(i) == int or type(i) == float:
            count += i
    return count

#-------------------------------------------------------------------------------------#

def Division(a,b):
    try:
        y = a/b
        return y
    except ZeroDivisionError:
        print("Sorry, you can't divide these ")
    except TypeError:
        print("Both input have to be numbers")
        
#-------------------------------------------------------------------------------------#

def printEnchLine(filename):
    f = open(filename, "r")
    l = f.readlines()
    for i in l:
        k = i.find("#")
        print(i[:k])
    f.close()

#-------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------#



#-------------------------------------------------------------------------------------#

class Manusia( object ):
    
    def __init__(self, s):
        self.name = s
        self.bodystate = "hungry"
        self.saving = 0
        
    def Saysalam(self):
        print("Assalamualaikum, my name is ",self.name)
        
    def exercise(self, sport):
        print(sport, "is fun.")
        self.bodystate = "hungry"

    def eat(self, foot):
        print("I just ate ", foot+".")
        self.bodystate = "full"
        
    def timesTwo(self, n):
        return n*2

#-------------------------------------------------------------------------------------#

def Student( Manusia ):
    
    courses = []
    
    def learnInClass( self, course ):
        print("I learned ", course)
        self.courses = self.courses.append(course)
        
    def enrolToUni(self, uni):
        print("I just enrolled to ", uni)
        self.campus = uni
        
        def eat(self, foot):
            print("Just ate", foot, "IT WAS AWESIOME")
            
#-------------------------------------------------------------------------------------#

def InformaticsStudent( Student ):
    
    skills = []
    def practice(self, language):
        print()
        self.skills.append(language)
        