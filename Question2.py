# Question2.Display following menu and write required function for it
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times


def display_char_for_even():
    character = input("Enter any name : ")
    even_character = []

    for i in range(len(character)):
        if i % 2 != 0:
            even_character.append(character[i])
    print(f"even characters is {even_character}")


def display_char_for_odd():
    character = input("Enter any name : ")
    odd_character = []

    for i in range(len(character)):
        if i % 2 == 0:
            odd_character.append(character[i])
    print(f"odd character is {odd_character}")


def display_len_string():
    character = input("Enter any name : ")
    len_char = len(character)
    print(f"length of string is {len_char}")


def add_a_at_end():
    character = input("Enter any name : ")
    add_char = character + "a" * len(character)
    print(add_char)


def print_menu():
    print("-" * 80)
    print("1.Display characters from even position")
    print("2. Display characters from odd position")
    print("3. Display length of a string")
    print("4. Add a at the end of string length times")
    print("-" * 80)

    choice = int(input("enter your choice: "))
    return choice


while True:
    ch = print_menu()

    if ch == 1:
        display_char_for_even()
    elif ch == 2:
        display_char_for_odd()
    elif ch == 3:
        display_len_string()
    elif ch == 4:
        add_a_at_end()
    else:
        print("bye bye")
        break
