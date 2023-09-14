# 2)Write a program that accepts a list from user and print the alternate element
# of list.

# ditiss80422@gmail.com

list = []

number = int(input("Enter any number : "))

for i in range(0, number):
    new_data = int(input("Enter any number "))
    list.append(new_data)

    print(list[::2])

