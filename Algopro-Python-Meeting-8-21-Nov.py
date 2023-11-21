#Algopro Meeting

#-----------------------------------------------------------#
def countLetters(n):
    a = 0
    for i in n:
        if i.isalpha():
            a += 1
    return a

#-----------------------------------------------------------#

def countNumbers(n):
    Num = 0
    for i in n:
        if i.isdigit():
            Num += 1
    return Num

#-----------------------------------------------------------#

def countVowels(n):
    Num = 0
    Vowels = "aiueo"
    for i in n:
        i.lower()
        if i in Vowels:
            Num += 1
    return Num

#-----------------------------------------------------------#

def countVowelsAndConsonants(n):
    Num_Vowels = 0
    Num_Consonants = 0
    Vowels = "aiueoAIUEO"
    Consonants = "QqWwRrTtYyPpSsDdFfGgHhJKkLlZzXxCcVvBbNnMm"
    for i in n:
        if i in Vowels:
            Num_Vowels += 1
        if i in Consonants:
            Num_Consonants +=1
    return Num_Vowels, Num_Consonants

#-----------------------------------------------------------#

def countThings(n):
    Num_Vowels = 0
    Num_Consonants = 0
    Num_Digits = 0
    Num_Nomer = ""
    Vowels = "aiueo"
    Consonants = "QqWwRrTtYyPpSsDdFfGgHhJKkLlZzXxCcVvBbNnMm"
    Nomer = "0123456789"
    for i in n.lower():
        if i in Vowels:
            Num_Vowels += 1
        if i in Consonants:
            Num_Consonants +=1
        if i.isdigit():
            Num_Digits += 1
        if i in Nomer:
            Num_Nomer = Num_Nomer + str(i)
    return Num_Vowels, Num_Consonants, Num_Digits, Num_Nomer

#-----------------------------------------------------------#

def countReport(n):
    A = countThings(n)
    B = SpellTheNumbers(A[3])
    if A[2]==1:
        print("Your string has " + str(A[0]) + " vowels, " + str(A[1]) + " consonants, and " + str(A[2]) + " digit. \nThe digit are " + str(A[3]) + "\nThat is : " + str(B))
    elif A[2]==0:
        print("Your string has " + str(A[0]) + " vowels, " + str(A[1]) + " consonants, and " + str(A[2]) + " digits.")
    else:
        print("Your string has " + str(A[0]) + " vowels, " + str(A[1]) + " consonants, and " + str(A[2]) + " digits. \nThe digits are " + str(A[3]) + "\nThat is : " + str(B))
#-----------------------------------------------------------#

angka = {"0" : "zero",
         "1" : "one",
         "2" : "two",
         "3" : "three",
         "4" : "four",
         "5" : "five",
         "6" : "six",
         "7" : "seven",
         "8" : "eight",
         "9" : "nine"}

def SpellTheNumbers(a):
    s = ""
    for i in a:
        s = s + " " + angka[i]
        c = s[1:]
    return c

#-----------------------------------------------------------#



#-----------------------------------------------------------#



#-----------------------------------------------------------#