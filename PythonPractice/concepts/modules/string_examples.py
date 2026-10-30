# string module
# The string module provides useful constants and a few helper classes for text.
# Most everyday string work is done with built-in str methods, but this module is handy for character sets
# (for example, when generating passwords) and for safe text templates.

import string

# Built-in character sets
# These are constant strings you can loop over or check membership against.
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)     # both lowercase and uppercase letters
print(string.digits)            # 0123456789
print(string.punctuation)       # symbols such as !, ?, #, and @
print(string.whitespace)        # space, tab, newline, and other blank characters

# Checking whether a character belongs to a set
# "in" tests membership. This works because each constant is just a string of characters.
letter = "g"
print(letter in string.ascii_lowercase)   # True

# Building a random password from the character sets
# random.choice() is used here for demo purposes. For real passwords, use the secrets module.
import random
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(12))   # "".join() glues the pieces together
print("Demo password:", password)

# Template strings
# Template uses $name placeholders, which is safer than f-strings when the template comes from users.
# substitute() raises an error if a placeholder has no matching value, so missing data is caught early.
from string import Template

greeting = Template("Hello, $name! You have $count new messages.")
print(greeting.substitute(name="Alice", count=3))

# safe_substitute() leaves unknown placeholders as they are, instead of raising an error.
print(greeting.safe_substitute(name="Bob"))   # "$count" stays in the output

# capwords()
# capwords() capitalizes the first letter of each word and lowercases the rest.
# It is similar to str.title(), but it handles extra spaces more cleanly.
print(string.capwords("python  MODULES are fun"))   # Python Modules Are Fun

# Formatter
# Formatter is the engine behind str.format(). You rarely need it, but it shows how formatting works.
from string import Formatter

formatter = Formatter()
print(formatter.format("{0} plus {1} is {2}", 2, 3, 5))
