
# - define student class -----------------------------------------------
class Student:
    def __init__(self, name, address, date_of_birth, course):
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.course = course

    def printName(self):
        print("Name :", self.name)
        print("Adrs :", self.address)
        print(25 * '-' )

    def printCourse(self):
        print("Course :", self.course)
        print(25 * '-' )

    def updateCourse(self):
        self.course = input(f"Enter new course for {self.name} : ")


# - Main Processing -----------------------------------------------------

# create a student object
Student1 = Student("Eric Idle", "99 Python Road", 19450329, "Comedy" )

# call method for updating Student course
Student1.updateCourse()

# call the methods defined for Student class
Student1.printName()
Student1.printCourse()
