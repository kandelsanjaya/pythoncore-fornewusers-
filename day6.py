# =========================================
# DICTIONARIES (dict) IN PYTHON
# =========================================
# A dictionary stores data in KEY : VALUE pairs.
# Example:
# "name" is the key
# "Sanjaya Kandel" is the value

# =========================================
# CREATING A DICTIONARY
# =========================================

student = {
    "name": "Sanjaya Kandel",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.8
}

# student dictionary contains:
# key -> value
# name -> Sanjaya Kandel
# age -> 21
# major -> Computer Science
# gpa -> 3.8


# =========================================
# ACCESSING VALUES
# =========================================
# We use square brackets [] with the key
# to get the value from the dictionary.

print(student["name"])   
# Output: Sanjaya Kandel

print(student["age"])    
# Output: 21

print(student["major"])  
# Output: Computer Science

print(student["gpa"])    
# Output: 3.8


# =========================================
# get() METHOD
# =========================================
# get() is another way to access values.
# It is safer than [] because it does not
# give an error if the key is missing.

print(student.get("name"))
# Output: Sanjaya Kandel

print(student.get("age"))
# Output: 21

# If the key does not exist:
print(student.get("address"))
# Output: None


# =========================================
# dict() FUNCTION
# =========================================
# dict() creates a dictionary using key=value format.

coordinate = dict(x=10, y=29)

print(coordinate)
# Output: {'x': 10, 'y': 29}


# =========================================
# LIST OF TUPLES TO DICTIONARY
# =========================================
# A tuple is written using ()
# A list is written using []
# dict() can convert list of tuples into dictionary.

student_and_courses = [
    ("cs101", 45),
    ("Math102", 40),
    ("Econ201", 35),
    ("Stat104", 50)
]

enrollment = dict(student_and_courses)

print(enrollment)

# Output:
# {
#   'cs101': 45,
#   'Math102': 40,
#   'Econ201': 35,
#   'Stat104': 50
# }


# =========================================
# CHECKING KEYS IN DICTIONARY
# =========================================
# "in" checks if a key exists.

grades = {
    "Ram": 85,
    "Hari": 70,
    "Chandra": 90
}

if "Ram" in grades:
    print("Ram is present in the dictionary")

# Output:
# Ram is present in the dictionary


# =========================================
# values() FUNCTION
# =========================================
# values() returns all values in the dictionary.

print(grades.values())

# Output:
# dict_values([85, 70, 90])


# =========================================
# CHECKING VALUES
# =========================================
# We can check if a value exists.

if 85 in grades.values():
    print("Found")
else:
    print("Not Found")

# Output:
# Found


# =========================================
# NESTED DICTIONARY
# =========================================
# A dictionary inside another dictionary
# is called a nested dictionary.

Catalog = {

    "cs101": {
        "title": "Computer Systems",
        "credits": 5,
        "students": ["Ram", "Hari", "Chandra"]
    },

    "cs102": {
        "title": "Data Structures",
        "credits": 7,
        "students": ["Shyam", "Dev", "Chandra"]
    }
}


# =========================================
# ACCESSING NESTED DICTIONARY
# =========================================

print(Catalog["cs101"])

# Output:
# {
#   'title': 'Computer Systems',
#   'credits': 5,
#   'students': ['Ram', 'Hari', 'Chandra']
# }


print(Catalog["cs102"]["title"])

# Output:
# Data Structures


print(Catalog["cs101"]["credits"])

# Output:
# 5


# =========================================
# keys() FUNCTION
# =========================================
# keys() returns all keys in the dictionary.

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'major', 'gpa'])


# =========================================
# items() FUNCTION
# =========================================
# items() returns both keys and values.

print(student.items())

# Output:
# dict_items([
#   ('name', 'Sanjaya Kandel'),
#   ('age', 21),
#   ('major', 'Computer Science'),
#   ('gpa', 3.8)
# ])


# =========================================
# LOOPING THROUGH A DICTIONARY
# =========================================
# items() helps us loop through keys and values.

for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Sanjaya Kandel
# age : 21
# major : Computer Science
# gpa : 3.8


# =========================================
# ADDING NEW VALUES
# =========================================
# We can add new key-value pairs.

student["address"] = "Nepal"

print(student)

# Output now includes:
# 'address': 'Nepal'


# =========================================
# UPDATING VALUES
# =========================================
# We can change existing values.

student["gpa"] = 4.0

print(student["gpa"])

# Output:
# 4.0


# =========================================
# REMOVING VALUES
# =========================================
# pop() removes a key and returns its value.

removed = student.pop("address")

print(removed)
# Output:
# Nepal


# =========================================
# SUMMARY
# =========================================
# Dictionary Functions:
#
# []          -> access values
# get()       -> safely get value
# dict()      -> create dictionary
# keys()      -> get all keys
# values()    -> get all values
# items()     -> get keys and values
# pop()       -> remove item
# update()    -> update dictionary
#
# Dictionaries are:
# - Fast
# - Easy to organize data
# - Very useful in Python
