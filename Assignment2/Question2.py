# Q2 Write a Python function to find the maximum of three numbers.

def find_Sum():
    value1 = int(input("Enter 1st number "))
    value2 = int(input("Enter 2nd number "))
    value3 = int(input("Enter 3rd number "))

    if value1 > value2 and value3:
        print(f"{value1} is greater than {value2} and {value3}")
    elif value2 > value3 and value1:
        print(f"{value2} is greater than {value3} and {value1}")
    else:
        print(f"{value3} is greater than {value1} and {value2}")

find_Sum()
