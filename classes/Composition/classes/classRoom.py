from classes.Composition.classes.student import Student


class Classroom:
    def __init__(self, name, student_names):
        self.name = name
        # הכיתה יוצרת בעצמה את התלמידים שלה
        # ומהשזה אומר שכשאני אמחק את הכיתה כל התלמידים יעלמו
        self.students = [Student(n) for n in student_names]
