# Question5.Write a Python program to count the number of characters (character
# frequency) in a string. Go to the editor
# Input:-
# Sample String : sunbeaminfo.com'
# Output:-
# {'s': 1, 'u': 1, 'n': 2, 'b': 1, 'e': 1, 'a': 1, 'm': 2, 'i': 1, 'f': 1, 'o': 2, '.': 1, 'c': 1}

user = "sunbeam.com"
all_character = {}
for i in user:
    if i in all_character:
        all_character[i] += 1
    else:
        all_character[i] = 1
print(all_character)
