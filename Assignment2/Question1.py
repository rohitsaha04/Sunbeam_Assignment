# Q.1. Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube funct
# ion]



def find_Cube():
    value1 = int(input("Enter 1st number "))
    value2 = int(input("Enter 2nd number "))
    value3 = int(input("Enter 3rd number "))
    value4 = int(input("Enter 4rth number "))
    value5 = int(input("Enter 5th number "))

    result = value1 + value2 + value3 + value4 + value5 ** 3
    print(result)

find_Cube()