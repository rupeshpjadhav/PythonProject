# Module Demo in Python
# A module is a Python file that contains reusable code.
# Python includes many built-in modules, and we can also install third-party modules.
# Importing modules helps us use ready-made functionality without writing everything ourselves.

# Example built-in modules (commented out here for reference):
# import math
# print(math.sqrt(16))
# print(math.factorial(5))
# print(math.pi)
#
# import random
# print(random.randint(1, 100))
# print(random.choice(['apple', 'banana', 'cherry']))

# datetime module is used to work with dates and time.
import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# %Y: full year (for example, 2025)
# %m: month number (for example, 01)
# %d: day of the month
# %H: hour in 24-hour format
# %M: minutes
# %S: seconds

# requests is a third-party module used to make HTTP requests.
# Install it if needed with: pip install requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# Why modules are useful:
# - They organize code into reusable pieces.
# - They reduce duplication.
# - They allow code to be shared across projects.
# - They let us use libraries written by others.

