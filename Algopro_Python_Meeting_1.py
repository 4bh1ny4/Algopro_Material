# n = 10298398420347017928483596280412
# 
# if n % 2 == 0:
#     print(n , "is even brooo")
#     print(n , "EVEEEEEEENNNNNNNNN")
#     if n % 2 == 0:
#         print(n , "kelipatan eman")
# else:
#     print(n , "is odd brooo")
#     print(n , "ODDDDDDDDDDDDDDDD")
# print(n , "thank youu")


# name = input("What's your name broo? ")
# s = "What year you bron, " + name + " ? "
# y = int( input (s))
# r = "Hello " + name + ", you are now " + str(2023-y) + " years old."
# print(r)
# if y % 2 == 0:
#     print(y , name + ", you were in even-numbered year brooo")
# else:
#     print(y , name + ", you were in odd-numbered year brooo")


# skors = input("Type your score: ")
# skor = int(skors)
# 
# if skor >= 80:
#     nilai = "A"
# elif skor >= 75:
#     nilai ="AB"
# elif skor >= 70:
#     nilai ="B"
# elif skor >= 65:
#     nilai ="BC"
# elif skor >= 55:
#     nilai ="C"
# elif skor >= 45:
#     nilai ="D"
# else:
#     nilai ="E"
#     
# print("you got " + nilai + " for your score. ")


# a = input ("Type the frist number: ")
# b = input ("Type the second number: ")
# c = input ("Type the third number: ")
# 
# if a > b and a > c:
#     print("the biggest number is ", a)
# elif b > a and b > c: 
#     print("the biggest number is ", b)
# else:
#     print("the biggest number is ", c)
    

#  k = 1
#  while k < 11:
#      print(k)
#      k = k + 1
#  print("\nSelesai ! \nTerimakasih !")


# p = int(input("up to? "))
# k = 1
# while k<p+1:
#     if k % 2 == 0:
#         print(k , " is even")
#     else:
#         print(k , " is odd")
#     k = k + 1
# print("\nSelesai! \nTerimakasih!")



# p = int(input("up to? "))
# k = 1
# while k<p+1:
#     if k % 5 == 0:
#         print(k , " is a multiple of 5")
#     else:
#         print(k)
#     k = k + 1
# print("\nSelesai! \nTerimakasih!")


# n = 7
# b = range(n)
# for i in b:
#     print(i)

# name = input("What is your name? >")
# num = int(input("up to? "))
# for i in range(1, num + 1):
#     square = i * i
#     message = f"{i} times {i} is {square}"
#     if square % 5 == 0:
#         message += ". It is a multiple of 5."
#     print(message)
# print("Thank you " + name )
# print("Have a nice day!")

p = int(input("up to? "))
name = input("What is your name? ")
count = 1
while count < (p+1):
    k = count
    k = k * k
    if k % 5 == 0:
        print(k , " It is a multiple of 5.")
    print (count, " times ", count, " is ", k)
    count += 1
print("Thank you " + name )
print("Have a nice day!")
