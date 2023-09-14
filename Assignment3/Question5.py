# Q5.Define a function overlapping() that takes two lists and returns True if they
# have at least one member in common, False otherwise


def overlapping():
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,5]
    if set(list1) & set(list2):
        print("True")
    else:
        print("false")

overlapping()
    