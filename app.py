from mymodule.models import Student
from mymodule.math_utils import average_grade

def __main__():

    print(f"Student & Grades:")

    studentRoster = []

    studentRoster.append(Student("Imaya Karunanayake", 100))
    studentRoster.append(Student("Kim Ascona", 92))
    studentRoster.append(Student("Tiffany Daniel", 86))
    studentRoster.append(Student("Emma Hassall", 93))
    studentRoster.append(Student("Vicky Tavdy", 94))
    studentRoster.append(Student("Leila Anderson", 93))
    studentRoster.append(Student("Sam Adams", 98))
    studentRoster.append(Student("Michael Landon", 88))
    studentRoster.append(Student("Mathew Singh", 83))
    studentRoster.append(Student("Emilie Hryszko", 99))

    for i in studentRoster:
        i.print_student_info()

    print(f"\nThe average grade of the students were: {average_grade(studentRoster)}.")

__main__()
