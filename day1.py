# ==========================================
# PYTHON COMPLETE BEGINNER EXAMPLE
# ==========================================

# ---------- 1. PRINT ----------
print("Welcome to Python Programming!")
print("--------------------------------")

# ---------- 2. VARIABLES & DATA TYPES ----------

# Integer
age = 21

# Float
height = 5.9

# String
name = "Sanjaya Kandel"

# Boolean
is_student = True

# List
fruits1 = ["Apple", "Banana", "Mango"]
fruits2 = ["Grapes", "Watermelon", "Peach"]

# Tuple
colors = ("Red", "Green", "Blue")

# Set
numbers_set = {1, 2, 3, 4}

# Dictionary
student = {
    "name": "Sanjaya Kandel",
    "age": 21,
    "grade": "BSc.CSIT"
}

# None Type
nothing = None

print("\n--- DATA TYPES ---")
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print(type(fruits1))
print(type(fruits2))
print(type(colors))
print(type(numbers_set))
print(type(student))
print(type(nothing))

# ---------- 3. USER INPUT ----------

print("\n--- USER INPUT ---")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello,", user_name)
print("You are", user_age, "years old.")

# ---------- 4. OPERATORS ----------

a = 10
b = 3

print("\n--- OPERATORS ---")

# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Comparison
print("a > b:", a > b)
print("a == b:", a == b)

# Logical
print("True and False:", True and False)

# ---------- 5. IF ELSE ----------

print("\n--- IF ELSE ---")

if user_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ---------- 6. LOOPS ----------

print("\n--- FOR LOOP ---")

for fruit in fruits1:
    print(fruit)

print("\n--- WHILE LOOP ---")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# ---------- 7. FUNCTIONS ----------

print("\n--- FUNCTIONS ---")

def add(x, y):
    return x + y

result = add(5, 7)

print("Addition Result:", result)

# ---------- 8. LIST METHODS ----------

print("\n--- LIST METHODS ---")

fruits1.append("Orange")
print(fruits1)

fruits1.remove("Banana")
print(fruits1)

fruits1.extend(fruits2)
print(fruits1)
fruits1.insert(1,"strawberry")
print(fruits1)










# ---------- 9. DICTIONARY ----------

print("\n--- DICTIONARY ---")

print(student["name"])

student["school"] = "ABC School"

print(student)

# ---------- 10. CLASSES & OBJECTS ----------

print("\n--- CLASSES & OBJECTS ---")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)

# Create object
my_car = Car("Toyota", "Corolla")

my_car.show_info()

# ---------- 11. EXCEPTION HANDLING ----------

print("\n--- EXCEPTION HANDLING ---")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a number.")

# ---------- 12. FILE HANDLING ----------

print("\n--- FILE HANDLING ---")

# Write file
file = open("sample.txt", "w")
file.write("Hello from Python file handling!")
file.close()

# Read file
file = open("sample.txt", "r")
content = file.read()
file.close()

print(content)

# ---------- 13. LAMBDA FUNCTION ----------

print("\n--- LAMBDA FUNCTION ---")

square = lambda x: x * x

print("Square of 5:", square(5))

# ---------- 14. LIST COMPREHENSION ----------

print("\n--- LIST COMPREHENSION ---")

squares = [x * x for x in range(1, 6)]

print(squares)


#if else else if statement 
num=int(input("emter a number :"))
if(num%2==0):
    print("even  number is ",num)
else:
    print("odd number is ",num)
    

















# ---------- 15. MODULE EXAMPLE ----------

import math

print("\n--- MATH MODULE ---")

print("Square root of 25:", math.sqrt(25))

# ---------- 16. FINAL MESSAGE ----------

print("\nProgram Finished Successfully!")