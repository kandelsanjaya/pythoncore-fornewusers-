# ---------- DAY 2 PYTHON PRACTICE ----------

# ---------- 1. EVEN OR ODD NUMBER ----------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even Number")
else:
    print(num, "is an Odd Number")


# ---------- 2. POSITIVE, NEGATIVE OR ZERO ----------

num = int(input("\nEnter another number: "))

if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print("The number is Zero")


# ---------- 3. CHECK DAY OF WEEK USING MATCH CASE ----------

day = input("\nEnter a day of the week: ")

match day.lower():

    case "sunday":
        print("Today is Sunday")

    case "monday":
        print("Today is Monday")

    case "tuesday":
        print("Today is Tuesday")

    case "wednesday":
        print("Today is Wednesday")

    case "thursday":
        print("Today is Thursday")

    case "friday":
        print("Today is Friday")

    case "saturday":
        print("Today is Saturday")

    case _:
        print("Invalid Day")


# ---------- 4. LOOPS ----------

print("\nEven numbers from 1 to 20:")

for i in range(1, 21):

    if i % 2 == 0:
        print(i, end=" ")


# ---------- 5. SIMPLE PASSWORD CHECKER ----------

password = input("\n\nEnter your password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")


# ---------- 6. SIMPLE CALCULATOR ----------

print("\n\nSimple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":

    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Choice")