#Tuples 
#Tuples are immutable, ordered collections of elements. They are defined using parentheses
#  () and can contain elements of different data types. Once a tuple is created, its elements 
# cannot be modified.


#creating a tuple 


from itertools import count


my_tuple =(1, "Hello", 3.14, True )
print(my_tuple)
#Accessing elements in a tuple 
print(my_tuple[0])#output 1
print(my_tuple[1])#output Hello
print(my_tuple[2])#output 3.14
print(my_tuple[3])#output True 
#Tuples are immutable, so we cannot change their elements after creation 
#my_tuple[0]=10 #This will raise a TypeError because tuples are immutable 
print(my_tuple)
length= len(my_tuple)
print(length)  #output 4 
if "Hello"in my_tuple :
    print("Hello in the tuple ")
else:
    print("Hello is not in the tuple ")



# Tuple unpacking
lst= list(my_tuple)
lst.append("mango")
my_tuple=tuple(lst)
print(lst)

#tuple unpacking

fruits =("apple" ,"banana", "cherry", "mango" )
(red,  yellow, green, purple )=fruits
print(red)#output apple 
print(yellow)#output banana
print(green)#output cherry
print(purple)#output mango






student= ( "john", 21, "computer science ")
(name, age , major )=student 
print(name )
print(age)
print(major)



# new 

fruits =("apple" ,"banana", "cherry", "mango" )
(green,red, yelloe, purple)=fruits 
print(green)
print(red)
print(yellow)







#tuple methods 
#count()
fruits =("apple" ,"banana", "cherry", "mango","apple","apple","apple","apple" )
(green, red, yellow, *purple)=fruits 
# print(green)
# print(red)
# print(yellow)
x=fruits.count("apple")
print(x)

#index()
y=fruits.index("cherry")
print(y)







#programms 



#Extract unique values from a list 

Wifi_Users_logins=["john", "alice", "bob", "hari", "ram", "shyam"]
unique_user=(set(Wifi_Users_logins))
for user in unique_user:
    unique_user.add(user)
    print(user)

#filtering unique values 
banned_words=["copy", "paste", "spam", "scam", "fraud", "complete"]
sentence=" This is a complete sentence eithout any copy or paste or spam or scam or fraud or complete "
sentence_words=sentence.split(" ")# output for split ['', 'This', 'is', 'a', 'complete', 'sentence', 'eithout', 'any', 'copy', 'or', 'paste', 'or', 'spam', 'or', 'scam', 'or', 'fraud', 'or', 'complete', '']
print(sentence_words)

clean_words=[]
for word in sentence_words:
    if word not in banned_words:
        clean_words.append(word)#output for clean_words ['', 'This', 'is', 'a', 'sentence', 'eithout', 'any', 'or', 'or', 'or', 'or', 'or', '']
print(clean_words)


# Password Strength Checker

def password_strength(password):

    strength = 0

    # Check password length
    if len(password) >= 8:
        strength += 1

    # Check uppercase letters
    if any(char.isupper() for char in password):
        strength += 1

    # Check lowercase letters
    if any(char.islower() for char in password):
        strength += 1

    # Check numbers
    if any(char.isdigit() for char in password):
        strength += 1

    # Check special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

    if any(char in special_characters for char in password):
        strength += 1

    # Final result
    if strength == 5:
        return "Strong Password"
    elif strength >= 3:
        return "Medium Password"
    else:
        return "Weak Password"


# User input
user_password = input("Enter your password: ")

# Check password strength
result = password_strength(user_password)

print("Password Strength:", result)

















