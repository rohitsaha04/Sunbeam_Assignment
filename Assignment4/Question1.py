# 1) Concatenate two lists in the following order by using list comprehension
# Input:- list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newlist = []
for item in list2 and list1:
    if "Hello" in item:
       newlist.append(item)
    elif "take" in item:
        newlist.append(item)

print(list1)
