# Check if a number is prime
def is_prime(num):
    count = 0
    for i in  range(1, num):
        if num % i == 0:
            count += 1
    if count > 1:
        return False
    return True

result = is_prime(23)
if result is True:
    print(f"Number is prime")
else:
    print(f"Number is not prime")



# Factorial using loop
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result *i
    return result

fact = factorial(4)
print(f"Factorial: {fact}\n")



# Fibonacci series up to x terms
def fibonacci(n):
    a = 1
    b = 1
    print(f"{a} {b}", end=" ")
    for i in range(n-2):
        c = a + b
        print(c, end=" ")
        a,b = b,c
print(f"Fibonacci series of 10 terms: ", end=" ")
fibonacci(n=10)
print("\n")


# Check a string for uppercase letters and construct a string that contains only the uppercase letters
def uppercase(s):
    result = ""
    for char in s:
        if char >= 'A' and char <='Z':
            result = result + char
    return result

string = "LICT Django Class"
uppercase_string = uppercase(string)
print(f"Uppercase letters: {uppercase_string}\n")



# Construct a list of even and odd numbers from a given list of numbers
def even_odd_list(numbers: list):
    length_of_list  = len(numbers)
    even_numbers = []
    odd_numbers = []

    for i in range(length_of_list):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])
    
    return even_numbers, odd_numbers

numbers = list(range(1,21))
even_numbers_list, odd_numbers_list = even_odd_list(numbers)
print(f"Even Numbers List: {even_numbers_list}")
print(f"Odd Numbers List: {odd_numbers_list}\n")



# Search for a target value in a list (Linear Search)
def search(numbers, target):
    length_of_list = len(numbers)
    for i in range(length_of_list):
        print(f"Checking index {i} with value: {numbers[i]} ...")
        if numbers[i] == target:
            return i
    return -1

def main():
    numbers = [3, 5, 9, 12, 17, 2, 1, 6, 8, 4]
    target = 4
    result = search(numbers, target)
    if result != -1:
        print(f"Target ({target}) found in list at index {result}\n")
    else:
        print("Target not found in the list.")
main()



# Sum of digits of an at-least 2 digit number
def sum_of_digits(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result + remainder
        number = number // 10
    return result

number = 67
result = sum_of_digits(number)
print(f"The sum of digits of number {number} is: {result}\n")



# Manually reverse a string
def reverse(word):
    length_of_string = len(word)
    reversed_string = ""
    for i in range(length_of_string - 1, -1, -1):
        reversed_string += word[i]
    return reversed_string

word = "reverse"
print(f"The reverse of {word} is: {reverse(word)}\n")



# Calculate sum, average, maximum and minimum of a list of numbers
def calculate(numbers):
    total = 0
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        total += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
    average = total / len(numbers)
    
    return total, average, maximum, minimum

numbers = [1, 2, 3, 4, 5]
total, average, maximum, minimum = calculate(numbers)
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}\n")