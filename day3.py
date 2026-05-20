# ==========================================
# Prime Number Check
# ==========================================

def is_prime(num: int) -> bool:
    """
    Check whether a number is prime or not.
    Returns True if prime, otherwise False.
    """

    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Example
number = 7

if is_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is NOT a Prime Number")


# ==========================================
# Factorial of a Number
# ==========================================

def factorial(num: int) -> int:
    """
    Calculate factorial of a number.
    Example: 5! = 5 × 4 × 3 × 2 × 1
    """

    result = 1

    for i in range(1, num + 1):
        result *= i

    return result


# Example
fact = factorial(5)
print(f"\nFactorial of 5 is: {fact}")


# ==========================================
# Fibonacci Series
# ==========================================

def fibonacci(n: int):
    """
    Print Fibonacci series up to n terms.
    """

    a, b = 1, 1

    print("\nFibonacci Series:")

    # Print first two numbers
    print(a, b, end=" ")

    # Generate remaining terms
    for _ in range(n - 2):
        c = a + b
        print(c, end=" ")

        a, b = b, c


# Example
fibonacci(10)


# ==========================================
# Extract Uppercase Letters from a String
# ==========================================

def extract_uppercase(word: str) -> str:
    """
    Extract all uppercase letters from a string.
    """

    uppercase_string = ""

    for char in word:
        if char.isupper():
            uppercase_string += char

    return uppercase_string


# Example
word = "This Is A Sample String With Uppercase Letters"

result = extract_uppercase(word)

print(f"\n\nUppercase letters in the string: {result}")



# ============================================
# Python Set and List Operations Examples
# ============================================


# --------------------------------------------
# Remove duplicates from a list (Method 1)
# --------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def no_duplicate_list(numbers: list):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    print("Original List:")
    print(numbers)

    print("\nList Without Duplicates:")
    print(new_list)


no_duplicate_list(numbers)


# --------------------------------------------
# Remove duplicates using set (Method 2)
# --------------------------------------------

def no_duplicate_set(numbers: list):
    new_set = set(numbers)

    print("\nUnique Values Using Set:")
    print(new_set)


no_duplicate_set(numbers)


# --------------------------------------------
# Accessing elements from a set
# --------------------------------------------

fruits = {"apple", "banana", "cherry", "mango"}

fruit_list = list(fruits)

print("\nAccessing Set Elements:")

print(fruit_list[0])
print(fruit_list[1])
print(fruit_list[2])
print(fruit_list[3])


# --------------------------------------------
# Check membership in a shopping list
# --------------------------------------------

shopping_list = {"apple", "banana", "grapes"}

print("\nShopping List Check:")

for fruit in fruits:
    if fruit in shopping_list:
        print(f"{fruit} is in the shopping list")
    else:
        print(f"{fruit} is NOT in the shopping list")


# --------------------------------------------
# Set Difference Operation
# --------------------------------------------

yesterday_stock = {"pant", "shirt", "shoes", "hat"}
today_stock = {"pant", "shirt", "socks", "bags"}

sold_out = yesterday_stock - today_stock

print("\nSold Out Items:")
print(sold_out)


# --------------------------------------------
# Set Intersection Operation
# --------------------------------------------

students = {"alice", "bob", "charlie", "david"}
captains = {"bob", "charlie"}

student_captain = students.intersection(captains)

print("\nStudent Captains:")
print(student_captain)


# --------------------------------------------
# Common Set Operations
# --------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print("\nSet Operations:")

# Union
print("Union:", a | b)

# Intersection
print("Intersection:", a & b)

# Difference
print("Difference (a - b):", a - b)

# Symmetric Difference
print("Symmetric Difference:", a ^ b)