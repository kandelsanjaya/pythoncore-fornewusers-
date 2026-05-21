# =========================================
# Updating Dictionary Records in Python
# =========================================

fruits = {
    "apple": 10,
    "banana": 20,
    "orange": 30,
    "grape": 40
}

# Updating values
fruits["apple"] = 15
fruits["banana"] = 25
fruits["orange"] = 10

# Adding new key-value pair
fruits["kiwi"] = 50

print(fruits)

# Output:
# {'apple': 15, 'banana': 25, 'orange': 10, 'grape': 40, 'kiwi': 50}


# =========================================
# Using update() method
# =========================================

fruits.update({
    "apple": 20,
    "banana": 45,
    "orange": 65,
    "grape": 75,
    "kiwi": 85
})

print(fruits)

# Output:
# {'apple': 20, 'banana': 45, 'orange': 65, 'grape': 75, 'kiwi': 85}


# =========================================
# Removing Dictionary Items using del
# =========================================

del fruits["kiwi"]

print(fruits)

# Output:
# {'apple': 20, 'banana': 45, 'orange': 65, 'grape': 75}


# =========================================
# Removing Dictionary Items using pop()
# =========================================

fruits.pop("grape")

print(fruits)

# Output:
# {'apple': 20, 'banana': 45, 'orange': 65}


# =========================================
# Overwriting Duplicate Keys
# =========================================

student = {
    "name": "Sanjaya Kandel",
    "age": 21,
    "address": "Baglung",
    "gpa": 3.8,
    "address": "Chitwan"   # Duplicate key
}

print(student)

# Output:
# {'name': 'Sanjaya Kandel', 'age': 21,
#  'address': 'Chitwan', 'gpa': 3.8}

# Note:
# The last value of a duplicate key is kept.


# =========================================
# Counting Letters using Dictionary
# =========================================

word = "Sanjaya Kandel"

count = {}

for letter in word:
    count[letter] = count.get(letter, 0) + 1

print(count)

# Output:
# {'S': 1, 'a': 4, 'n': 2, 'j': 1,
#  'y': 1, ' ': 1, 'K': 1,
#  'd': 1, 'e': 1, 'l': 1}


# =========================================
# Grouping Data using Dictionary
# =========================================

students = [
    ("Sanjaya Kandel", "Computer Science"),
    ("Ramesh Thapa", "Biology"),
    ("Sita Sharma", "Biology"),
    ("Harish Thapa", "Computer Science")
]

groups = {}

for name, course in students:
    groups.setdefault(course, []).append(name)

print(groups)

# Output:
# {
#   'Computer Science': ['Sanjaya Kandel', 'Harish Thapa'],
#   'Biology': ['Ramesh Thapa', 'Sita Sharma']
# }