
student = {
    'name': "Ziyuan Xue",
    'major': "Information Science",
    'favorite_food': "hot pot", 
    'favorite_color': "black",
    'grade': {'615': 4.0, '875':3.8, '611':3.5}
    }

def gpa(student):
    gpa = 0
    for v in student['grade'].values():
        gpa = gpa + v
    gpa = gpa/(len(student['grade']))
    return gpa

# print(student['grade'])

def print_student(student):
    print("The student's name is", student['name'])
    print("The student's major is", student['major'])
    print("The student's favorite food is", student['favorite_food'])
    print("The student's favorite color is", student['favorite_color'])
    print("The student's 615 grade is", student['grade']['615']) 
    print("The student's 875 grade is", student['grade']['875']) 
    print("The student's 611 grade is", student['grade']['611']) 
    gpa_student = gpa(student)
    print("The student's GPA is", gpa_student) 


print_student(student)


