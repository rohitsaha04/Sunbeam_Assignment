# Q1) Using for loop, write and run a Python program to find factorial from 0 to 10

def factorial():
    fact = 1
    number = int(input("Enter any number "))
    for i in range(1,number + 1):
        fact = fact * i
    print(f"{fact}")

factorial()

