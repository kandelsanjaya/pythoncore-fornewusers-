# str data type

# Declaring and initializing string variables

text = "Lumbini ICT Campus"
string_with_spaces = "  This string has spaces in the beginning and the end  "

# str methods for string manipulation
print(f"\n\nString Manipulation")

# Calculating length of a string
print(f"\nLength of string 'text': {len(text)}")

# Converting a string value to uppercase
print(f"\nString method 'upper()': {text.upper()}")

# Converting a string value to lowercase
print(f"\nString method 'lower()': {text.lower()}")

# Counting the number of times a specific character appears in a string
print(f"\nCount for the appearance of letter 'i' in text: {text.count('i')}") # does not count 'I'

# Finding the position of a specific character in a string
print(f"\nPosition of letter 'b' in text: {text.find('b')}") # index() method yeidls the same result to find() method

# Removing spaces from the beginning and the end of a string
print(f"\nString before removing spaces:{string_with_spaces}")
print(f"\nString after removing spaces: {string_with_spaces.strip()}")