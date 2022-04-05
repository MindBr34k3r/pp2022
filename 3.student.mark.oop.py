import numpy as np
import math


students = {}
courses = {}
end = False


def is_empty(dictionary):
    if len(dictionary) == 0:
        return True
    return False


def is_exist(dictionary, id):
    if id in dictionary:
        return True
    return False


def input_student_num():
    num = int(input("Input number of students: "))
    return num


def input_student_info():
    num = input_student_num()
    for num in range(num):
        id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")
        mark = {}
        gpa = 0
        students[id] = [name, dob, mark, gpa]
    print(f"{num} students have been added.")


def input_course_num():
    num = int(input("Input number of courses: "))
    return num


def input_course_info():
    num = input_course_num()
    for num in range(num):
        id = input("ID: ")
        name = input("Name: ")
        credit = input("Credits: ")
        courses[id] = [name, credit]
    print(f"{num} courses have been added.")


def select_course():
    show_course_list()
    user_choice = input("Input course ID: ")
    if is_exist(courses, user_choice):
        return user_choice
    return "None"


def select_student():
    show_student_list()
    user_choice = input("Input student ID: ")
    if is_exist(students, user_choice):
        return user_choice
    return "None"


def input_mark():
    course_id = select_course()
    if course_id == "None":
        print("There is no course like that!")
    else:
        for id in students:
            enter_mark = math.floor(float(input(f"Student ID: {id} - Student Name: {students[id][0]}\nInput mark: ")))
            students[id][2] = {courses[course_id][1]: enter_mark}


def show_student_list():
    i = 1
    print("{:3} | {:10} | {:20} | {:20}".format("No.", "ID", "Name", "Date of Birth"))
    for id in students:
        name = students[id][0]
        dob = students[id][1]
        print("{:3} | {:10} | {:20} | {:20}".format(str(i), id, name, dob))
        i = i+1


def show_course_list():
    i = 1
    print("{:3} | {:10} | {:20} | {:10}".format("No.", "ID", "Name", "Credits"))
    for id in courses:
        name = courses[id][0]
        credit = courses[id][1]
        print("{:3} | {:10} | {:20} | {:10}".format(str(i), id, name, credit))
        i = i+1


def show_mark_list():
    i = 1
    course_id = select_course()
    course_name = courses[course_id][1]
    if course_id == "None":
        print("There is no course like that!")
    else:
        print(f"{course_name} mark sheet")
        print("{:3} | {:10} | {:20} | {:10}".format("No.", "ID", "Name", "Mark"))
        for id in students:
            name = students[id][0]
            mark = students[id][2][course_name]
            print("{:3} | {:10} | {:20} | {:10}".format(str(i), id, name, str(mark)))
            i = i+1


def calculate_gpa(student_id):
    total_credit = 0
    total_mark = 0
    for id in courses:
        total_credit = total_credit + courses[id][1]



def show_student_gpa():
    student_id = select_student()
    if student_id == "None":
        print()
    pass


print("Welcome To Student Management Program!")
while not end:
    print("-----------menu----------")
    print("[1] Add Students")
    print("[2] Add Courses")
    print("[3] Show list of students")
    print("[4] Show list of courses")
    print("[5] Add student's marks to a course")
    print("[6] Show a course with marks")
    print("[7] Show a student's average GPA")
    print("[0] Exit")
    choice = input("Please choose an option: ")
    if choice == "1":
        input_student_info()
    elif choice == "2":
        input_course_info()
    elif choice == "3":
        empty = is_empty(students)
        if not empty:
            show_student_list()
        else:
            print("There are no students in class!")
    elif choice == "4":
        empty = is_empty(courses)
        if not empty:
            show_course_list()
        else:
            print("There are no courses!")
    elif choice == "5":
        input_mark()
    elif choice == "6":
        empty = is_empty(students)
        if not empty:
            show_mark_list()
        else:
            print("There are no students in class!")
    elif choice == "7":
        empty = is_empty(students)
        if not empty:
            show_mark_list()
        else:
            print("There are no students in class!")
    elif choice == "0":
        end = True
    else:
        print(f"{choice} is an invalid input!")
