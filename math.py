
while True:
    choice = input("Please pick a choice ['+','-','*','/']\n")
    if choice =='+':
        arg1 = input("First arg:\n")
        arg2 = input("second arg:\n")
        print ("{} + {} = {}".format(arg1,arg2,int(arg1) + int(arg2)))