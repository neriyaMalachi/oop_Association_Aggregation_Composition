# 1 Association
class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} teaches {student.name}")

t1 = Teacher("Neriya")
s1 = Student("Avi")

t1.teach(s1)




# 2 Aggregation
class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []  # הכיתה רק מחזיקה רשימה של תלמידים קיימים

    def add_student(self, student):
        self.students.append(student)

# תלמידים נוצרים מחוץ לכיתה
s1 = Student("Avi")
s2 = Student("Dana")

classroom = Classroom("Python Class")
classroom.add_student(s1)
classroom.add_student(s2)

print(f"{classroom.name} has {[s.name for s in classroom.students]}")


# 3 Composition
class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, name, student_names):
        self.name = name
        # הכיתה יוצרת בעצמה את התלמידים שלה
        # ומהשזה אומר שכשאני אמחק את הכיתה כל התלמידים יעלמו
        self.students = [Student(n) for n in student_names]

# הכיתה יוצרת את התלמידים בפנים
classroom = Classroom("Python Class", ["Avi", "Dana"])

print(f"{classroom.name} has {[s.name for s in classroom.students]}")
