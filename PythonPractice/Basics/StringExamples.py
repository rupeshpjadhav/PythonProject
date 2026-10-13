print("Hello World")
# Strings are sequences of characters used to store and manipulate text.
# Python strings are immutable, which means once created, they cannot be changed directly.
# Methods like upper(), lower(), and replace() return a new string instead of modifying the original.

# A string can contain normal text, special characters, and escape sequences like \n.
# \n means newline, so it moves the text to the next line when printed.
str2 = "Keywords are reserved words in python.\n They cannot be used as variable names."
print(str2)

# A string is created using quotes and assigned to a variable.
str1 = "Keywords cannot be used as variable names."

# Reversing a string using slicing.
# str1[::-1] means: start from the end, move backward by 1, and take every character.
reversed_str1 = str1[::-1]
print("Original string:", str1)
print("Reversed string:", reversed_str1)

print("\n--- String Basic Functions Examples ---")

# .upper() converts every letter to uppercase.
print("Uppercase:", str1.upper())

# .lower() converts every letter to lowercase.
print("Lowercase:", str1.lower())

# .title() capitalizes the first letter of each word.
print("Title Case:", str1.title())

# .capitalize() makes only the first letter uppercase.
print("Capitalize:", str1.capitalize())

# .count() counts how many times a character or substring appears.
print("Count of 'a':", str1.count('a'))

# .find() returns the starting index of a substring, or -1 if not found.
print("Position of 'used':", str1.find('used'))

# .replace() creates a new string by replacing old text with new text.
print("Replace 'Keywords' with 'Identifiers':", str1.replace('Keywords', 'Identifiers'))

# .split() breaks a string into a list of words.
print("Split into words:", str1.split())

# .startswith() checks whether the string starts with a given value.
print("Starts with 'Keywords':", str1.startswith('Keywords'))

# .endswith() checks whether the string ends with a given value.
print("Ends with 'names.':", str1.endswith('names.'))

# .strip() removes spaces and newline characters from both ends.
str3 = "   Hello Python   "
print("Original with spaces:", repr(str3))
print("Stripped:", repr(str3.strip()))

# join() combines list elements into a single string using a separator.
words = ['Python', 'is', 'fun']
print("Join words:", ' '.join(words))

# isalpha(), isdigit(), and isalnum() check the type of characters in the string.
print("'Python'.isalpha():", 'Python'.isalpha())
print("'123'.isdigit():", '123'.isdigit())
print("'Python3'.isalnum():", 'Python3'.isalnum())

# len() returns the number of characters in a string.
print("Length of str1:", len(str1))

# Important concept: strings cannot be modified in place.
# Example: str1[0] = 'X' would raise a TypeError.
# To make a change, we assign the new value back to the variable.
print(str1)



