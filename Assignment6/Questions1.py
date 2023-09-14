# Question1. 1)Write a menu Driven Program To Calculate the Parameter and Area of
# different Shapes(Circle,Square,Rectangle) using functions
def calculate_parameter_rectangle():
    length = int(input("Enter length value : "))
    width = int(input("Enter width value : "))
    parameter = (length + width) * 2
    print(f"parameter of rectangle is {parameter}")


def calculate_parameter_square():
    size = int(input("Enter length value : "))
    parameter = size * 4
    print(f"parameter of squd is {parameter}")


def calculate_parameter():
    print("-" * 80)
    print("1.Rectangle")
    print("2.Square")
    print("-" * 80)
    # length = int(input("Enter length value : "))
    # width = int(input("Enter width value : "))
    # parameter = (length + width) * 2
    # print(f"parameter of rectangle is {parameter}")
    choice2 = int(input("enter for Rectangle or Square : "))
    if choice2 == 1:
        calculate_parameter_rectangle()
    else:
        calculate_parameter_square()


def calculate_area():
    print("inside calculate area")


def print_menu():
    print("-" * 80)
    print("1.calculate parameter")
    print("2.calculate area")
    print("-" * 80)

    choice = int(input("enter your choice: "))
    return choice


while True:
    ch = print_menu()

    if ch == 1:
        calculate_parameter()
    elif ch == 2:
        calculate_area()
    else:
        print("bye bye")
        break
