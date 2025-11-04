class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []  # הכיתה רק מחזיקה רשימה של תלמידים קיימים

    def add_student(self, student):
        self.students.append(student)
