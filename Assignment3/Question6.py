# Q6.Find and display the largest number of a list without using built-in function
# max(). Your program should ask the user to input values in list from keyboard

list = []

number = int(input("Enter any number : "))

for i in range(0, number + 1):
    new_data = int(input("Enter any number "))
    list.append(new_data)
    new_data.sort()

    print(f"Maximum number is {list[-1]}")