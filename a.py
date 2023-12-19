 def a(filename):
     try:
        a = open(filename, "r")
    except FileNotFoundError:
        print("Sorry there is n such file ")