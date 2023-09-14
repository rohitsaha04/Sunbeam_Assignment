# Q3 write a program to find given number is positive ,negetive or zero.


def find_zero():
    user = int((input("Enter any number ")))
    if(user > 0):
        print("It is positive")
    elif(user < 0):
        print("It is negative")
    else:
        print("It is zero")

find_zero()
