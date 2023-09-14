# Q4.Write a program that prompts the user to input a year and determine whether the year is a leap year or 
# not. 
# Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100 is a leap y
# ear only if it is also evenly divisible by 400. Example : 
 
# 1992 Leap Year 
# 2000 Leap Year 
# 1900 NOT a Leap Year 
# 1995 NOT a Leap Year

def leap_year():
    user = int((input("Enter any number ")))
    if(user % 4 == 0 and user % 100 == 0 and user % 400 == 0):
        print("It is a leap year")
    else:
        print("It is not a leap year")

leap_year()

