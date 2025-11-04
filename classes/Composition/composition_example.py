from classes.Composition.classes.classRoom import Classroom

def start_composition_example():

    classroom = Classroom("Python Class", ["Avi", "Dana"])
    print(f"{classroom.name} has {[s.name for s in classroom.students]}")
