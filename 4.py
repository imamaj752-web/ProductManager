class Student:
    def __init__(self, name, course, id):
        self.name = name
        self.course = course
        self.id = id

    def info(self):
        return f"имя: {self.name}, курс: {self.course}"
"""Task2"""


class Student:
    def __init__(self, name, course, id):
        self.name, self.course, self.id = name, course, id

    def info(self): return f"имя: {self.name}, курс: {self.course}"


class School:
    def __init__(self, name):
        self.name, self.students = name, []

    def add_student(self, student):
        if any(s.id == student.id for s in self.students):
            print(f"студент (id:{student.id}) уже учиться.")
        else:
            self.students.append(student)

    def remove_student(self, id):
        if any(s.id == id for s in self.students):
            self.students = [s for s in self.students if s.id != id]
        else:
            print(f"студента (id:{id}) не нашел.")

    def list_students(self):
        print('\n'.join(f"{s.name} - {s.course}" for s in self.students))

    def students_by_course(self, course):
        return [s for s in self.students if s.course == course]

    def total_students(self):
        return len(self.students)