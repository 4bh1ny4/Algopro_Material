from time import ctime

#-----------------------------------------------------------#

angka = {"1" : "satu",
         "2" : "dua",
         "3" : "tiga",
         "4" : "empat",
         "5" : "lima",
         "6" : "eman",
         "7" : "tujuh",
         "8" : "delapan",
         "9" : "sembilan",
         "0" : "nol"}
day = {"Sun" : "Ahad",
       "Mon" : "Senin",
       "Tue" : "Selasa",
       "Wen" : "Rabu",
       "Thu" : "Kamis",
       "Fri" : "Jumat",
       "Sat" : "Sabtu"}
mounth = {"Jan" : "Januari",
          "Feb" : "Februari",
          "Mar" : "Maret",
          "Apr" : "April",
          "May" : "Mei",
          "Jun" : "Juni",
          "Jul" : "Juli",
          "Aug" : "Agustus",
          "Sep" : "September",
          "Oct" : "Oktober",
          "Nov" : "November",
          "Dec" : "Desember"}

#-----------------------------------------------------------#

def timeInfo():
    c = ctime()
    hari = c[0:3]
    bulan = c[4:7]
    tahun = c[20:]
    jam = c[11:16]
    tgl = c[8:10]
    m = mounth[bulan]
    h = day[hari]
    i = "Hari " + h + " tanggal " + tgl + " " + m + " " + tahun + ", pukul " + jam 
    return i

#-----------------------------------------------------------#

def countLetters(n):
    a = 0
    huruf = "abcdefghijklmnopqrstuvwxyz"
    for i in n:
        if i in huruf:
            a = int(i)+1
        return a
        a
    return a

#-----------------------------------------------------------#
