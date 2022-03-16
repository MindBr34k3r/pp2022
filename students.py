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
            print("{:3} | {:10} | {:20} | {:20}".format(str(i+1), self.students[i].id, self.students[i].name, self.students[i].dob))
