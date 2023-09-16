# Q8.Write a Python program to replace dictionary values(V,VI)and with their
# average.
# Input:-
# student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
# {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
# {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# Expected Output:
# [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5},
# {'subject': 'math', '
# id': 3, 'V+VI': 80.5}


def find_average(list_of_students):
    for d in list_of_students:
        s1 = d.pop('V')
        s2 = d.pop('VI')
        d['V+VI'] = (s1 + s2)/2
    return  list_of_students
student_details = [
{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(find_average(student_details))

