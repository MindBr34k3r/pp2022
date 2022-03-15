course_info = {}
student_info = {}
course_with_mark = {}
end = False


def input_course_info(info):
    num_of_course = input("Enter number of course : ")
    num = int(num_of_course)
    while num > 0:
        id = input("Enter course ID : ")
        if not is_exist(info, id):
            name = input("Enter course name : ")
            info[id] = [name]
            num = num - 1
        else:
            print(f"This id existed.")
    print(f"Add {num_of_course} courses success.")


def input_student_info(info):
    num_student = input("Input number of students: ")
    num = int(num_student)
    while num > 0:
        id = input("Input student's ID: ")
        if not is_exist(info, id):
            name = input("Input student's name: ")
            dob = input("Input student's date of birth (dd/mm/yyyy): ")
            info[id] = [name, dob]
            num = num - 1
        else:
            print(f"This id existed.")
    print(f"Add {num_student} students success.")


def list_student():
    print("{:10} | {:20} | {:20}".format("ID", "Name", "Date of Birth"))
    for key in student_info:
        print("{:10} | {:20} | {:20}".format(key, student_info[key][0], student_info[key][1]))


def list_course():
    print("{:10} | {:12}".format("ID", "Name"))
    for key in course_info:
        print("{:10} | {:12}".format(key, course_info[key][0]))


def list_course_with_mark():
    print("{:10} | {:20} | {:10}".format("ID", "Name", "Mark"))
    for key in course_with_mark:
        name = str(course_with_mark[key][0][0])
        mark = str(course_with_mark[key][0][1])
        print("{:10} | {:20} | {:10}".format(key, name, mark))


def add_mark_to_course(course_mark, student, course):
    input_course = input("Input a course's ID: ")
    for k_e_y in course:
        if k_e_y == input_course:
            course_mark[input_course] = []
            for key in student:
                student_mark = input(f"Student ID: {key} - Student Name: {student[key][0]}\nInput mark: ")
                course_mark[input_course].append([student[key][0], student_mark])
            break
        if k_e_y not in course:
            print(f"No {input_course} course exist!")


def is_empty(dictionary):
    if len(dictionary) == 0:
        return True
    return False


def is_exist(dictionary, id):
    if id in dictionary:
        return True
    return False


print("Welcome To Student Management Program!")
while not end:
    print("-----------menu----------")
    print("[1] Add Students")
    print("[2] Add Courses")
    print("[3] Show list of students")
    print("[4] Show list of courses")
    print("[5] Add student's marks to a course")
    print("[6] Show a course with marks")
    print("[0] Exit")
    choice = input("Please choose an option: ")
    if choice == "1":
        input_student_info(info=student_info)
    elif choice == "2":
        input_course_info(info=course_info)
    elif choice == "3":
        empty = is_empty(student_info)
        if not empty:
            list_student()
        else:
            print("There are no students in class!")
    elif choice == "4":
        empty = is_empty(course_info)
        if not empty:
            list_course()
        else:
            print("There are no courses!")
    elif choice == "5":
        add_mark_to_course(course_with_mark, student_info, course_info)
    elif choice == "6":
        empty = is_empty(course_with_mark)
        if not empty:
            list_course_with_mark()
        else:
            print("There are no courses have mark!")
    elif choice == "0":
        end = True
    else:
        print(f"{choice} is an invalid input!")
