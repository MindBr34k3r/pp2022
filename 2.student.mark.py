# from courses import CourseInfo
# from mark import MarkInfo
# from students import StudentInfo
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CourseInfo:
    def __init__(self):
        self.num = 0
        self.courses = []

    def num_of_student(self):
        self.num = int(input("Input number of courses: "))
        return self.num

    def add_course_info(self):
        for i in range(self.num_of_student()):
            id = input("ID: ")
            name = input("Name: ")
            course = Course(id, name)
            self.courses.append(course)
        print(f"{self.num} courses has been added")
        return self.courses

    def show_course_info(self):
        print("{:3} | {:10} | {:20} ".format("No.", "ID", "Name"))
        for i in range(len(self.courses)):
            print("{:3} | {:10} | {:20} ".format(str(i + 1), self.courses[i].id, self.courses[i].name))


class Mark:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark


def select_a_course(courses):
    user_select = input("Input course id: ")
    for i in range(len(courses)):
        if user_select == courses[i].id:
            return courses[i]
    return "Nah"


class MarkInfo:
    def __init__(self):
        self.marks = {}

    def add_mark(self, courses, students):
        select_course = select_a_course(courses)
        if select_course == "Nah":
            print("There is no course like that!")
        else:
            mark_list = []
            n = 0
            for i in range(len(students)):
                mark = input(f"Student ID: {students[i].id} - Student Name: {students[i].name}\nInput mark: ")
                student_mark = Mark(students[i].id, students[i].name, mark)
                mark_list.append(student_mark)
                n = n + 1
            self.marks[select_course.id] = mark_list
            print(f"{n} students has been added")
            return self.marks

    def show_mark(self, courses, students):
        select_course = select_a_course(courses)
        course_mark = self.marks[select_course.id]
        if select_course == "Nah":
            print("There is no course like that!")
        else:
            print(f"{select_course.name} mark sheet")
            print("{:3} | {:10} | {:20} | {:10}".format("No.", "ID", "Name", "Mark"))
            for i in range(len(students)):
                print("{:3} | {:10} | {:20} | {:10} ".format(str(i + 1), course_mark[i].id, course_mark[i].name,
                                                             course_mark[i].mark))


class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob


class StudentInfo:
    def __init__(self):
        self.num = 0
        self.students = []

    def num_of_student(self):
        self.num = int(input("Input number of students: "))
        return self.num

    def add_student_info(self):
        for i in range(self.num_of_student()):
            id = input("ID: ")
            name = input("Name: ")
            dob = input("Date of Birth: ")
            student = Student(id, name, dob)
            self.students.append(student)
        print(f"{self.num} students has been added")
        return self.students

    def show_student_info(self):
        print("{:3} | {:10} | {:20} | {:20}".format("No.", "ID", "Name", "Date of Birth"))
        for i in range(len(self.students)):
            print("{:3} | {:10} | {:20} | {:20}".format(str(i + 1), self.students[i].id, self.students[i].name,
                                                        self.students[i].dob))


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
