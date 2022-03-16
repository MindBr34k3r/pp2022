from courses import CourseInfo
from mark import MarkInfo
from students import StudentInfo

end = False
student_info = StudentInfo()
course_info = CourseInfo()
mark_info = MarkInfo()
students = []
courses = []

print("Welcome To Student Management Program!")
while not end:
    print("-----------menu----------")
    print("[1] Add Students")
    print("[2] Add Courses")
    print("[3] Show list of students")
    print("[4] Show list of courses")
    print("[5] Add student's marks to a course")
    print("[6] Show marks with a given course")
    print("[0] Exit")
    user_choice = input("Please choose an option: ")
    if user_choice == "1":
        students = student_info.add_student_info()
    elif user_choice == "2":
        courses = course_info.add_course_info()
    elif user_choice == "3":
        student_info.show_student_info()
    elif user_choice == "4":
        course_info.show_course_info()
    elif user_choice == "5":
        mark_info.add_mark(courses, students)
    elif user_choice == "6":
        mark_info.show_mark(courses, students)
    elif user_choice == "0":
        end = True
        print("Goodbye!")
    else:
        print(f"{user_choice} is an invalid input!")
