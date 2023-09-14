# Q3.Write a Python program to count the elements in a list until an element is a 
# tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3

list = [10, 20, 30, (40,50), 60, 70]
counter = 0
for item in list:
    if type(item) is tuple:
        break
    counter = counter + 1
    print(counter)


    
