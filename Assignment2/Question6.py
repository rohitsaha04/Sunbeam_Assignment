# Questions 6)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules: 
 
# Average Grade 
# 90-100 A 
# 80-89 B 
# 70-79 C 
# 60-69 D 
# 0-59 F


def marks():
    
    maths = int(input("Enter Math Marks "))
    english = int(input("Enter Enlish Marks "))
    science = int(input("Enter Science Marks "))
    average_grade = maths + english + science / 3 
    if(average_grade >= 0 and average_grade <= 59):
        print(f"You get {average_grade} and Grade F")
    elif(average_grade >= 60 and average_grade <= 69):
        print(f"You get {average_grade} and Grade D")
    elif(average_grade >= 70 and average_grade <= 79):
        print(f"You get {average_grade} and Grade C")
    elif(average_grade >= 80 and average_grade <= 89):
        print(f"You get {average_grade} and Grade B")
    elif(average_grade >= 90 and average_grade <= 100):
        print(f"You get {average_grade} and Grade A")
    else:
        print(f"you get {average_grade}")


marks()

    

