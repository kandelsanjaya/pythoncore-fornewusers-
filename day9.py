# Simple OOP Program for Beginners

class Student:

    # Class variable
    total_students = 0

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1

    # Instance method
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Static method
    @staticmethod
    def school_name():
        print("School Name: ABC School")

    # Class method
    @classmethod
    def show_total_students(cls):
        print("Total Students:", cls.total_students)


# Creating objects
student1 = Student("Ram", 18)
student2 = Student("Sita", 19)

# Calling instance method
student1.show_details()
print()

student2.show_details()
print()

# Calling static method
Student.school_name()
print()

# Calling class method
Student.show_total_students()