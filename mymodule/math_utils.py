from mymodule import models

def average_grade(roster):
    average = 0
    for student in len(roster):
        average += student.get_grade()
    return average
