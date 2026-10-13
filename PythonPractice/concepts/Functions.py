# Functions in Python
# A function is a reusable block of code that performs a specific task.
# It helps organize programs and avoid repeating the same logic.

# Defining a function.
def greet():
    print("Hello, welcome to Python programming!")

# Calling the function.
greet()

# Function with parameters.
# Parameters are variables defined in the function.
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

# Arguments are the actual values passed when calling the function.
greet_user("Alice")
greet_user("Bob")

# Returning values from a function.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The sum is: {result}")

# Variable scope in functions.
# Variables created inside a function are local variables.
# They can only be used inside that function.
length = 5  # This is a global variable.

def calculate_area():
    width = 3  # This is a local variable.
    return length * width

print(calculate_area())
print(length)

# Important concept:
# - Global variables can be used inside functions if not shadowed by local variables.
# - Local variables cannot be used outside the function.
# - We often define functions to keep programs modular and readable.
