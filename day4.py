# ---------- REMOVE DUPLICATES FROM A LIST ----------

numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

# Method 1 : Using Loop

def no_duplicate_list(numbers):

    new_list = []

    for num in numbers:

        if num not in new_list:
            new_list.append(num)

    print("Original List:", numbers)
    print("Without Duplicates:", new_list)

no_duplicate_list(numbers)


# ---------- METHOD 2 : USING SET ----------

def unique_values(numbers):

    new_set = set(numbers)

    print("\nUnique Values using Set:")
    print(new_set)

unique_values(numbers)


# ---------- ACCESSING SET VALUES ----------

fruits = {"apple", "banana", "cherry", "mango"}

fruit_list = list(fruits)

print("\nAccessing Set Elements:")

print(fruit_list[0])
print(fruit_list[1])
print(fruit_list[2])
print(fruit_list[3])


# ---------- CHECK ITEMS IN SHOPPING LIST ----------

shopping_list = {"apple", "banana", "cherry", "mango"}

print("\nShopping List Check:")

for fruit in fruits:

    if fruit in shopping_list:
        print(f"{fruit} is in the shopping list")

    else:
        print(f"{fruit} is NOT in the shopping list")


# ---------- SET DIFFERENCE ----------

yesterday_stock = {"pant", "shirt", "shoes", "hat"}

today_stock = {"pant", "shirt", "socks", "bags"}

sold_out = yesterday_stock - today_stock

print("\nSold Out Items:")
print(sold_out)


# ---------- SET INTERSECTION ----------

students = {"alice", "bob", "charlie", "david"}

captains = {"bob", "charlie"}

student_captain = students.intersection(captains)

print("\nStudent Captains:")
print(student_captain)