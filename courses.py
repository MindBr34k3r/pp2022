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
            print("{:3} | {:10} | {:20} ".format(str(i+1), self.courses[i].id, self.courses[i].name))
