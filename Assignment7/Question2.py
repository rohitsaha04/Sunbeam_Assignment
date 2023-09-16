# Question1.2)Write a Pandas program to add, subtract, multiple and divide two Pandas
# Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd



def add_pandas():
    number1 = [2, 4, 6, 8, 10]
    number2 = [1, 3, 5, 7, 9]

    result1 = pd.Series(number1)
    result2 = pd.Series(number2)
    print(f"addition is {result1 + result2}")


add_pandas()


def substract_pandas():
    number1 = [2, 4, 6, 8, 10]
    number2 = [1, 3, 5, 7, 9]

    result1 = pd.Series(number1)
    result2 = pd.Series(number2)
    print(f"substraction is {result1 - result2}")


substract_pandas()

def multiply_pandas():
    number1 = [2, 4, 6, 8, 10]
    number2 = [1, 3, 5, 7, 9]

    result1 = pd.Series(number1)
    result2 = pd.Series(number2)
    print(f"multiplication is {result1 * result2}")


multiply_pandas()

def division_pandas():
    number1 = [2, 4, 6, 8, 10]
    number2 = [1, 3, 5, 7, 9]

    result1 = pd.Series(number1)
    result2 = pd.Series(number2)
    print(f"division is {result1 / result2}")


division_pandas()




