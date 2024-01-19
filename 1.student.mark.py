students = []
courses = []
marks= []

#number of students in a class
def input_number_of_students():
    number_of_students = int(input("Enter The number of student:"))
    return number_of_students

#student's information
def input_students_information():
    id = input("Enter the student's id:")
    name = input("Enter the student's name:")
    DoB = input("Enter the student's date of birth:")  
    students.append({"id": id, "name": name, "DoB": DoB})

#number of courses
def input_number_of_courses():
    number_of_courses = int(input("Enter The number of courses:"))
    return number_of_courses

#course's information
def input_courses_information():
    id = input("Enter the course's id:")
    name = input("Enter the course's name:")
    courses.append({"id": id, "name": name})


#Student mark
def input_student_mark():
    course_id = input("Enter the course's id:")
    student_id = input("Enter the student's id:")
    mark = input("Enter the student's mark:")
    marks.append({"course_id": course_id, "student_id": student_id, "mark": mark})

def  list_courses():
    for course in courses:
        print(course)

def list_students():
    for student in students:
        print(student)

def list_marks():
    for mark in marks:
        print(mark)

num_students = input_number_of_students()
for _ in range(num_students):
    input_students_information()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_courses_information()

num_marks = input_number_of_courses()
for _ in range(num_marks):
    input_student_mark()


print(students)
print(courses)
print(marks)
