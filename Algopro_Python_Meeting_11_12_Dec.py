#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from time import ctime
from Algopro_Python_Meeting_7_14_Nov import mounth
from Algopro_Python_Meeting_7_14_Nov import day

def writeText(fname,text):
    f = open(fname, "w+")
    t = f.write(text+ "\n\n")
    s = ctime()
    
    day_en = s[0:3]
    month = s[4:7]
    year = s[20:]
    time = s[11:16]
    tanggal = s[8:10]
    
    hari = day[day_en]
    bulan = mounth[month]
    
    f.write("--" + " " + hari + ", " + tanggal + " " + bulan + " " + year + " " + time)
    f.close()

#-------------------------------------------------------------------------------------#

def myStatus(Status):
    fname = "Neko"
    f = open(fname, "a+")
    s = ctime()
    
    day_en = s[0:3]
    month = s[4:7]
    year = s[20:]
    time = s[11:16]
    tanggal = s[8:10]
    
    hari=day[day_en]
    bulan = mounth[month]

    f.write("\n\n"+ Status+"\n--" + " " + hari + ", " + tanggal + " " + bulan + " " + year + " " + time)
    f.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Argument in function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def myFun2( *args ):
    for i in args:
        print(i)
        
#-------------------------------------------------------------------------------------#

def addThis(*a):
    count = 0
    for i in a:
        if type(i) == str:
            continue
        else:
            count += i
    return count

#-------------------------------------------------------------------------------------#

