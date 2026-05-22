# =========================================
# DATE AND TIME IN PYTHON
# =========================================

import datetime

# Current Date and Time
current_date = datetime.datetime.now()

print("Current Date and Time:", current_date)

# Current Year
print("Current Year:", current_date.year)

# Current Day Name
print("Today is:", current_date.strftime("%A"))

# Custom Date
custom_date = datetime.datetime(2020, 5, 17)

print("Custom Date:", custom_date)


# =========================================
# MINIMUM AND MAXIMUM NUMBER
# =========================================

smallest = min(5, 10, 3, 8)
largest = max(35, 18, 8, 15)

print("Smallest Number:", smallest)
print("Largest Number:", largest)


# =========================================
# MATH FUNCTIONS
# =========================================

import math

print("Square Root of 16 =", math.sqrt(16))

print("2 Power 5 =", math.pow(2, 5))


# =========================================
# FACTORIAL USING DICTIONARY (MEMORY)
# =========================================

cache = {}

def factorial(n):

    # Check if factorial already exists
    if n in cache:
        print("Factorial found in memory!")
        return cache[n]

    # Calculate factorial
    result = 1

    for i in range(1, n + 1):
        result = result * i

    # Store result in dictionary
    cache[n] = result

    return result


# User Input
number = int(input("\nEnter a number to find factorial: "))

fact = factorial(number)

print("Factorial of", number, "=", fact)

print("Stored Dictionary:", cache)


# =========================================
# INVERTING A DICTIONARY
# =========================================

def invert_dictionary(data):

    inverted = {}

    for key, value in data.items():
        inverted[value] = key

    return inverted


students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print("\nOriginal Dictionary:")
print(students)

print("\nInverted Dictionary:")
print(invert_dictionary(students))


# =========================================
# MERGING TWO DICTIONARIES
# =========================================

def merge_sales(day1, day2):

    total_sales = {}

    # Copy first dictionary
    for item, amount in day1.items():
        total_sales[item] = amount

    # Add second dictionary values
    for item, amount in day2.items():

        if item in total_sales:
            total_sales[item] += amount

        else:
            total_sales[item] = amount

    return total_sales


# Sales Data
day1_sales = {
    "Apple": 10,
    "Banana": 20,
    "Orange": 50
}

day2_sales = {
    "Apple": 70,
    "Orange": 30,
    "Grape": 40,
    "Kiwi": 25
}

print("\nDay 1 Sales:")
print(day1_sales)

print("\nDay 2 Sales:")
print(day2_sales)

print("\nMerged Total Sales:")
print(merge_sales(day1_sales, day2_sales))