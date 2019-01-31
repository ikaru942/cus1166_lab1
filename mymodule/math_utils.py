from mymodule import models

def average_grade(studentRoster):

    average = 0

    for student in studentRoster:
        average += student.get_grade()

    return average/len(studentRoster)
