# INHERITANCE IN PYTHON

# Parent class
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(self.name, "has logged in.")

    def info(self):
        print("Name:", self.name)
        print("Email:", self.email)


# Child class 1
class Student(User):

    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Student ID:", self.student_id)


# Child class 2
class Teacher(User):

    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Subject:", self.subject)


# Object of parent class
u = User("Ram", "ram@gmail.com")

# Object of student class
s = Student("Sita", "sita@gmail.com", "101")

# Object of teacher class
t = Teacher("Hari", "hari@gmail.com", "Math")


# Calling methods
u.info()
u.login()

print()

s.info()
s.login()

print()

t.info()
t.login()


#super() function is used to call the parent class's method from the child class. It allows us to access the methods and properties of the parent class in the child class, even if they have been overridden. In the above code, we used super() to call the __init__ method of the User class from both the Student and Teacher classes to initialize the name and email attributes.


# Parent class
class Parent:

    def __init__(self):
        self.parent_name = input("Enter parent name:")


# Child class
class Child(Parent):

    def __init__(self):
        # Calling parent constructor
        super().__init__()

        self.child_name = input("Enter child name:")


# Objects
p = Parent()
c = Child()


# Output
print(p.parent_name)
print(c.parent_name)
print(c.child_name)

# Parent class
class Parent:

    def fun(self):
        print("Parent function called")


# Child1 class
class Child1(Parent):

    def fun(self):
        print("Child1 function called")


# Child2 class
class Child2(Parent):

    def fun(self):
        super().fun()
        print("Child2 function called")


# Multiple inheritance
class Child3(Child1, Child2):

    def fun(self):
        super().fun()
        print("Child3 function called")


# Object
c3 = Child3()

# Calling function
c3.fun()

# MRO
print(Child3.__mro__)


     












