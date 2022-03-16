class Mark:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark


class MarkInfo:
    def __init__(self):
        self.marks = {}

    def select_a_course(self, courses):
        user_select = input("Input course id: ")
        for i in range(len(courses)):
            if user_select == courses[i].id:
                return courses[i]
        return "Nah"

    def add_mark(self, courses, students):
        select_course = self.select_a_course(courses)
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
        select_course = self.select_a_course(courses)
        course_mark = self.marks[select_course.id]
        if select_course == "Nah":
            print("There is no course like that!")
        else:
            print(f"{select_course.name} mark sheet")
            print("{:3} | {:10} | {:20} | {:10}".format("No.", "ID", "Name", "Mark"))
            for i in range(len(students)):
                print("{:3} | {:10} | {:20} | {:10} ".format(str(i+1), course_mark[i].id, course_mark[i].name, course_mark[i].mark))
