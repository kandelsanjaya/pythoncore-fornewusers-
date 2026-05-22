# for loop
for i in range(5):                  # loop from 0 to 4
    print(f"{i}", end=" ")
print("\n")


for i in range(1, 10, 2):           # loop from 1 to 9 with a step of 2 (1, 3, 5, 7, 9)
    print(f"{i}", end=" ")
print("\n")                         # prints a newline after the loop is done


# for loops in strings
for char in "Hello":
    print(f"{char}", end=" ")       # prints each character in the string "Hello"
print("\n")


#for loop with break
for i in range(10):                  # loop from 0 to 9   
    if i == 5:
        break                        # exit the loop when i is 5
    print(f"{i}", end=" ")
print("\n")


# for loop with continue
for i in range(10):                  # loop from 0 to 9
    if i % 2 == 0:
        continue                     # skip the rest of the loop for even numbers
    print(f"{i}", end=" ")           # prints only odd numbers from 0 to 9
print("\n")


# while loop
count = 0
while count < 5:                     # loop until count is less than 5
    print(f"{count}", end=" ")
    count += 1                       # *important* to avoid infinite loop
print("\n")


# while loop with break
num = 0
while num < 10:                      # loop until num is less than 10    
    if num == 5:
        break                        # exit the loop when num is 5
    print(f"{num}", end=" ")
    num += 1
print("\n")


# while loop with continue
num = 0
while num < 10:                      # loop until num is less than 10
    if num % 2 == 0:
        num += 1
        continue                     # skip the rest of the loop for even numbers
    print(f"{num}", end=" ")         # prints only odd numbers from 0 to 9
    num += 1
print("\n")

