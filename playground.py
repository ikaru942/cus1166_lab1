
print("Imaya Karunanayake - CUS1166")

print("\nPracticing: Basic Program\n")

print("Software Engineering Class CUS1166")
# Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("\nWelcome to CUS1166 " + str(myname))
# Alternative way to format a string
print("Glad you signed up for CUS1166 %s" % myname)

print("\nDone practicing basic program")



print("\n\n\nPracticing: Variables\n")
numStudent = 30
print(f"The variable numStudent has the value {numStudent}.")
decimalNum = 12.023
print(f"The variable decimalNum has the value {decimalNum} and its type is {type(decimalNum)}")
t = True
print(f"The variable t has the value {t}")
na = None
print(f"The variable na has the value of {na}")

# tuple
abc = (100,95,90)
print(f"\nabc[0] has the value {abc[0]} and is of type: {type(abc)}")

# list
studentList = ["Anna", "Tom", "John"]
studentList = [100,99,98]
print(f"\nstudentList[0] has the value {studentList[0]} and is of type: {type(studentList)}")

# Sets variables
sampleSet = set()
sampleSet.add(10)
sampleSet.add(11)
sampleSet.add(12)
print(sampleSet)

# Dictionary
grades = {"Imaya Karunanayake" : "A", "Sakeena Zaidi": "A-"}
grades["Imaya Karunanayake"]
grades["Adrian"] = "D"

# Create an empty dictionary .
mydictionary = dict()

print("\nDone practicing variables")



print("\n\n\nPracticing: Conditionals\n")

num = 8
if (num > 0):
    print("The number num is positive.")
elif (num < 0):
    print("The number num is negative.")
else:
    print("The number num is zero.")

print("\nDone practicing Conditionals")



print("\n\n\nPracticing: Loops\n")

for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}")

print("\nDone practicing Loops")



print("\n\n\nPracticing: Functions\n")

x = 10

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

x = 5

def square_num(x):
    return x*x

print(f"Is the number 10 even? {is_even(x)}")
print(f"The number 5 squared is {square_num(x)}.")

print("\nDone practicing Functions")



print("\n\n\nPracticing: Classes\n")

class Book:
    def __init__(self, title="Introduction to Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)

myBook = []

myBook.append(Book("Software Engineering Textbook", "567456"))
myBook.append(Book("Intro to Data StructuresT Textbook", "323546"))
myBook.append(Book("Advanced Data Structures Textbook", "757453"))
myBook.append(Book("Natural Language Processing Textbook", "23464546"))
myBook.append(Book("Systems Analysis Textbook", "7853134"))

for i in myBook:
    i.printBook()

print("\nDone practicing Classes")



print("\n\n\nPracticing: Use a module\n")

from mymodule.helper_utils import square

print(square(100))
print(square(81))
print(square(64))

print("\nDone practicing using a module")
