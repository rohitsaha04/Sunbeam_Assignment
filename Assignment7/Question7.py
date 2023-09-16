# Q7.Write a Python function student_data () which will print the id of a student
# (student_id). If the user
# passes an argument student_name or student_class(use **kwargs) the function
# will print the
# student name and class.

def student_data(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


student_data(name="rohit", id=1)