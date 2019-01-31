from mymodule.models import Student

def __main__():
    roster = []

    roster.append(Student("Imaya", 99))
    roster.append(Student("Kim", 92))
    roster.append(Student("Tiffany", 86))
    roster.append(Student("Sal", 93))
    roster.append(Student("Andrew", 94))
    roster.append(Student("Manjit", 93))
    roster.append(Student("Mo", 105))
    roster.append(Student("Brenden", 88))
    roster.append(Student("Richard", 83))
    roster.append(Student("Kurtis", 100))
    
    for i in roster:
        i.print_student_info()
__main__()
