# Control flow statements: if, elif, else, match-case

# if statement
x = 10  
if x > 5:
    print("x is greater than 5")


# if-else statement
y = 3
if y % 2 == 0:
    print(f"{y} is even")  
else:
    print(f"{y} is odd")


# if-elif-else statement
z = 15
if z < 10:
    print(f"{z} is less than 10")
elif z == 10:
    print(f"{z} is equal to 10")
else:
    print(f"{z} is greater than 10")


# match-case statement (Python 3.10+)
num = int(input("Enter a number: "))
match num:
    case 0:
        print( "Zero")
    case 1:
        print( "One")
    case 2:
        print( "Two")
    case _:                 # default case
        print( "Other number")