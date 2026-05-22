# List data type in python

# Declaring and initializing list variables
fruits = ["apple", "banana", "mango",]
more_fruits = ["grapes", "persimmon", "melon"]

print(f"\n\nList Data Manipulation")
print(f"\nOriginal list: {fruits}")

# List methods for list manipulation

# Adding new data to the end of the list
fruits.append("apple")
print(f"\nList after appending data: {fruits}")

# Removing data from the list using values
fruits.remove("banana")
print(f"\nList after removing data: {fruits}")

# Joining two lists together
fruits.extend(more_fruits)
print(f"\nAfter joining another list to fruits: {fruits}")

# Inserting new data into a specific position in the list
fruits.insert(2, "lemon")
print(f"\nInserting new data to index 2 of the list: {fruits}")

# Counting the number of times a specific value appears in a list
num_of_apples = fruits.count("apple")
print(f"\nNumber of times 'apple' appears in the list: {num_of_apples}")

# Removing list data with index value
index_of_grapes = fruits.index("grapes")
fruits.pop(index_of_grapes)
print(f"\nRemoving data from list with their positional(index) value: {fruits}")

numbers = [2, 7, 1, 4, 3, 9, 5]
print(f"\n\nOriginal number list: {numbers}")

# Reversing the order of the list
reversed_numbers = numbers.reverse()
print(f"\nNumbers list, reversed: {reversed_numbers}")

# Sorting the list in ascending order
numbers.sort()
print(f"\nSorted Numbers list: {numbers}") # Sorts in ascending order by default

# Sorting the list in descending order
numbers.sort(reverse=True)
print(f"\nSorted Numbers list: {numbers}")

# Emptying lists
fruits.clear()
numbers.clear()
print(f"\n\nClearing the entire lists:")
print(f"\nFruits list: {fruits}")
print(f"\nNumbers list: {numbers}")
