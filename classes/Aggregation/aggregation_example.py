from classes.Aggregation.classes.classRoom import Classroom
from classes.Aggregation.classes.student import Student

def start_aggregation_example():
    # תלמידים נוצרים מחוץ לכיתה
    s1 = Student("Avi")
    s2 = Student("Dana")

    classroom = Classroom("Python Class")
    classroom.add_student(s1)
    classroom.add_student(s2)

    print(f"{classroom.name} has {[s.name for s in classroom.students]}")
